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


##Лабораторная работа 2

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
![скриншот 12](/images/lab02/arrays3.2.png)
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


