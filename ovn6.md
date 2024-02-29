# Övning 6 grudat24
### Onsdag 8/5 kl 8.00

- Gör (minst) en fil per uppgift och lägg filerna i katalogen <code>username-ovn6</code> i organisationen [grudat24 på KTH GitHub](https://gits-15.sys.kth.se/grudat24).
- Utgå från mallarna i [/grudat24/ovn0/](https://github.com/isakemma/grudat/tree/master/ovn0).
- Lösningar ska vara inlämnade före deadline.

Den här gången ska du testa vissa av dina lösningar på Kattis
innan du lämnar in dem på ditt githubkonto.

1. Du får tillgång till Kattis genom att [logga in](https://kth.kattis.com/login) med ditt KTH-id.
2. Du måste också [registrera dig på grudat24](https://kth.kattis.com/courses/DD1327/grudat24/register) i Kattis. (Kursomgången finns ännu inte i Kattis.)

Mer information om Kattis hittar du i den här utmärkta [exempelmanualen](https://kth.kattis.com/help).

## Individuellt projekt

Observera att en första version av API och övrig dokumentation till
det [individuella projektet](https://github.com/isakemma/grudat/blob/master/ovn7.md)
ska vara klar redan till denna övning.

[Tips om projektet](https://www.youtube.com/watch?v=dzo3TO_v0uk) (video)

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

### Reguljära uttryck (Kattis)

#### Uppgift [kth.progp.s1](https://kth.kattis.com/courses/DD1327/grudat24/assignments/x7p6as/problems/kth.progp.s1)

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

### 1. DNA
#### Testfall 1-2

Skriv ett regex som matchar en sträng om och endast om den är en DNA-sekvens, dvs bara består
av tecknen ACGT (endast stora bokstäver, ej acgt).

### 2. Sorterade tal
#### Testfall 3-4

Skriv ett regex som matchar en sträng över tecknen 0-9 om och endast om tecknen i strängen
är sorterade i fallande ordning. Till exempel ska “42”, “9876543210”, och “000” matchas, men
“4711”, “11119”, “123”, och “777a” inte matchas.

### 3. Sök efter given sträng – del 1
#### Testfall 5-10

Skriv ett regex som matchar en sträng s om och endast en given söksträng x förekommer som
delsträng i s. Om söksträngen x är “progp” ska alltså t.ex. strängarna “popororpoprogpepor” och
“progprogp” matchas, men inte “PROGP”, “programmeringsparadigm”, eller “inda”. Du kan anta
att indatasträngen x bara består av bokstäver och siffror.

### 4. Sök efter given sträng – del 2
#### Testfall 11-16

I den här uppgiften kan du ha användning av metoden
[string.join](https://docs.python.org/2/library/stdtypes.html#str.join)
([exempel](http://www.tutorialspoint.com/python/string_join.htm)).
Skriv ett regex som matchar en sträng s om och endast en given söksträng x förekommer som
delsekvens i s, dvs om vi genom att ta bort några tecken ur s kan bilda x. Om söksträngen x är
“progp” ska alltså alla strängar som matchade i exemplet för del 1 fortfarande matcha, men nu ska
även t.ex. “programmeringsparadigm” och “p r o g p” matcha (men inte “inda” eller “poprg”). Du
kan anta att indatasträngen x bara består av bokstäver och siffror.

## Betyg VG

### Mer dynamisk programmering

Uppdatera koden i G-uppgiften så att den inte bara beräknar den maximala inkomsten,
utan också ger en lista över halsdukar (garnåtgång och antal) som uppnår detta.
Om det finns flera möjliga lösningar så räcker det om du anger en.

### Mer reguljära uttryck (Kattis)

### 5. Ekvationer utan parenteser
#### Testfall 17-21

Eftersom reguljära uttryck inte kan användas för att kolla om en uppsättning
parenteser är balanserade så kan vi inte skriva regex för att matcha allmänna ekvationer. Men vi
kan skriva ett regex för att matcha aritmetiska uttryck och ekvationer som inte tillåts innehålla
parenteser, och det ska vi göra nu.

De aritmetiska uttrycken vi vill matcha består av ett eller flera heltal, åtskiljda av någon av operatorerna
för de fyra räknesätten: +, -, *, /. Heltalen kan ha inledande nollor (matchande exempel
4 nedan). I början av ett uttryck kan det finnas ett plus- eller minustecken för att explicit säga att
första talet är positivt eller negativt (matchande exempel 2, 3, 5 nedan), men vi tillåter inte detta på
tal i mitten av uttryck (icke-matchande exempel 2 nedan). En ekvation är två uttryck separerade
av ett likhetstecken. Bara ett likhetstecken kan förekomma (icke-matchande exempel 4 nedan).

```
Strängar som ska matchas    Strängar som inte ska matchas

1589+232                    5*x
-12*53+1-2/5                18/-35
18=+17/25                   *23
000=0                       7=7=7
+1+2+3=-5*2/3               3.14159265358
```
Tänk på att tecknen +, -, &#42; har speciell betydelse i reguljära uttryck
och att du måste använda \ för att de ska tolkas bokstavligt.
Se [Special characters](http://yourbasic.org/golang/regexp-cheat-sheet/#special-characters).

(Det finns ytterligare två deluppgifter om reguljära uttryck i Kattis som du gärna får göra.
De ingår dock inte i den här kursen.)
