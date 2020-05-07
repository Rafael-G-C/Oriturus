import re
import os.path as osp
import bib_reorder as br
import Oriturus_read as Or
import Oriturus_write as Ow

def main(path_to_file,name_of_file,read_write):

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
    for linenum, line in enumerate(file_lines):
        if "!!ref_start" in line: #break at the !!ref_start tag
            break
        tag_catcher = re.search("^!{2}(.+)>>{1}(.+)!",line) #look for any tags !!tag>>tag_name
        braquet_catcher = re.search("\[(.+)\]", line) # look for any type of braquet [Oriturus] [Turus.]
        if tag_catcher == None:
            pass # if no tags found continue
        else:
            continue # ignore all tags
        
        if braquet_catcher == None:
            if read_write == 1:
                text_rewriter(line,path_to_file,name_of_file) # if does not have braquets then just rewrite the line and go to the next line
            else:
                pass
            continue
        else: # if there are any braquets send it to Oriturus_write to rewrite the line
            new_line = Ow.oriturus_write(line,tag_dict,ref_info_dict,linenum+1)
            if read_write == 1:
                new_line = new_line + "\n" #add it as a new line
                text_rewriter(new_line,path_to_file,name_of_file) #rewrite it
            else:
                pass
    
    #Send the whole text to "bib_reorder" along with "ref_order_dict" to write new ordered bibliography
    if ref_start_signaler == 1: #if there's a !!ref_start tag
        print("Ordering bibliography...")
        br.bib_writer(file_lines,path_to_file,name_of_file,ref_info_dict,read_write) #write the bibliography normally
    
    else:
        print("!!ref_sart tag not found Oriturus won't order for references\n")
    
    if read_write == 1:
        print(f"\nFinished ordering {name_of_file} can be found as ORDERED_{name_of_file}; read_write = 1")
    else:
        print(f"\nFinished ordering {name_of_file} nothing was written; read_write = 0")

    

if __name__ == "__main__":
    print(f"Welcome to Oriturus the reference manager. version 2.1.0\nAvoid putting spaces between the braquets ex. [ Oriturus] [bird. ]\n")

    name_of_file = "parcial_analitica"
    path_to_file = "/home/kilimanjaro/Documents/borrar/"
        
    #name_of_file = "test2.txt"
    #path_to_file = "/home/kilimanjaro/Documents/Python/Oriturus/"
    
    read_write = 0 #read is 0 write is 1
    
    main(path_to_file,name_of_file,read_write)

        



