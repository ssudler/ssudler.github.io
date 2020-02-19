import os
from colorthief import ColorThief
from natsort import natsorted

player_total_data = open('/Users/ssudler/Projects/dataviz/playertotaldata.txt', 'w')
player_colors = []

for dir in os.listdir('/Users/ssudler/Projects/dataviz/teams'):
    if dir != '.DS_Store':
        print(dir)
        os.chdir('/Users/ssudler/Projects/dataviz/teams/' + dir)
        print(os.getcwd())
        team_salaries = open(os.getcwd() + '/' + dir + 'playerdata.txt', 'r')
        team_salaries_arr = team_salaries.read().split(',')
        print('Salaries: ' + str(team_salaries_arr))

        for img in natsorted(os.listdir(os.getcwd())):
            if '.txt' not in img:
                print(img)
                color_thief = ColorThief(os.getcwd() + '/' + img)
                color_rgb = str(color_thief.get_color(quality=1)).replace(',', '@').replace(' ', '')
                print('Dominant Color: ' + color_rgb)
                player_salary = team_salaries_arr[int(img.split('_')[0]) - 1]
                player_colors.append({'id': img, 'rgb': color_rgb, 'avgcolor': int(sum(color_thief.get_color(quality=1))), 'salary': player_salary})

player_total_data.write(str(player_colors))