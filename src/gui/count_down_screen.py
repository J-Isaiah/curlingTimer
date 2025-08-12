import pygame


def setup_timer(screen,time_left, total_time, is_set_up_time,h,w):
    if is_set_up_time:
        screen.fill((164,160,112))
        bar_w = w * .65
        bar_h = h * .14

        screen.fill((164, 160, 112))
        progress_bar = pygame.Rect(10, 10, (w- bar_w) / 2, (h- bar_h) / 2)

        pygame





def draw_rocks():
    pass

def draw_play_screen(screen, current_end, is_set_up_time: bool, time_left_in_set_up, height,width):
    if is_set_up_time:
        setup_timer(screen=screen,time_left=20,total_time=60, is_set_up_time=is_set_up_time,h=height,w=width)










if __name__ == '__main__':
    pygame.init()
    clock = pygame.time.Clock()

    info = pygame.display.Info()
    screen_width = info.current_w
    screen_height = info.current_h

    screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)


    current_test_end = 3
    is_set_up = True
    while True:
        draw_play_screen(screen,current_test_end,is_set_up,time_left_in_set_up=100,height=screen_height,width=screen_width)

        pygame.display.flip()
        clock.tick(30)