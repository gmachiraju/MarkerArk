from snorkel.snorkel import *
from snorkel.snorkel.snorkel import *
from snorkel.snorkel.candidates import Ngrams
import BiomarkerMatcher
import LevelsMatcher

def generateRelations(sentences):
    biomarker_ngrams = Ngrams(n_max=1)
    levels_ngrams = Ngrams(n_max=15)

    # Retrieve Matchers:
    BM = BiomarkerMatcher.getBiomarkerMatcher()
    L = LevelsMatcher.getLevelsMatcher()

    CandidateExtractor_BM = CandidateExtractor(biomarker_ngrams, BM)
    CandidateExtractor_L = CandidateExtractor(levels_ngrams, L)

    # Create Relations Object
    possiblePairs = Relations(
        sentences, CandidateExtractor_BM, CandidateExtractor_L)

    return possiblePairs
