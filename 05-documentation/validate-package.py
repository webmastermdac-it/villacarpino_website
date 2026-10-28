"""Offline validation of relocated Villa Carpino migration package."""
from pathlib import Path
import csv, json, re, hashlib
from urllib.parse import unquote
from lxml import html
from PIL import Image

root=Path(__file__).resolve().parents[1]
pages=list((root/'01-html-site').glob('*.html'))
assert len(pages)==7, len(pages)
expected_docs=['README.md','HANDOFF-CODEX.md','04-seo/seo-page-map.csv','04-seo/image-manifest.csv',
  '04-seo/internal-links-map.csv','04-seo/wordpress-url-map.csv','04-seo/content-inventory.md',
  '04-seo/seo-migration-checklist.md','03-elementor/elementor-global-typography.json',
  '03-elementor/google-fonts-audit.md']
for p in expected_docs: assert (root/p).is_file(), p

asset_refs=[]
for page in pages:
    doc=html.fromstring(page.read_text())
    assert len(doc.xpath('//main//h1'))==1, page
    assert doc.xpath('//title/text()'), page
    assert doc.xpath('//meta[@name="description"]/@content'), page
    for el in doc.xpath('//*[@src or @href or @srcset]'):
        values=[el.get(x,'') for x in ('src','href')]
        values.extend(v.strip().split()[0] for v in el.get('srcset','').split(',') if v.strip())
        for value in values:
            if not value or value.startswith(('#','http:','https:','tel:','mailto:','data:')): continue
            path=(page.parent/unquote(value.split('#')[0].split('?')[0])).resolve()
            assert path.is_relative_to(root.resolve()),(page,value)
            assert path.is_file() and path.stat().st_size>0,(page,value)
            asset_refs.append(path)
for css in (root/'02-assets/css').glob('*.css'):
    for token in re.findall(r'url\(([^)]+)\)',css.read_text()):
        val=token.strip(' "\'')
        if val.startswith(('data:','http:','https:')):continue
        target=(css.parent/val).resolve()
        assert target.is_file() and target.stat().st_size>0,(css,val)
for f in (root/'02-assets/images/ai-enhanced').glob('*.webp'):
    with Image.open(f) as im:im.verify()
assert len(list((root/'02-assets/images/ai-enhanced').glob('VC-*.webp')))==54
for f in root.rglob('*.json'):json.loads(f.read_text())
for f in root.rglob('*.csv'):
    with f.open(encoding='utf-8-sig',newline='') as h:list(csv.reader(h))
fonts=(root/'02-assets/css/fonts.css').read_text()
assert 'DM Sans' in fonts and 'Playfair Display' in fonts
assert 'fonts.googleapis.com' not in fonts
assert len(list((root/'02-assets/fonts').glob('*.ttf')))==7
print('PASS:',len(pages),'pages;',len(asset_refs),'local references; 54 enhanced WebP; JSON/CSV/font integrity')
