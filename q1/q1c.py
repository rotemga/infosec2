def fix_message(path):
    with open(path, 'rb') as reader:
        data = reader.read()
    # Fix message...

    #update size of the string to be zero. update the first char to be the given hexadecimal value.
    #So, this new msg as input we want get into the loop in validate.
    #It's will only check that the given hexadecimal value that given is equal to the first char, and return true.
    data = bytearray(data)
    data[0] = 0 
    data[1] = 219



    with open(path + '.fixed', 'wb') as writer:
        writer.write(data)


def main(argv):
    if len(argv) != 2:
        print('USAGE: python {} <msg-file>'.format(argv[0]))
        return -1
    path = argv[1]
    fix_message(path)
    print('done')


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
