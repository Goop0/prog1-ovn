svar = int(input('skriv in ett heltal: '))

inmatning = svar % 2

if inmatning == 1:
    print(f'Talet {svar} är ojämnt.')
else :
    print(f'Talet {svar} är jämnt.')