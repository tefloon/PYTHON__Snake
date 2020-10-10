import pygame
from enum import Enum


class Kierunek(Enum):
	PRAWO = 1,
	LEWO = 2,
	GORA = 3,
	DOL = 4


class Waz(object):
	"""docstring for Waz"""
	def __init__(self, xp=3, yp=3, bok=30, dl=3, kg=(255,0,0), ks=(245, 123, 6), k=Kierunek.PRAWO):
		self.bok = bok
		self.dl = dl
		self.kg = kg
		self.ks = ks
		self.k = k

		self.segmenty = []

		self.segmenty.append(Segment(xp, yp, bok, kg))

		for i in range(1,dl):
			self.segmenty.append(Segment(xp, yp+i, bok, ks))
		
	def rysuj(self, ekran):
		for s in self.segmenty:
			s.rysuj(ekran)

	def przesun(self):
		for i in range(len(self.segmenty) - 1, 0, -1):
			self.segmenty[i].x = self.segmenty[i-1].x
			self.segmenty[i].y = self.segmenty[i-1].y

		if self.k==Kierunek.PRAWO:
			self.segmenty[0].x += 1
		elif self.k==Kierunek.LEWO:
			self.segmenty[0].x -= 1
		elif self.k==Kierunek.GORA:
			self.segmenty[0].y -= 1
		elif self.k==Kierunek.DOL:
			self.segmenty[0].y += 1

	def update(self, ekran):
		self.przesun()
		self.rysuj(ekran)



class Segment():
	"""Klasa opisująca pojedynczy segment węża"""
	def __init__(self, x=3, y=3, bok=30, kolor=(245, 123, 6)):
		self.x = x
		self.y = y
		self.bok = bok
		self.kolor = kolor

	def przesun(self, x_nowy, y_nowy):
		self.x = x_nowy
		self.y = y_nowy

	def rysuj(self, ekran):
		g = 2

		pygame.draw.rect(ekran,  (0,0,0),   (self.x * self.bok, self.y * self.bok, self.bok, self.bok))	
		pygame.draw.rect(ekran, self.kolor, (self.x * self.bok + g, self.y * self.bok + g, self.bok - 2*g, self.bok - 2*g))	
		


