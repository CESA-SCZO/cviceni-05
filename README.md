# Cvičení 5

**Klonování repozitáře:**
- Klávesa Windows + R -> cmd -> Enter
```
mkdir c:\SCZO_2026
cd C:\SCZO_2026
git clone https://cesta.ke.forked.git.repozitari
uv sync
```

**Úkol 1:**
- Načtěte obraz 'basket.jpg' a převeďte jej na šedotónový obraz.
- Vytvořte obraz o velikosti načteného obrazu obsahující pouze aditivní gaussovský šum s nulovou střední hodnotou a rozptylem 0,3 (np.random.normal()).
- Zobrazte vytvořený šum spolu s jeho amplitudovým spektrem (využijte k tomu přiloženou funkci 'plot_3D()') a histogramem.
- Přidejte šum k originálnímu obrazu Vámi vytvořeným gaussovským šumem.
- Zobrazte v jednom okně originální obraz, jeho zašuměnou variantu a odpovídající histogramy.
- Měňte parametry šumu a pozorujte, jaký mají vliv na výsledný obraz. Zobrazte zároveň jeho spektrum a histogram šumu.

**Úkol 2:**
- Načtěte obraz 'basket.jpg' a převeďte jej na šedotónový obraz.
- Zašumte tento obraz impulsním šumem s hustotou zašumění 0,3 (random_noise()).
- Zobrazte zašuměný obraz spolu s jeho amplitudovým spektrem (využijte k tomu přiloženou funkci 'plot_3D()') a histogramem.
- Získejte obraz obsahující pouze použitý impulsní šum.
- Zobrazte obraz impulsního šumu spolu s jeho amplitudovým spektrem (využijte k tomu přiloženou funkci 'plot_3D()') a histogramem.
- Měňte parametry šumu a pozorujte, jaký mají vliv na výsledný obraz. Zobrazte zároveň spektrum a histogram jak obrazu, tak šumu.

**Úkol 3:**
- Definujte impulzní charakteristiky průměrujících konvolučních masek o velikostech 3x3, 7x7, 11x11.
- Definujte impulzní charakteristiky gaussovského filtru (gaussian_filter()) s rozptylem 3, 7 a 11.
- Zobrazte amplitudovou frekvenční charakteristiku jednotlivých filtrů.
- Pomocí definovaných průměrujících masek filtrujte ten zašuměný obraz, jehož šum lze potlačit pomocí průměrování.
- Pomocí mediánové filtrace s maskou o velikosti 3x3 filtrujte ten zašuměný obraz, jehož šum lze potlačit pomocí této filtrace.
- Měňte velikost masky a pozorujte, jaký mají vliv na výsledný obraz.

**Úkol 4:**
- Najděte a stáhněte si obrázek Vašeho favorita (vybírejte obrázek do velikosti 500x500, případně jej na tuto velikost podvzorkujte).
- Vygenerujte dvourozměrnou harmonickou funkci s parametry A=1, u=8, v=13, φ=0.
- Pomocí vygenerované harmonické funkce zašumte Vámi vybraný obraz favorita šumem moiré.
- Zobrazte spektra jak originálního, tak zašuměného obrazu favorita.
- Odstraňte úzkopásmový šum z obrázku pomocí nulování daných frekvencí ve spektru.
- Zobrazte zašuměný a vyfiltrovaný obraz spolu s jejich amplitudovými spektry.

**Závěr cvičení:**
```
git add .
git commit –m „message“
git push origin main
```