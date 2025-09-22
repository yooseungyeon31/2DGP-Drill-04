#코파일럿 가능
#커밋로그 점차적으로 꼭 쓰기
from pico2d import *

open_canvas()

#애니메이션1 이미지 로드
character1 = load_image('mario_animation.png')


# 캐릭터 중앙 위치
x, y = 400, 300

frame_width, frame_height = 30, 35
usable_width, left_margin = 350, 7
total_frames = (usable_width // frame_width) - 1
repeat_count = 5

for frame in range(repeat_count):

    for frame in range(total_frames):

        clear_canvas()
        clip_x = left_margin + frame * frame_width
        character1.clip_draw(clip_x, 0, frame_width, frame_height, x, y, frame_width*3, frame_height*3)
        update_canvas()
        delay(0.1)







close_canvas()
