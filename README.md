# Sentieri CAI-FVG
Estrapolazione dei dati dal sito del [CAI FVG](https://www.cai-fvg.it/sentieri-cai-fvg/) riguardo le informazioni dei sentieri.
## Librerie usate:
- 'requests'
- 're'
- 'BeautifulSoup'
## Esempio:
```python
import sentieriFVG as sentiero 

trail = sentiero.Sentiero('311')

print(trail.code)
print(trail.summary)
print(trail.desc)
print(trail.partenza)
print(trail.arrivo)
print(trail.dislivello)
print(trail.long)
print(trail.time)
print(trail.punti_app)

print(trail.imm_url)
print(trail.alt_url)
print(trail.gps)
```
* .code restituisce il codice del sentiero.
* .summary restituisce il sommario del sentiero.
* .desc restituisce la descrizione del percorso.
* .partenza restituisce il luogo della partenza. 
* .arrivo restituisce il luogo dell'arrivo.
* .dislivello restituisce il dislivello complessivo.
* .long restituisce la lunghezza del sentiero.
* .time restituisce il tempo di percorrenza.
* .punti_app restituisce eventuali punti di appoggio.
* .imm_url restituisce il link dell'immagine della mappa del sentiero.
* .alt_url restituisce il grafico dell'altimetria, se vuoto resituisce 'None'.
* .gps restituisce il link del file gps, se vuoto resituisce 'None'.

