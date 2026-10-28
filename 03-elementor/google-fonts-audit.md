# Audit Google Fonts — Villa Carpino

## Famiglie effettivamente utilizzate

| Ruolo | Famiglia Google Fonts | Pesi CSS richiesti | File presenti |
|---|---|---|---|
| Titoli, numeri e dettagli editoriali | **Playfair Display** | 400, 500, 600 | `playfair-display-{400,500,600}.ttf` |
| Body, navigazione, eyebrow, CTA, form | **DM Sans** | 400, 500, 600, 700 | `dm-sans-{400,500,600,700}.ttf` |

Nessun'altra famiglia principale è dichiarata nel CSS; `Georgia`, `Arial`, `serif` e `sans-serif` sono esclusivamente fallback di sistema, non font creativi aggiuntivi. La famiglia e il peso dichiarati nei sette file font sono stati ispezionati tramite metadata OpenType. Tutte le pagine importano `styles/fonts.css`, con `font-display: swap`.

**Strategia di consegna:** mantenere nel riferimento HTML i TTF locali ottenuti da Google Fonts, senza alcuna richiesta a Google Fonts CDN. Questo rispetta l'uso esclusivo di famiglie Google Fonts e permette navigazione HTML autonoma. In WordPress usare **Site Settings → Global Fonts** di Elementor, assegnando Playfair Display a Primary e DM Sans a Secondary/Text/Accent, oppure i nomi esatti della configurazione in `elementor-global-typography.json`.

Per WordPress scegliere **un solo caricatore**: Google Fonts integrato in Elementor **oppure** self-hosting di file font (se la configurazione e privacy lo richiedono). Non caricare sia i TTF locali sia gli stessi font dal CDN: duplicazioni possono peggiorare performance e creare divergenze di rendering. Se si sceglie l'API, la sintassi CSS2 ufficiale è:

`https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@400;500;600&display=swap`

Questa è una **specifica** e non viene aggiunta all'HTML per evitare una modifica tecnica arbitraria del Master. I valori degli heading sono anche nel design system, mentre le varianti per singola sezione restano descritte nei CSS HTML; vanno imitate puntualmente durante la conversione visuale.

## Punti tecnici aperti

- I TTF sono validi ma più grandi dei WOFF2: una conversione verificata in WOFF2 potrà essere eseguita nell'ambiente WordPress se si adotta self-hosting.
- La disponibilità di pesi e impostazioni globali deve essere verificata contro la versione effettiva di Elementor dopo il collegamento MCP.
- Eventuali richieste Google Fonts da tema WordPress o plugin devono essere disattivate per evitare famiglie non approvate.

Riferimento ufficiale: [Google Fonts CSS API v2](https://developers.google.com/fonts/docs/css2) e [Google Fonts Get Started](https://developers.google.com/fonts/docs/getting_started/).
