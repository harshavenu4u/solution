bookcost=24.95
discount=40
shipping=0.75
totalcopies=60
totalcost=bookcost*(3+totalcopies-1*shipping)
disc=(discount/totalcost)*100
print(disc)
