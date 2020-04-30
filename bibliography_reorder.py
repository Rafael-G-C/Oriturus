def bibliography_maker(file_lines,bib_line,path_to_file,name_of_file,ref_order_dict):
    #open bibliography
    
    """def restructured_ref(ref): #should not really restructure check it out
        stripped_ref = ref.strip()
        r_ref = "["+stripped_ref+"]"
        return r_ref """
    
    def ordered_bibliography_maker(string):
        with open(path_to_file+"raw_bib_"+name_of_file,"a+") as ordered_bibliography:
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
            call_ref = string.split("|")
            unordered_bib[call_ref[0]] = call_ref[1]
    for key in ref_order_dict:
        if key in unordered_bib:
            ordered_bibliography_maker(f"{key}|[{str(ref_index)}]{unordered_bib[key]}")
            ref_index +=1
        else:
            ordered_bibliography_maker(f"****** {key} not found *****\n")

     
    """while True:
        if key_counter == len(ref_order_dict):
            break 
        for key in ref_order_dict:
            if breaker == 0:
                
            r_key = restructured_ref(key)
            key_counter += 1
            for string in bib_ref:
                splitstring.split("|")
                if r_key in string:
                    print()
                    #ordered_bibliography_maker(f"[{ref_order_dict[key]}]| {string}")
                    breaker = 1
                    break
                breaker = 0 """
if __name__ == "__main__":
    print("bibliogrpahy_reorder running as main")
    pass
 

