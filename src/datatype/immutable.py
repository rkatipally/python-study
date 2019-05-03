def showImmutable():
    print("Strings===")
    print('{0:=<10} | {1:.>20}'.format('Raj', 'Katipally'))
    print('This is single quotes')
    print("this is double quotes")
    print('''this triple quotes 
    with multi line''')
    print(""" this is also triple quotes 
    with multi line""")
    print('length is ', len('Whatever'))
    print("Encoding")
    s = 'This is üŋíc0de'
    encoded_s = s.encode()
    encoded_s_byte = b'this byte code string'
    print(encoded_s)
    print(encoded_s_byte)
    print(type(encoded_s_byte))
    print(encoded_s.decode())

    print("=================String Operations===============")
    s = "The trouble is you think you have time."
    print('at 0 index:: ', s[0])
    print('stop at 4:: ', s[:4])
    print('start at 4:: ', s[4:])
    print('start at 2 and stop at 12:: ', s[2:12])
    print('start at 2 and stop at 12 and step 3:: ', s[2:12:3])
    print('make a copy:: ', s[:])
    print('step at 3:: ', s[::3])
    print('Reverse ::: ', s[len(s)::-1])

    print("=================Tuples==================")
    t = () #this is a tuple
    multi_tuple = (1,2,3)
    a,b,c = 1,2,3
    print("printing tuple:: ", (a,b,c))
    a,b = 1,2
    a,b = b,a
    print('swapping with tuples::: ', a, b )
    print('querying in tuple::: ', 3 in multi_tuple)



showImmutable()
