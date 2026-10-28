# Villa Carpino — Report miglioramento fotografico

**Intervento:** post-produzione conservativa delle fotografie effettivamente utilizzate nell'HTML Master V1.0.

## Risultati eseguiti

- 27 fotografie in uso individuate e processate.
- 27 WebP full-size pubblicati in `assets/images/ai-enhanced/` e 27 varianti da 480 px per il responsive.
- Originali JPG preservati integralmente in `assets/originals/` (41 fotografie); nessun originale sovrascritto.
- Set dei `<source>` in tutte e sette le pagine aggiornato verso `ai-enhanced`, con `srcset` e `sizes`; gli `<img>` mantengono i JPG originali come fallback di `<picture>`.
- Nessun cambiamento a testi, URL, metadata SEO, layout, menu, CSS o script.
- Nessun nuovo oggetto, ambiente, paesaggio, dettaglio architettonico o arredo generato.

## Metodologia fotografica

Pipeline non generativa e riproducibile con Pillow: esame statistico della luminanza, recupero molto leggero di ombre/mezzitoni su immagini scure, contrasto morbido soltanto dove necessario e sharpening limitato sulle sorgenti di bassa risoluzione. Conservati bilanciamento del bianco e inquadratura originali. Compressione WebP qualità 85 (varianti da 480 px qualità 82). Per la fotografia `VC-36` il primo encoder non ha prodotto un file valido: è stata pertanto mantenuta la versione WebP esistente, senza attribuirle correzioni non eseguite.

La trasformazione è stata volutamente **non generativa**, benché sia disponibile un generatore/editor AI: l'uso di tecniche generative su fotografie documentali della struttura avrebbe potuto alterare arredi, architettura e altri dettagli, violando il vincolo prioritario di fedeltà. Questo è un limite esplicito rispetto alla richiesta di *AI enhancement*.

Non sono stati applicati auto-white-balance aggressivi, correzioni prospettiche non misurate, riduzione rumore pesante, inventata super-risoluzione o upscaling AI. La risoluzione massima rimane quella delle sorgenti (molte immagini sono da 600×600 px). Le immagini già correttamente esposte hanno ricevuto solo compressione WebP e, dove utile, una minima nitidezza. Tutte le decisioni per immagine sono riportate nel manifest.

## Test completati

| Test | Esito |
|---|---|
| Integrità delle sette pagine, link e asset, CSS e JavaScript | PASS |
| File WebP enhanced originali e ridotti, lettura/decodifica PIL | PASS: 54 file |
| Tutti i `<source>` che citano `ai-enhanced` puntano a file validi | PASS |
| Le 27 fotografie utilizzate risultano referenziate nelle pagine | PASS |
| Gli originali restano disponibili come fallback JPEG | PASS |
| Ispezione a campione del confronto foto originale/migliorata | PASS, non esaustiva |

Ripetere con `python tests/test_site.py` e `python tests/test_enhanced_images.py`.

## Limiti e verifiche ancora necessarie

1. Non è stato possibile svolgere un'ispezione umana di **tutte** le 54 varianti alle dimensioni di pubblicazione; il controllo automatico di decodifica e riferimenti non garantisce assenza di ogni artefatto percettivo.
2. Nessuna misurazione Lighthouse/LCP o collaudo grafico automatizzato su browser desktop/mobile: browser headless non disponibile in questo ambiente.
3. Non sono stati usati modelli AI per upscaling, denoising o correzione geometrica. Qualsiasi successivo intervento generativo richiede una revisione puntuale della fedeltà documentale.
4. Alcune foto storiche, soprattutto da 600 px, rimangono limitate nella definizione se visualizzate molto grandi. Eventuali nuovi scatti professionali sarebbero preferibili a un ingrandimento inventato.
5. La collocazione soggetto/descrizione e l'attualità delle foto di pietanze richiedono conferma editoriale della proprietà.

**Manifest analitico:** `photo-enhancement-manifest.csv`. La cartella HTML risultante è navigabile e destinata al successivo passaggio SEO e ottimizzazione del sito.
