def f1(w, gifts, gift_variant):
    if sum(gift_variant) == w:
        print('OK', gift_variant)
        return
    if sum(gift_variant) > w:
        print('NOT OK', gift_variant)
        return
    for i in range(len(gifts)):
        print(w, gifts[:i] + gifts[i + 1:], gift_variant + [gifts[i]])
        f1(w, gifts[:i] + gifts[i + 1:], gift_variant + [gifts[i]])

def f2(q):
    s = q[0] * gifts[0] + q[1] * gifts[1] + q[2] * gifts[2]
    if s == w:
        print('OK', q)
        res.add(tuple(q))
        return
    if s > w:
        print('NOT OK', q)
        return
    for i in range(len(q)):
        next_q = q[:]
        next_q[i] += 1
        f2(next_q)
w = 40
gifts = [10, 25, 15]
# f1(w, gifts, [])
res = set()
f2([0, 0, 0])
print(len(res), ':', res)
