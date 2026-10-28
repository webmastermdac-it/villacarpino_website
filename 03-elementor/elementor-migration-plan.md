# Villa Carpino — piano operativo Codex + Elementor MCP

## Obiettivo e confini

Ricostruire **sette pagine**, header e footer globali in WordPress/Elementor, con testi e immagini modificabili. Il prototipo HTML rimane riferimento visivo. Nessuna connessione o pubblicazione è autorizzata in questa fase.

## Fase 0 — Prerequisiti e verifica ambiente

- [ ] Confermare hosting e staging pulito dopo il precedente incidente di sicurezza.
- [ ] Backup e ripristino testati; aggiornamenti WordPress/PHP/plugin, account e permessi minimi.
- [ ] Rilevare **versioni reali** WordPress, Elementor Core, Elementor Pro e funzioni Atomic V4/MCP.
- [ ] Inventariare widget e feature disponibili (Theme Builder, Form, Menu, Accordion, Grid, reusable components).
- [ ] Verificare l'effettiva connessione MCP Codex in modalità di test, dopo autorizzazione specifica.
- [ ] Validare se i template Elementor JSON siano esportabili/importabili nella release installata. **Non inventare schema.**

**Gate:** ambiente verificato, MCP operativo, nessun contenuto pubblicato.

## Fase 1 — Media e contenuti

1. Creare cartella Media Library “Villa Carpino”; importare WebP usati nel sito e mantenere l'archivio originale.
2. Conservare mappatura `VC-xx` → attachment ID/URL; non cambiare foto nel layout senza approvazione.
3. Confermare i nomi delle tre sale, disponibilità menu e fotografie eroiche insufficienti.
4. Caricare logo originale; preferire versione ad alta risoluzione/SVG autorizzata se disponibile.
5. Salvare permalink, title, meta description, H1 dal file `elementor-page-map.md`.

**Gate:** nessuna foto mancante, media rintracciabili, contenuti approvati invariati.

## Fase 2 — Design system

1. Leggere `elementor-design-system.json`.
2. Configurare Site Settings: colori, font e scale tipografiche; definire breakpoint reali.
3. Creare classi globali `vc-container`, `vc-section`, `vc-hero`, `vc-split`, `vc-card-grid`, `vc-button`, `vc-gallery-grid`.
4. Testare una sola card e una hero con le classi globali; verificare che rimangano editabili.
5. Usare il medesimo sistema per tutte le pagine, evitando copia-incolla di CSS inline.

**Gate:** componenti visivamente coerenti a 1440, 1024 e 390 px.

## Fase 3 — Global templates

1. Ricostruire Header G01: sfondo opaco, logo, sette voci a vista su desktop, Contattaci CTA, menu mobile e tasto Chiama.
2. Ricostruire Footer G02: informazioni contatto, sette link, copyright e spazi per policy/dati validati.
3. Impostare Theme Builder display conditions Entire Site.
4. Verificare che il template pagina non nasconda le parti globali (evitare Canvas se non motivato).
5. Testare link, tastiera, focus e responsive.

**Gate:** un solo header/footer in tutte le pagine, nessun link `.html` residuo.

## Fase 4 — Implementazione pagine in ordine controllato

| Ordine | Pagina | Sezioni | Perché in questa fase |
|---|---|---:|---|
| 1 | Home | H01–H07 | Stabilisce hero, split, cards, CTA e ritmi visivi |
| 2 | La Villa | V01–V06 | Introduce sale, badge anno e gallery asimmetrica |
| 3 | Ristorante | R01–R05 | Gallery 8 foto e contenuti gastronomici |
| 4 | Cerimonie ed Eventi | E01–E06 | Cards e FAQ, CTA commerciali |
| 5 | Matrimoni | M01–M05 | Gallery sfalsata e statement |
| 6 | Franciacorta | F01–F04 | Card editoriali e breadcrumb |
| 7 | Contatti | C01–C03 | Form, map, privacy e test funzionali |

Per **ogni sezione**:

1. Leggere riga corrispondente in `elementor-widgets-map.csv`.
2. Creare un container nativo con layout e classi specificate.
3. Inserire widget nativi, testo **identico** e immagini VC corrette.
4. Impostare padding/gap/dimensioni a desktop, tablet e mobile.
5. Salvare in **bozza**.
6. Confrontare il risultato con HTML e annotare divergenze.
7. Approvare il singolo blocco prima del successivo.

## Fase 5 — SEO e navigazione

- [ ] Slug esatti: `/`, `/la-villa/`, `/ristorante-franciacorta/`, `/cerimonie-eventi-franciacorta/`, `/matrimoni-franciacorta/`, `/franciacorta/`, `/contatti/`.
- [ ] Title e meta description come fonte HTML; un H1 per pagina.
- [ ] Canonical, Open Graph, sitemap, eventuale Restaurant/LocalBusiness schema con dati **verificati**.
- [ ] Link interni e CTA verso permalink WordPress, non verso file .html.
- [ ] Breadcrumb dove previsto e link telefono/mappa funzionanti.

## Fase 6 — Verifica funzionale e performance

- [ ] Desktop 1440/1280, tablet 1024/820, mobile 430/390/320.
- [ ] Menu mobile, touch, keyboard, focus, CTA e FAQ.
- [ ] Form invia davvero: destinatario, SMTP, antispam, email di test, stato errori e privacy.
- [ ] Hero prioritizzata; immagini sotto il fold lazy; crop WebP, ALT e proporzioni.
- [ ] Controllo CLS, LCP e INP mediante Lighthouse e, dopo il lancio, dati reali.
- [ ] Nessun overlay o immagine storica fuorviante.
- [ ] Controllo visuale tramite screenshot comparativi e revisione MDAC.

**Gate:** nessun blocker aperto; approvazione grafica e funzionale; autorizzazione separata prima della pubblicazione.

## Prompt base per Codex collegato a Elementor MCP

> Lavora nel sito di staging Villa Carpino. Non pubblicare. Leggi il design system e la mappa della pagina [NOME]. Crea soltanto la sezione [ID] utilizzando elementi Atomic/nativi e classi globali, senza un singolo widget HTML di pagina. Usa il testo identico al file sorgente, la foto VC-[ID] indicata e le impostazioni responsive documentate. Salva in bozza, restituisci la struttura dei container/widget effettivamente creata, segnala differenze rispetto al prototipo e fermati prima della sezione successiva.

## Tracking consigliato

| Campo | Scopo |
|---|---|
| Page/Section ID | Identifica il blocco costruito |
| Elementor document ID | Traccia la pagina/template |
| Source HTML commit/hash | Versione del reference visivo |
| Attachment ID | Foto VC utilizzata |
| Classe globale | Design token applicati |
| Desktop/tablet/mobile QA | Stato di conformità |
| SEO/functional QA | Verifica finale |
| Approvazione MDAC | Gate umano |

## Problemi aperti noti

- Le hero 600×600 non sono fotograficamente ideali per banner larghi; non inventare alternative.
- L'abbinamento delle fotografie alle sale è provvisorio.
- Il form HTML non invia dati; creare una versione WordPress completa.
- I dati societari, alcune informazioni di contatto e le policy richiedono conferma.
- Non è disponibile la versione effettiva di Elementor; quindi **nessun JSON dichiarato importabile**.
- Il prototipo HTML finale necessita del completamento dei test visuali in browser prima di essere considerato baseline visiva certificata.
