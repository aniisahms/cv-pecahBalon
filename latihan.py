# import random
# import pygame
# import cv2
# import numpy as np
# from cvzone.HandTrackingModule import HandDetector
# import time
#
# # MENYIAPKAN FITUR PERMAINAN DAN KAMERA
# pygame.init()
#
# width, height = 1280, 720
# window = pygame.display.set_mode((width, height))
# pygame.display.set_caption("Pecah Balon")
#
# fps = 30
# clock = pygame.time.Clock()
#
# cap = cv2.VideoCapture(0)
# cap.set(3, 1280)
# cap.set(4, 720)
#
# # Ukuran gambar aset
# imgNewWidth = 200
# imgNewHeight = 200
#
# # Balon berbagai warna
# imgBalloonRed = pygame.transform.scale((pygame.image.load('img/balloon_red.png').convert_alpha()),
#                                        (imgNewWidth, imgNewHeight))
#
# rectBalloon = imgBalloonRed.get_rect()
# rectBalloon.x, rectBalloon.y = 500, 300
#
# speed = 15
# score = 0
# startTime = time.time()
# totalTime = 30
# detector = HandDetector(detectionCon=0.8, maxHands=1)
#
# def resetBalloon():
#     # Titik koordinat tempat balon muncul
#     rectBalloon.x = random.randint(100, img.shape[1] - 100)
#     rectBalloon.y = img.shape[0] + 50
#
# start = True
# while start:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             start = False
#             pygame.quit()
#
#     timeRemain = int(totalTime - (time.time() - startTime))
#     if timeRemain < 0:
#         window.fill((255, 255, 255))
#         font = pygame.font.Font(None, 50)
#         textScore = font.render(f'Your Score: {score}', True, (50, 50, 255))
#         textTime = font.render('Time\'s Up', True, (50, 50, 255))
#         textTitle = font.render(f'Pecah Balon', True, (50, 50, 255))
#         window.blit(textTitle, (490, 35))
#         window.blit(textScore, (450, 350))
#         window.blit(textTime, (530, 275))
#
#     else:
#         success, img = cap.read()
#         img = cv2.flip(img, 1)
#         hands, img = detector.findHands(img, flipType=False)
#
#         rectBalloon.y -= speed
#         if rectBalloon.y < 0:
#             resetBalloon()
#             speed += 1
#
#         if hands:
#             hand = hands[0]
#             x, y = hand['lmList'][8][0:2]
#             if rectBalloon.collidepoint(x, y):
#                 resetBalloon()
#                 score += 10
#                 speed += 1
#
#         imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#         imgRGB = np.rot90(imgRGB)
#         frame = pygame.surfarray.make_surface(imgRGB).convert()
#         frame = pygame.transform.flip(frame, True, False)
#         window.blit(frame, (0, 0))
#         window.blit(imgBalloonRed, rectBalloon)
#
#         font = pygame.font.Font(None, 50)
#         textScore = font. render(f'Score: {score}', True, (50, 50, 255))
#         textTime = font.render(f'Time: {timeRemain}', True, (50, 50, 255))
#         textTitle = font.render(f'Pecah Balon', True, (50, 50, 255))
#         window.blit(textTitle, (490, 35))
#         window.blit(textScore, (35, 35))
#         window.blit(textTime, (1000, 35))
#
#     # Update tampilan dan frame rate
#     pygame.display.update()
#     clock.tick(fps)