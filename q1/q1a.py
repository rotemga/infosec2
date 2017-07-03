def check_message(path):

    with open(path, 'rb') as reader:

	data = reader.read()

    # In Python, strings are immutable, so let's "cast" it into a bytearray.
	data = bytearray(data)


    xor_result = 219 #this value is given in hexadecimal.
    size = data[0] #the size of the data array is saved in data[0]
    first_char = data[1] 
    
    #go over data from the second char to the end of the string.
    #xor second char with the hexadecimal value that given and 
    #continuity xor other chars with the result of the previous iteration.
    i = 0
    while (i < size):
	if (len(data) < size):
		return True;
        ch = data[i+2]    	
   	xor_result = xor_result ^ ch
	i = i+1
    #return true if the result from the xor is equal to the first char, else false.
    if (xor_result == first_char):
    	return True
    else:
    	return False
    pass # Check message...


def main(argv):
    if len(argv) != 2:
        print('USAGE: python {} <msg-file>'.format(argv[0]))
        return -1
    path = argv[1]
    if check_message(path):
        print('valid message')
        return 0
    else:
        print('invalid message')
        return 1


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
