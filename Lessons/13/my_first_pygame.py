# Import modułu pygame, dzięki któremu tworzymy aplikacje okienkowa
import pygame

from random import choice, randint

# Zmiana obecnej ścieżki pracy
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Inicjalizacja modułu
pygame.init()

# Utworzenie okna o określonych wymiarach
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

bonus_images = [
    "assets/bonus_1.png",
    "assets/bonus_2.png",
    "assets/bonus_3.png"
]

# Nadanie nazwy oknu
pygame.display.set_caption("Pierwsza Gra")

# Utworzenie zegara, który nadzoruje stałe wartości fps
clock = pygame.time.Clock()

# Zmienna określająca, czy należy zamknąć okno
game_status = True


def load_image(img_path: str, position):
    image = pygame.image.load(img_path)
    surface = image.convert()
    
    transpaernt_color = (0,0,0)
    surface.set_colorkey(transpaernt_color)

    rect = surface.get_rect(center=position)
    return [image, surface, rect]

def print_image(img_list) -> None:
    image, surface, rect = img_list
    screen_surface.blit(surface, rect)

def set_position_image(img_list, position):
    image, surface, rect = img_list
    rect = surface.get_rect(center=position)
    return [image, surface, rect]

def calculate_player_movement(keys):
    speed = 10
    delta_y = 0
    delta_x = 0

    if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
        speed *= 2

    if keys[pygame.K_w] or keys[pygame.K_UP]:
        delta_y -= speed
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        delta_y += speed

    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        delta_x -= speed
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        delta_x += speed

    return [delta_x, delta_y]

def limit_position(position):
    x, y = position

    x = max(0, min(x, SCREEN_WIDTH))
    y = max(0, min(y, SCREEN_HEIGHT))

    return [x, y]

def generate_bonus_object():
    image_name = choice(bonus_images)
    x = randint(0, SCREEN_WIDTH)
    y = randint(0, SCREEN_HEIGHT)
    position = [x, y]
    new_obj = load_image(image_name, position)
    bonus_objects.append(new_obj)

def print_bonus_objects():
    for obj in bonus_objects:
        print_image(obj)

def check_collisions():
    rect_player = player[2]

    for index in range(len(bonus_objects) - 1, -1, -1):
        obj = bonus_objects[index]
        rect = obj[2]
        if rect.colliderect(rect_player):
            bonus_objects.pop(index)

player_pos = [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2]
player = load_image("assets/player.png", player_pos)
background_color = [12, 45, 99]
bonus_objects = []
frames_cnt = 0


# Kod wykonywany póki aplikacja jest uruchomiona
while game_status:
    # Odczytanie zdarzeń zarejestrowanych przez komputer
    events = pygame.event.get()
    for event in events:
        # Naciśnięto X - zamykanie aplikacji
        if event.type == pygame.QUIT:
            game_status = False

    pressed_keys = pygame.key.get_pressed()
    delta_x, delta_y = calculate_player_movement(pressed_keys)

    player_pos[0] += delta_x
    player_pos[1] += delta_y

    player_pos = limit_position(player_pos)

    player = set_position_image(player, player_pos)

    screen_surface.fill(background_color)

    if frames_cnt % 60 == 0:
        generate_bonus_object()

    check_collisions()
    print_bonus_objects()

    # Wyświetl gracza
    print_image(player)

    # Odświeżenie wyświetlanego okna
    pygame.display.update()
    frames_cnt += 1
    clock.tick(60)

print("Zamykanie aplikacji")
# Zamknięcie aplikacji
pygame.quit()
# Zamknięcie skryptu
quit()
