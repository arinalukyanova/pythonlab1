price=float(input("цена: ").replace(",","."))
discount=float(input("скидка: ").replace(",","."))
vat=float(input("НДС: ").replace(",","."))
base = price * (1 - discount/100)
vat_amount = base * (vat/100)
total = base + vat_amount
print(f'База после скидки: {round(base,2)} ₽')
print(f'НДС: {round(vat_amount,2)} ₽')
print(f'Итого к оплате: {round(total,2)} ₽')