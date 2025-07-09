def outer_func():
    print("This is outher_func.")

    def inner_func():
        print("This is inner_func.")

        inner_func()



outer_func()