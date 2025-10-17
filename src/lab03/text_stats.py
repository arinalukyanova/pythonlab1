import lib.text

def text_stats(text: str) -> str:
    norm_text = lib.text.normalize(text)
    tokens = lib.text.tokenize(norm_text)
    freq = lib.text.count_freq(tokens)
    total_words = len(tokens)
    unique_words = len(freq)
    top_words = lib.text.top_n(freq, n = 5)
    print(f'Всего слов: {total_words}')
    print(f'Уникальных слов: {unique_words}')
    print('Топ-5:')
    for word, count in top_words:
        print(f'{word}: {count}')

if __name__ == '__main__':
    text = input()
    text_stats(text)
