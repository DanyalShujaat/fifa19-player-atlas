"""Create a compact browser dataset from the public FIFA 19 data.csv."""
import csv
import json
from pathlib import Path


def rating(value):
    try:
        return int(value)
    except (TypeError, ValueError):
        return None


rows = []
with Path("source-data.csv").open(encoding="utf-8-sig", newline="") as file:
    for item in csv.DictReader(file):
        overall = rating(item.get("Overall"))
        if not overall or not item.get("Name"):
            continue
        rows.append({"name": item["Name"], "age": rating(item.get("Age")),
                     "nation": item.get("Nationality") or "Unknown", "club": item.get("Club") or "Free agent",
                     "position": item.get("Position") or "—", "overall": overall,
                     "potential": rating(item.get("Potential")) or overall,
                     "value": item.get("Value") or "—", "wage": item.get("Wage") or "—"})
rows.sort(key=lambda r: (-r["overall"], -r["potential"], r["name"]))
Path("players.json").write_text(json.dumps(rows, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
print(f"Prepared {len(rows)} player records")
