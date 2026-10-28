# Villa Carpino — codice personalizzato minimo

## Decisione

Obiettivo **zero JS personalizzato per layout e navigazione**. La maggior parte della resa va ottenuta con container, Grid/Flex, classi globali, sfondi, filtri overlay e stati hover Elementor. Questo file documenta soltanto gli scostamenti potenziali. Non incollare automaticamente questi frammenti: usarli solo se l'editor effettivo non offre l'impostazione nativa.

## CSS opzionale

### Riduzione del movimento

Se gli effetti hover nativi non rispettano automaticamente le preferenze utente:

```css
@media (prefers-reduced-motion: reduce) {
  .vc-image-card img,
  .vc-button {
    transition: none !important;
    animation: none !important;
  }
}
```

### Ritaglio immagini e proporzioni

Preferire in Elementor height/aspect-ratio, object-fit Cover e object-position per dispositivo. In caso di limitazione:

```css
.vc-image-cover img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}
```

### Eventuale card cliccabile

Preferire link nativo sul container o un unico widget link completo. Non sovrapporre un elemento `a` assoluto invisibile se il container può già essere reso cliccabile in modo accessibile.

## Interazioni da ricostruire senza JS

1. **Menu mobile:** usare un menu nativo Elementor con toggle accessibile. La versione HTML usa `details/summary` come fallback; non occorre portare lo script originale.
2. **FAQ:** Accordion nativo con navigazione tastiera.
3. **Scroll a sezioni:** anchor o scroll HTML semplice; rispettare `prefers-reduced-motion`.
4. **Hover cards:** transizione immagine lieve (scale 1.04–1.05) dove possibile in editor.
5. **CTA telefono:** link `tel:` diretto.
6. **Mappa:** link esterno a Maps; embed eventuale solo dopo decisione privacy.

## Form Contatti

- Il form nel reference HTML è **dimostrativo**; non portare il listener `submit` come implementazione definitiva.
- Creare Elementor Pro Form con campi Nome, Email, Telefono, Tipologia, Data, Numero ospiti, Messaggio.
- Mappare field IDs stabili (es. `name`, `email`, `phone`, `request_type`, `date`, `guests`, `message`).
- Configurare Actions After Submit, destinatario autorizzato, From Email sul dominio, SMTP, antispam, log di test, notifiche e messaggi stato.
- Informativa privacy e checkbox/eventuale consenso secondo indicazioni legali approvate; non inventare testi.
- In caso di esito negativo, mostrare un messaggio utile senza falsi successi.

## Font e dipendenze

- Il reference HTML usa DM Sans e Playfair Display, originariamente da Google Fonts. Caricare file locali o usare le impostazioni font Elementor solo dopo aver verificato disponibilità/licenze e varianti effettive.
- Non introdurre jQuery, caroselli o plugin per semplici griglie.
- Le 27 fotografie impiegate hanno WebP derivati e JPEG originali nel pacchetto; preferire WebP, preservando rapporto e crop.

## Differenze inevitabili HTML → Elementor

| Aspetto | HTML | Elementor |
|---|---|---|
| Header/footer | Markup statico condiviso nel pacchetto | Documenti Theme Builder |
| CSS | File separati per layout e pagina | Classi globali + variabili + impostazioni elemento |
| Grid | Regole CSS e fr unit | Atomic Grid/Flex; gap e percentuali equivalenti |
| Picture/WebP | `picture` con fallback JPEG | Media Library WordPress e output responsive generato |
| Form | Demo senza invio | Widget Form e workflow server-side |
| Menu mobile | `details/summary` | Widget menu nativo, da verificare |
| URL | Collegamenti locali a `.html` | Permalink WordPress |
| Metadati | Tag HTML | CMS/SEO plugin |

## Verifica template JSON Elementor

**Stato: NON VERIFICATO. Nessun JSON Elementor importabile è incluso.** Il file `elementor-design-system.json` è un manifesto MDAC, non un documento esportato da Elementor.

La documentazione Elementor descrive il JSON come struttura serializzata di pagina/template e consente importazioni .json/.zip; tuttavia la compatibilità dipende dal tipo di documento, dai widget e dalla versione/schema installati.

Prima di produrre un template:

1. Verificare versioni WordPress, Elementor Core, Elementor Pro e disponibilità Atomic V4/MCP.
2. Creare nell'installazione di staging una pagina vuota con **una** sezione rappresentativa nativa.
3. Esportarla con la procedura ufficiale disponibile nell'editor installato.
4. Esaminare la struttura realmente esportata e il relativo `version`/widget types.
5. Reimportare una copia in staging e confrontare contenuto, CSS, classi e media.
6. Solo dopo, valutare template JSON generati automaticamente; preferenza per creazione diretta via MCP nativo.

Fonti ufficiali:
- https://elementor.com/help/how-to-build-and-edit-your-site-using-elementor-mcp/
- https://developers.elementor.com/docs/data-structure/
- https://elementor.com/help/template-library/
- https://elementor.com/help/import-and-export-elementor-website-templates/
