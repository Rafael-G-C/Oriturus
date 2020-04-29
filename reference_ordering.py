import cont_refs as cr
import copy as cp
def ref_indexer():
    #read the file
    path = "/home/kilimanjaro/Documents/acs/Compilacion_de_texto.txt"
    with open (path) as article:
        article_text = article.readlines()
        article.close() 
    #text = "hello [1,2] and [YOLE] and [Yile,Alo] but [2-4]"
    #if you see "[" start reference and read until "," read the other one or "]" to finish the reference
    ref_looker = 0
    holding_refs = {}
    ref_index = 1
    ref_as_word = ""
    last_char_signaler = 0
    for text in article_text:
        if "Bibliography" in text:
            break
        for char in text:
            if char == "[":
                ref_looker = 1
            elif char == "]":
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

    return holding_refs
    #print("article_ref,first_instance")
    #for key in holding_refs:
        #print(f"{key},{holding_refs[key]}")
    #print(holding_refs)
if __name__ == "__main__":
    holding_refs = ref_indexer()
    print(holding_refs)
