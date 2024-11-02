# Write a program that, given the number of available blocks, 
# calculates the number of blocks left over after building the 
# tallest possible valid structure.


# Problem

# Input will be an integer representing number of blocks available for building.
# Output will be an integer representing number of blocks left over at the end.

# Explicit rules:
# 1. The building blocks are cubes.
# 2. The structure is built in layers.
# 3. The top layer is a single block.
# 4. A block in an upper layer must be supported by four blocks in a lower layer.
# 5. A block in a lower layer can support more than one block in an upper layer.
# 6. You cannot leave gaps between blocks.

# Implicit Rules:
# 1. 2nd layer from top is 4 blocks (implicitly), 
# since 4 blocks must be used to support top layer. (2x2)
# 2. The 3rd layer down would best be made with a middle block giving some support to
# all 4 of the above blocks, and blocks surrounding that one, totalling 9 blocks. (3x3)
# 3. It looks like each layer will be a square number, the square of the layer count,
# starting from the top and working downward. 4x4, 5x5, and so on.

# Clarifying Questions:
# Honestly, the problem seems pretty clear.
# Is it necessary to output anything other than the remaining blocks?
# Such as number of layers in the structure, or blocks used.

# To respond to the questions posed in this section of the Step 1 discussion:
# 1. A lower layer cannot reasonably have more blocks than it needs, as this
# would violate some of the explicit rules, including the directive to
# build the TALLEST POSSIBLE structure, and possibly creating gaps between blocks.
# 2. No, sometimes remaining blocks will equal zero. For example, given 14 blocks,
# a block is th top layer, 4 are the second layer, and 9 are the third layer, 
# with none left over.


# Examples and Test Cases
# All of the provided test cases are consistent with my understanding of the problem. 
# I have copied them to the end of the code.


# Data Structures
# Possibly it might be worthwhile to use a series of lists to represent the
# layers of the structure. But I think this could be done more simply by having a loop
# that generates layers and then compares the total used against the total avaiable.

# Algorithm
# get available blocks as a parameter
# layer_num = 1
# blocks_used = 0
# While blocks_available > blocks_used:
# layer_blocks = layer_num * layer_num
# if blocks_available > (blocks_used + layer_blocks):
# blocks_available -= layer_blocks
# blocks_used += layer_blocks
# layer_num += 1
# else break
# return blocks_available


# Code

def calculate_leftover_blocks(blocks_available):
    layer_num = 1
    blocks_used = 0

    while blocks_available > 0:
        layer_blocks = layer_num**2

        if blocks_available >= layer_blocks:
            blocks_available -= layer_blocks
            blocks_used += layer_blocks
            layer_num += 1
        else:
            break

    return blocks_available

print(calculate_leftover_blocks(0) == 0)  # True
print(calculate_leftover_blocks(1) == 0)  # True
print(calculate_leftover_blocks(2) == 1)  # True
print(calculate_leftover_blocks(4) == 3)  # True
print(calculate_leftover_blocks(5) == 0)  # True
print(calculate_leftover_blocks(6) == 1)  # True
print(calculate_leftover_blocks(14) == 0) # True
print(calculate_leftover_blocks(55))
print(calculate_leftover_blocks(1000000))