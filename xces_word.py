from constants import WordType
import itertools

class XcesWord(object):

  id_iter = itertools.count()
  def  __init__(self, word, attributes):
    self.id = next(self.id_iter)
    self.original = word
    if len(attributes.keys()) != 0:
      self.lemma = attributes['lemma']
      self.ana = attributes['ana']
      self.type = WordType(self.ana[0])
      if 'chunk' in attributes:
        self.chunk = attributes['chunk']
      else:
        if self.type == WordType.PRONOUN:
          self.chunk = "---"
    else:
      if self.original == ',' or self.original == ';' or self.original == ':':
        self.type = WordType.PUNCTUATION
      else:
        self.type = WordType.END

  def is_word(self):
    return self.type == WordType.NOUN or self.type == WordType.PRONOUN
  
  def is_short_pronoun(self):
    return self.chunk == "---"
  
  def compute_order_for_short_pronoun(self, word):
    self.chunk = self.chunk + word.chunk[-1]

  def __str__(self):
    return "Word: " + self.original + " --- is_word: " + str(self.is_word())
  
  def __repr__(self):
    return str(self)
  
  def __eq__(self, other):
    if isinstance(other, self.__class__):
      return self.__dict__ == other.__dict__
    else:
      return False
