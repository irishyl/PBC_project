player_info = input()
print(player_info)
if player_info != 'RECORDSTOP':
    player_info = player_info.split(',')
    team = player_info[0]
    player = player_info[1]
    season = player_info[2]
    ab = player_info[3]
    hit = player_info[4]
    print(player_info)
    records.append([team, int(player), int(season), int(ab), int(hit)])
    else:
        break