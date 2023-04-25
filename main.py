import math as m

import pygame
from ROBOT import Graphics,Ultrasonic,Robot

map_dimensions = (600,1200)


gfx = Graphics(map_dimensions,'car.png','map.png')

start = (200,200)
robot = Robot(start,0.01*3779.52)


#the sensor
sensor_range = 250,m.radians(40)
ultra_sonic = Ultrasonic(sensor_range,gfx.map)

dt=0
last_time = pygame.time.get_ticks()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running= False

    dt = (pygame.time.get_ticks()-last_time)/1000
    last_time = pygame.time.get_ticks()
    
    gfx.map.blit(gfx.map_img,(0,0))

    robot.kinematics(dt)
    gfx.draw_robot(robot.x,robot.y,robot.heading)
    point_cloud = ultra_sonic.sense_obstacle(robot.x,robot.y,robot.heading)
    robot.avoid_obstacle(point_cloud,dt)
    gfx.draw_sensor_data(point_cloud)


    pygame.display.update()