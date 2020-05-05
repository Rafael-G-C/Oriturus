import re 
import bib_reorder as br
import Oriturus_read as Or
import Oriturus_write as Ow

path_to_file = ""
name_of_file = "test.txt"

def text_rewriter(new_line,path_to_file,name_of_file):
        with open(path_to_file+"ORDERED_"+name_of_file,"a+") as ordered:
                ordered.write(new_line)

#read the whole text
with open(path_to_file+name_of_file,"r") as file:
    file_lines = file.readlines()


#send the whole text to "ref_ordering" and it will return the "ref_order_dict" and the line where "!!ref_start" is
#ref_order_dict,bib_line = ro.ref_indexer(file_lines)
tag_dict,ref_info_dict = Or.oriturus_read(file_lines)

#send the whole text to "tag_finder"
#send the whole text to "ref_replacer" along with "ref_order_dict" to write a new file with the ordered references
#rp.text_writer(path_to_file,name_of_file,file_lines,ref_order_dict,bib_line)
for line in file_lines:
    if "!!ref_start" in line:
        break
    tag_catcher = re.search("^!{2}(.+)>>{1}(.+)!",line)
    braquet_catcher = re.search("\[(.+)\]", line)
    if tag_catcher == None:
        pass
    else:
        continue
    
    if braquet_catcher == None:
        text_rewriter(line,path_to_file,name_of_file)
        continue
    else:
        new_line = Ow.oriturus_write(line,tag_dict,ref_info_dict)
        new_line = new_line + "\n"
        text_rewriter(new_line,path_to_file,name_of_file)
#send the whole text to "bib_reorder" along with "ref_order_dict" to write new ordered bibliography and the "bib_line" to find the bibliography
br.bib_writer(file_lines,path_to_file,name_of_file,ref_info_dict)




