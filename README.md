## Лaбораторная работа 1

Задание 1
```python
name=input("Имя: ")
age=int(input("Возраст: "))
print(f'Привет, {name} ! Через год тебе будет {age+1}.')
```
![скриншот 1](/images/lab01/01_greeting.png)


Задание 2
```python
n1=float(input("a: ").replace(",","."))
n2=float(input("b: ").replace(",","."))
sum1=n1+n2
avg1=(n1+n2)/2
print(f'sum={round(sum1,2)} ; avg={round(avg1,2)}')
```
![скриншот 2](/images/lab01/02_sum_avg.png)


Задание 3 
```python
price=float(input("цена: ").replace(",","."))
discount=float(input("скидка: ").replace(",","."))
vat=float(input("НДС: ").replace(",","."))
base = price * (1 - discount/100)
vat_amount = base * (vat/100)
total = base + vat_amount
print(f'База после скидки: {round(base,2)} ₽')
print(f'НДС: {round(vat_amount,2)} ₽')
print(f'Итого к оплате: {round(total,2)} ₽')
```
![скриншот 3](/images/lab01/03_disciunt_vat.png)


Задание 4
```python
m=int(input())
hours=m//60
min=m%60
print(f'{hours}:{min}')
```
![скриншот 4](/images/lab01/04_minutes_to_hhmm.png)


Задание 5
```python
name = input("Имя: ").split()
s = 0
for i in name:
    s += len(i)
print("Инициалы:",f"{name[0][0]}{name[1][0]}{name[2][0]}",".") 
print("Длина (символов):",s+2)
```
![скриншот 5](/images/lab01/05_initials_and_len.png)


Задание 6
```python
n=int(input())
tr,fl=0,0
for i in range(n):
    a,b,c,d=list(input().split())
    if d=="True":
        tr+=1
    else:
        fl+=1
print(tr,fl)
```
![скриншот 6](/images/lab01/06_True_or_False.png)


Задание 7
```python
n=input()
a,b=0,0
k,d=-1,-1
for i in n:
    k+=1
    if i in 'QWERTYUIOPASDFGHJKLZXCVBNM':
        a=k
        break
for i in n:
    d+=1
    if i in '0123456789':
        b=d+1
        break
print(n[a::b-a])
```
![скриншот 7](/images/lab01/07_Hello.png)


## Лабораторная работа 2

Задание 1.1
```python
def min_max(nums:list[int|float])-> tuple[int|float,int|float]:
    if len(nums)==0:
        raise ValueError("передан пустой массив")
    else:
        return (min(nums),max(nums))
nums=[1.5, 2, 2.0, -3.1]
print(min_max(nums))
```
![скриншот 8](/images/lab02/arrays.png)
![скриншот 9](/images/lab02/arrays1.png)


Задание 1.2
```python
def unique_sorted(nums: list[float | int]) -> list[float | int]:
    return list(set(nums))
nums=[1.0, 1, 2.5, 2.5, 0]
print(unique_sorted(nums))
```
![скриншот 10](/images/lab02/arrays2.1.png)
![скриншот 11](/images/lab02/arrays2.2.png)


Задание 1.3
```python
def flatten(mat: list[list | tuple]) -> list:
    res=list()
    for n in mat:
        if type(n) != type([]) and type(n) != type(()):
            raise TypeError("строка не строка строки матрицы")
        for i in n:
            res.append(i)
    return res
mat=[[1], [], [2, 3]]
print(flatten(mat))
```
![скриншот 12](/images/lab02/arrays3.1.png)
![скриншот 13](/images/lab02/arrays3.2.png)


Задание 2.1
```python
def transpose(mat: list[list[float | int]]) -> list[list]:
    if len(mat)>0 and any(len(row)!=len(mat[0]) for row in mat):
        raise ValueError('Рванная матрица')
    return[list(row) for row in zip(*mat)]
mat=[[1, 2], [3, 4]]
print(transpose(mat))
```
![скриншот 14](/images/lab02/matrix.png)
![скриншот 15](/images/lab02/matrix1.png)


Задание 2.2
```python
def row_sums(mat: list[list[float | int]]) -> list[float]:
    if len(mat)>0 and any(len(row)!=len(mat[0]) for row in mat):
        raise ValueError('Рванная матрица')
    sums=[sum(row) for row in mat]
    return sums 
mat=[[1, 2, 3], [4, 5, 6]]
print(row_sums(mat))
```
![скриншот 16](/images/lab02/matrix2.1.png)
![скриншот 17](/images/lab02/matrix2.2.png)


Задание 2.3
```python
def col_sums(mat: list[list[float | int]]) -> list[float]:
    if not mat:
        return []
    kol_simv_in_first = len(mat[0])
    for row in mat:
        if len(row) != kol_simv_in_first:
            raise ValueError("Матрица не прямоугольная")
    sums = [0] * kol_simv_in_first
    for row in mat:
        for i in range(kol_simv_in_first):
            sums[i] += row[i]
    return sums
mat=[[-1, 1], [10, -10]]
print(col_sums(mat))
```
![скриншот 18](/images/lab02/matrix3.1.png)
![скриншот 19](/images/lab02/matrix3.2.png)


Задание 3
```python
def student_registration(fio: str, group: str, gpa: float) -> tuple[str, str, float]:
    if type(fio) is not str:
        raise TypeError('ФИО должно быть в формате строки')
    elif len(fio) == 1:
        raise ValueError('Слишком короткое ФИО')
    if type(group) is not str:
        raise TypeError('Группа студента должна быть в формате строки')
    if type(gpa) is not float:
        raise TypeError('GPA должен быть в формате float')
    return tuple([fio, group, gpa])
def format_record(rec: tuple[str, str, float]) -> str:
    if type(rec) is not tuple:
        raise TypeError('Ввод в неправильном формате')
    else:
        fio_parts = rec[0].split()
        group = rec[1]
        gpa = rec[2]
        if len(fio_parts) == 3:
            return f'{fio_parts[0].capitalize()} {fio_parts[1][0].upper()}.{fio_parts[2][0].upper()}., гр. {group}, GPA {round(gpa, 2)}'
        else:
            return f'{fio_parts[0].capitalize()} {fio_parts[1][0].upper()}., гр. {group}, GPA {round(gpa, 2)}'
data = input().split()
fio = " ".join(data[:-2])
group = data[-2]
gpa = float(data[-1])
rec = student_registration(fio, group, gpa)
print(format_record(rec))
```
![скриншот 20](/images/lab02/tuples1.png)


## Лабораторная работа 3

Задание 1.1
```python
def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if casefold==True:
        text=text.casefold()
    if yo2e==True:
        text=text.replace("ё","е")
        text=text.replace("Ё","Е")
    text=text.replace("\t"," ")
    text=text.replace("\r"," ")
    text=text.replace("\n"," ")
    text=text.split()
    text=" ".join(text)
    return text
text="Hello\r\nWorld"
result=normalize(text)
print(result)
```
![скриншот 21](/images/lib/normalize.png)


Задание 1.2
```python
import re

def tokenize(text: str) -> list[str]:
    r = r"[\w]+(?:-[\w]+)*"
    return re.findall(r, text)
text="emoji 😀 не слово"
result= tokenize(text)
print(result)
```
![скриншот 22](/images/lib/tokenize.png)


Задание 1.3
```python
def count_freq(tokens: list[str]) -> dict[str, int]:
    result={}
    for i in tokens:
        if i not in result:
            result[i]=1
        else:
            result[i]+=1
    return result
tokens=["a","b","a","c","b","a"]
result2=count_freq(tokens)
print(result2)
```
![скриншот 23](/images/lib/count_freq.png)


Задание 1.4
```python
def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    items = freq.items()
    sorted_items = sorted(items, key=lambda x: (-x[1], x[0]))
    return sorted_items[:n]
text = {"aa":2,"bb":2,"cc":1}
result = top_n(text, n=2)
print(result)
```
![скриншот 24](/images/lib/top_n.png)


Задание 2
```python
import lib.text

def text_stats(text: str) -> str:
    norm_text = lib.text.normalize(text)
    tokens = lib.text.tokenize(norm_text)
    freq = lib.text.count_freq(tokens)
    total_words = len(tokens)
    unique_words = len(freq)
    top_words = lib.text.top_n(freq, n = 5)
    print(f'Всего слов: {total_words}')
    print(f'Уникальных слов: {unique_words}')
    print('Топ-5:')
    for word, count in top_words:
        print(f'{word}: {count}')

if __name__ == '__main__':
    text = input()
    text_stats(text)
```
![скриншот 25](/images/lab03/text_stats.png)


## Лабораторная работа 4

Задание 1
```python
import csv
from pathlib import Path
from lib.text import normalize

def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    p = Path(path)
    with p.open("r", encoding=encoding) as f:
        text = f.read()
    return normalize(text)

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
```


Задание 2
```python
from pathlib import Path
from lab04.io_txt_csv import read_text,write_csv
from lib.text import count_freq, normalize, tokenize
from lab03.text_stats import text_stats
path = Path(input())
pathoutput = Path(input())
text = normalize(read_text(path))
count_f = count_freq(tokenize(text))
rows = list(count_f.items())
write_csv(rows, pathoutput, ('word', 'count'))
text_stats(text)
```
![скриншот 26](/images/lab04/text_report.png)
![скриншот 27](/images/lab04/output.csv.png)


## Лабораторная работа 5

Задание 1.1
```python
from pathlib import Path
import json
from lib.text import read_json,read_csv,write_json
from lab04.io_txt_csv import write_csv
def json_to_csv(json_path: Path | str, csv_path: Path | str) -> None:
    json_path=read_json(Path(json_path))
    headers=[]
    for one in json_path:
        for header in one.keys():
            if  header is not headers:
                headers.append(header)
    results=[]
    for one in json_path: 
        result = [one.get(header, '') for header in headers]
        results.append(result)
    write_csv(results,csv_path,tuple(headers))
```
![скриншот 28](/images/lab05/json_to_csv.png)


Задание 1.2
```python
def csv_to_json(csv_path: Path | str, json_path: Path | str) -> None:
    content=read_csv(csv_path)
    keys=content[0]
    result=[]
    for one in content[1:]:
        row={
            keys[i]:one[i]
            for i in range(len(one))
        }
        result.append(row)
    write_json(json_path,result)

if __name__ == '__main__':
    path_in = 'data/samples/people.csv'
    path_out = 'data/out/people_from_csv.json'
    csv_to_json(path_in,path_out)
```
![скриншот 29](/images/lab05/csv_to_json.png)


Задание 2
```python
from openpyxl import Workbook
from pathlib import Path

from lib.text import read_csv

def csv_to_xlsx(csv_path: Path, xlsx_path: Path) -> None:
    content = read_csv(csv_path)
    wb = Workbook()
    ws = wb.active
    ws.title = 'Data'
    for row in content:
        clean_row = [str(one).strip() for one in row]
        ws.append(clean_row)
    wb.save(xlsx_path)

if __name__ == "__main__":
    path_input = 'data/samples/people.csv'
    path_output = 'data/out/people.xlsx'
    csv_to_xlsx(path_input, path_output)
```
![скриншот 30](/images/lab05/csv_xlsx.png)


## Лабораторная работа 6

Задание 1
```python 
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
```
![скриншот 31](/images/lab06/json2csv.png)
![скриншот 32](/images/lab06/csv2json.png)
![скриншот 33](/images/lab06/csv2xlsx.png)


Задание 2
```python 
import argparse
from pathlib import Path

from lab03.text_stats import text_stats


def main():
    parser = argparse.ArgumentParser(description="CLI-утилиты лабораторной №6")
    subparsers = parser.add_subparsers(dest="command")

    cat_parser = subparsers.add_parser("cat", help="Вывести содержимое файла")
    cat_parser.add_argument("--input", required=True, type=Path)
    cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки")

    stats_parser = subparsers.add_parser("stats", help="Частота строк")
    stats_parser.add_argument("--input", type=str, required=True)
    stats_parser.add_argument("--top", type=int, default=5)
    stats_parser.add_argument("-p", action="store_true", help="Output in table form")

    args = parser.parse_args()

    if not args.command:
        parser.error("You")

    if args.command == "cat":
        with args.input.open("r", encoding="utf-8") as f:
            for number, text in enumerate(f):
                if args.n:
                    print(f"{number + 1}: {text.strip()}")
                else:
                    print(text.strip())
    elif args.command == "stats":
        with open(args.input, "r", encoding="utf-8") as f:
            text = f.read()
        text_stats(text, n=args.top)

if __name__ == "__main__":
    main()
```
![скриншот 34](/images/lab06/cat1.png)
![скриншот 35](/images/lab06/stats.png)


## Лабораторная работа 7

Задание 1
```python
import pytest
from src.lib.text import normalize, tokenize, count_freq, top_n


@pytest.mark.parametrize(
    "source, expected",
    [
        ("ПрИвЕт\nМИр\t", "привет мир"),
        ("ёжик, Ёлка", "ежик, елка"),
        ("Hello\r\nWorld", "hello world"),
        ("  двойные   пробелы  ", "двойные пробелы"),
        ("", ""),  
        ("!!!", "!!!"),  
        (" A   B   C ", "a b c"), 
    ],
)
def test_normalize_basic(source, expected):
    assert normalize(source) == expected


@pytest.mark.parametrize(
    "source, expected",
    [
        ("привет мир",["привет", "мир"]),
        ("hello,world!!!",["hello", "world"]),
        ("по-настоящему круто",["по-настоящему", "круто"]),
        ("", []), 
        ("!!!", []), 
        ("a a a", ["a", "a", "a"]), 
    ],
)
def test_tokenize_basic(source, expected):
    assert tokenize(source) == expected


def test_count_freq_and_top_n():
    tokens = ["a", "b", "a", "c", "b", "a"]
    freq = count_freq(tokens)

    assert freq == {"a": 3, "b": 2, "c": 1}
    assert top_n(freq, 2) == [("a", 3), ("b", 2)]
    assert top_n(freq, 5) == [("a", 3), ("b", 2), ("c", 1)]


def test_top_n_tie_breaker():
    freq = {"яблоко": 2, "арбуз": 2, "банан": 2}

    expected_sorted = [
        ("арбуз", 2),
        ("банан", 2),
        ("яблоко", 2),
    ]

    assert top_n(freq, 10) == expected_sorted
```
![скриншот 36](/images/lab07/test_text.png)


Задание 2
```python
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
```
![скриншот 37](/images/lab07/test_json_csv.png)


## Лабораторная работа 8

Задание 1
```python
import datetime
from dataclasses import dataclass


@dataclass
class Student:
    fio: str
    birthdate: str
    group: str
    gpa: float

    def __post_init__(self):
        try:
           self.birthdate_obj= datetime.datetime.strptime(self.birthdate, "%Y/%m/%d")
        except ValueError:
            raise ValueError("Неправильный формат вводы даты рождения. Попробуйте YYYY/MM/DD")
        if not isinstance(self.fio,str):
            raise TypeError("ФИО должно быть в виде строки")
        if len(self.fio.split())!=3:
            raise ValueError("ФИО должно состоять из трех слов")
        
        if not (0 <= self.gpa <= 10):
            raise ValueError("Gpa должно быть не меньше 0 и не больше 10")

    def age(self) -> int:
        birthdate = self.birthdate_obj
        today = datetime.date.today()
        age=(
            today.year
            - birthdate.year
            - ((today.month, today.day) < (birthdate.month, birthdate.day))
        )
        return age

    def to_dict(self) -> dict:
        return {
            "fio": self.fio,
            "birthdate": self.birthdate,
            "group":self.group,
            "gpa": self.gpa,
        }

    @classmethod
    def from_dict(cls, d: dict):
        required=["fio","birthdate","group","gpa"]
        for i in required:
            if i not in d.keys():
                raise ValueError("Dict must contain fio, birthdate, group, gpa")
        return cls(
            fio=d["fio"],
            birthdate=d["birthdate"],
            group=d["group"],
            gpa=d["gpa"],
        )

    def __str__(self):
        return f"{self.fio}, {self.group},{self.birthdate}, GPA:{self.gpa}"
```


Задание 2 
```python
from pathlib import Path
from lab08.models import Student 
from lib.text import write_json,read_json


def students_to_json(students: list[Student], path:Path)->None:
    path = Path(path) 
    path.parent.mkdir(parents=True, exist_ok=True)
    data = [s.to_dict() for s in students]
    write_json(data, path)


def students_from_json(path:Path)->list[Student]:
    content=read_json(path)
    result=[
        Student(
            one.get("fio", None),
            one.get("birthdate", None),
            one.get("group", None),
            one.get("gpa", None),
        )
        for one in content
    ]
    return result
if __name__=="__main__":
    Arina=Student("Arina Lukyanova Sergeevna","2003/11/09","Misis",4.8)
    students_to_json([Arina],"data/lab08/students_output.json")
```
![скриншот 38](/images/lab08/rerialize.png)


## Лабораторная работа 9

Задание 1
```python
import csv
from pathlib import Path
from dataclasses import dataclass
from lab08.models import Student
from lib.text import read_csv
from lab04.io_txt_csv import write_csv


class Group:
    def __init__(self, storage_path: str):
        self.path = Path(storage_path)
        self.content=self._read_all()
        if not self.path.exists():
            self.path.write_text("", encoding="utf-8") 

    def __post_init__(self):
        if self.content[0] !=["fio,birthdate,group,gpa"]:
            write_csv(self.content,self.path,[["fio,birthdate,group,gpa"]])
            self.content=self._read_all()


    def _read_all(self)->list[list]:
        return read_csv(self.path)

    def list(self)->list[Student]:
        result=[]
        for one_stud in self.content[1:]:
            stud=Student.from_dict({"fio":one_stud[0],"birthdate":one_stud[1],"group":one_stud[2],"gpa":one_stud[3]})
            result.append(stud)
        return result
    
    def add(self, student: Student):
        one=[student.fio,student.birthdate,student.group,student.gpa]
        self.content.append(one)
        write_csv(self.content[1:],self.path,self.content[0])


    def find(self, substr: str)->bool:
        arr=[]
        for one in self.content[1:]:
            if substr in one[0]:
                return True
        return False
            
        
          

    def remove(self, fio: str):
        new_content=[self.content[0]]
        for one in self.content[1:]:
            if not(fio in one[0]):
                new_content.append(one)
        write_csv(new_content[1:],self.path,new_content)
        self.content=self._read_all()
           
    def update(self, fio: str, **fields)->None:
        new_content=[]
        for one in self.content[1:]:
            if fio in one[0]:
                one=[
                    fields.get("fio",one[0]),
                    fields.get("birthdate",one[1]),
                    fields.get("group",one[2]),
                    fields.get("gpa",one[3]),
                ]
            new_content.append(one)
        write_csv(new_content[1:],self.path,new_content)
        self.content=self._read_all()

if __name__ == "__main__":
    group = Group("data/lab09/students.csv")
    group.add(Student("Arina Lukyanova Sergeevna", "2007/11/09", "25-4", 4.8))
    print(group.list())
```
![скриншот 39](/images/lab09/group.png)
![скриншот 40](/images/lab09/student.png)


## Лабораторная работа 10

Задание 1
```python
from collections import deque
from typing import Any

class Queue:
    def __init__(self):
        self._data: deque[Any] = deque()

    def enqueue(self, item) -> None:
        self._data.appendleft(item)

    def dequeue(self) -> Any:
        if self.__len__ == 0:
            raise IndexError("")
        return self._data.pop()

    def peak(self) -> Any | None:
        if self.__len__ == 0:
            raise IndexError("")
        return self._data[-1]

    def is_empty(self) -> bool:
        if self.__len__ == 0:
            return True
        return False

    def __len__(self) -> int:
        return len(self._data)


class Stack:
    def __init__(self):
        self._data: list[Any] = []

    def push(self, item) -> None:
        self._data.append(item)

    def pop(self) -> Any:
        if self.__len__ == 0:
            raise IndexError("Sosi pissy")
        return self._data.pop()

    def peek(self) -> Any | None:
        if self.__len__ == 0:
            return None
        return self._data[-1]

    def is_empty(self) -> bool:
        if self.__len__ == 0:
            return True
        return False

    def __len__(self) -> int:
        return len(self._data)
```
![скриншот 41](/images/lab10/structures.png)


Задание 2
```python
class Node:
    def __init__(self, value: any, next):
        self.value = value
        self.next = next


class SinglyLinkedList:
    def __init__(self, head: Node, tail: Node):
        self.head = None
        self.tail = None
        self._size: int = 0

    def append(self, value: any) -> None:
        new = Node(value, None)
        if self.head == None:
            self.head = new
            self.tail = new
        else:
            self.tail.next = new
            self.tail = new
        self._size += 1

    def prepend(self, value: any) -> None:
        new = Node(value, self.head)
        self.head = new
        if self.tail == None:
            self.tail = new
        self._size += 1

    def insert(self, idx: int, value: any) -> None:
        if not (0 < idx < self.__len__):
            raise IndexError("")
        cur = self.head
        for i in range(idx - 1):
            cur = cur.next
        new = Node(value, None)
        new.next = cur.next
        cur.next = new
        self._size += 1

    def remove(self, value: any) -> None:
        if self.head == None:
            return
        old = cur
        cur = self.head
        while cur.next:
            if cur.next.value == value:
                cur.next = cur.next.next
                if cur.next is None:
                    self.tail = cur
                self._size -= 1
                return
            cur = cur.next

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current.value
            current = current.next

    def __len__(self) -> int:
        return self._size

    def __rerp__(self) -> str:
        return f"SinglyLinkedList({list(self)})"
```
![скриншот 42](/images/lab10/linked_list.png)
