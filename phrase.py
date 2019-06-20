from constants import WordType, Gender, Number

class Phrase():
  def __init__(self, word, phrase_type):
    self.words = []
    self.type = WordType(phrase_type[0])
    self.order = int(phrase_type[-1])
    self.add_to_phrase(word)
    self.gender = Gender.F
    self.number = Number.SINGURLAR
  
  def add_to_phrase(self, word):
    if self.type == WordType.ADPOSITION:
      word.preposition = True
    self.words.append(word)
  
  def compute_phrase_gender_number(self):
    if self.type == WordType.NOUN:
      word_count = 0
      for word in self.words:
        word_count += 1
        if word.gender == Gender.M:
          self.gender = Gender.M
      if word_count > 1:
        self.number = Number.PLURAL
  
  def __str__(self):
    return "Phrase type: " + str(self.type) + " order: " + str(self.order) + " word count: " + str(len(self.words)) + " words: " + str(self.words)
  
  def __repr__(self):
    return str(self)
