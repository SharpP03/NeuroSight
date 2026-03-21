import pygame
import sys
import math
import random

def run():
    pygame.init()

    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Top-Down Shooter")

    clock = pygame.time.Clock()

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)

    font = pygame.font.SysFont(None, 48)

    # ---------- FUNKCJE ----------
    def draw_text(text, x, y):
        img = font.render(text, True, WHITE)
        screen.blit(img, (x, y))

    def shoot(player_pos, bullets):
        mouse_x, mouse_y = pygame.mouse.get_pos()

        dx = mouse_x - player_pos[0]
        dy = mouse_y - player_pos[1]

        dist = math.sqrt(dx**2 + dy**2)
        if dist == 0:
            return

        dx /= dist
        dy /= dist

        bullets.append({
            "x": player_pos[0],
            "y": player_pos[1],
            "dx": dx,
            "dy": dy
        })

    # ---------- MENU ----------
    def menu():
        while True:
            screen.fill(BLACK)
            draw_text("TOP-DOWN SHOOTER", 220, 200)
            draw_text("Press ENTER to Play", 230, 300)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return

    # ---------- GAME OVER ----------
    def game_over():
        while True:
            screen.fill(BLACK)
            draw_text("GAME OVER", 300, 200)
            draw_text("Press R to Restart", 230, 300)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        return

    # ---------- GRA ----------
    def game():
        player_size = 50
        player_pos = [WIDTH // 2, HEIGHT // 2]
        player_speed = 5
        player_hp = 5

        bullets = []
        bullet_speed = 10

        enemies = []
        enemy_size = 40
        enemy_speed = 2

        spawn_timer = 0

        while True:
            # EVENTY
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        shoot(player_pos, bullets)

            # RUCH GRACZA
            keys = pygame.key.get_pressed()
            if keys[pygame.K_a]:
                player_pos[0] -= player_speed
            if keys[pygame.K_d]:
                player_pos[0] += player_speed
            if keys[pygame.K_w]:
                player_pos[1] -= player_speed
            if keys[pygame.K_s]:
                player_pos[1] += player_speed

            # BLOKADA EKRANU
            player_pos[0] = max(0, min(WIDTH - player_size, player_pos[0]))
            player_pos[1] = max(0, min(HEIGHT - player_size, player_pos[1]))

            # SPAWN ENEMY
            spawn_timer += 1
            if spawn_timer > 60:
                spawn_timer = 0

                side = random.choice(["top", "bottom", "left", "right"])

                if side == "top":
                    x = random.randint(0, WIDTH)
                    y = 0
                elif side == "bottom":
                    x = random.randint(0, WIDTH)
                    y = HEIGHT
                elif side == "left":
                    x = 0
                    y = random.randint(0, HEIGHT)
                else:
                    x = WIDTH
                    y = random.randint(0, HEIGHT)

                enemies.append([x, y])

            # RUCH ENEMY
            for enemy in enemies:
                dx = player_pos[0] - enemy[0]
                dy = player_pos[1] - enemy[1]

                dist = math.sqrt(dx**2 + dy**2)
                if dist != 0:
                    dx /= dist
                    dy /= dist

                enemy[0] += dx * enemy_speed
                enemy[1] += dy * enemy_speed

            # RUCH POCISKÓW
            for bullet in bullets:
                bullet["x"] += bullet["dx"] * bullet_speed
                bullet["y"] += bullet["dy"] * bullet_speed

            # USUWANIE POCISKÓW
            bullets = [
                b for b in bullets
                if 0 < b["x"] < WIDTH and 0 < b["y"] < HEIGHT
            ]

            # ---------- KOLIZJE ----------
            new_enemies = []
            for enemy in enemies:
                hit = False

                for bullet in bullets:
                    if (
                        enemy[0] < bullet["x"] < enemy[0] + enemy_size and
                        enemy[1] < bullet["y"] < enemy[1] + enemy_size
                    ):
                        hit = True
                        bullets.remove(bullet)
                        break

                if not hit:
                    new_enemies.append(enemy)

            enemies = new_enemies

            # ENEMY UDERZA W GRACZA
            new_enemies = []
            for enemy in enemies:
                if (
                    player_pos[0] < enemy[0] < player_pos[0] + player_size and
                    player_pos[1] < enemy[1] < player_pos[1] + player_size
                ):
                    player_hp -= 1
                else:
                    new_enemies.append(enemy)

            enemies = new_enemies

            # GAME OVER
            if player_hp <= 0:
                return

            # RYSOWANIE
            screen.fill(BLACK)

            pygame.draw.rect(screen, WHITE, (*player_pos, player_size, player_size))

            for bullet in bullets:
                pygame.draw.rect(screen, WHITE, (bullet["x"], bullet["y"], 10, 10))

            for enemy in enemies:
                pygame.draw.rect(screen, RED, (*enemy, enemy_size, enemy_size))

            draw_text(f"HP: {player_hp}", 10, 10)

            pygame.display.flip()
            clock.tick(60)

    # ---------- FLOW GRY ----------
    while True:
        menu()
        game()
        game_over()