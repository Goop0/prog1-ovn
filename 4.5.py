starthöjd = 1
while starthöjd >0:
    starthöjd = int(input('skriv en höjd med heltal och i meter '))
    if starthöjd <=0:
          
        print('skriv ett tal som inte är negativt eller 0')
        break
    elif starthöjd >0.01:
        studsar = 0
        while starthöjd > 0.01:
            starthöjd = starthöjd * 0.7
            studsar += 1
        print(f'bollen stannar efter {studsar} studsar')