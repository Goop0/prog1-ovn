import math #en kodning som berättar vilken omkrets och area en cirkel har med vis radie
a = float(input('radie'))
if a>0: #om det är mer än 0 så räknar programmet ut det inskrivna värdet
    b = 3.14
    area = b* a**2
    omkrets= 2*b*a
    print('arean på cikeln', area)
    print('omkretsen på cirkeln', omkrets)
else:
    print('gör om rut')
    

    