## reading all the info
import ref_ordering as ro
import re
def oriturus_read(file_lines):

    class tag_object():
        def __init__(self,tag_long):
            self.tag_long = tag_long
            self.ref_info_dict = {}
        def add_ref_info(self,ref):
            if ref not in self.ref_info_dict:
                ref_index = len(self.ref_info_dict)
                self.ref_info_dict[ref] = ref_index + 1

    def tag_adder(caught_string,tag_dict):
        word_constructor = ""
        tag_caller = re.search("\[(.+)\.(.+(\-|\,).+)\]",caught_string)
        if tag_caller == None:
            pass
        else:
            for char in tag_caller.group(2):
                if char != "-" and char != ",":
                    word_constructor += char
                else:
                    tag_dict[tag_caller.group(1)].add_ref_info(word_constructor)
                    word_constructor = ""
            tag_dict[tag_caller.group(1)].add_ref_info(word_constructor)
            return
            
        tag_caller = re.search("\[(.+)\.(.+)\]",caught_string)
        if tag_caller == None:
            pass
        else:
            tag_dict[tag_caller.group(1)].add_ref_info(tag_caller.group(2))

    def ref_adder(caught_string,ref_info_dict,ref_index):
        category_lookup = re.search("\[((.+)(\,|\-)(.+)\])",caught_string) # complicated type ref
        if category_lookup == None:
            pass
        else:
            ref_info_dict,ref_index = ro.ref_indexer(category_lookup.group(1),ref_info_dict,ref_index)
            return ref_info_dict, ref_index
        
        
        category_lookup = re.search("\[(.+)\]",caught_string) # simple type ref
        if category_lookup.group(1) not in ref_info_dict:
            ref_info_dict[category_lookup.group(1)] = ref_index
            ref_index += 1
            return ref_info_dict, ref_index
        else:
            return ref_info_dict, ref_index

    tag_dict = {}
    ref_info_dict = {}
    volatile_dict = {}
    ref_index = 1
    bib_line = 0

    #making tags
    for line in file_lines:
            tag_catcher = re.search("^!{2}(.+)>>{1}(.+)!",line)
            if tag_catcher == None:
                pass
            else:
                tag_dict[tag_catcher.group(1)] = tag_object(tag_catcher.group(2))
                continue


    # READING
    for line in file_lines:

        if "!!ref_start" in line:
            break

        line_as_strings = line.split()
        for string in line_as_strings:

            category_lookup = re.search("\[(.+)\.(.+)?\]",string)
            if category_lookup == None:
                pass
            else:
                tag_adder(string,tag_dict)
                continue
            
            category_lookup = re.search("\[(.+)\]",string)
            if category_lookup == None:
                pass
            else:
                ref_info_dict,ref_index = ref_adder(string,ref_info_dict,ref_index)
                continue
            
            continue
    # READING 
    return tag_dict,ref_info_dict