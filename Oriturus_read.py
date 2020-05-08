## reading all the info
import ref_ordering as ro
import re
import sys
def oriturus_read(file_lines,ref_start_signaler):

    class tag_object(): #tag object that contains the name and the diccionary with all the references
        def __init__(self,tag_long):
            self.tag_long = tag_long
            self.ref_list = []
        def add_ref_info(self,ref): #will add references to the dictionary 
            if ref not in self.ref_list: 
                self.ref_list.append(ref) #add the reference


    def tag_adder(caught_string,tag_dict,linenum):
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
            
            #because simplest type tag is [tag.] and it does not fall into any category it is ignored
        except:
            print(f'ERROR! line {linenum} "{tag_caller.group(1)}." tag not found make sure to initalize it with !!{tag_caller.group(1)}>>some_name!')

    def ref_adder(caught_string,ref_list):
        
        category_lookup = re.search("\[((.+)(\,|\-)(.+)\])",caught_string) # check if it is a complicated type ref ex. [REF1,REF2-REF3,REF4]
        if category_lookup == None:
            pass
        else:
            #group 1 catches REF1,REF2-REF3,REF4]
            ref_list = ro.ref_indexer(category_lookup.group(1),ref_list) #call ref_ordering module to deal with it
            return ref_list
        
        
        category_lookup = re.search("\[(.+)\]",caught_string) # simple type ref [REF]
        #group 1 catches REF
        if category_lookup.group(1) not in ref_list: #check if REF isn't in the dictionary
            ref_list.append(category_lookup.group(1))
            return ref_list
        else:
            return ref_list #if it is in the dictionary return eveything

    tag_dict = {}
    ref_list = []

    #making tags 
    #read everything and if you see anything like !!tag>>name!
    #even reading the whole text could slow the program this method let's us write the tags wherever we want
    for line in file_lines:
            tag_catcher = re.search("^!{2}(.+)>>{1}(.+)!",line)
            #group 1 catches tag
            #group 2 catches name
            if tag_catcher == None:
                pass
            else:
                tag_dict[tag_catcher.group(1)] = tag_object(tag_catcher.group(2)) #add to the tag dict the "tag" make an object from it and initialize this object with "name"
                continue


    # READING
    
    for linenum, line in enumerate(file_lines):

        # look for the tag !!ref_start once found stop reading and tell return the signaler as 1
        if "!!ref_start" in line: 
            ref_start_signaler = 1 
            break
        
        tag_catcher = re.search("^!{2}(.+)>>{1}(.+)!",line)
        #group 1 catches tag
        #group 2 catches name
        if tag_catcher == None:
            pass
        else:
            continue

        line_as_strings = line.split() #split the line into strings
        for string in line_as_strings: #start looking at each string to see if it falls into any category
                
                category_lookup = re.search("(\[(.+)\]){2,}",string) #two or more braquets causes errors
                if category_lookup == None:
                    pass
                else:
                    continue
                    
                category_lookup = re.search("\[(.+)\.(.+)?\]",string) #type tag ex. [tag.REF1-REF2,REF3] or [tag.REF4] or [tag.]
                if category_lookup == None:
                    pass # if it doesn't fall into this type check the other
                else:
                    tag_adder(string,tag_dict,linenum+1)
                    continue
                    
                
                category_lookup = re.search("\[(.+)\]",string) #type ref [REF1,REF2-REF3] or [REF]
                if category_lookup == None:
                    continue #if it doesn't fall into this type just continue reading
                else:
                    ref_list = ref_adder(string,ref_list)

            
    # READING 
    return tag_dict,ref_list,ref_start_signaler

if __name__ == "__main__":
    print("Oriturus_read running as main")