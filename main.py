import code
# code.interact(local=dict(globals(), **locals()))
from mitkov import Mitkov

# response = Ttl.pos_tag("Maria are blănuri. Ele sunt foarte frumoase.")
# sentences = Sentence.get_all_sentences("Maria are blănuri? Ele sunt foarte frumoase.")
# "Lupoaica are blănuri. Ele sunt foarte frumoase și sunt pe mese."
# Soldatul a luat mașina, a spălat-o, a curățat-o și a înapoiat-o.
# code.interact(local=dict(globals(), **locals()))
text = "Câinele și băiatul sunt afară. Ei sunt cuminți."
text = text.replace(','," ")
text = text.replace(':', " ")
text = text.replace(';', " ")
text = text.replace('\"', " ")
text = text.replace('\'', " ")
mitkov = Mitkov(text)
mitkov.anaphora_resolution()
