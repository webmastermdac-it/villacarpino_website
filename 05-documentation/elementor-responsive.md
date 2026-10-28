# Villa Carpino — specifica responsive per Elementor

## Baseline e metodo

- Riferimento: HTML/CSS nella cartella `villa_carpino_final`, non una cattura fotografica definitiva.
- Larghezza contenuto ordinaria: **1200 px max**; header: **1390 px max**.
- Desktop: gutter 40 px per lato; mobile: 19–21 px.
- I valori nella tabella sono target di configurazione Elementor; verificare ogni breakpoint con screenshot comparativi prima di pubblicare.
- Il codice originario usa soglie 1200, 1100, 1000, 850, 800, 760, 510 e 480 px. Evitare di ricostruirle tutte alla cieca: preferire i breakpoint Elementor disponibili e applicare eccezioni solo dove il layout ne ha bisogno.

| Fascia | Configurazione target | Comportamento |
|---|---|---|
| Desktop >1200 px | container 1200; section padding 105/112 verticali | Due colonne, griglie 3/4, header con sette voci |
| Laptop 1025–1200 px | gutter 21–40; gap ridotti | Header compatto, immagini in cover |
| Tablet 801–1024 px | container fluid; colonne se ancora leggibili | Ridurre gap/heading; verificare wrap del menu |
| Mobile <=800 px | padding sezioni 70; gutter 21 | Header con logo, Chiama e details Menu; due colonne diventano una |
| Piccolo mobile <=480 px | H1 circa 41; cards 1 colonna | Gallery 2 colonne dove leggibile; form a una colonna |

## Componenti

### Header

- Desktop: sfondo pieno `#2D3B30`, altezza minima 112 px, logo 210 px, menu 7 link a vista, ultima voce “Contattaci” color avorio.
- Mobile <=800: fascia circa 85 px, logo circa 175 px, pulsante `Chiama` e comando `Menu`. Implementare con menu nativo responsive; in HTML reference si usa `details/summary` senza dipendere da JavaScript.
- Niente CTA “Prenota un tavolo” nell'header. L'attività di prenotazione resta nelle sezioni del sito.

### Hero

- Home: altezza minima 665 px desktop / 690 px mobile, fotografia VC-04 in cover e overlay scuro; H1 in primo piano, CTA.
- La Villa: 630 / 590 px, VC-25, testo in primo piano.
- Ristorante, Cerimonie, Matrimoni, Franciacorta: minima 550 / 530 px, fotografia in cover, overlay 90° e contenuto allineato a sinistra.
- Contatti: hero editoriale avorio senza fotografia, intenzionalmente diversa.
- Foto hero: priorità alta, niente lazy. Su Elementor confrontare ritaglio e `object-position` con HTML.

### Sezioni split

- Desktop: 2 colonne circa 50/50, gap 95 px, contenuto verticalmente centrato, fotografia 510 px in altezza.
- La Villa intro: 0.95fr/1.05fr; storia: 1fr/1fr con gap 110 px; altri split 1fr/1fr.
- Mobile <=800: una colonna; mantenere ordine narrativo testo/foto previsto; fotografia circa 350–400 px.
- Evitare altezze fisse su testi; usare `min-height` soltanto se serve.

### Griglie

- Home ambienti 2 colonne (1.2/0.8), mobile 1; altezza card 520 / 400 px.
- Home eventi 3 colonne, mobile 1.
- Sale La Villa 3 colonne, mobile 1; foto 345 / 340 px.
- Ristorante gallery 4 colonne desktop, 2 mobile; foto 255 / 205 px.
- Cerimonie 3 colonne, tablet 2, mobile 1; foto 260–270 px.
- Franciacorta 3 card testuali desktop, 1 mobile.
- Matrimoni: 2 fotografie sfalsate, mobile in colonna con altezza 340 px.

### Form e mappa

- Contatti form: layout 0.75fr/1.25fr desktop e una colonna <=850; campi due colonne fino a 510, poi una.
- Form nativo Elementor Pro se disponibile; non replicare lo script demo HTML.
- Mappa: 0.78fr/1.22fr desktop, in colonna <=850, altezza circa 420 / 350 px.
- Prima del caricamento della mappa terza parte, definire la gestione privacy.

### Accessibilità e test

1. Viewport: 1440, 1280, 1024, 820, 768, 430, 390, 320 px.
2. Verificare overflow orizzontale, ordine di lettura, tap target >=44 px, visibilità focus, contrasto.
3. Controllare il menu aperto, Escape, tastiera, CTA telefonica, form, FAQ e link mappa.
4. Impostare dimensioni intrinseche delle immagini per contenere il CLS; lazy solo sotto il fold.
5. Confrontare screenshot delle sezioni in Elementor rispetto al reference HTML, senza correggere la fonte grafica approvata.
