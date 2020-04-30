import reference_ordering as ro
import ref_replacer as rp
import bibliography_reorder as br
#call the reference_ordering 
#path_to_article = #path
def adding_the_whole(string,path_to_file,name_of_file):
    with open(path_to_file+"ordered_"+name_of_file,"a") as full_text:
        full_text.write(string)

def raw_bib_maker(string,path_to_file,name_of_file):
    with open(path_to_file+"raw_bib_"+name_of_file,"a+") as raw_bib:
        raw_bib.write(string)



path_to_file = "/home/kilimanjaro/Documents/acs/"
name_of_file = "super_impor.txt"
bib_name = "referencias\n"

#strip bibliography from main text
with open(path_to_file+name_of_file,"r") as file:
    #read everything 
    file_lines = file.readlines()

#DONE - grab main text and send it to reference_ordering and he will return the ref_order_dict
ref_order_dict,bib_line = ro.ref_indexer(file_lines)

#copy whats below the bibliography mark into a new file
raw_bib_maker("UNORDERED_BIB\n",path_to_file,name_of_file)
for linenum, line in enumerate(file_lines):
    if bib_line < linenum:
        raw_bib_maker(line,path_to_file,name_of_file)

#grab the bibliography and send it to bibliography_reorder along with ref_order_dict to write new ordered bibliography
br.bibliography_maker(path_to_file,name_of_file,ref_order_dict)

#DONE - grab main text and send it to ref_replacer along with ref_order_dict to write the ordered_text
rp.text_remaker(path_to_file,name_of_file,file_lines,ref_order_dict,bib_line)
#append the bibliography to ordered text
with open(path_to_file+"raw_bib_"+name_of_file,"r") as raw_bib:
    ordered_bib = raw_bib.readlines()

start_writing = 0
for line in ordered_bib:
    if "ORDERED_BIB" in line:
        start_writing = 1
        continue
    if start_writing == 1:
        just_ordered_ref = line.split("|")
        adding_the_whole(just_ordered_ref[1],path_to_file,name_of_file)




