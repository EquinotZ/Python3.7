# use landscape mode

poem='''Set among hills in the midst of five valleys,
Once home of the cloth it gave its name to, 
This peaceful little market town we inhabit
Refuses vociferously to be a conformer. 
Uphill and down again its streets lead you. 
Despite its faults it leaves us all charmed.'''


word =''
# leave blank to find one automatically

def check_word(word, verbose=False):
    word = word.strip('.,!?-;:&')
    lines = poem.split('\n')
    if len(lines) != len(word):
        if verbose:
            print('length of word doesn\'t',
            'match length of poem')
        return False 
    combo = zip(lines, word)
    for c in combo:
        line, letter = c
        if (letter.lower()
        not in line.lower()):
            if verbose:
                print('error: letter',
                repr(letter), 'not in line',
                repr(line))
            return False 
    return True 

def find_words():
    return [word.strip('.,!?-;:&')
    for word in poem.split()
    if check_word(word)]

if (not word or
    not check_word(word, verbose=True)):
    w = find_words()
    if w:
        from random import choice
        word = choice(w)

def acrostic_poem(poem, word):
    lines = poem.split('\n')
    if not check_word(word, verbose=True):
        return None
    combo = zip(lines, word)
    indices = []
    offset = None
    combo = zip(lines, word)
    for c in combo:
        line, letter = c
        indices.append([n for n in
        range(len(line)) if line[n].lower()
        == letter.lower()])
        
        if (len(indices[-1]) == 1 and
        (not offset or offset
        < indices[-1][0])):
            offset = indices[-1][0]
        elif len(indices[-1]) > 1 and (not
        offset or all(n > offset for n
        in indices[-1])):
            offset = min(indices[-1])
    
    i = 0
    for h in zip(lines, indices):
        line, offsets = h
        if len(offsets) == 1:
            o = offsets[0]
        else:
            # find best offset
            u = 0
            while True:
                if offset+u in offsets:
                    o = offset+u
                    break
                u -= 1
        print(' ' * (offset-o) + line[:o]
        + '*' + word[i].upper() + '*'
        + line[o+1:])
        i += 1

if word:
    acrostic_poem(poem, word)
else:
    print('no word')
