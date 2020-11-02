import random
gissa = 0
försök=0
correct = random.randint (1,10000)
while gissa !=correct:
    försök+=1
    gissa=int(input('skriv en gissing '))
    if gissa <correct:
        print('högre')
        
    elif gissa >correct:
        print('mindre')
        
else: 
    print('korrekt')
print('antal försök', försök)