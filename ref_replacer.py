#list_string = ["I'm a tree [1] but not a bird [bird,3] but im a flower [3-flower]","perhaps if i were a bird [flower]"]
#ref_order_dict = {"bird":1,"3":2,"1":3,"flower":4}
def text_remaker(path_to_file,name_of_file,file_lines,ref_order_dict,bib_line):
    def file_writer(new_string,path,output_text):
        with open(path+output_text,"a+") as ordered:
            ordered.write(new_string)

    output_text = "ordered_"+name_of_file #need a name

    with open (path_to_file+name_of_file) as article:
        article_text = article.readlines()


    recieve_input = 0
    word_constructor = ""
    new_string = ""
    for linenum, string in enumerate(article_text):
        if linenum == bib_line:
            break
        for char in string:
            if char == "[":
                new_string += char
                recieve_input = 1
            elif char == "]":
                new_string += str(ref_order_dict[word_constructor])
                new_string += char
                recieve_input = 0
                word_constructor = ""
            elif recieve_input == 1:
                if char == "," or char == "-":
                    new_string += str(ref_order_dict[word_constructor])
                    new_string += char
                    word_constructor = ""
                else:
                    word_constructor += char
            else:
                new_string += char
        file_writer(new_string,path_to_file,output_text)
        new_string = ""

if __name__ == "__main__":
    print("ref_replacer running as main")
    pass
        
        

