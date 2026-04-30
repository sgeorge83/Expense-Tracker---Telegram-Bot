import csv
from pathlib import Path


def export_transactions_csv(rows: list[dict], file_path: str) -> str:
    path = Path(file_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        rows = [{"amount": 0, "category": "none", "description": "no data"}]
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
    return str(path)
