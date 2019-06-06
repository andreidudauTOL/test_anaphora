from constants import WordType
from xces_word import XcesWord
from word import Word
from ttl import Ttl
import xml.etree.ElementTree as ET

class WordParser:
  @staticmethod
  def use_word_class(word):
    if len(word.attrib.keys()) != 0:
      type = WordType(word.attrib['ana'][0])
      if type == WordType.NOUN or type == WordType.PRONOUN:
        return True
    return False

  # Ttl.pos_tag("Maria are blănuri. Ele sunt foarte frumoase.")
  @staticmethod
  def get_all_words(text):
    words = []
    pos_text = Ttl.pos_tag(text)
    xml = ET.fromstring("<root>" + pos_text + "</root>")
    for child in xml:
      for word in child[0]:
          print("--- word", word.text, word.attrib)
          if WordParser.use_word_class(word):
            w = Word(word.text, word.attrib)
            if w.is_short_pronoun():
              print("--short", w, w.chunk)
              w.compute_order_for_short_pronoun(words[-1])
              print("--short2", w, w.chunk)
            words.append(w)
            # print("--- word", w.original, w.type)
          else:
            xw = XcesWord(word.text, word.attrib)
            words.append(xw)
            # print("--- xces_word", xw.original, xw.type)
    return words
