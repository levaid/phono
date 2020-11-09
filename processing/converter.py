import re

class PhonemeConverter():
    def __init__(self):
        #kapcsolók
        #sentence = ''
        pass


    def process_orig(self, sentence: str):
        sentence = self.fast_double_letters(sentence)
        sentence = self.degemination(sentence)
        sentence = self.l_assimilation(sentence)
        sentence = self.n_assimilation(sentence)
        sentence = self.nasalisation(sentence)
        sentence = self.palatal_assimilation(sentence)
        sentence = self.sibilant_assimilation(sentence)
        sentence = self.voice_assimilation(sentence)
        sentence = self.hiatus_filling(sentence)
        sentence = self.n_nasalization(sentence)
        return(sentence)

    def process(self, sentence: str):
        sentence = self.fast_double_letters(sentence)

        sentence = self.degemination(sentence)
        sentence = self.fast_degemination(sentence)

        sentence = self.n_assimilation(sentence)
        sentence = self.fast_n_assimilation(sentence)

        sentence = self.palatal_assimilation(sentence)
        sentence = self.fast_palatal_assimilation(sentence)

        sentence = self.sibilant_assimilation(sentence)
        sentence = self.fast_sibilant_assimilation(sentence)

        sentence = self.voice_assimilation(sentence)
        sentence = self.fast_voice_assimilation(sentence)

        sentence = self.nasalisation(sentence)
        sentence = self.fast_nasalisation(sentence)

        sentence = self.hiatus_filling(sentence)
        sentence = self.n_nasalization(sentence)
        sentence = self.l_assimilation(sentence)

        return(sentence)

    def fast_process(self, sentence: str):

        sentence = self.fast_double_letters(sentence)
        sentence = self.fast_degemination(sentence)
        sentence = self.fast_n_assimilation(sentence)
        sentence = self.fast_palatal_assimilation(sentence)
        sentence = self.fast_sibilant_assimilation(sentence)
        sentence = self.fast_voice_assimilation(sentence)
        sentence = self.fast_voice_assimilation(sentence)
        sentence = self.fast_nasalisation(sentence)
        sentence = self.hiatus_filling(sentence)
        sentence = self.n_nasalization(sentence)
        sentence = self.l_assimilation(sentence)

        return(sentence)



    def optimal_process(self, sentence: str):
        
        sentence = self.fast_double_letters(sentence)
        sentence = self.fast_degemination(sentence)
        sentence = self.fast_n_assimilation(sentence)
        sentence = self.fast_palatal_assimilation(sentence)
        sentence = self.fast_sibilant_assimilation(sentence)
        sentence = self.fast_voice_assimilation(sentence)
        sentence = self.fast_voice_assimilation(sentence)
        sentence = self.fast_nasalisation(sentence)
        sentence = self.fast_stronger_long_letters(sentence)
        sentence = self.hiatus_filling(sentence)
        sentence = self.n_nasalization(sentence)
        sentence = self.l_assimilation(sentence)
        sentence = self.fast_degemination(sentence)
        sentence = self.fast_n_assimilation(sentence)
        sentence = self.fast_palatal_assimilation(sentence)
        sentence = self.fast_sibilant_assimilation(sentence)
        sentence = self.fast_voice_assimilation(sentence)
        sentence = self.fast_voice_assimilation(sentence)
        sentence = self.fast_nasalisation(sentence)
        sentence = self.fast_stronger_long_letters(sentence)

        sentence = self.hiatus_filling(sentence)
        sentence = self.n_nasalization(sentence)
        sentence = self.l_assimilation(sentence)
        sentence = self.fast_degemination(sentence)
        sentence = self.fast_n_assimilation(sentence)
        sentence = self.fast_palatal_assimilation(sentence)
        sentence = self.fast_sibilant_assimilation(sentence)
        sentence = self.fast_voice_assimilation(sentence)
        sentence = self.fast_voice_assimilation(sentence)
        sentence = self.fast_nasalisation(sentence)
        sentence = self.hiatus_filling(sentence)
        sentence = self.n_nasalization(sentence)
        sentence = self.l_assimilation(sentence)
        sentence = self.fast_stronger_long_letters(sentence)

        sentence = self.fast_degemination(sentence)
        sentence = self.fast_n_assimilation(sentence)
        sentence = self.fast_palatal_assimilation(sentence)
        sentence = self.fast_sibilant_assimilation(sentence)
        sentence = self.fast_voice_assimilation(sentence)
        sentence = self.fast_voice_assimilation(sentence)
        sentence = self.fast_nasalisation(sentence)
        sentence = self.hiatus_filling(sentence)
        sentence = self.n_nasalization(sentence)
        sentence = self.l_assimilation(sentence)

        return(self.fast_long_letters(sentence))


    def fast_long_letters(self, sentence: str):
        sentence = re.sub(r'([bcdfghjklmnpqrstvxzčďǧɲʃťž])\1', lambda m: m.group(1).upper(), sentence) # HACK HACK HACK
        return(sentence)
    
    def fast_stronger_long_letters(self, sentence: str):
        sentence = re.sub(r'([bcdfghjklmnpqrstvxzčďǧɲʃťž])[|~§#]?\1', lambda m: m.group(1).upper(), sentence) # HACK HACK HACK
        return(sentence)


    def fast_double_letters(self, sentence: str):
        double_long = [('ccs','Č'),('ddz','Ď'),('ggy','Ǧ'),('lly','J'),('nny','Ɲ'),('ssz','Ʃ'),('tty','Ť'),('zzs','Ž')]
        double = [('cs','č'),('dz','ď'),('gy','ǧ'),('ly','j'),('ny','ɲ'),('sz','ʃ'),('ty','ť'),('zs','ž')]
        for old, new in double_long + double:
            sentence = sentence.replace(old, new)

        sentence = self.fast_long_letters(sentence)

        return(sentence)


    def l_assimilation(self, sentence: str):
        sentence = re.sub(r'[lL][|§#~]?r', r'R', sentence)
        return(self.fast_double_letters(sentence))


    def nasalisation(self, sentence: str):
        sentence = re.sub(r'(n)([|~§#]?[pbfv])',r'm\g<2>',sentence)
        sentence = re.sub(r'(n)([|~§#]?[ǧť])',r'ɲ\g<2>',sentence)
        sentence = re.sub(r'(n)([|~§#]?ɲ)',r'Ɲ',sentence)
        return(self.fast_double_letters(sentence))

    def fast_nasalisation(self, sentence: str):
        pairs = {'p': 'm', 'b': 'm', 'f': 'm', 'v': 'm', 'ǧ': 'ɲ', 'ť': 'ɲ'}
        sentence = re.sub(r'n([|~§#]?)([pbfvǧť])', lambda m: pairs[m.group(2)]+m.group(1)+m.group(2), sentence)
        sentence = re.sub(r'(n)([|~§#]?ɲ)',r'Ɲ',sentence)
        return(self.fast_long_letters(sentence))


    def n_assimilation(self, sentence: str):
        sentence = re.sub(r'(n)([|~§]?l)',r'L',sentence)
        sentence = re.sub(r'(n)([|~§]?r)',r'R',sentence)
        return(self.fast_double_letters(sentence))

    def fast_n_assimilation(self, sentence: str):
        sentence = re.sub(r'n[|~§]?([lr])', lambda m: m.group(1).upper(), sentence)
        return(self.fast_long_letters(sentence))


    def sibilant_assimilation(self, sentence: str):
        sentence = re.sub(r'(t)([|~§#]?ʃ)',r'C',sentence)
        #sentence = re.sub(r'(d)([|~§]?z)',r'R',sentence) is 'dz' long or not in every situation?
        sentence = re.sub(r'(t)([|~§#]?s)',r'Č',sentence)
        sentence = re.sub(r'(t)([|~§# ]?c)',r'C',sentence)
        sentence = re.sub(r'(t)([|~§# ]?č)',r'Č',sentence)
        sentence = re.sub(r'(d)([|~§#]?ʃ)',r'C',sentence)
        sentence = re.sub(r'(d)([|~§#]?s)',r'Č',sentence)
        return(self.fast_long_letters(sentence))

    def fast_sibilant_assimilation(self, sentence: str):
        sentence = re.sub(r'(t)([|~§#]?ʃ)',r'C',sentence)
        #sentence = re.sub(r'(d)([|~§]?z)',r'R',sentence) is 'dz' long or not in every situation?
        sentence = re.sub(r'(t)([|~§#]?s)',r'Č',sentence)
        sentence = re.sub(r'(t)([|~§# ]?c)',r'C',sentence)
        sentence = re.sub(r'(t)([|~§# ]?č)',r'Č',sentence)
        sentence = re.sub(r'(d)([|~§#]?ʃ)',r'C',sentence)
        sentence = re.sub(r'(d)([|~§#]?s)',r'Č',sentence)
        return(self.fast_long_letters(sentence))

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

        return(self.fast_double_letters(sentence))

    def fast_voice_assimilation(self, sentence: str):
        voiced = 'bdǧgzžď'
        voiceless = 'ptťkʃscf'
        pairs = {'p':'b','b':'p','t':'d','d':'t','ť':'ǧ','ǧ':'ť','k':'g','g':'k','f':'v','v':'f','ʃ':'z','z':'ʃ','s':'ž','ž':'s','c':'ď','ď':'c'} #cs/dzs
        
        sentence = re.sub(r'([bdǧgzžďv])([|~§#]?[ptťkʃscfh])', lambda m: pairs[m.group(1)]+m.group(2), sentence) # HACK h

        sentence = re.sub(r'([ptťkʃscf])([|~§#]?[bdǧgzžď])', lambda m: pairs[m.group(1)]+m.group(2), sentence) # HACK h

        return(self.fast_long_letters(sentence))


    def palatal_assimilation(self, sentence: str):
        full = [('ǧ','j','Ǧ'),('d','j','Ǧ'),('l','j','J'),('n','j','Ɲ'),('ɲ','j','Ɲ'),('t','j','Ť'),('ť','j','Ť')]
        partial = [('d','ǧ','Ǧ'),('t','ǧ','Ǧ'),('d','ť','Ť'),('t','ť','Ť')]
        optional = [('d','ɲ','ǧɲ'),('t','ɲ','ťɲ')]

        for first,second,replace in full:
            sentence = re.sub(f'{first}([|~§#]?{second})',replace,sentence)

        for first,second,replace in partial+optional:
            sentence = re.sub(f'{first}([|~§# ]?{second})',replace,sentence)

        return(self.fast_long_letters(sentence))

    def fast_palatal_assimilation(self, sentence: str):
        full = [('ǧ','j','Ǧ'),('d','j','Ǧ'),('l','j','J'),('n','j','Ɲ'),('ɲ','j','Ɲ'),('t','j','Ť'),('ť','j','Ť')]
        partial = [('d','ǧ','Ǧ'),('t','ǧ','Ǧ'),('d','ť','Ť'),('t','ť','Ť')]
        optional = [('d','ɲ','ǧɲ'),('t','ɲ','ťɲ')]

        full_dict = {'ǧ': 'Ǧ', 'd': 'Ǧ', 'l': 'J', 'n': 'Ɲ', 'ɲ': 'Ɲ', 't': 'Ť', 'ť': 'Ť'}
        # partial is [dt][ǧť] and the second is upper
        optional_dict = {'d': 'ǧɲ', 't': 'ťɲ'}
        

        sentence = re.sub(r'([ǧdlnɲtť])[|~§#]?j', lambda m: full_dict[m.group(1)], sentence)

        sentence = re.sub(r'[dt][|~§# ]?([ǧť])', lambda m: m.group(1).upper(), sentence)

        sentence = re.sub(r'([dt])[|~§# ]?ɲ', lambda m: optional_dict[m.group(1)], sentence)

        return(self.fast_long_letters(sentence))

    def hiatus_filling(self, sentence: str):
        vowels = 'aáeéoóöőüűuú'
        sentence = re.sub(f'i[|~§]?([{vowels}])',r'ij\g<1>',sentence)
        sentence = re.sub(f'([{vowels}])i[|~§]?',r'\g<1>ji',sentence)
        return(sentence)

    
    def n_nasalization(self, sentence: str):
        sentence = re.sub(r'n[|~§#]?([gk])',r'ŋ\g<1>',sentence)
        return(self.fast_double_letters(sentence))


    def degemination(self, sentence: str):
        consonants = 'bcdfghjklmnpqrstvwxzčďǧɲʃťž'
        long_consonants = 'BCDFGHJKLMNPQRSTVWXZČĎǦƝƩŤŽ'
        liquid = 'jlr'
        nasal = 'mnɲ'
        obstruents = 'bcdfghkpqstvwxzčďǧʃťž'                


        for cons in long_consonants: #192B
            sentence = re.sub(f'{cons}[|§~# ]?([{consonants}])',cons.lower()+r' \g<1>',sentence)
        
        for cons in consonants: #192C
            sentence = re.sub(f'([{consonants}]{cons})[|#§~ ]{cons}',r'\g<1>',sentence)

        for cons in long_consonants:
            sentence = re.sub(f'([{consonants}]){cons}',r'\g<1>'+cons.lower(),sentence)

        for cons in consonants: #192D
            sentence = re.sub(f'{cons}[|~#§ ]({cons}[{obstruents}])',r'\g<1>',sentence)

        for cons in long_consonants:
            sentence = re.sub(f'{cons}([{obstruents}])',cons.lower()+r'\g<1>',sentence)

        for cons in consonants: #optional
            sentence = re.sub(f'{cons}[|~#§ ]({cons}[{nasal}])',r'\g<1>',sentence)

        for cons in long_consonants:
            sentence = re.sub(f'{cons}([{nasal}])',cons.lower()+r'\g<1>',sentence)

        

        return(self.fast_long_letters(sentence))

    def fast_degemination(self, sentence: str):

        consonants = 'bcdfghjklmnpqrstvwxzčďǧɲʃťž'
        long_consonants = 'BCDFGHJKLMNPQRSTVWXZČĎǦƝƩŤŽ'
        liquid = 'jlr'
        nasal = 'mnɲ'
        obstruents = 'bcdfghkpqstvwxzčďǧʃťž'                


        # print(re.findall(r'([BCDFGHJKLMNPQRSTVWXZČĎǦƝƩŤŽ])[|§~# ]?([bcdfghjklmnpqrstvwxzčďǧɲʃťž])', sentence))
        sentence = re.sub(r'([BCDFGHJKLMNPQRSTVWXZČĎǦƝƩŤŽ])([|§~# ]?)([bcdfghjklmnpqrstvwxzčďǧɲʃťž])', lambda m: m.group(1).lower()+m.group(2)+m.group(3),sentence)

        # print(re.findall(r'([bcdfghjklmnpqrstvwxzčďǧɲʃťž]([bcdfghjklmnpqrstvwxzčďǧɲʃťž]))[|#§~ ]\2', sentence))
        sentence = re.sub(r'([bcdfghjklmnpqrstvwxzčďǧɲʃťž]([bcdfghjklmnpqrstvwxzčďǧɲʃťž]))[|#§~ ]\2',r'\g<1>', sentence)
        # print('after______', sentence)

        # print(re.findall(r'([bcdfghjklmnpqrstvwxzčďǧɲʃťž])([BCDFGHJKLMNPQRSTVWXZČĎǦƝƩŤŽ])', sentence))
        sentence = re.sub(r'([bcdfghjklmnpqrstvwxzčďǧɲʃťž])[|~#§]([BCDFGHJKLMNPQRSTVWXZČĎǦƝƩŤŽ])', lambda m: m.group(1)+m.group(2).lower(), sentence)

        # print(re.findall(r'([bcdfghjklmnpqrstvwxzčďǧɲʃťž])[|~#§ ](\1[bcdfghkpqstvwxzčďǧʃťž])', sentence))
        sentence = re.sub(r'([bcdfghjklmnpqrstvwxzčďǧɲʃťž])[|~#§ ](\1[bcdfghkpqstvwxzčďǧʃťž])',r'\g<2>',sentence)
        
        # print(re.findall(r'([BCDFGHJKLMNPQRSTVWXZČĎǦƝƩŤŽ])([bcdfghkpqstvwxzčďǧʃťž])', sentence))
        sentence = re.sub(r'([BCDFGHJKLMNPQRSTVWXZČĎǦƝƩŤŽ])([bcdfghkpqstvwxzčďǧʃťž])', lambda m: m.group(1).lower()+m.group(2),sentence)

        # print(re.findall(r'([bcdfghjklmnpqrstvwxzčďǧɲʃťž])[|~#§ ](\1[mnɲ])', sentence))
        sentence = re.sub(r'([bcdfghjklmnpqrstvwxzčďǧɲʃťž])[|~#§ ](\1[mnɲ])',r'\g<2>',sentence) # optional

        # print(re.findall(r'([BCDFGHJKLMNPQRSTVWXZČĎǦƝƩŤŽ])([mnɲ])', sentence))
        sentence = re.sub(r'([BCDFGHJKLMNPQRSTVWXZČĎǦƝƩŤŽ])([mnɲ])',lambda m: m.group(1).lower()+m.group(2),sentence)


        return(self.fast_long_letters(sentence))


    def ipaization(self, sentence: str):
        ipa_sentence = ''
        ipa = {'a':'ɒ', 'á':'aː', 'b':'b', 'c':'t͡s', 'č':'t͡ʃ', 'd':'d', 'ď':'d͡z', 'e':'ɛ', 'é':'eː', 'f':'f', 'g':'ɡ', 'ǧ':'ɟ', 'h':'h', 'i':'i', 'í':'iː', 'j':'j', 'k':'k', 'l':'l', 'ly':'j', 'm':'m', 'n':'n', 'ɲ':'ɲ', 'o':'o', 'ó':'oː', 'ö':'ø', 'ő':'øː', 'p':'p', 'q':'k', 'r':'r', 's':'ʃ', 'ʃ':'s', 't':'t', 'ť':'c', 'u':'u', 'ú':'uː', 'ü':'y', 'ű':'yː', 'v':'v', 'w':'v', 'x':'ks', 'y':'i', 'z':'z', 'ž':'ʒ', 'B':'bː', 'C':'t͡sː', 'Č':'t͡ʃː', 'D':'dː', 'Ď':'d͡zː', 'F':'fː', 'G':'ɡː', 'Ǧ':'ɟː', 'H':'hː', 'J':'jː', 'K':'kː', 'L':'lː', 'ly':'j', 'M':'mː', 'N':'nː', 'Ɲ':'ɲː', 'P':'pː', 'Q':'kː', 'R':'rː', 'S':'ʃː', 'Ʃ':'sː', 'T':'tː', 'Ť':'cː', 'V':'vː', 'W':'vː', 'X':'ksː', 'Z':'zː', 'Ž':'ʒː' }
        #'dzs':'d͡ʒ',
        sentence = self.fast_long_letters(re.sub(r'[|~§#]', '', sentence))
        for letter in sentence:
            ipa_sentence += ipa.get(letter, letter)

        return(ipa_sentence)




