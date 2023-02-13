import os

import pygame
import sys
from PIL import Image, ImageDraw
import random

all_sprites = pygame.sprite.Group()
enemys_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
pygame.init()
word = ''
ru = {}
W = 1200
H = 800
count = 0
enemys = []
hit = False
FPS = 25
clock = pygame.time.Clock()
score = 0
screen = pygame.display.set_mode((1200, 800))
lvl_1 = ('й', 'ц', 'у', 'к', 'е', 'н', 'г', 'ш', 'щ', 'з', 'х', 'ъ')
lvl_2 = ('й', 'ц', 'у', 'к', 'е', 'н', 'г', 'ш', 'щ', 'з', 'х', 'ъ',
         'ф', 'ы', 'в', 'а', 'п', 'р', 'о', 'л', 'д', 'ж', 'э')
lvl_3 = ('й', 'ц', 'у', 'к', 'е', 'н', 'г', 'ш', 'щ', 'з', 'х', 'ъ',
         'ф', 'ы', 'в', 'а', 'п', 'р', 'о', 'л', 'д', 'ж', 'э',
         'я', 'ч', 'с', 'м', 'и', 'т', 'ь', 'б', 'ю')
lvl_4 = ('дед', 'кук', 'цыц', 'как', 'кок', 'мим', 'тут', 'лол', 'поп', 'тот', 'кик')
lvl_5 = ('мама', 'папа', 'баба', 'дядя', 'нуну', 'тото', 'цаца', 'додо', 'хаха', 'чача')
lvl_6 = ('рак', 'пар', 'жар', 'жир', 'дом', 'жук', 'гот', 'жор', 'ход', 'мор', 'хор', 'тор')
lvl_7 = ('жижа', 'каша', 'маша', 'даша', 'ваша', 'наша', 'саша', 'тара', 'гора', 'чаща', 'фара')
lvl_8 = ('лодка', 'ходка', 'ветка', 'метка', 'корка', 'шашка', 'мурка', 'горка', 'чашка', 'кашка', 'будка')


def fill_ru():
    ru[pygame.K_q] = 'й'
    ru[pygame.K_w] = 'ц'
    ru[pygame.K_e] = 'у'
    ru[pygame.K_r] = 'к'
    ru[pygame.K_t] = 'е'
    ru[pygame.K_y] = 'н'
    ru[pygame.K_u] = 'г'
    ru[pygame.K_i] = 'ш'
    ru[pygame.K_o] = 'щ'
    ru[pygame.K_p] = 'з'
    ru[pygame.K_LEFTBRACKET] = 'х'
    ru[pygame.K_RIGHTBRACKET] = 'ъ'
    ru[pygame.K_a] = 'ф'
    ru[pygame.K_s] = 'ы'
    ru[pygame.K_d] = 'в'
    ru[pygame.K_f] = 'а'
    ru[pygame.K_g] = 'п'
    ru[pygame.K_h] = 'р'
    ru[pygame.K_j] = 'о'
    ru[pygame.K_k] = 'л'
    ru[pygame.K_l] = 'д'
    ru[pygame.K_SEMICOLON] = 'ж'
    ru[pygame.K_QUOTE] = 'э'
    ru[pygame.K_z] = 'я'
    ru[pygame.K_x] = 'ч'
    ru[pygame.K_c] = 'с'
    ru[pygame.K_v] = 'м'
    ru[pygame.K_b] = 'и'
    ru[pygame.K_n] = 'т'
    ru[pygame.K_m] = 'ь'
    ru[pygame.K_COMMA] = 'б'
    ru[pygame.K_PERIOD] = 'ю'
    ru[pygame.K_BACKQUOTE] = 'ё'


def gener(width, height, color, file):
    img = Image.new(mode="RGB", size=(width, height))
    img.putalpha(0)
    draw = ImageDraw.Draw(img)
    if color == 'green':
        draw.ellipse((0, 0, width, height), fill=(0, 255, 0))
    elif color == 'red':
        draw.ellipse((0, 0, width, height), fill=(255, 0, 0))
    else:
        draw.ellipse((0, 0, width, height), fill=(255, 255, 0))
    img.save(f'Sprites/{file}.png')


class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y, gr, *group):
        super().__init__(*group)
        if gr == 'pl':
            self.image = pygame.image.load("Sprites/1.png")
        else:
            self.image = pygame.image.load("Sprites/3.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


def get_random_coords():
    bord = random.randint(1, 4)
    if bord == 1:
        return random.randint(0, W - 50), 70
    elif bord == 2:
        return W - 50, random.randint(0, H - 50)
    elif bord == 3:
        return random.randint(0, W - 50), H - 50
    else:
        return 50, random.randint(0, H - 50)


class Unit(Ball):
    def __init__(self, x, y, gr, word, *group):
        super().__init__(x, y, gr, *group)
        centr_x = x + 45
        centr_y = y + 45
        self.step = 1200
        self.Vx = (W / 2 - centr_x) / self.step
        self.Vy = (H / 2 - centr_y) / self.step
        self.x = x
        self.y = y
        self.f1 = pygame.font.Font(None, 24)
        self.word = word
        self.text1 = self.f1.render(self.word, True, (180, 0, 0))
        self.Tx = 55
        self.Ty = 25

    def move(self, is_first=False):
        self.x += self.Vx
        self.y += self.Vy
        self.rect.x = int(self.x)
        self.rect.y = int(self.y)
        self.Tx = int(self.x) + 5
        self.Ty = int(self.y) - 20
        if is_first:
            self.text1 = self.f1.render(self.word, True, (180, 0, 0))
        else:
            self.text1 = self.f1.render(self.word, True, (180, 180, 0))
        screen.blit(self.text1, (self.Tx, self.Ty))

    def update_color(self):
        self.image = pygame.image.load("Sprites/2.png")
        self.rect = self.image.get_rect()





def terminate():
    pygame.quit()
    sys.exit()


def start_screen():
    intro_text = ['Название проекта', "",
                  "Правила игры:",
                  "Введите надпись или букву над шариком красного цвета",
                  "Нажмите Enter",
                  "По мере прохождения, разнообразие надписей и букв будет увеличиваться",
                  "Если вы ввели правильную комбинацию, шарик пропадёт и следующая цель станет красной",
                  "Если же вы ввели не правильную комбинацию, нажмите Enter и продолжайте вводить заново",
                  "!Обязательно нужно вклюить английскую раскладку, но печатать русскими буквами!"
                  ]

    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, True, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return
        pygame.display.flip()
        clock.tick(FPS)


def get_enemy():
    x, y = get_random_coords()
    if count == 500:
        enemy = Unit(x, y, 'en', random.choice(lvl_2), all_sprites)
    elif count == 1000:
        enemy = Unit(x, y, 'en', random.choice(lvl_3), all_sprites)
    elif count == 2000:
        enemy = Unit(x, y, 'en', random.choice(lvl_4), all_sprites)
    elif count == 3000:
        enemy = Unit(x, y, 'en', random.choice(lvl_5), all_sprites)
    elif count == 5000:
        enemy = Unit(x, y, 'en', random.choice(lvl_6), all_sprites)
    elif count == 7000:
        enemy = Unit(x, y, 'en', random.choice(lvl_7), all_sprites)
    elif count == 10000:
        enemy = Unit(x, y, 'en', random.choice(lvl_8), all_sprites)
    else:
        enemy = Unit(x, y, 'en', random.choice(lvl_1), all_sprites)
    return enemy


if len(os.listdir('Sprites')) != 3:
    gener(100, 100, 'green', 1)
    gener(50, 50, 'red', 2)
    gener(50, 50, 'yellow', 3)
player = Ball(550, 350, 'pl', all_sprites)
player_group.add(player)
fill_ru()
print(ru)
screen.fill('Black')
start_screen()
f1 = pygame.font.SysFont('san-serif', 48)
while not hit:
    text1 = f1.render(f"{score}", False, (0, 180, 0))
    screen.blit(text1, (10, 50))
    pygame.time.delay(40)
    count += 1
    if count % 20 == 0:
        enemy = get_enemy()
        enemys.append(enemy)
        enemys_group.add(enemy)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if enemys:
            if event.type == pygame.KEYDOWN:
                if event.key in ru:
                    word += ru[event.key]
                    print(word)
                    print(enemys[0].word)
                if event.key == pygame.K_RETURN:
                    if enemys[0].word == word:
                        enemys[0].kill()
                        enemys.remove(enemys[0])
                        enemys[0].update_color()
                    word = ''
                    score += 1
    screen.fill((0, 0, 0))
    all_sprites.draw(screen)
    if len(enemys):
        for i in enemys:
            if i == enemys[0]:
                i.move(True)
            else:
                i.move()
        if enemys[0].rect.right > player.rect.left and \
                enemys[0].rect.left < player.rect.right and \
                enemys[0].rect.bottom > player.rect.top and \
                enemys[0].rect.top < player.rect.bottom:
            hit = True
    pygame.display.flip()
for i in enemys:
    i.Vx, i.Vy = 0, 0
    i.kill()
while True:
    f1 = pygame.font.Font(None, 24)
    text1 = f1.render('Вы проиграли', True,
                      (180, 0, 0))
    screen.fill('Black')
    screen.blit(text1, (10, 50))