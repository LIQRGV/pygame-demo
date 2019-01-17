import pygame

pixel_unit = 36
n_tiles = 5
screen = pygame.display.set_mode((pixel_unit * n_tiles, pixel_unit * n_tiles))

done = False
while not done:
  for event in pygame.event.get():
    print(event)
