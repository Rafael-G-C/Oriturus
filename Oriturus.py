import ref_ordering as ro
import ref_replacer as rp
import bib_reorder as br 

path_to_file = ""
name_of_file = "test.txt"


#read the whole text
with open(path_to_file+name_of_file,"r") as file:
    file_lines = file.readlines()


#send the whole text to "ref_ordering" and it will return the "ref_order_dict" and the line where "!!ref_start" is
ref_order_dict,bib_line = ro.ref_indexer(file_lines)
#send the whole text to "tag_finder"
#send the whole text to "ref_replacer" along with "ref_order_dict" to write a new file with the ordered references
rp.text_writer(path_to_file,name_of_file,file_lines,ref_order_dict,bib_line)

#send the whole text to "bib_reorder" along with "ref_order_dict" to write new ordered bibliography and the "bib_line" to find the bibliography
br.bib_writer(file_lines,bib_line,path_to_file,name_of_file,ref_order_dict)




