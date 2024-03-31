import pygame

pygame.init()
font = pygame.font.Font("Samson.ttf", 24)
text_surface = font.render("Welcome to the paint application!!", None, (0, 255, 255))
win = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Paint")
run = True
brush_size = 15
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
PURPLE = (255, 0, 255)
CYAN = (0, 255, 255)
ORANGE = (255, 165, 0)
PINK = (255, 192, 203)
DARK_BLUE = (0, 0, 128)
drawing = False
current_color = RED
shape = 'circle'
win.fill((255, 255, 255))
paint_icon = pygame.image.load("paint.png")
pygame.display.set_icon(paint_icon)
rectangle_size = 15

while run:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: 
                drawing = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1: 
                drawing = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c: 
                shape = 'circle'
            elif event.key == pygame.K_q:
                shape = 'rectangle'
            elif event.key == pygame.K_v:
                current_color = BLACK 
            elif event.key == pygame.K_r:
                current_color = RED
            elif event.key == pygame.K_g:
                current_color = GREEN
            elif event.key == pygame.K_b:
                current_color = BLUE
            elif event.key == pygame.K_w:
                current_color  = WHITE 
            elif event.key == pygame.K_p:
                current_color = PURPLE
            elif event.key == pygame.K_d:
                current_color = DARK_BLUE
            elif event.key == pygame.K_y:
                current_color = YELLOW
            elif event.key == pygame.K_n:
                win.fill((255, 255, 255))
            elif event.key == pygame.K_1:
                brush_size = 15
            elif event.key == pygame.K_2:
                brush_size = 20
            elif event.key == pygame.K_3:
                brush_size = 30
            elif event.key == pygame.K_4:
                brush_size = 40
            elif event.key == pygame.K_5:
                brush_size = 50
            

    if drawing:
        if shape == 'circle': 
            pos = pygame.mouse.get_pos()
            pygame.draw.circle(win, current_color, pos, brush_size)
        elif shape == 'rectangle':
            rect_pos = pygame.mouse.get_pos()
            pygame.draw.rect(win, current_color, (rect_pos[0] - 20, rect_pos[1] - 20, brush_size*2, brush_size*2))
    win.blit(text_surface, (0, 0))

    pygame.display.update()

pygame.quit()
