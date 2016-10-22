from snorkel.snorkel import *
from snorkel.candidates import *
from snorkel.matchers import *
#-----------redundant by 1st import?-----------
from snorkel.snorkel.snorkel import *
from snorkel.snorkel.candidates import Ngrams
from snorkel.snorkel.parser import *
#----------------------------------------------
import doc_parser
import matchers
import cPickle
import pickle
import unicodedata


def biomarkerUnitsRelations(sentences):
    biomarker_ngrams = Ngrams(n_max=1)
    unit_ngrams = Ngrams(n_max=10)

    # Retrieve Matchers:
    BM = matchers.getBiomarkerMatcher()
    U = matchers.getUnitsMatcher()

    CandidateExtractor_BM = CandidateExtractor(biomarker_ngrams, BM)
    CandidateExtractor_U = CandidateExtractor(unit_ngrams, U)

    # Create Relations Object
    possiblePairs = Relations(
        sentences, CandidateExtractor_BM, CandidateExtractor_U)

    return possiblePairs


def biomarkerLevelsRelations(sentences):
    biomarker_ngrams = Ngrams(n_max=1)
    levels_ngrams = Ngrams(n_max=15)

    # Retrieve Matchers:
    BM = matchers.getBiomarkerMatcher()
    L = matchers.getLevelsMatcher()

    CandidateExtractor_BM = CandidateExtractor(biomarker_ngrams, BM)
    CandidateExtractor_L = CandidateExtractor(levels_ngrams, L)

    # Create Relations Object
    possiblePairs = Relations(
        sentences, CandidateExtractor_BM, CandidateExtractor_L)

    return possiblePairs


def biomarkerMeasurementRelations(sentences):
    biomarker_ngrams = Ngrams(n_max=1)
    measurement_type_ngrams = Ngrams(n_max=5)

    # Retrieve Matchers:
    BM = matchers.getBiomarkerMatcher()
    MT = matchers.getMeasurementTypeMatcher()

    CandidateExtractor_BM = CandidateExtractor(biomarker_ngrams, BM)
    CandidateExtractor_MT = CandidateExtractor(measurement_type_ngrams, MT)

    # Create Relations Object
    possiblePairs = Relations(
        sentences, CandidateExtractor_BM, CandidateExtractor_MT)

    return possiblePairs


def biomarkerTestsetRelations(sentences):
    biomarker_ngrams = Ngrams(n_max=1)
    test_set_ngrams = Ngrams(n_max=10)

    # Retrieve Matchers:
    BM = matchers.getBiomarkerMatcher()
    TS = matchers.getTestSetMatcher()

    CandidateExtractor_BM = CandidateExtractor(biomarker_ngrams, BM)
    CandidateExtractor_TS = CandidateExtractor(test_set_ngrams, TS)

    # Create Relations Object
    possiblePairs = Relations(
        sentences, CandidateExtractor_BM, CandidateExtractor_TS)

    return possiblePairs


def biomarkerDiseaseRelations(_filename):
    # Processing the input data and converting to sentences

    # If the file has already been parsed, there is no point in reparsing.
    # Just open the already parsed sentences
    #pckl_f = _filename
    # try:
    #     #Try to see if the sentences have been parsed
    # with open(pckl_f, 'rb') as f:
    #         #Load em in if they have
    #    sentences = pickle.load(f)
    # except:
    #doc_parser = TextDocParser(_filename)
    #sent_parser = SentenceParser()
    #corpus = Corpus(doc_parser, sent_parser)
    # print corpus

    # Sentences havent been parsed, so parse them now
    #sentences = corpus.get_contexts()
    sentences = doc_parser.parseDoc(_filename)
    print sentences

    # Serialize so that you dont have to deal with parsing in the future
    # if not os.path.exists("cache/" + _filename +"/" ):
    #     os.makedirs("cache/" + _filename + "/")
    # with open(pckl_f, 'w+') as f:
    #     cPickle.dump(sentences, f)

    biomarker_ngrams = Ngrams(n_max=1)
    disease_ngrams = Ngrams(n_max=5)

    # Create the two matchers who have been defined in separate classes
    BM = BiomarkerMatcher.getBiomarkerMatcher()
    DM = DiseaseMatcher.getDiseaseMatcher()

    CandidateExtractor_BM = CandidateExtractor(biomarker_ngrams, BM)
    CandidateExtractor_DM = CandidateExtractor(disease_ngrams, DM)

    # #fix disease candidate generator error- "ovarian and prostate cancer"
    # with open('diseaseDatabase.pickle', 'rb') as f:
    #     diseaseDictionary = pickle.load(f)
    # DiseaseMatch = DictionaryMatch(label = "Diseases", dictionary = diseaseDictionary, ignore_case= True)
    # E = Entities(sentences, DiseaseMatch)
    # filename = "AGR2_blood_biomarker.txt"
    # text = open(filename, "r").read()
    # editedText = DiseaseCandidateGenerator.addDiseaseBases(E, diseaseDictionary ,text)
    # editedSentences = []
    # sentence_parser = SentenceParser()
    # list = sentence_parser.parse(editedText, 1)
    # for editsentence in list:
    #     editedSentences.append(editsentence)
    # Create the relations using the two matchers

    possiblePairs = Relations(
        sentences, CandidateExtractor_BM, CandidateExtractor_DM)

    # badCount = 0
    # goodCount = 0
    # allGoodPairs = []
    # for goodPair in possiblePairs:
    #     allGoodPairs.append(goodPair.sent_id)
    # #Return these pairs
    # for sentence in sentences:
    #     if sentence.sent_id in allGoodPairs:
    #         print "GOOD PAIR: "
    #         print sentence.words
    #         print "\n"
    #         goodCount += 1
    #     else:
    #         print "BAD PAIR:"
    #         print sentence.words
    #         print "\n"
    #         badCount += 1
    # print goodCount
    # print badCount

    # print possiblePairs
    return possiblePairs


def biomarkerDrugRelations(filename):
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

    BM = matchers.getBiomarkerMatcher()
    DAM = matchers.getDrugAssociationMatcher()

    CandidateExtractor_BM = CandidateExtractor(biomarker_ngrams, BM)
    CandidateExtractor_DAM = CandidateExtractor(drug_association_ngrams, DAM)

    possiblePairs = Relations(
        sentences, CandidateExtractor_BM, CandidateExtractor_DAM)

    return possiblePairs


def biomarkerMediumRelations(filename):
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

    # Create the two matchers who have been defined in separate classes
    BM = matchers.getBiomarkerMatcher()
    MM = matchers.getMediumMatcher()

    CandidateExtractor_BM = CandidateExtractor(biomarker_ngrams, BM)
    CandidateExtractor_MM = CandidateExtractor(medium_ngrams, MM)

    # Create the relations using the two matchers
    possiblePairs = Relations(
        sentences, CandidateExtractor_BM, CandidateExtractor_MM)
    return possiblePairs


def biomarkerTypeRelations(filename):
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

    BM = matchers.getBiomarkerMatcher()
    TM = matchers.getBiomarkerTypeMatcher()

    CandidateExtractor_BM = CandidateExtractor(biomarker_ngrams, BM)
    CandidateExtractor_TM = CandidateExtractor(biomarker_type_ngrams, TM)

    possiblePairs = Relations(
        sentences, CandidateExtractor_BM, CandidateExtractor_TM)

    return possiblePairs


# Above baseline extraction:
#---------------------------
# Generate all possible Multi-Relational objects from top 4 relation extractors

def AllLevelsRelationTuples(filename):
    sentences = doc_parser.parseDoc(filename)
    possiblePairs_BM_U = biomarkerUnitsRelations(sentences)
    possiblePairs_BM_L = biomarkerLevelsRelations(sentences)
    possiblePairs_BM_MT = biomarkerMeasurementRelations(sentences)
    possiblePairs_BM_TS = biomarkerTestsetRelations(sentences)

    # highly innefficient...fix!
    all = []
    for pair_BM_L in possiblePairs_BM_L:
        for pair_BM_TS in possiblePairs_BM_TS:
            if pair_BM_L.mention1(attribute='sent_id') == pair_BM_TS.mention1(
                    attribute='sent_id') and pair_BM_L.mention1(attribute='char_offsets') == pair_BM_TS.mention1(
                    attribute='char_offsets'):
                for pair_BM_MT in possiblePairs_BM_MT:
                    if pair_BM_L.mention1(attribute='sent_id') == pair_BM_MT.mention1(
                            attribute='sent_id') and pair_BM_L.mention1(attribute='char_offsets') == pair_BM_MT.mention1(
                            attribute='char_offsets'):
                        for pair_BM_U in possiblePairs_BM_U:
                            if pair_BM_L.mention1(attribute='sent_id') == pair_BM_U.mention1(
                                    attribute='sent_id') and pair_BM_L.mention1(
                                    attribute='char_offsets') == pair_BM_U.mention1(attribute='char_offsets'):
                                multiRelation = [
                                    pair_BM_L, pair_BM_TS, pair_BM_MT, pair_BM_U]
                                all.append(multiRelation)

    return all
