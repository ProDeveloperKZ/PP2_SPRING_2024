import pygame
import datetime

pygame.init()
current_date = datetime.datetime.now()

SECONDS  = current_date.second
MINUTE = current_date.minute
win = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Mickeyclock")

image = pygame.image.load("mainclock.png")
right_hand_image = pygame.image.load("righthand.png")
left_hand_image = pygame.image.load("lefthand.png")

right_hand_image = pygame.transform.scale(right_hand_image, (int(right_hand_image.get_width() * 0.6), int(right_hand_image.get_height() * 0.6)))
left_hand_image = pygame.transform.scale(left_hand_image, (int(left_hand_image.get_width() * 0.6), int(left_hand_image.get_height() * 0.6)))

image = pygame.transform.scale(image, (800, 600))
image_width, image_height = image.get_size()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    current_time = datetime.datetime.now()
    second_angle  =  90 - current_time.second * 6
    minute_angle = 60 - current_time.minute * 6 
    rotated_image_left  =  pygame.transform.rotate(left_hand_image , second_angle)
    rotated_image_right  = pygame.transform.rotate(right_hand_image, minute_angle)
    

    win.fill((255, 255, 255))
    win.blit(image, (0, 0))

    right_hand_x = (image_width - right_hand_image.get_width()) //2 
    right_hand_y = (image_height - right_hand_image.get_height()) //2 
    left_hand_x = (image_width - left_hand_image.get_width()) //2
    left_hand_y = (image_height - left_hand_image.get_height()) // 2
    rotated_image_x = (image_width - rotated_image_left.get_width()) // 2
    rotated_image_y  = (image_height - rotated_image_left.get_height()) // 2
    rotated_image_x1 = (image_width - rotated_image_right.get_width()) // 2
    rotated_image_y1 = (image_height - rotated_image_right.get_height())  // 2

    win.blit(rotated_image_right, (rotated_image_x1, rotated_image_y1))

    win.blit(rotated_image_left,(rotated_image_x,rotated_image_y))

    pygame.display.update()

pygame.quit()