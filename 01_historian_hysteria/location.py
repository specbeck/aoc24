filename = "input.txt"

contents = []

with open(filename) as file:
    for line in file:
        contents.append(line.split("   "))
        #team1.append([ int(id[0]) for id in line.split("   ")])
        #team2.append([ int(id.strip("\n")) for id in [ id[1] for id in line.split("   ") ] ])

team1 = sorted([ int(id[0]) for id in contents ])
team2 = sorted([ int(id[1].strip("\n")) for id in contents])

result = [ abs(id1 - id2) for id1, id2 in zip(team1, team2) ]

print(f"Total distance between the lists is {sum(result)}")

sim = []

for i in range(len(team1)):
    sim.append(sum( 1 for n in team2 if team1[i] == n))


sim_score = 0
for i1, i2 in zip(team1, sim):
    sim_score += i1*i2
#sim_score = [ k * v for k, v in sim.items() ]

print(f"Similarity scores give out {sim_score}")
#print(team1, team2)
