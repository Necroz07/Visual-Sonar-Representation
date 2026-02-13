# 1px = 10m

import pygame
import math
import time


pygame.init()
pygame.mixer.init()

wave_startsound = pygame.mixer.Sound("wave start.wav")
wave_endsound = pygame.mixer.Sound("wave end.wav")
hitsound = pygame.mixer.Sound("cat.mp3")
click = pygame.mixer.Sound("click.mp3")
bgm = pygame.mixer.Sound("bg.mp3")
pause = pygame.mixer.Sound("pause.mp3")

sfx_vol = 0.6
bg_vol = 0.6


font = pygame.font.Font("Minecraftia-Regular.ttf", 19)


text = font.render("Distance", True, (255, 255, 255))
text2 = font.render("Time", True, (255, 255, 255))

screen=pygame.display.set_mode((600,600))
pygame.display.set_caption("Sonar visualization")

wave_surf = pygame.Surface((600, 600), pygame.SRCALPHA)
echo_surf = pygame.Surface((600, 600), pygame.SRCALPHA)

score_overlay = pygame.Surface((600,600), pygame.SRCALPHA)
pause_overlay = pygame.Surface((600,600), pygame.SRCALPHA)

echo_wave = False

icon = pygame.image.load("icon.png").convert_alpha()
icon = pygame.transform.scale(icon, (50, 50))
icon_rect = icon.get_rect()

clock1 = pygame.image.load("clock.png").convert_alpha()
clock1 = pygame.transform.scale(clock1, (40,40))
clock1_rect = clock1.get_rect()


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


unit = font.render("1px = 10m", True, (255, 255, 255))

summon = False
inc=True
pausebool = False


bgm.play(-1)

while running:

    wave_startsound.set_volume(sfx_vol)
    wave_endsound.set_volume(sfx_vol)
    hitsound.set_volume(sfx_vol)
    click.set_volume(sfx_vol)
    bgm.set_volume(bg_vol)
    pause.set_volume(bg_vol)

    wave_surf.fill((0,0,0,0))
    echo_surf.fill((0,0,0,0))
    score_overlay.fill((0,0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONUP and not pausebool:
            summon = True
            click.play()
            spawn_rect.center = event.pos
            spawncenter= (spawn_rect.center[0]-12, spawn_rect.center[1]-12)
            spawntime = pygame.time.get_ticks()

        elif event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_ESCAPE) and (not pausebool):
                pausebool = True
                pygame.mixer.music.pause()
                pause.play()
                
            elif (event.key == pygame.K_ESCAPE) and (pausebool):
                pausebool = False
                pygame.mixer.music.stop()
                pygame.mixer.music.unpause()

            

    pygame.draw.circle(wave_surf, (0, 0, 0, 200), obj_rect.center, wave_radius, 5)

    pygame.draw.polygon(score_overlay, (0, 0, 0, 210), [(0,600), (50, 530), (100, 530), (200, 530), (300,530), (400, 530), (500, 530), (550, 530), (600,600)])
    
    #mid line
    pygame.draw.line(score_overlay, (50, 205, 50), (53, 537), (545, 537), 3)

    #left line
    pygame.draw.line(score_overlay, (50, 205, 50), (3,610), (53, 537), 4)

    #right line
    pygame.draw.line(score_overlay, (50, 205, 50), (545, 537), (597, 610), 4)

    #top square
    pygame.draw.polygon(score_overlay, (0, 0, 0, 175), [(20, 20), (155, 20), (155, 67),  (20, 67)])

    
#top GUI
    #top line
    pygame.draw.line(score_overlay, (50, 205, 50), (27, 27), (147, 27), 2)

    #bottom line
    pygame.draw.line(score_overlay, (50, 205, 50), (147, 60), (27, 60), 2)

    #left line
    pygame.draw.line(score_overlay, (50, 205, 50), (27, 27), (27, 60), 2)

    #right line
    pygame.draw.line(score_overlay, (50, 205, 50), (147, 60), (147, 27), 2)


    

    

    if not pausebool:
        screen.blit(bg, (0,0))
        screen.blit(obj, obj_rect)
        screen.blit(wave_surf, (0, 0))

    if inc==True and not pausebool:
        wave_radius += wave_speed


    elif inc==False and not pausebool:
        wave_radius -= wave_speed

    
    if echo_wave==True and not pausebool:
        pygame.draw.circle(echo_surf, (0, 0, 0, 150), (spawncenter[0]+11, spawncenter[1]+11), echo_rad, 5)
    
        screen.blit(echo_surf, (0,0))
        echo_rad += echo_speed

        if abs((dist-7)-echo_rad)<=3:

            echo_wave=False
            hit_locked = False
            hitsound.play()

            echo_endt = pygame.time.get_ticks()
            t2= echo_endt-echo_time
            totaltime = (t1 + t2)/1000
            distancem = int(1500 * totaltime)/2
            distancepx = int(distancem/10)

            text = font.render(f"{distancem}m or {distancepx}px", True, (255, 255, 255))
            text2 = font.render(f"Time- {totaltime}s", True, (255, 255, 255))

    

    if wave_radius > 415:
        inc = False
        circle_shrink_start = pygame.time.get_ticks()
        wave_endsound.play()

    if wave_radius < 17:
        inc = True
        circle_time_start = pygame.time.get_ticks()
        wave_startsound.play()



    if summon == True and not pausebool:
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
            wave_startsound.play()
            hit_locked = True
            hit_lockedtil = pygame.time.get_ticks() + locked_ms  

    
    score_overlay.blit(icon, (50, 545))
    score_overlay.blit(clock1, (345, 550))
    score_overlay.blit(unit, (35, 31))
    

    if text or text2:
        score_overlay.blit(text, (106, 557))
        score_overlay.blit(text2, (395, 557))

    if not pausebool:
        screen.blit(score_overlay, (0,0))

    pygame.display.flip()
    
    clock.tick(60)  #FPS

pygame.quit()
