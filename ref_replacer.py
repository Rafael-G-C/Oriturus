def text_writer(path_to_file,name_of_file,file_lines,ref_order_dict,bib_line):
    
    def text_rewriter(new_line,path_to_file,name_of_file):
        with open(path_to_file+"ORDERED_"+name_of_file,"a+") as ordered:
            ordered.write(new_line)


    recieve_input = 0
    ref_constructor = ""
    new_line = ""
    for linenum, line in enumerate(file_lines):
        if linenum == bib_line:
            break
        for char in line:
            if char == "[":
                new_line += char
                recieve_input = 1
            elif char == "]":
                new_line += str(ref_order_dict[ref_constructor])
                new_line += char
                recieve_input = 0
                ref_constructor = ""
            elif recieve_input == 1:
                if char == "," or char == "-":
                    new_line += str(ref_order_dict[ref_constructor])
                    new_line += char
                    ref_constructor = ""
                else:
                    ref_constructor += char
                    ref_constructor = ref_constructor.strip()
            else:
                new_line += char
        
        text_rewriter(new_line,path_to_file,name_of_file)
        new_line = ""

if __name__ == "__main__":
    print("ref_replacer running as main")
        
        

