def rotate_90(a):
    col = len(a)
    row = len(a[0])
    result = [[0]* row for _ in range(col)]
    for i in range(col):
        for j in range(row):
            result[j][row-i-1] = a[i][j]
    return result


def check(new_lock):
    lock_length = len(new_lock) // 3
    for i in range(lock_length, lock_length*2):
        for j in range(lock_length,lock_length*2):
            if new_lock[i][j] != 1:
                return False
    return True


def sol(key, lock):
    n = len(key)
    m = len(lock)

    new_lock = [[0]*(n*3) for _ in range(n*3)]

    for i in range(n):
        for j in range(n):
            new_lock[i+n][j+n] = lock[i][j]
    
    for rotation in range(4):
        ket = rotate_90(key)
        for x in range(n*2):
            for y in range(n*2):
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] += ket[i][j]
                    if check(new_lock) == True:
                        return True
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] -= key[i][j]
    return False