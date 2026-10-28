# Handoff Codex / Elementor MCP — Prompt 4

## Stato

Sorgente tecnica: `../` (HTML Master V1.1, sette pagine con enhanced WebP). Il Master è **immutato** nei contenuti, nella navigazione e nella resa visiva. Sono stati aggiunti soltanto CSV, JSON e documentazione, e corretta una nota obsoleta nel design system Elementor.

## Ordine di lavoro consigliato

1. Verificare versione WordPress, Elementor, licenza Pro, theme, plugin SEO, plugin moduli e capacità del connettore MCP. Nessun JSON Elementor va dichiarato importabile prima di questa verifica.
2. Definire i colori e gli stili globali da `../elementor-design-system.json`. Applicare i font da `elementor-global-typography.json` con la strategia unica concordata nel font audit.
3. Realizzare e collaudare header/footer, mantenendo menu desktop opaco e sempre visibile e senza prenotazione in header.
4. Caricare la Media Library da `../assets/images/ai-enhanced/`; conservare master JPEG, registrare gli ID attachment restituiti e trasferire ALT dal CSV.
5. Costruire Home e La Villa come pagine pilota per validare tipografia, responsive, componenti e resa fotografica; proseguire Ristorante, Cerimonie, Matrimoni, Franciacorta e Contatti.
6. Inserire title, description, H1 e URL identici al CSV; aggiornare link interni ai permalink.
7. Configurare il form reale e la privacy; testare invio e consegna. Gestire eventuale consenso per iframe di Google Maps.
8. Verificare responsive e accessibilità con browser reale, poi Core Web Vitals su staging e SEO tecnico prima del go-live.

## File di riferimento prioritari

1. `seo-page-inventory.csv`
2. `seo-content-sections.csv`
3. `seo-image-map.csv`
4. `seo-internal-links.csv`
5. `elementor-global-typography.json`
6. `google-fonts-audit.md`
7. `../elementor-page-map.md`, `../elementor-widgets-map.csv`, `../elementor-components.md`, `../elementor-responsive.md`

## Verifiche effettuate

- Sette page title, sette description, sette H1 unici presenti.
- Ogni asset referenziato dall'inventario immagini è presente; i WebP enhanced sono verificati anche da `../tests/test_enhanced_images.py`.
- Nessuna famiglia tipografica artistica aggiuntiva a Playfair Display e DM Sans nel CSS; fallback di sistema consentiti.
- I test statici HTML e asset si eseguono con `python tests/test_site.py` e `python tests/test_enhanced_images.py` dalla cartella Master.

## Differenze non risolte

Nessuna pubblicazione o accesso WordPress effettuati. Non disponibili il reale schema Elementor, gli attachment ID Media Library, dominio canonical, sitemap, invio email, dati legali aggiornati o collaudo browser visuale. Questi non sono ricostruibili in modo affidabile dalla sola sorgente statica.
