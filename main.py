import gzip
from processing.converter import PhonemeConverter
import re 
from itertools import islice


sentences = []
conv = PhonemeConverter()

@profile
def process(converter: PhonemeConverter, sentence: str):
    sentence = converter.double_letters(sentence)
    sentence = converter.fast_double_letters(sentence)

    sentence = converter.degemination(sentence)
    sentence = converter.fast_degemination(sentence)

    sentence = converter.n_assimilation(sentence)
    sentence = converter.fast_n_assimilation(sentence)

    sentence = converter.palatal_assimilation(sentence)
    sentence = converter.fast_palatal_assimilation(sentence)

    sentence = converter.sibilant_assimilation(sentence)
    sentence = converter.fast_sibilant_assimilation(sentence)

    sentence = converter.voice_assimilation(sentence)
    sentence = converter.fast_voice_assimilation(sentence)

    sentence = converter.nasalisation(sentence)
    sentence = converter.fast_nasalisation(sentence)

    sentence = converter.hiatus_filling(sentence)
    sentence = converter.n_nasalization(sentence)
    sentence = converter.l_assimilation(sentence)

    return(sentence)

@profile
def fast_process(converter: PhonemeConverter, sentence: str):

    sentence = converter.fast_double_letters(sentence)
    sentence = converter.fast_degemination(sentence)
    sentence = converter.fast_n_assimilation(sentence)
    sentence = converter.fast_palatal_assimilation(sentence)
    sentence = converter.fast_sibilant_assimilation(sentence)
    sentence = converter.fast_voice_assimilation(sentence)
    sentence = converter.fast_nasalisation(sentence)

    sentence = converter.hiatus_filling(sentence)
    sentence = converter.n_nasalization(sentence)
    sentence = converter.l_assimilation(sentence)

    return(sentence)

@profile
def slow_process(converter: PhonemeConverter, sentence: str):

    sentence = converter.double_letters(sentence)
    sentence = converter.degemination(sentence)
    sentence = converter.n_assimilation(sentence)
    sentence = converter.palatal_assimilation(sentence)
    sentence = converter.sibilant_assimilation(sentence)
    sentence = converter.voice_assimilation(sentence)
    sentence = converter.nasalisation(sentence)

    sentence = converter.hiatus_filling(sentence)
    sentence = converter.n_nasalization(sentence)
    sentence = converter.l_assimilation(sentence)

    return(sentence)

sentences = []
batchsize = 1000
limit = 100000 // batchsize
with gzip.open('testfile.txt.gz','rt') as f:
    i = 0
    while True:
        batch = ''.join((islice(f, batchsize)))
        if i < limit:
            process(conv, batch)
            fast_process(conv, batch)
            slow_process(conv, batch)
            i += 1
        if not batch or i >= limit:
            break
#print(sentences[1].split(' '))
            

#print(conv.convert(sentences[1]))
peldak = 'balra, modellre, széngyűrű, szén|pénz, verssel, kardja, hangya, ajánlat, tanrész, döfj, fúrj, szívből, hatvan, pechből, adhat, metszet, jutsz, kétség,'\
 'fűtsd, hat cica, kalapot cserél, ötödször, fáradtság, dobtam, képzés, adhat, hétből, edzhet, ketrecben, fogtam, zsákból, ágytól, pintyből, szívtam, széfben, méztől,'\
     ' mészből, rúzstól, hasba, hatvan, korccsal, rontson, koszttól, direkttermő, tankként, combból, talppont, szerb bor, sztrájkkor, sért talán, verssel, ponttá,'\
         'akttal, küldte, rajzzon, kardja, nagyja, adja, tolja, unja, hányja, látja, atyja, folyjon, hadgyakorlat, nemzetgyúlés, vadtyúk, hat tyúk, lúdnyak, átnyúlik'\
             ' hallva, vers|sel, '

peldak += 'jobbra, pattra, gallyra, has|sba, szebbnél'
peldak = conv.double_letters(peldak)
print(peldak)


consonants = 'bcdfghjklmnpqrstvwxzčďǧɲʃťž'
long_consonants = 'BCDFGHJKLMNPQRSTVWXZČĎǦƝƩŤŽ'
liquid = 'jlr'
nasal = 'mnɲ'
obstruents = 'bcdfghkpqstvwxzčďǧʃťž'    

# print(peldak)
peldak_orig = conv.degemination(peldak)
print('orig______', peldak_orig)

peldak_fast = conv.fast_degemination(peldak)
print('fast______', peldak_fast)
# HACK although I hope it works fast AF









