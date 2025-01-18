from sys import argv
import Oriturus_read as Or
import Oriturus_write as Ow

def Oriturus(file):
    '''
    Processes a file, reading it, finding the tags and references then swaping them.

    Args:
        file (str): The path to the input file that needs processing.

    Returns:
        list: new text with swaped tags and references
        dict: tags and references 
        dict: metadata of the file changes and errors
        
    '''
    with open(file,"r") as text:
        raw = text.readlines()

    tag_dict,changes_dict = Or.oriturus_read(raw)
    
    #updated file_lines with the replaced lines
    new_text = Ow.oriturus_write(raw,tag_dict,changes_dict)
    return new_text, tag_dict, changes_dict, 

    

if __name__ == "__main__":
    print(f"Welcome to Oriturus the reference manager. version 1.1.0")

    file = "example/test.txt" #argv[1]
    new_text, tag_dict, changes_dict = Oriturus(file)
    for line in new_text:
        print(line)
    for error in changes_dict["errors"]:
        print(error)

        



