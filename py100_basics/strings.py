print(len("These aren't the droids you're looking for."))
###
confetti = 'confetti floating everywhere'
big_confetti = confetti.upper()
print(big_confetti)
###
name = 'Roger'

if name.casefold() == 'RoGeR'.casefold():
    print('true')
else:
    print('false')
###
pirate = '''A pirate I was meant to be!
Trim the sails and roam the sea!'''
print(pirate)
###
char_sequence = 'TXkgaG92ZXJjcmFmdCBpcyBmdWxsIG9mIGVlbHMu'
print('x' in char_sequence)
###
def is_empty(string_in):
    if bool(string_in) != True:
        return True
    else:
        return False
    
print(is_empty('pears'))
print(is_empty(''))
###
def is_empty_or_blank(in_str):
    return not in_str or in_str.isspace()
    
print(is_empty_or_blank('watermelon'))
print(is_empty_or_blank('   '))
print(is_empty_or_blank(''))
###
title = 'launch school tech & talk'

print(title.title())
###
def starts_with(string1, prefix):
    return string1.startswith(prefix)

print(starts_with('Mr. Hodges', 'Mr.'))
print(starts_with('Mr. Hodges', 'Cpt'))
###
def count_substrings(string2, sub2):
    return string2.count(sub2)