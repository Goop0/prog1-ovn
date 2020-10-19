starthöjd = int(input('skriv en höjd i m '))
förlust = 0.7
höjd = starthöjd

while höjd > 0.01:
    höjd = höjd * förlust
    studsar = starthöjd/höjd
    studsar=int(studsar)
print(f'boll blir täckt efter {studsar} studsar')