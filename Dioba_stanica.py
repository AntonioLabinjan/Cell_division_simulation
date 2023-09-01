# SIMULACIJA DIOBE STANICA
import matplotlib.pyplot as plt
import random
import time

# Početni broj stanica
broj_stanica = 1

# Vrijeme simulacije u sekundama
vrijeme_simulacije = 60

# Vremenski koraci (svaku sekundu)
koraci = list(range(vrijeme_simulacije))

# Lista za praćenje broja stanica u svakom vremenskom koraku
stanice_u_vremenu = []

# Simulacija diobe stanica
for korak in koraci:
    # Generirajte slučajan broj stanica koje se dijele ili umiru
    nova_stanica = random.randint(0, 2)  # Može biti 0, 1 ili 2

    # Dodajte novu stanicu u popis
    broj_stanica += nova_stanica

    # Dodajte trenutni broj stanica u listu za praćenje
    stanice_u_vremenu.append(broj_stanica)

    # Ispis informacija o diobi stanica
    print(f'Vrijeme: {korak} sekundi, Broj stanica: {broj_stanica}')

    # Pauzirajte simulaciju na trenutak kako biste mogli pratiti izlaz
    time.sleep(1)

# Vizualizacija broja stanica tijekom vremena
plt.plot(koraci, stanice_u_vremenu)
plt.xlabel('Vrijeme (sekunde)')
plt.ylabel('Broj stanica')
plt.title('Simulacija diobe stanica')
plt.show()
