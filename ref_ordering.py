import cont_refs as cr
import copy as cp

def ref_indexer(file_lines):
    recieve_input = 0
    ref_and_index_dict = {}
    ref_index = 1
    ref_constructor = ""
    last_char_signaler = 0
    bib_line = 0
    for linenum, line in enumerate(file_lines):
        if "!!ref_start" in line:
            bib_line = linenum
            break
        for char in line:
            if char == "[":
                recieve_input = 1
            elif char == "]":
                ref_constructor = ref_constructor.strip()
                if ref_constructor not in ref_and_index_dict:
                    if last_char_signaler == 1:
                        last_char = ref_constructor
                        middle_refs = cr.middle_ref_maker(previous_char,last_char)
                        for ref in middle_refs:
                            ref_and_index_dict[ref] = ref_index
                            ref_index += 1
                        recieve_input = 0
                        ref_constructor = ""
                        last_char_signaler = 0
                    else:
                        ref_and_index_dict[ref_constructor] = ref_index
                        recieve_input = 0
                        ref_index += 1
                        ref_constructor = ""
                else:
                    ref_constructor = ""
                    recieve_input = 0
            elif recieve_input == 1:
                ref_constructor = ref_constructor.strip()
                if char == ",":
                    if ref_constructor not in ref_and_index_dict:
                        ref_and_index_dict[ref_constructor] = ref_index
                        ref_constructor = ""
                        ref_index += 1
                    else:
                        ref_constructor = ""
                elif char == "-":
                    last_char_signaler = 1
                    previous_char = cp.deepcopy(ref_constructor)
                    ref_constructor = ""
                else:
                    ref_constructor += char

    return ref_and_index_dict, bib_line

if __name__ == "__main__":
    print("ref_ordering is running as main")
