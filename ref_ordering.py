import cont_refs as cr
import copy as cp
# because complicated type refs ex [REF1,REF2-REF3,REF4] may contain multiple and different combinations of "," and "-" and references then
#we need to look re write the refs from each char and stop whenever we see a "," "-" or "]" and see if the re written ref is in the dictionary if it's not then
#add it, otherwise ignore it

## A bug was found on 5/may/2020. bug [REF1-REF3] [A] [B] [REF1-REF4] translates into [1-3] [4] [5] [1-6] because there is a global index and REF4 is added last it is given the wrong index

def ref_indexer(caught_ref,full_list):
    volatile_list = []
    ref_constructor = ""
    last_char_signaler = 0

    def shift_merge(full_list,middle_refs,previous_ref):
        cuttof_index = full_list.index(previous_ref)
        left_list = full_list[:cuttof_index]
        for ref in middle_refs:
            if ref in full_list:
                cuttof_ref = ref
                continue
            else:
                cuttof_index = full_list.index(cuttof_ref)
                right_list = full_list[cuttof_index+1:]
        
        full_list = left_list + middle_refs + right_list
        return full_list
    
    for char in caught_ref:
        if char != "]" and char != "," : #if the character isn't a terminator continue
            pass
        else:
            if ref_constructor not in full_list: #if the word isn't in the dictionary 

                if last_char_signaler == 1: # if there was a hyphen
                    

                    middle_refs = cr.middle_ref_maker(previous_ref,ref_constructor) #construct the middle refs ex REF1,REF2,REF3,REF4
                    
                    if previous_ref not in full_list:
                        full_list = full_list + middle_refs 
                    else:
                        full_list = shift_merge(full_list,middle_refs,previous_ref)


                    ref_constructor = "" 
                    last_char_signaler = 0
                    continue

                else:
                    volatile_list.append(ref_constructor)
                    ref_constructor = ""
                    continue
            
            else:
                ref_constructor = ""
                continue

        #hyphened references start at one reference and end at another reference many numbers after the last one ex. [REF1-REF5]
        #we need to add these middle refs into the dictionary ex REF1 REF2 REF3 REF4 REF5
        if char == "-":
            last_char_signaler = 1
            previous_ref = cp.deepcopy(ref_constructor)
            ref_constructor = ""
            continue

        ref_constructor += char #adding the chars to a string


    return full_list

if __name__ == "__main__":
    print("ref_ordering is running as main")
