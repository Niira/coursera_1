A = int(input())   # размер кирпича A*B*C
B = int(input())
C = int(input())
D = int(input())   # отверстие D*E
E = int(input())
X = 'NO'
if A * B <= D * E:
    if A <= D and B <= E or A <= E and B <= D:
        X = 'YES'
if A * C <= D * E:
    if A <= D and C <= E or A <= E and C <= D:
        X = 'YES'
if B * C <= D * E:
    if B <= D and C <= E or B <= E and C <= D:
        X = 'YES'
print(X)
