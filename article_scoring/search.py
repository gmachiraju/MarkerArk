from __future__ import division
import pickle
import re
import unicodedata
import os

"""
Returns the citations of the text
if sentence has a colon, delete the string completely
if it has a hyphen between numbers (ex. 234-456), delete the string completely
if it has "references", delete the word "references" from the string
if it's four numbers in a row (ex 2008), delete the numbers from the string
if it doesn't start with a capital letter, delete the word from the string
delete "et al" and everything after that in the string
"""

# after all that is deleted, split the list using .split(',')

#(?<=\s)[A-Z][a-zA-Z]{1,}\s[A-Z]{1,3}(?=[.,])|(?<=^)[A-Z][a-zA-Z]{1,}\s[A-Z]{1,3}(?=[.,])

# One for getting names with -
#(?<=\s)[A-Z][a-zA-Z]{1,}-[A-Z][a-zA-Z]{1,}\s[A-Z]{1,3}(?=[.,])|(?<=^)[A-Z][a-zA-Z]{1,}-[A-Z][a-zA-Z]{1,}\s[A-Z]{1,3}(?=[.,])


def getAuthors(filename):
    text = open(filename, "r").read()
    check_after_index = 0

    # find references in article to shorten amount of text being checked
    if "references" in text:
        check_after_index = text.index("references")
    elif "REFERENCES" in text:
        check_after_index = text.index("REFERENCES")
    elif "References" in text:
        check_after_index = text.index("References")
    else:  # just check entire file
        check_after_index = 0

    shorter_text = text[check_after_index:]
    authorList = []
    generator_authorsCited_reg_normal = re.finditer(
        "(?<=\s)[A-Z][a-zA-Z]{1,}\s[A-Z]{1,4}(?=[.,])|(?<=^)[A-Z][a-zA-Z]{1,}\s[A-Z]{1,4}(?=[.,])", shorter_text)
    generator_authorsCited_reg_dash = re.finditer(
        "(?<=\s)[A-Z][a-zA-Z]{1,}-[A-Z][a-zA-Z]{1,}\s[A-Z]{1,3}(?=[.,])|(?<=^)[A-Z][a-zA-Z]{1,}-[A-Z][a-zA-Z]{1,}\s[A-Z]{1,3}(?=[.,])", shorter_text)

    for match in generator_authorsCited_reg_normal:
        authorList.append(fixParseNotation(match.group()))
    for match in generator_authorsCited_reg_dash:
        authorList.append(fixParseNotation(match.group()))

    return authorList

# remove \n notation that occurs when parsing doc into text


def fixParseNotation(author):
    if "\n" in author:
        newLineIndex = author.index("\n")
        removed = author[0:newLineIndex] + " " + author[newLineIndex + 1:]
        return removed
    else:
        return author


def applyAuthorScore(authorList, articleCitations):
    if len(authorList) == 0:
        for author in articleCitations:
            authorList.append([1, author])
    else:
        for author in articleCitations:
            objIndex = -1
            noMatch = True
            for authorObj in authorList:
                objIndex = objIndex + 1
                if author == authorObj[1]:
                    authorList[objIndex][0] = authorList[objIndex][
                        0] + 1  # increase author score by one
                    noMatch = False
            if noMatch:
                authorList.append([1, author])

    return sorted(authorList)


def getFinalAuthorScore(authorList):
    scores = []
    for author in authorList:
        newScore = (len(authorList) - authorList.index(author)) / \
            len(authorList) * 100
        scores.append(newScore)

    return scores


authors = getAuthors("AGR2_blood_biomarker.txt")
