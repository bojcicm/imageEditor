# Image analysis and processing

Implement various basic image analysis and processing algorithms

### Task list for project:

- [x] Transformacija slike u boji u sliku sivih razina
  - Solution : `gray = 0.299⋅R+0.587⋅G+0.114⋅B`
- [x] Računanje histograma i kumulativnog histograma
- [x] Rastezanje histograma
- [x] Ujednačavanje histograma
- [x] Gamma korekcija
- [x] Amplitudna segmentacija (korisnik odabire prag temeljem prikazanog histograma slike)
- [x] Konvolucija (proizvoljnim filtrom koji zadaje korisnik)
- [x] Korelacija (proizvoljnim uzorkom koji zadaje korisnik)
- [ ] Median filter
- [ ] Image sharpening
- [ ] Otkrivanje magnitude i orjentacije rubova na slici
- [ ] Kombiniranje slika
- [ ] Morfološke operacije na binarnoj slici (erozija, dilatacija, opening, closing)

### Comments:
- Images loaded using opencv are in BGR not in RGB