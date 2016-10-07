from snorkel.snorkel.snorkel import *
from snorkel.snorkel.matchers import *

def getTestSetMatcher():
   
    noun_regex = RegexMatchEach(rgx=r'[A-Z]?NN[A-Z]?', ignore_case=True, attrib='poses')
    complete_obj_regex = RegexMatchSpan(noun_regex, rgx=r'[J]{2,}\sNN[A-Z]?', ignore_case=True, attrib='poses')
    
    return complete_obj_regex
    
