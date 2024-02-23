n = int(input())
def gener(n):
    while(n>=0):
        yield(n)
        n -= 1
nums = gener(n)
print(list(nums))