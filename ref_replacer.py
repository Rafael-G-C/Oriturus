def text_writer(caught_ref,full_list):
    
    def coma_hyphen(removed):
        if len(removed) == 1:
            new_line = f"{removed[0]},"
        elif len(removed) == 2:
            new_line = f"{removed[0]},{removed[1]},"
        else:
            new_line = f"{removed[0]}-{removed[-1]},"
        return new_line

    def comp_ref(removed,new_line,ref_list,ref):
        removed.append(ref_list[ref])
        new_line = new_line + coma_hyphen(removed)
        removed.clear()
        return removed, new_line
    
    ref_constructor = ""
    new_line = ""
    ref_list = []
    removed = []
    for char in caught_ref:
        
        if char != "]" and char != "," and char != "-" : #if the char isn't any terminator
            pass
        else:
            ref_list.append(full_list.index(ref_constructor)+1) #if you see any terminator look for it in the dict and write its index
            ref_constructor = ""
            continue

        ref_constructor += char #construct the reference
    
    ref_list.sort()
    for ref in range(len(ref_list)):
        try:
            if ref_list[ref] + 1 == ref_list[ref+1]:
                removed.append(ref_list[ref])
            else:
                removed, new_line = comp_ref(removed,new_line,ref_list,ref)

        except IndexError:
            removed, new_line = comp_ref(removed,new_line,ref_list,ref)
            new_line = new_line[:-1]
            return new_line





if __name__ == "__main__":
    print("ref_replacer running as main")
        
        

