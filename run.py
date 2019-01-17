import pygame

pixel_unit = 36
n_tiles = 5
screen = pygame.display.set_mode((pixel_unit * n_tiles, pixel_unit * n_tiles))

circle_black = pygame.image.load("images/circle_black.png")
circle_white = pygame.image.load("images/circle_white.png")
tile = pygame.image.load("images/tile.png")

circle_black_pos = (0,0)
circle_white_pos = (pixel_unit * (n_tiles - 1), pixel_unit * (n_tiles - 1))
tile_array_pos = []
for i in range(0, n_tiles):
  for j in range(0, n_tiles):
    tile_array_pos.append((i * pixel_unit, j * pixel_unit))

screen.fill((255,255,255))
for position in tile_array_pos:
  screen.blit(tile, position)
screen.blit(circle_black, circle_black_pos)
screen.blit(circle_white, circle_white_pos)
# rendering things with flip
pygame.display.flip()
