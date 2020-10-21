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
peldak = 'balra, modellre, széngyűrű, szén|pénz, verssel, kardja, hangya, ajánlat, tanrész, döfj, fúrj, szívből, hatvan, pechből, adhat, metszet, jutsz, kétség,'\
 'fűtsd, hat cica, kalapot cserél, ötödször, fáradtság, dobtam, képzés, adhat, hétből, edzhet, ketrecben, fogtam, zsákból, ágytól, pintyből, szívtam, széfben, méztől,'\
     ' mészből, rúzstól, hasba, hatvan, korccsal, rontson, koszttól, direkttermő, tankként, combból, talppont, szerb bor, sztrájkkor, sért talán, verssel, ponttá,'\
         'akttal, küldte, rajzzon, kardja, nagyja, adja, tolja, unja, hányja, látja, atyja, folyjon, hadgyakorlat, nemzetgyúlés, vadtyúk, hat tyúk, lúdnyak, átnyúlik'\
             ' hallva, vers|sel'
peldak = conv.double_letters(peldak)
peldak = conv.process(peldak)
peldak = conv.process(peldak)
print(conv.ipaization(peldak))




