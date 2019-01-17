import pygame
from random import randrange
from operator import add
from functools import reduce

pygame.init()

pixel_unit = 36
n_tiles = 5
font_size = 15
top_pad = font_size * 2
screen = pygame.display.set_mode((pixel_unit * n_tiles, pixel_unit * n_tiles + top_pad))

circle_black = pygame.image.load("images/circle_black.png")
circle_white = pygame.image.load("images/circle_white.png")
tile = pygame.image.load("images/tile.png")

pos_to_pix = lambda x: (x[0] * pixel_unit, x[1] * pixel_unit + top_pad)
is_valid_cell = lambda x: reduce(lambda accum, unit: accum and unit, map(lambda pos: 0 <= pos < 5, x))

circle_black_pos = (0,0)
circle_white_pos = (n_tiles - 1, n_tiles - 1)

circle_black_pix = pos_to_pix(circle_black_pos)
circle_white_pix = pos_to_pix(circle_white_pos)

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
  screen.fill((0,0,255)) # add background to next screen

  for position in tile_array_pos: # draw tile to next screen
    screen.blit(tile, position)

  playing_text = "{} turn".format(playing_side)
  screen.blit(font.render(playing_text, True, (255,255,255)), (0,0))

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      done = True
    elif event.type == pygame.KEYDOWN:
      pressed_key = pygame.key.get_pressed()
      reagent = None
      if pressed_key[pygame.K_UP]:
        reagent = (0, -1)
      elif pressed_key[pygame.K_DOWN]:
        reagent = (0, 1)
      elif pressed_key[pygame.K_LEFT]:
        reagent = (-1, 0)
      elif pressed_key[pygame.K_RIGHT]:
        reagent = (1, 0)
      else:
        continue

      if "black" == playing_side:
        new_circle_black_pos = tuple(map(add, circle_black_pos, reagent))
        if not is_valid_cell(new_circle_black_pos):
          print("Invalid move")
          break
        circle_black_pos = new_circle_black_pos
        circle_black_pix = pos_to_pix(circle_black_pos)
        playing_side = "white"
      else:
        new_circle_white_pos = tuple(map(add, circle_white_pos, reagent))
        if not is_valid_cell(new_circle_white_pos):
          print("Invalid move")
          break
        circle_white_pos = new_circle_white_pos
        circle_white_pix = pos_to_pix(circle_white_pos)
        playing_side = "black"

  screen.blit(circle_black, circle_black_pix) # draw black circle to next screen
  screen.blit(circle_white, circle_white_pix) # draw white circle to next screen
  # rendering things with flip
  pygame.display.flip()

pygame.quit()
