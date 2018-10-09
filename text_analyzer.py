def get_num_of_characters(inputStr):
    # Type your code here
    return len(inputStr)
def output_without_whitespace(inputStr):
    new_string = ""
    for char in inputStr:
        if char in " \t\n":
            pass
        else:
            new_string += char
    return new_string

if __name__ == '__main__':
    # Type your code here
    entered_str = input("Enter a sentence or phrase:\n\n")
    print("You entered:",entered_str)
    #char_num = get_num_of_characters(entered_str)
    print()
    print("Number of characters:",get_num_of_characters(entered_str))
    print("String with no whitespace:",output_without_whitespace(entered_str)) 
