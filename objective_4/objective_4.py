#
# Implement the 'params' function below so that it takes one required and one optional
# parameter and returns a list containing the parameters supplied. 
#
def params(p1, p2=None):
    return [p1, p2] if p2 else [p1]
