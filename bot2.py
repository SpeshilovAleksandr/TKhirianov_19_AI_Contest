n = 0

def move(me, enemies, bullets, bonuses, m):
    global n

    n += 1

    if (n // 100) % 2:
        m.left()
    else:
        m.right()

    m.shot(400, 300)
