import time
current_time = time.time()

#function decorator with a pass through variable which is the name of the nested function
def speed_calc_decorator(function):
    #the nested wrapper function called by the decorator
    def wrapper():
        start_time = time.time()
        function()
        end_time = time.time()
        print(f'{function.__name__} runspeed: {end_time - start_time}')
    return wrapper

#the first function which will be run by the calling the decorator
@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i
    return current_time

#the second function that will be run by calling the decorator
@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i
    return 


#initializing the two functions and passing through the response of the nested function, showing the difference in the time it takes for the two to run because of the differences in the i range
fast_function()
slow_function()
