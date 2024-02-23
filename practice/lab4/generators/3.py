n = int(input())
def divisible(n):
    for i in range(n):
        if i%3 == 0 or i%4 == 0:
            yield(i)
nums = divisible(n)
for i in nums:
    print(i)

