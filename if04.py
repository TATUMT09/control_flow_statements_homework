def main(a,b,c):
    """
    Find how many positive numbers there are in the given numbers.
    Args:
        a: integer
        b: integer
        c: integer
    returns:
        integer: the number of positive numbers in the given numbers
            Berilgan sonlarda nechta musbat son borligini toping.
    Args:
        a: butun son
        b: butun son
        c: butun son
    qaytaradi:
        butun son: berilgan sonlardagi musbat sonlar soni
    """
  
    musbat=0
    if a>0:
        musbat +=1
    if b>0:
        musbat+=1
    if c>0:
        musbat+=1  
        
    return musbat
a=int(input())
b=int(input())
c=int(input())
musbat=main ( a, b, c) 
print("Berilgan musbat sonlarda",musbat,"ta musbat son" )