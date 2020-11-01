import os, gzip
import json
import re
from collections import defaultdict

class Transciber():
    def __init__(self):  
        #fname = 'data/2017_2018_0001.tsv.gz'
        self.MAIN_POS = {'/V', '/N', '/Adj', '/Adv'}


    def transcibe(self,infilename: str, outfilename: str):
        with gzip.open(infilename, 'rt') as infile, gzip.open(outfilename,'wt') as outfile:
            tag_dict = defaultdict(int)
            for i, line in enumerate(infile):
                if line == '\n':
                    outfile.write('\n')
                if not line.startswith('#'):
                    splitted_line = line.split('\t')
                    if len(splitted_line) == 4 and i != 0:
                        anas = json.loads(splitted_line[1])
                        anas_sorted = [x['morphana'] for x in sorted(anas, key = lambda s: s['morphana'].count('+'), reverse = True) ]
                        if anas_sorted == [] or anas_sorted == ['']:
                            outfile.write(splitted_line[0].lower() + ' ')
                        else:
                            tags, morphs, _ = zip(*re.findall(r"\[(.*?)\]=(.*?)(\+|$)", anas_sorted[0]))
                            morphs = [x.lower() for x in morphs]
                            if len(morphs) == 1:
                                outfile.write(morphs[0] + ' ')
                                pass
                            else:
                                word_to_print = []
                                is_end_of_main = False
                                for i in range(len(morphs)-1):
                                    word_to_print.append(morphs[i])
                                    if morphs[i+1] == '':
                                        continue #to avoid empty | in the end
                                    curr_is_main, next_is_main = tags[i] in self.MAIN_POS, tags[i+1] in self.MAIN_POS
                                    if is_end_of_main:
                                        word_to_print.append('|')
                                    elif curr_is_main and next_is_main:
                                        word_to_print.append('#')
                                    elif not curr_is_main and next_is_main:
                                        word_to_print.append('§')
                                    elif curr_is_main and not next_is_main:
                                        word_to_print.append('~')
                                        is_end_of_main = True
                                    elif not curr_is_main and not next_is_main:
                                        word_to_print.append('|')

                                else:
                                    if morphs[-1] != '':
                                        word_to_print.append(morphs[-1])
                                outfile.write(''.join(word_to_print) + ' ')
                                
                #if i >= 8:
                    #break


