#코파일럿 가능
#커밋로그 점차적으로 꼭 쓰기
from pico2d import *

open_canvas()

#애니메이션1 이미지 로드
character1 = load_image('mario_animation.png')
character2 = load_image('mario_animation2.png')
character3 = load_image('mario_animation3.png')
character4 = load_image('mario_animation4.png')


# 캐릭터 중앙 위치
x, y = 400, 300

character_data = [
    {'image': character1, 'frame_width': 30, 'frame_height': 35, 'left_margin': 7, 'usable_width': 350},
    {'image': character2, 'frame_width': 32, 'frame_height': 36, 'left_margin': 5, 'usable_width': 360},
    {'image': character3, 'frame_width': 36, 'frame_height': 41, 'left_margin': 1, 'usable_width': 287},
    {'image': character4, 'frame_width': 29, 'frame_height': 35, 'left_margin': 1, 'usable_width': 222}
]

#반복 횟수
repeat_count = 5

def animate_character(data, repeat=1):
    total_frames = (data['usable_width'] // data['frame_width']) - 1

    for frame in range(repeat):
        for frame in range(total_frames):
            clear_canvas()
            clip_x = data['left_margin'] + frame * data['frame_width']
            data['image'].clip_draw(clip_x, 0, data['frame_width'], data['frame_height'],
                                    x, y, data['frame_width'] * 7.5, data['frame_height'] * 7.5)
            update_canvas()
            delay(0.1)

while True:
    for data in character_data:
        animate_character(data, repeat=repeat_count)
        delay(1)




close_canvas()
