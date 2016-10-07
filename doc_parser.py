from itertools import izip_longest

import os, glob
import pdfminer, os
import unicodedata
from pdfminer.converter import *
from pdfminer.layout import *
from pdfminer.pdfparser import *
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice
from snorkel.snorkel.snorkel import *
import os, glob

def grouper(n, iterable, fillvalue=None):

    "Collect data into fixed-length chunks or blocks"

    # grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx

    args = [iter(iterable)] * n

    return izip_longest(fillvalue=fillvalue, *args)

def grouper(n, iterable, fillvalue=None):

    "Collect data into fixed-length chunks or blocks"

    # grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx

    args = [iter(iterable)] * n

    return izip_longest(fillvalue=fillvalue, *args)

def pdfToText(folder):
    ocean = os.listdir(folder)
    for fish in ocean:
        if(fish.endswith(".pdf")):
            print fish
            output = StringIO()
            manager = PDFResourceManager()
            converter = TextConverter(manager, output, laparams=LAParams())
            interpreter = PDFPageInterpreter(manager, converter)

            infile = file(folder + "/" +  fish, 'rb')
            for page in PDFPage.get_pages(infile, set()):
                interpreter.process_page(page)
            infile.close()
            converter.close()
            text = output.getvalue()

            with open(folder + "/" +  fish + ".txt", "w+") as f:
                f.write(text)


def parseDoc (_filename):
    original_path = os.getcwd()
# _____File Parser______________________________________________________________________________________________________
    if os.path.isfile(_filename):
        filename = _filename
        text = ""
        import string

        with open(_filename, "rb") as f:
            text = f.read()
            printable = set(string.printable)
            text = filter(lambda x: x in printable, text)
            text = text.encode('utf-8')
            # text = text.decode('utf-8')
            # text = text.encode('utf-8')
            f.close()
        with open(_filename, "w+") as f:
            f.write(text)
            f.close()
        allSentences = []
        try:
            sent_parser = SentenceParser()
            doc_parser = TextDocParser(filename)
            corpus = Corpus(doc_parser, sent_parser)
            allSentences = corpus.get_contexts()
            print allSentences
        except(ValueError):
            n = 100
            with open(filename, 'rb+') as f:
                small_file_list = []
                for i, g in enumerate(grouper(n, f, fillvalue=''), 1):
                    with open(filename + '_{0}'.format(i * n), 'w') as fout:
                        small_file_list.append(filename + '_{0}'.format(i * n))
                        fout.writelines(g)
            print small_file_list
            for small_file in small_file_list:
                try:
                    sent_parser = SentenceParser()
                    doc_parser = TextDocParser(small_file)
                    corpus = Corpus(doc_parser, sent_parser)
                    sentences = corpus.get_contexts()
                except(ValueError):
                    sentences = maxParseDoc(small_file, 50)
                for sentence in sentences:
                    allSentences.append(sentence)
        return allSentences
# _______Doc Parser_____________________________________________________________________________________________________
    elif os.path.isdir(_filename):
        #create list of pdf.txt files to parse
        text_file_list = os.listdir(_filename)
        temp_list = []
        for file in text_file_list:
            if (file.endswith(".pdf.txt")):
                temp_list.append(file)
        text_file_list = temp_list
        #take list of pdf.txt files and break each file into smaller files
        for filename in text_file_list:
            text = ""
            import string

            with open(_filename + filename, "rb") as f:
                text = f.read()
                printable = set(string.printable)
                text = filter(lambda x: x in printable, text)
                text = text.encode('utf-8')
                f.close()
            with open(_filename + filename, "w+") as f:
                f.write(text)
                f.close()
            n = 200
            with open(_filename + filename, 'rb+') as f:
                print os.getcwd()
                print "dir: "+ _filename + filename
                for i, g in enumerate(grouper(n, f, fillvalue=''), 1):
                    with open(_filename+'parsed_text/' + filename + '_{0}'.format(i * n), 'w') as fout:
                        fout.writelines(g)
                        fout.close()
                f.close()

        #create list of all small files to analyze
        os.chdir(os.getcwd()+'/'+_filename+'parsed_text')
        small_file_list = glob.glob("*")
        print small_file_list

        #parse small files into documents
        allSentences = []
        for small_file in small_file_list:
            try:
                if not os.path.isdir(small_file):
                    sent_parser = SentenceParser()
                    doc_parser = TextDocParser(small_file)
                    print small_file
                    corpus = Corpus(doc_parser, sent_parser)
                    sentences = corpus.get_contexts()
            except(ValueError):
                if not os.path.isdir(small_file):
                    sentences = maxParseDoc(small_file, 100)
            for sentence in sentences:
                allSentences.append(sentence)

        os.chdir(original_path)
        return allSentences


def maxParseDoc (_filename, parsePerLine):
    filename = _filename
    allSentences = []
    try:
        sent_parser = SentenceParser()
        doc_parser = TextDocParser(filename)
        corpus = Corpus(doc_parser, sent_parser)
        allSentences = corpus.get_contexts()
    except:
        n = parsePerLine
        with open(filename, 'rb+') as f:
            small_file_list = []
            print os.getcwd()
            for i, g in enumerate(grouper(n, f, fillvalue=''), 1):
                with open('too_large/' + filename + '_{0}'.format(i * n), 'w') as fout:
                    print filename + '_{0}'.format(i * n)
                    small_file_list.append(filename + '_{0}'.format(i * n))
                    fout.writelines(g)
        print small_file_list
        for small_file in small_file_list:
            sent_parser = SentenceParser()
            doc_parser = TextDocParser('too_large/'+small_file)
            corpus = Corpus(doc_parser, sent_parser)
            sentences = corpus.get_contexts()
            for sentence in sentences:
                allSentences.append(sentence)
    return allSentences


