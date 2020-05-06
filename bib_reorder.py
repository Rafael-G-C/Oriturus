def bib_writer(file_lines,path_to_file,name_of_file,ref_order_dict):

#the script that writes the bibliography in order

    def ref_stripper(ref): #strips the braquets from the ref, if there are more braquets than it should ir sends an error code
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
    
    
    def ordered_bibliography_maker(line): #adds text to the bib file
        with open(path_to_file+"RAW_BIB_"+name_of_file,"a+") as ordered_bibliography:
            ordered_bibliography.write(line)
    
    def add_to_text(line): #adds text to the main file
        with open(path_to_file+"ORDERED_"+name_of_file,"a") as full_text:
            full_text.write(line)

    


    ref_index = 1
    unordered_bib = {}
    bib_start = 0
    for line in file_lines:
        
        if "!!ref_start" in line: #start looking for refs after !!ref_start
            bib_start = 1
            continue
        else:
            if bib_start == 1:
                pass
            else:
                continue
        
        call_ref = line.split(" ",1) #the refs have the format [REF] words so it can be splitted at the first space
        stripped_ref,error_code = ref_stripper(call_ref[0]) #return REF and check if something is wrong
        
        if error_code == 1: #print error message and write it to the file and the bib file
            line = line.strip("\n")
            error_message_one = (f"|| ERROR! CONTAINS EXTRA WHITESPACES OR BRAQUETS || {line}\n")
            ordered_bibliography_maker(error_message_one)
            add_to_text(error_message_one)
            print(error_message_one)
            continue
        
        unordered_bib[stripped_ref] = call_ref[1] #add REF as a key to a dictionary that has words as value
    
    for key in ref_order_dict: #for every key in the ordered dict 
        if key in unordered_bib: #check every key in the dictionary that was just made and if they match write the ordered ref
            ordered_bibliography_maker(f"{key}|[{str(ref_index)}] {unordered_bib[key]}")
            add_to_text(f"[{str(ref_index)}] {unordered_bib[key]}")
            ref_index +=1
        else: #otherwise send the error message
            error_message_two = (f"|| ERROR! NOT FOUND || {key}|[{ref_index}]\n")
            ordered_bibliography_maker(error_message_two)
            add_to_text(error_message_two)
            print(error_message_two)
            ref_index += 1

     
if __name__ == "__main__":
    print("bib_reorder running as main")
 

