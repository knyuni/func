def prime_numbers(count):

	i = 2
	result = []

	while i < count:
		flag = True


		for item in range(2, int(i**0.5)+1):
			if i % item == 0 and i != item: 
				flag = False
				break
			if flag:
				result.append(i)

		i += 1
		return result

print(prime_numbers(1000000))



	
