import pygame
import time
from enum import Enum

class Kierunki(Enum):
	PRAWO = 1,
	LEWO = 2,
	GORA = 3,
	DOL = 4

# === ZMIENNE OGÓLNE ===
WIELKOSC_OKNA = (800, 600)
FPS = 2

# === ZMIENNE PLANSZY ===
bok = 30
szer = 20
wys = 15
kolor_planszy = (10,255,10)

# === ZMIENNE WĘŻA ===
xg = 3
yg = 3

kolor_glowy = (255,0,0)
kolor_segmentu = (230,50,50)

kierunek = Kierunki.PRAWO


pygame.init()
ekran = pygame.display.set_mode(WIELKOSC_OKNA)

def przesun():
	global xg, yg
	if kierunek == Kierunki.PRAWO:
		xg += 1
	if kierunek == Kierunki.LEWO:
		xg -= 1
	if kierunek == Kierunki.GORA:
		yg -= 1
	if kierunek == Kierunki.DOL:
		yg += 1

	rysujKwadrat(xg * bok, yg * bok, kolor_glowy)

def rysujKwadrat(x, y, kolor):
	pygame.draw.rect(ekran, kolor, (x, y, bok, bok))



while True:
	for event in pygame.event.get():
		# print(event)
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				kierunek = Kierunki.GORA
			if event.key == pygame.K_DOWN:
				kierunek = Kierunki.DOL
			if event.key == pygame.K_LEFT:
				kierunek = Kierunki.LEWO
			if event.key == pygame.K_RIGHT:
				kierunek = Kierunki.PRAWO
			
	ekran.fill(kolor_planszy)
	przesun()
	# rysujKwadrat(xg, yg, kolor_glowy)
	pygame.display.update()
	pygame.time.delay(100)
