# 가장 빠른 답을 보고 수정한 것
# 메모리: 30840 KB, 시간: 68 ms

dice = sorted(list(map(int, input().split())))

if len(set(dice)) == 1:
    print(10000 + (dice[0]*1000))
elif len(set(dice)) == 2:
    print(1000 + (dice[1]*100))    # 3개 중 2개가 중복이므로 중간을 선택한다.
else:
    print(dice[2]*100)
    
    
    
# 원래 제출했던 코드
# 메모리: 30840 KB, 시간: 72 ms

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
