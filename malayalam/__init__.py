from __future__ import absolute_import, division
from __future__ import print_function, unicode_literals
from io import open
import json
from malayalam.splitter import *
from malayalam.postprocessor import PostProcessor
from malayalam.joiner import Joiner
from pkg_resources import resource_filename
from phonetics.python.morphology.__init__ import Analyser

class splitter:
    def __init__(self):
        # modelfilename = resource_filename()
        modelfile = open('malayalam/model.json', 'r', encoding='utf-8')
        serialized = json.load(modelfile)
        modelfile.close()
        self.splitter = Splitter(model=serialized)
        self.postprocessor = PostProcessor()
        self.joiner = Joiner()

    def set_model(self, model):
        self.splitter = Splitter(model=model)

    def split(self, word):
        ps = self.splitter.splits(word)
        split_words = self.postprocessor.split(word, ps)
        print(split_words)
        if len(split_words)==1:
            split_words = Analyser().analyse(word)
            return (split_words['morphemes'])
        else:
            return split_words

    def join(self, words):
        return self.joiner.join_words(words)

    def get_module_name(self):
        return "word analyser"

    def get_info(self):
        return "word analyser for malayalam"


def getInstance():
    return Sandhisplitter()
