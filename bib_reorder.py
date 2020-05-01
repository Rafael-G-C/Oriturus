def bib_writer(file_lines,bib_line,path_to_file,name_of_file,ref_order_dict):

    
    def ref_stripper(ref): #should not really restructure check it out
        stripped_ref = ""
        pass_catcher = 0
        error_code = 0
        for char in ref:
            if char == "[" or char == "]":
                pass_catcher += 1
                continue
            else:
                stripped_ref += char
        if pass_catcher != 2 or stripped_ref == "":
            error_code = 1
        return stripped_ref,error_code
    
    
    def ordered_bibliography_maker(string):
        with open(path_to_file+"RAW_BIB_"+name_of_file,"a+") as ordered_bibliography:
            ordered_bibliography.write(string)
    
    def adding_the_whole(string):
        with open(path_to_file+"ORDERED_"+name_of_file,"a") as full_text:
            full_text.write(string)

    #grab the bibliography and print the references in order


    ref_index = 1
    unordered_bib = {}

    for linenum, string in enumerate(file_lines):
        if bib_line < linenum:
            call_ref = string.split(" ",1)
            stripped_ref,error_code = ref_stripper(call_ref[0])
            if error_code == 1:
                string = string.strip("\n")
                error_message_one = (f"|| ERROR! CONTAINS EXTRA WHITESPACES OR BRAQUETS || {string}\n")
                ordered_bibliography_maker(error_message_one)
                adding_the_whole(error_message_one)
                print(error_message_one)
                continue
            unordered_bib[stripped_ref] = call_ref[1]
    for key in ref_order_dict:
        if key in unordered_bib:
            ordered_bibliography_maker(f"{key}|[{str(ref_index)}] {unordered_bib[key]}")
            adding_the_whole(f"[{str(ref_index)}] {unordered_bib[key]}")
            ref_index +=1
        else:
            error_message_two = (f"|| ERROR! NOT FOUND || {key}|[{ref_index}]\n")
            ordered_bibliography_maker(error_message_two)
            adding_the_whole(error_message_two)
            print(error_message_two)
            ref_index += 1

     
if __name__ == "__main__":
    print("bib_reorder running as main")
 

