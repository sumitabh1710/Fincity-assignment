def findPies(array, max_sweet):
    ans = []
    pies(array, max_sweet, 0, ans)
    return ans
        
def pies(array, max_sweet, curr, ans):
    new_max_sweet = max_sweet - array[curr]
    ans.append(array[curr])
    if new_max_sweet == 0:
        return ans
    elif new_max_sweet < 0:
        if len(ans) == 0:
            pass
        else:
            ans.pop()
        return pies(array, max_sweet, curr+1, ans)
    elif new_max_sweet > 0:
        pies(array, new_max_sweet, curr+1, ans)
    return ans

print(findPies([8, 4, 3, 2, 6, 5], 6))
print(findPies([1, 2, 3, 2, 1], 6))