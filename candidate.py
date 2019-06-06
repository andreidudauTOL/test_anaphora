import code

class Candidate:
  def __init__(self, word, first_sentence, reiteration_score, distance_score):
    self.word = word
    self.np_ind = 0
    self.definite_score = 0
    self.preposition_score = 0
    self.first_sentence = first_sentence
    self.first_sentence_score = 0
    self.reiteration_score = reiteration_score
    self.resolving_it_score = 0
    self.distance_score = distance_score

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
    # print(noun)
    # print(self.pronoun.gender, noun.gender, self.pronoun.number, noun.number)
    return (self.pronoun.gender == noun.gender and self.pronoun.number == noun.number) or noun.proper == True
  
  def run_algorithm(self):
    for candidate in self.candidates:
      self.definiteness_1(candidate)
      self.preposition_2(candidate)
      self.first_sentence_3(candidate)
      self.indicating_verbs_4(candidate)
      self.lexical_reiteration_5(candidate)
      self.term_in_genre_6(candidate)
      self.collocation_pattern_7(candidate)
      self.rezolving_it_8(candidate)
      self.referential_distance_9(candidate)

  
  def definiteness_1(self, candidate):
    if not candidate.word.definite:
      candidate.np_ind -= 1
      candidate.definite_score = -1
  
  def preposition_2(self, candidate):
    if candidate.word.preposition:
      candidate.np_ind -= 1
      candidate.preposition_score = -1
  
  def first_sentence_3(self, candidate):
    if candidate.first_sentence:
      candidate.np_ind += 1
      self.first_sentence_score = 1
  
  def indicating_verbs_4(self, candidate):
    pass

  def lexical_reiteration_5(self, candidate):
    candidate.np_ind += candidate.reiteration_score
  
  def term_in_genre_6(self, candidate):
    pass
  
  def collocation_pattern_7(self, candidate):
    pass
  
  def rezolving_it_8(self, candidate):
    if self.pronoun.after_verb and candidate.word.after_verb:
      candidate.np_ind += 2
      candidate.resolving_it_score = 2
  
  def referential_distance_9(self, candidate):
    # pass
    candidate.np_ind += candidate.distance_score
  
  def __str__(self):
    return "\npron: " + str(self.pronoun) + " | candidates: " + str(self.candidates)

  def __repr__(self):
    return str(self)
