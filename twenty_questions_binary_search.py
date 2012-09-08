"""
Twenty Questions using Binary Search

Uses a binary search to beat the game twenty questions.
"""
def main():
	dictionary_file = open("2of12inf.txt")
	dictionary_of_words = []

	# Read dictionary text file into memory so it can
	# be searched.
	for line in dictionary_file:
		dictionary_of_words.append(line)

	min_index = 0
	max_index = len(dictionary_of_words)
	mid_index = ((max_index - min_index) / 2) + min_index

	question_count = 0
	
	while mid_index != max_index:
		print "Does your word come after '{0}' in the dictionary?".format(dictionary_of_words[mid_index].strip().strip('%'))		
		while True:
			answer = raw_input(">").lower()
			if answer == "yes" or answer == "y":
				min_index = mid_index + 1
				mid_index = ((max_index - min_index) / 2) + min_index
				break
			elif answer == "no" or answer == "n":
				max_index = mid_index
				mid_index = ((max_index - min_index) / 2) + min_index
				break
			else:
				print "Please answer with a yes or no (y or n)"
		question_count = question_count + 1

	print "I think your word is '{0}'. (Found in {1} questions)".format(dictionary_of_words[mid_index].strip().strip('%'), question_count) 

if __name__ == "__main__":
    main()
