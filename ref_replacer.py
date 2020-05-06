def text_writer(caught_ref,full_dict):
    
    ref_constructor = ""
    new_line = ""
    
    for char in caught_ref:
        if char != "]" and char != "," and char != "-" : #if the char isn't any terminator
            pass
        else:
            new_line += str(full_dict[ref_constructor]) #if you see any terminator look for it in the dict and write its index
            new_line += char #add the char that triggered this statement
            ref_constructor = ""
            continue

        ref_constructor += char #construct the reference

    new_line = "[" + new_line #the caught refs come as REF,REF] so [ is needed
    return new_line

if __name__ == "__main__":
    print("ref_replacer running as main")
        
        

