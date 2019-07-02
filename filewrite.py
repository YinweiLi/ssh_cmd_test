

for i in range(0,100):
    a = open('test_log.txt', 'a')
    b = str(i)+str(i) + '\n'
    print(b,i,'something')
    a.write(b)
    a.close()

