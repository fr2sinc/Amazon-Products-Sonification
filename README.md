# Amazon-products-sonification
Amazon-products-sonification è un applicativo client-server, che permette all'utente di sonificare lo sconto di un qualsiasi prodotto scelto da lui venduto dallo store online amazon.it .

# Utilizzo
L'utente lancia l'applicativo, passando come argomento l'url del prodotto che intende sonificare.
In base alla percentuale di sconto del prodotto, calcolata a partire dal prezzo di vendita e prezzo di listino, verrà generato un suono.
Più è alto lo sconto più il suono sarà acuto e con lfo rate maggiore.
In questo modo, l'utente inserendo prima un prodotto e poi un altro, ascoltando il suono ottenuto ad ogni step, sarà in grado di confrontarli e capire quale dei due ha attualmente uno sconto maggiore.



# Configurazione ed esecuzione

## 1) Requisiti
1. Installare pure data
2. Installare python-3 e pip
3. Recarsi nella cartella dove sono contenuti i sorgenti
4. Aggiungere le librerie esterne richieste, che si trovano in requirements.txt
5. In modo semplificato: `pip install -r requirements.txt`


## 2) Esecuzione
1. Lanciare `server.pd` ed attivare il DSP
2. Eseguire: `python client.py -u "LINK DI UN PRODOTTO AMAZON.it"`
3. E' fondamentale inserire il link del prodotto tra doppi apici perchè alcuni link complessi potrebbero dare problemi di escape
4. Verrà generato un suono
5. Rieseguire lo step 2 per ottenere un nuovo suono e confrontarlo con il precedente
2. Eseguire: `python client.py -h` per avere info su come inserire Ip e porta del server senza utilizzare quelle di default

# Author
### Francesco Raitano
### Matricola: s259760
