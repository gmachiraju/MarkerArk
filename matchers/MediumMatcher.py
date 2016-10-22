import pickle
from snorkel.snorkel.matchers import *

medium = ['blood', 'blood plasma', 'serum', 'urine', 'cell', 'saliva', 'amniotic fliud', 'tears', 'breast milk', 'vitreous humor', 'aqueous humor', 'cerebrospinal fluid', 'bile', 'cerumen', 'chyle', 'lymph', 'interstitial fluid', 'sera', 'ascites', 'CSF', 'sputum', 'bone marrow', 'synovial fluid', 'cerumen', 'broncheoalveolar lavage fluid', 'semen', 'postatic fluid', 'cowper\'s fluid',
          'pre-ejaculatory fluid', 'female ejaculate', 'sweat', 'feces', 'fecal matter', 'hair', 'cyst fluid', 'pleural fluid', 'peritoneal fluid', 'pericardinal fluid', 'chyme', 'menses', 'pus', 'sebum', 'vomit', 'vaginal secretion', 'stool water', 'pancreatic juice', 'pancreatic fluid', 'lavage fluids', 'bronchopulmonary aspirates', 'blastocyl cavity fluid', 'umbilical chord blood']


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
