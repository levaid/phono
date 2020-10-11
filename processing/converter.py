import re

class PhonemeConverter():
    def __init__(self):
        #kapcsolók
        #sentence = ''
        pass

    def convert(self, sentence: str):
        sentence = self.double_letters(sentence)
        return(sentence)

    def double_letters(self, sentence: str):
        double_long = [('ccs','\u010c'),('ddz','\u010e'),('ggy','\u01e6'),('lly','J'),('nny','\u019d'),('ssz','\u01a9'),('tty','\u0164'),('zzs','\u017d')]
        double = [('cs','\u010d'),('dz','\u010f'),('gy','\u01e7'),('ly','j'),('ny','\u0272'),('sz','\u0283'),('ty','\u0165'),('zs','\u017e')]
        single_long = [('bb','B'),('cc','C'),('dd','D'),('ff','F'),('gg','G'),('hh','H'),('jj','J'),('kk','K'),('ll','L'),
                       ('mm','M'),('nn','N'),('pp','P'),('rr','R'),('ss','S'),('tt','T'),('vv','V'),('zz','Z')]
        for old, new in double_long + double + single_long:
            sentence = sentence.replace(old, new)

        return(sentence)






