import copy as cp
# because complicated type refs ex [REF1,REF2-REF3,REF4] may contain multiple and different combinations of "," and "-" and references then
#we need to look re write the refs from each char and stop whenever we see a "," "-" or "]" and see if the re written ref is in the dictionary if it's not then
#add it, otherwise ignore it

## A bug was found on 5/may/2020. bug [REF1-REF3] [A] [B] [REF1-REF4] translates into [1-3] [4] [5] [1-6] because there is a global index and REF4 is added last it is given the wrong index

def ref_indexer(string,caught_ref,full_list,linenum,bib_list):
    ref_constructor = ""
    
    for char in caught_ref:
        if char != "]" and char != "," : #if the character isn't a terminator continue
            pass
        else:
            if ref_constructor not in bib_list:
                print(f'WARNING! line {linenum} reference not found Oriturus will rewrite "{ref_constructor}" in {string}')
                ref_constructor = ""
                continue
            
            if ref_constructor not in full_list: #if the word isn't in the dictionary
                full_list.append(ref_constructor)
                ref_constructor = ""
                continue
            
            ref_constructor = ""
            continue

        if char == "-":
            print(f'WARNING! line {linenum} "{string}" ORITURUS DEALS WITH HYPHENS ON ITS OWN THERE IS NO NEED TO WRITE THEM, HYPHEN WILL BE TREATED LIKE A COMMA')
            ref_constructor = ""
            continue

        ref_constructor += char #adding the chars to a string


    return full_list

if __name__ == "__main__":
    print("ref_ordering is running as main")
