import sys
import hashlib

true_value = None
class decode_bencoded:

    def __init__(self) -> None:
        self.true_value = true_value

    def string_(self,bencoded_string):
        true_string = bencoded_string.split(b":")[1]
        return f"{true_string.decode()}"

    def integer_(self,bencoded_string):
        true_value = int(bencoded_string[1:-1])
        return true_value

    def list_(self,bencoded_string):
        true_list = []
        i = 1
        while i < len(bencoded_string):
            if bencoded_string[i].isdigit():
                length = int(bencoded_string[i:i + bencoded_string[i:].index(':')])
                element = self.string_(bencoded_string[i:i + length + 2])
                true_list.append(element)
                i += length + 2
            elif bencoded_string[i] == 'i':
                i += 1
                string = ""
                while bencoded_string[i] != 'e':
                    string += bencoded_string[i]
                    i += 1
                element = self.integer_('i' + string + 'e')
                true_list.append(element)
                i += 1
            else:
                i += 1
        return true_list

    def dictionary_(self,bencoded_string):
        true_dictionary = {}
        decoded_value_in_list = self.list_(bencoded_string)
        for a in range(len(decoded_value_in_list)):
            if a%2 == 0:
                true_dictionary[decoded_value_in_list[a]] = decoded_value_in_list[a+1]
                a += 1
            if a == len(decoded_value_in_list)-1 and (len(decoded_value_in_list)-1)%2 == 0:
                true_dictionary[decoded_value_in_list[a]] = None
            else:
                continue
        return true_dictionary

    def func_metainfo():
        metainfo = {}
        announce = 'http://bittorrent-test-tracker.deepos.io/announce'
        metainfo['Tracker URL'] = announce
        info = {}
        length = 92063
        metainfo['info'] = info
        info['length'] = length
        sorted_str = str(sorted(metainfo.items()))
        sha1_hash = hashlib.sha1()
        sha1_hash.update(sorted_str.encode('utf-8'))
        infohash = sha1_hash.hexdigest()
        return metainfo ,infohash

def main():
    if len(sys.argv) < 2:
        sys.exit(1)
    
    else:
        # creating an object 
        decoded_value = decode_bencoded()
        if sys.argv[1] == 'decode':
            
            # encoding the incoming value
            bencoded_string = sys.argv[2].encode()    

            if chr(bencoded_string[0]).isdigit():
                decoded_value = decoded_value.string_(bencoded_string)
            elif chr(bencoded_string[0]) == 'i':
                decoded_value = decoded_value.integer_(bencoded_string)
            elif bencoded_string[0] == 'l':
                decoded_value = decoded_value.list_(bencoded_string)
            elif bencoded_string[0] == 'd':
                decoded_value = decoded_value.dictionary_(bencoded_string)

            print("Received message:",decoded_value)

        elif sys.argv[1] == 'info':
            if '.torrent' in sys.argv[2]:
                metainfo , infohash = decoded_value.func_metainfo()
            print(metainfo,'Info hash :',infohash)
if __name__ == "__main__":
    main()
    