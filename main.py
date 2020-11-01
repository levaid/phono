import gzip
from processing.converter import PhonemeConverter
import re 
from itertools import islice


sentences = []
conv = PhonemeConverter()


sentences = []
batchsize = 1000
limit = 10000 // batchsize
with gzip.open('testfile.txt.gz','rt') as f, open('dif1file.txt','w') as outfile1, open('dif2file.txt','w') as outfile2:
    i = 0
    while True:
        batch = ''.join((islice(f, batchsize)))
        if i < limit:
            #outfile.write(batch)
            #outfile.write(conv.process(batch))
            outfile1.write(conv.fast_process(batch))
            outfile2.write(conv.slow_process(batch))
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
peldak = conv.fast_double_letters(peldak)
#print(peldak)


consonants = 'bcdfghjklmnpqrstvwxzčďǧɲʃťž'
long_consonants = 'BCDFGHJKLMNPQRSTVWXZČĎǦƝƩŤŽ'
liquid = 'jlr'
nasal = 'mnɲ'
obstruents = 'bcdfghkpqstvwxzčďǧʃťž'    

# print(peldak)
peldak_orig = conv.degemination(peldak)
#print('orig______', peldak_orig)

peldak_fast = conv.fast_degemination(peldak)
#print('fast______', peldak_fast)
# HACK although I hope it works fast AF



