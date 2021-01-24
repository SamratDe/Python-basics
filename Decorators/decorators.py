# decorator function
def new_decorator(org_fun):
    def wrap_func():
        print('Extra code, before the original function')
        org_fun()
        print('Some code, after the original function')

    return wrap_func


# Run anyone of the below types -

# type 1:
def func_that_needs_decorator():
    print('Decorate my function')

decorated_func = new_decorator(func_that_needs_decorator)


# type 2: (proper syntax of using decorators)
@new_decorator
def func_that_needs_decorator():
    print('Decorate my function')

func_that_needs_decorator()