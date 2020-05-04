import re
import ref_ordering as ro
import ref_replacer as rp
#def tag_finder(file_lines):
#recieve the whole text look for tags like this !!tag big_name_of_tag
class tag_object():
    def __init__(self,tag_long):
        self.tag_long = tag_long
        self.ref_info_dict = {}
    def add_ref_info(self,ref):
        if ref not in self.ref_info_dict:
            ref_index = len(self.ref_info_dict)
            self.ref_info_dict[ref] = ref_index + 1


def ref_adder(caught_string):
    pass

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
        print(f'{tag_dict[tag_caller.group(1)].tag_long} {"".join(tag_index_constructor)}',end=" ")
        return
    
    tag_caller = re.search("\[(.+)\.(.+)\]",caught_string)
    if tag_caller == None:
        pass
    else:
        print(f"{tag_dict[tag_caller.group(1)].tag_long} {tag_dict[tag_caller.group(1)].ref_info_dict[tag_caller.group(2)]}.",end=" ")
        return
    tag_caller = re.search("\[(.+)\.]",caught_string)
    print(f"{tag_dict[tag_caller.group(1)].tag_long}",end=" ")




file_lines = ["[azulero] h! [t.REF-BLUE,ALL-REF] DONDE","[good_bye,no1-no5,no5-no7,si] excuse me [no1-no3,hello1-hello3] DONE [azulero]","[t.BLUE] DONE","[fig.] D [fig.REF-AZUL] O [fig.AZUL] N [fig.REF] E im not a bird stop saying it [t.REF].","!!t-Table","[t.BLUE]","[hello] QQQQ PPPPP","!!fig-Figure","tables [good_bye] tttttttt","tobles aaaaaa"]
tag_dict = {}
ref_info_dict = {}
volatile_dict = {}
lines_to_ignore = []
ref_index = 1

#making tags
for line in file_lines:
    line_as_strings = line.split()
    for string in line_as_strings:
        tag_catcher = re.search("^!{2}(.+)-{1}(.+)",string)
        if tag_catcher == None:
            continue
        else:
            tag_dict[tag_catcher.group(1)] = tag_object(tag_catcher.group(2))
            continue


# READING
for line in file_lines:
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
            ref_info_dict,ref_index = ro.ref_indexer(string,ref_info_dict,ref_index)
            continue
        
        continue
# READING 

#WRITTING
for line in file_lines:
    line_as_strings = line.split()
    for string in line_as_strings:

        tag_catcher = re.search("^!{2}(.+)-{1}(.+)",string)
        if tag_catcher == None:
            pass
        else:
            continue

        category_lookup = re.search("\[(.+)\.(.+)?\]",string)
        if category_lookup == None:
            pass
        else:
            tag_replacer(string,tag_dict)
            continue
        
        category_lookup = re.search("\[(.+)\]",string)
        if category_lookup == None:
            pass
        else:
            rp.text_writer(string,ref_info_dict)
            continue
        
        print(string,end=" ")
#WRITTING
        

            
        



