import ref_replacer as rp
import re
def oriturus_write(line,tag_dict,ref_info_dict):
    def tag_replacer(caught_string,tag_dict):
        word_constructor = ""
        tag_index_constructor = []
        tag_caller = re.search("\[(.+)\.(.+(\-|\,).+)\]",caught_string)
        if tag_caller == None:
            pass
        else:
            for char in tag_caller.group(2):
                if char != "," and char != "-":
                    word_constructor += char
                else:
                    tag_index_constructor.append(str(tag_dict[tag_caller.group(1)].ref_info_dict[word_constructor]))
                    tag_index_constructor.append(char)
                    word_constructor = ""
            tag_index_constructor.append(str(tag_dict[tag_caller.group(1)].ref_info_dict[word_constructor]))
            joined_list = "".join(tag_index_constructor)
            new_string = f"{tag_dict[tag_caller.group(1)].tag_long}{joined_list}"
            return new_string

        tag_caller = re.search("\[(.+)\.(.+)\]",caught_string)
        if tag_caller == None:
            pass
        else:
            new_string = f"{tag_dict[tag_caller.group(1)].tag_long}{tag_dict[tag_caller.group(1)].ref_info_dict[tag_caller.group(2)]}"
            return new_string

        tag_caller = re.search("\[(.+)\.]",caught_string)
        new_string = f"{tag_dict[tag_caller.group(1)].tag_long}"
        return new_string

    def ref_replacer(caught_string,ref_info_dict):
        category_lookup = re.search("\[((.+)(\,|\-)(.+)\])",caught_string) # complicated type ref
        if category_lookup == None:
            pass
        else:
            replaced_string = rp.text_writer(category_lookup.group(1),ref_info_dict)
            return replaced_string

        category_lookup = re.search("\[(.+)\]",caught_string) # simple type ref
        if category_lookup.group(1) not in ref_info_dict:
            print("ERROR!!")
        else:
            replaced_string = str(f"[{ref_info_dict[category_lookup.group(1)]}]")
            return replaced_string

    #WRITTING
    new_line = ""
    string = ""
    line_as_strings = line.split()
    for string in line_as_strings:

        category_lookup = re.search("(.+)?\[(.+)\.(.+)?\](.+)?",string)
        if category_lookup == None:
            pass
        else:
            string = tag_replacer(string,tag_dict)
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
        
        category_lookup = re.search("(.+)?\[(.+)\](.+)?",string)
        if category_lookup == None:
            pass
        else:
            string = ref_replacer(string,ref_info_dict)
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