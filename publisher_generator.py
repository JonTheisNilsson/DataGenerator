import random
import linecache

# Config
number_of_publishers_to_generate = 100
outputfilename = "output/publishers.txt"

#
count = 0


print("Opening output file: " + outputfilename)
outputfile = open(outputfilename, "a")


def get_random_from_file(filename, length):
    random_line = linecache.getline(filename, (random.randint(1, length)))
    return random_line.strip()


def get_adjective():
    return get_random_from_file("datasets/adjectives.txt", 912).capitalize()


def get_adverb():
    return get_random_from_file("datasets/adverbs.txt", 330).capitalize()


def get_determiner():
    return get_random_from_file("datasets/determiners.txt", 39)


def get_noun():
    return get_random_from_file("datasets/nouns.txt", 6885).capitalize().capitalize()


def get_preposition():
    return get_random_from_file("datasets/prepositions.txt", 70)


def get_verb():
    return get_random_from_file("datasets/verbs.txt", 1042).capitalize()


def addline():
    global count

    struc1 = "The House of the " + get_adjective() + " " + get_noun()
    struc2 = get_verb() + " Press"
    struc3 = "Press of " + get_verb()
    struc4 = "The " + get_adjective() + " Publisher"

    bag = {
        1: struc1,
        2: struc2,
        3: struc3,
        4: struc4,
    }
    o = bag[random.randint(1, 4)]
    print(o)
    outputfile.write(o)

    count = count + 1


while (count < number_of_publishers_to_generate):
    addline()

print("Closing outputfile: " + outputfilename)
outputfile.close()
