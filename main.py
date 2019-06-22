import code
# code.interact(local=dict(globals(), **locals()))
from mitkov import Mitkov

# response = Ttl.pos_tag("Maria are blănuri. Ele sunt foarte frumoase.")
# sentences = Sentence.get_all_sentences("Maria are blănuri? Ele sunt foarte frumoase.")
# "Lupoaica are blănuri. Ele sunt foarte frumoase și sunt pe mese."
# Soldatul a luat mașina și copiii, a spălat-o, a curățat-o și a înapoiat-o.
# "Câinele și băiatul sunt afară. Ei sunt cuminți."
# Soldatul a luat mașina și copiii, a spălat-o, a curățat-o și a înapoiat-o. Ea este curată. Maria și Andrei iubesc mașina lui.
# Maria cântă la pian. Ea cântă foarte frumos. Tatăl său a învățat-o să cânte la pian. El este bătrân.
text = "Soldatul a luat mașina și copiii, a spălat-o, a curățat-o și a înapoiat-o. Ea este curată. Maria și Andrei iubesc mașina lui."
text = text.replace(','," ")
text = text.replace(':', " ")
text = text.replace(';', " ")
text = text.replace('\"', " ")
text = text.replace('\'', " ")
print(text)
mitkov = Mitkov(text)
mitkov.anaphora_resolution()
