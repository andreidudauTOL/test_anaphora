import code

class Candidate:
  def __init__(self, word):
    self.word = word
    self.np_ind = 0
    self.definite_score = 0
    self.preposition_score = 0

  def __str__(self):
    return "Candidate: " + str(self.word.original) + "--- np_ind: " + str(self.np_ind)

  def __repr__(self):
    return str(self)

class AnaphoraCandidates:
  def __init__(self, pronoun):
    self.pronoun = pronoun
    self.candidates = []
  
  def add_candidate(self, candidate):
    self.candidates.append(candidate)
  
  def agrees(self, noun):
    print(noun)
    print(self.pronoun.gender, noun.gender, self.pronoun.number, noun.number)
    return (self.pronoun.gender == noun.gender and self.pronoun.number == noun.number) or noun.proper == True
  
  def run_algorithm(self):
    for candidate in self.candidates:
      self.definiteness_1(candidate)
      self.preposition_2(candidate)
  
  def definiteness_1(self, candidate):
    if not candidate.word.definite:
      candidate.np_ind -= 1
      candidate.definite_score = -1
  
  def preposition_2(self, candidate):
    if candidate.word.preposition:
      candidate.np_ind -= 1
      candidate.preposition_score = -1
  
  def __str__(self):
    return "pron: " + str(self.pronoun) + "\n--- candidates: " + str(self.candidates)

  def __repr__(self):
    return str(self)
