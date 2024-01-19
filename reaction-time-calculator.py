import time, random, csv
from termcolor import colored
#text for introduction
print(colored("Hello!", "cyan"))
time.sleep(1.5)
print(colored("We are testing your reaction time for 30 trials.", "cyan"))
time.sleep(3)
print(colored("Press ENTER key as fast as you can, when you see the word ", "cyan"))
time.sleep(3)
print(colored("PIKACHU", "yellow"))
time.sleep(3)
get_ready = raw_input(colored("Press ENTER key when you are ready to start!", "cyan"))
print(colored("Ready? Here we go!\n", "cyan"))
time.sleep(random.randint(2, 3))

#record user's reaction time
res =[]
for i in range(30): 
    print(colored("PIKACHU", "yellow"))
    start_time = time.time()
    user_input = raw_input() 
    end_time = time.time()
    react_time = end_time-start_time
    print(f"Trial {i+1} Reaction Time is {int(react_time*1000)} milliseconds.\n")
    res.append(int(react_time*1000))
    time.sleep(1)
    if i+1 !=30:
        print(colored("Get ready for the next trial!\n", "cyan"))
        time.sleep(random.randint(1,2))

time.sleep(1)
#summary of the user's reaction time    
print(f"Your average reaction time is {int(sum(res) / len(res))} milliseconds.")

#store the file into csv in unit of milliseconds
with open('reaction_time_result.csv', 'w') as f: 
    
    write = csv.writer(f) 
    write.writerow(res)

time.sleep(1)
print(colored("Your reaction time has been recorded.", "cyan"))
time.sleep(1)
print(colored("Thank you very much for your participation!", "cyan"))
