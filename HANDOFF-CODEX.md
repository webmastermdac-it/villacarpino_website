# HANDOFF CODEX — Villa Carpino / Elementor MCP

## Missione

Ricostruisci in WordPress/Elementor le sette pagine di Villa Carpino — ristorante con sale e parco a Ome (BS), in Franciacorta — **massimamente fedeli** a `01-html-site/`, rispettando testi, SEO, fotografia e design. Ogni sezione deve risultare modificabile attraverso container e widget nativi Elementor: **non inserire intere pagine in widget HTML**.

Non pubblicare e non modificare produzione senza autorizzazione espressa. Prima di operare, verifica WordPress/Elementor, plugin, MCP, tema, versioni e permessi effettivi. Non inventare strumenti MCP, capacità o template JSON importabili.

## Pagine e URL

| Ordine | Pagina | File | Permalink |
|---|---|---|---|
| 1 | Home | `villa_carpino_home.html` | `/` |
| 2 | La Villa | `la-villa.html` | `/la-villa/` |
| 3 | Ristorante | `ristorante-franciacorta.html` | `/ristorante-franciacorta/` |
| 4 | Cerimonie ed eventi | `cerimonie-eventi-franciacorta.html` | `/cerimonie-eventi-franciacorta/` |
| 5 | Matrimoni | `matrimoni-franciacorta.html` | `/matrimoni-franciacorta/` |
| 6 | Franciacorta | `franciacorta.html` | `/franciacorta/` |
| 7 | Contatti | `contatti.html` | `/contatti/` |

Sorgenti: `01-html-site/`. Mappa dettagliata delle sezioni e widget: `03-elementor/elementor-page-map.md`, `elementor-widgets-map.csv`, `elementor-components.md`; inventario DOM: `04-seo/seo-content-sections.csv`.

## Identità visiva e tipografia

- Palette e spaziature: `03-elementor/elementor-design-system.json`. Avorio caldo, antracite, verde bosco e champagne; serif elegante per titoli e sans leggibile per testo.
- Esclusivamente **Google Fonts**: **Playfair Display** per titoli, display e accenti; **DM Sans** per corpo, navigazione, pulsanti e form. Pesi Playfair 400/500/600; DM Sans 400/500/600/700.
- Configurazione: `03-elementor/elementor-global-typography.json`, `google-fonts-audit.md`. Usare Elementor Site Settings/Global Fonts, senza duplicare loader remoto e font self-hosted.
- Responsive: `03-elementor/elementor-responsive.md`. Verificare breakpoint nell'istanza reale; gli HTML CSS restano la fonte per valori esatti, ove differiscano dalle specifiche generiche.

## Elementi globali

- **Header** opaco e sempre visibile, **sette voci desktop sempre esposte**, senza pulsante Prenota un tavolo nell'header; menu mobile compatto e CTA telefonica. Verificare sticky effettivo dal CSS, senza inventare nuove animazioni.
- Footer coerente con logo, URL, recapiti, privacy/cookie/dati societari **solo dopo verifica**.
- Componenti riutilizzabili: hero fotografico, eyebrow, titoli, split testo+foto, card/gallery, CTA, form, map, FAQ dove presenti.
- Evitare widget HTML come container principale; CSS/JS custom solo se strettamente necessari, dopo prova dei widget nativi.

## Gestione fotografie

- Foto definitive: `02-assets/images/ai-enhanced/` — 27 WebP full size e 27 versioni `-480.webp`.
- Originali: `02-assets/images/originals/` — 41 JPG e logo; non sovrascrivere.
- Fonti di verità per collocazione e alt: `04-seo/image-manifest.csv`, `04-seo/seo-image-map.csv`, `05-documentation/photo-enhancement-manifest.csv`.
- Caricare nella Media Library e annotare gli **attachment ID reali**. Inserire immagini con widget Image/Background nativi e configurare `srcset` responsivo ove applicabile.
- Non sostituire immagini con stock o AI; non inventare dettagli e non descrivere piatti storici come menu attuale.

## SEO vincolante

- Copiare **esattamente** title, description, H1 e slug da `04-seo/seo-page-map.csv`.
- Usare `04-seo/wordpress-url-map.csv`, `04-seo/internal-links-map.csv` e `04-seo/content-inventory.md` per testi e relazioni.
- Preservare ordine H1-H6 e il testo di ogni pagina HTML. Non aggiungere servizi, promesse, orari o dati aziendali non verificati.
- Canonical e sitemap: configurare soltanto dopo conferma del dominio. `04-seo/schema-markup/README.md` spiega perché non è stato inventato JSON-LD.
- Verificare meta/robots e plugin SEO attivo sull'installazione; evitare duplicati o conflitti.

## Piano operativo in Elementor

1. Audit dell'ambiente e registrazione versioni/capacità di WordPress, Elementor, tema, SEO e MCP.
2. Site Settings: palette, font globali e larghezze; impostare header/footer con Theme Builder se supportato.
3. Caricare asset, attribuire alt e registrare mapping attachment ID reali.
4. Costruire Home e La Villa; confronto screenshot desktop/mobile con HTML Master prima di scalare.
5. Costruire Ristorante, Cerimonie, Matrimoni, Franciacorta e Contatti con i widget suggeriti.
6. Collegare form reale con consenso/privacy e delivery; controllare map embed e relativo consenso.
7. Inserire SEO plugin metadata e permalink; ricontrollare tutte le CTA e gli anchor.
8. Verificare mobile/tablet/desktop e accessibilità; valutare Core Web Vitals su staging.
9. Rilasciare solo dopo approvazione finale e correzione blocker.

## Dipendenze e problemi da non nascondere

- In HTML il modulo Contatti non invia email. Servono form compatibile, antispam e invio verificato.
- Google Maps è un iframe esterno che potrebbe richiedere consenso e gestione privacy.
- Recapiti, società e privacy/cookie policy non sono qui garantiti come aggiornati.
- Le foto migliorate sono state corrette con strumenti deterministici, non con generazione AI; alcune sono da 600×600 px.
- Nessun browser headless disponibile per il collaudo visuale/real CWV durante la creazione del Master.
- La struttura JSON Elementor importabile resta **non verificata** finché non si conoscono versione e API reali; il JSON incluso rappresenta un design system, non un template pronto.

## Checklist di accettazione

- [ ] Sette pagine con permalink esatti e contenuto modificabile in Elementor.
- [ ] Nessuna pagina incorporata integralmente in widget HTML.
- [ ] Header/footer globali fedeli e menu desktop sempre visibile, fondo opaco, nessun booking CTA in header.
- [ ] Solo Playfair Display e DM Sans come font grafici, con pesi e dimensioni equivalenti.
- [ ] Foto originali corrette e immagini enhanced in posizioni corrispondenti, con alt.
- [ ] SEO title, description, H1, testo, anchor e link interni fedeli al Master.
- [ ] Breakpoint e layout verificati a 1440, 1024, 768, 390 e 320 px.
- [ ] Tab/focus, tastiera, mobile nav, link, gallerie, moduli e mappa collaudati.
- [ ] Form reale testato end-to-end; policy e dati societari verificati.
- [ ] Lighthouse/Core Web Vitals misurati su staging e criticità risolte.
- [ ] Revisione visuale fianco a fianco e approvazione MDAC prima della pubblicazione.

**Fonte di verità:** HTML e asset dentro questa cartella, non mockup o screenshot non verificati. Il sito WordPress risultante deve riprodurre il più fedelmente possibile il Master HTML.
