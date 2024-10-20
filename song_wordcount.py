import os
import re
from collections import Counter
import socket

file1 = '/home/data/IF.txt'
file2 = '/home/data/AlwaysRememberUsThisWay.txt'
output_file = '/home/data/output/result.txt'
os.makedirs('/home/data/output', exist_ok=True)

def count_words(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
        words = re.findall(r'\b\w+\b', text)
        return len(words), words

def most_frequent_words(words, n=3):
    counter = Counter(words)
    return counter.most_common(n)

def handle_contractions(words):
    expanded_words = []
    for word in words:
        if "'" in word:
            expanded_words.extend(re.findall(r'\b\w+\b', re.sub(r"’", "", word)))
        else:
            expanded_words.append(word)
    return expanded_words

count1, words1 = count_words(file1)
count2, words2 = count_words(file2)
grand_total = count1 + count2

top_words_if = most_frequent_words(words1)

expanded_words2 = handle_contractions(words2)
top_words_ar = most_frequent_words(expanded_words2)

ip_address = socket.gethostbyname(socket.gethostname())

os.makedirs(os.path.dirname(output_file), exist_ok=True)

with open(output_file, 'w') as out_file:
    out_file.write(f"Word count of IF.txt: {count1}\n")
    out_file.write(f"Word count of AlwaysRememberUsThisWay.txt: {count2}\n")
    out_file.write(f"Total words: {grand_total}\n")
    out_file.write("Top 3 words most common in IF.txt are:\n")
    for word, count in top_words_if:
        out_file.write(f"{word}: {count}\n")
    out_file.write("Top 3 words most common in AlwaysRememberUsThisWay.txt are:\n")
    for word, count in top_words_ar:
        out_file.write(f"{word}: {count}\n")
    out_file.write(f"IP: {ip_address}\n")

with open(output_file, 'r') as file:
    print(file.read())