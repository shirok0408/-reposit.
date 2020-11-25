import pygame
import random
from time import sleep

global crashcnt, totallife

WHITE = (255, 255, 255)  ##white색 정의
RED = (255, 0, 0)  ##RED 색 정의
pad_width = 949
pad_height = 717
background_width = 949
ast_width = 70
ast_height = 68
aircraft_width = 80
aircraft_height = 45
fireball1_width = 120
fireball2_width = 75
fireball1_height = 50
fireball2_height = 50
purple_height = 100
purple_width = 90
totallife = 0
crashcnt = 0

def drawTotal(cnt):
    global gamepad

    font = pygame.font.SysFont(None, 25)
    text = font.render('total shot: '+str(cnt), True, WHITE)
    gamepad.blit(text, (0,50)) ##목표; 종료하기 전까지 죽어도 누적되는 총점(총 점수) 표시

def drawCount(cnt):
    global gamepad

    font = pygame.font.SysFont(None, 25)
    text = font.render('combo count: '+str(cnt), True, WHITE)
    gamepad.blit(text, (0,25)) ##combo수(샷카운트) 표시

def drawCrash(crashct):
    global gamepad, crashc, totallife
    crashc = totallife - crashct

    font = pygame.font.SysFont(None, 25)
    text = font.render('Life Left: ' + str(crashc), True, WHITE)
    gamepad.blit(text, (0, 0))  ##충돌수 표시

def gameover():
    global gamepad
    dispMessage('GAME OVER')

def textObj(text, font):
    textSurface = font.render(text, True, RED)
    return textSurface, textSurface.get_rect()  ##빨간 텍스트 쓰기


def dispMessage(text):
    global gamepad

    largetext = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = textObj(text, largetext)
    TextRect.center = ((pad_width / 2), (pad_height / 2))
    gamepad.blit(TextSurf, TextRect)
    pygame.display.update()
    sleep(1)
    runGame()  ##글자 위치, 폰트


def crash():
    global gamepad, crashcnt
    crashcnt += 1

def crash1():
    global gamepad, totallife
    if crashcnt >= totallife:
        dispMessage('Crashed!')  ##Crash 텍스트 나타냄


def drawObject(obj, x, y):  ##어떤 그림을 등장시키는 것
    global gamepad
    gamepad.blit(obj, (x, y))


def runGame():
    global gamepad, aircraft, clock, background1, background2, ast, fires, purple, BatShot, purpl, crashcnt, aircraft_width, aircraft_height  ##변수선언(global)

    bullet_xy = []  ##오른쪽으로 가는 총알 위치 담을 list

    x = pad_width * 0.05
    y = pad_height * 0.5  ##초기 위치 정의
    y_change = 0
    x_change = 0
    background1_x = 0
    background2_x = background_width

    ast_x = pad_width
    ast_y = random.randrange(0, pad_height)
    Delta_x = random.randrange(2, 6)
    Delta_y = random.randrange(2, 6)
    r = 0
    boom_count1 = 0
    boom_count2 = 0
    BatShot = False
    PurpleShot = False
    tin=0

    fire_x = pad_width
    fire_y = random.randrange(0, pad_height)
    magnus_x = random.randrange(0, pad_width - purple_width / 2)
    magnus_y = 0
    random.shuffle(fires)
    fire = fires[0]
    random.shuffle(purple)
    magnus_purple = purple[0]
    shotcnt = 0

    crashed = False  ##crashed == False -> 게임을 계속 돌려라
    while not crashed:
        for event in pygame.event.get():  ##event는 pygame 자체에서 정의해준 event들이 있음 - QUIT, KEYDOWN 등
            if event.type == pygame.QUIT:
                crashed = True  ##QUIT에 해당하는 명령이 오면 crashed를 True로 설정 -> loop 탈출

            if event.type == pygame.KEYDOWN:  ## 키 누르기
                if event.key == pygame.K_UP:  ##위 방향키
                    y_change = -5
                if event.key == pygame.K_DOWN:  ##아래 방향키
                    y_change = 5
                if event.key == pygame.K_LEFT:  ##왼쪽 방향키
                    x_change = -5
                if event.key == pygame.K_RIGHT:  ##오른쪽 방향키
                    x_change = 5
                if event.key == pygame.K_LCTRL:
                    bullet_x = x + aircraft_width
                    bullet_y = y + aircraft_height / 2
                    bullet_xy.append([bullet_x, bullet_y])  ##bullet 발사시의 좌표설정 - 비행기 바로 오른쪽 앞
                if event.key == pygame.K_LALT:
                    if shotcnt >= 5:
                        shotcnt -= 5
                        drawObject(boom, ast_x + ast_width / 4, ast_y + ast_height / 4)
                        drawObject(boom, magnus_x + purple_width / 3, magnus_y + purple_height / 3)
                        ast_x = pad_width
                        ast_y = random.randrange(0, pad_height)
                        Delta_x = random.randrange(2, 6)
                        Delta_y = random.randrange(2, 6)
                        fire_x = pad_width
                        fire_y = random.randrange(0, pad_height)
                        magnus_x = random.randrange(0, pad_width - purple_width / 2)
                        magnus_y = 0
                        sleep(0.5)

            if event.type == pygame.KEYUP:  ##키에서 손떼기
                if event.key == pygame.K_UP or pygame.K_DOWN:
                    y_change = 0
                if event.key == pygame.K_RIGHT or pygame.K_LEFT:
                    x_change = 0

        y += y_change
        x += x_change
        if y < -aircraft_height / 2:
            y = -aircraft_height / 2
        elif x > pad_width:
            x = pad_width
        elif x < -aircraft_width / 2:
            x = -aircraft_width / 2
        elif y > pad_height - aircraft_height / 2:
            y = pad_height - aircraft_height / 2  ##비행기가 화면을 넘어가지 않게 설정

        gamepad.fill(WHITE)

        background1_x -= 2  ##배경 움직임 효과
        background2_x -= 2  ##배경 움직임 효과

        ast_x -= Delta_x * (-1) ** r
        ast_y += Delta_y  ##초록운석 다가오는 속도

        if r == 0:
            if ast_x <= 0 or ast_y >= pad_height:  ##맵 끝까지 갔을 경우
                para = random.randrange(-1, 1) ##왼쪽 혹은 오른쪽에서 무작위로 나옴
                if para >= 0:
                    ast_x = pad_width
                    ast_y = random.randrange(0, pad_height)
                    Delta_x = random.randrange(3, 6)
                    Delta_y = random.randrange(2, 5)
                    r = 0
                elif para < 0:
                    ast_x = 0
                    ast_y = random.randrange(0, pad_height)
                    Delta_x = random.randrange(3, 6)
                    Delta_y = random.randrange(2, 5)
                    r = 1

        elif r == 1:
            if ast_x >= pad_width or ast_y >= pad_height:
                para = random.randrange(-1, 1)
                if para >= 0:
                    ast_x = pad_width
                    ast_y = random.randrange(0, pad_height)
                    Delta_x = random.randrange(2, 5)
                    Delta_y = random.randrange(2, 5)
                    r = 0
                elif para < 0:
                    ast_x = 0
                    ast_y = random.randrange(0, pad_height)
                    Delta_x = random.randrange(3, 6)
                    Delta_y = random.randrange(1, 5)
                    r = 1

        if len(bullet_xy) != 0:
            for i, bxy in enumerate(bullet_xy):
                bxy[0] += 15  ##총알 날아가는 속도는 15로 한다
                bullet_xy[i][0] = bxy[0]  ##각 총알의 좌표를 bullet_xy에 갱신한다

                if ast_x + ast_width > bxy[0] > ast_x:
                    if ast_y < bxy[1] < ast_y + ast_height:
                        bullet_xy.remove(bxy)
                        BatShot = True

                if magnus_x + purple_width > bxy[0] > magnus_x:
                    if magnus_y < bxy[1] < magnus_y + purple_height:
                        bullet_xy.remove(bxy)
                        PurpleShot = True

                if bxy[0] > pad_width:
                    try:
                        bullet_xy.remove(bxy)  ##끝까지 갔을 때 총알 제거
                    except:
                        pass

        if fire[1] == None:  ##fire[1]의 fireball을 발사함
            fire_x -= 30  ##fireball이 안쏴졌을 경우 30의 속도로 옴(=그냥 시간지연임)
        else:
            fire_x -= 6  ##fireball이 쏴졌을 경우 6의 속도로 옴

        if fire_x <= 0:  ##맵 왼쪽 끝까지 갔을 경우
            fire_x = pad_width
            fire_y = random.randrange(0, pad_height)  ##맨 오른쪽 어딘가에서 생성됨
            random.shuffle(fires)
            fire = fires[0]  ##랜덤으로 섞고 첫번째를 fire에 넣음 - 만약 None이라면 그냥 발사 안되고 시간만 지날거고 None이 아닌 우리가 append한(뒤에서 할 것) fireball 또는 fireball2라면 발사될것

        if magnus_y >= pad_height:  ##맵 아래 끝까지 갔을 경우
            magnus_y = -purple_height/2
            magnus_x = random.randrange(0, pad_width - purple_width / 2)  ##맨 위 어딘가에서 생성됨
            random.shuffle(fires)
            magnus_purple = fires[0]

        if magnus_purple == 0:
            magnus_y += 20
        else:
            magnus_y += 3

        if ast_x + ast_width > x + aircraft_width / 2 > ast_x:
            if ast_y - aircraft_height / 2 < y < ast_y - aircraft_height / 2 + ast_height:
                crash()
                drawCrash(crashcnt)
                ast_x = pad_width
                ast_y = random.randrange(0, pad_height - ast_height)
                crash1()

        if fire[1] != None:
            if fire[0] == 0:
                fireball_width = fireball1_width
                fireball_height = fireball1_height
            elif fire[0] == 1:
                fireball_width = fireball2_width
                fireball_height = fireball2_height

            if fire_x + fireball_width > x + aircraft_width / 2 > fire_x:
                if fire_y + fireball_height > y + aircraft_height / 2 > fire_y:
                    crash()
                    drawCrash(crashcnt)
                    fire_x = pad_width
                    fire_y = random.randrange(0, pad_height)
                    crash1()

        if magnus_x + purple_width > x + aircraft_width / 2 > magnus_x:
            if magnus_y + purple_height - aircraft_height / 2 > y > magnus_y - aircraft_height / 2:
                crash()
                crash()
                drawCrash(crashcnt)
                magnus_y = 0
                magnus_x = random.randrange(0, pad_width - purple_width / 2)
                crash1()

        if background1_x <= -background_width:
            background1_x = background_width  ##background1 기준으로 맵 두개가 다 지나갔으면 background1부터 새로 시작해야함
        if background2_x <= -background_width:
            background2_x = background_width  ##background2 기준으로 맵 두개가 다 지나갔으면 background2부터 새로 시작해야함

        drawObject(background1, background1_x, 0)
        drawObject(background2, background2_x, 0)

        drawObject(ast, ast_x, ast_y)

        if fire[1] != None:  ##None이 아닐때만 그거에 해당하는 fireball 발사(1이든 2든)
            drawObject(fire[1], fire_x, fire_y)

        if magnus_purple != 0:  ##None이 아닐때만 그거에 해당하는 보라운석 발사
            drawObject(purpl, magnus_x, magnus_y)

        if len(bullet_xy) != 0:
            for bx, by in bullet_xy:
                drawObject(bullet, bx, by)

        if not BatShot:
            drawObject(ast, ast_x, ast_y)
        else:
            drawObject(boom, ast_x+ast_width/4, ast_y+ast_height/4)
            boom_count1 += 1
            if boom_count1 > 5:  ##시간을 끄는 역할을 한다. 5번의 루프동안 boom 표시를 계속 띄울 것이다.
                boom_count1 = 0
                ast_x = pad_width
                ast_y = random.randrange(0, pad_height - ast_height)
                shotcnt += 1
                BatShot = False

        if not PurpleShot:
            drawObject(purpl, magnus_x, magnus_y)
        else:
            drawObject(boom, magnus_x+purple_width/3, magnus_y+purple_height/3)
            boom_count2 += 1
            if boom_count2 > 5:  ##시간을 끄는 역할을 한다. 5번의 루프동안 boom 표시를 계속 띄울 것이다.
                boom_count2 = 0
                magnus_y = 0
                magnus_x = random.randrange(0, pad_width - purple_width / 2)
                shotcnt += 1
                PurpleShot = False

        drawCount(shotcnt) ##목표: shotcnt=5일때마다 폭탄 겟, 폭탄: 사용시 모든 장애물 일시 초기화
        drawCrash(crashcnt)

        drawObject(aircraft, x, y)
        pygame.display.update()  ##비행기 위치 화면에 업데이트
        clock.tick(90)  ## FPS값 90FPS로 설정

    pygame.quit()  ##게임 종료
    quit()


def initGame():
    global gamepad, aircraft, clock, background1, background2, ast, fires, purple, bullet, boom, purpl, crashcnt, totallife

    fires = []
    purple = []
    crashcnt = 0

    pygame.init()
    gamepad = pygame.display.set_mode((pad_width, pad_height))  ##패드 크기 정의
    pygame.display.set_caption('PyPlaneGame')  ##게임창 타이틀 정하기
    aircraft = pygame.image.load('plane.png')
    background1 = pygame.image.load('maxresdefault.jpg')
    background2 = pygame.image.load('maxresdefault.jpg')  ##background1이랑 같은 그림 - 다른 그림 원하면 그냥 다른 그림 넣으면 됨
    ast = pygame.image.load('Magnus_green.gif')
    bullet = pygame.image.load('bullet.png')
    purpl = pygame.image.load('Magnus_purple1.gif')
    boom = pygame.image.load('boom.png')
    purple.append(pygame.image.load('Magnus_purple1.gif'))
    fires.append((0, pygame.image.load('fireball.png')))
    fires.append((1, pygame.image.load('fireball2.png')))  ##fireball에는 두 종류(속도같음) 있음

    for i in range(5):
        fires.append((i + 2, None))  ##계속 append만 되면 확률이 나중에는 1이 될거니까 None도 좀 넣어줌(3개씩)
        purple.append(None)

    clock = pygame.time.Clock()  ##게임의 FPS 설정을 위함
    totallife = int(input("Total Life: ", )) ##Total Life 몇으로 게임할건지 결정
    runGame()  ## 게임 돌리기

initGame()