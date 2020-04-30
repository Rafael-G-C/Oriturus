import reference_ordering as ro
import ref_replacer as rp
import bibliography_reorder as br
#call the reference_ordering 
#path_to_article = #path
def adding_the_whole(string,path_to_file,name_of_file):
    with open(path_to_file+"ORDERED_"+name_of_file,"a") as full_text:
        full_text.write(string)

path_to_file = ""
name_of_file = "test.txt"

#strip bibliography from main text
with open(path_to_file+name_of_file,"r") as file:
    #read everything 
    file_lines = file.readlines()

#DONE - grab main text and send it to reference_ordering and he will return the ref_order_dict
ref_order_dict,bib_line = ro.ref_indexer(file_lines)

#grab the bibliography and send it to bibliography_reorder along with ref_order_dict to write new ordered bibliography
br.bibliography_maker(file_lines,bib_line,path_to_file,name_of_file,ref_order_dict)

#DONE - grab main text and send it to ref_replacer along with ref_order_dict to write the ordered_text
rp.text_remaker(path_to_file,name_of_file,file_lines,ref_order_dict,bib_line)
#append the bibliography to ordered text
with open(path_to_file+"RAW_BIB_"+name_of_file,"r") as raw_bib:
    ordered_bib = raw_bib.readlines()

start_writing = 0
for line in ordered_bib:
    if "ORDERED_BIB" in line:
        start_writing = 1
        continue
    if start_writing == 1:
        if "not found"in line:
            print(line)
            continue
        just_ordered_ref = line.split("|")
        adding_the_whole(just_ordered_ref[1],path_to_file,name_of_file)




