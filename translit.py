#!/usr/bin/env python3

import re
import json
from lark import Transformer

with open('terminals.json') as fh:
    TERMINALS = json.load(fh)

class Gdpi(Transformer):
    """Convert Teochew pengim parse tree to Gengdang Pêng'im"""

    def NASAL(self, value):
        return('n')

    def initial(self, items):
        trdict = { term : TERMINALS['initials'][term]['gdpi'] for term in TERMINALS['initials'] if 'gdpi' in TERMINALS['initials'][term] }
        return(trdict[items[0].type])

    def medial(self, items):
        trdict = { term : TERMINALS['medials'][term]['gdpi'] for term in TERMINALS['medials'] if 'gdpi' in TERMINALS['medials'][term] }
        return(trdict[items[0].type])

    def coda(self, items):
        return("".join([str(i) for i in items]))

    def codastops(self, items):
        trdict = { term : TERMINALS['codastops'][term]['gdpi'] for term in TERMINALS['codastops'] if 'gdpi' in TERMINALS['codastops'][term] }
        trdict['COD_T'] = 'g' # Gengdang Pêng'im does not have stop -t
        return(trdict[items[0].type])

    def codanasal(self, items):
        trdict = { term : TERMINALS['codanasals'][term]['gdpi'] for term in TERMINALS['codanasals'] if 'gdpi' in TERMINALS['codanasals'][term] }
        trdict['COD_N'] = "ng" # Gengdang Pêng'im does not have coda n
        return(trdict[items[0].type])

    def final(self, items):
        return("".join([str(i) for i in items]))

    def tone(self, items):
        if len(items) == 1:
            return(str(items[0]))
        elif len(items) == 2:
            return(str(items[0]) + "(" + str(items[1]) + ")")
        else:
            return("")

    def syllable_tone(self, items):
        return("".join([str(i) for i in items]))

    def syllable_toneless(self, items):
        return("".join([str(i) for i in items]))

    def word_sep(self, items):
        return("".join(items))

    def sentence(self, items):
        return("".join(items))


class Ggnn(Transformer):
    """Convert Teochew pengim parse tree to Gaginang Peng'im"""

    def NASAL(self, value):
        return('ñ')

    def initial(self, items):
        trdict = { term : TERMINALS['initials'][term]['ggnn'] for term in TERMINALS['initials'] if 'ggnn' in TERMINALS['initials'][term] }
        return(trdict[items[0].type])

    def medial(self, items):
        trdict = { term : TERMINALS['medials'][term]['ggnn'] for term in TERMINALS['medials'] if 'ggnn' in TERMINALS['medials'][term] }
        return(trdict[items[0].type])

    def coda(self, items):
        return("".join([str(i) for i in items]))

    def codastops(self, items):
        trdict = { term : TERMINALS['codastops'][term]['ggnn'] for term in TERMINALS['codastops'] if 'ggnn' in TERMINALS['codastops'][term] }
        return(trdict[items[0].type])

    def codanasal(self, items):
        trdict = { term : TERMINALS['codanasals'][term]['ggnn'] for term in TERMINALS['codanasals'] if 'ggnn' in TERMINALS['codanasals'][term] }
        return(trdict[items[0].type])

    def final(self, items):
        return("".join([str(i) for i in items]))

    def tone(self, items):
        if len(items) == 1:
            return(str(items[0]))
        elif len(items) == 2:
            return(str(items[0]) + "(" + str(items[1]) + ")")
        else:
            return("")

    def syllable_tone(self, items):
        return("".join([str(i) for i in items]))

    def syllable_toneless(self, items):
        return("".join([str(i) for i in items]))

    def word_sep(self, items):
        return("".join(items))

    def sentence(self, items):
        return("".join(items))


class Tlo(Transformer):
    """Convert Teochew pengim parse tree to Tie-lo"""

    def NASAL(self, value):
        return('nn')

    def SYLLABLE_SEP(self, value):
        # Change all syllable separators to hyphens
        return('-')

    def initial(self, items):
        trdict = {
            'INIT_BH' : "b",
            'INIT_P'  : "ph",
            'INIT_B'  : "p",
            'INIT_M'  : "m",
            'INIT_NG' : "ng",
            'INIT_N'  : "n",
            'INIT_GH' : "g",
            'INIT_K'  : "kh",
            'INIT_G'  : "k",
            'INIT_D'  : "t",
            'INIT_T'  : "th",
            'INIT_Z'  : "ts",
            'INIT_C'  : "tsh",
            'INIT_S'  : "s",
            'INIT_H'  : "h",
            'INIT_R'  : "z",
            'INIT_L'  : "l",
        }
        return(trdict[items[0].type])

    def medial(self, items):
        trdict = {
            'MED_AI'  : "ai" ,
            'MED_AU'  : "au" ,
            'MED_IA'  : "ia" ,
            'MED_IAU' : "iau" ,
            'MED_IEU' : "ieu" ,
            'MED_IOU' : "iou" ,
            'MED_IU'  : "iu" ,
            'MED_IE'  : "ie" ,
            'MED_IO'  : "io" ,
            'MED_OI'  : "oi" ,
            'MED_OU'  : "ou" ,
            'MED_UAI' : "uai" ,
            'MED_UA'  : "ua" ,
            'MED_UE'  : "ue" ,
            'MED_UI'  : "ui" ,
            'MED_A'   : "a" ,
            'MED_V'   : "ur" ,
            'MED_E'   : "e" ,
            'MED_I'   : "i" ,
            'MED_O'   : "o" ,
            'MED_U'   : "u",
        }
        return(trdict[items[0].type])

    def coda(self, items):
        return("".join([str(i) for i in items]))

    def codastops(self, items):
        trdict = {
            'COD_P' : "p",
            'COD_K' : "k",
            'COD_H' : "h",
            'COD_T' : 't',
        }
        return(trdict[items[0].type])

    def codanasal(self, items):
        trdict = {
            'COD_M' : "m",
            'COD_NG': "ng",
            'COD_N' : "n",
        }
        return(trdict[items[0].type])

    def final(self, items):
        return("".join([str(i) for i in items]))

    def tone(self, items):
        # Only return the citation tone
        return(str(items[0]))

    def syllable_tone(self, items):
        # Tie-lo is less straightforward because it marks
        # tones with diacritics
        trdict = {
            '1' : "",
            '2' : '\u0301',
            '3' : '\u0300',
            '4' : "",
            '5' : '\u0302',
            '6' : '\u0306',
            '7' : '\u0304',
            '8' : '\u0302',
            '0' : ""
        }
        # TODO put tone mark on first vowel letter else on first letter of final
        syllab = "".join(items[:-1]) # syllable without tone
        tone = items[-1]
        firstvowel = re.search(r'[aeiou]', syllab)
        if firstvowel:
            # put tone mark on first vowel letter
            inspos = firstvowel.span()[1]
            syllab = syllab[0:inspos] + trdict[tone] + syllab[inspos:]
        else:
            # no vowel in syllable, put on first character
            syllab = syllab[0] + trdict[tone] + syllab[1:]
        return(syllab)

    def syllable_toneless(self, items):
        return("".join([str(i) for i in items]))

    def word_sep(self, items):
        # replace all syllable separators with hyphens
        # and separate syllables with hyphens if no
        # syllable separator is present
        return('-'.join([i for i in items if i != '-']))

    def sentence(self, items):
        return("".join(items))


class Duffus(Transformer):
    """Convert Teochew pengim parse tree to Duffus system"""

    def NASAL(self, value):
        return('\u207f')

    def SYLLABLE_SEP(self, value):
        # Change all syllable separators to hyphens
        return('-')

    def initial(self, items):
        trdict = {
            'INIT_BH' : "b",
            'INIT_P'  : "ph",
            'INIT_B'  : "p",
            'INIT_M'  : "m",
            'INIT_NG' : "ng",
            'INIT_N'  : "n",
            'INIT_GH' : "g",
            'INIT_K'  : "kh",
            'INIT_G'  : "k",
            'INIT_D'  : "t",
            'INIT_T'  : "th",
            'INIT_Z'  : "ts",
            'INIT_C'  : "tsh",
            'INIT_S'  : "s",
            'INIT_H'  : "h",
            'INIT_R'  : "z",
            'INIT_L'  : "l",
        }
        return(trdict[items[0].type])

    def medial(self, items):
        trdict = {
            'MED_AI'  : "ai" ,
            'MED_AU'  : "au" ,
            'MED_IA'  : "ia" ,
            'MED_IAU' : "iau" ,
            'MED_IEU' : "ieu" ,
            'MED_IOU' : "iou" ,
            'MED_IU'  : "iu" ,
            'MED_IE'  : "ie" ,
            'MED_IO'  : "io" ,
            'MED_OI'  : "oi" ,
            'MED_OU'  : "ou" ,
            'MED_UAI' : "uai" ,
            'MED_UA'  : "ua" ,
            'MED_UE'  : "ue" ,
            'MED_UI'  : "ui" ,
            'MED_A'   : "a" ,
            'MED_V'   : "ṳ" ,
            'MED_E'   : "e" ,
            'MED_I'   : "i" ,
            'MED_O'   : "o" ,
            'MED_U'   : "u",
        }
        return(trdict[items[0].type])

    def coda(self, items):
        return("".join([str(i) for i in items]))

    def codastops(self, items):
        trdict = {
            'COD_P' : "p",
            'COD_K' : "k",
            'COD_H' : "h",
            'COD_T' : 't',
        }
        return(trdict[items[0].type])

    def codanasal(self, items):
        trdict = {
            'COD_M' : "m",
            'COD_NG': "ng",
            'COD_N' : "n",
        }
        return(trdict[items[0].type])

    def final(self, items):
        return("".join([str(i) for i in items]))

    def tone(self, items):
        # Only return the citation tone
        return(str(items[0]))

    def syllable_tone(self, items):
        # Tie-lo is less straightforward because it marks
        # tones with diacritics
        trdict = {
            '1' : "",
            '2' : '\u0301',
            '3' : '\u0300',
            '4' : "",
            '5' : '\u0302',
            '6' : '\u0303',
            '7' : '\u0304',
            '8' : '\u0307',
            '0' : ""
        }
        # TODO put tone mark on first vowel letter else on first letter of final
        syllab = "".join(items[:-1]) # syllable without tone
        tone = items[-1]
        firstvowel = re.search(r'[aeiou]', syllab)
        if firstvowel:
            # put tone mark on first vowel letter
            inspos = firstvowel.span()[1]
            syllab = syllab[0:inspos] + trdict[tone] + syllab[inspos:]
        else:
            # no vowel in syllable, put on first character
            syllab = syllab[0] + trdict[tone] + syllab[1:]
        return(syllab)

    def syllable_toneless(self, items):
        return("".join([str(i) for i in items]))

    def word_sep(self, items):
        # replace all syllable separators with hyphens
        # and separate syllables with hyphens if no
        # syllable separator is present
        return('-'.join([i for i in items if i != '-']))

    def sentence(self, items):
        return("".join(items))