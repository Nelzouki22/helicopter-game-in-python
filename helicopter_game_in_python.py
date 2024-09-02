import pygame
import sys

# إعدادات اللعبة
WIDTH, HEIGHT = 800, 600
BACKGROUND_COLOR = (135, 206, 250)  # اللون السماوي

# إعدادات الهليكوبتر
HELICOPTER_BODY_COLOR = (0, 100, 255)  # لون جسم الهليكوبتر
HELICOPTER_ROTOR_COLOR = (0, 0, 0)     # لون الشفرات
HELICOPTER_WIDTH, HELICOPTER_HEIGHT = 100, 60
ROTOR_WIDTH = 10
ROTOR_LENGTH = 70
PERSON_COLOR = (255, 220, 185)         # لون الشخص (بشرة فاتحة)

# إعدادات الصواريخ
MISSILE_COLOR = (255, 0, 0)            # لون الصواريخ
MISSILE_WIDTH, MISSILE_HEIGHT = 10, 30
MISSILE_SPEED = 10

# إعدادات الرشاشات
GUN_COLOR = (0, 255, 0)                # لون الرشاشات
GUN_WIDTH, GUN_HEIGHT = 5, 15
GUN_SPEED = 15

# قائمة الصواريخ والرشاشات
missiles = []
guns = []

# دالة لرسم الهليكوبتر
def draw_helicopter(screen, x, y):
    pygame.draw.rect(screen, HELICOPTER_BODY_COLOR, (x, y, HELICOPTER_WIDTH, HELICOPTER_HEIGHT))
    pygame.draw.line(screen, HELICOPTER_ROTOR_COLOR, (x + HELICOPTER_WIDTH // 2 - 20, y - ROTOR_LENGTH // 2), (x + HELICOPTER_WIDTH // 2 + 20, y - ROTOR_LENGTH // 2), ROTOR_WIDTH)
    pygame.draw.line(screen, HELICOPTER_ROTOR_COLOR, (x + HELICOPTER_WIDTH // 2, y - ROTOR_LENGTH), (x + HELICOPTER_WIDTH // 2, y), ROTOR_WIDTH)
    pygame.draw.line(screen, HELICOPTER_ROTOR_COLOR, (x + HELICOPTER_WIDTH - 20, y + HELICOPTER_HEIGHT // 2 - 10), (x + HELICOPTER_WIDTH - 20 + ROTOR_LENGTH, y + HELICOPTER_HEIGHT // 2 - 10), ROTOR_WIDTH)
    person_x = x + HELICOPTER_WIDTH // 2
    person_y = y + HELICOPTER_HEIGHT // 2
    pygame.draw.circle(screen, PERSON_COLOR, (person_x, person_y - 10), 10)
    pygame.draw.rect(screen, PERSON_COLOR, (person_x - 10, person_y, 20, 20))

# دالة لرسم الصواريخ
def draw_missiles(screen):
    for missile in missiles:
        pygame.draw.rect(screen, MISSILE_COLOR, missile)

# دالة لرسم الرشاشات
def draw_guns(screen):
    for gun in guns:
        pygame.draw.rect(screen, GUN_COLOR, gun)

# دالة لتحريك الصواريخ
def move_missiles():
    global missiles
    missiles = [pygame.Rect(m.x, m.y - MISSILE_SPEED, MISSILE_WIDTH, MISSILE_HEIGHT) for m in missiles if m.y > -MISSILE_HEIGHT]

# دالة لتحريك الرشاشات
def move_guns():
    global guns
    guns = [pygame.Rect(g.x, g.y - GUN_SPEED, GUN_WIDTH, GUN_HEIGHT) for g in guns if g.y > -GUN_HEIGHT]

# دالة لتشغيل اللعبة
def play_game():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Helicopter Game")

    clock = pygame.time.Clock()
    x, y = WIDTH // 2, HEIGHT // 2

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and y > 0:
            y -= 5
        if keys[pygame.K_DOWN] and y < HEIGHT - HELICOPTER_HEIGHT:
            y += 5
        if keys[pygame.K_LEFT] and x > 0:
            x -= 5
        if keys[pygame.K_RIGHT] and x < WIDTH - HELICOPTER_WIDTH:
            x += 5
        if keys[pygame.K_SPACE]:  # إطلاق صواريخ
            missiles.append(pygame.Rect(x + HELICOPTER_WIDTH // 2 - MISSILE_WIDTH // 2, y - MISSILE_HEIGHT, MISSILE_WIDTH, MISSILE_HEIGHT))
        if keys[pygame.K_RETURN]:  # إطلاق رشاشات
            guns.append(pygame.Rect(x + HELICOPTER_WIDTH // 2 - GUN_WIDTH // 2, y, GUN_WIDTH, GUN_HEIGHT))

        move_missiles()
        move_guns()

        screen.fill(BACKGROUND_COLOR)
        draw_helicopter(screen, x, y)
        draw_missiles(screen)
        draw_guns(screen)
        pygame.display.flip()

        clock.tick(60)  # 60 إطار في الثانية

if __name__ == "__main__":
    play_game()



