import time

import apytl

NTOTAL = 25
WAIT = 0.1


for emojikey, emojicode in apytl._EMOJI.items():
    tstring = 'Are these {} emojis?'.format(emojikey)
    vs = 'V'*len(tstring)
    print(tstring)
    print(vs)
    for ind, val in enumerate(range(NTOTAL)):
        apytl.drawbar(ind, NTOTAL, fill=emojicode)
        time.sleep(WAIT)
    print('')

tstring = 'Are these octothorpes?'
vs = 'V'*len(tstring)
print(tstring)
print(vs)
for ind, val in enumerate(range(NTOTAL)):
    apytl.drawbar(ind, NTOTAL)
    time.sleep(WAIT)
print('')

tstring = 'Are these randomly selected?'
vs = 'V'*len(tstring)
print(tstring)
print(vs)
for ind, val in enumerate(range(NTOTAL)):
    apytl.drawbar(ind, NTOTAL, fill='random')
    time.sleep(WAIT)
print('')
