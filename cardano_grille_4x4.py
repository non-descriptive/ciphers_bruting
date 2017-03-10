'''Bruteforce algorithm for solving 4x4 Cardano grille'''

'''TEST CASES'''
bgrille = '''БУОП СТВЕ КРКВ АЕАН''' #resulting 'ПЕРЕСТАНОВКА БУКВ'
tgrille = '''перт чаис иквр каав''' #resulting 'приветкрасавчика'
def clear_mask(mask):
    '''change mask format from XXXX XXXX XXXX XXXX to XXXXXXXXXXXXXXX'''
    return ''.join(mask.split(' '))

def norm_mask(clear_mask):
    '''change mask format from XXXXXXXXXXXXXXX to XXXX XXXX XXXX XXXX'''
    return clear_mask[0:4]+" "+clear_mask[4:8]+" "+clear_mask[8:12]+" "+clear_mask[12:16]

def turn(mask):
    '''returns mask turned 90 degree clockwise'''
    oldmask = clear_mask(mask)
    newmask = list("0000000000000000")
    turns = [
        (0,3),
        (1,7),
        (2,11),
        (3,15),
        (4,2),
        (5,6),
        (6,10),
        (7,14),
        (8,1),
        (9,5),
        (10,9),
        (11,13),
        (12,0),
        (13,4),
        (14,8),
        (15,12)
    ]
    for i in range(len(oldmask)):
        if oldmask[i] =='1':
            idx = turns[i][1]
            newmask[idx]='1'
    newmask = ''.join(newmask)

    final = norm_mask(newmask)
    return final;


def test_turn_collapse(masks):
    '''correct masks should collapse to zero. returns true if collapsed'''
    mask1 = int("0b"+clear_mask(masks[0]),2)
    mask2 = int("0b"+clear_mask(masks[1]),2)
    mask3 = int("0b"+clear_mask(masks[2]),2)
    mask4 = int("0b"+clear_mask(masks[3]),2)
    return (mask1 & mask2 & mask3 & mask4) == 0


def testlen(masks):
    '''correct grille should have no more than side size holes'''
    x = True
    for mask in masks:
        holes_count = mask.count('1')
        if holes_count != 4:
            return  False
    return True

def gen_turns(mask):
    '''returns tuple with all four turns for mask'''
    mask1 = mask
    mask2 = turn(mask1)
    mask3 = turn(mask2)
    mask4 = turn(mask3)
    return (mask1, mask2, mask3, mask4)

def print_message(mask, grille):
    '''deciphered message for mask and grille'''
    turns=gen_turns(mask)
    message = ""
    for mask in turns:
        for n in range(len(mask)):
            if mask[n] == '1':
                message+=grille[n]
    print(mask, message)

# maximal size of mask for 4x4 grille
maxmask = 65535

if __name__ == "__main__":
    masks = []
    for i in range(maxmask):
        # making mask from integer
        curr_mask = norm_mask("{0:016b}".format(i))
        turns = gen_turns(curr_mask)
        # checking mask correctness
        isgood = test_turn_collapse(turns) and testlen(turns)
        if isgood:
            # final output
            print_message(curr_mask, bgrille)
