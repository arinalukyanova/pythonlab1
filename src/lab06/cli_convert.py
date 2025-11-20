import argparse
from pathlib import Path
from lab05.json_csv import json_to_csv, csv_to_json
from lab05.csv_xlsx import csv_to_xlsx


def main():
    parser = argparse.ArgumentParser(description="Конверты данных")
    subparsers = parser.add_subparsers(dest="command")

    json2csv = subparsers.add_parser("json2csv", help="перевод из json в csv файл")
    json2csv.add_argument("--in", required=True, type=Path, dest="path_in")
    json2csv.add_argument("--out", required=True, type=Path, dest="path_out")

    csv2json = subparsers.add_parser("csv2json", help="перевод из csv в json файл")
    csv2json.add_argument("--in", required=True, type=Path, dest="path_in")
    csv2json.add_argument("--out", required=True, type=Path, dest="path_out")

    csv2xlsx = subparsers.add_parser("csv2xlsx", help="перевод из csv в xlsx файл")
    csv2xlsx.add_argument("--in", required=True, type=Path, dest="path_in")
    csv2xlsx.add_argument("--out", required=True, type=Path, dest="path_out")

    args = parser.parse_args()

    if args.command == "json2csv":
        json_to_csv(args.path_in, args.path_out)
    elif args.command == "csv2json":
        csv_to_json(args.path_in, args.path_out)
    elif args.command == "csv2xlsx":
        csv_to_xlsx(args.path_in, args.path_out)

if __name__ == "__main__":
    main()