from enum import Enum, unique
@unique
class WordType(Enum):
  NOUN = "N"
  VERB = "V"
  ADJECTIVE = "A"
  PRONOUN = "P"
  DETERMINER = "D"
  ARTICLE = "T"
  ADVERB = "R"
  ADPOSITION = "S"
  CONJUNCTION = "C"
  NUMERAL = "M"
  INTERJECTION = "I"
  RESIDUAL = "X"
  ABBREVIATION = "Y"
  PARTICLE = "Q"
  END = "."
  PUNCTUATION = ","
  PUNCTUATION2 = ";"
  PUNCTUATION3 = ":"
  SHORT_PRONOUN = "-"

  @staticmethod
  def is_punctuation(word_type):
    return word_type == WordType.PUNCTUATION or word_type == WordType.PUNCTUATION2 or word_type == WordType.PUNCTUATION3

@unique 
class Gender(Enum):
  M = "m"
  F = "f"

@unique
class Number(Enum):
  SINGURLAR = "s"
  PLURAL = "p"
