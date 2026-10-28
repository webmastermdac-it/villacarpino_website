# Villa Carpino — HTML Master V1.0

Versione statica di riferimento per la futura ricostruzione in WordPress/Elementor. Non è un sito pubblicato e non contiene una connessione a WordPress.

## Apertura e struttura

Aprire `villa_carpino_home.html` in browser; gli altri URL locali sono collegati dal menu. Per un test HTTP locale è possibile servire questa directory con un server statico.

| Pagina | File | URL WordPress previsto |
|---|---|---|
| Home | `villa_carpino_home.html` | `/` |
| La Villa | `la-villa.html` | `/la-villa/` |
| Ristorante | `ristorante-franciacorta.html` | `/ristorante-franciacorta/` |
| Cerimonie ed eventi | `cerimonie-eventi-franciacorta.html` | `/cerimonie-eventi-franciacorta/` |
| Matrimoni | `matrimoni-franciacorta.html` | `/matrimoni-franciacorta/` |
| Franciacorta | `franciacorta.html` | `/franciacorta/` |
| Contatti | `contatti.html` | `/contatti/` |

- `styles/`: CSS condivisi, CSS di pagina e font locali.
- `scripts/site.js`: interazioni minime.
- `assets/images/`: versioni WebP ottimizzate di fotografie originali.
- `assets/images/ai-enhanced/`: post-produzione conservativa WebP e varianti responsive effettivamente referenziate nelle pagine. Vedere `photo-enhancement-report.md` e `photo-enhancement-manifest.csv`.
- `assets/originals/`: fotografie JPG originali e logo, conservati senza sostituzioni artificiali.
- `assets/fonts/`: Playfair Display e DM Sans locali (TTF).
- `image-map.csv`: inventario e corrispondenza immagini.
- `elementor-page-map.csv` e `elementor-*`: specifiche di supporto alla conversione visuale; verificare sempre la versione reale di Elementor prima di importare o costruire template.
- `tests/test_site.py`: regressione statica eseguibile con Python, lxml e Node.js disponibili.

## Interventi nella V1.0

1. Uniformati header e footer delle sette pagine. Menu desktop con sette voci sempre visibili; header con fondo opaco; nessun pulsante «Prenota» nell'header. Su mobile, menu nativo espandibile e chiamata rapida.
2. Estratti gli stili di pagina e rimossi selettori ereditati da navigazioni precedenti; aggiunti stili condivisi per componenti e accessibilità.
3. Localizzati i font, eliminando la dipendenza runtime da Google Fonts.
4. Conservati i JPG originali; create varianti WebP per le immagini utilizzate e fallback JPG tramite `picture` dove applicabile.
5. Inserite dimensioni intrinseche, `alt`, caricamento differito per immagini secondarie e priorità di caricamento per immagini hero.
6. Preservati integralmente i testi nel contenuto principale, così come title, description e H1 delle sette pagine.
7. Ridotto il JavaScript e reso il menu mobile utilizzabile senza JavaScript.

## Esito test

- **PASS** — Integrità HTML, struttura delle sette pagine, heading principale, metadata SEO, header/footer coerenti, menu e link/anchor interni.
- **PASS** — Presenza e integrità dei file immagine e dei WebP, `alt`, dimensioni intrinseche e riferimenti CSS/JS locali.
- **PASS** — 41 JPG originali conservati, 27 WebP validi e logo originale presente.
- **PASS** — Controllo sintattico JavaScript tramite Node.js e controllo statico dei CSS.
- **PASS** — Confronto automatizzato dei testi di `<main>` con le bozze HTML V4: nessuna variazione.
- **NON ESEGUITO** — Collaudo visivo reale e misure Lighthouse/Core Web Vitals: l'installazione del browser headless nel runtime non è riuscita. Il responsive è stato predisposto nel CSS ma richiede verifica visiva manuale.

Per ripetere i test: `python tests/test_site.py` dalla directory principale del sito.
Per i riferimenti fotografici migliorati: `python tests/test_enhanced_images.py`.

## Punti aperti prima della pubblicazione

1. **Form Contatti** — È una demo front-end: non invia email. In WordPress configurare form, destinatario verificato, consenso/privacy, antispam e messaggi di conferma.
2. **Dati di contatto e legali** — Validare recapiti, dati societari, privacy e cookie policy. Le indicazioni provvisorie nel footer non sostituiscono testi legali.
3. **Google Maps** — L'iframe di Contatti è l'unica dipendenza esterna runtime rilevata. Necessita connessione e verifica delle modalità privacy/consenso; è disponibile anche il link alla mappa.
4. **Fotografie** — Confermare attualità, associazione soggetto/nome file e qualità fotografica delle immagini storiche; non presentare i piatti come menu attuale. Alcuni originali potrebbero non consentire una hero di altissima definizione.
5. **Verifica visiva** — Collaudare almeno a 1440, 1024, 768, 390 e 320 px; controllare menu aperto/chiuso, focus da tastiera, ingombri hero, testi lunghi, gallery e form.
6. **Performance reali** — Misurare LCP, CLS, INP e peso rete su ambiente accessibile via browser; valutare eventuale conversione dei font locali in WOFF2 e ulteriori varianti responsive delle foto se i test lo richiedono.
7. **Elementor** — Ricostruire container e widget nativi, non incollare pagine intere in widget HTML. Header/footer globali e impostazioni tipografiche dovranno essere verificati nella versione Elementor effettivamente installata. Gli URL definitivi vanno impostati come permalink WordPress.

Questa cartella è il **riferimento tecnico statico** per la migrazione. L'approvazione finale di resa grafica, funzionalità form e aspetti legali resta subordinata ai punti aperti.
