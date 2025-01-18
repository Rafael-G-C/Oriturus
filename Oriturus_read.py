import re

#tag object that contains the name and the dictionary with all the references
class tag_object: 
        def __init__(self,tag_long):
            self.tag_long = tag_long
            self.ref_dict = {}

def oriturus_read(file_lines):

    def tag_ref_adder(caught_string,tag_dict,linenum):
        #remove the "[]"" and split it using the "." 
        #the length of the split defines a Reference (1) or tag (2)
        #a second split is done to get all the references and add them accordingly
        #if they were declared otherwise return error
        cleaned_string = caught_string.strip('[]').split(".")
        
        if len(cleaned_string) == 1 and "REFERENCES" in tag_dict:
            refs = cleaned_string[0].split(",")
            for ref in refs:
                if ref in tag_dict["REFERENCES"].ref_dict and ref not in changes_dict["ref_order"]:
                    changes_dict["ref_order"][ref] = len(changes_dict["ref_order"]) + 1
                    return
            
                elif ref not in tag_dict["REFERENCES"].ref_dict:
                    return f'line {linenum + 1} "{ref}" reference not declared'
        
        elif len(cleaned_string) == 2:        
            tag = cleaned_string[0]
            refs = cleaned_string[1].split(",")

            if tag not in tag_dict:
                return f'line {linenum + 1} "{tag}" tag not declared'
            
            for ref in refs:
                if ref not in tag_dict[tag].ref_dict and ref != '':
                    tag_dict[tag].ref_dict[ref] = len(tag_dict[tag].ref_dict) + 1
            return
                


    #changes_dict is used to track what lines to remove, change and the order of the refs    
    changes_dict = {"remove" : {}, "change": {}, "ref_order" : {}, "errors": []}
    tag_dict = {}

    if "!!ref_start!\n" in file_lines:
        reference_tag = tag_object("REFERENCES")
        tag_dict = {"REFERENCES" : reference_tag}
        ref_line = file_lines.index("!!ref_start!\n") + 1
        changes_dict["REFERENCES"] = ref_line
        try:
            for reference in file_lines[changes_dict["REFERENCES"]:]:
                reference = reference.split(" ", 1)
                tag_dict["REFERENCES"].ref_dict[reference[0].strip("[]")] = reference[1]
        except:
            print("No References below !!ref_start")
    
        file_lines = file_lines[:ref_line]
    else:
        print("No !!ref_start in file. References won't be ordered")
    #begin reading lines
    for linenum, line in enumerate(file_lines):
        
        #!!item[0]>>item[1]!
        tag_declare = re.findall("!{2}(.+)>>{1}(.+)!",line)
        for item in tag_declare:  
            changes_dict["remove"][linenum] = None
            tag_dict[item[0]] = tag_object(item[1]) 

        #any type of tag [a] [b.] [a,b,c] [ex.a,b,c]
        tag_ref_catcher = re.findall("\[[^[]+\]",line)
        for item in tag_ref_catcher:
            changes_dict["change"][linenum] = None
            error = tag_ref_adder(item,tag_dict,linenum)
            if error != None:
                changes_dict["errors"].append(error)

    return tag_dict,changes_dict     

if __name__ == "__main__":
    print("Oriturus_read running as main")