import random


numberOfStreaks = 0

for experimentNumber in range(10000):
  experiment = []

  for i in range(99):
    experiment.append(random.randint(0,1))
  
  counter = 0

  for i, n in enumerate(experiment):
    if i == 0: # Skip first iteration 
      continue
    if counter == 6:
      numberOfStreaks += 1
    if n == experiment[i - 1]:
      counter += 1
    else:
      counter = 0
            

print(f"Chance of streak: {numberOfStreaks / (100*10000)}")