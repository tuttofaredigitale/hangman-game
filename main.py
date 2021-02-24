import random
from impiccato_disegno import d_impiccato, logo
from parole_impiccato import lista_parole

scelta_parola = random.choice(lista_parole)

print(logo)

game_over = False
energia = len(d_impiccato)-1

campo_gioco = []
for i in scelta_parola:
  campo_gioco += '_'

while not game_over:  

  indovina = input('Indovina la lettera: ')

  for posizione in range(len(scelta_parola)):
    lettera = scelta_parola[posizione]
    if lettera == indovina:
      campo_gioco[posizione] = lettera
  print(f"{' '.join(campo_gioco)}")  

  if indovina not in scelta_parola:
    print(f"Hai tentato con la lettera {indovina}, non è la lettera corretta. Hai perso una vita.")
    energia -= 1
    if energia == 0:
      game_over = True
      print(f"Hai perso! La parola corretta era {scelta_parola}")

  if not '_' in campo_gioco:
    game_over = True
    print('Complimenti hai vinto!') 

  print(d_impiccato[energia]) 
