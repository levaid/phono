import os, gzip
import json
import re
from collections import defaultdict

def legfinomabb(t):
    
    d = json.loads(t)
    
    if False:
        for j in range(len(t)): 
            if t[j] == '"morphana":' and len(t[j+1].split('+')) > longest:
                longest = len(t[j+1].split('+'))
                final_morph = t[j+1]
    #print(longest)
    
        return(final_morph)


fname = 'data/2017_2018_0001.tsv.gz'
MAIN_POS = {'/V', '/N', '/Adj', '/Adv'}

with gzip.open(fname, 'rt') as f, gzip.open('testfile.txt.gz','wt') as outfile:
    tag_dict = defaultdict(int)
    for i, line in enumerate(f):
        if line == '\n':
            outfile.write('\n')
        if not line.startswith('#'):
            splitted_line = line.split('\t')
            if len(splitted_line) == 4 and i != 0:
                anas = json.loads(splitted_line[1])
                anas_sorted = [x['morphana'] for x in sorted(anas, key = lambda s: s['morphana'].count('+'), reverse = True) ]
                if anas_sorted == [] or anas_sorted == ['']:
                    outfile.write(splitted_line[0] + ' ')
                    #print(splitted_line[0])
                    #pass
                else:
                    tags, morphs, _ = zip(*re.findall(r"\[(.*?)\]=(.*?)(\+|$)", anas_sorted[0]))
                    morphs = [x.lower() for x in morphs]
                    if len(morphs) == 1:
                        outfile.write(morphs[0] + ' ')
                        #print(morphs[0]) 
                        pass
                    else:
                        #print(splitted_line[0])
                        word_to_print = []
                        is_end_of_main = False
                        for i in range(len(morphs)-1):
                            word_to_print.append(morphs[i])
                            if morphs[i+1] == '':
                                continue #to avoid empty | in the end
                            curr_is_main, next_is_main = tags[i] in MAIN_POS, tags[i+1] in MAIN_POS
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
            





        #if i >= 80:
            #break


### === CUPPPCSÓÓÓÓÓÓ === ###


