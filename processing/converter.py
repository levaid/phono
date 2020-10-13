import re

class PhonemeConverter():
    def __init__(self):
        #kapcsolók
        #sentence = ''
        pass

    def process(self, sentence: str):
        sentence = self.double_letters(sentence)
        sentence = self.l_assimilation(sentence)
        return(sentence)

    def double_letters(self, sentence: str):
        double_long = [('ccs','\u010c'),('ddz','\u010e'),('ggy','\u01e6'),('lly','J'),('nny','\u019d'),('ssz','\u01a9'),('tty','\u0164'),('zzs','\u017d')]
        double = [('cs','\u010d'),('dz','\u010f'),('gy','\u01e7'),('ly','j'),('ny','\u0272'),('sz','\u0283'),('ty','\u0165'),('zs','\u017e')]
        single_long = [('bb','B'),('cc','C'),('dd','D'),('ff','F'),('gg','G'),('hh','H'),('jj','J'),('kk','K'),('ll','L'),
                       ('mm','M'),('nn','N'),('pp','P'),('rr','R'),('ss','S'),('tt','T'),('vv','V'),('zz','Z')]
        for old, new in double_long + double + single_long:
            sentence = sentence.replace(old, new)
        return(sentence)

    def l_assimilation(self, sentence: str):
        sentence = re.sub(r'[lL][|§#~]?r', r'R', sentence)
        return(sentence)

    def nasalisation(self, sentence: str):
        sentence = re.sub(r'(n)([|~§#]?[pbfv])',r'm\g<2>',sentence)
        sentence = re.sub(r'(n)([|~§#]?[ǧť])',r'ɲ\g<2>',sentence)
        sentence = re.sub(r'(n)([|~§#]?ɲ)',r'Ɲ',sentence)
        return(sentence)

    def n_assimilation(self, sentence: str):
        sentence = re.sub(r'(n)([|~§]?l)',r'L',sentence)
        sentence = re.sub(r'(n)([|~§]?r)',r'R',sentence)
        return(sentence)

    def sibilant_assimilation(self, sentence: str):
        sentence = re.sub(r'(t)([|~§#]?ʃ)',r'C',sentence)
        #sentence = re.sub(r'(d)([|~§]?z)',r'R',sentence) is 'dz' long or not in every situation?
        sentence = re.sub(r'(t)([|~§#]?s)',r'Č',sentence)
        sentence = re.sub(r'(t)([|~§# ]?c)',r'C',sentence)
        sentence = re.sub(r'(t)([|~§# ]?č)',r'Č',sentence)
        sentence = re.sub(r'(d)([|~§#]?ʃ)',r'C',sentence)
        sentence = re.sub(r'(d)([|~t]?d)',r'Č',sentence)
        return(sentence)

    def voice_assimilation(self, sentence: str):
        voiced = 'bdǧgzžď'
        voiceless = 'ptťkʃscf'
        pairs = {'p':'b','b':'p','t':'d','d':'t','ť':'ǧ','ǧ':'ť','k':'g','g':'k','f':'v','v':'f','ʃ':'z','z':'ʃ','s':'ž','ž':'s','c':'ď','ď':'c'} #cs/dzs
        for letter in voiced + 'v':
            pattern = letter + r'([|~§#]?' + f'[{voiceless}h])' #HACK h
            sub = pairs[letter] + r'\g<1>'
            sentence = re.sub(pattern,sub,sentence)

        for letter in voiceless:
            pattern = letter + r'([|~§#]?' + f'[{voiced}])'
            sub = pairs[letter] + r'\g<1>'
            sentence = re.sub(pattern,sub,sentence)

        return(sentence)





