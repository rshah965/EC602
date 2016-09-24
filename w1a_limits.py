# Author Rishab Shah rishah@bu.edu

Table = "{:<6} {:<22} {:<22} {:<22}"

def cplclc(a):
    b=2**(8*a)-1
    c=-2**((8*a)-1)
    d=2**((8*a)-1)-1     
    print(Table.format(a,b,c,d))
    return;
print(Table.format('Bytes','Largest Unsigned Int','Minimum Signed Int','Maximum Signed Int'))
cplclc(1)
cplclc(2)
cplclc(4)
cplclc(8)
