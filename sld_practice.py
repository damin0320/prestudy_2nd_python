from __future__ import print_function
A = "Wecode"
B = [1, 2, 3, 4, 5, 6, 7]
C = {'Irene' : 'Leader', 'Seulgi' : 'Dancer', 'Wendy' : 'Vocal', 'Joy':'Sub_vocal', 'Yeri': 'Sub_rapper'}

def sld():
    for i in A:
        print(i, end = "")
    
    for j in B:
        print(j, end = "")
    
    for k, v in C.items():
        print(k, v, end = "")

print(sld())