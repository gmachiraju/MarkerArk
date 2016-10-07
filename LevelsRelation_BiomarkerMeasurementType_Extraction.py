# imports
from snorkel.snorkel.snorkel import *
from snorkel.snorkel.candidates import Ngrams
import BiomarkerMatcher, MeasurementTypeMatcher

def generateRelations(_sentences):
    sentences = _sentences
    biomarker_ngrams = Ngrams(n_max=1)
    measurement_type_ngrams = Ngrams(n_max=5)

    # Retrieve Matchers:
    BM = BiomarkerMatcher.getBiomarkerMatcher()
    MT = MeasurementTypeMatcher.getMeasurementTypeMatcher()

    CandidateExtractor_BM = CandidateExtractor(biomarker_ngrams, BM)
    CandidateExtractor_MT = CandidateExtractor(measurement_type_ngrams, MT)

    # Create Relations Object
    possiblePairs = Relations(sentences, CandidateExtractor_BM, CandidateExtractor_MT)

    return possiblePairs
