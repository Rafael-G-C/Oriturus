import cont_refs as cr
import copy as cp
def ref_indexer(caught_ref,full_dict,ref_index):
    volatile_dict = {}
    ref_constructor = ""
    last_char_signaler = 0
    
    for char in caught_ref:
        if char != "]" and char != "," :
            pass
        else:
            if ref_constructor not in full_dict:

                if last_char_signaler == 1:

                    middle_refs = cr.middle_ref_maker(previous_char,ref_constructor)

                    for ref in middle_refs:
                        if ref not in full_dict:
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

        if char == "-":
            last_char_signaler = 1
            previous_char = cp.deepcopy(ref_constructor)
            ref_constructor = ""
            continue

        ref_constructor += char #adding the chars to a string


    full_dict.update(volatile_dict)
    return full_dict, ref_index

if __name__ == "__main__":
    print("ref_ordering is running as main")
