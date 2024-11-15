Manual för Krypterings- och Dekrypteringsprogram

Detta program låter dig enkelt kryptera och dekryptera filer. Alla krypteringsnycklar sparas automatiskt i en JSON-fil, så du behöver inte tänka på eller hantera nycklarna manuellt.
Användningsexempel:

För att kryptera en fil, skriv:

python3 crypt.py encrypt dokument.txt
    

För att dekryptera en fil, skriv:

python3 crypt.py decrypt dokument.txt_encrypted

Felhantering

Programmet informerar om:

Filen saknas eller om fel filnamn anges.
Nyckeln saknas för dekryptering.
Argument är ogiltiga eller saknas.

Du kan alltså fokusera på filerna, så sköter programmet alla nycklar åt dig!
