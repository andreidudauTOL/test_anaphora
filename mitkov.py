from sentence import Sentence, WordType
from candidate import AnaphoraCandidates, Candidate
import code

class Mitkov():
  def __init__(self, text):
    self.sentences = Sentence.get_all_sentences(text)
    print(self.sentences)
    self.anaphoras = []
  
  
  def anaphora_resolution(self):
    self.get_anaphoras()
    for anaphora in self.anaphoras:
      anaphora.run_algorithm()
    print("---anaphoras", self.anaphoras)

  def get_pronouns(self):
    pronouns = []
    for sentence in self.sentences:
      for word in sentence.words:
        if word.type == WordType.PRONOUN:
          self.compute_after_verb(word)
          pronouns.append(word)
    return pronouns
  
  def get_anaphoras(self):
    pronouns = self.get_pronouns()
    # code.interact(local=dict(globals(), **locals()))
    for pronoun in pronouns:
      anaphora = AnaphoraCandidates(pronoun)
      preceding_sentences = 0
      pronoun_found = False
      first_sentence = True
      for sentence in self.sentences:
        if pronoun_found:
          preceding_sentences += 1
        if preceding_sentences > 2:
          break
        for phrase in sentence.phrases.values():
          # code.interact(local=dict(globals(), **locals()))
          if phrase.type == WordType.NOUN:
            for word in phrase.words:
              if word.type == WordType.NOUN and anaphora.agrees(word):
                reiteration = self.get_reiteration_count(word)
                self.compute_after_verb(word)
                distance = self.get_distance(pronoun, word)
                candidate = Candidate(word, first_sentence, reiteration, distance)
                anaphora.add_candidate(candidate)
        first_sentence = False
      self.anaphoras.append(anaphora)
  
  def get_reiteration_count(self, word):
    count = -1
    for sentence in self.sentences:
      for iterator_word in sentence.words:
        if iterator_word.type == WordType.NOUN and word.lemma == iterator_word.lemma and count<2:
          count += 1
    return count
  
  def compute_after_verb(self, word):
    prev_word = self.get_previous_word(word)
    if prev_word is not None and prev_word.type == WordType.VERB:
      word.after_verb = True
  

  def get_previous_word(self, word):
    for sentence in self.sentences:
      # if x is not None:
      prev_word = None
      for iterator_word in sentence.words:
        if iterator_word == word:
          return prev_word
        else:
          prev_word = iterator_word
    return prev_word

  def get_distance(self, pronoun, word):
    pronoun_sentence = 0
    noun_sentence = 0
    pronound_found = False
    noun_found = False
    # code.interact(local=dict(globals(), **locals()))
    for sentence in self.sentences:
      if not pronound_found:
        pronoun_sentence += 1
      if not noun_found:
        noun_sentence += 1
      for iterator_word in sentence.words:
        if iterator_word == pronoun:
          pronound_found = True
        if iterator_word == word:
          noun_found = True
    distance = abs(pronoun_sentence - noun_sentence)
    print("---- distance", distance)
    if distance <= 2:
      return 2-distance
    else:
      return 2


