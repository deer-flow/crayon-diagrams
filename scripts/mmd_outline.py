#!/usr/bin/env python3
"""Extract a node/edge outline from a Mermaid flowchart or sequence diagram.

This is the "semantic layer" helper for crayon-diagrams: parse the source
diagram, then paste the outline into the prompt as an explicit graph contract.

Usage:
    python3 scripts/mmd_outline.py examples/message-gateway/source.mmd
    python3 scripts/mmd_outline.py examples/*/source.mmd --json

Supported subset: Mermaid flowchart (LR/TB/RL/BT), subgraphs, node shapes,
labelled and unlabelled arrows; sequenceDiagram participants, messages, notes.
Unknown lines are reported as warnings instead of failing silently.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

# Longest shapes first so [[..]] is not consumed by [..].
SHAPE = r"(?:\[\[.*?\]\]|\[\(.*?\)\]|\[/.*?/\]|\[.*?\]|\(\(.*?\)\)|\(.*?\)|\{.*?\}|>.*?\])"
NODE_DEF = re.compile(r"(?<![\w.-])([A-Za-z_][\w.]*)\s*(" + SHAPE + r")")
INLINE_NODE = re.compile(r"(?<![\w.-])([A-Za-z_][\w.]*)\s*" + SHAPE)
ARROW = r"(?P<arrow><==>|<-.->|<-->|==>|-->>|-\.->|-->|---|--[xo])"
# The target node is a lookahead so chained edges (A --> B --> C) are all found.
EDGE = re.compile(
    r"(?P<a>[A-Za-z_][\w.]*)\s*" + ARROW + r"\s*(?:\|(?P<label>[^|]+)\|\s*)?(?=(?P<b>[A-Za-z_][\w.]*))"
)
NAMED_EDGE = re.compile(r"(?P<a>[A-Za-z_][\w.]*)\s*--\s+(?P<label>[^->]+?)\s+-->\s+(?P<b>[A-Za-z_][\w.]*)")
SUBGRAPH = re.compile(r"^subgraph\s+([A-Za-z_][\w.]*)\s*\[(.*)\]$")
PARTICIPANT = re.compile(r"^(?:participant|actor)\s+([A-Za-z_][\w.]*)(?:\s+as\s+(.+))?$")
MESSAGE = re.compile(r"^([A-Za-z_][\w.]*)\s*(-->>|->>|-->|->)\s*([A-Za-z_][\w.]*)\s*:\s*(.+)$")
NOTE = re.compile(r"^Note\s+(?:over|left of|right of)\s+([^:]+):\s*(.+)$")


def clean_label(shape: str, node_id: str) -> str:
    label = shape.strip()
    for left, right in (("[[", "]]"), ("[(", ")]"), ("[/", "/]"), ("((", "))"), ("[", "]"), ("(", ")"), ("{", "}"), (">", "]")):
        if label.startswith(left) and label.endswith(right):
            label = label[len(left) : len(label) - len(right)]
            break
    label = label.strip().strip("\"'")
    if label.startswith(("(", "[")) and label.endswith((")", "]")):
        label = label[1:-1]
    return label or node_id


def add_node(nodes: dict[str, dict[str, str]], node_id: str, label: str, warnings: list[str]) -> None:
    if node_id in nodes:
        if nodes[node_id]["label"] != label and label != node_id:
            warnings.append(f"node {node_id!r} redefined: {nodes[node_id]['label']!r} -> {label!r}")
            nodes[node_id]["label"] = label
        return
    nodes[node_id] = {"id": node_id, "label": label}


def parse_flowchart(lines: list[str], direction: str) -> dict[str, Any]:
    nodes: dict[str, dict[str, str]] = {}
    edges: list[dict[str, str]] = []
    warnings: list[str] = []

    for raw in lines:
        line = raw.split("%%", 1)[0].strip()
        if not line:
            continue
        sub = SUBGRAPH.match(line)
        if sub:
            add_node(nodes, sub.group(1), sub.group(2).strip().strip("\"'"), warnings)
            continue
        if line in {"end"} or line.startswith(("classDef", "class ", "style ", "linkStyle", "click ")):
            continue

        # Register every inline node definition first.
        for match in NODE_DEF.finditer(line):
            add_node(nodes, match.group(1), clean_label(match.group(2), match.group(1)), warnings)

        # Reduce A[Label] --> B(Label) to A --> B for edge parsing.
        bare = INLINE_NODE.sub(r"\1", line)
        def take_named(match: re.Match[str]) -> str:
            edge = match.groupdict()
            edges.append(
                {"from": edge["a"], "to": edge["b"], "label": edge["label"].strip(), "arrow": "-->"}
            )
            return " " * len(match.group(0))

        had_named = NAMED_EDGE.search(bare) is not None
        bare = NAMED_EDGE.sub(take_named, bare)
        matches = list(EDGE.finditer(bare))
        for index, match in enumerate(matches):
            edge = match.groupdict()
            edges.append(
                {
                    "from": edge["a"],
                    "to": edge["b"],
                    "label": (edge["label"] or "").strip(),
                    "arrow": edge["arrow"],
                }
            )
            if index and matches[index - 1].group("b") != edge["a"]:
                warnings.append(f"possible unparsed chain near: {line!r}")

        if (
            not matches
            and not had_named
            and not NODE_DEF.search(line)
            and not line.startswith(("flowchart", "graph"))
        ):
            warnings.append(f"unparsed line: {line!r}")

    for edge in edges:
        for end in ("from", "to"):
            add_node(nodes, edge[end], edge[end], warnings)

    return {
        "type": "flowchart",
        "direction": direction,
        "nodes": list(nodes.values()),
        "edges": edges,
        "warnings": warnings,
    }


def parse_sequence(lines: list[str]) -> dict[str, Any]:
    participants: dict[str, dict[str, str]] = {}
    messages: list[dict[str, str]] = []
    notes: list[str] = []
    warnings: list[str] = []

    for raw in lines:
        line = raw.split("%%", 1)[0].strip()
        if not line or line.startswith("sequenceDiagram"):
            continue
        note = NOTE.match(line)
        if note:
            notes.append(f"{note.group(1).strip()}: {note.group(2).strip()}")
            continue
        participant = PARTICIPANT.match(line)
        if participant:
            pid, alias = participant.groups()
            participants[pid] = {"id": pid, "label": (alias or pid).strip()}
            continue
        message = MESSAGE.match(line)
        if message:
            a, arrow, b, text = message.groups()
            messages.append({"from": a, "to": b, "arrow": arrow, "label": text.strip()})
            for pid in (a, b):
                participants.setdefault(pid, {"id": pid, "label": pid})
            continue
        warnings.append(f"unparsed line: {line!r}")

    return {
        "type": "sequence",
        "direction": "",
        "participants": list(participants.values()),
        "messages": messages,
        "notes": notes,
        "warnings": warnings,
    }


def parse(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    lines = [line for line in text.splitlines() if line.strip() and not line.strip().startswith("%%")]
    first = lines[0].strip() if lines else ""
    if first.startswith("sequenceDiagram"):
        result = parse_sequence(lines)
    else:
        direction_match = re.match(r"(?:flowchart|graph)\s+(\w+)", first)
        if not direction_match:
            raise ValueError(f"{path}: not a Mermaid flowchart or sequence diagram")
        result = parse_flowchart(lines, direction_match.group(1))
    result["source"] = str(path)
    return result


def render_text(result: dict[str, Any]) -> str:
    out = [f"# {result['source']}", f"type: {result['type']}" + (f" {result['direction']}" if result["direction"] else "")]
    if result["type"] == "sequence":
        out.append(f"\n## Participants ({len(result['participants'])})")
        out.extend(f"- {p['id']}: {p['label']}" for p in result["participants"])
        out.append(f"\n## Messages ({len(result['messages'])})")
        for i, message in enumerate(result["messages"], 1):
            out.append(f"{i}. {message['from']} {message['arrow']} {message['to']}: {message['label']}")
        if result["notes"]:
            out.append(f"\n## Notes ({len(result['notes'])})")
            out.extend(f"- {note}" for note in result["notes"])
    else:
        out.append(f"\n## Nodes ({len(result['nodes'])})")
        out.extend(f"- {node['id']}: {node['label']}" for node in result["nodes"])
        out.append(f"\n## Edges ({len(result['edges'])})")
        for i, edge in enumerate(result["edges"], 1):
            label = f"  [{edge['label']}]" if edge["label"] else ""
            symbol = "<->" if edge["arrow"] in {"<-->", "<==>", "<-.->"} else "->"
            out.append(f"{i}. {edge['from']} {symbol} {edge['to']}{label}")
    if result["warnings"]:
        out.append(f"\n## Warnings ({len(result['warnings'])})")
        out.extend(f"- {warning}" for warning in result["warnings"])
    return "\n".join(out)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", nargs="+", type=Path)
    parser.add_argument("--json", action="store_true", help="emit JSON instead of Markdown")
    parser.add_argument("--strict", action="store_true", help="exit 1 when warnings were reported")
    args = parser.parse_args()

    results = []
    had_warnings = False
    for path in args.files:
        try:
            result = parse(path)
        except (OSError, ValueError) as error:
            print(f"error: {error}", file=sys.stderr)
            return 2
        results.append(result)
        had_warnings = had_warnings or bool(result["warnings"])
        if not args.json:
            print(render_text(result))
            print()

    if args.json:
        print(json.dumps(results, ensure_ascii=False, indent=2))
    return 1 if args.strict and had_warnings else 0


if __name__ == "__main__":
    raise SystemExit(main())
