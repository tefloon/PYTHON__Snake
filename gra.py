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


# === ZMIENNE WĘŻA === #
xp = 3
yp = 3

kolor_g = (255,0,0)
kolor_s = (230,50,50)

kobra = waz.Waz()


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


# === INICJALIZACJA === #
pygame.init()
ekran = pygame.display.set_mode(WIELKOSC_OKNA)


# === PĘTLA GŁÓWNA === #
while True:
	ekran.fill(KOLOR_PLANSZY)

	sprawdzWejscie()

	kobra.update(ekran)

	pygame.display.update()
	pygame.time.delay(100)
