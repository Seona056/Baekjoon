dice = [int(i) for i in input().split()]

dice_set = list(set(dice))

if len(dice_set) == 1:
    print(10000+(dice_set[0]*1000))
    
elif len(dice_set) == 2:
    
    for d in dice_set:
        dice.remove(d)
    
    print(1000 + (dice[0]*100))
    
else:
    print(max(dice) * 100)
