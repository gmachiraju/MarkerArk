import pickle
import sys
from snorkel.snorkel.matchers import *


def getBiomarkerTypeMatcher():
    with open('databases/typesDatabase.pickle', 'rb') as f:
        typeDatabase = pickle.load(f)

    typeMatcher = DictionaryMatch(d=typeDatabase, ignore_case=True)
    return typeMatcher
