import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <message1> <message2> ...")
        sys.exit(1)

    messages = sys.argv[2]
    message = messages.split(":")
    print("Received messages:", "".join(message[1]))