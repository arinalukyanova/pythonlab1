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