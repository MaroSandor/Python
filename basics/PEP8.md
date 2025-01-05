# Python PEP8 szabvány
___
A Python PEP8 szabvány egy úgynevezett felesztési javaslat, 
amely irányelveket és javaslatokat tartalmaz a kódformázásra vontakozóan.

## Mire jó?
1. Olvashatóság javítása
> Az egységes formázás révén a kód könnyebben érthető és követhető lesz.
2. Csapatmunka támogatása
> Ha mindenki ugyanazt a szabványt követi, egyszerűbb a közös munka és a kódok áttekintése.
3. Hibakeresés megkönnyebítése
> Az egységes formázás segíthet gyorsabban azonosítani a hibákat.
5. Professzionalizmus
> A PEP8 szabványnak megfelelő kód professzionálisabb hatást kelt, különösen, ha másokkal osztod meg a munkádat (például open-source projektekben).

## Mikor használjuk?
1. Minden esetben Python kód írása közben
> Függetlenül attól, hogy egyéni projektet vagy csapatmunkát végzel, érdemes a PEP8 szabványt követni.
2. Kódáttekintések során
> A szabványt követve könnyebb mások kódját véleményezni, mivel az elvárt stílusok egyértelműek.
3. Automatizált eszközök használatakor
> A legtöbb modern kódszerkesztő (például Visual Studio Code, PyCharm) támogatja a PEP8 ellenőrzését és formázását.

## Mennyire hasznos?
1. Csapatprojektek
> A szabvány egységesíti a kódot, függetlenül attól, hogy ki írta.
2. Tanulás és tanítás
> Az új programozóknak segít megtanulni a helyes kódírási szokásokat.
3. Hosszú távú karbantartás
> Az olvashatóbb kód könnyebben karbantartható, különösen idő múlásával.
___

## Főbb irányelvek a PEP8-ban
1. **Behúzás:** Használj 4 szóközt.
2. **Maximális sorhossz:** 79 karakter, doc esetén 72 karakter)
3. **Üres sorok:** Elkülönítik a függvényeket, osztályokat vagy kódrészeket.
4. **Változó- és függvénynevek:** Kisbetűs, aláhúzással elválasztott (snake_case).
5. **Importok:** Minden import a fájl tetején legyen, logikusan csoportosítva.
6. **Whitespace:** Kerüld a felesleges szóközöket (pl. =, + műveletek körül).
7. **Docstring-ek:** Használj leíró docstringeket minden függvényhez, osztályhoz és modulhoz.

### Eszközök az ellenőrzéshez

```commandline
brew install flake8 // Hibakeresés és szabványellenőrzés
brew install black // Automatikus formázó eszköz
brew install pylint // Hibák és stílusproblémák ellenőrzés
```