# must contain  - all words 
# -all noun phrases
from word_parser import WordParser, WordType
from phrase import Phrase
import code
# code.interact(local=dict(globals(), **locals()))

class Sentence(object):

  def __init__(self, words):
    self.words = words
    self.phrases = {}
    for word in words:
      if word.type == WordType.END or word.type == WordType.CONJUNCTION:
        continue
      for phrase in word.chunk.split(','):
        if phrase in self.phrases:
          # if phrase object with this type and number already exists
          # add the word to the existing phrase object
          self.phrases[phrase].add_to_phrase(word)
        else:
          # create a new Phrase Object
          self.phrases[phrase] = Phrase(word)

  def __str__(self):
    return " ||Sentence|| \n phrases--- " + str(self.phrases) + "\n Sentence-Words--- " + str(self.words) + "\n\n"
  
  def __repr__(self):
    return str(self)

  @staticmethod
  def get_all_sentences(text):
    sentences = []
    words = WordParser.get_all_words(text)
    temp_words = []
    # code.interact(local=dict(globals(), **locals()))
    for word in words:
      if word.type == WordType.END:
        temp_words.append(word)
        sentences.append(Sentence(temp_words))
        temp_words = []
      else:
        temp_words.append(word)
    return sentences
