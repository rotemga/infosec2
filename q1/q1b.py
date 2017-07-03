def fix_message(path):
    with open(path, 'rb') as reader:
        data = reader.read()
    # Fix message...

    #update first char to be the xor result.
    #validate return true if first char equal to the xor result.
    #So, this change will cause validate to return True on the fixed msg.
    data = bytearray(data)
    xor_result = 219 #this value is given in hexadecimal.

    size = data[0]

    if (len(data) < size):#if the size is not right, we fix the msg in a different way.
	data[0] = 0;
	data[1] = 219;
	
    else:
	    first_char = data[1]  
	    i = 0
	    while (i < size):
		ch = data[i+2]    	
	    	xor_result = xor_result ^ ch
		i = i+1
	
	    data[1] = xor_result



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
