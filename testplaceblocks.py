import random
from minecraft import Minecraft
mc = Minecraft.create()

def get_random_block():
    possible_blocks = ['STONE', 'DIRT', 'GRASS', 'SAND', 'GRAVEL']
    return random.choice(possible_blocks)

def place_blocks(x, y):
    width = 30
    height = 15
    
    for row in range(height):
        for column in range(width):
            mc.setBlock(x + column, y + row, 'AIR')
            mc.setBlock(x + column, y + row, get_random_block())
            
place_blocks(-100, 64) # Change x and z coordinates as desired
