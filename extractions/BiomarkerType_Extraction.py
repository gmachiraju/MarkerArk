import BiomarkerMatcher
import BiomarkerTypeMatcher
from snorkel.snorkel.parser import *
from snorkel.snorkel.snorkel import *
from snorkel.snorkel.candidates import Ngrams
import doc_parser


def generateRelations(filename):
    """
    Processing the input data and converting to sentences
    """

    # If the file has already been parsed, there is no point in reparsing.
    # Just open the already parsed sentences
    # pckl_f = "cache/" + filename + "/" + 'sentences.pkl'
    # try:
    #     #Try to see if the sentences have been parsed
    #     with open(pckl_f, 'rb') as f:
    #         #Load em in if they have
    #         sentences = cPickle.load(f)
    # except:

    sentences = doc_parser.parseDoc(filename)

    # Serialize so that you dont have to deal with parsing in the future
    # if not os.path.exists("cache/" + filename +"/" ):
    #     os.makedirs("cache/" + filename + "/")
    # with open(pckl_f, 'w+') as f:
    #     cPickle.dump(sentences, f)

    biomarker_ngrams = Ngrams(n_max=1)
    biomarker_type_ngrams = Ngrams(n_max=2)

    BM = BiomarkerMatcher.getBiomarkerMatcher()
    TM = BiomarkerTypeMatcher.getBiomarkerTypeMatcher()

    CandidateExtractor_BM = CandidateExtractor(biomarker_ngrams, BM)
    CandidateExtractor_TM = CandidateExtractor(biomarker_type_ngrams, TM)

    possiblePairs = Relations(
        sentences, CandidateExtractor_BM, CandidateExtractor_TM)

    return possiblePairs
