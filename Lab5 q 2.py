nums = [random.randint(0, 50) for _ in range(20)]
target = int(input("Enter a number to find: "))
positions = [i for i, x in enumerate(nums) if x == target]

print("Generated list:", nums)
print(f"Occurrences of {target} at positions:", positions)
