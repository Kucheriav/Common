people = 1_000_000
zombie = 0
wave_n = 0
while zombie < people:
    wave = 3 ** wave_n
    zombie += wave
    wave_n += 1
print(wave_n)

time = 10 * wave_n
h = time // 60
m = time % 60
print(h, m)