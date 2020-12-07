## reading all the info
import ref_ordering as ro
import re
import sys
def oriturus_read(file_lines,ref_start_signaler,bib_list,tag_dict):

    def tag_adder(string,caught_string,tag_dict,linenum):
        try:
            word_constructor = ""
            tag_caller = re.search("\[(.+)\.(.+(\-|\,).+\])",caught_string) #check if it is a complicated type tag ex [tag.REF1,REF2-REF3]
            if tag_caller == None:
                pass
            else:
                #group 1 catches tag
                #group 2 catches REF1,REF2-REF3]
                for char in tag_caller.group(2): #go to every char in group two if the char is not a "-" or "," 
                    if char != "-" and char != "," and char != "]":
                        word_constructor += char #write the char
                    else:
                        if char == "-":
                            print(f'WARNING! line {linenum+1} "{string}" ORITURUS DEALS WITH HYPHENS ON ITS OWN THERE IS NO NEED TO WRITE THEM, HYPHEN WILL BE TREATED LIKE A COMMA')
                        
                        tag_dict[tag_caller.group(1)].add_ref_info(word_constructor) #call the tag_dict inside the "tag" key and call the function add_ref_info in it
                        word_constructor = "" #restart the word_constructor
                return
                
            tag_caller = re.search("\[(.+)\.(.+)\]",caught_string) #check if it a simple type tag ex. [tag.REF]
            if tag_caller == None:
                pass
            else:
                #group 1 catches tag
                #group 2 catches REF
                tag_dict[tag_caller.group(1)].add_ref_info(tag_caller.group(2)) #call the tag_dict inside the "tag" key and call the function add_ref_info in it
                return
            if caught_string[1:-2] not in tag_dict:
                raise Exception
            return
        except:
            print(f'WARNING! line {linenum+1} tag not found oriturus will rewrite "{string}"')
            
    def ref_adder(string,caught_string,ref_list,linenum):
        category_lookup = re.search("\[((.+)(\,|\-)(.+)\])",caught_string) # check if it is a complicated type ref ex. [REF1,REF2-REF3,REF4]
        if category_lookup == None:
            pass
        else:
            #group 1 catches REF1,REF2-REF3,REF4]
            ref_list = ro.ref_indexer(string,category_lookup.group(1),ref_list,linenum+1,bib_list) #call ref_ordering module to deal with it
            return ref_list
        
        
        category_lookup = re.search("\[(.+)\]",caught_string) # simple type ref [REF]
        #group 1 catches REF
        if category_lookup.group(1) not in bib_list:
            print(f'WARNING! line {linenum+1} reference not found Oriturus will rewrite "{string}"')
            return ref_list
        
        if category_lookup.group(1) not in ref_list: #check if REF isn't in the dictionary
            ref_list.append(category_lookup.group(1))
            return ref_list
        
        return ref_list #if it is in the dictionary return eveything
            

    ref_list = []
    # READING
    
    for linenum, line in enumerate(file_lines):

        # look for the tag !!ref_start once found stop reading and tell return the signaler as 1
        if "!!ref_start" in line: 
            break
        #!{2}[^!{2}]+!{2}   #Comment type tag
        
        category_lookup = re.search("\[(.+)\]",line) 
        if category_lookup == None:
            continue

        category_lookup = re.findall("(\[[^\[\]]+\.[^\[\]]*\])",line)
        #type tag ex. [tag.REF1-REF2,REF3] or [tag.REF4] or [tag.]
        if len(category_lookup) == 0:
            pass # if it doesn't fall into this type check the other
        else:
            for item in category_lookup:
                cleaned_item = item.replace(" ","")
                tag_adder(item,cleaned_item,tag_dict,linenum+1)
            
        
        if ref_start_signaler != 0:
            category_lookup = re.findall("\[[^\[\]\.\!)]+\]",line) #type ref [REF1,REF2-REF3] or [REF]
            if len(category_lookup) == 0:
                continue #if it doesn't fall into this type just continue reading
            else:
                for item in category_lookup:
                    cleaned_item = item.replace(" ","")
                    ref_list = ref_adder(item,cleaned_item,ref_list,linenum)

            
    # READING 
    return ref_list

if __name__ == "__main__":
    print("Oriturus_read running as main")