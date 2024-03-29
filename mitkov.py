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
    finals = []
    for anaphora in self.anaphoras:
      final = anaphora.run_algorithm()
      if final is None:
        print("--- NO ANAPHORA FOUND FOR ", anaphora.pronoun)
      else:
        finals.append(final)
    print("---anaphoras", self.anaphoras)
    print("--- finals", finals)

  def get_pronouns(self):
    pronouns = []
    for sentence in self.sentences:
      for word in sentence.words:
        if word.type == WordType.PRONOUN:
          self.compute_after_verb(word)
          word.pattern = sentence.get_colocation_pattern()
          pronouns.append(word)
    return pronouns
  
  def get_anaphoras(self):
    pronouns = self.get_pronouns()
    # code.interact(local=dict(globals(), **locals()))
    for pronoun in pronouns:
      anaphora = AnaphoraCandidates(pronoun)
      recent_count = 0
      preceding_sentences = 0
      pronoun_found = False
      first_sentence = True
      for sentence in self.sentences:
        if pronoun_found:
          preceding_sentences += 1
        if preceding_sentences > 0: #pronoun already found, don't go further in th text. This is just anaphora.
          break
        for phrase in sentence.phrases.values():
          # code.interact(local=dict(globals(), **locals()))
          if phrase.type == WordType.NOUN:
            at_least_one_found = False
            for word in phrase.words:
              word.pattern = sentence.get_colocation_pattern()
              if word.type == WordType.NOUN and anaphora.agrees(word):
                at_least_one_found = True
                reiteration = self.get_reiteration_count(word)
                self.compute_after_verb(word)
                distance = self.get_distance(pronoun, word)
                prev_word = self.get_previous_word(word)
                candidate = Candidate(
                    word, first_sentence, reiteration, distance, recent_count, prev_word)
                anaphora.add_candidate(candidate)
                recent_count += 1
            if not at_least_one_found: #no specific word agrees with pronoun, try whole phrase
              phrase.compute_phrase_gender_number()
              if anaphora.agrees(phrase):
                recent_count += 1
                for word in phrase.words:
                  if word.type == WordType.NOUN:
                    reiteration = self.get_reiteration_count(word)
                    self.compute_after_verb(word)
                    distance = self.get_distance(pronoun, word)
                    prev_word = self.get_previous_word(word)
                    # candidate with multiple
                    candidate = Candidate(
                        word, first_sentence, reiteration, distance, recent_count, prev_word, True)
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
    if distance <= 2:
      return 2-distance
    else:
      return 2


