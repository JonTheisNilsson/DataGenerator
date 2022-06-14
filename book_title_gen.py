import random
import linecache

# Config
amount_to_generate = 40000
#outputfilename = "output/book_titles.txt"
outputfilename = "output/test.txt"

# Setup
count = 0
adjectives_line_count = len(open("datasets/adjectives.txt").readlines(  ))
adverbs_line_count = len(open("datasets/adverbs.txt").readlines(  ))
determiners_line_count = len(open("datasets/determiners.txt").readlines(  ))
nouns_line_count = len(open("datasets/nouns.txt").readlines(  ))
places_line_count = len(open("datasets/places.txt").readlines(  ))
prepositions_line_count = len(open("datasets/prepositions.txt").readlines(  ))
topics_line_count = len(open("datasets/topics.txt").readlines())
verbs_line_count = len(open("datasets/verbs.txt").readlines())


print("Opening output file: " + outputfilename)
outputfile = open(outputfilename, "a")

# region helpers
def get_random_from_file(filename, length):
    random_line = linecache.getline(filename, (random.randint(1, length)))
    return random_line.strip()


def get_adjective():
    return get_random_from_file("datasets/adjectives.txt", adjectives_line_count).capitalize()


def get_adverb():
    return get_random_from_file("datasets/adverbs.txt", verbs_line_count).capitalize()


def get_determiner():
    return get_random_from_file("datasets/determiners.txt", determiners_line_count)


def get_noun():
    return get_random_from_file("datasets/nouns.txt", nouns_line_count).capitalize().capitalize()


def get_preposition():
    return get_random_from_file("datasets/prepositions.txt", prepositions_line_count)


def get_verb():
    return get_random_from_file("datasets/verbs.txt", verbs_line_count).capitalize()


def get_topic():
    return get_random_from_file("datasets/topics.txt", topics_line_count)


def get_place():
    return get_random_from_file("datasets/places.txt", places_line_count)
# endregion

def addline():
    global count

    #TODO maybe refactoring into functions
    bag = {
        1: get_determiner().capitalize() + " " + get_noun(),
        2: get_determiner().capitalize() + " " + get_adjective() + " " + get_noun(),
        3: get_topic() + " " + get_preposition().capitalize() + " " + get_topic(),
        4: get_verb() + " " + get_preposition() + " " + get_determiner() + " " + get_noun(),
        5: "Introduction to " + get_topic(),
        6: "History of " + get_topic(),
        7: get_topic().capitalize() + ": A Modern Approach",
        8: "Advanced " + get_topic(),
        9: get_adjective() + " " + get_topic().capitalize(),
        10: "Certification in " + get_topic(),
        11: "The Science of " + get_topic(),
        12: "History of " + get_place(),
        13: get_noun() + "s " + get_preposition() + " " + get_place()
    }
    o = bag[random.randint(1, len(bag))]
    #print(o)
    outputfile.write(o + "\n")
    count = count + 1


while count < amount_to_generate:
    addline()

print("Closing outputfile: " + outputfilename)
outputfile.close()
