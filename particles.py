#!/usr/bin/env python3

# MIT License

# Copyright (c) 2022 Elijah Gordon (NitrixXero) <nitrixxero@gmail.com>

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


from sys import exit
from random import randint, uniform
from math import pi, cos, sin
import pygame
from pygame import init, display, FULLSCREEN, event, QUIT, KEYDOWN, K_ESCAPE, draw, time

init()

screen_info = display.Info()
WIDTH = screen_info.current_w
HEIGHT = screen_info.current_h

screen = display.set_mode((WIDTH, HEIGHT), FULLSCREEN)
display.set_caption("Particles")


def change_color(key):
    colors = {
        pygame.K_b: (0, 0, 255),
        pygame.K_c: (0, 255, 255),
        pygame.K_d: (110, 75, 38),
        pygame.K_e: (255, 121, 77),
        pygame.K_f: (246, 74, 138),
        pygame.K_g: (0, 255, 0),
        pygame.K_h: (223, 115, 255),
        pygame.K_r: (255, 0, 0),
        pygame.K_w: (255, 255, 255),
        pygame.K_y: (255, 255, 0),
        pygame.K_m: (255, 0, 255),
        pygame.K_o: (128, 128, 0),
        pygame.K_t: (0, 128, 128),
    }
    return colors.get(key)


class Particle:
    def __init__(self):
        self.x = randint(0, WIDTH)
        self.y = randint(0, HEIGHT)
        self.radius = randint(1, 3)
        self.color = (0, 0, 255)

        self.speed = uniform(0.1, 2)
        self.angle = uniform(0, pi * 2)

    def move(self):
        self.x += cos(self.angle) * self.speed
        self.y += sin(self.angle) * self.speed

        if self.x < 0:
            self.x = WIDTH
        elif self.x > WIDTH:
            self.x = 0
        if self.y < 0:
            self.y = HEIGHT
        elif self.y > HEIGHT:
            self.y = 0


def draw_particles(particles):
    for particle in particles:
        draw.circle(
            screen,
            particle.color,
            (int(particle.x), int(particle.y)),
            particle.radius
        )


def generate_particles(num_particles):
    return [Particle() for _ in range(num_particles)]


running = True
particles = generate_particles(500)

while running:
    for evt in event.get():
        if evt.type == QUIT:
            running = False

        elif evt.type == KEYDOWN:
            if evt.key == K_ESCAPE:
                running = False

            new_color = change_color(evt.key)
            if new_color:
                for particle in particles:
                    particle.color = new_color

    screen.fill((0, 0, 0))

    for particle in particles:
        particle.move()

    draw_particles(particles)

    display.flip()
    time.delay(30)

pygame.quit()
exit()
