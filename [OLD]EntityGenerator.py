#imports
import BiomarkerMatcher
import os
from snorkel.snorkel.parser import *
from snorkel.snorkel.candidates import *
from snorkel.snorkel.matchers import *
from snorkel.snorkel.snorkel import *
def generateRelations(_filename):
    print os.listdir('.')
    doc_parser = TextDocParser(_filename)
    sent_parser = SentenceParser()
    corpus = Corpus(doc_parser, sent_parser)
    # print corpus
    # Sentences havent been parsed, so parse them now
    sentences = corpus.get_contexts()
    # print sentences
    # Serialize so that you dont have to deal with parsing in the future
    # if not os.path.exists("cache/" + _filename +"/" ):
    #     os.makedirs("cache/" + _filename + "/")
    # with open(pckl_f, 'w+') as f:
    #     cPickle.dump(sentences, f)

    biomarker_ngrams = Ngrams(n_max=5)
    #Create the two matchers who have been defined in separate classes
    BM = CandidateExtractor(biomarker_ngrams, RegexMatch(rgx=r'(^|(?<=\s))[A-Za-z][A-Z1-6-]{2,}', ignore_case=False,attrib='words'))
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

    #Create the relations using the two matchers
    possiblePairs = Entities(sentences, BM)
    print possiblePairs
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
generateRelations("text/AGR2_blood_biomarker.txt")