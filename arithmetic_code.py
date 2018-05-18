def divided_step(lower_bound, higher_bound, distribution, character):
	characters = sorted(distribution.keys())
	distance = higher_bound - lower_bound
	new_lower_bound = lower_bound
	for char in characters:
		if char != character:
			new_lower_bound += distribution[char] * distance
		else:
			break
	new_higher_bound = new_lower_bound + distribution[character] * distance
	return (new_lower_bound, new_higher_bound)

def arithmetic_code(origin, distribution):
	length = len(origin)
	lower_bound = 0
	higher_bound = 1
	for i in range (length):
		lower_bound, higher_bound = divided_step(lower_bound, higher_bound, distribution, origin[i])
	return (lower_bound, higher_bound)

if __name__ == '__main__':
	sequence = "badcd"
	distribution = {"a": 0.5, "b": 0.25, "c": 0.125, "d": 0.125}
	encoded_result = arithmetic_code(sequence, distribution)
	print(encoded_result)