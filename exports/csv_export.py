import csv
from pathlib import Path


def export_transactions_csv(rows: list[dict], file_path: str) -> str:
    path = Path(file_path)
    path.parent.mkdir(parents=True, exist_ok=True)
   if not rows:
    rows = [{"amount": 0, "category": "none", "description": "no data"}]

    fieldnames = sorted({key for row in rows for key in row.keys()})

    with path.open("w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(
        f,
        fieldnames=fieldnames,
        extrasaction="ignore",
    )
    writer.writeheader()
    writer.writerows(rows)
    return str(path)
