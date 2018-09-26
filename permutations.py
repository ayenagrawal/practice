"""Python program to print all possible combinations of given chars"""
res = []
op = ["", "", "", "", ""]
def func1(chars, min, max):
    global res
    if min == max:
        res.append("". join(chars))
    else:
        for i in range(0, max+1):
            j = chars[min]
            chars[min] = chars[i]
            chars[i] = j
            func1(chars, min+1, max)
            j = chars[min]
            chars[min] = chars[i]
            chars[i] = j

def mainf():
    charset = ['a', 'e', 'i', 'o', 'u']
    func1(charset, 0, len(charset) -1)
    op = []
    count = 0
    for j in res:
        if j not in op:
            op.append(j)
            count += 1
    print("number of strings formed without repetetions: ", count)
    op.sort()
    for i in op:
        print(i)
mainf()

'''import itertools
def func1():
    abc = set(list(itertools.permutations('aeiou')))
    abc = list(abc)
    print(abc)
func1()'''
