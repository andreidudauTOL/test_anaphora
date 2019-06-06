from constants import WordType

class Phrase():
  def __init__(self, word):
    self.words = []
    self.type = WordType(word.chunk[0])
    self.order = int(word.chunk[-1])
    self.add_to_phrase(word)
  
  def add_to_phrase(self, word):
    if self.type == WordType.ADPOSITION:
      word.preposition = True
    self.words.append(word)
  
  def __str__(self):
    return "Phrase type: " + str(self.type) + " order: " + str(self.order) + " word count: " + str(len(self.words)) + " words: " + str(self.words)
  
  def __repr__(self):
    return str(self)
