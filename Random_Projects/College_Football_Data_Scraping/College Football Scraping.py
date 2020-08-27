import time

import pandas as pd
import requests
from bs4 import BeautifulSoup
from lxml import html


def schedule_stats(team_name):
    r = requests.get("https://www.sports-reference.com/cfb/schools/" + team_name + "/2017-schedule.html")
    tree = html.fromstring(r.content)
    data_trs = tree.xpath('//*[@id="schedule"]/tbody/tr')
    data2 = []
    col_names = ['Date', 'Time', 'Day', 'School', 'Site', 'Opponent', 'Conference', 'Result', 'Points',
                 'Opponent Points',
                 'Win', 'Loss', 'Streak', 'TV', 'Notes']

    for tr in data_trs:
        tds = tr.findall('td')
        data = [td.text_content().strip() for td in tds]
        data2.append(data)

    schedule2 = pd.DataFrame(data2)

    schedule2.columns = col_names
    del schedule2['Date'], schedule2['Time'], schedule2['Day'], schedule2['School'], schedule2['Conference'], \
        schedule2['Win'], schedule2['Loss'], schedule2['Streak'], schedule2['TV'], schedule2['Notes']
    schedule2['Site'] = schedule2['Site'].replace(['@'], 'Away')
    schedule2['Site'] = schedule2['Site'].replace(['N'], 'Neutral')
    for i in range(schedule2.shape[0]):
        if schedule2.iloc[i, 0] == 'Neutral':
            pass
        elif schedule2.iloc[i, 0] == 'Away':
            pass
        else:
            schedule2.ix[i, 0] = 'Home'

    for i in range(schedule2.shape[0]):
        if schedule2.iloc[i, 2] == 'W':
            pass
        elif schedule2.iloc[i, 2] == 'L':
            pass
        else:
            location_of_next_game = schedule2.iloc[i, 0]
            if location_of_next_game == 'Away':
                location_of_next_game = 'Road'
            if location_of_next_game == 'Neutral':
                print('This game will be at a neutral site')
                location_of_next_game = 'Home'
            break

    schedule2["Score"] = schedule2["Points"] + '-' + schedule2["Opponent Points"]

    del schedule2['Points'], schedule2['Opponent Points']
    schedule2.columns.name = 'Schedule'
    return schedule2, location_of_next_game
    return schedule2


# Offensive Stats
def offensive_stats(team_name, location):
    r = requests.get("https://www.sports-reference.com/cfb/schools/" + team_name + "/2017/splits/")
    tree = html.fromstring(r.content)
    data_trs = tree.xpath('//*[@id="all_offense"]/tbody/tr')
    data2 = []
    for tr in data_trs:
        tds = tr.findall('td')
        data = [td.text_content().strip() for td in tds]
        data2.append(data)
    offense2 = pd.DataFrame(data2)
    col_names = ['Values', 'Games', 'Wins', 'Losses', 'Passing Completions', 'Passing Attempts', 'Percentage',
                 'Passing Yards', 'Passing TDs', 'Rushing Attempts', 'Rushing Yards', 'Average Rush', 'Rushing TDs',
                 'Plays per Game', 'Yards per Game', 'Yards per Play', 'Passing First Downs', 'Rushing First Downs',
                 'First Downs by Penalty', 'Total First Downs', 'Number of Penalties', 'Penalty Yards', 'Fumbles',
                 'Interceptions', 'Total Turnovers']

    offense2.columns = col_names

    row_names = []
    for i in range(offense2.shape[0]):
        if i == 0:
            row_names.append(1)
        elif offense2.iloc[i, 0] == location:
            row_names.append(1)
        else:
            row_names.append(0)
    offense2 = offense2.set_index([row_names])
    offense2 = offense2.ix[1]
    offense2.iloc[0, 0] = 'Overall'
    offense2['Record'] = offense2['Wins'] + '-' + offense2['Losses']
    offense2['Pass Comp/Att'] = offense2['Passing Completions'] + '/' + offense2['Passing Attempts']
    offense2['Pass Yards/TDs'] = offense2['Passing Yards'] + '/' + offense2['Passing TDs']
    offense2['Rush Attempts/YPA'] = offense2['Rushing Attempts'] + '/' + offense2['Average Rush']
    offense2['Rush Yards/TDs'] = offense2['Rushing Yards'] + '/' + offense2['Rushing TDs']
    offense2['Game Yards/Play Yards'] = offense2['Yards per Game'] + '/' + offense2['Yards per Play']
    offense2['First Downs'] = offense2['Total First Downs']
    offense2['Penalties/Yards'] = offense2['Number of Penalties'] + '/' + offense2['Penalty Yards']
    offense2['Turnovers/Game'] = offense2['Total Turnovers']

    for name in col_names:
        del offense2[name]

    offense2 = offense2.transpose()
    offense2.columns = ['Overall', location]
    offense2.columns.name = 'Offense'
    return offense2


# Defensive Stata
def defensive_stats(team_name, location):
    r = requests.get("https://www.sports-reference.com/cfb/schools/" + team_name + "/2017/splits/")
    tree = html.fromstring(r.content)
    data_trs = tree.xpath('//*[@id="all_defense"]/tbody/tr')
    data2 = []
    for tr in data_trs:
        tds = tr.findall('td')
        data = [td.text_content().strip() for td in tds]
        data2.append(data)
    defense2 = pd.DataFrame(data2)
    col_names = ['Values', 'Games', 'Wins', 'Losses', 'Passing Completions', 'Passing Attempts', 'Percentage',
                 'Passing Yards', 'Passing TDs', 'Rushing Attempts', 'Rushing Yards', 'Average Rush', 'Rushing TDs',
                 'Plays per Game', 'Yards per Game', 'Yards per Play', 'Passing First Downs', 'Rushing First Downs',
                 'First Downs by Penalty', 'Total First Downs', 'Number of Penalties', 'Penalty Yards', 'Fumbles',
                 'Interceptions', 'Total Turnovers']
    defense2.columns = col_names

    row_names = []
    for i in range(defense2.shape[0]):
        if i == 0:
            row_names.append(1)
        elif defense2.iloc[i, 0] == location:
            row_names.append(1)
        else:
            row_names.append(0)
    defense2 = defense2.set_index([row_names])
    defense2 = defense2.ix[1]
    defense2.iloc[0, 0] = 'Overall'
    defense2['Record'] = defense2['Wins'] + '-' + defense2['Losses']
    defense2['Pass Comp/Att'] = defense2['Passing Completions'] + '/' + defense2['Passing Attempts']
    defense2['Pass Yards/TDs'] = defense2['Passing Yards'] + '/' + defense2['Passing TDs']
    defense2['Rush Attempts/YPA'] = defense2['Rushing Attempts'] + '/' + defense2['Average Rush']
    defense2['Rush Yards/TDs'] = defense2['Rushing Yards'] + '/' + defense2['Rushing TDs']
    defense2['Game Yards/Play Yards'] = defense2['Yards per Game'] + '/' + defense2['Yards per Play']
    defense2['First Downs'] = defense2['Total First Downs']
    defense2['Penalties/Yards'] = defense2['Number of Penalties'] + '/' + defense2['Penalty Yards']
    defense2['Turnovers/Game'] = defense2['Total Turnovers']

    for name in col_names:
        del defense2[name]

    defense2 = defense2.transpose()
    defense2.columns = ['Overall', location]
    defense2.columns.name = 'Defense'
    return defense2


# Other Stats
def get_other_stats(team_name):
    page = requests.get("https://www.sports-reference.com/cfb/schools/" + team_name + "/2017/splits/")
    soup = BeautifulSoup(page.text, 'html.parser')
    # print(soup.prettify())
    for i in range(len(soup.find_all('p'))):
        # print(soup.find_all('p')[i].get_text())
        phrase = soup.find_all('p')[i].get_text()
        if phrase[0:8] == 'Points/G':
            points_per_game = phrase[10:14]
        if phrase[0:9] == 'Opp Pts/G':
            opp_ppg = phrase[11:15]
        if i == 3:
            if phrase[0:4] == 'Rank':
                rank = phrase[6:10]
            else:
                rank = 'none'

    return points_per_game, opp_ppg, rank


# Print Stats
t0 = time.time()
matchup = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
team1 = ['southern-california', 'florida-atlantic', 'florida-international', 'toledo', 'new-mexico-state',
         'central-florida', 'oklahoma', 'auburn', 'boise-state', 'clemson', 'ohio-state', 'arkansas-state']
team2 = ['stanford', 'north-texas', 'massachusetts', 'akron', 'south-alabama', 'memphis', 'texas-christian',
         'georgia', 'fresno-state', 'miami-fl', 'wisconsin', 'troy']
writer = pd.ExcelWriter(r'/Users/jackfrancis/OneDrive/CollegeFootballMatchups_1128.xls')

for i in range(len(matchup)):
    matchup_number = i + 1
    first_team = team1[i]
    schedule, location = schedule_stats(first_team)
    defense = defensive_stats(first_team, location)
    offense = offensive_stats(first_team, location)
    points_per_game, opp_ppg, rank = get_other_stats(first_team)

    sheet_name = 'Matchup %s' % (matchup_number)

    schedule.to_excel(writer, sheet_name, startrow=5)
    offense.to_excel(writer, sheet_name, startrow=21)
    defense.to_excel(writer, sheet_name, startrow=34)

    worksheet = writer.sheets[sheet_name]
    worksheet.write(0, 1, '%s' % first_team)
    worksheet.write(1, 1, '%s is currently ranked %s' % (first_team, rank))
    worksheet.write(2, 1, '%s scores %s points per game' % (first_team, points_per_game))
    worksheet.write(3, 1, '%s gives up %s points per game' % (first_team, opp_ppg))
    worksheet.write(19, 1, 'Offensive Stats')
    worksheet.write(32, 1, 'Defensive Stats')

    second_team = team2[i]

    schedule, location = schedule_stats(second_team)
    defense = defensive_stats(second_team, location)
    offense = offensive_stats(second_team, location)
    points_per_game, opp_ppg, rank = get_other_stats(second_team)

    sheet_name = 'Matchup %s' % (matchup_number)

    schedule.to_excel(writer, sheet_name, startrow=5, startcol=7)
    offense.to_excel(writer, sheet_name, startrow=21, startcol=7)
    defense.to_excel(writer, sheet_name, startrow=34, startcol=7)

    worksheet = writer.sheets[sheet_name]
    worksheet.write(0, 8, '%s' % second_team)
    worksheet.write(1, 8, '%s is currently ranked %s' % (second_team, rank))
    worksheet.write(2, 8, '%s scores %s points per game' % (second_team, points_per_game))
    worksheet.write(3, 8, '%s gives up %s points per game' % (second_team, opp_ppg))
    worksheet.write(19, 8, 'Offensive Stats')
    worksheet.write(32, 8, 'Defensive Stats')

    print('Finished with matchup %s' % (i + 1))

writer.save()
t1 = time.time()

print(t1 - t0)
