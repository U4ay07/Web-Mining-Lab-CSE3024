index = {}  # dictionary to hold the word of the files as key and their index with offset as list.


def read_files(filename, file_number):
    f = open(filename)
    l1 = f.readlines()
    counter = 0
    words = []
    print('File content: ')
    print(l1)
    print()
    for i in l1:
        temp = i.split(' ')
        for j in temp:
            words.append(j.lower().replace("\n", ""))
    for i in words:
        if not i in index.keys():
            index[i] = [(file_number, counter)]
            counter = counter + 1
        else:
            index[i].append((file_number, counter))
            counter = counter + 1

    f.close()
    return None


# calling the declared function with different input files
read_files('./input1.txt', 1)
read_files('./input2.txt', 2)

# preparing the index dictionary for output as well as storing in the output.txt file
sorted_keys = sorted(index.keys())

f = open("output.txt", "w")
output_line = "Word".ljust(15) + "Frequency".ljust(15) + "\n"
f.writelines(output_line)
f.writelines('------------------------------------------------\n\n')
print("       MY DICTIONARY       ")
print("\nWord".ljust(15) + "Frequency".ljust(15))
print('------------------------------------------')
for i in sorted_keys:
    print(str(i).ljust(15), str(len(index[i])).ljust(15))
    output_string = str(i).ljust(15) + str(len(index[i])).ljust(15) + "\n"
    f.writelines(output_string)

f.close()

print('\n\n\n')

f = open("output1.txt", "w")
output_line1 = "Word".ljust(15) + "Posting List".ljust(15) + "\n"
f.writelines(output_line1)
f.writelines('----------------------------------------------------\n\n')
print("             POSTINGS LIST               ")
print("\nWord".ljust(15) + "Frequency".ljust(15) + "Posting List".ljust(15))
print('---------------------------------------------')
for i in sorted_keys:
    print(str(i).ljust(15), str(len(index[i])).ljust(15), str(index[i]).ljust(15))
    output_string1 = str(i).ljust(15) + str(index[i]).ljust(15) + "\n"
    f.writelines(output_string1)

f.close()
