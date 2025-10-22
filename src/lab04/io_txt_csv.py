from pathlib import Path
from lib.text import normalize
def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    p = Path(path)
    f=open(Path)
    text=f.readlines()
    text=lib.text.normalize(text)
    return text
path=input()
result=read_text(path)
print(result)