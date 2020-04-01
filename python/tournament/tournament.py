# results = [
#             "Allegoric Alaskans;Blithering Badgers;win",
#             "Blithering Badgers;Courageous Californians;win",
#             "Courageous Californians;Allegoric Alaskans;loss",
#         ]
def tally(rows):
    teams={}
    for row in rows:
        team=row.split(';')
        result=team[2]
        addToDict(team, teams)
        
        teams[team[0]][0]+=1
        teams[team[1]][0]+=1
        if result=='win':
            #Team 1
            teams[team[0]][1]+=1
            teams[team[0]][4]+=3

            #Team 2
            teams[team[1]][3]+=1

        elif result=='loss':
            #Team 1
            teams[team[0]][3]+=1

            #Team 2
            teams[team[1]][1]+=1
            teams[team[1]][4]+=3
        else:
            #Team 1
            teams[team[0]][2]+=1
            teams[team[0]][4]+=1

            #Team 2
            teams[team[1]][2]+=1
            teams[team[1]][4]+=1


    table=printDict(teams)
    return table
def addToDict(team, teams):
    for i in range(2):
        if team[i] not in teams:
            teams[team[i]]=[0,0,0,0,0]
# table = [
#             "Team                           | MP |  W |  D |  L |  P",
#             "Allegoric Alaskans             |  2 |  1 |  0 |  1 |  3",
#             "Blithering Badgers             |  2 |  1 |  0 |  1 |  3",
#         ]
#31
def printDict(teams):
    table=["Team                           | MP |  W |  D |  L |  P"]
    for key in teams:
        temp=key
        spaces=31-len(key)
        temp+=' '*spaces +'|  '
        
        for i in range(5):
            temp+=str(teams[key][i])+' |  '
        table.append(temp[:-4])
    return table






results =["Allegoric Alaskans;Blithering Badgers;loss",
            "Devastating Donkeys;Allegoric Alaskans;loss",
            "Courageous Californians;Blithering Badgers;draw",
            "Allegoric Alaskans;Courageous Californians;win"]
table=tally(results)
for t in table:
    print(t)







