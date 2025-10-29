import csv
from pathlib import Path
from lib.text import normalize

def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    p = Path(path)
    with p.open("r", encoding=encoding) as f:
        text = f.read()
    return normalize(text)
##path=input()
##result=read_text(path)
##print(result)


def write_csv(rows: list[tuple | list], path: str | Path,
              header: tuple[str, ...] | None = None) -> None:
    p = Path(path)
    rows = list(rows)
    if not rows and header is None:
            raise ValueError
    row_length = len(rows[0]) if rows else len(header)
    for r in rows:
        if len(r) != row_length:
            raise ValueError
    if header is not None and len(header) != row_length:
        raise ValueError
    with p.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if header is not None:
            w.writerow(header)
        for r in rows:
            w.writerow(r)

