

two = 'two'
four = 'four'
seq='1234567890'
uniq = list(set([c for c in two + four]))
conv = {k:v for k,v in zip(uniq, seq)}


def test_win(two, four, conv):
    two_n = ''
    four_n = ''
    for c in two:
        two_n += conv[c]
    for c in four:
        four_n += conv[c]
    if int(two_n) + int(two_n) == int(four_n):
        return True
    else:
        return False


def rec_search(two, four, conv, layer=0):
    
    if layer == len(uniq) or len(set(conv.values())) != len(uniq):
        return False
    if test_win(two, four, conv):
        return conv
    for n in seq:
        new_conv = conv.copy()
        new_conv[uniq[layer]] = n
        attempt = rec_search(two, four, new_conv, layer+1)
        if attempt:
            return attempt
        

result_conv = rec_search(two, four, conv)




        
