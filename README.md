# Misija Nexus - Projekt Analize Marsovih Podataka

## Izvršni sažetak

Misija Nexus ima za cilj otkrivanje optimalnih lokacija za bušenje na Marsu, fokusirajući se na krater Jezero. Korištenjem podataka o temperaturi tla, pH vrijednostima, postotku vode i prisutnosti metana, razvili smo metodologiju koja omogućuje prepoznavanje prometnih točaka za buduće misije. Ovaj projekt koristi Python skripte za obradu podataka i generiranje vizualizacija, te automatski generira JSON naloge za bušenje temeljem analiziranih podataka. Rezultati analize ključni su za daljnji razvoj autonomnih sustava za ispitivanje tla Marsa.

## Metodologija obrade podataka (Data Wrangling)

Podaci korišteni u ovom projektu dolaze iz dviju CSV datoteka: `mars_lokacije.csv` i `mars_uzorci.csv`, koje sadrže informacije o Marsovim lokacijama, uzorcima tla i senzorima. 

### Koraci obrade podataka:
1. **Učitavanje podataka:** Podaci su učitani koristeći Pandas, uzimajući u obzir separator (točka-zarez) i decimalnu točku (zarez).
2. **Spajanje podataka:** Obje datoteke spojene su prema zajedničkom identifikatoru (`ID_Uzorka`), čime je stvoren jedan objedinjeni skup podataka.
3. **Filtriranje anomalija:** Korištenjem logičkih uvjeta, uklonjeni su svi podaci koji sadrže nelogične ili ekstremne vrijednosti za temperaturu, pH, postotak vode i druge važne parametre.
4. **Podjela na čiste i anomalne podatke:** Čisti podaci su spremljeni u zasebnu datoteku (`cisti_podaci.csv`), dok su anomalije spremljene u drugu datoteku (`anomalije.csv`).

### Filtriranje uvjeta:
Podaci su filtrirani prema sljedećim uvjetima:
- Temperatura tla između -100°C i 40°C
- pH vrijednost između 0 i 14
- Postotak vode između 0% i 100%

Podaci koji nisu zadovoljili ove uvjete označeni su kao anomalni i premješteni u zasebnu tablicu.

## Geoprostorna analiza i vizualizacija

Za analizu geografskih podataka korišteni su grafovi koji pokazuju razne odnose među parametrima, kao i geografske karte koje vizualiziraju lokacije bušenja.

### Generirani grafovi:
1. **Graf1 - Temperatura vs. Postotak vode**: Ovaj graf prikazuje odnos između temperature tla i postotka vode s označenim točkama koje pokazuju prisutnost metana.
   - **Ime datoteke:** `graf1_temperatura_voda.png`
   
2. **Graf2 - Karta dubine bušenja**: Geografska karta na kojoj je prikazana dubina bušenja prema GPS koordinatama.
   - **Ime datoteke:** `graf2_karta_dubine.png`

3. **Graf3 - Karta metana**: Ovaj graf prikazuje geografsku rasprostranjenost metana, s crvenim označavanjem pozitivnih očitanja metana, a plavim negativnih.
   - **Ime datoteke:** `graf3_metan.png`

4. **Graf4 - Karta kandidata**: Geografska karta na kojoj su označeni kandidati za bušenje (lokacije s metanom i organskim molekulama), koji su označeni velikim crvenim zvjezdicama.
   - **Ime datoteke:** `karta_kandidata.png`

5. **Graf5 - Misijska karta Jezero**: Satelitska snimka kratera Jezero sa superponiranim podacima o GPS koordinatama, čime se omogućuje vizualna orijentacija za misiju.
   - **Ime datoteke:** `misijska_karta_jezero.jpg`

Za generiranje svih ovih vizualizacija korišteni su `matplotlib` i `seaborn` biblioteke.

## Komunikacijski protokol (JSON Uplink)

Nakon vizualizacije podataka i pronalaska kandidata za bušenje, sljedeći korak je slanje naloga za bušenje robotskim sustavima putem JSON formata. Svaka od odabranih lokacija dobiva tri vrste akcija: **NAVIGACIJA**, **SONDIRANJE** i **SLANJE_PODATAKA**.

### Struktura JSON paketa:
```json
{
  "kandidati": [
    {
      "ID_Uzorka": 12345,
      "GPS_LAT": 12.3456,
      "GPS_LONG": 98.7654,
      "akcije": [
        { "tip": "NAVIGACIJA" },
        { "tip": "SONDIRANJE" },
        { "tip": "SLANJE_PODATAKA" }
      ]
    },
    ...
  ]
}
