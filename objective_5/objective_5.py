#
# Create and implement the `Greeter` class as described in the README for this objective.
#

class Greeter:
    def __init__(self):
        self.num_sayhello_calls = 0

    def sayhello(self, name=""):
        self.num_sayhello_calls += 1
        if name == "":
            return "Hello, World."
        return "Hello, {}.".format(name)

    def tally(self):
        return self.num_sayhello_calls
