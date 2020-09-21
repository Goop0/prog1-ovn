svar = int(input('skriv in antalet sekunder: ')) # antalet sekunder du skriver in
sek = int(svar) # konverterar svaret till ett heltal

dag = sek // 86400 
sek = sek % 86400
tim = sek // 3600 #delar antalet sekunder med antalet sekunder på en timme 
sek = sek % 3600 #använder modulo för att räkna ut antalet sekunder som blev över från timmarna
min = sek // 60
sek = sek % 60


print(f'dagar: {dag} \ntimmar: {tim} \nMinuter: {min} \nSekunder: {sek}')