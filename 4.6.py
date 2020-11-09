#beräkning av x upphöjt till n
x=float(input('x?'))
n= int(input('n?'))
k=1
for i in range(n):
    k=k * x
print('resultat', k)