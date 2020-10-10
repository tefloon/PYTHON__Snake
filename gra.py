import pygame
import time
import waz
import random


# === ZMIENNE OGÓLNE === #
BOK = 30
KOLUMNY = 12
RZEDY = 20

WIELKOSC_OKNA = (BOK*KOLUMNY, BOK*RZEDY)
KOLOR_PLANSZY = (10,255,10)

punkty = 0


# === ZMIENNE WĘŻA === #
xp = 3
yp = 3
dl = 55

kolor_g = (255, 0, 0)
kolor_s = (245, 123, 6)

kobra = waz.Waz(xp, yp, BOK, dl, kolor_g, kolor_s)

# === ZMIENNE JAPKA === #
xj = random.randint(0, KOLUMNY - 1)
yj = random.randint(0, RZEDY - 1)

kolor_j = (255, 0, 0)

japko = waz.Segment(xj, yj, BOK, kolor_j)


# === FUNKCJE === #
def sprawdzWejscie():
	for event in pygame.event.get():
		# print(event)
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				kobra.k = waz.Kierunek.GORA

			if event.key == pygame.K_DOWN:
				kobra.k = waz.Kierunek.DOL

			if event.key == pygame.K_LEFT:
				kobra.k = waz.Kierunek.LEWO

			if event.key == pygame.K_RIGHT:
				kobra.k = waz.Kierunek.PRAWO

def noweJapko():
	czyDobrze = False

	while not czyDobrze > 0:
		czyDobrze = True

		xj = random.randint(0, KOLUMNY - 1)
		yj = random.randint(0, RZEDY - 1)

		for s in kobra.segmenty:
			if s.x == xj and s.y == yj:
				czyDobrze = False
				break
	
	japko.przesun(xj, yj)

def sprawdzKolizje():
	if kobra.segmenty[0] == japko:
		noweJapko()
		kobra.przedluz()


# === INICJALIZACJA === #
pygame.init()
ekran = pygame.display.set_mode(WIELKOSC_OKNA)


# === PĘTLA GŁÓWNA === #
while True:
	ekran.fill(KOLOR_PLANSZY)

	sprawdzWejscie()

	kobra.update(ekran)
	japko.rysuj(ekran)

	sprawdzKolizje()

	pygame.display.update()
	pygame.time.delay(100)
