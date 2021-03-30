
# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovelluksen avulla käyttäjä voi valvoa opintojensa edistystä. Käyttäjä voi lisätä kursseja suunnitelmaan ja merkitä niitä suoritetuiksi, ja ohjelma kertoo käyttäjälle, toteutuuko hänen suunnitelmassaan ja suorituksissa esim. Kelan vaatimukset tai yliopiston suosittelema aikataulu.

## Perusversion tarjoama toiminnallisuus

### Suunnittelu
 - Käyttäjä voi lisätä kurssin nimellä ja opintopistemäärällä
	 - Kurssille annetaan myös jokin ajanjakso (periodi, vuosi)
	 - Kursseja voi myös poistaa
- Ohjelma kertoo, montako opintopistettä kertyy vuodessa, perioidissa
- Ohjelma kertoo, täyttyykö vuodelta Kelan vaatimukset
	- Ohjelma kertoo, miten paljolla ei jos ei täyty, tai kuinka paljon on ylimääräisiä pisteitä jos niitä on
- Ohjelma kertoo, täyttyykö vuodelta yliopiston aikataulusuositus
  	- Ohjelma kertoo, miten paljolla ei jos ei täyty, tai kuinka paljon on ylimääräisiä pisteitä jos niitä on

### Suoritus
- käyttäjä voi merkitä kurssin suoritetuksi
- Suorituksen voi poistaa
- Ohjelma kertoo, täyttävätkö suoritetut kurssit kelan vaatimukset, aikataulusuosituksen
	- Tarjoaa muutenkin samat tiedot kuin suunniteluvaiheessa, mutta suoritetuille
- Ohjelma kertoo, kuinka suuri prosentti suunnitelmasta on toteutunut

## Jatkokehitysideoita

Perusversion jälkeen järjestelmää täydennetään ajan salliessa esim. seuraavilla toiminnallisuuksilla

- Mahdollisuus luoda useita suunnitelmia
- Statistiikkaa useampien vuosien yli
- Mahdollisuus viedä suunnitelmat jossain jaettavassa tiedostomuodossa
- Suoritettuihin kursseihin arvosanat
- Erillinen ajaton ja ajallinen suunnittelu (mitkä kurssit tulee suorittaa ja milloin ne suoritetaan erotettu)
- Lisää hyödyllistä analyysiä