from xces_word import XcesWord
from constants import WordType, Gender, Number
import code

class Word(XcesWord):

  def __init__(self, word, attributes):
    super().__init__(word, attributes)
    self.gender = Gender.M
    self.number = Number.SINGURLAR
    self.proper = False
    self.definite = False
    self.preposition = False
    self.after_verb = False
    if self.type == WordType.PRONOUN:
      self.gender = Gender(self.ana[3])
      self.number = Number(self.ana[4])
    else:
      if len(self.ana) > 2:
        self.gender = Gender(self.ana[2])
        self.number = Number(self.ana[3])
        if self.ana[5] == "y":
          self.definite = True
      else:
        self.proper = True
  

