CELTRA študentski izziv
=======================
Cilj iziva je bil maksimizirati dobiček pri igranju igralnih avtomatov, ki imajo različne možnosti
izplačila. Gre za tako imenovani multi-armed bandit problem.

Navodila za zagon

Gitbash ukaz: git clone https://github.com/polysalama/celtra

a) Kot izvršljiva Windows 7/8/8.1 datoteka:
Povezava do izvršljive datoteke: https://github.com/polysalama/celtra/raw/master/bandit.7z
Izvršljiva datoteka deluje samo na 64 bitni verziji operacijskega sistema!
Iz repozitorija povlecite bandit.7z arhiv in ga razširite. Odprite ukazno vrstico in se prestavite v imenik
kamor ste razširili arhiv. Program zaženete z ukazom:

>>>bandit.exe http://<ime_domene>/<št._primera>

Program bo po končanem izvajanju izpisal število uspešnih potegov.

b) Kot Python skripta:
Povezava do skripte: https://github.com/polysalama/celtra/raw/master/source/bandit.py
Pred uporabo je potrebno namestiti:
- Python 3.4 https://www.python.org/download/releases/3.4.0/
- NumPy 1.9.1 http://www.numpy.org/
- SciPy 0.14 http://www.scipy.org/
Najprej namestite Python. V PATH dodajte pot do Python34 in Python/Scripts direktorija. Za
namestitev NumPy-a in SciPy-a v ukazni vrstici zaženite:

>>>pip install numpy
>>>pip install scipy

Za Windows platformo lahko SciPy in NumPy dobite tudi v obliki primerni za klasično nameščanje:
https://dl.dropboxusercontent.com/u/32392228/numpy1.9.1_scipy0.14_win_amd64_py3.4.7z
https://dl.dropboxusercontent.com/u/32392228/numpy1.9.1_scipy0.14_win32_py3.4.7z
Python skripta se nahaja v source mapi repozitorija. Za zagon programa v ukazno vrstico vnesite:

>>>python bandit.py http://<ime_domene>/<št._primera>

Program bo po končanem izvajanju izpisal število uspešnih potegov.

c) Kot Python skripta z Anacondo
Anaconda je verzija Pythona, ki vsebuje potrebne dodatke za Python. Iz
http://continuum.io/downloads povlecite 3.4 verzijo za Windows, Linux ali Mac OS. Po potrebi
dodajte v PATH pot do Anaconda3/ in Anaconda3/Scripts direktorija. Program poženite z:

>>> python bandit.py http://<ime_domene>/<št._primera>
