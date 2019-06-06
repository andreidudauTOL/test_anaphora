from constants import WordType

class Phrase():
  def __init__(self, word, phrase_type):
    self.words = []
    self.type = WordType(phrase_type[0])
    self.order = int(phrase_type[-1])
    self.add_to_phrase(word)
  
  def add_to_phrase(self, word):
    if self.type == WordType.ADPOSITION:
      word.preposition = True
    self.words.append(word)
  
  def __str__(self):
    return "Phrase type: " + str(self.type) + " order: " + str(self.order) + " word count: " + str(len(self.words)) + " words: " + str(self.words)
  
  def __repr__(self):
    return str(self)
