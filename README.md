## Лaбораторная работа 1

Задание 1
```python
name=input("Имя: ")
age=int(input("Возраст: "))
print("Привет,",name,"! Через год тебе будет",age+1,".")
```
![скриншот 1](/images/lab01/01_greeting.png)


Задание 2
```python
n1=float(input("a: ").replace(",","."))
n2=float(input("b: ").replace(",","."))
sum1=n1+n2
avg1=(n1+n2)/2
print("sum=",round(sum1,2),";","avg=",round(avg1,2))
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
print("База после скидки:",round(base,2),"₽")
print("НДС:",round(vat_amount,2),"₽")
print("Итого к оплате:",round(total,2),"₽")
```
![скриншот 3](/images/lab01/03_disciunt_vat.png)


Задание 4
```python
m=int(input())
hours=m//60
min=m%60
print(hours,":",min)
```
![скриншот 4](/images/lab01/04_minutes_to_hhmm.png)


Задание 5
```python
name = input("Имя: ").split()
s = 0
for i in name:
    s += len(i)
print("Инициалы:",f"{name[0][0]}{name[1][0]}{name[2][0]}",".") 
print("Длина (символов):",s)
```
![скриншот 5](/images/lab01/05_initials_and_len.png)
