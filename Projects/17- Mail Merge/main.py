with open(r"D:\CODED_LIFE\###Udemy-100 Days of Pyt\Projects\24- Mail Merge\invited_names.txt") as names:
    names_list = names.read().splitlines()
# for line in names_list:
#     fixed_line = line.replace("\\n", "")
#     fixed_line = line

with open(r"D:\CODED_LIFE\###Udemy-100 Days of Pyt\Projects\24- Mail Merge\starting_letter.txt") as letter:
    content = letter.read().replace("Angela", "Yours truly,\n\nIshrak")
    
save_dir = r"D:\CODED_LIFE\###Udemy-100 Days of Pyt\Projects\24- Mail Merge\Ready to Send\\"

for name in names_list:
    personalized_letter = content.replace("[name]", name)
    file_name = f"letter_for_{name}.txt"
    with open(file= save_dir + file_name, mode="w") as final_letter:
        final_letter.write(personalized_letter)

# print(names_list)

