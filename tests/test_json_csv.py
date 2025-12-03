import pytest
from src.lab05.json_csv import csv_to_json, json_to_csv
from src.lab04.io_txt_csv import write_csv
from src.lib.text import read_json,write_json,read_csv


@pytest.mark.parametrize(
    "input_path, output_path, expexted",
    [
        ("tmp/input.json", "tmp/output.csv", [["name", "age"],["Arina", "18"]]),
        ("tmp/not_exist.json", None, None),
        ("tmp/empty.json", "tmp/output.csv", None),
    ],
)
def test_json_to_csv(input_path, output_path, expexted):
    if input_path=="tmp/not_exist.json":
        with pytest.raises(FileNotFoundError, match= "Файл не найден"):
            json_to_csv(input_path, output_path)
    elif input_path=="tmp/empty.json":
        with pytest.raises(ValueError, match="Json is empty"):
            json_to_csv(input_path, output_path)    
    else:
        write_json([{"name": "Arina", "age": "18"}], input_path)
        json_to_csv(input_path, output_path)
        assert read_csv(output_path) == expexted


@pytest.mark.parametrize(
    "input_path, output_path, expected",
    [
        ("tmp/input.csv","tmp/output.json", [{"name": "Arina", "age": "18"}]),
        ("tmp/empty.csv","tmp/output.json", [{"name": "Arina", "age": "18"}]),
        ("tmp/not_exist.csv","tmp/output.json", [{"name": "Arina", "age": "18"}]),
    ],
)
def test_csv_to_json(input_path, output_path, expected):
    if input_path == "tmp/empty.csv":
        with pytest.raises(ValueError, match="Csv is empty"):
            csv_to_json(input_path, output_path)
    elif input_path == "tmp/not_exist.csv":
        with pytest.raises(FileNotFoundError, match="Файл не найден"):
            csv_to_json(input_path, output_path)
    else:
        write_csv([["Arina", "18"]], input_path, tuple(["name", "age"]))
        csv_to_json(input_path, output_path)
        assert read_json(output_path) == expected