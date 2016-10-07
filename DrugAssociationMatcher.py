from snorkel.ddlite import *
from snorkel.snorkel.matchers import *
import pickle

def getDrugAssociationMatcher():

    with open('databases/drugDatabase.pickle', 'rb') as f:
        drugDictionary = pickle.load(f)

    DrugMatch = DictionaryMatch(label = "Drug", d = drugDictionary, ignore_case = True)

    return DrugMatch

