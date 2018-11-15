print("Testing scope with global and non-local")

test = 1
def outer():
    #global test
    #nonlocal test - not allowed
    test = 2
    def inner():
        #nonlocal test
        global test
        test = 3
        print("Inner", test)
    inner()
    print("Outer", test)
outer()
print("Global", test)