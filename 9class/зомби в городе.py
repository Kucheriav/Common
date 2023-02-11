people = 100_0000
zombie = 0
wave_n = 0
while zombie < people:
    wave = 3 ** wave_n
    zombie += wave
    wave_n += 1



