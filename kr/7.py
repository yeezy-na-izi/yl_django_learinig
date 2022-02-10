class Team:
    def __init__(self, name, city):
        self.name = name
        self.city = city
        self.players = []

    def __str__(self):
        return self.name

    def add(self, player):
        self.players.append(player)

    def remove(self, player):
        self.players.remove(player)


class Player:
    def __init__(self, name, team):
        self.name = name
        self.team = team

    def __str__(self):
        return self.name

    def __eq__(self, other):
        return self.name == other.name


count_1, count_2 = [int(i) for i in input().split()]
teams = dict()
players = dict()

for i in range(count_1):
    query = input().split()
    teamName = query[0]
    teamCity = query[1]
    playerNames = query[2:]

    team = Team(teamName, teamCity)
    for playerName in playerNames:
        player = Player(playerName, team)
        players[playerName] = player
        team.add(player)
    teams[teamName] = team

for i in range(count_2):
    query = input().split()
    playerName = query[0]

    if len(query) == 1:
        player = players.pop(playerName)
        player.team.remove(player)

    elif len(query) == 2:
        newTeam = teams[query[1]]

        player = Player(playerName, newTeam)
        players[playerName] = player
        newTeam.add(player)

    else:
        transferedPlayer = players[playerName]
        oldTeam = teams[query[1]]
        newTeam = teams[query[2]]

        oldTeam.remove(transferedPlayer)
        newTeam.add(transferedPlayer)
        transferedPlayer.team = newTeam

ans = set()
for i in teams.values():
    if len(i.players) >= 5:
        ans.add(i.city)

print(*sorted(ans), sep='\n')
