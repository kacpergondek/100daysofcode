name_list_path = 'Input/Names/invited_names.txt'

starting_letter_path = 'Input/Letters/starting_letter.txt'

output_folder_path = 'Output/ReadyToSend/Letter_for_'

#Remove spaces
with open(name_list_path,'r') as file:
    mylist = [line.rstrip('\n') for line in file]

#Load starting letter
with open(starting_letter_path,'r') as file:
    starting_letter = file.read()
#Create new letters
for name in mylist:
    new_letter = open(output_folder_path + name, 'a')
    new_letter.write(starting_letter.replace('[name]', name))

    