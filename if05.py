def nomer(a,b,c):
 """
    Find how many negative numbers there are in the given numbers.
    Args:
        a: integer
        b: integer
        c: integer
    returns:
        integer: the number of negative numbers in the given numbers
    """
 nomer=0
 if a<0:
    nomer+=1
 if b<0:
    nomer+=1
 if c<0:
    nomer+=1
    return nomer
 a=3
 b=-3
 c=4
 print(nomer())