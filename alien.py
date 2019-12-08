import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	"""Uma classe que representa um único alienígena da frota."""
	def __init__(self, ai_settings, screen):
		"""Inicializa o alienígena e define sua posição inicial"""
		super(Alien, self).__init__()
		self.screen = screen
		self.ai_settings = ai_settings
