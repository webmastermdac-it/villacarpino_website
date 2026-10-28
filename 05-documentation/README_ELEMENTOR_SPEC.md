# Villa Carpino — specifica di implementazione Elementor

Questa cartella contiene il reference HTML/CSS/JS delle sette pagine e i sette documenti richiesti per la ricostruzione tramite Codex + Elementor MCP. **Non contiene template JSON Elementor dichiarati importabili.**

## Documenti principali

1. `elementor-page-map.md` — 36 sezioni, foto, struttura container, ordine.
2. `elementor-components.md` — header/footer globali e componenti comuni.
3. `elementor-design-system.json` — token di design MDAC non importabili direttamente in Elementor.
4. `elementor-responsive.md` — comportamento per breakpoint e QA.
5. `elementor-widgets-map.csv` — 38 righe di mapping sezione/widget, incluse 2 globali.
6. `elementor-custom-code.md` — codice residuo e criteri per Pro/plugin.
7. `elementor-migration-plan.md` — fasi, gate, prompt e controlli.

## Asset e sorgenti

- `*.html` — sette pagine navigabili.
- `styles/` e `scripts/` — codice frontend.
- `assets/images/` — WebP generati da fotografie autentiche.
- `assets/originals/` — archivio fotografico JPEG e logo.
- `image-map.csv` — mapping media VC-xx.
- `elementor-page-map.csv` — mapping URL SEO.

## Limiti espliciti

- Nessuna connessione WordPress è stata effettuata.
- Nessun JSON di template Elementor è stato inventato.
- L'installazione Elementor reale (release, widget, schema export) non è disponibile.
- Form, privacy, cookie e dati societari non sono pronti per la pubblicazione.
- Il reference HTML richiede ancora QA visiva browser finale prima del gate di fedeltà.

## Sequenza di lettura per Codex

1. `elementor-migration-plan.md`
2. `elementor-design-system.json`
3. `elementor-components.md` e `elementor-responsive.md`
4. `elementor-page-map.md` e `elementor-widgets-map.csv`
5. `elementor-custom-code.md`

Le specifiche definiscono valori target; replicare le proprietà originali dell'HTML e segnalare ogni divergenza rilevante prima di procedere.
