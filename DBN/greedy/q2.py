nums = input()

result = int(nums[0])
for i in range(1, len(nums)):
    num = int(nums[i])
    if result != 0 and num > 1:
        result *= num
    else:
        result += num

print(result)
