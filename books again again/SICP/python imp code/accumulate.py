import operator

def accu(combiner, init_v, term, a, next_v, b):
    if a > b: return init_v
    else:
        return accu(combiner, combiner(init_v, term(a)),
                    term, next_v(a), next_v, b)
    
def accu_recur(combiner, init_v, term, a, next_v, b):
    if a > b: return init_v
    else:
        return combiner(term(a),
                        accu_recur(combiner, init_v, term, next_v(a), next_v, b))

def sum_(term, next_v, a, b):
    return accu_recur(operator.add, 0, term, a, next_v, b)
def product(term, next_v, a, b):
    return accu_recur(operator.mul, 1, term, a, next_v, b)
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
sum, product 都是某种累积。是accumulate的更一般概念的特殊情况。
