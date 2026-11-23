"""Authored label-suggestion replay. Never executes any command."""
import json
from distance import edit_distance

LABELS = ("deploy", "status", "logs")
THRESHOLD = 1


def replay():
    query = "deply"
    distances = {label: edit_distance(query, label) for label in LABELS}
    candidates = [label for label in LABELS if distances[label] <= THRESHOLD]
    return {"kind": "authored local label helper", "query": query,
            "known_labels": list(LABELS), "threshold": THRESHOLD,
            "distances": distances, "candidates": candidates,
            "passed": candidates == ["deploy"] and distances["deploy"] == 1,
            "executes_commands": False}


if __name__ == "__main__":
    result = replay()
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result["passed"] else 1)
