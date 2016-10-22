import cPickle
from snorkel.snorkel.parser import *
from snorkel.snorkel.snorkel import *
import  BiomarkerMatcher
import  DiseaseMatcher
from snorkel.snorkel.candidates import Ngrams
import doc_parser
import MediumMatcher

def generateRelations(filename):
    # Processing the input data and converting to sentences

    # If the file has already been parsed, there is no point in reparsing.
    # Just open the already parsed sentences
    pckl_f = "cache/" + filename + "/" + 'sentences.pkl'
    # try:
    #     #Try to see if the sentences have been parsed
    #     with open(pckl_f, 'rb') as f:
    #         #Load em in if they have
    #         sentences = cPickle.load(f)
    # except:
    sentences = doc_parser.parseDoc(filename)

    # Serialize so that you dont have to deal with parsing in the future
    # if not os.path.exists("cache/" + _filename +"/" ):
    #     os.makedirs("cache/" + _filename + "/")
    # with open(pckl_f, 'w+') as f:
    #     cPickle.dump(sentences, f)

    biomarker_ngrams = Ngrams(n_max=1)
    medium_ngrams = Ngrams(n_max=3)

    #Create the two matchers who have been defined in separate classes
    BM = BiomarkerMatcher.getBiomarkerMatcher()
    CandidateExtractor_BM = CandidateExtractor(biomarker_ngrams, BM)
    MM = MediumMatcher.getMediumMatcher()
    CandidateExtractor_MM = CandidateExtractor(medium_ngrams, MM)

    #Create the relations using the two matchers
    possiblePairs = Relations(sentences, CandidateExtractor_BM, CandidateExtractor_MM)
    return possiblePairs