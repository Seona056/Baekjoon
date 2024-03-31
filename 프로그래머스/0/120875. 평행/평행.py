def solution(dots):
    answer = 0
    line1 = [(0,1), (0,2), (0,3)]
    line2 = [(2,3), (1,3), (1,2)]

    for l1, l2 in zip(line1,line2):
        [x1, y1] = dots[l1[0]]
        [x2, y2] = dots[l1[1]]
        [x3, y3] = dots[l2[0]]
        [x4, y4] = dots[l2[1]]

        if (x2-x1)/(y2-y1) == (x4-x3)/(y4-y3):
            return 1
    return answer