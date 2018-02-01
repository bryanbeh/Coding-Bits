from tkinter import *
from IPython.display import clear_output
import random
import re

#caesar cipher encrypter, each text is encoded with a different sequence
def caesar_encrypt():
    alp = 'abcdefghijklmnopqrstuvwxyz'

    c = []

    text = e1_value.get()
    word = text.split()
    number = [random.randint(1,13) for x in range(len(word))]
    y = random.randint(0,1)
    counter = 0

    a = [[] for x in range(len(word))]
    b = [[] for x in range(len(word))]

    if y == 0:
        choice = 'left'

    else:
        choice = 'right'

    for element in word:
        counter += 1

        for i in element:
            a[counter-1].append(re.search(i, alp).start())


        for ind in a[counter-1]:
            if choice == 'right':
                b[counter-1].append(alp[ind+number[counter-1]-26])
            else:
                b[counter-1].append(alp[ind-number[counter-1]])

            thing = ''.join(b[counter-1])


        c.append(thing)

    d = ' '.join(c)

    t1.insert(END, d + ' ')
#word database
import json
from difflib import get_close_matches

data = json.load(open("text copy.json"))

for i in 'bcdefghjklmnopqrstvwxyz':
    data.pop(i, None)

for i in 'jt lv mw oy sc td wg yi ak bl cm dn eo fp hr po qp sr ts ut vu xw az ba cb dc ed fe hg ji ml nm bo cp er fs gt hu iv ly na ob pc re sf tg uh vi bn co dp eq fr gs ht kw lx rd se ug wi vt wu ay bz ca db ec ge hf ki mk nl om sq tr tp ws bx cy dz ea hd lh mi nj pl qm ger sqd xvi mb od pe rg sh ti wl yn zo ap cr ds et fu gv hw ix alc par rct bsf ctg jan riv all doo grr tee xii vr ie rn adv log mph rum sri bar gung jule sty uva bch hin ijo dg eh fi il kn lo mp or ps qt sv ux ad be cf pix sla unc vod ati hap'.split():
    data.pop(i, None)

for i in 'bu fy ha ib le mf ng pi sl tm un vo yr zs jo ns ot pu qv va wb xc yd af bg ch di gl wr xs yt av dy fa id lg mh ni pk ql rm sn pg qh tk ar bs ct du fw hy ja kb lc md ne ai ck dl em fn hp iq jr lt mu nv ow qy sa tb uc vd gur jg li ol qn ro sp vs wt xu ax by da fc gd op pq qr rs st tu za ab cd de ef fg hi kl lm mn ju kv ny oz pa rc sd te vg wh xi al bm ep gr hs doo grr tee xii kran esp max sgd pdq rfs aob kyl coo lxx siol prau hm bits boe huk orra sho tip cry fub lah clo lux rad gau mr ngai og ph sk um wo as bt cu ew ia kc ld'.split():
    data.pop(i, None)

def word_check(w):
    w = w.lower()
    p = w[0].upper() + w[1:].lower()
    z = []
    if w in data:
        return w

    elif p in data:
        return p

    else:
        pass
#caesar cipher decoder

def caesar_decode():
    text = e1_value.get()
    word = re.split(', |  | ', text)
    alp = 'abcdefghijklmnopqrstuvwxyz'
    counter = 0
    print(word)

    u = [[] for x in range(len(word))]
    v = [[] for x in range(len(word))]
    d = [[] for x in range(len(word))]

    for element in word:
        counter += 1
        for letter in element:
            u[counter-1].append(re.search(letter, alp).start())
        for n in range(len(alp)):
            for ind in u[counter-1]:
                v[counter-1].append(alp[ind+n-26])
        for n in range(len(alp)):
            d[counter-1].append(''.join(v[counter-1][n*len(element):(n+1)*len(element)]))


    return d


def caesar_check():
    clear_output()
    c = caesar_decode()
    e = []
    for element in c:
        for i in element:
            e.append(word_check(i))

    a = [x for x in e if x != None]
    g = ' '.join(a)

    t1.insert(END, g + ' ')

window = Tk()

b1 = Button(window, text='Encode', font = 'Optima', activebackground = 'red', command = caesar_encrypt)
b1.grid(row = 1, column = 0)

b2 = Button(window, text='Decode', font = 'Optima', activebackground = 'red', command = caesar_check)
b2.grid(row = 2, column = 0)


e1_value = StringVar()
e1 = Entry(window, textvariable = e1_value, width = 30)
e1.grid(row = 0,column = 1)

t1 = Text(window, height = 5, width = 40)
t1.grid(row = 1, column = 1, rowspan = 2 )

l1= Label(window,text="Caesar Encrypter/Decoder")
l1.grid(row=0,column=0)

window.mainloop()
