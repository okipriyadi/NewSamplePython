"""
So far, we’ve only discussed catching of exceptions; how do you throw them?You use the
raise statement. Let’s assume you created an API call that requires those writing against
your library to send in a positive integer greater than 0.With the help of the isinstance
built-in function that verifies the type of an object, your code can look something like this:
"""
    
def foo(must_be_positive_int):
    """foo() -- take positive integer and process it"""
    # check if integer
    if not isinstance(must_be_positive_int, int):
        raise TypeError("ERROR foo(): must pass in an integer!")
    # check if positive
    if must_be_positive_int < 1:
        raise ValueError("ERROR foo(): integer must be greater than zero!")
    # normal processing here