import unicodedata
from snorkel.ddlite import *


class Article():
    """
    An Article object represents a PUBMED publication that gets analyzed by Snorkel. 
    Initially, an Article has a name (or empty string) and relations (or None object), (describe further).
    """

    article_name = ""
    relations = None

    def __init__(self, name, relations):
        self.article_name = name
        self.relations = relations

    def getScore(self, disease, biomarker, article_list):
        return

    def num_mentions_scorer(self, disease, biomarker, article_list):
        """
        Obtain a list of articles that has the disease and biomarker in it. Pretend that this 
        list has been populated and is now stored in the variable "article_list". This list is 
        populated by Article objects. The article that I am scoring will be called curr_article 
        (format is Article object).
        """
        curr_article = self
        # For the sake of writing an algorithm, pretend that curr_article is
        # actually a thing
        article_list = sorted(article_list, key=self.getNumMentions())
        # Now get the position of the article
        position = article_list.index(curr_article)
        # Now divide the position by the number of elements for our score. This
        # score is out of 100
        return (position + 1) / len(article_list) * 100

    def getNumMentions(self):
        return len(self.relations)

    def parseDocIntoWords(filename):
        text = open(filename, "r").read()
        sentence_parser = SentenceParser()
        list = sentence_parser.parse(text, 1)
        words = []

        for sentence in list:
            words.append(sentence)
        return words

    def extractTitle(sentences_Article):
        numWordsToExtract, wordsExtracted, indexInSentence = 50, 0, 0
        currSentenceWords, sentenceNum, unicode_title = '', 0, []

        for sentence in sentences_Article:
            currSentenceWords = sentence.words

        for word in currSentenceWords:
            unicode_title.append(word)
            wordsExtracted = wordsExtracted + 1
            if wordsExtracted is numWordsToExtract:
                return unicodedata.normalize('NFKD', ' '.join(unicode_title)).encode('ascii', 'ignore')

    def articleScorer(self, filename, biomarkerName, diseaseName, article_list):
        sentences_Article = self.parseDocIntoWords(filename)
        title = self.extractTitle(sentences_Article)
        titleScore, relationsRatScore, mentionsScore = 0, 0, 0
        # Title:
        markerTitleScore, diseaseTitleScore = 0, 0

        if biomarkerName in title:
            markerTitleScore = 1
        if diseaseName in title:
            diseaseTitleScore = 1

        titleScore = 50 * ((diseaseTitleScore + markerTitleScore) / 2)
        # mentions:
        mentionsScore = 25 * self.num_mentions_scorer(
            disease=diseaseName, biomarker=biomarkerName, article_list=article_list)

        # relationsRat:
        relationsRatScore = 25 * len(self.relations) / len(sentences_Article)
        totalScore = titleScore + mentionsScore + relationsRatScore

        return totalScore
