#### Tic Tac Toe programmieren
#### Grafik aufbauen fuer Tic Tac Toe
#
#
# Divide and conquer
# Teile und herrsche
#
#
#
## benoetigte Module importieren

import turtle
import random

#Aufgabe 1 - Turtle verstecken und den Speed auf 100 setzen

# Init function fuer Initialisierung der Turtle Grafik
def init():
  turtle.hideturtle()
  turtle.speed(100)
  turtle.pensize(4)
  turtle.penup()
  

# Function fuer zeichnen der Linien
def zeichnen(xstart,ystart,richtung):
  if richtung=="h":
    offsetx=300
    offsety=0
  if richtung=="v":
    offsetx=0
    offsety=300  
  turtle.goto(xstart,ystart)
  turtle.pendown()
  turtle.goto(xstart+offsetx,ystart+offsety)
  turtle.penup()


# Aufgabe 2
# Function fuer das Zeichnen eines Kreises
# Kreis soll blau gefuellt sein
# Radius 20, Mittelpunkt in 0,0

def zeichne_kreis(xstart,ystart):
  turtle.penup()
  turtle.color("blue")
  turtle.begin_fill()
  turtle.goto(xstart,ystart-20)
  turtle.pendown()
  turtle.circle(20)
  turtle.end_fill()
  turtle.penup()
  return
  

# Aufgabe 3
# Function fuer Zeichnen eines Kreuzes
# Kreuz in rot
# jeweils 20 Pixeleinheiten nach links/oben, rechts/oben

def zeichne_x(xstart,ystart):
  turtle.penup()
  turtle.color("red")
  turtle.goto(xstart-20,ystart-20)
  turtle.pendown()
  turtle.goto(xstart+20,ystart+20)
  turtle.penup()
  turtle.goto(xstart+20, ystart-20)
  turtle.pendown()
  turtle.goto(xstart-20,ystart+20)
  turtle.penup()
  return

# Aufgabe 4
# Function um in die Felder die Zahlen 1-9 zu schreiben
# immer rechts ins eck
# mit FOnt size 24
# mit Farbe schwarz

def zeichne_felder():
  turtle.penup()
  turtle.color("black")

  turtle.goto(-70,60)
  turtle.pendown()
  turtle.write("1", font=("Arial",24))
  turtle.penup()

  turtle.goto(30,60)
  turtle.pendown()
  turtle.write("2", font=("Arial",24))
  turtle.penup()

  turtle.goto(130,60)
  turtle.pendown()
  turtle.write("3", font=("Arial",24))
  turtle.penup()

  turtle.goto(-70,-40)
  turtle.pendown()
  turtle.write("4", font=("Arial",24))
  turtle.penup()

  turtle.goto(30,-40)
  turtle.pendown()
  turtle.write("5", font=("Arial",24))
  turtle.penup()

  turtle.goto(130,-40)
  turtle.pendown()
  turtle.write("6", font=("Arial",24))
  turtle.penup()

  turtle.goto(-70,-140)
  turtle.pendown()
  turtle.write("7", font=("Arial",24))
  turtle.penup()

  turtle.goto(30,-140)
  turtle.pendown()
  turtle.write("8", font=("Arial",24))
  turtle.penup()

  turtle.goto(130,-140)
  turtle.pendown()
  turtle.write("9", font=("Arial",24))
  turtle.penup()

  return



# Aufgabe 5
# Function um einen Move zu machen
# spieler, "spieler1" Kreis oder "spieler2" kreuz
# feld 1 bis 9

def spielzug(spieler, feld):
  if feld==1:
    xpos=-100
    ypos=100
  if feld==2:
    xpos=0
    ypos=100
  if feld==3:
    xpos=100
    ypos=100
  if feld==4:
    xpos=-100
    ypos=0
  if feld==5:
    xpos=0
    ypos=0
  if feld==6:
    xpos=100
    ypos=0
  if feld==7:
    xpos=-100
    ypos=-100
  if feld==8:
    xpos=0
    ypos=-100
  if feld==9:
    xpos=100
    ypos=-100
  if spieler=="spieler1":
    zeichne_kreis(xpos,ypos)
  if spieler=="spieler2":
    zeichne_x(xpos,ypos)

  return

# Aufgabe 6
# Titel Tic-Tac-Toe

def titel():
  turtle.penup()
  turtle.color("black")
  turtle.goto(0,200)
  turtle.write("TIC TAC TOE", align="center", font=("Arial",30))
  turtle.down()

def freies_feld(feld):
    if feld_belegung[feld-1]==0:
        return True
    else:
        return False

    
    
########################################
# Start des Hauptprogramms

def zug_sieg(player):
  #erste Horizontale
  if player=="spieler1" and (feld_belegung[0]+feld_belegung[1]+feld_belegung[2])==3:
    return True
  
  #zweit Horizontale
  if player=="spieler1" and (feld_belegung[3]+feld_belegung[4]+feld_belegung[5])==3:
    return True
  
  #drite Horizontale
  if player=="spieler1" and (feld_belegung[6]+feld_belegung[7]+feld_belegung[8])==3:
    return True
  
  #erste vertikale
  if player=="spieler1" and (feld_belegung[0]+feld_belegung[3]+feld_belegung[6])==3:
    return True
  
  #zweite vertikale
  if player=="spieler1" and (feld_belegung[2]+feld_belegung[4]+feld_belegung[6])==3:
    return True
  #dritte vertikale
  if player=="spieler1" and (feld_belegung[3]+feld_belegung[5]+feld_belegung[8])==3:
    return True
  #erste diagonale
  if player=="spieler1" and (feld_belegung[0]+feld_belegung[4]+feld_belegung[8])==3:
    return True
  #zweite digonale
  if player=="spieler1" and (feld_belegung[2]+feld_belegung[4]+feld_belegung[6])==3:
    return True
  #drite diagonale
  if player=="spieler1" and (feld_belegung[3]+feld_belegung[4]+feld_belegung[6])==3:
    return True
#zweiter spieler

  #erste Horizontale
  if player=="spieler2" and (feld_belegung[0]+feld_belegung[1]+feld_belegung[2])==-3:
    return True
  
  #zweit Horizontale
  if player=="spieler2" and (feld_belegung[3]+feld_belegung[4]+feld_belegung[5])==-3:
    return True
  
  #drite Horizontale
  if player=="spieler2" and (feld_belegung[6]+feld_belegung[7]+feld_belegung[8])==-3:
    return True
  
  #erste vertikale
  if player=="spieler2" and (feld_belegung[0]+feld_belegung[3]+feld_belegung[6])==-3:
    return True
  
  #zweite vertikale
  if player=="spieler2" and (feld_belegung[2]+feld_belegung[4]+feld_belegung[6])==-3:
    return True
  #dritte vertikale
  if player=="spieler2" and (feld_belegung[3]+feld_belegung[5]+feld_belegung[8])==-3:
    return True
  #erste diagonale
  if player=="spieler2" and (feld_belegung[0]+feld_belegung[4]+feld_belegung[8])==-3:
    return True
  #zweite digonale
  if player=="spieler2" and (feld_belegung[2]+feld_belegung[4]+feld_belegung[6])==-3:
    return True
  #drite diagonale
  if player=="spieler2" and (feld_belegung[3]+feld_belegung[4]+feld_belegung[6])==-3:
    return True
### Initialisieren der Turtle
init()

### Zeichne das Spielfeld
zeichnen(-150,-150,"h")
zeichnen(-150,-50,"h")
zeichnen(-150,50,"h")
zeichnen(-150,150,"h")
## vertikalen
zeichnen(-150,-150,"v")
zeichnen(-50,-150,"v")
zeichnen(50,-150,"v")
zeichnen(150,-150,"v")


### Testen dewr Kreis und x Funktion

#zeichne_kreis(0,0)
#zeichne_x(0,0)
zeichne_felder()
titel()
#spielzug("spieler1",1)
#spielzug("spieler2",9)
#spielzug("spieler2",4)
feld_belegung=[0,0,0,0,0,0,0,0,0,]
i=0
gewonnen=0



while gewonnen == 0:
  

    valid=0
   
    while valid==0 and gewonnen == 0:

        a=int(input("Spieler1, mache deinen Zug:"))
        if freies_feld(a):
          i=i+1
          spielzug("spieler1",a)
          feld_belegung[a-1]=1
          if zug_sieg("spieler1"):
            print("spieler1 du hast gewonnen")  
            gewonnen=1
        valid=1

    if i==9:
      break


    valid=0
    while valid==0 and gewonnen == 0:
        b=int(input("Spieler2, mache deinen Zug:"))
        
        if freies_feld(b):
          spielzug("spieler2",b)
          
          i=i+1
          feld_belegung[b-1]=-1      
          valid=1
          if zug_sieg("spieler2"):
            print("spieler2 du hast gewonnen")
            gewonnen=1








print(feld_belegung)













