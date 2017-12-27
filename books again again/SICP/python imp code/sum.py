;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
def sum_(term, next_v, a, b):
    if a > b:
        return 0
    else:
        return term(a) + sum_(term, next_v, next_v(a), b)

"""平方和"""
def square_sum(a, b):
    def term(x):
        return x*x
    def next_v(a):
        return a+1
    return sum_(term, next_v, a, b)

def pi_sum(a, b):
    "有递归深度限制，且收敛很慢"
    def term(n):
        return 1.0/(n * (n+2))
    def next_v(n):
        return n+4
    return 8*sum_(term, next_v, a, b)

print(pi_sum(1, 1000))
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
值得学习的地方：
1. 使用高阶函数抽象出了求和模式
2. 每个term，next_v 函数都作为局部函数，嵌在内部，不向外暴露。
