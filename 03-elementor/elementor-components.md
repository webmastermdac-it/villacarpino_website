# Villa Carpino — componenti riutilizzabili in Elementor

## Principi

Il sito deve essere ricostruito con elementi nativi editabili. Questa è una **specifica di implementazione**, non un file di importazione Elementor. Nel catalogo MCP verificato dalla documentazione 2026 sono previsti elementi Atomic V4, classi e variabili globali, template e componenti riutilizzabili. La disponibilità esatta dei widget Classic/Pro va controllata nell'editor installato.

## Componenti globali

| ID | Componente | Struttura container | Widget/elementi | Layout e stile | Riutilizzo e note |
|---|---|---|---|---|---|
| G01 | Header | Section full width > Flex row max 1390 > Logo + Nav; in mobile Logo + Call + Menu | Image, Nav Menu o elementi link, Button tel | Min-height 112; fondo #2D3B30; gap 32; mobile ~85 | Theme Builder Header, display Entire Site; sette voci, Contattaci CTA; nessun bottone prenota |
| G02 | Footer | Section full width > Flex max 1200 > Logo/contatti + Nav; fondo e legal row | Image, Text, Icon List/Nav, Text | Fondo #242E26; top/bottom padding 62/27, gap 40 | Theme Builder Footer, display Entire Site; dati legali da validare |
| G03 | Breadcrumb | Flex row | Text/links oppure widget Breadcrumb SEO, se disponibile | 11 px uppercase, letter spacing .12em | Ora visibile su Franciacorta; uniformare solo se approvato |
| C01 | Hero fotografico | Full-width min-height 550–665 > Image/background + Overlay + Content flex column | Image o background nativo, Heading H1, Text, Button | Cover, left, max 1200; overlay verde scuro; foto prioritaria | Home, La Villa, Ristorante, Eventi, Matrimoni, Franciacorta |
| C02 | Hero testuale | Section avorio > container > title/text/CTA + aside | Heading H1, Text, Button, Icon List | 95 px vertical; mobile 70; due aree desktop | Contatti |
| C03 | Section heading | Flex column | Text eyebrow, Heading H2, Text | Max-width 680–780; gap 18–24 | Tutte; versione centered e left |
| C04 | Split editoriale | Grid/Flex 2 columns | Heading, Text, Button, Image | Gap ~95; image 510; responsive 1 column | Intro, storia, cucina, territorio, event, matrimon |
| C05 | Image card | Container relative > Image + gradient overlay + text | Image, Heading, Text, link | Photo 400–520, object-fit cover | Home ambienti; non richiede widget HTML |
| C06 | Card servizi/eventi | Grid 3 > Card image/text/CTA | Image, Heading H3, Text, Text link | Gap 23–25; img 260–290 | Home eventi; Cerimonie |
| C07 | Card sala | Grid 3 > photo + number + heading + description | Image, Text, Heading H3 | Background avorio; photo 345 | La Villa, nomi foto da confermare |
| C08 | Gallery fotografica | Grid 4 o masonry controllata | Image / Basic Gallery se mantiene crop | Gap 14–22; 255 px tile | Ristorante, parco; no slider pesanti |
| C09 | CTA band | Section colorata > center/flex column | Eyebrow, Heading, Text, Button | Padding 80–105; crema o champagne | Finale Ristorante, Contatti, Matrimoni |
| C10 | FAQ | Column > Accordion | Accordion nativo o Atomic Accordion | Max 900, divider #C6C5B9 | Cerimonie; mantenere domanda/risposta editabili |
| C11 | Form richieste | Grid 0.75/1.25 > Text + Form | Elementor Pro Form (se installato) | 2 campi/row desktop; 1 mobile | Contatti; invio, SMTP e privacy da configurare |
| C12 | Mappa/indirizzo | Grid 0.78/1.22 | Heading, Text, Button link Maps, Map/HTML consentito | 420 desktop/350 mobile | Contatti; caricare embed solo se conforme alle scelte privacy |
| C13 | Panel editoriale territorio | Grid 3 > card number/decor/title/body | Container, Text, Heading | Min-height 370, sfondi differenziati | Franciacorta; lettere decorative con Text/Heading |
| C14 | Quote decorativa | Section center > separator > Text > caption | Divider, Text, Text | Fondo sabbia; 76 px vertical | Home; non trasformare in testimonianza attribuita |

## Classi proposte per Elementor

- `vc-section`: sezione standard con padding verticale responsivo.
- `vc-container`: max-width 1200 e gutter.
- `vc-eyebrow`, `vc-section-heading`, `vc-body-copy`: tipografia.
- `vc-hero`, `vc-hero--home`, `vc-hero--inner`: hero.
- `vc-split`, `vc-card-grid`, `vc-gallery-grid`: layout.
- `vc-button`, `vc-button--outline`, `vc-button--light`: stati bottoni.
- `vc-image-cover`: gestione crop, oggetto e proporzione.
- `vc-bg-forest`, `vc-bg-ivory`, `vc-bg-sand`: background.

Definire le classi globali nel gestore classi/variabili di Elementor, evitando selettori generici come `header`, `.container` o `.title` nel CSS personalizzato.

## Theme Builder

**Header** — un solo template globale. Desktop con logo e sette voci sempre visibili, fondo opaco; mobile con logo, chiamata e navigazione compatta. Verificare comportamento nativo del menu disponibile. Link della CTA Contattaci a `/contatti/`.

**Footer** — un solo template globale. Indirizzo, telefono, sette link, copyright, privacy, cookie e dati societari **solo dopo verifica**. La fonte HTML usa note provvisorie; non importarle come testi legali definitivi.

**Pagine** — template Default o Full Width appropriato, non Canvas se deve mostrare header/footer globali. Impostare condizioni di visualizzazione Entire Site per parti globali, evitare duplicazioni.

## Animazioni e interazioni

- Hover: leggero zoom immagini card (circa 1.04–1.05), underline navigazione, lift del button 2 px.
- Smooth scroll solo se accettabile per `prefers-reduced-motion`.
- Menu mobile: apertura/chiusura e focus tastiera; preferire widget nativo; fallback senza JS.
- FAQ: accordion con tastiera e ARIA.
- Form: campi obbligatori, validazione, invio reale, messaggi stato e antispam.
- Mappa: link esterno funzionante e scelta di caricamento embed.
- **Non introdurre** animazioni di entrata, parallax o slider non presenti nel prototipo.

## Elementor Pro, plugin e codice

| Funzione | Opzione preferita | Dipendenza |
|---|---|---|
| Header/footer globali | Theme Builder Elementor | In pratica Elementor Pro o equivalente supportato dall'installazione |
| Modulo contatti | Form widget Elementor | Elementor Pro |
| Menu responsive | Nav Menu/Atomic menu compatibile con editor | Verificare release e widget disponibili |
| FAQ | Accordion nativo | In genere senza plugin dedicati |
| Gallery | Image/Grid nativi | Nessun plugin se layout semplice |
| Google Map | Widget nativo o Embed con consenso | Verificare privacy e policy |
| SMTP | WP Mail SMTP o invio transazionale approvato | Plugin/configurazione server |
| SEO | Plugin SEO o metadati gestiti da WordPress | Scelta da definire, un solo proprietario dei metadati |

Non replicare le pagine dentro widget HTML. Usare custom CSS soltanto per il minimo scostamento non raggiungibile con proprietà responsive e classi native.
