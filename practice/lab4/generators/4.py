a = int(input())
b = int(input())
def square(a,b):
    for i in range(a,b+1):
        yield(i*i)
nums = square(a,b)
for i in range(a,b+1):
    print (i*i)
print (list(nums))