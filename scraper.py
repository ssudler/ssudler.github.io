from colorthief import ColorThief
import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import os

baseUrl = "http://www.espn.com/nba/players"
response = requests.get(baseUrl)
parsedHtml = BeautifulSoup(response.text, 'html.parser')
for link in parsedHtml.select('div', id='my-players-table'):
    if link.find('a'):
        href = link.find('a')['href']
        if href[0:4] == '/nba' and href != '/nba/':
            print(href)

            teamUrl = 'https://espn.com' + href
            teamResponse = requests.get(teamUrl)
            teamParsedHtml = BeautifulSoup(teamResponse.text, 'html.parser')

            dir_name = href.split('=')[1]
            os.mkdir(os.path.join('/Users/ssudler/Projects/dataviz/teams', dir_name))

            img_count = 0

            for figure in teamParsedHtml.select('figure'):
                if figure.find('img')['alt'][0:5] == 'https':
                    if len(figure.find('img')['alt'].split('/')) == 9:
                        img_count += 1
                        img_id = figure.find('img')['alt'].split('/')[8]
                        img_url = 'https://a.espncdn.com/combiner/i?img=/i/headshots/nba/players/full/' + img_id + '&h=45&w=110&scale=crop'
                        print(img_url)
                        urllib.request.urlretrieve(img_url, '/Users/ssudler/Projects/dataviz/teams/' + dir_name + '/' + str(img_count) + '_' + dir_name.upper() + 'headshot' + '.png')
                        print('Downloaded image')

            player_data = open('/Users/ssudler/Projects/dataviz/teams/' + dir_name + '/' + dir_name.upper() + 'playerdata.txt', 'w')
            temp_data = []
            for tr in teamParsedHtml.select('tbody', {'class': 'Table__TBODY'}):
                for span in tr.findAll('span'):
                    if len(span.text) > 0:
                        if span.text[0] == '$' or span.text[0] == '-':
                            print('salary: ' + span.text)
                            temp_data.append(span.text.replace(',', ''))

            stringified_data = str(temp_data).replace('$', '').replace("'", '').replace('[', '').replace(']', '').replace(' ', '')

            player_data.write(stringified_data)