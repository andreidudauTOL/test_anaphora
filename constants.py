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

@unique 
class Gender(Enum):
  M = "m"
  F = "f"

@unique
class Number(Enum):
  SINGURLAR = "s"
  PLURAL = "p"