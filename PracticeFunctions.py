# def max_of_numbers(x,y,z):
#     biggest_number= max(x,y,z)
#     return biggest_number
#
# output= max_of_numbers(8,20,32)
# print(output)


# def prod_of_all_numbers():
#     my_list=[8,2,3,-1,7]
#     result = 1
#     for number in my_list:
#         result *= number
#     return result
#
# output = prod_of_all_numbers()
# print(output)


# def walk(steps):
#     for step in range(1, steps +1):
#         print(f"You walked #{step}")

def walk(steps):
    if steps == 0:
        return
    walk (steps -1)
    print(f"You walked #{steps}")

walk(900)


