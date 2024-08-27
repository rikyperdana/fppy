import fp as _

# Uncomment any of the prints below to test them

# Aray Methods --------------------------------------------
## Create a new indexed array
# print(_.array(6)) # get [0, 1, 2, 3, 4, 5]
# print(_.array(6, _.pow(2))) # get [0, 1, 4, 9, 16, 25]

## Filter an Array
# print(_.filter(_.array(6), _.isOdd)) # get [1, 3, 5]
fruits = ["banana", "apple", "melon", "apple"]
# print(_.filter(fruits, lambda i : i  == "apple"))

## Find something that satisfies a given function
# print(_.find(_.array(6), _.isOdd)) # get 1
# print(_.find(fruits, lambda i: i == "melon")) # get melon

## Map an Array according to a given function
# print(_.map(_.array(6), lambda i: i - 5))
# print(_.map(fruits, lambda i: i.upper()))

## Get unique items in an Array
# print(_.uniq(fruits)) # get ['melon', 'banana', 'apple']

## Reduce an Array into anything we specify
# print(_.reduce(fruits, "", lambda a, b: a + b))
# get 'bananaapplemelonapple'


## Math Methods -------------------------------------------
# print(_.isOdd(3)) # get True
# print(_.pow(2)(3)) # get 9
# print(_.sum(_.array(6))) # get 15
# print(_.mul(_.array(6)[1:])) # get 120
# equivalent to the factorial of 5


## Object Methods -----------------------------------------
# Update the content of any given object with another object
# print(_.assign({'a': 1}, {'b': 2})) # get {'a': 1, 'b': 2}

# Remove certain keys from a given object
# print(_.omit({'a': 1, 'b': 2}, ['a'])) # get {'b': 2}


## Conditional Methods ------------------------------------
# conditions is an array pairs of expression and value
conditions = [
  1 == 2 and 'inequal',
  3 < 0 and 'this is wrong',
  1 + 1 and 'no more elseifs'
]
# Whence feed into ors, it shall return the first truthy pair
# print(_.ors(conditions)) # get 'no more elseif'

# ands function shall return the last one in an array
# only if the entire expressions in the array is truthy
all_is_true = [True, 42, 'yeah']
# print(_.ands(all_is_true)) # get 'yeah'
# print(_.ands([*all_is_true, 0])) # get False

# The functional replacement of if else statement
expression = (2 + 3 < 1, 'Right', 'Wrong')
# print(_.ternary(*expression))


# Expressive Function -------------------------------------
# This one is not equal to native Python 'with as'
# Use withAs if you want to make an expressive function
# _.withAs(1, print)