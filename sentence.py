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
    self.phrase_order = []
    phrase_index = -1
    for word in words:
      if word.type == WordType.END or word.type == WordType.CONJUNCTION or WordType.is_punctuation(word.type):
        continue
      for phrase in word.chunk.split(','):
        if phrase in self.phrases:
          # if phrase object with this type and number already exists
          # add the word to the existing phrase object
          word.index_in_sentence = phrase_index
          self.phrases[phrase].add_to_phrase(word)
        else:
          # create a new Phrase Object
          phrase_index += 1
          self.phrase_order.append(phrase)
          word.index_in_sentence = phrase_index
          self.phrases[phrase] = Phrase(word, phrase)

  def get_colocation_pattern(self):
    pattern = []
    for order in self.phrase_order:
      phrase = self.phrases[order]
      pattern.append(phrase.type)
    return pattern

  def __str__(self):
    return " ||Sentence|| \n phrases--- " + str(self.phrases) + "\n Sentence-Words--- " + str(self.words) + "\n\n"
  
  def __repr__(self):
    return str(self)

  @staticmethod
  def get_all_sentences(text):
    sentences = []
    words = WordParser.get_all_words(text)
    temp_words = []
    for word in words:
      if word.type == WordType.END:
        temp_words.append(word)
        sentences.append(Sentence(temp_words))
        temp_words = []
      else:
        temp_words.append(word)
    return sentences
