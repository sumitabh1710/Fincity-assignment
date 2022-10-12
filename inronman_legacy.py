def findTheRange(planets, reception):
    dict = {}
    for i in range(planets):
        dict.update({i:0})

    for i in range(len(reception)):
        curr = reception[i]
        for i in range(curr[0], curr[1]):
            dict[i] += curr[2]
    
    max = [0,0,0]
    for i in range(planets):
        if dict[i] > max[2]:
            max[2] = dict[i]
            max[0] = i
            max[1] = i+1
        else:
            pass
    return max


print(findTheRange(5, [[2, 4, 5], [1, 3, 6], [2, 4, 7]]))