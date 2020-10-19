while True:
    n=int(input("n?, Skriv ett tal <=0 för att sluta: "))
    if n <= 0:
        break
    summa = 0
    k=1
    while k<=n:
        summa=summa+k
        k=k+1
    print("Summan blir", summa)

starthöjd = int(input('skriv en höjd i m '))
förlust = 0.7
höjd = starthöjd

while höjd > 0.01:
    höjd = höjd * förlust
    studsar = starthöjd/höjd
    studsar=int(studsar)
print(f'boll blir täckt efter {studsar} studsar')