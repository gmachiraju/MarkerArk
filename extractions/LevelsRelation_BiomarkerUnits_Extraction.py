from snorkel.snorkel.snorkel import *
from snorkel.snorkel.candidates import Ngrams
import BiomarkerMatcher, UnitsMatcher

def generateRelations(sentences):
    biomarker_ngrams = Ngrams(n_max=1)
    unit_ngrams = Ngrams(n_max=10)

    # Retrieve Matchers:
    BM = BiomarkerMatcher.getBiomarkerMatcher()
    U = UnitsMatcher.getUnitsMatcher()

    CandidateExtractor_BM = CandidateExtractor(biomarker_ngrams, BM)
    CandidateExtractor_U = CandidateExtractor(unit_ngrams, U)

    # Create Relations Object
    possiblePairs = Relations(sentences, CandidateExtractor_BM, CandidateExtractor_U)

    return possiblePairs
