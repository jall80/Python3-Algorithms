string_1 = "un perro y un gato vieron a otro gato"

def count_words(text: str) -> dict:

	if not text:
		return -1

	text_list = text.split()
	
	text_dict = {}

	for word in set(text_list):

		text_dict[word] = text_dict.get(word, 0) + 1

	return text_dict

print(count_words(string_1))