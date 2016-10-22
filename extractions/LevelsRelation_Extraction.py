import BiomarkerMatcher
import LevelsMatcher
import LevelsRelation_BiomarkerLevels_Extraction
import LevelsRelation_BiomarkerMeasurementType_Extraction
import LevelsRelation_BiomarkerTestSet_Extraction
import LevelsRelation_BiomarkerUnits_Extraction
import MeasurementTypeMatcher
import TestSetMatcher
import UnitsMatcher
import doc_parser
import pickle
from snorkel.candidates import Ngrams
from snorkel.matchers import CandidateExtractor
from snorkel.candidates import *
from snorkel.matchers import *
from snorkel.snorkel.snorkel import Relations


def generateRelations(filename):
    sentences = doc_parser.parseDoc(filename)
    possiblePairs = LevelsRelation_BiomarkerLevels_Extraction.generateRelations(
        sentences)

    return possiblePairs


def generateAllTupleRelations(filename):
    sentences = doc_parser.parseDoc(filename)
    possiblePairs_BM_L = LevelsRelation_BiomarkerLevels_Extraction.generateRelations(
        sentences)
    possiblePairs_BM_TS = LevelsRelation_BiomarkerTestSet_Extraction.generateRelations(
        sentences)
    possiblePairs_BM_MT = LevelsRelation_BiomarkerMeasurementType_Extraction.generateRelations(
        sentences)
    possiblePairs_BM_U = LevelsRelation_BiomarkerUnits_Extraction.generateRelations(
        sentences)
    all = []

    # Generate all possible Multi-Relational Objects
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


# def normalize (sentences):
    # for sentence in sentences:
