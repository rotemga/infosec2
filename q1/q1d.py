def patch_program(path):
    with open(path, 'rb') as reader:
        data = reader.read()

    # Patch program...

    # In Python, strings are immutable, so let's "cast" it into a bytearray.
    data = bytearray(data)
 
    #offset of result of xor
    offset = 0x593
    #put first_char inside the result of xor (0x596 is the offset of the first char in the string).
    data[offset] = data[0x596]

    #it will always return true with the cmp command.

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
