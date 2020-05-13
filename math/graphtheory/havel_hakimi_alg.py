
def hh(seq):
    seq = list(filter(lambda x: x>0, seq))
    while(seq):
        seq.sort(reverse=True)
        elt = seq.pop()
        if(elt > len(seq)): 
            return False
        seq = list(map(lambda x: x-1, seq[:elt])) + seq[elt:]
        seq = list(filter(lambda x: x>0, seq))
    return True        
        

msg = "Error!"
assert hh([5, 3, 0, 2, 6, 2, 0, 7, 2, 5]) == False, msg
assert hh([4, 2, 0, 1, 5, 0]) == False, msg
assert hh([3, 1, 2, 3, 1, 0]) == True, msg
assert hh([16, 9, 9, 15, 9, 7, 9, 11, 17, 11, 4, 9, 12, 14, 14, 12, 17, 0, 3, 16]) == True, msg
assert hh([14, 10, 17, 13, 4, 8, 6, 7, 13, 13, 17, 18, 8, 17, 2, 14, 6, 4, 7, 12]) == True, msg
assert hh([15, 18, 6, 13, 12, 4, 4, 14, 1, 6, 18, 2, 6, 16, 0, 9, 10, 7, 12, 3]) == False, msg
assert hh([6, 0, 10, 10, 10, 5, 8, 3, 0, 14, 16, 2, 13, 1, 2, 13, 6, 15, 5, 1])  == False, msg
assert hh([2, 2, 0])   == False, msg
assert hh([3, 2, 1])  == False, msg
assert hh([1, 1]) == True, msg
assert hh([1])  == False, msg
assert hh([]) == True, msg
