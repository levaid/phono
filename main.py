import gzip
from processing.converter import PhonemeConverter

limit = 10
sentences = []
conv = PhonemeConverter()

with gzip.open('testfile.txt.gz','rt') as f:
    for i, line in enumerate(f):
        if i < limit:
            sentences.append(line.strip())

#print(sentences[1].split(' '))

#print(conv.convert(sentences[1]))


from processing.converter import PhonemeConverter
peldak = 'balra, modellre, széngyűrű, szén|pénz, verssel, kardja, hangya, ajánlat, tanrész, döfj, fúrj, szívből, hatvan, pechből, adhat, metszet, jutsz, kétség, fűtsd, hat cica, kalapot cserél, ötödször, fáradtság'
peldak = conv.double_letters(peldak)
print(conv.sibilant_assimilation(peldak))




