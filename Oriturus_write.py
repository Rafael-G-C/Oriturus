import re
import copy as cp

def oriturus_write(file_lines,tag_dict,changes_dict):

    def ref_handler(found_refs,dictionary):
        #gets send the refs on the current working tag and the dictinary it belongs to
        if found_refs[0] == '':
            return ''
        
        #changes gets the numbers of the refs in a list
        refs = []
        for ref in found_refs:
            refs.append(dictionary[ref])
            
        #gets a working copy out of said list
        #makes a list of sequential references given the current lenght of the working list and the starting number
        #ex. [1,2,3] given a length "3" and a starting number "1"
        #if there are only two refs then add a comma otherwise if they are consecutive add a hyphen ex. [2,4] = 2,4 [2,3,4] = 2-4
        #remove those from the working directory and go over it again
        refs.sort()
        working = cp.deepcopy(refs)
        cleaned = []
        
        while len(working) > 0:
            cont = [working[0] + n for n in range(len(working))]
            if len(working) <= 2 and working == cont:
                cleaned.append(",".join(str(item) for item in refs))
                working = refs[refs.index(refs[-1]) + 1:]
            elif working == cont:
                cleaned.append(f"{refs[0]}-{refs[-1]}")
                working = refs[refs.index(refs[-1]) + 1:]
            else:
                working.pop(-1)
        return ",".join(cleaned)
    
    def tag_replacer(line):
        #cycles through all the tags found
        #remove the "[]"" and split it using the "." 
        #the length of the split defines a Reference (1) or tag (2)
        #a second split is done to get all the references and fix them
        tag_ref_catcher = re.findall("\[[^[]+\]",line)
        swapped_str = ""
        for tag_caught in tag_ref_catcher:
            cleaned_string = tag_caught.strip('[]').split(".")
            
            if len(cleaned_string) == 1:
                refs = cleaned_string[0].split(",")
                
                #"all" compares that all the tags in ref are in ref_order dict if they are it returns true
                if all(ref in changes_dict["ref_order"] for ref in refs):
                    swapped_str = ref_handler(refs,changes_dict["ref_order"])
                    line = line.replace(tag_caught,f"[{swapped_str}]")
            
            elif len(cleaned_string) == 2:
                tag = cleaned_string[0]
                refs = cleaned_string[1].split(",")
                if tag in tag_dict:
                    swapped_str = f"{tag_dict[tag].tag_long}"
                    refs = ref_handler(refs,tag_dict[tag].ref_dict)
                    line = line.replace(tag_caught,f"{swapped_str}{refs}")

        return line
    
    for removal in changes_dict["remove"]:
        file_lines[removal] = ""
    
    for change in changes_dict["change"]:
        file_lines[change] = tag_replacer(file_lines[change])
    
    if "!!ref_start!\n" in file_lines:
        file_lines = file_lines[:changes_dict["REFERENCES"] - 1]
        for index, reference in enumerate(changes_dict["ref_order"]):
            file_lines.append(f"[{index + 1}] {tag_dict['REFERENCES'].ref_dict[reference]}")    

    return file_lines


if __name__ == "__main__":
    print("Oriturus_write running as main")