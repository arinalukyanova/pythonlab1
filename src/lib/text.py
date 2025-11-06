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
##print(result)


import re

def tokenize(text: str) -> list[str]:
    r = r"[\w]+(?:-[\w]+)*"
    return re.findall(r, text)
text="emoji 😀 не слово"
result= tokenize(text)
##print(result)


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
##print(result2)

##print(count_freq(tokenize(normalize(text))))


def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    items = freq.items()
    sorted_items = sorted(items, key=lambda x: (-x[1], x[0]))
    return sorted_items[:n]
text = {"aa":2,"bb":2,"cc":1}
result = top_n(text, n=2)
##print(result)


from pathlib import Path
import json
def read_json(path_to_json: Path | str)-> list[dict]:
    p=Path(path_to_json)
    if not path_to_json.exists():
        raise FileNotFoundError()
    if path_to_json.suffix.lower()!=".json":
        raise ValueError()
    with p.open("r") as f:
        text = f.read()
    if text== "":
        raise ValueError
    result=json.loads(text)
    return result


def write_json(path_to_text: Path | str ,text: list[dict])->None:
    p=Path(path_to_text)
    if not path_to_text.exists():
        raise FileNotFoundError()
    if text== []:
        raise ValueError()
    with p.open("w",text) as f:
        f.write(json.dumps(text))
   

def read_csv(path_to_csv: Path | str )->list[str]:
    p=Path(path_to_csv)
    if not path_to_csv.exists():
        raise FileNotFoundError()
    if path_to_csv.suffix.lower()!=".csv":
        raise ValueError()
    with p.open("r") as f:
        text = f.read()
    if text== "":
        raise ValueError()
    text=text.split("\n")
    result=[]
    for one in text:
        result.append(one.split(", "))
    return result


def csv_to_xlsx