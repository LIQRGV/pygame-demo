import pygame
from random import randrange

pygame.init()

pixel_unit = 36
n_tiles = 5
font_size = 15
top_pad = font_size * 2
screen = pygame.display.set_mode((pixel_unit * n_tiles, pixel_unit * n_tiles + top_pad))

circle_black = pygame.image.load("images/circle_black.png")
circle_white = pygame.image.load("images/circle_white.png")
tile = pygame.image.load("images/tile.png")

circle_black_pos = (0,0 + top_pad)
circle_white_pos = (pixel_unit * (n_tiles - 1), pixel_unit * (n_tiles - 1) + top_pad)
tile_array_pos = []
for i in range(0, n_tiles):
  for j in range(0, n_tiles):
    tile_array_pos.append((i * pixel_unit, j * pixel_unit + top_pad))

available_fonts = pygame.font.get_fonts()
random_index = randrange(len(available_fonts))
choosen_font = available_fonts[random_index]
font = pygame.font.SysFont(choosen_font, font_size)

done = False
playing_side = "black"
while not done:
  for position in tile_array_pos: # draw tile to next screen
    screen.blit(tile, position)

  screen.fill((0,0,255)) # add background to next screen

  playing_text = "{} turn".format(playing_side)
  screen.blit(font.render(playing_text, True, (255,255,255)), (0,0))

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      done = True
  screen.blit(circle_black, circle_black_pos) # draw black circle to next screen
  screen.blit(circle_white, circle_white_pos) # draw white circle to next screen
  # rendering things with flip
  pygame.display.flip()

