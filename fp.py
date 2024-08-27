# Array Methods
array = lambda n, func=(lambda x: x) : map([*range(n)], func)
filter = lambda arr, func: [i for i in arr if func(i)]
find = lambda arr, func: filter(arr, func)[0]
map = lambda arr, func: [func(i) for i in arr]
uniq = lambda arr: list(set(arr))
def reduce(arr, init, func):
  for i in arr: init = func(init, i)
  return init

# Math Methods
isOdd = lambda n: bool(n % 2)
pow = lambda p: lambda n: n**p
sum = lambda arr: reduce(arr, 0, lambda a, b: a + b)
mul = lambda arr: reduce(arr, 1, lambda a, b: a * b)

# Object Methods
assign = lambda obj, update: {**obj, **update}
omit = lambda obj, keys: {k: v for k, v in obj.items() if k not in keys}

# Condition Methods
ors = lambda arr: find(arr, bool)
ands = lambda arr: all(arr) and arr[-1]
ternary = lambda term, true, false: true if term else false

# Expressive Function
withAs = lambda obj, cb: cb(obj)