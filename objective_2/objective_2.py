# Implement the following function:
#
# Function Name: chop
# Input type: <int>, <string>
# Return type: <tuple>
#
# Description: Returns a tuple consisting of the leftmost <int> characters and rightmost <int> characters of the <string>
def chop(n, str):
    str_len = len(str)
    if n > str_len:
        return (str, str)
    return (str[ : n], str[str_len - n : ])