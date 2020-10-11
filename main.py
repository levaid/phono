import gzip
from processing.converter import PhonemeConverter
import gzip

limit = 10
sentences = []
conv = PhonemeConverter()

with gzip.open('testfile.txt.gz','rt') as f:
    for i, line in enumerate(f):
        if i < limit:
            sentences.append(line.strip())

print(sentences[1].split(' '))

print(conv.convert(sentences[1]))





