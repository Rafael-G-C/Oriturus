import re
import os.path as osp
import bib_reorder as br
import Oriturus_read as Or
import Oriturus_write as Ow

def main(path_to_file,name_of_file):

    print(f"---------------\nOrdering {name_of_file}...")

    def text_rewriter(new_line,path_to_file,name_of_file):
            with open(path_to_file+"ORDERED_"+name_of_file,"a+") as ordered:
                    ordered.write(new_line)

    #read the whole text
    with open(path_to_file+name_of_file,"r") as file:
        file_lines = file.readlines()


    #Send the whole text to "Oriturus_read" to get the tag_dict, the ref_order_info, and see if there's a !!ref_start tag
    ref_start_signaler = 0 
    tag_dict,ref_info_dict,ref_start_signaler = Or.oriturus_read(file_lines,ref_start_signaler)

    
    #Send lines to "Oriturus_write" to replace them with the changed ones
    for line in file_lines:
        if "!!ref_start" in line: #break at the !!ref_start tag
            break
        tag_catcher = re.search("^!{2}(.+)>>{1}(.+)!",line) #look for any tags !!tag>>tag_name
        braquet_catcher = re.search("\[(.+)\]", line) # look for any type of braquet [Oriturus] [Turus.]
        if tag_catcher == None:
            pass # if no tags found continue
        else:
            continue # ignore all tags
        
        if braquet_catcher == None:
            text_rewriter(line,path_to_file,name_of_file) # if does not have braquets then just rewrite the line and go to the next line
            continue
        else: # if there are any braquets send it to Oriturus_write to rewrite the line
            new_line = Ow.oriturus_write(line,tag_dict,ref_info_dict)
            new_line = new_line + "\n" #add it as a new line
            text_rewriter(new_line,path_to_file,name_of_file) #rewrite it
    
    #Send the whole text to "bib_reorder" along with "ref_order_dict" to write new ordered bibliography
    if ref_start_signaler == 1: #if there's a !!ref_start tag
        print("Ordering bibliography...")
        br.bib_writer(file_lines,path_to_file,name_of_file,ref_info_dict) #write the bibliography normally
    
    else:
        print("!!ref_sart tag not found Oriturus won't order for references\n")
    
    print(f"\nFinished ordering {name_of_file} can be found as ORDERED_{name_of_file}")
    

if __name__ == "__main__":
    print(f"Welcome to Oriturus the reference manager. version 2.1.0\nAvoid putting spaces between the braquets ex. [ Oriturus] [bird. ]\n")
    
    while True:
        print("Please write the name of the file")
        name_of_file = input("Oriturus: ")
        print("Please write the path to the file")
        path_to_file = input("Oriturus: ")
        
        if osp.isfile(path_to_file+name_of_file):
            main(path_to_file,name_of_file)
            break
        else:
            print(f"ERROR! {name_of_file} not found at {path_to_file} please try again...")
            continue
        



