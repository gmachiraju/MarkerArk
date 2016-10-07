import BiomarkerMatcher
import DiseaseCandidateGenerator

from snorkel.ddlite import *

parser = DocParser('thing.txt', ftreader=TextReader())
sentences = parser.parseDocSentences()

BM = BiomarkerMatcher.generateBiomarkerCandidates()
DM = DiseaseCandidateGenerator.generateDiseaseCandidates()

possiblePairs = Relations(sentences, BM, DM)
feats = possiblePairs.extract_features()
otherModel = DDLiteModel(possiblePairs, feats)


# 1
def LF_distance(m):
    distance = abs(m.e2_idxs[0] - m.e1_idxs[0])
    if distance < 10:
        # print "RETURNING ONE"
        return 1
    else:
        return 0


# 2
def LF_associate(m):
    if ('associate' in m.post_window1('lemmas')) and ('associate' in m.pre_window2('lemmas')):
        return 1
    else:
        return 0


# 3
def LF_express(m):
    return 1 if ('express' in m.post_window1('lemmas')) and ('express' in m.pre_window2('lemmas')) else 0


# 4
def LF_marker(m):
    return 1 if ('marker' in m.post_window1('lemmas') or 'biomarker' in m.post_window1('lemmas')) and (
        'marker' in m.post_window2('lemmas') or 'biomarker' in m.post_window2('lemmas')) else 0


# 5
def LF_elevated(m):
    return 1 if ('elevated' in m.post_window1('lemmas')) and ('elevated' in m.pre_window2('lemmas')) else 0


def LF_decreased(m):
    return 1 if ('decreased' in m.post_window1('lemmas')) and ('decreased' in m.pre_window2('lemmas')) else 0


# 6
def LF_correlation(m):
    return 1 if ('correlation' in m.pre_window1('lemmas')) else 0


# 7
def LF_correlate(m):
    return 1 if ('correlates' in m.post_window1('lemmas')) and ('found' in m.pre_window2('lemmas')) else 0


# 8
def LF_found(m):
    return 1 if ('found' in m.post_window1('lemmas')) and ('found' in m.pre_window2('lemmas')) else 0


# 9 (-1 if biomarker is confused with a name of a person)
def LF_People(m):
    return -1 if ('NNP' in m.mention1(attribute='poses')) else 0


# 10
def LF_diagnosed(m):
    return 1 if ('diagnose' in m.post_window1('lemmas')) else 0


# 11
def LF_variant(m):
    return 1 if ('variant of' in m.pre_window1('lemmas')) else 0


# 12
def LF_appear(m):
    return 1 if ('appear' in m.post_window1('lemmas')) else 0


# 13
def LF_connect(m):
    return 1 if ('connect' in m.post_window1('lemmas')) else 0


# 14
def LF_relate(m):
    return 1 if ('relate' in m.post_window1('lemmas')) else 0


# 15
def LF_exhibit(m):
    return 1 if ('exhibit' in m.post_window1('lemmas')) else 0


# 16
def LF_indicate(m):
    return 1 if ('indicate' in m.post_window1('lemmas')) else 0


# 17
def LF_signify(m):
    return 1 if ('signify' in m.post_window1('lemmas')) else 0


# 18
def LF_show(m):
    return 1 if ('show' in m.post_window1('lemmas')) else 0


# 19
def LF_demonstrate(m):
    return 1 if ('demonstrate' in m.post_window1('lemmas')) else 0


# 20
def LF_reveal(m):
    return 1 if ('reveal' in m.post_window1('lemmas')) else 0


# 21
def LF_suggest(m):
    return 1 if ('suggest' in m.post_window1('lemmas')) else 0


# 22
def LF_evidence(m):
    return 1 if ('evidence for' in m.post_window1('lemmas')) else 0


# 23
def LF_indication(m):
    return 1 if ('indication of' in m.post_window1('lemmas')) else 0


# 24
def LF_elevation(m):
    return 1 if ('elevation' in m.post_window1('lemmas')) else 0


# 25
def LF_diagnosis(m):
    return 1 if ('diagnosis of' in m.post_window1('lemmas')) else 0


# 26
def LF_variation(m):
    return 1 if ('variation of' in m.pre_window1('lemmas')) else 0


# 27
def LF_modification(m):
    return 1 if ('modification of' in m.pre_window1('lemmas')) else 0


# 28
def LF_suggestion(m):
    return 1 if ('suggestion' in m.post_window1('lemmas')) else 0


# 29
def LF_link(m):
    return 1 if ('link' in m.post_window1('lemmas')) else 0


# 30
def LF_derivation(m):
    return 1 if ('derivation of' in m.pre_window1('lemmas')) else 0


# 31
def LF_denote(m):
    return 1 if ('denote' in m.post_window1('lemmas')) else 0


# 32
def LF_denotation(m):
    return 1 if ('denotation' in m.post_window1('lemmas')) else 0


# 33
def LF_demonstration(m):
    return 1 if ('demonstration' in m.post_window1('lemmas')) else 0


# 34
def LF_magnification(m):
    return 1 if ('magnification' in m.pre_window1('lemmas')) else 0


# 35
def LF_depression(m):
    return 1 if ('depression' in m.pre_window1('lemmas')) else 0


# 36
def LF_boost(m):
    return 1 if ('boost' in m.pre_window1('lemmas')) else 0


# 37
def LF_level(m):
    return 1 if ('level' in m.pre_window1('lemmas')) else 0


# 38
def LF_advance(m):
    return 1 if ('advance' in m.pre_window1('lemmas')) else 0


# 39
def LF_augmentation(m):
    return 1 if ('augmentation' in m.pre_window1('lemmas')) else 0


# 40
def LF_decline(m):
    return 1 if ('decline' in m.pre_window1('lemmas')) else 0


# 41
def LF_lessening(m):
    return 1 if ('lessening' in m.pre_window1('lemmas')) else 0


# 42
def LF_enhancement(m):
    return 1 if ('enhancement' in m.pre_window1('lemmas')) else 0


# 43
def LF_expression(m):
    return 1 if ('expression' in m.post_window1('lemmas')) else 0


# 44
def LF_buildup(m):
    return 1 if ('buildup' in m.pre_window1('lemmas')) else 0


# 45
def LF_diminishing(m):
    return 1 if ('diminishing' in m.pre_window1('lemmas')) else 0


# 46
def LF_diminishment(m):
    return 1 if ('diminishment' in m.pre_window1('lemmas')) else 0


# 47
def LF_reduction(m):
    return 1 if ('reduction' in m.pre_window1('lemmas')) else 0


# 48
def LF_drop(m):
    return 1 if ('drop' in m.pre_window1('lemmas')) else 0


# 49
def LF_dwindling(m):
    return 1 if ('dwindling' in m.pre_window1('lemmas')) else 0


# 50
def LF_lowering(m):
    return 1 if ('lowering' in m.pre_window1('lemmas')) else 0


LFs = [LF_distance, LF_associate, LF_express, LF_marker, LF_elevated, LF_decreased, LF_correlation, LF_correlate,
       LF_found, LF_People, LF_diagnosed, LF_variant, LF_appear, LF_connect, LF_relate, LF_exhibit, LF_indicate,
       LF_signify, LF_show, LF_demonstrate, LF_reveal, LF_suggest, LF_evidence, LF_indication, LF_elevation,
       LF_diagnosis, LF_variation, LF_modification, LF_suggestion, LF_link, LF_derivation, LF_denote, LF_denotation,
       LF_demonstration, LF_magnification, LF_depression, LF_boost, LF_level, LF_advance, LF_augmentation, LF_decline,
       LF_lessening, LF_enhancement, LF_expression, LF_buildup, LF_diminishing, LF_diminishment, LF_reduction, LF_drop,
       LF_dwindling, LF_lowering]

otherModel.open_mindtagger(num_sample=1000, width='100%', height=1200)
otherModel.add_mindtagger_tags()
input = raw_input("hola")

