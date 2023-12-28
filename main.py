import random
import pygame
import cv2
import numpy as np
from cvzone.HandTrackingModule import HandDetector
import time

# MENYIAPKAN FITUR PERMAINAN DAN KAMERA
pygame.init()

width, height = 1280, 720
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pecah Balon")

fps = 30
clock = pygame.time.Clock()

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

# Ukuran gambar aset
imgNewWidth = 200
imgNewHeight = 200

# Gambar balon pecah
imgPop = pygame.transform.scale((pygame.image.load('img/balloon_pop.png').convert_alpha()),
                                (imgNewWidth, imgNewHeight))

# Sfx balon pecah
popSound = pygame.mixer.Sound('sfx/balloon_pop.wav')

# List tempat menyimpan objek balon dan posisi balon
imgBalloons = []
rectBalloons = []

# List nama balon berbagai warna
imgBalloonsName = ['img/balloon_red.png', 'img/balloon_green.png', 'img/balloon_yellow.png',
                   'img/balloon_pink.png', 'img/balloon_purple.png']

def loadBalloons():
    for color in imgBalloonsName:
        # Load objek ke list imgBalloons
        imgBalloons.append(pygame.transform.scale((pygame.image.load(color).convert_alpha()),
                                                  (imgNewWidth, imgNewHeight)))

    for i in range(len(imgBalloons)):
        # Get dan append posisi objek ke list rectBalloons
        rectBalloons.append(imgBalloons[i].get_rect())


def resetBalloon(balloonIndex):
    # Atur titik koordinat tempat balon muncul
    if balloonIndex == 0:
        rectBalloons[0].x = random.randint(100, img.shape[1] - 200)
        rectBalloons[0].y = img.shape[0] + random.randint(1, 100)
    if balloonIndex == 1:
        rectBalloons[1].x = random.randint(100, img.shape[1] - 200)
        rectBalloons[1].y = img.shape[0] + random.randint(1, 100)
    if balloonIndex == 2:
        rectBalloons[2].x = random.randint(100, img.shape[1] - 200)
        rectBalloons[2].y = img.shape[0] + random.randint(1, 100)
    if balloonIndex == 3:
        rectBalloons[3].x = random.randint(100, img.shape[1] - 200)
        rectBalloons[3].y = img.shape[0] + random.randint(1, 100)
    if balloonIndex == 4:
        rectBalloons[4].x = random.randint(100, img.shape[1] - 200)
        rectBalloons[4].y = img.shape[0] + random.randint(1, 100)

# Fuction animasi dan suara balon saat pecah
def popFxPlay(x, y):
    window.blit(imgPop, (x, y))
    pygame.display.update()
    pygame.time.delay(60)
    popSound.play()

speed = 15
score = 0
startTime = time.time()
totalTime = 30
detector = HandDetector(detectionCon=0.8, maxHands=2)

# Load awal
loadBalloons()

start = True
while start:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False
            pygame.quit()

    timeRemain = int(totalTime - (time.time() - startTime))
    if timeRemain < 0:
        window.fill((255, 255, 255))
        font = pygame.font.Font(None, 50)
        textScore = font.render(f'Your Score: {score}', True, (50, 50, 255))
        textTime = font.render('Time\'s Up', True, (50, 50, 255))
        textTitle = font.render(f'Pecah Balon', True, (50, 50, 255))
        window.blit(textTitle, (490, 35))
        window.blit(textScore, (450, 350))
        window.blit(textTime, (530, 275))

    else:
        success, img = cap.read()
        img = cv2.flip(img, 1)
        hands, img = detector.findHands(img, flipType=False)

        # Mengatur pergerakan balon dari bawah ke atas
        for i in range(len(rectBalloons)):
            rectBalloons[i].y -= speed
            if rectBalloons[i].y < 0:
                resetBalloon(i)
                speed += 1/2

        if hands:
            for hand in hands:
            # hand = hands[0]
                x, y = hand['lmList'][8][0:2]
                for i in range(len(rectBalloons)):
                    if rectBalloons[i].collidepoint(x, y):
                        popFxPlay(rectBalloons[i].x, rectBalloons[i].y)
                        resetBalloon(i)
                        score += 10
                        speed += 1/2

        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        imgRGB = np.rot90(imgRGB)
        frame = pygame.surfarray.make_surface(imgRGB).convert()
        frame = pygame.transform.flip(frame, True, False)
        window.blit(frame, (0, 0))

        for i in range(len(rectBalloons)):
            window.blit(imgBalloons[i], rectBalloons[i])

        font = pygame.font.Font(None, 50)
        textScore = font. render(f'Score: {score}', True, (50, 50, 255))
        textTime = font.render(f'Time: {timeRemain}', True, (50, 50, 255))
        textTitle = font.render(f'Pecah Balon', True, (50, 50, 255))
        window.blit(textTitle, (490, 35))
        window.blit(textScore, (35, 35))
        window.blit(textTime, (1000, 35))

    pygame.display.update()
    clock.tick(fps)