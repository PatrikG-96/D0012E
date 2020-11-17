
#broken
def activity_selector_rec(s, f, k, n):
    m = k
    while m < n and s[m] < f[k]:
        m = m + 1
    if m < n:
        return [m] + activity_selector_rec(s, f, m , n)
    else:
        return []


def activity_selector_iter(s, f):
    n = len(s)
    A = [0]
    k = 0
    for m in range(1, n):
        if s[m] >= f[k]:
            A = A + [m]
            k = m

    return A

s = [1,3,0,5,3,5,6, 8, 8, 2, 12]
f = [4,5,6,7,9,9,10,11,12,14,16]

lst = activity_selector_rec(s,f,0,len(s))
print(lst)

lst2 = activity_selector_iter(s,f)
print(lst2)
