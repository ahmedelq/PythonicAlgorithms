def count_vowels(txt):
	vs = "a, e, i, o, u".split(', ')
	return sum([1 for t in txt if t in vs])
	

	
print(count_vowels('Hello world'))