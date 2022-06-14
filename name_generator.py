import random
import linecache


# Config
number_of_authors_to_generate = 10000
outputfilename = "output/data_authors.sql"


#
count = 0
fname = ""
lname = ""


print ("Opening output file: " + outputfilename)
outputfile = open(outputfilename, "a")

def get_random_from_file(filename, length):
    random_line = linecache.getline(filename, (random.randint(1, length)))
    return random_line.strip()

def addline():
    global count
    global fname
    global lname
    
    fname = get_random_from_file("datasets/first_name.txt", 6782)
    lname = get_random_from_file("datasets/last_name.txt", 1000)
    
    outputfile.write("INSERT INTO author_descriptor (f_name, l_name) VALUES ('"+fname+"', '"+lname+"');\n")
    count = count + 1

while (count < number_of_authors_to_generate):
    addline()


print ("Closing outputfile: " + outputfilename)
outputfile.close()
 
