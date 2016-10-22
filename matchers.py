from snorkel.snorkel.snorkel import *
from snorkel.snorkel.matchers import *
from snorkel.ddlite import *
import pickle
import sys

# These matchers are either based on Regex scans or DB matches via Snorkel

prefixes = [['Y', 'yotta'], ['Z', 'zetta'], ['E', 'exa'], ['P', 'peta'], ['T', 'tera'], ['G', 'giga'], ['M', 'mega'], ['k', 'kilo'], ['h', 'hecto'],
            ['da', 'deka'], ['d', 'deci'], ['c', 'centi'], ['\u03bc', 'micro'], ['n', 'nano'], ['p', 'pico'], ['f', 'femto'], ['a', 'atto'], ['z', 'zepto'], ['y', 'yocto']]
length_unit = ['m', 'meter']
area_unit = ['m2', 'square ', 'meter']
volume_unit = ['m3', 'cubic ', 'meter']
liquid_volume_unit = ['L', 'liter']
mass_unit = ['g', 'gram']
all_prefixes_units = [['Ym', 'yottameter'], ['Zm', 'zettameter'], ['Em', 'exameter'], ['Pm', 'petameter'], ['Tm', 'terameter'], ['Gm', 'gigameter'], ['Mm', 'megameter'], ['km', 'kilometer'], ['hm', 'hectometer'], ['dam', 'dekameter'], ['dm', 'decimeter'], ['cm', 'centimeter'], ['\\u03bcm', 'micrometer'], ['nm', 'nanometer'], ['pm', 'picometer'], ['fm', 'femtometer'], ['am', 'attometer'], ['zm', 'zeptometer'], ['ym', 'yoctometer'], ['Ym2', 'square yottameter'], ['Zm2', 'square zettameter'], ['Em2', 'square exameter'], ['Pm2', 'square petameter'], ['Tm2', 'square terameter'], ['Gm2', 'square gigameter'], ['Mm2', 'square megameter'], ['km2', 'square kilometer'], ['hm2', 'square hectometer'], ['dam2', 'square dekameter'], ['dm2', 'square decimeter'], ['cm2', 'square centimeter'], ['\\u03bcm2', 'square micrometer'], ['nm2', 'square nanometer'], ['pm2', 'square picometer'], ['fm2', 'square femtometer'], ['am2', 'square attometer'], ['zm2', 'square zeptometer'], ['ym2', 'square yoctometer'], ['Ym2', 'cubic yottameter'], ['Zm2', 'cubic zettameter'], ['Em2', 'cubic exameter'], ['Pm2', 'cubic petameter'], ['Tm2', 'cubic terameter'], ['Gm2', 'cubic gigameter'], [
    'Mm2', 'cubic megameter'], ['km2', 'cubic kilometer'], ['hm2', 'cubic hectometer'], ['dam2', 'cubic dekameter'], ['dm2', 'cubic decimeter'], ['cm2', 'cubic centimeter'], ['\\u03bcm2', 'cubic micrometer'], ['nm2', 'cubic nanometer'], ['pm2', 'cubic picometer'], ['fm2', 'cubic femtometer'], ['am2', 'cubic attometer'], ['zm2', 'cubic zeptometer'], ['ym2', 'cubic yoctometer'], ['YL', 'yottaliter'], ['ZL', 'zettaliter'], ['EL', 'exaliter'], ['PL', 'petaliter'], ['TL', 'teraliter'], ['GL', 'gigaliter'], ['ML', 'megaliter'], ['kL', 'kiloliter'], ['hL', 'hectoliter'], ['daL', 'dekaliter'], ['dL', 'deciliter'], ['cL', 'centiliter'], ['\\u03bcL', 'microliter'], ['nL', 'nanoliter'], ['pL', 'picoliter'], ['fL', 'femtoliter'], ['aL', 'attoliter'], ['zL', 'zeptoliter'], ['yL', 'yoctoliter'], ['Yg', 'yottagram'], ['Zg', 'zettagram'], ['Eg', 'exagram'], ['Pg', 'petagram'], ['Tg', 'teragram'], ['Gg', 'gigagram'], ['Mg', 'megagram'], ['kg', 'kilogram'], ['hg', 'hectogram'], ['dag', 'dekagram'], ['dg', 'decigram'], ['cg', 'centigram'], ['\\u03bcg', 'microgram'], ['ng', 'nanogram'], ['pg', 'picogram'], ['fg', 'femtogram'], ['ag', 'attogram'], ['zg', 'zeptogram'], ['yg', 'yoctogram']]
medium = ['blood', 'blood plasma', 'serum', 'urine', 'cell', 'saliva', 'amniotic fliud', 'tears', 'breast milk', 'vitreous humor', 'aqueous humor', 'cerebrospinal fluid', 'bile', 'cerumen', 'chyle', 'lymph', 'interstitial fluid', 'sera', 'ascites', 'CSF', 'sputum', 'bone marrow', 'synovial fluid', 'cerumen', 'broncheoalveolar lavage fluid', 'semen', 'postatic fluid', 'cowper\'s fluid',
          'pre-ejaculatory fluid', 'female ejaculate', 'sweat', 'feces', 'fecal matter', 'hair', 'cyst fluid', 'pleural fluid', 'peritoneal fluid', 'pericardinal fluid', 'chyme', 'menses', 'pus', 'sebum', 'vomit', 'vaginal secretion', 'stool water', 'pancreatic juice', 'pancreatic fluid', 'lavage fluids', 'bronchopulmonary aspirates', 'blastocyl cavity fluid', 'umbilical chord blood']


def getUnitsMatcher():
    unitsDatabase = all_prefixes_units
    unit_regex = RegexMatchEach(
        rgx=r'(?<=\s)[a-zA-Z]{1,2}[1-9]?(?=[\s\,\.])|(?<=\s)[a-zA-Z]{1,2}[1-9]?[\/]{1}[a-zA-Z]{1,2}[1-9]?(?=[\s\.\,])', ignore_case=False, attrib='words')
    return unit_regex


def getLevelsMatcher():
    normal_syntax_regex = RegexMatchEach(
        rgx=r'(?<=[^a-zA-Z:;])[0-9]+[-,\.]?[0-9]+', ignore_case=False, attrib='lemmas')
    range_syntax_regex = RegexMatchSpan(
        normal_syntax_regex, rgx=r'[0-9]+[\W^;]?[0-9]+\s[()][^\sa-zA-Z()]+[()]', ignore_case=False, attrib='text')
    return range_syntax_regex


def getMeasurementTypeMatcher():
    noun_regex = RegexMatchEach(
        rgx=r'[A-Z]?NN[A-Z]?', ignore_case=True, attrib='poses')
    complete_obj_regex = RegexMatchSpan(
        noun_regex, rgx=r'[J]{2,}\sNN[A-Z]?', ignore_case=True, attrib='poses')
    # CE = Union(noun_regex, complete_obj_regex)
    return complete_obj_regex


def getTestSetMatcher():
    noun_regex = RegexMatchEach(
        rgx=r'[A-Z]?NN[A-Z]?', ignore_case=True, attrib='poses')
    complete_obj_regex = RegexMatchSpan(
        noun_regex, rgx=r'[J]{2,}\sNN[A-Z]?', ignore_case=True, attrib='poses')
    return complete_obj_regex


def getDiseaseMatcher():
    with open('databases/diseaseAbbreviationsDatabase.pickle', 'rb') as f:
        diseaseAbb = pickle.load(f)

    with open('databases/diseaseDatabase.pickle', 'rb') as f:
        diseaseDictionary = pickle.load(f)

    DiseaseMatch = DictionaryMatch(d=diseaseDictionary, ignore_case=True)
    AbbMatch = DictionaryMatch(d=diseaseAbb, ignore_case=False)
    return Union(DiseaseMatch, AbbMatch)


def getDrugAssociationMatcher():
    with open('databases/drugDatabase.pickle', 'rb') as f:
        drugDictionary = pickle.load(f)

    DrugMatch = DictionaryMatch(
        label="Drug", d=drugDictionary, ignore_case=True)
    return DrugMatch


def getMediumMatcher():
    with open('databases/mediumDatabase.pickle', 'rb') as f:
        mediumDatabase = pickle.load(f)

    mediumMatcher = DictionaryMatch(d=mediumDatabase, ignore_case=True)
    return mediumMatcher

    # number of mentions of medium associated in biomarker (largest number of
    # mentions = medium)
    """
    max_name = None
    max_count = 0
    count = 0
    #print type(entities)
    while(count < len(entities)):
        numInstances = 0
        counter = count
        while(counter < len(entities) - 1):
            #print "ENTERED LOOP"
            if(entities[counter].mention(attribute="words") == entities[counter + 1].mention(attribute="words")):
                #print "FOUND A MATCH"
                numInstances += 1
            counter += 1
        if(numInstances > max_count):
            max_name = entities[count]
            max_count = numInstances
        count += 1
    return max_name.mention(attribute='words')
    """


def getBiomarkerTypeMatcher():
    with open('databases/typesDatabase.pickle', 'rb') as f:
        typeDatabase = pickle.load(f)

    typeMatcher = DictionaryMatch(d=typeDatabase, ignore_case=True)
    return typeMatcher


# Utility Functions:
#--------------------

def addDiseaseBases(EE, diseaseDictionary, final_article_str):
    counter = 0
    listCounter = 0
    wordIndex = 0
    currentPos = ''
    disease_candidates_edits = []

    for entity in EE:
        disease_index = entity.idxs[0]

        if disease_index is not 0:
            sentenceWords = entity.pre_window(
                attribute='words', n=disease_index)
            diseaseName = unicodedata.normalize('NFKD', ' '.join(
                entity.mention(attribute='words'))).encode('ascii', 'ignore')
            sentencePos = entity.pre_window(attribute='poses', n=disease_index)
            normalized_Pos = unicodedata.normalize(
                'NFKD', sentencePos[0]).encode('ascii', 'ignore')

            if normalized_Pos == 'CC':
                # get base of disease(tumor,cancer)
                disease_base = ' ' + \
                    entity.mention(attribute='words')[
                        len(entity.idxs) - 1] + ' '
                normalized_disease_base = unicodedata.normalize(
                    'NFKD', disease_base).encode('ascii', 'ignore')
                sentenceWords.reverse()
                joined_sentenceWords = ' '.join(sentenceWords)
                normalized_sentenceWords = unicodedata.normalize(
                    'NFKD', joined_sentenceWords).encode('ascii', 'ignore')
                normalized_unjoined_sentenceWords = []

                for sentence in sentenceWords:
                    normalized_sentence = unicodedata.normalize(
                        'NFKD', sentence).encode('ascii', 'ignore')
                    normalized_unjoined_sentenceWords.append(
                        normalized_sentence)

                cutSentence = ' '.join(sentenceWords[0:len(sentenceWords) - 1])
                normalized_cutSentence = unicodedata.normalize(
                    'NFKD', cutSentence).encode('ascii', 'ignore')
                sentenceIdx = substringIndex(
                    final_article_str, normalized_unjoined_sentenceWords)
                indicesOfAnd = [(m.start(0)) for m in re.finditer(
                    'and', normalized_sentenceWords)]
                numberOfCommas = len([(m.start(0)) for m in re.finditer(
                    ',', normalized_sentenceWords)])  # commas add one extra whitespace

                # add sentence Index + Index of And - 1 - number of commas
                editIdx = sentenceIdx + \
                    indicesOfAnd[len(indicesOfAnd) - 1] - numberOfCommas

                for disease_candidate in diseaseDictionary:
                    normalized_disease_candidate_name = unicodedata.normalize(
                        'NFKD', disease_candidate).encode('ascii', 'ignore')
                    if normalized_disease_candidate_name.lower() in (normalized_cutSentence + normalized_disease_base).lower():
                        disease_candidates_edits.append(
                            [editIdx, normalized_cutSentence, normalized_disease_base])  # EDITED
                        listCounter = listCounter + 1

        counter = counter + 1

    disease_candidates_edits = removeRepeats(disease_candidates_edits)
    disease_candidates_edits.sort()
    # reverse so that we edit the article back-front to avoid index errors
    disease_candidates_edits.reverse()
    counter = 0

    for edit in disease_candidates_edits:
        edit_str_addition = edit[2]
        edit_index = edit[0]
        final_article_str = final_article_str[
            0:edit_index] + edit_str_addition + final_article_str[edit_index:len(final_article_str)]
        counter = counter + 1

    return final_article_str


def substringIndex(text, listWords):
    end = -3
    candidate_index = -2
    word = listWords[0]
    allIndices = [m.start() for m in re.finditer(word, text)]

    for index in allIndices:
        end = substringIndex_help(text, listWords, index)

        if (end is not -1 and end is not None):
            candidate_index = index
            return candidate_index

    return candidate_index


def substringIndex_help(text, listWords, index):
    if len(listWords) is 0:
        return 0
    elif len(listWords) is 1:
        withinRange = text[index:index + 15 + len(listWords[0])]
        if listWords[0] in withinRange:
            index = withinRange.index(listWords[0])
            return substringIndex_help(text, [], index)
        else:
            return -1
    else:
        parsedPaper = text[index:]
        withinRange = text[index:index +
                           len(listWords[0]) + 15 + len(listWords[1])]
        if listWords[1] in withinRange:
            index = withinRange.index(listWords[1])
            return substringIndex_help(parsedPaper, listWords[1:], index)
        else:
            return -1


def removeRepeats(list):
    counter = 1
    case = None
    for edit in list:
        for check in list[counter:]:
            if edit[0] is check[0]:  # If the two objects have the same edit index
                list.remove(check)
            counter = counter + 1
    return list
