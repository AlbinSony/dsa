cnt = 0

def f():
    global cnt
    if cnt == 3:
        return
    print(cnt)
    cnt += 1
    f()

f()
