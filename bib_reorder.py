import re
def bib_writer(ref_init,file_lines,path_to_file=None,name_of_file=None,ref_list=None,tag_dict=None,unordered_bib=None,read_write=None):

#the script that writes the bibliography in order

    class tag_object(): #tag object that contains the name and the diccionary with all the references
        def __init__(self,tag_long):
            self.tag_long = tag_long
            self.ref_list = []
        def add_ref_info(self,ref): #will add references to the dictionary 
            if ref not in self.ref_list: 
                self.ref_list.append(ref) #add the reference
        
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
        with open(path_to_file+"TAGS_"+name_of_file,"a+") as ordered_bibliography:
            ordered_bibliography.write(line)
    
    def add_to_text(line): #adds text to the main file
        with open(path_to_file+"ORDERED_"+name_of_file,"a") as full_text:
            full_text.write(line)

    if ref_init == True:
        tag_dict = {}
        unordered_bib = {}
        bib_start = 0
        for linenum, line in enumerate(file_lines):
            
            tag_catcher = re.search("!{2}(.+)>>{1}(.+)!",line)
            #group 1 catches tag
            #group 2 catches name
            if tag_catcher == None:
                pass
            else:
                tag_dict[tag_catcher.group(1)] = tag_object(tag_catcher.group(2)) #add to the tag dict the "tag" make an object from it and initialize this object with "name"
                continue
            
            if "!!ref_start" in line: #start looking for refs after !!ref_start
                bib_start = 1
                continue
            elif bib_start == 1 and line.startswith("\n") == False:
                pass
            else:
                continue
            
            call_ref = line.split(" ",1) #the refs have the format [REF] words so it can be splitted at the first space
            stripped_ref,error_code = ref_stripper(call_ref[0]) #return REF and check if something is wrong
            
            if error_code == 1: #print error message and write it to the file and the bib file
                line = line.strip("\n")
                error_message_one = (f"|| ERROR! line: {linenum+1} CONTAINS EXTRA WHITESPACES OR BRAQUETS ||\n")
                if read_write == 1:
                    ordered_bibliography_maker(error_message_one)
                    add_to_text(error_message_one)
                    print(error_message_one)
                else:
                    print(error_message_one)
                continue

            try:
                unordered_bib[stripped_ref] = call_ref[1] #add REF as a key to a dictionary that has words as value
            except:
                print(f"ERROR! line {linenum+1} no information on {call_ref[0]}")
                unordered_bib[stripped_ref] = "ERROR! no information found"
        return unordered_bib,bib_start,tag_dict

    else:
        for key in ref_list: #for every key in ref_list 
                ordered_bibliography_maker(f"{key}|[{ref_list.index(key)+1}] {unordered_bib[key]}\n")
                add_to_text(f"[{ref_list.index(key)+1}] {unordered_bib[key]}\n")
        
        for tag in tag_dict:
            if len(tag_dict[tag].ref_list) == 0:
                ordered_bibliography_maker(f"{tag}.|{tag_dict[tag].tag_long}\n")
            else:
                for ref in tag_dict[tag].ref_list:
                    ordered_bibliography_maker(f"{tag}.{ref}|{tag_dict[tag].tag_long}{tag_dict[tag].ref_list.index(ref)+1}\n")



     
if __name__ == "__main__":
    print("bib_reorder running as main")
 

