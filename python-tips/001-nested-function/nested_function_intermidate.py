# Here's a simple example of a closure:
# https://www.freecodecamp.org/news/nested-functions-in-python/
# Closures make it possible to pass data to inner 
# functions without first passing them to outer functions 
# with parameters like the greeting example at the beginning 
# of the article. They also make it possible to invoke the inner 
# function from outside of the encapsulating outer function. 
# All this with the benefit of data encapsulation / hiding mentioned before.
def num1(x):
  def num2(y):
    return x + y
  return num2

print(num1(10)(5))