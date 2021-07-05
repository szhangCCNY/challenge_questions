
import os
## this gets all the .txt files in current working directory
txt_list = [x for x in os.listdir() if (x.endswith(".txt") and not x.endswith("taboo_words.txt"))]
## this is current working directory
cwd = os.getcwd()
print(cwd)
print(txt_list)
import shutil


def replace_word(file_str, taboo_list):
    print("This is the content of .txt file before replacing:")
    print(file_str, '\n')

    count = 0
    new_str = ''
    for word in file_str:
        if word in taboo_list:
            replace_str = ''
            replace_str += '*'*len(word)
            new_str+= (replace_str + ' ')
            count += 1
        else:
            new_str += word + ' '
            
    print("This is the content of .txt file after replacing:")
    print(new_str)
    return new_str, count


def main():
    taboo_list = []
    taboo_file = open("taboo_words.txt", "r")
    taboo_list = taboo_file.read()
    taboo_file.close()

    print("This is the list of Taboo words:")
    print(taboo_list, '\n')

    for file in txt_list:
        taboo_count = 0
        f = open(file, "r+")
        data = f.read()
        data = data.split()
        new_data, taboo_count = replace_word(data, taboo_list)
        if taboo_count > 5:
            source_file = cwd + "/" + file
            dest_folder = cwd + "/trash"
            shutil.move(source_file, dest_folder)
        else:
            f.seek(0)
            f.write(new_data)
        f.close()
        print(taboo_count, "taboo words from", file)
        print('\n')

main()