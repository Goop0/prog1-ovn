ng = 0
x=int(input('x värde?'))
b=2*x**2 - 5*x +1
for i in range (-10, 11, b):
    ng = ng +1
    i = i/10

    print(i) 

print('du fick', ng, 'som värde')