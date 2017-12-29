"""
How to Write a (Lisp) Interpreter (in Python)—— Peter Norvig
原文链接：http://norvig.com/lispy.html
"""
Symbol = str              # A Scheme Symbol is implemented as a Python str
Number = (int, float)     # A Scheme Number is implemented as a Python int or float
Atom   = (Symbol, Number) # A Scheme Atom is a Symbol or Number
List   = list             # A Scheme List is implemented as a Python list
Exp    = (Atom, List)     # A Scheme expression is an Atom or List
Env    = dict             # A Scheme environment (defined below) 
                          # is a mapping of {variable: value}

def tokenize(chars: str) -> list:
    "Convert a string of characters into a list of tokens."
    return chars.replace('(', ' ( ').replace(')', ' ) ').split()

def parse(program: str) -> Exp:
    "Read a Scheme expression from a string."
    return read_from_tokens(tokenize(program))

def read_from_tokens(tokens: list) -> Exp:
    "Read an expression from a sequence of tokens."
    if len(tokens) == 0:
        raise SyntaxError('unexpected EOF')
    token = tokens.pop(0) # pop the leftmost token
    if token == '(':
        L = []
        while tokens[0] != ')':
            L.append(read_from_tokens(tokens))
        tokens.pop(0) # pop off ')'
        return L
    elif token == ')':
        raise SyntaxError('unexpected')

    else:
        return atom(token)

def atom(token: str) -> Atom:
    "Numbers become numbers; every other token is a symbol."
    try: return int(token)
    except ValueError: # indicate that it's not int
        try: return float(token)
        except ValueError:
            return Symbol(token)

import math, pprint
import operator as op
def standard_env() -> Env:
    "An environment with some Scheme standard procedures."
    env = Env()
    env.update(vars(math)) # sin, cos, sqrt, pi, ...
    env.update({
        '+':op.add, '-':op.sub, '*':op.mul, '/':op.truediv, 
        '>':op.gt, '<':op.lt, '>=':op.ge, '<=':op.le, '=':op.eq, 
        'abs':     abs,
        'append':  op.add,  
        'apply':   lambda proc, args: proc(*args),
        'begin':   lambda *x: x[-1],
        'car':     lambda x: x[0],
        'cdr':     lambda x: x[1:], 
        'cons':    lambda x,y: [x] + y,
        'eq?':     op.is_, 
        'expt':    pow,
        'equal?':  op.eq, 
        'length':  len, 
        'list':    lambda *x: List(x), 
        'list?':   lambda x: isinstance(x, List), 
        'map':     map,
        'max':     max,
        'min':     min,
        'not':     op.not_,
        'null?':   lambda x: x == [], 
        'number?': lambda x: isinstance(x, Number),  
	'print':   print,
        'procedure?': callable,
        'round':   round,
        'symbol?': lambda x: isinstance(x, Symbol),
    })
    return env
global_env = standard_env()

def _eval_(x: Exp, env=global_env) -> Exp:
    "Evaluate an expression in an environment"
    if isinstance(x, Symbol):   # variable reference
        return env[x]
    elif isinstance(x, Number): # constant number
        return x
    elif x[0] == 'if':          # conditional
        (_, test, conseq, alt) = x
        exp = (conseq if _eval_(test, env) else alt)
        return _eval_(exp, env)
    elif x[0] == 'define':      # definition
        (_, symbol, exp) = x
        env[symbol] = _eval_(exp, env)
    else:                       # procedure
        proc = _eval_(x[0], env)
        args = [_eval_(arg, env) for arg in x[1:]]
        return proc(*args)

def repl(prompt='scheme==> '):
    "A prompt-read-eval-print loop."
    while True:
        pro_exp = input(prompt)
        if pro_exp == 'quit': break
        val = _eval_(parse(pro_exp))
        if val is not None: 
            print(schemestr(val))

def schemestr(exp):
    "Convert a Python object back into a Scheme-readable string."
    if isinstance(exp, List):
        return '(' + ' '.join(map(schemestr, exp)) + ')' 
    else:
        return str(exp)       

if __name__ == '__main__':
    repl()
