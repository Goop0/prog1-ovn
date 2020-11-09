while True:
    starthöjd = int(input('skriv en höjd med heltal och i meter '))
    if starthöjd <=0:
          
        print('skriv ett tal som inte är negativt eller 0')
        break
    elif starthöjd >0:
        förlust = 0.7
        höjd = starthöjd
        while höjd > 0.01:
            höjd = höjd * förlust
            studsar = starthöjd/höjd
            studsar=int(studsar)
        print(f'bollen stannar efter {studsar} studsar')