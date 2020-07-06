def greet(name, msg="Good morning!"):
    """
    This function greets to
    the person with the
    provided message.

    If the message is not provided,
    it defaults to "Good
    morning!"
    """

    print("Hello", name + ', ' + msg)


greet("Vikram")
greet("Vikram", "How do you do?")


# Python Arbitrary Arguments

def welcome(*name):
    for val in name:
        print("Hello {}".format(val))
        # or
        print("Hola", name)


welcome("vikram", "pratap", "sahu")
