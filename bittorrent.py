import sys
true_value = None

def decode_bencoded_string(bencoded_string):
    true_string = bencoded_string.split(":")[1]
    return true_string 

def decode_bencoded_integer(bencoded_string):
    true_value = int(bencoded_string[1:-1])
    return true_value

def decode_bencoded_list(bencoded_string):
    true_list = []
    i = 1
    while i < len(bencoded_string):
        if bencoded_string[i].isdigit():
            length = int(bencoded_string[i:i + bencoded_string[i:].index(':')])
            element = decode_bencoded_string(bencoded_string[i:i + length + 2])
            true_list.append(element)
            i += length + 2
        elif bencoded_string[i] == 'i':
            i += 1
            string = ""
            while bencoded_string[i] != 'e':
                string += bencoded_string[i]
                i += 1
            element = decode_bencoded_integer('i' + string + 'e')
            true_list.append(element)
            i += 1
        else:
            i += 1
    return true_list

def decode_bencoded_dictionary(bencoded_string):
    true_dictionary = {}
    decoded_string_in_list = decode_bencoded_list(bencoded_string)
    for a in range(len(decoded_string_in_list)):
        if a%2 == 0:
            true_dictionary[decoded_string_in_list[a]] = decoded_string_in_list[a+1]
            a += 1
        if a == len(decoded_string_in_list)-1 and (len(decoded_string_in_list)-1)%2 == 0:
            true_dictionary[decoded_string_in_list[a]] = None
        else:
            continue
    return true_dictionary
def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <message1> <message2> ...")
        sys.exit(1)

    bencoded_string = sys.argv[2]
    if bencoded_string[0].isdigit():
        decoded_string = decode_bencoded_string(bencoded_string)
    elif bencoded_string[0] == 'i':
        decoded_string = decode_bencoded_integer(bencoded_string)
    elif bencoded_string[0] == 'l':
        decoded_string = decode_bencoded_list(bencoded_string)
    elif bencoded_string[0] == 'd':
        decoded_string = decode_bencoded_dictionary(bencoded_string)
    print("Received message:",decoded_string)

if __name__ == "__main__":
    main()
    