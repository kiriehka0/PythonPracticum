all_divs = []
nums = sorted(list(map(int, set(input().split('; ')))))
divisors = {}
for x in nums:
	divs = set()
	for k in range(1, int(x ** 0.5) + 1):
		if x % k == 0:
			divs.add(k)
			divs.add(x // k)
	all_divs.append(sorted(list(divs)))
for i in range(len(nums)):
	for j in range(i + 1, len(nums)):
		if set(all_divs[i]) & set(all_divs[j]) == {1} and all_divs[i] != [1]:
			if nums[i] not in divisors:
				divisors[nums[i]] = [nums[j]]
			else:
				divisors[nums[i]] += [nums[j]]
			if nums[j] not in divisors:
				divisors[nums[j]] = [nums[i]]
			else:
				divisors[nums[j]] += [nums[i]]
for a, b in sorted(divisors.items()):
	print(f'{a} - ', end='')
	for i in range(len(b)):
		if i + 1 < len(b):
			print(b[i], end=', ')
		else:
			print(b[i])
