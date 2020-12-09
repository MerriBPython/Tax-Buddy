
### Insert whatever file you want to read here ###
### Note: Must have two letter state abbreviations on right, and ammount with no dollar sign or decimal on the right. ###

source = open('list.txt', 'r')

job_list = []


pricing = []

### Blank lists we can add each job to later ###

missouri_jobs =[]
illinois_jobs = []
nebraska_jobs = []
iowa_jobs = []
tennessee_jobs = []
kansas_jobs = []
oklahoma_jobs = []
arkansas_jobs = []
indiana_jobs = []
southdakota_jobs = []
minnesota_jobs = []
virginia_jobs = []
wisconsin_jobs = []
mississippi_jobs = []
colorado_jobs = []
ohio_jobs = []
kentucky_jobs = []
michigan_jobs = []

### Takes your file, and converts it into python readable lists ###

for line in source.readlines():
    stripped_lines = line.strip()
    list_of_lines = stripped_lines.split()
    job_list.append(list_of_lines)

### Seperating each state and their ammount into seperate lists ###

for list in job_list:
    if 'MO' in list:
        missouri_jobs.append(list)
    elif 'Mo' in list:
        missouri_jobs.append(list)
    elif 'MOÂ' in list:
        missouri_jobs.append(list)
    elif 'IL' in list:
        illinois_jobs.append(list)
    elif 'NE' in list:
        nebraska_jobs.append(list)
    elif 'IA' in list:
        iowa_jobs.append(list)
    elif 'TN' in list:
        tennessee_jobs.append(list)
    elif 'KS' in list:
        kansas_jobs.append(list)
    elif 'OK' in list:
        oklahoma_jobs.append(list)
    elif 'OKÂ' in list:
        oklahoma_jobs.append(list)
    elif 'IN' in list:
        indiana_jobs.append(list)
    elif 'SD' in list:
        southdakota_jobs.append(list)
    elif 'VA' in list:
        virginia_jobs.append(list)
    elif 'MI' in list:
        michigan_jobs.append(list)
    elif 'AR' in list:
        arkansas_jobs.append(list)
    elif 'WI' in list:
        wisconsin_jobs.append(list)
    elif 'MN' in list:
        minnesota_jobs.append(list)
    elif 'CO' in list:
        colorado_jobs.append(list)
    elif 'OH' in list:
        ohio_jobs.append(list)
    elif 'KY' in list:
        kentucky_jobs.append(list)
    elif 'MS' in list:
        mississippi_jobs.append(list)
#    else:
    #    print(list)

### Summing each ammount in each state, and printing it to the terminal ###

for list in missouri_jobs:
    amount = int(list[1])
    pricing.append(amount)

print('Missouri total is: ', sum(pricing))
pricing.clear()

for list in illinois_jobs:
    amount = int(list[1])
    pricing.append(amount)

print('Illinois total is: ', sum(pricing))
pricing.clear()

for list in nebraska_jobs:
    amount = int(list[1])
    pricing.append(amount)

print('Nebraska total is: ', sum(pricing))
pricing.clear()

for list in southdakota_jobs:
    amount = int(list[1])
    pricing.append(amount)

print('South Dakota total is: ', sum(pricing))
pricing.clear()

for list in kansas_jobs:
    amount = int(list[1])
    pricing.append(amount)

print('Kansas total is: ', sum(pricing))
pricing.clear()

for list in indiana_jobs:
    amount = int(list[1])
    pricing.append(amount)

print('Indiana total is: ', sum(pricing))
pricing.clear()

for list in arkansas_jobs:
    amount = int(list[1])
    pricing.append(amount)

print('Arkansas total is: ', sum(pricing))
pricing.clear()

for list in iowa_jobs:
    amount = int(list[1])
    pricing.append(amount)

print('Iowa total is: ', sum(pricing))
pricing.clear()

for list in mississippi_jobs:
    amount = int(list[1])
    pricing.append(amount)

print('Mississippi total is: ', sum(pricing))
pricing.clear()

for list in tennessee_jobs:
    amount = int(list[1])
    pricing.append(amount)

print('Tennessee total is: ', sum(pricing))
pricing.clear()

for list in virginia_jobs:
    amount = int(list[1])
    pricing.append(amount)

print('Virginia total is: ', sum(pricing))
pricing.clear()

for list in wisconsin_jobs:
    amount = int(list[1])
    pricing.append(amount)

print('Wisconsin total is: ', sum(pricing))
pricing.clear()

for list in minnesota_jobs:
    amount = int(list[1])
    pricing.append(amount)

print('Minnesota total is: ', sum(pricing))
pricing.clear()

for list in oklahoma_jobs:
    amount = int(list[1])
    pricing.append(amount)

print('Oklahoma total is: ', sum(pricing))
pricing.clear()

for list in colorado_jobs:
    amount = int(list[1])
    pricing.append(amount)

print('Colorado total is: ', sum(pricing))
pricing.clear()

for list in ohio_jobs:
    amount = int(list[1])
    pricing.append(amount)

print('Ohio total is: ', sum(pricing))
pricing.clear()


for list in kentucky_jobs:
    amount = int(list[1])
    pricing.append(amount)

print('Kentucky total is: ', sum(pricing))
pricing.clear()

for list in michigan_jobs:
    amount = int(list[1])
    pricing.append(amount)

print('Michigan total is: ', sum(pricing))
pricing.clear()
