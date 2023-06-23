# Python Practical 19 : To write a python program to simulate bouncing ball in Pygame.

# this will not work in VS Code - SO kindly use Python Proper IDE.

# import pygame 
# import random

# pygame.init()

# WIDTH = 800
# HEIGHT = 600

# BALL_RADIUS = 20
# BALL_COLOR = (255, 0, 0)

# window = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Bouncing Ball")

# clock = pygame.time.Clock()

# ball_pos = [WIDTH // 2, HEIGHT // 2]
# ball_vel = [random.randint(-5, 5), random.randint(-5, 5)]

# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     window.fill((255, 255, 255))  # White

#     ball_pos[0] += ball_vel[0]
#     ball_pos[1] += ball_vel[1]

#     if ball_pos[0] + BALL_RADIUS >= WIDTH or ball_pos[0] - BALL_RADIUS <= 0:
#         ball_vel[0] = -ball_vel[0]
#     if ball_pos[1] + BALL_RADIUS >= HEIGHT or ball_pos[1] - BALL_RADIUS <= 0:
#         ball_vel[1] = -ball_vel[1]

#     pygame.draw.circle(window, BALL_COLOR, (ball_pos[0], ball_pos[1]), BALL_RADIUS)

#     pygame.display.update()
#     clock.tick(60)  # Limit the frame rate to 60 FPS

# pygame.quit()

print("\n\n\n Name: Kumar Devanshu \t Roll No: 2200970139009 \t Section: IT-A2")

print("\n")

