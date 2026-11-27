# Vaimuraamat · lugemiste kujundamise demo

**ChatGPT-ga alustamiseks:** ava [gen.md](gen.md) ja anna ChatGPT-le selle faili link koos juhisega:

> Loe see juhend läbi ja alusta selles kirjeldatud töövoogu: https://github.com/sviljus/vr-demo/blob/main/gen.md

Otsefail: [gen.md raw-kujul](https://raw.githubusercontent.com/sviljus/vr-demo/main/gen.md).

ChatGPT peaks suhtlema eesti keeles, paluma Wordi faili ning küsima, kas kasutaja nõustub alamagendi lõppkontrolliga. Alamagentide ja failide töötlemise võimalused sõltuvad konkreetsest ChatGPT keskkonnast; link ei lisa puuduvaid tööriistu. Täpne nõusoleku ja võimalike piirangute käsitlus on juhendis.

- [Näidis-Word](reference/sample-02.docx) ja [näidis-PDF](reference/sample-02.pdf) — visuaalne võrdlusalus.
- [Näidislehekülgede pildid](reference/pages/) — võrdlemiseks ka ilma PDF-renderdajata.
- [Stiiliraamat](stylebook.md) — kujunduse ja toimetamise reeglid.
- [HTML-mall](templates/reading.html) ja [muudetav Wordi mall](templates/reading.docx).
- [Täidetud näidisandmed](data/reading-02.json) ja [tühi sisumall](data/reading.template.json).
- [Tööriistade kasutamine](docs/usage.md), [andmeskeem](data/reading.schema.json), [kontrollijuhend](review/subagent-checklist.md).

## Kohalik töövoog

```sh
npm ci
python3 -m pip install -r requirements.txt
npx playwright install chromium
python3 scripts/validate.py data/reading-02.json
python3 scripts/build.py data/reading-02.json --out build/sample-02.html
node scripts/pdf.cjs build/sample-02.html build/sample-02.pdf
python3 scripts/build_docx.py data/reading-02.json --out build/sample-02.docx
```

Python 3.10+ ja Node.js 20+. Täiteskript kasutab Python standardteeki. PDF-eksport kasutab Playwrighti, Chromiumi ja PDF-libi. Fondid: Georgia ja Arial või stiiliraamatus lubatud alternatiivid.

Töövoog: **Word → toimetatud sisu → JSON → HTML → PDF → visuaalne kontroll → nõusolekul alamagendi kontroll**.

Iga valmis töö väljundiks on nii muudetav Wordi fail (.docx) kui ka PDF. Iga kristalli pildi valikul tuleb avada ja võrrelda 3–4 fotot ning kontrollida nimetust, tüüpilist välimust ja kasutusõigusi. Võrdluse protokoll on [siin](review/crystal-image-review.template.md).

Roosa servariba näitab lehekülje asukohta kogu lugemises: kolme lehe puhul kolmandik, viie puhul viiendik. Jaotus arvutatakse pärast PDF-i tegeliku lehekülgede arvu selgumist.

Laaditud kliendifailid ja tulemused lähevad Gitist välja jäetud `incoming/` ning `build/` kaustadesse. Avalik repo sisaldab ainult üldist number 2 näidist, kujundust ja tööriistu. Piltide õigused on kirjas [RIGHTS.md](RIGHTS.md) ja [assets/manifest.json](assets/manifest.json).

Iga lugemise viimane sisulõik on eristatud lõpumõte: **Iga number räägib oma loo. Iga kivi kannab oma energiat.** Mõlemad generaatorid lisavad selle ühe korra ja eemaldavad sama mõtte varasemad kordused.
