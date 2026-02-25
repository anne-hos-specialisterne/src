
import os 

file_in = '../data/navneliste.txt'
#file_out = '../data/out.txt'
#sort_type = 'L'

file_out = input("This script will take the names in the 'navneliste.txt' file\n" +
                 " and write the list in sorted format. Please specify the file you want to create:\n")
 

while os.path.exists(file_out):
    user_in = input('The specied output file already exist. Do you want to change it? (Y/N)\n')
    if user_in == 'Y':
        file_out = input("Please specify the new path:\n")
    else:
        break 

                
sort_type = input("Would you like to sort your file alpabetically (A), lenghtwise (L)\n" +
                  " or return a dictionary with length for each name (D)?\n")


def read_file_to_list(filename):
    file = open(filename, 'r')

    names = file.readlines()[0]
    file.close()

    names1 = names.split(sep = ',')
    return(names1)


def write_list_to_file(filename, sorted_names):
    out = open(filename, 'w')

    for name in sorted_names:
        out.write(name + '\n')

    out.close()

def write_dict_to_file(filename, dict_names):
    out = open(filename, 'w')

    for name, length in dict_names.items():
        out.write(name + ":" + str(length) + '\n')

    out.close()


def sort_name_list_by_type(names, sort_type):
    if sort_type == 'A':
        sorted_names_alpha = sorted(names)
        write_list_to_file(file_out, sorted_names_alpha)
    elif sort_type == 'L':
        sorted_names_len = sorted(names, key = len)
        write_list_to_file(file_out, sorted_names_len)
    elif sort_type == 'D':
        length_dictionary = {}
        print(names)
        for name in names:
            n = list(name)
            length_dictionary[name] = len(n)

        write_dict_to_file(file_out, length_dictionary)


names = read_file_to_list(file_in)

sort_name_list_by_type(names, sort_type)