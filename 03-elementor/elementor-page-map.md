# Villa Carpino — mappa delle sette pagine per Elementor MCP

**Fonte:** i sette HTML nella cartella `villa_carpino_final` (riferimento V4 tecnico); testi e metadati SEO si copiano dall'HTML senza riscritture. Sono censite **36 sezioni principali** più header/footer globali e alcuni separatori editoriali. Questa mappa non è uno schema JSON importabile.

## Legenda

- `F` = container Flex; `G` = container Grid. Le indicazioni `F>F` o `G>F` indicano annidamento.
- `E` = Eyebrow Text; `H1/H2/H3` = Heading con tag semantico corretto; `T` = Text; `I` = Image; `B` = Button/link; `A` = Accordion.
- Base: max-width 1200; section vertical padding 105 px (Home/La Villa talvolta 110–112); gutter desktop 40; mobile 21; salvo eccezioni.
- La colonna foto usa il catalogo VC; impiegare `assets/images/VC-xx.webp` con originale JPEG a disposizione. Non cambiare crop senza confronto visivo.
- In Elementor ogni sezione resta un container nativo indipendente; non utilizzare widget HTML come contenitore dell'intera pagina.

## Home — `/`

- Sorgente: `villa_carpino_home.html`
- SEO title: **Villa Carpino | Ristorante e location per eventi a Ome in Franciacorta**
- H1: **Il piacere di stare insieme.**
- Dipendenze: header/footer globali; CTA telefoniche e link interni; hover cards. Nessuna API.

| ID e ordine | Sezione | Container e dimensioni | Widget Elementor | Foto | Responsive / criticità |
|---|---|---|---|---|---|
| H01 / 1 | Hero emozionale | Full-width min-height 665; overlay gradient; inner F column max 1200, align start; padding top/bottom 100/114 | E, H1, T, B; background/image | VC-04 | Mobile min-height 690, H1 ~58; foto larga 1472×491 richiede verifica LCP e crop |
| H02 / 2 | Benvenuto e storia | G 2 col 1/1.06, gap 105; photo height 515; text left | E, H2, T×2, B, I, badge “Dal 1994” | VC-02 | Mobile 1 col, gap 38, photo 370; badge decorativo |
| H03 / 3 | Ambienti interni/esterni | Section sand; heading split; G 1.2/.8 gap 24; photo cards 520 | E, H2, T, I×2, H3×2, links | VC-12, VC-27 | Mobile cards 1 col/400; card cliccabili; overlay gradient |
| H04 / 4 | Cucina | Full-width G 1/1, photo min-height 570, content padding 75–135 | I, E, H2, T, B | VC-33 | Mobile photo ~350 then text; titolo bianco su verde |
| H05 / 5 | Eventi | Heading center; G 3 col gap 24, photo 290 | E, H2, T, I×3, H3×3, T×3, link×3 | VC-16, VC-29, VC-14 | Mobile 1 col, foto e testo; link a Matrimoni/Eventi |
| H06 / 6 | Frase editoriale | Full-width center, padding 76, divider verticale | Divider, T grande, caption | — | Mobile 65; frase non è una recensione esterna |
| H07 / 7 | Invito a visitare | G .92/1.08, content padding 80, photo min-height 480 | E, H2, T, Text contatti, B, I | VC-26 | Mobile 1 col, photo 360; CTA telefonica |

Elemento intermedio fuori da `main/section`: fascia testuale “Un'atmosfera autentica…” tra H02/H03; realizzarla come sottile container full-width, padding verticale circa 30. Header e footer in Theme Builder, non nella pagina.

## La Villa — `/la-villa/`

- Sorgente: `la-villa.html`
- SEO title: **La Villa e il parco | Villa Carpino a Ome**
- H1: **La Villa: storia, sale e parco a Ome**
- Dipendenze: immagini autentiche; confermare l'abbinamento foto/nome Sala del Lino, delle Rose e del Camino.

| ID e ordine | Sezione | Container e dimensioni | Widget | Foto | Responsive / criticità |
|---|---|---|---|---|---|
| V01 / 1 | Hero La Villa | Full-width 630h, overlay, F column max1200, padding top 210 | E, H1, T | VC-25 | Mobile 590h, padding ~195/70; 600×600 non ideale hero |
| V02 / 2 | Territorio e nome | G .95/1.05 gap95; photo 580; text col | I, E, H2, T×2 | VC-18 | Mobile testo prima foto, photo 400 |
| V03 / 3 | Tradizione dal 1994 | Forest G 1/1 gap110; photo 440; grande 1994 | E, H2, T×2, Text anno, I | VC-11 | Mobile 1 col; photo 300; border foto decorativo |
| V04 / 4 | Le tre sale | Section sand; G 3 col gap25; photo 345; cards | E, H2, T, I×3, H3×3, T×3, B | VC-12, VC-16, VC-14 | Mobile 1 col; verificare nomi sale; CTA foto punta al parco nella fonte |
| V05 / 5 | Parco | Heading G .75/1.25; gallery G 1.1/.9, 2 righe 270 | E, H2, T, I×3, B | VC-27, VC-21, VC-24 | Mobile gallery grande sopra, due sotto; layout asimmetrico |
| V06 / 6 | CTA contatto | Full-width sand center, padding 105 | E, H2, T, B | — | Mobile padding 65; CTA chiamata |

## Ristorante — `/ristorante-franciacorta/`

- Sorgente: `ristorante-franciacorta.html`
- SEO title: **Ristorante in Franciacorta | Villa Carpino Ome**
- H1: **Il ristorante Villa Carpino in Franciacorta**
- Dipendenze: telefono; menu attuale non presente; foto piatti dichiaratamente storiche.

| ID e ordine | Sezione | Container e dimensioni | Widget | Foto | Responsive / criticità |
|---|---|---|---|---|---|
| R01 / 1 | Hero cucina | Full-width min 550, overlay, inner left | E, H1, T | VC-32 | Mobile min530; foto 600×600, crop da verificare |
| R02 / 2 | Gusto e ospitalità | G 1/1 gap95, photo 510 | E, H2, T, B, I | VC-02 | Mobile 1 col, photo350 |
| R03 / 3 | Cucina tradizionale | Forest G 1/1 gap95, photo 510, testo bianco | I, E, H2, T×2 | VC-31 | Mobile 1 col, verificare ordine foto/testo |
| R04 / 4 | Galleria piatti | Sand, center heading, G 4 col gap14, tile 255 | E, H2, T, I×8, note, B | VC-30,33,35,36,37,38,40,41 | Mobile G 2 col, tile 205; non rappresentare menu corrente |
| R05 / 5 | CTA finale | Sand center padding95 | E, H2, T, B | — | Mobile line wrap e CTA contatti |

## Cerimonie ed Eventi — `/cerimonie-eventi-franciacorta/`

- Sorgente: `cerimonie-eventi-franciacorta.html`
- SEO title: **Cerimonie ed eventi in Franciacorta | Villa Carpino**
- H1: **Cerimonie ed eventi in Franciacorta**
- Dipendenze: recapito, conferma spazi e menu attuali.

| ID e ordine | Sezione | Container e dimensioni | Widget | Foto | Responsive / criticità |
|---|---|---|---|---|---|
| E01 / 1 | Hero eventi | Full-width min550, overlay | E, H1, T | VC-14 | Mobile min530; foto 600 |
| E02 / 2 | Introduzione | G 1/1 gap95, photo 510 | E, H2, T, B, I | VC-29 | Mobile colonna singola |
| E03 / 3 | Ricorrenze famiglia | Sand, center heading, G 3 cards gap23 | E, H2, T, I×3, H3×3, T×3 | VC-16,17,28 | Tablet 2, mobile 1; nessun menu fisso promesso |
| E04 / 4 | Aziende / Sala del Lino | Forest G 1/1 gap95, photo510 | I, E, H2, T×2, note | VC-13 | Associazione sala/foto da confermare |
| E05 / 5 | Menu eventi | G 1/1 gap95, photo510 | E, H2, T, B, I | VC-33 | CTA “Richiedi una proposta” telefonica |
| E06 / 6 | FAQ | Sand, center heading, F column max900, accordion rows | E, H2, T, A×4, B | — | Accordion tastiera, focus, uno o più pannelli aperti secondo default scelto |

## Matrimoni — `/matrimoni-franciacorta/`

- Sorgente: `matrimoni-franciacorta.html`
- SEO title: **Matrimoni in Franciacorta | Villa Carpino**
- H1: **Matrimoni in Franciacorta a Villa Carpino**
- Dipendenze: telefono, foto e disponibilità da confermare.

| ID e ordine | Sezione | Container e dimensioni | Widget | Foto | Responsive / criticità |
|---|---|---|---|---|---|
| M01 / 1 | Hero matrimonio | Full-width min550 overlay | E, H1, T | VC-26 | Mobile min530; 600×600 hero |
| M02 / 2 | Cornice speciale | G 1/1 gap95 photo510 | E, H2, T, B, I | VC-16 | Mobile colonna singola |
| M03 / 3 | Spazi giornata | Sand heading center; G 1.1/.9 gap22, photo 470/340 sfalsate | E, H2, T, I×2, B | VC-12, VC-22 | Mobile 1 col, foto 340 e niente offset |
| M04 / 4 | Ricevimento insieme | Forest G 1/1 gap95 photo510 | I, E, H2, T, B | VC-29 | Mobile colonna singola |
| M05 / 5 | Statement finale | Sand F row, heading width~670 + right text/CTA | H2, T, B | — | Mobile F column, heading ~38 |

## Franciacorta — `/franciacorta/`

- Sorgente: `franciacorta.html`
- SEO title: **Villa Carpino e la Franciacorta | Cosa vedere a Ome**
- H1: **Villa Carpino nel cuore della Franciacorta**
- Dipendenze: nessuna API, link interno Ristorante. Mancano foto territoriali senza numerazioni sovrapposte.

| ID e ordine | Sezione | Container e dimensioni | Widget | Foto | Responsive / criticità |
|---|---|---|---|---|---|
| F01 / 1 | Hero + breadcrumb | Full-width min550 overlay, inner left | Breadcrumb links, E, H1, T | VC-04 | Mobile min530; breadcrumb non globale |
| F02 / 2 | Territorio | G 1/1 gap95, photo510 | E, H2, T×2, I | VC-27 | Mobile 1 col |
| F03 / 3 | Esperienze | Sand center head; G 3 col cards min370 | E, H2, T, decorative character Text, H3×3, T×3 | — | Mobile 1 col, card min280; nessuna immagine AI |
| F04 / 4 | Ristorante | Forest G 1/1 gap95, photo510 | I, E, H2, T, B | VC-02 | Mobile 1 col; link Ristorante |

## Contatti — `/contatti/`

- Sorgente: `contatti.html`
- SEO title: **Contatti e prenotazioni | Villa Carpino Ome**
- H1: **Contatta Villa Carpino a Ome**
- Dipendenze: form Pro/SMTP e privacy; Google Maps; recapiti e dati legali da verificare.

| ID e ordine | Sezione | Container e dimensioni | Widget | Foto | Responsive / criticità |
|---|---|---|---|---|---|
| C01 / 1 | Intro e recapiti | Sand Flex row: content + aside min285, padding 95 | E, H1, T, B Chiama, Heading/Texts recapiti | — | Mobile stacked; CTA telefono |
| C02 / 2 | Form | G .75/1.25 gap110; form panel padding48; fields G 2 col gap23 | E, H2, T, Form Pro, status/error | — | <=850 stack, <=510 campi 1 col; HTML demo non invia |
| C03 / 3 | Come arrivare | Sand G .78/1.22 gap60; map 420h | E, H2, Address Text, B Maps, Map/HTML embed | — | <=850 stack; map 350; consenso/terze parti |

## Regola editoriale comune

Non cambiare title, description, H1, testo dei paragrafi, label CTA, foto o ordine delle sezioni. Per ogni sezione costruita in Elementor: creare container, applicare classe globale, inserire testo esatto dall'HTML, assegnare media, verificare crop, responsive e comportamento, poi salvare in bozza.
