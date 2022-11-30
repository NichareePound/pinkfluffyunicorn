football_team  = []

#append 11 players 
for i in range(11):
    name = input("Add a player to the football team: ")
    football_team.append(name)
print(football_team)  

repeat = 'Y'
while repeat == 'Y' : 
    edit = int(input("which player do you want to change?"))
    football_team[edit-1] = input("Edit the new player: ")
    print(football_team)

    delete = int(input("which player do you want to delete?: "))
    del football_team[delete-1]
    print(football_team)

    repeat("do you want to edsit or delete the name (Y/N) ")






 

