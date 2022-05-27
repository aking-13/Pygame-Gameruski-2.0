#Star Trek Gameruski
#Game designed for URI SIS Lab to inspire coding and show applications of systems engineering.
#Written by Aaron King, also included editing by Melissa Carcone
#Edited Spring 2022
#3/4/2022

import pygame
import sys
import random
from tkinter import *
from tkinter import messagebox
from PIL import Image 
import pygame_menu
import os

pygame.init()
pygame.display.set_caption('Star Trek Gameruski')

screen_max_x = 720
screen_max_y = 480
screen = pygame.display.set_mode((720, 480))

if not os.path.exists("highscore.txt"):
    open("highscore.txt", "w+")

if not os.path.exists("recordholder.txt"):
    open("recordholder.txt", "w+")

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

def game_over(score):
    global playername
    try:
        playername
    except NameError:
        playername = "Captain Kirk"
    
    myfont = pygame.font.SysFont('Comic Sans MS', 20)
    text = "Press SPACE to return to main menu"
    label = myfont.render(text, 1, white)
    screen.blit(label, [100, 300])
    end_score = "You, '"+str(playername)+"' scored: "+str(score)+" points"
    label_2 = myfont.render(end_score, 1, white)
    screen.blit(label_2, [100, 100])
    hs_file = open("highscore.txt", "r") #find current highscore
    highscore = hs_file.read()
    highscore = int(highscore)
    hs_file.close()
    hs_ply_file = open("recordholder.txt", "r") #read current record holder identity
    hs_ply_name = hs_ply_file.read()
    hs_ply_name = str(hs_ply_name)
    hs_ply_file.close()
    if highscore < score:
        delete_labels()
        print(str(score)+" in if statement")
        hs_file = open("highscore.txt", "w")
        hs_file.write(str(score))
        hs_ply_name = open("recordholder.txt","w")
        hs_ply_name.write(str(playername))
        done = False
        while not done:
            hs = "Congrats! You got the highscore: "+str(score)+" points. Well done!"
            label_3 = myfont.render(hs, 1, white)
            screen.blit(label_3, [50,200]) 
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        done = True
    elif highscore > score or highscore == score:
        delete_labels()
        done = False
        while not done:
            hs = "'"+str(hs_ply_name)+"' holds highscore of: "+str(highscore)+" points. Live Long and Prosper!"
            label_7 = myfont.render(hs, 1, white)
            screen.blit(label_7, [50, 200])
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        done = True
def delete_labels():
    try:
        labels=[label,label_2,label_3,label_4,label_5,label_7]
        for label in labels:
            del label
    except NameError:
        pass

def beat_lvl1(score):
    global playername
    try:
        playername
    except NameError:
        playername = "Captain Kirk"
    delete_labels()
    done = False
    while not done:
        myfont = pygame.font.SysFont('Comic Sans MS', 20)
        bigfont = pygame.font.SysFont('Comic Sans MS', 30)
        text = "Press SPACE to continue to boss level"
        label = myfont.render(text, 1, white)
        screen.blit(label, [200,400])
        hype = "Level One Completed."
        label_2 = bigfont.render(hype, 1, white)
        screen.blit(label_2, [200,50])
        cs = "Instructions: Avoid the Klingons and Hit the Borg Cubes."
        label_3 = myfont.render(cs,1,white)
        screen.blit(label_3, [100,300])
        beware = "Beware you are now traveling to the Klingon homeworld!"
        label_4 = myfont.render(beware,1,white)
        screen.blit(label_4, [100,250])
        pygame.display.update()
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        done = True
        
def level_1():
    delete_labels()
    clock = pygame.time.Clock()
    global score
    global collisions
    collisions = 0
    background_image = pygame.image.load("background.png").convert()
    FPS = 60  # Frames per second
    drop_rect = pygame.Rect((random.randrange(0, screen_max_x - 32, 1), 0), (32, 32))
    drop_image = pygame.Surface((32, 32))

    drop_rect1 = pygame.Rect((random.randrange(0, screen_max_x - 32, 1), 0), (32, 32))
    drop_image1 = pygame.Surface((32, 32))

    BORG_IMAGE = pygame.image.load('borgcube.png').convert()  
    rect = BORG_IMAGE.get_rect()
    rect.center = (360, 240)

    ENTRPS_IMAGE = pygame.image.load('Enterprise03.png').convert()  
    #entr_rect = ENTRPS_IMAGE.get_rect()
    #entr_rect.center = (32, 32)

    #enable key repeating (delay, rate)
    pygame.key.set_repeat(1,5)
    
    done = False
    while not done:
        clock.tick(FPS)
        # reset dropping rectangle when it reaches bottom
        if drop_rect.bottom == screen_max_y or drop_rect1.bottom == screen_max_y:
            done = True

        # drop rectangle
        drop_rect.move_ip(0,1)
        drop_rect1.move_ip(0,1)

        #collision detect, move dropping rectangle to top (with random x) when collision detected
        if drop_rect.y > rect.y -32 and drop_rect.y < rect.y + 32 and drop_rect.x > rect.x -32 and drop_rect.x < rect.x + 32 :
            drop_rect.y = 0
            drop_rect.x = random.randrange(0, screen_max_x - 21, 1)
            collisions += 1
            score += 10
        if drop_rect1.y > rect.y -32 and drop_rect1.y < rect.y + 32 and drop_rect1.x > rect.x -32 and drop_rect1.x < rect.x + 32 :
           drop_rect1.y = 0
           drop_rect1.x = random.randrange(0, screen_max_x - 21, 1)
           collisions += 1
           score += 10

        if collisions == 10:
            done = True

        # check for keyboard inputs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:    # close window (X)
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    rect.move_ip(0, -1)
                elif event.key == pygame.K_DOWN:
                    if rect.bottom < 480:
                        rect.move_ip(0, 1)
                elif event.key == pygame.K_LEFT:
                    if rect.left > 0:
                        rect.move_ip(-1, 0)
                    elif rect.left == 0:
                        rect.x = 720
                        rect.y = rect.top
                elif event.key == pygame.K_RIGHT:
                    if rect.right < 720:
                        rect.move_ip(1, 0)
                    elif rect.right == 720:
                        rect.x = 0
                        rect.y = rect.top
                elif event.key == pygame.K_q:
                    done = True
                elif event.key == pygame.K_ESCAPE: #escape key leaves game
                    done = True

        screen.blit(background_image, [0, 0])
        screen.blit(BORG_IMAGE, rect)
        screen.blit(ENTRPS_IMAGE, drop_rect)
        screen.blit(ENTRPS_IMAGE,drop_rect1)
        bigfont = pygame.font.SysFont('Comic Sans MS', 30)
        text = "Score: "+str(score)
        label_5 = bigfont.render(text, 1, white)
        screen.blit(label_5, [550,25])
        pygame.display.update()  # Or pygame.display.flip()

def level_2():
    delete_labels()
    clock = pygame.time.Clock()    
    global score
    global collisions
    collisions = 0
    background_image = pygame.image.load("background.png").convert()
    FPS = 60  # Frames per second
    
    drop_rect = pygame.Rect((random.randrange(0, screen_max_x - 32, 1), 0), (32, 32))
    drop_image = pygame.Surface((32, 32))
    drop_rect1 = pygame.Rect((random.randrange(0, screen_max_x - 32, 1), 0), (32, 32))
    drop_image1 = pygame.Surface((32, 32))
    drop_rect2 = pygame.Rect((random.randrange(0, screen_max_x - 32, 1), 0), (32, 32))
    drop_image2 = pygame.Surface((32, 32))
    drop_kling = pygame.Rect((random.randrange(0, screen_max_x - 32, 1), 0), (32,32))
    drop_image3 = pygame.Surface((32,32))

    BORG_IMAGE = pygame.image.load('borgcube.png').convert()  
    borgcube_rect = BORG_IMAGE.get_rect()
    borgcube_rect.center = (64, 64)

    KLINGON_IMAGE = pygame.image.load('Top_Klingon.jpg').convert()
    KLINGON_IMAGE = pygame.transform.scale(KLINGON_IMAGE, drop_kling.size)
    #kling_rect = KLINGON_IMAGE.get_rect()
    #kling_rect.center = (32,32)

    ENTRPS_IMAGE = pygame.image.load('Enterprise03.png').convert()  
    rect = ENTRPS_IMAGE.get_rect()
    rect.center = (360, 240)

    #enable key repeating (delay, rate)
    pygame.key.set_repeat(1,5)
    
    done = False
    while not done:
        clock.tick(FPS)
        # reset dropping rectangle when it reaches bottom
        if drop_rect.bottom == screen_max_y or drop_rect1.bottom == screen_max_y or drop_rect2.bottom == screen_max_y:
            done = True
        if drop_kling.bottom == screen_max_y:
            drop_kling.y = 0
            drop_kling.x = random.randrange(0,screen_max_x - 32, 1)
            score += 20
        
        # drop rectangle
        drop_rect.move_ip(0,1)
        drop_rect1.move_ip(0,1)
        drop_rect2.move_ip(0,1)
        drop_kling.move_ip(0,1)

        #collision detect, move dropping rectangle to top (with random x) when collision detected
        if drop_rect.y > rect.y -32 and drop_rect.y < rect.y + 32 and drop_rect.x > rect.x -32 and drop_rect.x < rect.x + 32 :
            drop_rect.y = 0
            drop_rect.x = random.randrange(0, screen_max_x - 32, 1)
            collisions += 1
            score += 10
        if drop_rect1.y > rect.y -32 and drop_rect1.y < rect.y + 32 and drop_rect1.x > rect.x -32 and drop_rect1.x < rect.x + 32 :
            drop_rect1.y = 0
            drop_rect1.x = random.randrange(0, screen_max_x - 32, 1)
            collisions += 1
            score += 10
        if drop_rect2.y > rect.y -32 and drop_rect2.y < rect.y + 32 and drop_rect2.x > rect.x -32 and drop_rect2.x < rect.x + 32 :
            drop_rect2.y = 0
            drop_rect2.x = random.randrange(0, screen_max_x - 32, 1)
            collisions += 1
            score += 10
        if drop_kling.y > rect.y -32 and drop_kling.y < rect.y + 32 and drop_kling.x > rect.x -32 and drop_kling.x < rect.x + 32 :
            done = True

        # check for keyboard inputs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:    # close window (X)
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    rect.move_ip(0, -1)
                elif event.key == pygame.K_DOWN:
                    if rect.bottom < 480:
                        rect.move_ip(0, 1)
                elif event.key == pygame.K_LEFT:
                    if rect.left > 0:
                        rect.move_ip(-1, 0)
                    elif rect.left == 0:
                        rect.x = 720
                        rect.y = rect.top
                elif event.key == pygame.K_RIGHT:
                    if rect.right < 720:
                        rect.move_ip(1, 0)
                    elif rect.right == 720:
                        rect.x = 0
                        rect.y = rect.top
                elif event.key == pygame.K_q:
                    done = True
                elif event.key == pygame.K_ESCAPE: #escape key leaves game
                    done = True

        screen.blit(background_image, [0, 0])
        screen.blit(BORG_IMAGE, rect)
        screen.blit(ENTRPS_IMAGE, drop_rect)
        screen.blit(ENTRPS_IMAGE,drop_rect1)
        screen.blit(ENTRPS_IMAGE,drop_rect2)
        screen.blit(KLINGON_IMAGE,drop_kling)
        bigfont = pygame.font.SysFont('Comic Sans MS', 30)
        text = "Score: "+str(score)
        label_5 = bigfont.render(text, 1, white)
        screen.blit(label_5, [550,25])
        pygame.display.update()

def PlayerName(name):
    global playername
    playername = name
    return playername

def set_difficulty(value,difficulty):
    pass

def start_the_game():
    global score
    score = 0
    global collisions
    delete_labels()
    pygame.mixer.music.load("TNG8BitBacktrack.mp3") 
    pygame.mixer.music.play(-1,0.0)
    #start game play
    donzo = False
    while not donzo:
        level_1()
        if score > 90:
            beat_lvl1(score)
            level_2()
            donzo = True
        else:
            donzo = True

    game_over(score)
font = pygame_menu.font.FONT_FRANCHISE

myimage = pygame_menu.baseimage.BaseImage(
    image_path="test-image-cover.jpg",
    drawing_mode=pygame_menu.baseimage.IMAGE_MODE_REPEAT_XY)
mytheme = pygame_menu.themes.THEME_DARK.copy()
mytheme.background_color = myimage
mytheme.widget_font=font
mytheme.widget_font_size = 50
menu = pygame_menu.Menu('Welcome Space Cadet', screen_max_x,screen_max_y,
                        theme=mytheme)
menu.add.text_input('Name: ', default='Captain Kirk', onchange=PlayerName, font_color=white)
#for selecting which level you would like to start on
#menu.add.selector('Start Level: ', [('Easy', 1), ('Moderate', 2), ('Hard', 3)], onchange=set_difficulty)
menu.add.button('Play', start_the_game,font_color=white) #function for starting the game
menu.add.button('Quit',pygame_menu.events.EXIT,font_color=white)

menu.mainloop(screen)
























