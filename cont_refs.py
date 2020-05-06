import copy as cp

#this script runs when a hyphen is found and it is given the ref before the hyphen and the ref after the hyphen, and build the refs that should be inbetween
# ex Oriturus1-Oriturus5 should return a list containing Oriturus1,Oriturus2,Oriturus3,Oriturus4,Oriturus5

#return a list of the digits between the refs that ran this script
def middle_ref_maker(first_ref,last_ref):
    def middle_int_rebuilder(first_int,last_int):
        middle_digits = []
        for integer in range(first_int,last_int+1):
            middle_digits.append(integer)
        return middle_digits


    # for every integer that goes inbetween including the starting refs add the base name and that digit into a list
    def middle_rebuilder(ref_name,first_ref,last_ref,middle_digits):
        middle_strings = []
        copied_string = cp.deepcopy(ref_name)
        for integer in middle_digits:
            ref_name += str(integer)
            middle_strings.append(ref_name)
            ref_name = copied_string

        return middle_strings

    #remove every char that isn't a digit. when a digit is found it sends it to middle_int_rebuilder
    def main(first_ref,last_ref):
        index = 0
        ref_name = ""
        ref_copy = cp.deepcopy(first_ref)
        while True:
            test_ref = ref_copy
            test_ref = test_ref[index:]
            if str.isdigit(test_ref):
                first_ref = first_ref[index:]
                last_ref = last_ref[index:]
                middle_digits = middle_int_rebuilder(int(first_ref),int(last_ref))
                middle_refs = middle_rebuilder(ref_name,first_ref,last_ref,middle_digits)
                break
            else:
                ref_name += ref_copy[index]
                index += 1
        
        
        return middle_refs #return a list with the middle refs 
    
    middle_refs = main(first_ref,last_ref)
    
    return middle_refs
        

if __name__ == "__main__":
    first_ref = "A10"
    last_ref = "A15"
    middle_refs = middle_ref_maker(first_ref,last_ref)
    print(middle_refs)
