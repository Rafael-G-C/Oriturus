import cont_refs as cr
import copy as cp
# because complicated type refs ex [REF1,REF2-REF3,REF4] may contain multiple and different combinations of "," and "-" and references then
#we need to look re write the refs from each char and stop whenever we see a "," "-" or "]" and see if the re written ref is in the dictionary if it's not then
#add it, otherwise ignore it

## A bug was found on 5/may/2020. bug [REF1-REF3] [A] [B] [REF1-REF4] translates into [1-3] [4] [5] [1-6] because there is a global index and REF4 is added last it is given the wrong index

def ref_indexer(caught_ref,full_dict,ref_index,linenum):
    volatile_dict = {}
    ref_constructor = ""
    last_char_signaler = 0
    
    for char in caught_ref:
        if char != "]" and char != "," : #if the character isn't a terminator continue
            pass
        else:
            if ref_constructor not in full_dict: #if the word isn't in the dictionary 

                if last_char_signaler == 1: # if there was a hyphen
                    

                    middle_refs = cr.middle_ref_maker(previous_char,ref_constructor) #construct the middle refs ex REF1,REF2,REF3,REF4

                    for ref in middle_refs: #add them to a volatile dictionary the dictionary
                        if ref not in full_dict:
                            if previous_char in full_dict:
                            
                                print(f"WARNING!! line {linenum} {previous_char} already in reference dictionary {ref} could have the wrong index")
                                pass
                        
                            volatile_dict[ref] = ref_index
                            ref_index += 1


                    ref_constructor = "" 
                    last_char_signaler = 0
                    continue

                else:
                    volatile_dict[ref_constructor] = ref_index
                    ref_index += 1
                    ref_constructor = ""
                    continue
            
            else:
                ref_constructor = ""
                continue

        #hyphened references start at one reference and end at another reference many numbers after the last one ex. [REF1-REF5]
        #we need to add these middle refs into the dictionary ex REF1 REF2 REF3 REF4 REF5
        if char == "-":
            last_char_signaler = 1
            previous_char = cp.deepcopy(ref_constructor)
            ref_constructor = ""
            continue

        ref_constructor += char #adding the chars to a string


    full_dict.update(volatile_dict) #update the dictionary
    return full_dict, ref_index

if __name__ == "__main__":
    print("ref_ordering is running as main")
