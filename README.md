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
