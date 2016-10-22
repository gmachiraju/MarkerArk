import DrugAssociationMatcher
import BiomarkerMatcher
from snorkel.snorkel.snorkel import *
from snorkel.snorkel.candidates import Ngrams
import doc_parser


def generateRelations(filename):

    # Processing the input data and converting to sentences
    sentences = doc_parser.parseDoc(filename)
    # If the file has already been parsed, there is no point in reparsing.
    # Just open the already parsed sentences

    # print sentences
    # Serialize so that you dont have to deal with parsing in the future
    # if not os.path.exists("cache/" + filename +"/" ):
    #     os.makedirs("cache/" + filename + "/")
    # with open(pckl_f, 'w+') as f:
    #     cPickle.dump(sentences, f)

    biomarker_ngrams = Ngrams(n_max=1)
    drug_association_ngrams = Ngrams(n_max=5)

    BM = BiomarkerMatcher.getBiomarkerMatcher()
    DAM = DrugAssociationMatcher.getDrugAssociationMatcher()

    CandidateExtractor_BM = CandidateExtractor(biomarker_ngrams, BM)
    CandidateExtractor_DAM = CandidateExtractor(drug_association_ngrams, DAM)

    possiblePairs = Relations(
        sentences, CandidateExtractor_BM, CandidateExtractor_DAM)

    return possiblePairs
