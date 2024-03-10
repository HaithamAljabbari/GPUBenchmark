import random
from customtkinter import *
import time
import pygame
import math
import threading

root = CTk()

root.title("GPU BENCHMARK TEST")

progress_bar = CTkProgressBar(root, width=200, progress_color="red")
progress_bar.set(0)
progress_bar.pack()

def move_progress(num):
    progress_bar.set(num)

def start():
    pygame.init()
    move_progress(0)
    screen = pygame.display.set_mode((1200, 720))
    pygame.display.set_caption("GPU BENCHMARK")
    running = True

    circle_pos = pygame.Vector2(screen.get_width()/2, screen.get_height()/2)
    circle_perimeter = 400*math.pi

    start = time.time()

    x = 600
    y = 360

    n = 0

    speed_x = random.uniform(1, 90)
    speed_y = random.uniform(1, 90)


    while n < 1000:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.draw.circle(screen, "blue", (x, y), radius=2, width=1)
        pygame.draw.rect(screen, "red",(500, 260, 200, 200), 1)
    
        if x > 697:
            n += 1
            progress_bar.set(n)
            title_button.pack()
            speed_x = -(random.uniform(1, 20))
    #elif x < 400:
    #    speed_x = -(random.uniform(1, 20))
        elif y > 448:
            n += 1 
            progress_bar.set(n)
            title_button.pack()
            speed_y = -(random.uniform(1, 20))
        elif y < 260:
            n += 1
            progress_bar.set(n)
            title_button.pack()
            speed_y = (random.uniform(1, 20))
        elif x < 500:
            n += 1
            progress_bar.set(n)
            title_button.pack()
            speed_x = (random.uniform(1, 20))
    
        x += speed_x
        y += speed_y
        pygame.display.update()
        pygame.display.flip()

    pygame.quit()

    end = time.time()
    results = CTkLabel(root, text=(" score: " + str(round(n+100*(end - start))) + " time: " + str(round(end - start))))
    results.pack()

title_button = CTkLabel(root, text="GPU BENCHMARK")
title_button.pack()
start_button = CTkButton(root, text="run", command=lambda: start())
start_button.pack(ipadx=5, ipady=5, expand=True)
root.mainloop()
