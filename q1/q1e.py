def patch_program(path):
    with open(path, 'rb') as reader:
        data = reader.read()
    # Patch program...
    # In Python, strings are immutable, so let's "cast" it into a bytearray.
    data = bytearray(data)
    #offset of mov command we want to change
    offset = 0x6DD 

    #put 0 instead of 1.
    data[offset + 1] = '\0'


    with open(path + '.patched', 'wb') as writer:
        writer.write(data)


def main(argv):
    if len(argv) != 2:
        print('USAGE: python {} <msgcheck-program>'.format(argv[0]))
        return -1
    path = argv[1]
    patch_program(path)
    print('done')


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
