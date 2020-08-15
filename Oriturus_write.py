import ref_replacer as rp
import re
# Oriturus sends every line in the file and it may fall into the tag category [tag.name] or the ref category [REF]
#oriturus write checks which category is and writes the corresponding information
def oriturus_write(line,tag_dict,ref_list,linenum):
    #
    def tag_replacer(caught_string,tag_dict,linenum):
        try:
            tag_caller = re.search("\[(.+)\.(.+(\-|\,).+\])",caught_string) #complicated type tag [tag.REF1-REF2,REF3]
            if tag_caller == None:
                pass
            else:
                #group 2 catches REF1-REF2,REF3]
                ordered_tag_refs = rp.text_writer(tag_caller.group(2),tag_dict[tag_caller.group(1)].ref_list)
                new_string = f"{tag_dict[tag_caller.group(1)].tag_long}{ordered_tag_refs}"
                return new_string,True

            tag_caller = re.search("\[(.+)\.(.+)\]",caught_string) #simple type tag [tag.name]
            #group 1 catches tag
            #group 2 catches name
            if tag_caller == None:
                pass
            else:
                new_string = f"{tag_dict[tag_caller.group(1)].tag_long}{tag_dict[tag_caller.group(1)].ref_list.index(tag_caller.group(2))+1}"
                return new_string,True
            
            #we just print the tag long
            tag_caller = re.search("\[(.+)\.]",caught_string) # simplest type tag [a.]
            new_string = f"{tag_dict[tag_caller.group(1)].tag_long}"
            return new_string,True
        except:
            return "default",False

    def ref_replacer(caught_string,ref_list):
        try:
            ref_catcher = re.search("\[((.+)(\,|\-)(.+)\])",caught_string) # complicated type ref [REF1,REF2-REF3,REF4]
            #group 1 catches REF1,REF2-REF3,REF4]
            if ref_catcher == None:
                pass
            else:
                replaced_string = rp.text_writer(ref_catcher.group(1),ref_list)
                replaced_string = "[" + replaced_string + "]"
                return replaced_string,True

            ref_catcher = re.search("\[(.+)\]",caught_string) # simple type ref [REF1]
            #group 1 catches REF1
            replaced_string = str(f"[{ref_list.index(ref_catcher.group(1))+1}]")
            return replaced_string,True
        except:
            return "default",False

    #WRITTING
    #because words could be mixed with the refs or tags ex hello[REF]bye we catch them and write them along with the changed ref
    line = re.sub("\[![^\[\]]+\]","",line) # delete al comment tags

    category_lookup = re.findall("(\[[^\[\]]+\.[^\[\]]*\])",line) #tag catcher
    if len(category_lookup) == 0:
        pass
    else:
        for item in category_lookup:
            cleaned_item = item.replace(" ","")
            replaced_string,check = tag_replacer(cleaned_item,tag_dict,linenum)
            if check == True:
                line = line.replace(item,replaced_string)
    
    category_lookup = re.findall("\[[^\[\]\.]+\]",line) # ref catcher
    if len(category_lookup) == 0:
        pass
    else:
        for item in category_lookup:
            cleaned_item = item.replace(" ","")
            replaced_string,check = ref_replacer(cleaned_item,ref_list)
            if check == True:
                line = line.replace(item,replaced_string)
        
    return line
    #WRITTING

if __name__ == "__main__":
    print("Oriturus_write running as main")