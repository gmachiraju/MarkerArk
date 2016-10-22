from snorkel.snorkel.snorkel import *
from snorkel.snorkel.candidates import Ngrams
import BiomarkerMatcher
import TestSetMatcher

def generateRelations(_sentences):
    sentences = _sentences
    biomarker_ngrams = Ngrams(n_max=1)
    test_set_ngrams = Ngrams(n_max=10)

    # Retrieve Matchers:
    BM = BiomarkerMatcher.getBiomarkerMatcher()
    TS = TestSetMatcher.getTestSetMatcher()

    CandidateExtractor_BM = CandidateExtractor(biomarker_ngrams, BM)
    CandidateExtractor_TS = CandidateExtractor(test_set_ngrams, TS)

    # Create Relations Object
    possiblePairs = Relations(
        sentences, CandidateExtractor_BM, CandidateExtractor_TS)

    return possiblePairs
