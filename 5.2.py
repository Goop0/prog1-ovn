t = str(input('skriv en text '))
print(len(t))
print(f'det första tecknet är {t[0]}')
h = len(t) 
h = h -1
print(f'det sista tecknet är {t[h]}')
if t[0]==t[h]:
    print('båda har samma tecken')
elif t[0] != t[h]:
    print('båda har inte samma tecken')