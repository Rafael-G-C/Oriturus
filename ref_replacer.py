def text_writer(caught_ref,full_dict):
    
    """def text_rewriter(new_line,path_to_file,name_of_file):
        with open(path_to_file+"ORDERED_"+name_of_file,"a+") as ordered:
            ordered.write(new_line """
            #text_rewriter(new_line,path_to_file,name_of_file)

    
    ref_constructor = ""
    new_line = ""
    
    for char in caught_ref:
        if char != "]" and char != "," and char != "-" :
            pass
        else:
            new_line += str(full_dict[ref_constructor])
            new_line += char
            ref_constructor = ""
            continue

        ref_constructor += char

    new_line = "[" + new_line
    return new_line

if __name__ == "__main__":
    print("ref_replacer running as main")
        
        

