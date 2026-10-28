# SEO, contenuti e immagini — matrice di migrazione

La documentazione CSV di questa cartella è estratta direttamente dalle sette pagine HTML Master V1.1, senza riscrittura editoriale.

## File prodotti

- `seo-page-inventory.csv`: URL, file originale, SEO title, meta description, H1 e conteggi.
- `seo-content-sections.csv`: sequenza di 42 elementi `section`/`article`, ID, classi, titoli e anteprima testo per creare container e widget modificabili.
- `seo-image-map.csv`: tutti i 58 inserimenti `<img>` nelle sette pagine, compresi logo ripetuto, fallback JPEG, WebP, `srcset`, alt, dimensioni e lazy loading.
- `seo-internal-links.csv`: i 175 link non esterni come appaiono nei documenti, inclusi menu/header/footer e anchor di sezione.
- `elementor-global-typography.json`: assegnazione globale Playfair Display e DM Sans; **specifica di configurazione, non template Elementor importabile**.

## URL canonici pianificati

| Pagina | WordPress | File Master |
|---|---|---|
| Home | `/` | `villa_carpino_home.html` |
| La Villa | `/la-villa/` | `la-villa.html` |
| Ristorante | `/ristorante-franciacorta/` | `ristorante-franciacorta.html` |
| Cerimonie ed eventi | `/cerimonie-eventi-franciacorta/` | `cerimonie-eventi-franciacorta.html` |
| Matrimoni | `/matrimoni-franciacorta/` | `matrimoni-franciacorta.html` |
| Franciacorta | `/franciacorta/` | `franciacorta.html` |
| Contatti | `/contatti/` | `contatti.html` |

## Regole vincolanti per Codex + Elementor MCP

1. Creare le sette pagine con i permalink indicati; home come front page di WordPress.
2. Trascrivere SEO title, meta description e H1 **esattamente** dal CSV; non generare nuovi claim o copy. Usare il plugin SEO effettivamente installato.
3. Ricostruire sezione per sezione con container e widget Elementor nativi; lasciare modificabili testi, fotografie, pulsanti e sfondi.
4. Caricare le foto WebP di `assets/images/ai-enhanced/`, con i JPEG originali nell'archivio media come master/fallback. Riassegnare l'alt indicato, verificando i duplicati.
5. Sostituire riferimenti locali `.html` con i permalink WordPress e testare tutti i link dopo la migrazione. Conservare gli anchor in-page.
6. Creare header/footer globali in Theme Builder se disponibile. Header opaco, sette voci sempre visibili su desktop, nessun pulsante di prenotazione nell'header; CTA telefonica e menu compatto su mobile.
7. Non convertire le pagine in un singolo widget HTML e non importare JSON Elementor non verificati.
8. Preservare l'ordine e la gerarchia delle sezioni; eventuali variazioni vanno segnalate prima di applicarle.

## Questioni SEO da verificare nell'istanza reale

- Dominio pubblico e canonical: non inseriti per mancanza di URL di produzione confermato.
- Sitemap XML, robots.txt e indicizzazione: saranno gestiti in WordPress, non nei file statici.
- Social Open Graph, dati strutturati LocalBusiness/Restaurant e breadcrumb: proposte tecniche da verificare, **non aggiunte** per non modificare la struttura SEO approvata.
- Recapiti, orari, menu e dati societari: confermare prima di usarli in structured data, footer o snippet.
- Form contatti: nel Master è una demo e richiede backend, consenso/privacy e antispam.
- Fotografie storiche dei piatti: non associarle a un menu corrente senza verifica.
