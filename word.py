from xces_word import XcesWord
from constants import WordType, Gender, Number
import code

female_names = []
f = open("female_names.txt", "r")
for x in f:
  female_names.append(x.replace(' ', '').replace('\n', ''))

male_names = []
f = open("male_names.txt", "r")
for x in f:
  male_names.append(x.replace(' ', '').replace('\n', ''))


class Word(XcesWord):

  def __init__(self, word, attributes):
    super().__init__(word, attributes)
    self.gender = Gender.M
    self.number = Number.SINGURLAR
    self.proper = False
    self.definite = False
    self.preposition = False
    self.after_verb = False
    self.pattern = []
    self.index_in_sentence = 0
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
        if self.lemma in female_names:
          self.gender = Gender.F
  

