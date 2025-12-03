import csv
from pathlib import Path
from src.lib.text import normalize


def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    p = Path(path)
    with p.open("r", encoding=encoding) as f:
        text = f.read()
    return normalize(text)


##path=input()
##result=read_text(path)
##print(result)


def write_csv(
    rows: list[tuple | list],
    path: str | Path,
    header: tuple[str, ...] | None = None,
    *,
    file_name: str = None,
) -> None:
    p = Path(path)
    if not rows and header is None:
        raise ValueError("Нельзя создать пустой CVS без заголовка и данных")
    row_length = len(rows[0]) if rows else len(header)
    for r in rows:
        if len(r) != row_length:
            raise ValueError(
                f"Несовпадение длины строк: ожидалось {row_length}, а получено {len(r)}"
            )
    if header is not None and len(header) != row_length:
        raise ValueError("Длина header не совпадает с длиной строки")
    with p.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if header is not None:
            writer.writerow(header)
        writer.writerows(rows)
