import code
# code.interact(local=dict(globals(), **locals()))
from mitkov import Mitkov

# response = Ttl.pos_tag("Maria are blănuri. Ele sunt foarte frumoase.")
# sentences = Sentence.get_all_sentences("Maria are blănuri? Ele sunt foarte frumoase.")
# code.interact(local=dict(globals(), **locals()))
mitkov = Mitkov("Lupoaica are blănuri. Ele sunt foarte frumoase și sunt pe mese.")
mitkov.anaphora_resolution()
