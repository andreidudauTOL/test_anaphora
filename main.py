import code
# code.interact(local=dict(globals(), **locals()))
from mitkov import Mitkov

# response = Ttl.pos_tag("Maria are blănuri. Ele sunt foarte frumoase.")
# sentences = Sentence.get_all_sentences("Maria are blănuri? Ele sunt foarte frumoase.")
# "Lupoaica are blănuri. Ele sunt foarte frumoase și sunt pe mese."
# code.interact(local=dict(globals(), **locals()))
mitkov = Mitkov("Soldatul a luat mașina, a spălat-o, a curățat-o și a înapoiat-o.")
mitkov.anaphora_resolution()
