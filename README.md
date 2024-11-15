Manual för Krypterings- och Dekrypteringsprogram

Detta program låter dig enkelt kryptera och dekryptera filer. Alla krypteringsnycklar sparas automatiskt i en JSON-fil, så du behöver inte tänka på eller hantera nycklarna manuellt.
Användningsexempel

För att kryptera en fil, skriv:

    python3 crypt.py encrypt dokument.txt
        Krypterar dokument.txt och skapar en nyckel som automatiskt lagras för framtida dekryptering.

För att dekryptera en fil, skriv:

    python3 crypt.py decrypt dokument.txt_encrypted
        Dekrypterar dokument.txt_encrypted och sparar den som dokument.txt_decrypted, så länge rätt nyckel finns lagrad.

Felhantering

Programmet informerar om:

    Filen saknas eller om fel filnamn anges.
    Nyckeln saknas för dekryptering.
    Argument är ogiltiga eller saknas.

Du kan alltså fokusera på filerna, så sköter programmet alla nycklar åt dig!
