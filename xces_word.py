from constants import WordType

class XcesWord(object):

  def  __init__(self, word, attributes):
    self.original = word
    if len(attributes.keys()) != 0:
      self.lemma = attributes['lemma']
      self.ana = attributes['ana']
      self.type = WordType(self.ana[0])
      if 'chunk' in attributes:
        self.chunk = attributes['chunk']
    else:
      self.type = WordType.END

  def is_word(self):
    return self.type == WordType.NOUN or self.type == WordType.PRONOUN

  def __str__(self):
    return "Word: " + self.original + " --- is_word: " + str(self.is_word())
  
  def __repr__(self):
    return str(self)
