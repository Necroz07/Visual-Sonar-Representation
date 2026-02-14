# 1px = 10m

import pygame
import math
import os
from pathlib import Path

os.chdir(Path(__file__).resolve().parent)


pygame.init()
pygame.mixer.init()

wave_startsound = pygame.mixer.Sound("sounds/wave_start.wav")
wave_endsound = pygame.mixer.Sound("sounds/wave_end.wav")
hitsound = pygame.mixer.Sound("sounds/cat.wav")
click = pygame.mixer.Sound("sounds/click.mp3")
pause = pygame.mixer.Sound("sounds/pause.wav")

sfx = True
bgm = True
sfx_vol = 0.8
bg_vol = 0.6

distances=[]

x=50


font = pygame.font.Font("assets/Minecraftia-Regular.ttf", 19)


font1 = pygame.font.Font("assets/Minecraftia-Regular.ttf", 57)


font2 = pygame.font.Font("assets/Minecraftia-Regular.ttf", 27)

font3 = pygame.font.Font("assets/Minecraftia-Regular.ttf", 17)


text = font.render("Distance", True, (255, 255, 255))
text2 = font.render("Time", True, (255, 255, 255))

screen=pygame.display.set_mode((600,600))
pygame.display.set_caption("Sonar visualization")

wave_surf = pygame.Surface((600, 600), pygame.SRCALPHA)
echo_surf = pygame.Surface((600, 600), pygame.SRCALPHA)

score_overlay = pygame.Surface((600,600), pygame.SRCALPHA)
tab_overlay = pygame.Surface((600,600), pygame.SRCALPHA)

echo_wave = False

icon = pygame.image.load("assets/icon.png").convert_alpha()
icon = pygame.transform.scale(icon, (50, 50))
icon_rect = icon.get_rect()

clock1 = pygame.image.load("assets/clock.png").convert_alpha()
clock1 = pygame.transform.scale(clock1, (40,40))
clock1_rect = clock1.get_rect()


musicpng = pygame.image.load("assets/music.png")
musicpng = pygame.transform.scale(musicpng, (180, 180))
musicpng_rect = musicpng.get_rect()


sfxpng = pygame.image.load("assets/sfx.png")
sfxpng = pygame.transform.scale(sfxpng, (180, 180))
sfxpng_rect = sfxpng.get_rect()


bg = pygame.image.load("assets/background.png").convert()
bg = pygame.transform.scale(bg, (600,600))

obj = pygame.image.load("assets/object1.png").convert_alpha()
obj = pygame.transform.scale(obj, (60, 60))
obj_rect = obj.get_rect(center=(300,300))

spawn = pygame.image.load("assets/spawn.png").convert_alpha()
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

alpha = 0


last_time = pygame.time.get_ticks()


unit = font.render("1px = 10m", True, (255, 255, 255))

summon = False
inc=True
pausech = 'no'

pygame.mixer.music.load("sounds/bg.mp3")
pygame.mixer.music.play(-1)


while running:

 
    wave_surf.fill((0,0,0,0))
    echo_surf.fill((0,0,0,0))
    score_overlay.fill((0,0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #clicking when not paused
        elif event.type == pygame.MOUSEBUTTONUP and pausech=='no' and echo_wave==False and summon==False:
            summon = True
            click.play()
            spawn_rect.center = event.pos
            spawncenter= (spawn_rect.center[0]-12, spawn_rect.center[1]-12)
            spawntime = pygame.time.get_ticks()

        #enabling pause
        elif event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_ESCAPE) and (pausech=='no'):
                pausech = 'pause'
                alpha = 0
                pygame.mixer.music.pause()
                pause.play(-1)
            
            #disabling pause
            elif (event.key == pygame.K_ESCAPE) and (pausech=='pause'):
                pausech = 'no'
                pause.stop()
                pygame.mixer.music.unpause()

            #tab enable
            elif (event.key == pygame.K_TAB) and (pausech=='no'):
                pausech= 'tab'

            #tab disable
            elif (event.key == pygame.K_TAB) and (pausech=='tab'):
                pausech = 'no'



        if event.type == pygame.MOUSEBUTTONDOWN and pausech=='pause':
            if boxbgm.collidepoint(event.pos):
                click.play()

                if bgm:
                    bgm=False
                else:
                    bgm=True

            elif boxsfx.collidepoint(event.pos):
                click.play()

                if sfx:
                    sfx=False
                else:
                    sfx=True


                

            

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



    
    screen.blit(bg, (0,0))
    screen.blit(obj, obj_rect)
    screen.blit(wave_surf, (0, 0))

    if inc==True and pausech=='no':
        wave_radius += wave_speed


    elif inc==False and pausech=='no':
        wave_radius -= wave_speed

    
    if echo_wave==True and pausech=='no':
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

            i = (distancem, distancepx, totaltime, spawncenter)
            distances.append(i)

    

    if wave_radius > 415:
        inc = False
        circle_shrink_start = pygame.time.get_ticks()
        wave_endsound.play()

    if wave_radius < 17:
        inc = True
        circle_time_start = pygame.time.get_ticks()
        wave_startsound.play()



    if summon == True and pausech=='no':
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

    if pausech=='no':
        screen.blit(score_overlay, (0,0))


    if pausech=='pause':

        if alpha<=210:
            pygame.draw.polygon(score_overlay, (0, 0, 0, alpha), [(0,100), (0,500), (600, 500), (600, 100)])
            alpha+=5
        else:
            pygame.draw.polygon(score_overlay, (0, 0, 0, 220), [(0,100), (0,500), (600, 500), (600, 100)])
        
        #outline box for pause
        pygame.draw.polygon(score_overlay, (0, 250, 0, 220), [(15, 115), (15, 485), (585, 485), (585, 115)], 3)

        #music button outline box
        boxbgm = pygame.draw.polygon(score_overlay, (255, 255, 255, 220), [(55, 215), (55, 450), (280, 450), (280, 215)], 3)

        #sfx button outline box
        boxsfx = pygame.draw.polygon(score_overlay, (255, 255, 255, 220), [(330, 215), (550, 215), (550, 450), (330, 450)], 3)



        PAUSEtext= font1.render("PAUSE", True, (255, 255, 255, 255))

        score_overlay.blit(PAUSEtext, (200, 130))

        score_overlay.blit(musicpng, (75, 245))
        score_overlay.blit(sfxpng, (350, 245))


        if bgm:
        
            pygame.mixer.music.set_volume(bg_vol)
            pause.set_volume(bg_vol)
        else:
            pygame.mixer.music.set_volume(0)
            pause.set_volume(0)

            pygame.draw.line(score_overlay, (255, 0, 0), (85, 245), (250, 420), 8)

        if sfx:
            wave_startsound.set_volume(sfx_vol)
            wave_endsound.set_volume(sfx_vol)
            hitsound.set_volume(sfx_vol)
            click.set_volume(sfx_vol)

        else:
            wave_startsound.set_volume(0)
            wave_endsound.set_volume(0)
            hitsound.set_volume(0)
            click.set_volume(0)

            pygame.draw.line(score_overlay, (255, 0, 0), (360, 245), (520, 420), 8)

        screen.blit(score_overlay, (0,0))

    if pausech=='tab':

        if alpha<=210:
            pygame.draw.polygon(tab_overlay, (0, 0, 0, alpha), [(0, 50), (0, 550), (600, 550), (600, 50)])
            alpha+=5
        else:
            pygame.draw.polygon(tab_overlay, (0, 0, 0, 220), [(0, 50), (0, 550), (600, 550), (600, 50)])
        
        #outline box for pause
        pygame.draw.polygon(tab_overlay, (0, 250, 0, 220), [(15, 65), (15, 535), (585, 535), (585, 65)], 3)



        ctrltext= font2.render("Controls", True, (0, 255, 0, 255))

        tab_overlay.blit(ctrltext, (220, 80))

        clicktxt = font3.render("click: place ping", True, (255, 255, 255, 255))
        tabtxt = font3.render("tab: overview", True, (255, 255, 255, 255))
        esctxt = font3.render("esc: pause", True, (255, 255, 255, 255))

        tab_overlay.blit(clicktxt, (50, 130))
        tab_overlay.blit(tabtxt, (250, 130))
        tab_overlay.blit(esctxt, (430, 130))

        historytxt = font2.render("History", True, (0, 255, 0, 255))

        tab_overlay.blit(historytxt, (230, 180))

        titles = font3.render(f"Distance(m)/(px):                  Time:                      Coordinates: ", True, (0, 255, 0, 255))

        tab_overlay.blit(titles, (30, 240))

        if len(distances)<1:
            disttxt = font3.render("Please place a node first.", True, (255, 255, 255, 255))

            tab_overlay.blit(disttxt, (50, 240))

        else:
            
            tab_overlay.blit(titles, (30, 240))

            
            y=0
            for j in range(-1, -6, -1):
                try:
                    disttxt = font3.render(f"{distances[j][0]}/{distances[j][1]}                                 {distances[j][2]}                         {distances[j][3]}", True, (255, 255, 255, 255))
                    y+=1
                    tab_overlay.blit(disttxt, (30, 240+(x*y)))
                    
                except:
                    print(".")
            

        
        screen.blit(tab_overlay, (0, 0))

    pygame.display.flip()
    
    clock.tick(60)  #FPS

pygame.quit()
