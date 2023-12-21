import random

paikat = 28

pelaajat = {
   "Lauri": {"paikkaLaudalla": 0, "pisteet": 0, "lupaLiikkua": False, "maalit": 0},
   "Tolone": {"paikkaLaudalla": 0, "pisteet": 0, "lupaLiikkua": False, "maalit": 0},
   "Salmu": {"paikkaLaudalla": 0, "pisteet": 0, "lupaLiikkua": False, "maalit": 0},
   "Purane": {"paikkaLaudalla": 0, "pisteet": 0, "lupaLiikkua": False, "maalit": 0}
}

def heita_noppaa():
    tulos = random.randint(1,6)
    return tulos

def siirra_nappulaa_pelaaja(nimi, heitto):
   pelaaja = pelaajat[nimi]
   if not pelaaja["lupaLiikkua"]:
      if heitto == 6:
         pelaaja["lupaLiikkua"] = True
         pelaaja["paikkaLaudalla"] = 1
         pelaaja["pisteet"] = 1
      else:
        print(f"Sait luvun {heitto}, joten et saa liikkua")   
   else:
      pelaaja["pisteet"] += heitto
      pelaaja["paikkaLaudalla"] += heitto
      if pelaaja["pisteet"] >= paikat:
         pelaaja["maalit"] += 1
         pelaaja["pisteet"] = 0
         pelaaja["paikkaLaudalla"] = 0
         pelaaja["lupaLiikkua"] = False
         print(f"Sait nappulan maaliin!")   

   return False     

def siirra_nappulaa_tietokone(nimi, heitto):
    pelaaja = pelaajat[nimi]
    if not pelaaja["lupaLiikkua"]:
      if heitto == 6:
         pelaaja["lupaLiikkua"] = True
         pelaaja["pisteet"] = 1
         if nimi == "Tolone":
            pelaaja["paikkaLaudalla"] = 8
         if nimi == "Salmu":
            pelaaja["paikkaLaudalla"] = 15
         if nimi == "Purane":
            pelaaja["paikkaLaudalla"] = 22      
         print(f"Pelaaja {nimi} sai kuutosen, ja lähtee liikkeelle")
      else:
        print(f"{nimi} ei pääse liikkeelle")    
    else:
      pelaaja["pisteet"] += heitto
      pelaaja["paikkaLaudalla"] += heitto
      if pelaaja["paikkaLaudalla"] > 28:
         pelaaja["paikkaLaudalla"] = pelaaja["paikkaLaudalla"] - 28
      if pelaaja["pisteet"] >= paikat:
         pelaaja["maalit"] += 1
         pelaaja["pisteet"] = 0
         pelaaja["lupaLiikkua"] = False
         pelaaja["paikkaLaudalla"] = 0
         print(f"{nimi} sai nappulan maaliin!")   

    return False

def pelin_tilanne(pelaajan_nimi):
   pelaaja = pelaajat[pelaajan_nimi]
   print(f"Pelaajan {pelaajan_nimi} maalit:", pelaaja["maalit"], " JA pisteet:", pelaaja["pisteet"], " JA paikka laudalla:", pelaaja["paikkaLaudalla"])

def syo_nappula(pelaajan_nimi, paikka):
   for nimi, tiedot in pelaajat.items():
      if nimi != pelaajan_nimi and tiedot["paikkaLaudalla"] == paikka and tiedot["paikkaLaudalla"] != 0:
         if pelaajan_nimi == "Lauri":
            input(f"Syö pelaajan {nimi} nappula painamalla enteriä")
         tiedot["pisteet"] = 0
         tiedot["paikkaLaudalla"] = 0
         tiedot["lupaLiikkua"] = False
         print(f"Söit pelaajan {nimi} nappulan")   

def tallenna_peli():
   with open("pelin_tilanne.txt", "w") as file:
      for nimi, tiedot in pelaajat.items():
         file.write(f"{nimi}: {tiedot}\n")

def lataa_peli():
    try:
        with open("pelin_tilanne.txt", "r") as file:
            for rivi in file:
                nimi, tiedot_str = rivi.strip().split(": ", 1)
                tiedot = eval(tiedot_str) 
                pelaajat[nimi] = tiedot
    except FileNotFoundError:
        print("Ei aiempaa peliä, aloitetaan uusi peli.")                    

peli_jatkuu = True
winner = ""

lataus = input("Lataa aiempi peli painamalla X: ")
if lataus == "X":
   lataa_peli()

while True:
   if not peli_jatkuu:
      print(f"PELAAJA {winner} VOITTI PELIN!!!")
      break

   for pelaaja in pelaajat:
      if pelaaja == "Lauri":
        input(f"Heitä noppaa {pelaaja} painamalla Enter")
        heitto = heita_noppaa()
        siirra_nappulaa_pelaaja(pelaaja, heitto)
        print(f"Heitit numeron {heitto}")
        paikka = pelaajat[pelaaja]["paikkaLaudalla"]
        syo_nappula(pelaaja, paikka)
        if heitto == 6:
          print(f"{pelaaja} voit heittää uudestaan")
          heitto2 = heita_noppaa()
          print(f"Heitit numeron {heitto2}")
          siirra_nappulaa_pelaaja(pelaaja, heitto2)
          paikka = pelaajat[pelaaja]["paikkaLaudalla"]
          syo_nappula(pelaaja, paikka)
          if heitto2 == 6:
            print(f"{pelaaja} voit heittää uudestaan")
            heitto3 = heita_noppaa()
            print(f"Heitit numeron {heitto3}")
            siirra_nappulaa_pelaaja(pelaaja, heitto3)
            paikka = pelaajat[pelaaja]["paikkaLaudalla"]
            syo_nappula(pelaaja, paikka)

      else:
        print(f"{pelaaja} heittää")
        heitto = heita_noppaa()
        print(f"{pelaaja} heitti numeron {heitto}")
        siirra_nappulaa_tietokone(pelaaja, heitto)
        paikka = pelaajat[pelaaja]["paikkaLaudalla"]
        syo_nappula(pelaaja, paikka)
        if heitto == 6:
          print(f"{pelaaja} heittää uudestaan")
          heitto2 = heita_noppaa()
          print(f"{pelaaja} heitti numeron {heitto2}")
          siirra_nappulaa_tietokone(pelaaja, heitto2)
          paikka = pelaajat[pelaaja]["paikkaLaudalla"]
          syo_nappula(pelaaja, paikka)
          if heitto2 == 6:
            print(f"{pelaaja} heittää uudestaan")
            heitto3 = heita_noppaa()
            print(f"{pelaaja} heitti numeron {heitto3}")
            siirra_nappulaa_tietokone(pelaaja, heitto3)
            paikka = pelaajat[pelaaja]["paikkaLaudalla"]
            syo_nappula(pelaaja, paikka)

      input("Paina Enteriä antaaksesi vuoron seuraavalle") 

   print("KIERROS OHI")
   print("Tämän hetkinen tilanne alla:")

   for pelaaja in pelaajat:
      pelin_tilanne(pelaaja)
      voittaja = pelaajat[pelaaja]
      if voittaja["maalit"] == 4:
         winner += pelaaja
         peli_jatkuu = False

   tallennus = input("Paina X, jos haluat tallentaa pelin, ja jatkaa myöhemmin ")      
   if tallennus == "X":
      tallenna_peli()
      break
         
print("PELI ON OHI!!!")         
    
      