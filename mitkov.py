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
    print(self.anaphoras)

  def get_pronouns(self):
    pronouns = []
    for sentence in self.sentences:
      for word in sentence.words:
        if word.type == WordType.PRONOUN:
          pronouns.append(word)
    return pronouns
  
  def get_anaphoras(self):
    pronouns = self.get_pronouns()
    for pronoun in pronouns:
      anaphora = AnaphoraCandidates(pronoun)
      preceding_sentences = 0
      pronoun_found = False
      for sentence in self.sentences:
        if pronoun_found:
          preceding_sentences += 1
        if preceding_sentences > 2:
          break
        code.interact(local=dict(globals(), **locals()))
        for phrase in sentence.phrases.values():
          # code.interact(local=dict(globals(), **locals()))
          if phrase.type == WordType.NOUN:
            for word in phrase.words:
              if word.type == WordType.NOUN and anaphora.agrees(word):
                anaphora.add_candidate(Candidate(word))
      self.anaphoras.append(anaphora)
