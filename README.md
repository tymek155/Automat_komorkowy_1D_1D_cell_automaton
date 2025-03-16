Go to [English version](#english-version)
# Ogólne informacje
Projekt realizuje implementację jednowymiarowego automatu komórkowego, wraz z 
dwoma warunkami brzegowymi - periodycznym oraz absorpcyjnym (w pierwszym skrajne 
komórki sąsiadują z komórkami przy przeciwnej granicy, w drugim komórki skrajne 
sąsiadują z komórkami o stałej wartości równej 0). Automat generuje odpowiednie 
stany komórek (0 lub 1) na podstawie zadanej reguły binarnej i zapisuje wyniki 
do pliku w formacie CSV.

# Technologie
W kodzie użyto:
* Python 3.12
* moduł `csv`
* moduł `random`
	
# Wykorzystanie
Kod był uruchamiany i napisany w środowisku PyCharm. Struktura kodu składa się 
z funkcji `zapisz_do_csv`, która zapisuje wszystkie stany do pliku CSV o 
odpowiednim numerze zgodnie z iteracją, `decimal_to_binary_with_padding` 
konwertującej zadaną liczbę reguły na ciąg binarny 8-bitowy, `slownik_reguly` 
tworzącej strukturę słownika, mapującą odpowiednie kombinacje 3-bitowe na nowe 
stany komórek, `generate_p` generującej nowy stan dla warunków periodycznych - 
wykonuje sprawdzenie sąsiadów z zawinięciem brzegów, `generate_a` generującej 
nowy stan dla warunków absorpcyjnych - końce zawsze są zerowe, `automat_periodyczny` 
odopowiadającej za symulację automatu periodycznego, `automat_absorpcyjny` 
odpowiadajćej za symulację automatu absorpcyjnego oraz `main`, gdzie użytkownik w 
zaprojektowanym menu może wybrać liczbę komórek, liczbę iteracji oraz numer reguły.

## Przykładowe użycie z warunkiem brzegowym periodycznym
<img width="731" alt="image" src="https://github.com/user-attachments/assets/74a797b2-5cdc-4920-9602-ae4bba1039c3" />

## Przykładowe użycie z warunkiem brzegowym absorpcyjnym
<img width="695" alt="image" src="https://github.com/user-attachments/assets/ae341e89-9402-430d-80a1-29dbf58c66d8" />


# English version
  
# General Information  
The project implements a one-dimensional cellular automaton with two boundary 
conditions: periodic and absorptive (in the first, the edge cells neighbor 
cells at the opposite boundary; in the second, the edge cells neighbor cells 
with a fixed value of 0). The automaton generates cell states (0 or 1) based 
on a specified binary rule and saves the results to a CSV file.  

# Technologies  
The code uses:  
* Python 3.12
* `csv` module
* `random` module

# Usage  
The code was run and written in the PyCharm environment. The code structure 
consists of the function `zapisz_do_csv`, which saves all states to a CSV file 
with a corresponding number according to the iteration, 
`decimal_to_binary_with_padding`, converting a specified rule number into an 
8-bit binary string; `slownik_reguly`, creating a dictionary structure mapping 
3-bit combinations to new cell states; `generate_p`, generating a new state for 
periodic boundary conditions – checking neighbors with edge wrapping; `generate_a`, 
generating a new state for absorptive boundary conditions – ends are always zero, 
`automat_periodyczny`, responsible for simulating the periodic automaton, 
`automat_absorpcyjny`, responsible for simulating the absorptive automaton, 
and `main`, where the user can select the number of cells, number of iterations, 
and rule number in the designed menu.  


## Example use with periodic boundary condition
<img width="731" alt="image" src="https://github.com/user-attachments/assets/74a797b2-5cdc-4920-9602-ae4bba1039c3" />

## Example use with absorption boundary condition
<img width="695" alt="image" src="https://github.com/user-attachments/assets/ae341e89-9402-430d-80a1-29dbf58c66d8" />
