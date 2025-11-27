from openpyxl import Workbook
from pathlib import Path

from lib.text import read_csv


def csv_to_xlsx(csv_path: Path, xlsx_path: Path) -> None:
    content = read_csv(csv_path)
    wb = Workbook()
    ws = wb.active
    ws.title = "Data"
    for row in content:
        clean_row = [str(one).strip() for one in row]
        ws.append(clean_row)
    wb.save(xlsx_path)


if __name__ == "__main__":
    path_input = "data/samples/people.csv"
    path_output = "data/out/people.xlsx"
    csv_to_xlsx(path_input, path_output)
