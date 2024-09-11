def main():
    count = 0
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)
        words = file_contents.split()
        for i in words:
            if isinstance(i, str):
                count = count + 1 
    print ("There are " + str(count) + " words in the Frankenstein book.")
main()

def charr():
    with open("books/frankenstein.txt") as r:
        char_count = {}
        rile_contents = r.read()
        words_lower = rile_contents.lower()
        for char in words_lower:
            if char.isalpha():
                if char in char_count:
                    char_count[char] += 1
                else:
                    char_count[char] = 1 
        print (char_count)
charr()

def charrr():
    with open("books/frankenstein.txt") as r:
        char_count = {}
        rile_contents = r.read()
        words_lower = rile_contents.lower()

        # Count words
        words = words_lower.split()
        word_count = len(words)

        # Count characters
        for char in words_lower:
            if char.isalpha():
                if char in char_count:
                    char_count[char] += 1
                else:
                    char_count[char] = 1 

        # Generate the report
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{word_count} words found in the document\n")

        # Sort characters by frequency in descending order
        for char, count in sorted(char_count.items(), key=lambda item: item[1], reverse=True):
            print(f"The '{char}' character was found {count} times")

        print("--- End report ---")

# Call the function
charrr()