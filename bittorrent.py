import sys
true_value : int
def decode_bencoded_string(bencoded_string):
    true_string = bencoded_string.split(":")[1]
    return true_string 

def decode_bencoded_integer(bencoded_string):
    true_value = bencoded_string[1:len(bencoded_string)-1]
    return true_value


def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <message1> <message2> ...")
        sys.exit(1)

    bencoded_string = sys.argv[2]
    if bencoded_string[0].isdigit():
        decoded_string = decode_bencoded_string(bencoded_string)
    if bencoded_string[0] == 'i':
        decoded_string = decode_bencoded_integer(bencoded_string)

    print("Received message:",decoded_string)

if __name__ == "__main__":
    main()
    