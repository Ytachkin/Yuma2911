# cache function
def cache(times):
    def mind(func):
        def memory():
            memory.count += 1  # this line is responsible for tracking the number of requests
            if memory.count == 1 or memory.count > times + 1:  # start and end
                memory.x = func()  # putting the hash into memory
                memory.count = 1  # for reset the counter we use this string
            else:
                print(memory.x)

        # defining variables
        memory.x = ''  # for the record cache
        memory.count = 0  # to count calls to the function
        return memory

    return mind