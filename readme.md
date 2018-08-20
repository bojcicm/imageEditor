# Image analysis and processing

Implement various basic image analysis and processing algorithms.
Requirements:
- Python 2.7 + pip
- install python packages (numpy, matplotlib,..)
  - `pip install numpy`
  - `pip install matplotlib`
  - `pip install opencv-python`

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
- [x] Median filter
- [x] Image sharpening
- [x] Otkrivanje magnitude i orjentacije rubova na slici
- [x] Kombiniranje slika
- [x] Morfološke operacije na binarnoj slici (erozija, dilatacija, opening, closing)

### Comments:
- Images loaded using opencv are in BGR not in RGB
