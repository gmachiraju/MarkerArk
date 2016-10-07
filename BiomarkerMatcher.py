import pickle
from snorkel.snorkel import *
from snorkel.snorkel.matchers import *

def getBiomarkerMatcher():
    with open('databases/markerData.pickle', 'rb') as f:

        markerDatabase = pickle.load(f)

    marker_dm = DictionaryMatch(d=markerDatabase, ignore_case=False)

    marker_regex = RegexMatchEach(rgx=r'(^|(?<=\s))[A-Za-z][A-Z1-6-]{2,}', ignore_case=False,attrib='words')

    matcher = Union(marker_regex, marker_dm)
    
    return matcher
# with open ("databases/markerData.pickle", "rb") as f:
#     diseaseData = (pickle.load(f))
# if "with" in diseaseData:
#     print "ASDF"
# with open("databases/diseaseAbbreviationsDatabase.pickle", "rb") as f:
#     diseaseData = (pickle.load(f))
# if "with" in diseaseData:
#     print "ASDF"