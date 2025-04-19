def word_count(document):
	num_words = len(document.split())

	return num_words

def char_count(document):
	lowered_document = document.lower()
	chars = {}
	for char in lowered_document:
		if char not in chars:
			chars[char] = 1
		else:
			chars[char] += 1

	return chars

def sort_chars(char_dict):
	char_list = []
	for char, count in char_dict.items():
		char_list.append({"char": char, "count": count})

	def sort_on(dict):
		return dict["count"]

	char_list.sort(reverse=True, key=sort_on)

	return char_list

