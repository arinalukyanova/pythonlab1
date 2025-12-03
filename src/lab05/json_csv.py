from pathlib import Path
import json
from src.lib.text import read_json, read_csv, write_json
from src.lab04.io_txt_csv import write_csv


def json_to_csv(json_path: Path | str, csv_path: Path | str) -> None:
    json_path = read_json(Path(json_path))
    if not json_path:
        raise ValueError("Json is empty")
    headers = []
    for one in json_path:
        for header in one.keys():
            if header is not headers:
                headers.append(header)
    results = []
    for one in json_path:
        result = [one.get(header, "") for header in headers]
        results.append(result)
    write_csv(results, csv_path, tuple(headers))


def csv_to_json(csv_path: Path | str, json_path: Path | str) -> None:
    try:
        content = read_csv(csv_path)
    except FileNotFoundError:
        raise FileNotFoundError("Файл не найден")
    if not content:
        raise ValueError("Csv is empty")
    keys = content[0]
    result = []
    for one in content[1:]:
        row = {keys[i]: one[i] for i in range(len(one))}
        result.append(row)
    write_json(result,json_path)


if __name__ == "__main__":
    path_in = "data/samples/people.csv"
    path_out = "data/out/people_from_csv.json"
    csv_to_json(path_in, path_out)
