import reference_ordering as ro #get the reference dictionary for ref_dict
path = "/home/kilimanjaro/Documents/acs/bibliography"
#open bibliography
with open (path) as bibliography:
    bib_ref = bibliography.readlines()
    bibliography.close()
def restructured_ref(ref):
    stripped_ref = ref.strip()
    r_ref = "["+stripped_ref+"]"
    return r_ref


#ref_dict = {"YOLE" : 1, "Yale" :2}
#string_one = ["[Yale] Author year","[YOLE] Author year","[Yoel] Author year"]
#grab the bibliography and print the references in order

ref_dict = ro.ref_indexer()
ref_index = 0
breaker = 1
key_counter = 0
while True:
    if key_counter == len(ref_dict):
        break 
    for key in ref_dict:
        if breaker == 0:
            print(f"****** {r_key} not found ******\n")
        r_key = restructured_ref(key)
        key_counter += 1
        for string in bib_ref:
            if r_key in string:
                #print(f"[{ref_dict[key]}]| {string}")
                breaker = 1
                break
            breaker = 0
 

