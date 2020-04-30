import cont_refs as cr
import copy as cp
def ref_indexer(article_text):
    #text = "hello [1,2] and [YOLE] and [Yile,Alo] but [2-4]"
    #if you see "[" start reference and read until "," read the other one or "]" to finish the reference
    ref_looker = 0
    holding_refs = {}
    ref_index = 1
    ref_as_word = ""
    last_char_signaler = 0
    bib_line = 0
    for linenum, text in enumerate(article_text):
        if "!!ref_start" in text:
            bib_line = linenum
            break
        for char in text:
            if char == "[":
                ref_looker = 1
            elif char == "]":
                ref_as_word.strip()
                if ref_as_word not in holding_refs:
                    if last_char_signaler == 1:
                        last_char = ref_as_word
                        middle_refs = cr.middle_ref_maker(previous_char,last_char)
                        for ref in middle_refs:
                            holding_refs[ref] = ref_index
                            ref_index += 1
                        ref_looker = 0
                        ref_as_word = ""
                        last_char_signaler = 0
                    else:
                        holding_refs[ref_as_word] = ref_index
                        ref_looker = 0
                        ref_index += 1
                        ref_as_word = ""
                else:
                    ref_as_word = ""
                    ref_looker = 0
            elif ref_looker == 1:
                ref_as_word.strip()
                if char == ",":
                    if ref_as_word not in holding_refs:
                        holding_refs[ref_as_word] = ref_index
                        ref_as_word = ""
                        ref_index += 1
                    else:
                        ref_as_word = ""
                elif char == "-":
                    last_char_signaler = 1
                    previous_char = cp.deepcopy(ref_as_word)
                    ref_as_word = ""
                else:
                    #print(char,end="")
                    ref_as_word += char

    return holding_refs, bib_line
    #print("article_ref,first_instance")
    #for key in holding_refs:
        #print(f"{key},{holding_refs[key]}")
    #print(holding_refs)
if __name__ == "__main__":
    print("reference_ordering is running as main")
    path_to_file = ""
    #read the file
    with open (path_to_file,"r") as article:
        article_text = article.readlines()
    
    holding_refs,bib_line = ref_indexer(article_text)
    print(holding_refs)
