meter = 1
while meter > 0:
    meter = int(input('skriv en höjd i m '))
    
    centimeter = 100 * meter
    studsar = 0

    while centimeter > 1:
        centimeter = centimeter * 0.7
        studsar += 1
    print(f'boll blir täckt efter {studsar} studsar')
print('hejdå')
