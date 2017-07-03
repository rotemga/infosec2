import assemble

def patch_program(path):
    with open(path, 'rb') as reader:
        data = reader.read()
    # Patch program...
    # In Python, strings are immutable, so let's "cast" it into a bytearray.
    data = bytearray(data)
    # Convert the assembly patches to binary string in python.
    patch1 = bytearray(assemble.assemble_file('patch1.asm'))
    patch2 = bytearray(assemble.assemble_file('patch2.asm'))
    # The indexes of the dead zones.
    index_for_patch1 = 0x0633
    index_for_patch2 = 0x05CD
    # Binary patching
    data[index_for_patch1:index_for_patch1 + len(patch1)] = patch1
    data[index_for_patch2:index_for_patch2 + len(patch2)] = patch2

    with open(path + '.patched', 'wb') as writer:
        writer.write(data)


def main(argv):
    if len(argv) != 2:
        print('USAGE: python {} <readfile-program>'.format(argv[0]))
        return -1
    path = argv[1]
    patch_program(path)
    print('done')


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
