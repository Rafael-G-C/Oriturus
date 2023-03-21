import Oriturus_read as Or
import Oriturus_write as Ow

def main(path_to_file,name_of_file,read_write):
    with open(path_to_file+name_of_file,"r") as file:
        file_lines = file.readlines()

    tag_dict,changes_dict = Or.oriturus_read(file_lines)
    
    if read_write == 1:
         #updated file_lines with the replaced lines
         file_lines = Ow.oriturus_write(file_lines,tag_dict,changes_dict,)

         with open(path_to_file+"ORDERED_"+name_of_file,"w+") as ordered:
            for line in file_lines:
                ordered.write(line)

    

if __name__ == "__main__":
    print(f"Welcome to Oriturus the reference manager. version 1.1.0")

    path_to_file = ""
    name_of_file = ""
    read_write = 0

    
    main(path_to_file,name_of_file,read_write)

        



