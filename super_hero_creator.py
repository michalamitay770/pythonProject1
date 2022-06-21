import json
import os
import sys
import random
import datetime
import time

dir = sys.argv[1]
number = int(sys.argv[2])

names = ["Spiderman", "WonderWoman", "Batman", "Thor", "CaptainAmerica", "HalJordan", "SuperMan", "Deadpoll", "BarryAllen", "InvisibleWoman", "MotherOfDragons", "Wolverine", "IronMan", "Supergirl", "HarryPotter" ]
catchphrases = ["Your'e a wizard harry", "i say hello hello hello", "nyan nyan nyan nyan nyan nyan nyan nyan nyan nyan nyan nyan nyan nyan nyan", "You killed my father . Prepare to die", "You know nothing jon snow", "dracarys"]

for i in range(1, number + 1):
    rand = random.getrandbits(30)
    current_path = os.path.join(dir, f'SuperHero{rand}.json')
    current_log = os.path.join(dir, f'SuperHero{rand}.log')
    print(f"populating file {current_path}")
    dic = {"id": i,
           "name": random.choice(names),
           "DateBecomingSuperHero": datetime.datetime.now().isoformat(),
           "Catchphrase": random.choice(catchphrases),
           "IsEvil": random.choice([True, False])}
    if not os.path.isdir(dir):
        os.mkdir(dir)
    with open(current_path, 'w') as outfile:
        json.dump(dic, outfile)
    with open(current_log, 'w') as log_file:
        pass
    time.sleep(1)

