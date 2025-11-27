from pathlib import Path
from lab04.io_txt_csv import read_text, write_csv
from lib.text import count_freq, normalize, tokenize
from lab03.text_stats import text_stats

path = Path(input())
pathoutput = Path(input())
text = normalize(read_text(path))
count_f = count_freq(tokenize(text))
rows = list(count_f.items())
write_csv(rows, pathoutput, ("word", "count"))
text_stats(text)
