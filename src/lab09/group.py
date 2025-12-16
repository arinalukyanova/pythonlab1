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