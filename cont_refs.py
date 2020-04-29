import copy as cp
def middle_ref_maker(first_ref,last_ref):
    def middle_int_rebuilder(first_int,last_int):
        middle_digits = []
        for integer in range(first_int,last_int+1):
            middle_digits.append(integer)
        return middle_digits



    def middle_rebuilder(ref_name,first_ref,last_ref,middle_digits):
        middle_strings = []
        copied_string = cp.deepcopy(ref_name)
        for integer in middle_digits:
            ref_name += str(integer)
            middle_strings.append(ref_name)
            ref_name = copied_string

        return middle_strings

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
        
        
        return middle_refs
    
    middle_refs = main(first_ref,last_ref)
    
    return middle_refs
        

if __name__ == "__main__":
    first_ref = "A10"
    last_ref = "A15"
    middle_refs = middle_ref_maker(first_ref,last_ref)
    print(middle_refs)
