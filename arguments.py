def greeting_and_multiply(*args,**kwargs):
    multiply = 1
    for nums in args:
        multiply*=nums
    print(multiply)
    print(f"Hello{kwargs}")    