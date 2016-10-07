from ddlite import *
import BiomarkerMatcher, BiomarkerTypeMatcher, pickle


def doEverything():
    parser = DocParser('AGR2_blood_biomarker.txt', ftreader=TextReader())
    sentences = parser.parseDocSentences()

    BM = BiomarkerMatcher.getBiomarkerMatcher()
    TM = BiomarkerTypeMatcher.generateTypeMatcher()

    possiblePairs = Relations(sentences, BM, TM)
    feats = possiblePairs.extract_features()
    otherModel = DDLiteModel(possiblePairs, feats)
    
    negationWords = ["not", "nor", "neither"]

    def presenceOfNot(m):
        for word in negationWords:
            if (word in m.post_window1('lemmas', 20)) and (word in m.pre_window2('lemmas', 20)):
                return True
        return False
        
    def LF_distance(m):
        # print m.lemmas
        # print m.dep_labels
        distance = abs(m.e2_idxs[0] - m.e1_idxs[0])
        if distance < 8:
            # print "RETURNING ONE"
            return 0
        else:
            return -1

    def LF_isAMemberOf(m):
        return 1 if ('is' in m.post_window1('lemmas', 20) and 'a' in m.post_window1('lemmas', 20) and
            'member' in m.post_window1('lemmas', 20) and 'of' in m.post_window1('lemmas', 20)) and (('is' in
            m.pre_window2('lemmas', 20) and 'a' in m.pre_window2('lemmas', 20) and 'member' in
            m.pre_window2('lemmas', 20) and 'of' in m.pre_window2('lemmas', 20))) else 0

    def LF_membersOf(m):
        return 1 if ('member' in m.post_window1('lemmas'), 20) and 'of' in m.post_window1('lemmas', 20) and (
        ('member' in m.pre_window2('lemmas'), 20) and 'of' in m.pre_window2('lemmas', 20)) else 0

    def LF_family(m):
        return 1 if ('family' in m.post_window1('lemmas', 20) and 'family' in m.post_window2('lemmas', 20)) else 0

    def LF_cancerrelated(m):
        return 1 if ('cancer' in m.post_window1('lemmas', 20) and '-' in m.post_window1('lemmas', 20) and
            'related' in m.post_window1('lemmas', 20)) and ('cancer' in m.pre_window2('lemmas', 20) and '-' in m.pre_window1('lemmas', 20) and
            'related' in m.pre_window1('lemmas', 20)) else 0

    def LF_isA(m):
        return 1 if ('is' in m.post_window1('lemmas', 20) and 'a' in m.post_window1('lemmas', 20) and
        ('is' in m.pre_window2('lemmas', 20) and 'a' in m.pre_window2('lemmas', 20))) else 0

    def LF_types(m):
        return 1 if ('type' in m.post_window1('lemmas', 20) or ('type' in m.pre_window2('lemmas', 20))) else 0

    def LF_isaBiomarker(m):
        post_window1_lemmas = m.post_window1('lemmas', 20)
        pre_window2_lemmas = m.pre_window2('lemmas', 20)
        if ('biomarker' in post_window1_lemmas and 'biomarker' in pre_window2_lemmas) or (
                'marker' in post_window1_lemmas and 'marker' in pre_window2_lemmas) or (
                'indicator' in post_window1_lemmas and 'indicator' in pre_window2_lemmas):
            marker_idx_post_window1 = -1
            markers = ['biomarker', 'marker', 'indicator']
            for marker in markers:
                try:
                    # print post_window1_lemmas
                    findMarker = post_window1_lemmas.index(marker)
                    if not findMarker == -1:
                        marker_idx_post_window1 = findMarker
                        print marker
                except:
                    pass
            if 'cop' in m.post_window1('dep_labels', 20):
                try:
                    cop_idx_post_window1 = m.post_window1('dep_labels', 20).index('cop')
                except:
                    pass

                print "MarkerIdx:"
                print marker_idx_post_window1
                print "ROOTIdx:"
                try:
                    print  m.post_window1('dep_labels', marker_idx_post_window1)
                    print  m.post_window1('dep_labels', marker_idx_post_window1).index('ROOT')
                except:
                    pass
                print '\n'

                return 1 if ('nsubj' in m.mention1(attribute='dep_labels')) and (
                marker_idx_post_window1 - cop_idx_post_window1 < 4)  else 0
        return 0

    LFs = [isAMemberOf, membersOf, family, cancerrelated, isA, types]
    gts = []
    uids = []
    for tuple in mindtaggerToTruth("tags4.tsv"):
        uids.append(tuple[0])
        gts.append(tuple[1])
    otherModel.update_gt(gt=gts, uids=uids)
    # otherModel.open_mindtagger(num_sample=100, width='100%', height=1200)
    # otherModel.add_mindtagger_tags()
    otherModel.set_holdout(validation_frac=0.5)
    otherModel.apply_lfs(LFs, clear=False)
    return otherModel
    # """DEBUGGING CODE"""
    # otherModel.open_mindtagger(num_sample=100, width='100%', height=1200)
    # otherModel.add_mindtagger_tags()
    # otherModel.plot_lf_stats()
    #
    # """END"""
    # # with open("thing.xml", "wb") as f:
    #


def mindtaggerToTruth(filename):
    uids = []
    list = re.split("[^\\S ]", open(filename).read())
    # print list
    count = 7
    while count < len(list):
        number = 0
        if (list[count + 6] == "true"):
            number = 1
        elif (list[count + 6] == "false"):
            number = -1
        uids.append((list[count + 5] + "::" + list[count + 3] + "::[" + list[count + 4] + ", " + list[count] + "]::['" +
                     list[count + 1] + "', '" + list[count + 2] + "']", number))
        count += 7
    return uids
