import ref_replacer as rp
import re
# Oriturus sends every line in the file and it may fall into the tag category [tag.name] or the ref category [REF]
#oriturus write checks which category is and writes the corresponding information
def oriturus_write(line,tag_dict,ref_list,linenum):
    #
    def tag_replacer(caught_string,tag_dict,linenum):
        try:
            word_constructor = ""
            tag_index_constructor = []
            tag_caller = re.search("\[(.+)\.(.+(\-|\,).+\])",caught_string) #complicated type tag [tag.REF1-REF2,REF3]
            if tag_caller == None:
                pass
            else:
                #group 2 catches REF1-REF2,REF3]
                for char in tag_caller.group(2):
                    if char != "," and char != "-" and char != "]":
                        word_constructor += char
                    else:
                        tag_index_constructor.append(str(tag_dict[tag_caller.group(1)].ref_list.index(word_constructor)+1))
                        tag_index_constructor.append(char)
                        word_constructor = ""
                joined_list = "".join(tag_index_constructor)
                new_string = f"{tag_dict[tag_caller.group(1)].tag_long}{joined_list}"
                return new_string

            tag_caller = re.search("\[(.+)\.(.+)\]",caught_string) #simple type tag [tag.name]
            #group 1 catches tag
            #group 2 catches name
            if tag_caller == None:
                pass
            else:
                new_string = f"{tag_dict[tag_caller.group(1)].tag_long}{tag_dict[tag_caller.group(1)].ref_list.index(tag_caller.group(2))+1}"
                return new_string
            
            #we just print the tag long
            tag_caller = re.search("\[(.+)\.]",caught_string) # simplest type tag [a.]
            new_string = f"{tag_dict[tag_caller.group(1)].tag_long}"
            return new_string
        except:
            return "ERROR!"

    def ref_replacer(caught_string,ref_list):
        category_lookup = re.search("\[((.+)(\,|\-)(.+)\])",caught_string) # complicated type ref [REF1,REF2-REF3,REF4]
        #group 1 catches REF1,REF2-REF3,REF4]
        if category_lookup == None:
            pass
        else:
            replaced_string = rp.text_writer(category_lookup.group(1),ref_list)
            return replaced_string

        category_lookup = re.search("\[(.+)\]",caught_string) # simple type ref [REF1]
        #group 1 catches REF1
        replaced_string = str(f"[{ref_list.index(category_lookup.group(1))+1}]")
        return replaced_string

    #WRITTING
    #because words could be mixed with the refs or tags ex hello[REF]bye we catch them and write them along with the changed ref
    new_line = ""
    string = ""
    line_as_strings = line.split()
    for string in line_as_strings:

        category_lookup = re.search("(\[(.+)\]){2,}",string)
        if category_lookup == None:
            pass
        else:
            print(f"ERROR! line {linenum} {string} contains side by side braquets")
            string == "ERROR!"
            continue

        category_lookup = re.search("(.+)?\[(.+)\.(.+)?\](.+)?",string) #tag catcher
        if category_lookup == None:
            pass
        else:
            string = tag_replacer(string,tag_dict,linenum)
            if category_lookup.group(1) == None:
                pass
            else:
                string = category_lookup.group(1) + string
            if category_lookup.group(4) == None:
                pass
            else:
                string = string + category_lookup.group(4)
            
            new_line += string + " "
            string = ""
            continue
        
        category_lookup = re.search("(.+)?\[(.+)\](.+)?",string) # ref catcher
        if category_lookup == None:
            pass
        else:
            string = ref_replacer(string,ref_list)
            if category_lookup.group(1) == None:
                pass
            else:
                string = category_lookup.group(1) + string
            if category_lookup.group(3) == None:
                pass
            else:
                string = string + category_lookup.group(3)
            
            new_line += string + " "
            string = ""
            continue
        
        new_line += string + " "
        string = ""
    return new_line
    #WRITTING

if __name__ == "__main__":
    print("Oriturus_write running as main")