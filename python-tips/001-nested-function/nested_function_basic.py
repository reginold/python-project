def function1(): # outer function  
    print ("Hello from outer function")
    def function2(): # inner function
        print ("Hello from inner function")
    function2()

function1() 


# output:
# Hello from outer function
# Hello from inner function