import reference_ordering as ro
#list_string = ["I'm a tree [1] but not a bird [bird,3] but im a flower [3-flower]","perhaps if i were a bird [flower]"]
#ref_replacer_dict = {"bird":1,"3":2,"1":3,"flower":4}

def file_writer(new_string,path,output_text):
    with open(path+output_text,"a+") as ordered:
        ordered.write(new_string)

path = "/home/kilimanjaro/Documents/acs/"
input_text = "Compilacion_de_texto.txt"
output_text = "re_order_text.txt"

with open (path+input_text) as article:
    article_text = article.readlines()


ref_replacer_dict = ro.ref_indexer()
recieve_input = 0
word_constructor = ""
new_string = ""
for string in article_text:
    for char in string:
        if char == "[":
            new_string += char
            recieve_input = 1
        elif char == "]":
            new_string += str(ref_replacer_dict[word_constructor])
            new_string += char
            recieve_input = 0
            word_constructor = ""
        elif recieve_input == 1:
            if char == "," or char == "-":
                new_string += str(ref_replacer_dict[word_constructor])
                new_string += char
                word_constructor = ""
            else:
                word_constructor += char
        else:
            new_string += char
    file_writer(new_string,path,output_text)
    new_string = ""
    
    

