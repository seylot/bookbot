import sys
if len(sys.argv) < 2:
	print("Usage: python3 main.py <path_to_book>")
	sys.exit(1)

def get_book_text(path_to_file):

	with open (path_to_file) as f:
		file_contents = f.read()

	return file_contents

def main():
	# book = get_book_text("./books/frankenstein.txt")
	book = get_book_text(sys.argv[1])
	from stats import word_count, char_count, sort_chars
	num_words = word_count(book)
	print(f"============ BOOKBOT ============\nAnalyzing book found at {sys.argv[1]}...")
	print(f"----------- Word Count ----------\nFound {num_words} total words")
	num_char = char_count(book)
	sorted_char = sort_chars(num_char)
	print("--------- Character Count -------")
	for char_dict in (sorted_char):
		if char_dict["char"].isalpha():
			print(f"{char_dict["char"]}: {char_dict["count"]}")
	print("============= END ===============")

main()
