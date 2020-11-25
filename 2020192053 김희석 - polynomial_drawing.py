import numpy as np
from numpy.polynomial import polynomial as P
import pygame

WHITE = (255, 255, 255)
pad_width = 1024
pad_height = 720
ball_x = 0
ball_y = 0
ball_height = 50
ball_width = 50

def PolyCoefficients(x, coeff):
    deg = len(coeff)-1
    y = 0
    for i in range(deg+1):
        y += coeff[i]*x**i
    return y

def drawObject(obj, x, y):  ##어떤 그림을 등장시키는 것
    global gamepad
    gamepad.blit(obj, (x, y))


def runPro():
    global ball, ball_x, ball_y, gamepad, coeffs
    endpg = False  ##crashed == False -> 게임을 계속 돌려라
    Delta_x = 1
    Delta_y = PolyCoefficients(ball_x+1, coeffs) - PolyCoefficients(ball_x, coeffs)
    while not endpg:
        gamepad.fill(WHITE)

        ball_x += Delta_x
        ball_y += Delta_y

        for event in pygame.event.get():  ##event는 pygame 자체에서 정의해준 event들이 있음 - QUIT, KEYDOWN 등
            if event.type == pygame.QUIT:
                endpg = True

        if ball_y < -pad_height / 2:
            Delta_y = 0
            Delta_x = 0
        elif ball_x > pad_width:
            Delta_y = 0
            Delta_x = 0
        elif ball_x < -pad_width / 2:
            Delta_y = 0
            Delta_x = 0
        elif ball_y > pad_height - ball_height / 2:
            Delta_y = 0
            Delta_x = 0
        else:
            Delta_x = 1
            Delta_y = PolyCoefficients(ball_x+1, coeffs) - PolyCoefficients(ball_x, coeffs)

        drawObject(ball, ball_x, ball_y)
        pygame.display.update()  ##비행기 위치 화면에 업데이트
        clock.tick(90)  ## FPS값 90FPS로 설정

    pygame.quit()  ##게임 종료
    quit()

def initPro():
    global ball, gamepad, clock, coeffs

    pygame.init()
    clock = pygame.time.Clock()
    ball = pygame.image.load('ball1.jpg')
    coeffs = [int(x) for x in input('각 계수를 띄어쓰기로 순서대로 입력하세요: ').split(' ')] ## basis: 0차~deg차 순서
    gamepad = pygame.display.set_mode((pad_width, pad_height))
    pygame.display.set_caption('PolyDisp')
    runPro()

initPro()