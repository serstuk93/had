import pygame
import random
import sys

from config import config


def update_position(snake, direction, step):
    if direction == "UP":
        snake = [snake[0], snake[1] - step]
    # snake = [round(snake[0] / 10) * 10, (round(snake[1] / 10) * 10)-step]
    if direction == "DOWN":
        snake = [snake[0], snake[1] + step]
    #  snake = [round(snake[0] / 10) * 10, (round(snake[1] / 10) * 10)+step]
    if direction == "LEFT":
        snake = [snake[0] - step, snake[1]]
    #  snake = [int(round((snake[0]-step) / 10) * 10), (round((snake[1] / 10) * 10))]
    if direction == "RIGHT":
        snake = [snake[0] + step, snake[1]]
    return snake


def update_direction(direction, keys):
    if keys[pygame.K_LEFT]:
        return "LEFT" if direction != "RIGHT" else direction
    if keys[pygame.K_RIGHT]:
        return "RIGHT" if direction != "LEFT" else direction
    if keys[pygame.K_UP]:
        return "UP" if direction != "DOWN" else direction
    if keys[pygame.K_DOWN]:
        return "DOWN" if direction != "UP" else direction
    return direction


def is_out(snake, game_res, step ,direction ):
    if immortality==True and (new_position[0] < 0 or new_position[1] < 0 or new_position[0] > game_res[0] - config.SNAKE_SIZE or new_position[1] > game_res[
        1] - config.SNAKE_SIZE or (new_position[0] <= score_text.get_size()[0]+15 and new_position[1] <= score_text.get_size()[1])):
        if direction=="LEFT":
            snake = [config.GAME_RES[0]- step, snake[1]]
        if direction=="RIGHT":
            snake = [0+ step, snake[1]]
        if direction == "UP":
            snake = [snake[0], config.GAME_RES[1] - step]
        if direction=="DOWN":
            snake = [snake[0], 0 + step]

        return snake
    if new_position[0] < 0 or new_position[1] < 0 or new_position[0] > game_res[0] - config.SNAKE_SIZE or new_position[1] > game_res[
        1] - config.SNAKE_SIZE or (new_position[0] <= score_text.get_size()[0]+15 and new_position[1] <= score_text.get_size()[1]):
        return True
    else:
        return False


def end_game(window):
    print("GAME OVER")
    window.fill(config.BACKGROUND_COLOR)
    pygame.quit()
    sys.exit()

def generate_apple(game_res, snake_size):
    while True:
        tt= False
        x = random.choice(range(0, game_res[0] - snake_size + 1, snake_size))
        y = random.choice(range(0, game_res[1] - snake_size + 1, snake_size))
        if y <= score_text.get_size()[1]+5:
            x = random.choice(range(round((score_text.get_size()[0]+15)/10)*10, game_res[0] - snake_size + 1, snake_size))
        for part in snake:
            if [x,y] == part:
                tt=True
        if tt == False:
            return [x, y]


def generate_multi_apple(game_res, snake_size):
    while True:
        tt = False
        x = random.choice(range(0, game_res[0] - snake_size + 1, snake_size))
        y = random.choice(range(0, game_res[1] - snake_size + 1, snake_size))
        if y <= score_text.get_size()[1]+5:
            x = random.choice(range(round((score_text.get_size()[0]+15)/10)*10, game_res[0] - snake_size + 1, snake_size))
        for part in snake:
            if [x, y] == part:
                tt = True
        if tt == False:
            return [x, y]

def generate_immortal_apple(game_res, snake_size):
    while True:
        tt = False
        x = random.choice(range(0, game_res[0] - snake_size + 1, snake_size))
        y = random.choice(range(0, game_res[1] - snake_size + 1, snake_size))
        if y <= score_text.get_size()[1]+5:
            x = random.choice(range(round((score_text.get_size()[0]+15)/10)*10, game_res[0] - snake_size + 1, snake_size))
        for part in snake:
            if [x, y] == part:
                tt = True
        if tt == False:
            return [x, y]

def is_collision(snake_head, apple):
    if snake_head[0] == apple[0] and snake_head[1] == apple[1]:
        return True
    return False

def own_collision(snake_head, snake):
    if snake_head in snake:
        if immortality==True:
            return False
        return True
    return False


if __name__ == "__main__":
    pygame.init()
    clock = pygame.time.Clock()
    soundObj = pygame.mixer.Sound('kim-lightyear-legends-109307.mp3')
    soundObj.play(loops = -1)
    pygame.display.set_caption('Super Hadík')
    Icon = pygame.image.load('pythonik2.jpg')
    endimage = pygame.image.load("pythonik2.jpg")
    pygame.display.set_icon(Icon)
    window = pygame.display.set_mode(config.GAME_RES)
    snake = [[config.GAME_RES[0] // 2, config.GAME_RES[1] // 2]]
    direction = "UP"

    running = True
    score=0
    game_font = pygame.font.SysFont("comicsans", 30)
    score_text = game_font.render(f"Score {score}", True, (255, 255, 255))
    pygame.draw.rect(window, config.APPLE_COLOR,
                     pygame.Rect(0, 0, score_text.get_size()[0]+10, score_text.get_size()[1]+5), 3)
    apple = generate_apple(config.GAME_RES, config.SNAKE_SIZE)
    immortal_apple = None
    multi_apple = None
    multiply=False
    immortality=False
    multiplier=0

    counter=0
    bonus_ticker=0
    time_delay = 1000
    timer_event = pygame.USEREVENT + 1
    timer_event_immortal_duration = pygame.USEREVENT + 1
    timer_event_multi_duration = pygame.USEREVENT + 1
    counterdurationimortal = 0
    counterdurationmulti = 0
    pygame.time.set_timer(timer_event, time_delay)
    font = pygame.font.SysFont(None, 100)
    text = font.render(str(counter), True, (0, 128, 0))

    while True:

        score_text = game_font.render(f"skóre {score}", True, (255, 255, 255))
        pygame.draw.rect(window, config.APPLE_COLOR,
                         pygame.Rect(0,0, score_text.get_size()[0] + 15, score_text.get_size()[1] + 5), 3)
        window.blit(score_text, (5, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if (event.type == pygame.KEYDOWN and running==False):
                running = True
                snake = [[config.GAME_RES[0] // 2, config.GAME_RES[1] // 2]]
                pygame.mixer.unpause()
                new_position = update_position(snake[0], direction, config.SNAKE_SIZE)
                apple = generate_apple(config.GAME_RES, config.SNAKE_SIZE)
                multi_apple= None
                immortal_apple= None
                direction = "UP"
                score=0


            elif event.type == timer_event and immortality==True:
                counter += 1
                text = font.render(str(counter), True, (0, 128, 0))
                print(counter)
                if counter >=10:
                    immortality = False
                    counter = 0
                    config.COLOR_SNAKE = config.COLOR_SNAKE_BASIC

            if immortal_apple is not None:
                if event.type == timer_event_immortal_duration:
                    counterdurationimortal += 1
                if counterdurationimortal >= 4:
                    immortality = False
                    immortal_apple = None
                    counterdurationimortal = 0

            if multi_apple is not None:
                if event.type == timer_event_multi_duration:
                    counterdurationmulti += 1

                if counterdurationmulti >= 4:
                    multiply = False
                    multi_apple = None
                    counterdurationmulti = 0







        if running:
            ms_frame = clock.tick(config.GAME_FPS)
            move_per_frame = config.MOVE_PER_SECOND * ms_frame / 1000

            keys = pygame.key.get_pressed()
            direction = update_direction(direction, keys)

            new_position = update_position(snake[0], direction, config.SNAKE_SIZE)

            bonus_ticker = random.choice(range(0, 100))

            if multi_apple is None and bonus_ticker == 50:
                multi_apple = generate_multi_apple(config.GAME_RES, config.SNAKE_SIZE)
            if immortal_apple is None and bonus_ticker == 10:
                immortal_apple = generate_immortal_apple(config.GAME_RES, config.SNAKE_SIZE)

            if multi_apple is not None:
                pygame.draw.rect(window, config.IMMORTAL_APPLE_COLOR,
                                 pygame.Rect(multi_apple[0], multi_apple[1], config.SNAKE_SIZE, config.SNAKE_SIZE))
                if is_collision(snake[0], multi_apple):
                    print("multiCollision")
                    multiply=True
                    score += 3
                    multi_apple = None
            if immortal_apple is not None:
                pygame.draw.rect(window, config.MULTI_APPLE_COLOR,
                                 pygame.Rect(immortal_apple[0], immortal_apple[1], config.SNAKE_SIZE, config.SNAKE_SIZE))

                if is_collision(snake[0], immortal_apple):
                    print("immortalCollision")
                    score += 1
                    immortal_apple = None
                    config.COLOR_SNAKE= pygame.Color(218,165,32)
                    immortality=True
                    counter=0




            if own_collision(new_position, snake):
               running = False

            snake.insert(0, new_position)

            if is_collision(snake[0], apple):
                print("Collision")
                apple = generate_apple(config.GAME_RES, config.SNAKE_SIZE)
                score += 1
            elif multiply==True:
                if multiplier <=1:
                    multiplier+=1
                else:
                    multiply=False
                    multiplier=0
            else:
                snake.pop()

            if is_out(new_position, config.GAME_RES,config.SNAKE_SIZE,direction) is True:
                running=False
             #   end_game(window)
            check_list = isinstance(is_out(new_position, config.GAME_RES,config.SNAKE_SIZE,direction), list)
            if check_list==True :
                new_position = is_out(new_position, config.GAME_RES,config.SNAKE_SIZE,direction)
                snake.insert(0, new_position)
                snake.pop()


            for part in snake:
                pygame.draw.rect(window, config.COLOR_SNAKE,
                                 pygame.Rect(part[0], part[1], config.SNAKE_SIZE, config.SNAKE_SIZE))
            pygame.draw.rect(window, config.APPLE_COLOR,
                             pygame.Rect(apple[0], apple[1], config.SNAKE_SIZE, config.SNAKE_SIZE))
        if not running:
            pygame.mixer.pause()
            window.blit(endimage, (0, 0))
            window.blit(score_text, (5, 0))
            end_text = game_font.render(f"Haha, nevies hrat?"
                                        , True, (255, 255, 255))

            window.blit(end_text, ((config.GAME_RES[0]/2 - int(end_text.get_width() / 2)),
                                   (config.GAME_RES[1]/2 - int(end_text.get_size()[1] / 2))))

        pygame.display.update()
        window.fill(config.BACKGROUND_COLOR)
        clock.tick(config.GAME_FPS)
