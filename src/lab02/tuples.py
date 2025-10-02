def student_registration(fio: str, group: str, gpa: float) -> tuple[str, str, float]:
    if type(fio) is not str:
        raise TypeError('ФИО должно быть в формате строки')
    elif len(fio) == 1:
        raise ValueError('Слишком короткое ФИО')
    if type(group) is not str:
        raise TypeError('Группа студента должна быть в формате строки')
    if type(gpa) is not float:
        raise TypeError('Группа должна быть в формате float')
    return tuple([fio, group, gpa])

def format_record(rec: tuple[str, str, float]) -> str:
    if type(rec) is not tuple:
        raise TypeError('Ввод в неправильном формате')
    else:
        fio = list(rec[0].split())
        if len(fio) == 3:
            return f'{fio[0][0].upper() + fio[0][1:]} {fio[1][0].upper()}.{fio[2][0].upper()}., гр. {group}, GPA {round(rec[2], 2)}'
        else:
            return f'{fio[0][0].upper() + fio[0][1:]} {fio[1][0].upper()}., гр. {group}, GPA {round(rec[2], 2)}'
fio=input()
group=input()
gpa=float(input())
rec=student_registration(fio,group,gpa)
print(format_record(rec))