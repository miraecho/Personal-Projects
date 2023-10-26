# I will read my assignment 3 and read
# each line to display its line count,
# character count, and word count.

file_to_read = open('jadencho_a3.py')

# Split will split each word as its own element in the list.
# The word variable will keep track of the current word while
# looping through each line in the file.
line_count, character_count, word_count = 0, 0, 0
character_list, split = [], []
word = ''

for line in file_to_read:
    text = line.strip()
    character_list = [character for character in line]
    for character in character_list:
        character_count += 1

    # For each character in the stripped line, if a character is a space or period
    # and the word is not empty, the word will be added at the end of the split list. The word
    # variable will also be reset to empty to prevent two words from being considered
    # the same element. Else, we should add the character to the word.
    for character in text:
        if (character == ' ' or character == '.') and word:
            split = split + [word]
            word = ''
            word_count += 1
        else:
            word += character

    print str(line_count + 1) + ' - ' + text
    line_count += 1
        
print '\nLine Count: ' + str(line_count)
print 'Character Count: ' + str(character_count)
print 'Word Count: ' + str(word_count)
