import random, time

def insert_sort(olist: list):
    n = len(olist)
    for i in range(1, n): # 从第二个元素开始
        key = olist[i]
        for j in range(i-1, -1, -1):
            if key < olist[j]:
                olist[j+1], olist[j] = olist[j], key
            else:
                break

def genlist(n: int, p,q):
    "生成n个介于[p, q]之间的随机整数列表"
    return [random.randint(p,q) for i in range(n)]

def timed(fn, *args):
    start = time.clock() 
    res = fn(*args)
    end = time.clock()
    return res, round(end-start, 2) # 保留两位小数

if __name__ == '__main__':
    olist = genlist(10000, 0,100000)
    res, t = timed(insert_sort, olist)
    print(t, ' s')



