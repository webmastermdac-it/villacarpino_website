# Villa Carpino — Pacchetto definitivo di migrazione Elementor

## Obiettivo

Ricostruire il sito di Villa Carpino, ristorante a Ome in Franciacorta, con **WordPress e Elementor** e massima fedeltà alla versione HTML approvata. Testi, immagini, sezioni, pulsanti e layout devono rimanere modificabili nell'editor Elementor. **Non** usare una singola pagina HTML incorporata come soluzione di base.

Il pacchetto è una **specifica tecnica e una sorgente statica**, non un sito WordPress né un template JSON Elementor verificato. Non sono stati eseguiti accessi o pubblicazioni su WordPress.

## Come visualizzare il sito

Aprire `01-html-site/villa_carpino_home.html` nel browser. I link interni si riferiscono agli altri sei file nella stessa cartella; CSS, JS, immagini e font si caricano relativamente da `02-assets/`. In alternativa servire la cartella principale via un server HTTP statico. La mappa incorporata richiede connessione a Internet; il form Contatti è dimostrativo.

## Pagine

| Pagina | File HTML | Permalink WordPress da configurare |
|---|---|---|
| Home | `villa_carpino_home.html` | `/` |
| La Villa | `la-villa.html` | `/la-villa/` |
| Ristorante | `ristorante-franciacorta.html` | `/ristorante-franciacorta/` |
| Cerimonie ed eventi | `cerimonie-eventi-franciacorta.html` | `/cerimonie-eventi-franciacorta/` |
| Matrimoni | `matrimoni-franciacorta.html` | `/matrimoni-franciacorta/` |
| Franciacorta | `franciacorta.html` | `/franciacorta/` |
| Contatti | `contatti.html` | `/contatti/` |

## Struttura cartelle

- `01-html-site/`: sette pagine HTML complete e navigabili, con riferimenti agli asset nella cartella gemella.
- `02-assets/`: `css/`, `js/`, `fonts/`, `images/originals/` (JPG originali e logo), `images/webp/` (varianti preesistenti), `images/ai-enhanced/` (WebP definitivi e varianti da 480 px).
- `03-elementor/`: mappa pagine, widget e componenti, design system, responsive, CSS/JS necessario, audit font e tipografia globale.
- `04-seo/`: mappatura SEO, sezioni, link e immagini, URL WordPress, checklist, inventario testi e cartella `schema-markup/` con limitazioni.
- `05-documentation/`: audit, report fotografico, dipendenze, funzionalità, integrità dei file, README tecnici precedenti.
- `06-migration/`: ordine di lavoro, caricamento Media Library, configurazione Elementor e checklist collaudo.

Il documento prioritario per una nuova sessione Codex è **`HANDOFF-CODEX.md`**, nella radice.

## Design approvato

Classico contemporaneo premium, avorio caldo e verde bosco, accenti champagne, titoli **Playfair Display**, testi e navigazione **DM Sans**. Entrambi sono Google Fonts; nel riferimento statico sono serviti da file TTF locali, senza richieste a servizi font esterni. Su WordPress selezionare una sola strategia di caricamento e configurare Elementor Global Fonts. Header con sfondo opaco, sette voci desktop sempre visibili, senza pulsante di prenotazione nell'header.

## Dipendenze

- HTML, CSS e JavaScript vanilla, senza framework CSS/JS esterni.
- Google Fonts Playfair Display e DM Sans, già inclusi localmente.
- Google Maps nella pagina Contatti: unico contenuto embedded remoto rilevato.
- In WordPress: versione Elementor/Pro, tema, plugin SEO e modulo contatti da accertare prima della costruzione.

## Migrazione consigliata

1. Leggere `HANDOFF-CODEX.md` e `06-migration/elementor-migration-plan.md`.
2. Verificare in WordPress versioni, tema, Elementor MCP e disponibilità Theme Builder.
3. Impostare il design system e tipografia globali da `03-elementor/`.
4. Caricare foto ottimizzate, conservando master JPEG e mappa alt.
5. Realizzare globalmente header/footer; ricostruire tutte le pagine con container e widget Elementor.
6. Applicare URL, titoli, descrizioni, H1 e collegamenti di `04-seo/`.
7. Configurare form reale, policy privacy e dati societari verificati.
8. Collaudare su staging con browser reale e misurazioni Core Web Vitals.

## Limitazioni e controlli

Superati i test statici sui file HTML Master, asset, immagini, CSS e JS; il sito riorganizzato richiede anch'esso il test dei percorsi in `05-documentation/technical-final-audit.md`. Non sono stati eseguiti test visuali browser/Lighthouse. Le fotografie migliorate sono frutto di correzioni deterministiche conservative, **non** di elaborazione generativa AI. Nessun template JSON Elementor è dichiarato importabile senza verifica della reale installazione.

Punti aperti: form non collegato; dati legali e recapiti da confermare; mappa/consenso; domini canonical e sitemap da impostare; foto storiche da validare editorialmente; test responsive visuali e performance reali da completare.
