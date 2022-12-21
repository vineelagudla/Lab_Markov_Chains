"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    file = open(file_path).read()
    #print(file)
    #split file into an array/list of words that can than be filtered
    #splitting file by "?" character then joining the string with " " and than we are splitting at the space
    new_string = " ".join(file.split()).rstrip()
    print(new_string)
    # # generate library chain
    # # for loop to generate tuple pairs based on string? ? (" ".join(file.split("?"))).lower().split()
    # tple_list =[]
    # for item, index in enumerate(new_string):
    #     tple_list += (item, new_string[index+1])
    # return tple_list


    # # your code goes here

    return new_string
    #close file


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    # your code goes here
    #for loop through words to create tuple of keys?
    new_lst = text_string.split()
    #generate bigram in lst from words in text

    for index in range(0,len(new_lst)-2):
        #key is a tuple of (word1, word2) or (index-current, index+1) 
        key = (new_lst[index], new_lst[index+1])
        #value is the word after the tuple, so lst of index+2
        value = [new_lst[index+2]]
        #dict generation
        #confirm key exists, filler is starting []
        # value is concated to the current lst [] + index+2 so []
        chains[key] = chains.get(key, []) + value
    #sort chain, must include .items() to sort the dictionary as a whole
    #sorted(dict) only sorts keys
    # chains_sorted = sorted(chains.items())
    return chains

print(make_chains(open_and_read_file("green-eggs.txt")))



def make_text(chains):
    """Return text from chains."""

    words = []

    # your code goes here
    #make a dictionary list of chain keys
    #-> convert dict list into standard list
    #-> chose randomly of that list
    key_start = random.choice(list(chains.keys()))
    value = random.choice(chains.get(key_start, []))
    #chains[key_start] = chains.get(key_start, []).remove(value)

    words += [key_start[0] ,  key_start[1] , value]
    #grab the last two words to be the key tuple for chain/dict search
    #if last two words (new keys) are not a valid key in the chain/dict then get out of th loop 
    #if the key exists then grab a word from the value list 

    
    
    key = (words[-2]+words[-1])
    value = random.choice(chains.get(key, -1))
    
    if value == -1:

    words += [key_start[0] ,  key_start[1] , value]
    #words [key1, key2 random value]
    #To generate random text, pick a key and a value from the generated chains
    # Example: (('Would', 'you'), ['could', 'could', 'could', 'could', 'like', 'like'])
    #          (('you', 'could'): ['you', 'you', 'you', 'you'])
    # output: 'Would you could' or 'would you like'

    #for loop of chain
    #random choice of key -> than add to lst-words
    #make a sliding key that would run through the list
    #if in valid key is return than otherwise select another rando key.


#     This is the expected output found in the lab manual     #
#  box? Would you could you with a mouse? Would you could you
# in a house? Would you could you in a house? Would you
# could you in a house? Would you could you with a fox?
# Would you like green eggs and ham? Would you like them, Sam
# I am?

    return ' '.join(words)

print(make_text(make_chains(open_and_read_file("green-eggs.txt"))))

input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
