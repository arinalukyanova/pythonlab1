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