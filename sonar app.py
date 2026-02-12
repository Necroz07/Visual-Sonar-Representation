# 1px = 10m

import pygame
import math
import time



pygame.init()

font = pygame.font.Font("Minecraftia-Regular.ttf", 19)


text = None

screen=pygame.display.set_mode((600,600))
pygame.display.set_caption("Sonar visualization")

wave_surf = pygame.Surface((600, 600), pygame.SRCALPHA)
echo_surf = pygame.Surface((600, 600), pygame.SRCALPHA)

score_overlay = pygame.Surface((600,600), pygame.SRCALPHA)

echo_wave = False

icon = pygame.image.load("icon.png").convert_alpha()
icon = pygame.transform.scale(icon, (50, 50))
icon_rect = icon.get_rect()


bg = pygame.image.load("background.png").convert()
bg = pygame.transform.scale(bg, (600,600))

obj = pygame.image.load("object1.png").convert_alpha()
obj = pygame.transform.scale(obj, (60, 60))
obj_rect = obj.get_rect(center=(300,300))

spawn = pygame.image.load("spawn.png").convert_alpha()
spawn = pygame.transform.scale(spawn, (25, 25))
spawn_rect = spawn.get_rect()


clock=pygame.time.Clock()

running=True
hit_locked = False
hit_lockedtil = 0
locked_ms= 1500

wave_radius = 0
wave_speed = 2
echo_rad = 0
echo_speed = 2


last_time = pygame.time.get_ticks()



summon = False
inc=True

while running:

    wave_surf.fill((0,0,0,0))
    echo_surf.fill((0,0,0,0))
    score_overlay.fill((0,0,0,0))

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONUP:
            summon = True
            spawn_rect.center = event.pos
            spawncenter= (spawn_rect.center[0]-12, spawn_rect.center[1]-12)
            spawntime = pygame.time.get_ticks()

    pygame.draw.circle(wave_surf, (0, 0, 0, 200), obj_rect.center, wave_radius, 5)

    pygame.draw.polygon(score_overlay, (0, 0, 0, 210), [(0,600), (50, 530), (100, 530), (200, 530), (300,530), (400, 530), (500, 530), (550, 530), (600,600)])
    
    #mid line
    pygame.draw.line(score_overlay, (50, 205, 50), (53, 537), (545, 537), 3)

    #left line
    pygame.draw.line(score_overlay, (50, 205, 50), (3,610), (53, 537), 4)

    #right line
    pygame.draw.line(score_overlay, (50, 205, 50), (545, 537), (597, 610), 4)

    


    screen.blit(bg, (0,0))
    screen.blit(obj, obj_rect)
    screen.blit(wave_surf, (0, 0))

    if inc==True:
        wave_radius += wave_speed


    elif inc==False:
        wave_radius -= wave_speed

    
    if echo_wave==True:
        pygame.draw.circle(echo_surf, (0, 0, 0, 150), (spawncenter[0]+11, spawncenter[1]+11), echo_rad, 5)
    
        screen.blit(echo_surf, (0,0))
        echo_rad += echo_speed

        if abs((dist-7)-echo_rad)<=3:

            echo_wave=False
            hit_locked = False

            echo_endt = pygame.time.get_ticks()
            t2= echo_endt-echo_time
            totaltime = (t1 + t2)/1000
            distancem = int(1500 * totaltime)/2
            distancepx = int(distancem/10)

            text = font.render(f"{distancem}m/{distancepx}px", True, (255, 255, 255))

            print(f"distance- {distancem}m/{distancepx}px, total time- {totaltime}")

    

    if wave_radius > 415:
        inc = False
        circle_shrink_start = pygame.time.get_ticks()

    if wave_radius < 17:
        inc = True
        circle_time_start = pygame.time.get_ticks()



    if summon == True:
        screen.blit(spawn, (spawncenter))

        if pygame.time.get_ticks() - spawntime > 3000:
            summon = False
            hit_locked = False

        dist = math.hypot(spawncenter[0]-300, spawncenter[1]-300)
        
        if abs(dist-wave_radius)<=3 and not hit_locked and (pygame.time.get_ticks() >= hit_lockedtil):
            current= pygame.time.get_ticks()
            echo_time = pygame.time.get_ticks()


            if inc:
                t1=current-circle_time_start
            elif not inc:
                t1=((circle_shrink_start-circle_time_start)-(echo_time-circle_shrink_start))
        
            echo_rad=0
            pygame.draw.circle(echo_surf, (0, 0, 0, 150), spawncenter, echo_rad, 5)

            echo_wave = True
            hit_locked = True
            hit_lockedtil = pygame.time.get_ticks() + locked_ms  

    score_overlay.blit(icon, (50, 545))
    

    if text:
        score_overlay.blit(text, (95, 557))

        
    screen.blit(score_overlay, (0,0))

    pygame.display.flip()

    
    clock.tick(60)  #FPS

pygame.quit()
