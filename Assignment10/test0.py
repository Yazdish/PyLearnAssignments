# def add_five(x):
#     return x + 5

# nums = [11, 22, 33, 44, 55]
# result = list(map(add_five, nums))
# print(result)

# nums = [11, 22, 33, 44, 55]

# result = list(map(lambda x: x+5, nums))
# print(result)

# nums = [11, 22, 33, 44, 55]
# res = list(filter(lambda x: x%2==0, nums))
# print(res)

# def numbers(x):
#   for i in range(x):
#     if i % 2 == 0:
#       yield i

# print(list(numbers(11)))

# def make_word():
#   word = ""
#   for ch in "spam":
#     word +=ch
#     yield word

# print(list(make_word()))

def decor(func):
    def wrap():
        print("============")
        func()
        print("============")
    return wrap

@decor
def print_text():
    print("Hello world!")

print_text()