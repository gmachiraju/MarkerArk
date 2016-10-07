import pickle, sys

from snorkel.snorkel.matchers import *
#from databases import *
#sys.path.append('/Users/cameronbaab/Documents/Marker-Reader4')


def getBiomarkerTypeMatcher():

    with open('databases/typesDatabase.pickle', 'rb') as f:
        typeDatabase = pickle.load(f)
    typeMatcher = DictionaryMatch(d = typeDatabase, ignore_case = True)

    return typeMatcher
    """
    max_name = None
    max_count = 0
    count = 0
    #print type(entities)
    while(count < len(entities)):
        numInstances = 0
        counter = count
        while(counter < len(entities) - 1):
            if(entities[counter].mention(attribute="words") == entities[counter + 1].mention(attribute="words")):
                numInstances += 1
            counter += 1
        if(numInstances >= max_count):
            max_name = entities[count]
            max_count = numInstances
        count += 1
    return max_name.mention(attribute='words')
    """
