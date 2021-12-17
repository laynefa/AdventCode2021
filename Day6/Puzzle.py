def part_one(file, days):
    with open(file, 'r') as initial_data:
        fish = [int(i) for i in initial_data.read().strip().split(',')]
    while days > 0:
        new_fish = 0
        for pos,timer in enumerate(fish):
            if timer == 0:
                new_fish += 1
                fish[pos] = 6
            else:
                fish[pos] -= 1
        for _ in range(new_fish):
            fish.append(8)
        days -= 1
    #print(fish)
    print(len(fish))

def part_two(file, days):
    with open(file, 'r') as initial_data:
        fish = [int(i) for i in initial_data.read().strip().split(',')]
    total_fish = []
    for i in range(9): 
        total_fish.append(fish.count(i)) #list of number of fish currently in each stage, where index = stage number
    for _ in range(days):
        reset_fish = total_fish.pop(0) #get all fish that are at 0 and resetting to 6
        total_fish[6] += reset_fish
        total_fish.append(reset_fish) #add new fish that get spawned as stage 8
    print(sum(total_fish))
    
#part_one('.\\day6\\input.txt', 80)
part_two('.\\day6\\input.txt', 256)