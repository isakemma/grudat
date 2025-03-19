# Övning 2 grudat25
### Deadline: Torsdag 27/3 kl 19:00

**Vid övningen ska du vara beredd att muntligt presentera och diskutera dina lösningar och din programkod. Du ska också ha med en utskrift av din inlämning för kamratgranskning på övningen.**

- Gör (minst) en fil per uppgift och lägg filerna i katalogen <code>username-ovn2</code> i organisationen [grudat25 på KTH GitHub](https://gits-15.sys.kth.se/grudat25).
- Utgå från mallarna i [/grudat25/ovn0/](https://github.com/isakemma/grudat/tree/master/ovn0).
- Lösningar ska vara inlämnade före deadline.

Du väljer själv vilket av programspråken Python, Go eller Java du vill använda.
**Observera att all kod på den här kursen ska dokumenteras och testas.**

*Gör antingen uppgift 2.3 eller 2.5, inte båda.*

## Betyg G

### 2.1 Ordo-notation

Ordna funktionerna i följande lista i växande ordning med
avseende på tillväxtstakt. Funktionen <i>f(n)</i> ska alltså
komma före funktionen <i>g(n)</i> i listan om
<i>f(n)</i> är <i>O</i>(<i>g(n)</i>).

<ul>
<li><i>f<sub>1</sub>(n)</i>&nbsp;=&nbsp;<i>n</i><sup>1.5</sup>
</li>
<li><i>f<sub>2</sub>(n)</i>&nbsp;=&nbsp;10<sup><i>n</i></sup>
</li>
<li><i>f<sub>3</sub>(n)</i>&nbsp;=&nbsp;<i>n</i>&nbsp;log&nbsp;<i>n</i>
</li>
<li><i>f<sub>4</sub>(n)</i>&nbsp;=&nbsp;<i>n</i>&nbsp;+100
</li>
<li><i>f<sub>5</sub>(n)</i>&nbsp;=&nbsp;2<sup><i>n</i></sup>
</li>
</ul>

Vilka av följande påståenden är sanna? Motivera dina svar.

<ul>
<li><i>n</i>(<i>n</i>&nbsp;+&nbsp;1)&nbsp;/&nbsp;2 = <i>O</i>(<i>n</i><sup>3</sup>)</li>
<li><i>n</i>(<i>n</i>&nbsp;+&nbsp;1)&nbsp;/&nbsp;2 = <i>O</i>(<i>n</i><sup>2</sup>)</li>
<li><i>n</i>(<i>n</i>&nbsp;+&nbsp;1)&nbsp;/&nbsp;2 = &Theta;(<i>n</i><sup>3</sup>)</li>
<li><i>n</i>(<i>n</i>&nbsp;+&nbsp;1)&nbsp;/&nbsp;2 = &Omega;(<i>n</i>)</li>
</ul>

[Video om ordo-notation](https://www.youtube.com/watch?v=rZvpB4Ip2_M)

### 2.2 Prefixsumma

Indata är en heltalsvektor <i>A</i> med <i>n</i>&nbsp;element.
Vi vill beräkna en vektor <i>B</i>, där <i>B</i>[i]&nbsp;=
<i>A</i>[0]&nbsp;+&nbsp;<i>A</i>[1]&nbsp;+&nbsp;...&nbsp;+&nbsp;<i>A</i>[i].
Här är en enkel algoritm som löser problemet.

<pre><code><b>for</b> i = 0 <b>to</b> n-1
    Add the numbers A[0] thru A[i].
    Store the result in B[i].
</code></pre>

- Beräkna tidskomplexiteten för denna algoritm och uttryck den på
  formen&nbsp;<i>O</i>(<i>f(n)</i>), där funktionen&nbsp;<i>f(n)</i>
  är så liten och enkel som möjligt.

- Visa att tidskomplexiteten också är &Omega;(<i>f(n)</i>).

- Hitta på en algoritm med bättre asymptotisk tidskomplexitet.
  Beskriv algoritmen i pseudokod och ange dess
  tidskomplexitet med Θ-notation.
  
[Video om tidskomplexitet](https://www.youtube.com/watch?v=x04gACtJHX0)
  
### 2.3 Binärt sökträd

Implementera ett *obalanserat* binärt sökträd som lagrar textsträngar.

-  Använd koden för den länkade listan i övning&nbsp;1 som mall.
- Gör ett tydligt API med publika dokumenterade metoder.
- Skriv utförlig testkod.

Följande metoder ska finnas:

- Skapa ett tomt träd.
- Lägg till ett nytt element.
- Returnera antalet element i trädet.
- Returnerar en sträng med alla element i bokstavsordning.

*Ange tidskomplexiteten i värstafall för samtliga operationer.*

[Tips och råd](https://www.youtube.com/watch?v=NCzRttSCeH4) (Video)

## Betyg VG

### 2.4 En ovanlig funktion?

Ge ett exempel på en positiv funktion <i>f(n)</i> sådan att
<i>f(n)</i> varken är <i>O</i>(<i>n</i>) eller
&Omega;(<i>n</i>).

### 2.5 Treap (alternativ till 2.3)

Gör uppgift 2.3 med ett randomiserat binärt sökträd i stället för ett obalanserat träd.
