def solution(a, b):
    week = ['THU','FRI','SAT','SUN','MON','TUE','WED']
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    return week[(sum(month[:a-1])+b)%7]