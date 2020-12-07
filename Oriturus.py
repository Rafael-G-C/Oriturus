import re
import os.path as osp
import os
import bib_reorder as br
import Oriturus_read as Or
import Oriturus_write as Ow
import sys 

def main(path_to_file,name_of_file,read_write):

    def text_rewriter(new_line,path_to_file,name_of_file):
            with open(path_to_file+"ORDERED_"+name_of_file,"a+") as ordered:
                    ordered.write(new_line)

    #read the whole text
    with open(path_to_file+name_of_file,"r") as file:
        file_lines = file.readlines()


    #Send the whole text to "Oriturus_read" to get the tag_dict, the ref_order_info, and see if there's a !!ref_start tag
    ref_start_signaler = 0 
    bib_list,ref_start_signaler,tag_dict = br.bib_writer(True,file_lines)
    
    if ref_start_signaler == 0:
        print("!!ref_start tag not found Oriturus won't order for references\n")
    
    ref_list = Or.oriturus_read(file_lines,ref_start_signaler,bib_list,tag_dict)
    
    #Send lines to "Oriturus_write" to replace them with the changed ones
    if read_write == 1:
        ignore_lines = 0
        for linenum, line in enumerate(file_lines):
            # checks if the line should be ignored
            tag_catcher = re.search("!{2}.*!?",line)
            if "!!ref_start!" in line:
                break
            elif "!#" in line:
                ignore_lines = not ignore_lines
                continue
            
            elif ignore_lines == 1 or tag_catcher != None:
                continue
            
            
            # checks if something needs to be replaced
            braquet_catcher = re.search("\[(.+)\]", line) # look for any type of braquet [Oriturus] [Turus.]
            if braquet_catcher == None:
                text_rewriter(line,path_to_file,name_of_file)

            else: # if there are any braquets send it to Oriturus_write to rewrite the line
                new_line = Ow.oriturus_write(line,tag_dict,ref_list,linenum+1)
                #new_line = new_line + "\n" #add it as a new line
                text_rewriter(new_line,path_to_file,name_of_file) #rewrite it    
    
    if read_write == 1 and ref_start_signaler == 1:
        #Send the whole text to "bib_reorder" along with "ref_order_dict" to write new ordered bibliography
        br.bib_writer(False,file_lines,path_to_file,name_of_file,ref_list,tag_dict,bib_list,read_write) #write the bibliography normally
        print(f"\nFinished ordering {name_of_file} can be found as ORDERED_{name_of_file} and TAGS_{name_of_file}; read_write = 1")
    else:
        print(f"\nFinished ordering {name_of_file} nothing was written; read_write = 0")

    

if __name__ == "__main__":
    print(f"Welcome to Oriturus the reference manager. version 4.0.0")

    try:
        read_write = sys.argv[1] == "-w"
        name_of_file = sys.argv[2]
    except:
        read_write = 0
        name_of_file = sys.argv[1]

    
    path_to_file = osp.abspath(os.getcwd()) + "/"
    
    main(path_to_file,name_of_file,read_write)

        



