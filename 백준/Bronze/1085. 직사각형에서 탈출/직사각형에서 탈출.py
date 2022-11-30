x, y, w, h = map(int, input().split())
print(min(x, y, w-x, h-y))    # (x, y)는 직사각형 안에 있으므로 abs를 하지 않아도 된다!