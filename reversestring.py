# Sample String : "1234abcd"
# Expected Output : "dcba4321"

def reverse_a_string(simple_string):
    result_string = simple_string[::-1]
    return result_string

output= reverse_a_string("1234abcd")
print(output)

