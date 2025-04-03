# Övning 6 grudat25
### Deadline: Onsdag 30/4 kl 19:00

Mål:
 - formulera och implementera rekursiva algoritmer
 - skriva och använda enkel BNF-syntax
 - konstruera och använda reguljära uttryck

**Vid övningen ska du vara beredd att muntligt presentera och diskutera dina lösningar och din programkod. Du ska också ha med en utskrift av din inlämning för kamratgranskning på övningen.**

- Gör (minst) en fil per uppgift och lägg filerna i katalogen <code>username-ovn6</code> i organisationen [grudat25 på KTH GitHub](https://gits-15.sys.kth.se/grudat25).
- Utgå från mallarna i [/grudat25/ovn0/](https://github.com/isakemma/grudat/tree/master/ovn0).
- Lösningar ska vara inlämnade före deadline.

Den här gången ska du testa vissa av dina lösningar på Kattis 
innan du lämnar in dem på ditt githubkonto. Om du inte gjorde övning 1 behöver du först registrera dig på kursen.

1. Du får tillgång till Kattis genom att [logga in](https://kth.kattis.com/login) med ditt KTH-id.
2. Du måste också [registrera dig på grudat25](https://kth.kattis.com/courses/DD1327/grudat25/register) i Kattis. 



## Betyg G
### Dynamisk programmering

<!-- CC BY-SA 2.0: https://www.flickr.com/photos/bekathwia/5148701602 -->
![Knitting machine HACKED](https://github.com/isakemma/grudat/blob/master/knitting-machine-hacked.jpg)

[Hacking the Brother KH-930e Knitting Machine](https://www.youtube.com/watch?v=GhnTSWMMtdU)

En F-teknolog har kommit över en stickmaskin och ett parti garn och planerar att sticka och sälja halsdukar.

Efter en noggrann marknadsundersökning har teknologen sammanställt en tabell över priset på olika typer av halsdukar:
h[n] är det högsta priset på en halsduk som man kan sticka av n meter garn.

För att tjäna så mycket pengar som möjligt vill vi förstås hitta en optimal kollektion.
Följande rekursion beräknar den maximala inkomsten p(n) som man kan tjäna genom att sticka halsdukar av n meter garn:

> p(0) = 0,  
> p(n) = max<sub>1 &le; i &le; n</sub>(h[i] + p(n-i)) om n > 0.

- Förklara varför rekursionen fungerar.
- Implementera en rekursiv funktion som beräknar p(n). Glöm inte dokumentation och testkod.
- Beräkna p(5) när h[1] = 2, h[2] = 5, h[3] = 6, h[4] = 9 och h[n] = 0 när n > 4.
  Simulera beräkningen för hand och rita ett träd över alla funktionsanrop.
  (Det går bra med ett foto på ett handritat träd.)
- Förklara varför tidskomplexiteten för denna funktion är exponentiell.
- Förbättra tidskomplexiteten genom att skriva en version av programmet som cachar delresultat.
- Räkna ut en tabell över p(n) för n = 0, 1, 2, 3, 4, 5 (med samma h som ovan). Gör beräkningen för hand.
- Visa att tidskomplexiteten för den uppdaterade koden är O(n<sup>2</sup>).

[Tips om dynamisk programmering](https://www.youtube.com/watch?v=obslDoqkm7E) (video)

Uppdatera koden så att den inte bara beräknar den maximala inkomsten,
utan också ger en lista över halsdukar (garnåtgång och antal) som uppnår detta.
Om det finns flera möjliga lösningar så räcker det om du anger en.

### Reguljära uttryck (Kattis)

#### Uppgift [kth.<kattisnamn>](https://kth.kattis.com/courses/DD1327/grudat25/assignments/xxxx)

[Tips om reguljära uttryck](https://www.youtube.com/watch?v=NvKvCXac7sM) (video)

Dina funktioner måste ligga i en fil som heter s1.py, annars får du Run Time Error (“ImportError”) i Kattis.

Använd kodskelettet [s1.py](s1.py). Funktionerna i skelettet returnerar alla en tom sträng,
men de ska i din lösning returnera strängar som innehåller reguljära uttryck som löser deluppgifterna nedan.
I två av uppgifterna ska det reguljära uttryck du konstruerar bero på en söksträng som skickas som
indata.

De uttryck du konstruerar får vara högst 250 tecken långa (en generöst tilltagen gräns),
förutom i de två uppgifterna som tar en söksträng som indata.
Om du i någon av de andra uppgifterna returnerar ett för långt uttryck så får du ett Run Time Error i Kattis.
I de två uppgifterna med en söksträng som indata finns ingen specifik övre gräns
på hur långt ditt uttryck får vara, men om det är för långt och komplicerat
kommer din lösning att få Time Limit Exceeded.

I uppgifter där kravet är att hela strängen ska uppfylla något villkor så måste du använda
de speciella symbolerna ^ och $.

Kattis kommer att testa uppgifterna i ordning. När du är klar med första uppgiften
kan du alltså skicka in din lösning och se om du klarar alla testfall som hör
till första uppgiften, och så vidare.

### 1.

### 2. 

### 3. 

### 4. 

## VG-uppgift (10 högrebetygspoäng): Mer dynamisk programmering eller miniräknarsyntax?



## VG-uppgift (10 högrebetygspoäng): Syntax, svårare


