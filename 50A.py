# CodeForces task 50A
# Andrey Pompeev 20.06.2017 13:46

tile_size = 2
field_size = tuple(map(int, input().split(' ')))

result = (field_size[0] // tile_size) * field_size[1] if not (field_size[0] % tile_size) else (field_size[
                                                                                                   0] // tile_size) * \
                                                                                              field_size[1] + \
                                                                                              field_size[1] // tile_size
print(result)