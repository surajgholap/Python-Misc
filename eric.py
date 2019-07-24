from collections import Counter
import requests


def top_five(corpus):
    count_map = {}
    for i in corpus:
        try:
            count_map[i] += 1
        except:
            count_map[i] = 1

    # words = corpus.split()
    # counter = Counter(words)
    # most_fav = counter.most_common(5)

    # for i in most_fav:
    #     print(i)


def clean_func(corpus, stop):
    new = []
    for i in corpus.split(" "):
        i = i.lower()
        if i.isalpha() and i not in stop:
            new.append(i)
    top_five(" ".join(new))


response = requests.get(
    "https://ocw.mit.edu/ans7870/6/6.006/s08/lecturenotes/files/t8.shakespeare.txt")
stop_words = requests.get(
    "https://gist.githubusercontent.com/sebleier/554280/raw/7e0e4a1ce04c2bb7bd41089c9821dbcf6d0c786c/NLTK's%2520list%2520of%2520english%2520stopwords")
stop_list = stop_words.text.splitlines()
# print(stop_list)
content = response.text.splitlines()
content = " ".join(content[245:])
# print(content)

clean_func(content, stop_list)
