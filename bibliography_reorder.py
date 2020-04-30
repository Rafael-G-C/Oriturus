def bibliography_maker(file_lines,bib_line,path_to_file,name_of_file,ref_order_dict):
    #open bibliography
    
    def ref_stripper(ref): #should not really restructure check it out
        stripped_ref = ""
        for char in ref:
            if char == "[" or char == "]":
                continue
            else:
                stripped_ref += char
        return stripped_ref
    
    def ordered_bibliography_maker(string):
        with open(path_to_file+"RAW_BIB_"+name_of_file,"a+") as ordered_bibliography:
            ordered_bibliography.write(string)

    #ref_order_dict = {"YOLE" : 1, "Yale" :2}
    #string_one = ["[Yale] Author year","[YOLE] Author year","[Yoel] Author year"]
    #grab the bibliography and print the references in order


    ref_index = 1
    #breaker = 1
    #key_counter = 0
    unordered_bib = {}
    ordered_bibliography_maker("ORDERED_BIB\n")
    for linenum, string in enumerate(file_lines):
        if bib_line < linenum:
            call_ref = string.split(" ",1)
            stripped_ref = ref_stripper(call_ref[0])
            unordered_bib[stripped_ref] = call_ref[1]
    for key in ref_order_dict:
        if key in unordered_bib:
            ordered_bibliography_maker(f"{key}|[{str(ref_index)}] {unordered_bib[key]}")
            ref_index +=1
        else:
            ordered_bibliography_maker(f"{key}|[{ref_index}] {'ERROR! NOT FOUND '*10}\n")
            ref_index += 1

     
if __name__ == "__main__":
    print("bibliography_reorder running as main")
    pass
 

