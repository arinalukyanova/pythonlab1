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
