
def compare(file1, file2):
    with open(file1, 'r') as file1:
        content1 = file1.read()
    with open(file2, 'r') as file2:
        content2 = file2.read()
    if content1 == content2:
        return True
    else:
        return False

def restore(modified, original):
    for m, o in zip(modified, original):
        with open(o, 'r') as src_file:
            content = src_file.read()
        with open(m, 'w') as dest_file:
            dest_file.write(content)
        src_file.close()
        dest_file.close()


def test1a():
    filename = 'test1.txt'
    with open(filename, "r+") as my_file:
        my_file.write("========")
        r = my_file.readline()

        my_file.close()
    if compare('test1.txt', 'test1_corr.txt'):
        print('Test 1a - PASSED')
    else:
        print('Test 1a - FAILED')


def test1b():
    filename = 'test1.txt'
    with open(filename, "r+") as my_file:
        my_file.write("========")
        my_file.close()
    if compare('test1.txt', 'test1_corr.txt'):
        print('Test 1b - PASSED')
    else:
        print('Test 1b - FAILED')

def test2a():
    filename = 'test2.txt'
    f = open(filename, 'r+')
    f.write('....')
    f.read()
    f.close()
    if compare('test2.txt', 'test2_corr.txt'):
        print('Test 2a - PASSED')
    else:
        print('Test 2a - FAILED')

def test2b():
    filename = 'test2.txt'
    f = open(filename, 'w+')
    f.write('....')
    f.readline()
    f.close()
    if compare('test2.txt', 'test2_corr.txt'):
        print('Test 2b - PASSED')
    else:
        print('Test 2b - FAILED')

def test2c():
    filename = 'test2.txt'
    f = open(filename, 'r+')
    f.write('....')
    f.readline(3)
    f.close()
    if compare('test2.txt', 'test2_corr.txt'):
        print('Test 2c - PASSED')
    else:
        print('Test 2c - FAILED')

def test3a():
    filename = 'test3.txt'
    f = open(filename, 'r+')
    f.write('^^^^^^^^')
    f.readline()
    f.close()
    if compare('test3.txt', 'test3_corr.txt'):
        print('Test 3a - PASSED')
    else:
        print('Test 3a - FAILED')

def test3b():
    filename = 'test3.txt'
    f = open(filename, 'r+')
    print("Initial:", f.tell())
    f.write('^^^^^^^^')
    # print("After write:", f.tell())
    f.readline(3)
    print("End:", f.tell())
    f.close()
    if compare('test3.txt', 'test3_corr.txt'):
        print('Test 3b - PASSED')
    else:
        print('Test 3b - FAILED')

def test3c():
    filename = 'test3.txt'
    f = open(filename, 'r+')
    f.write('^^^^^^^^')
    f.flush()
    f.readline()
    f.close()
    if compare('test3.txt', 'test3_corr.txt'):
        print('Test 3c - PASSED')
    else:
        print('Test 3c - FAILED')

test1a()
restore(['test1.txt', 'test3.txt'], ['test1_orig.txt', 'test3_orig.txt'])
test1b()
restore(['test1.txt', 'test2.txt'], ['test1_orig.txt', 'test2_orig.txt'])
test2a()
restore(['test1.txt', 'test2.txt'], ['test1_orig.txt', 'test2_orig.txt'])
test2b()
restore(['test1.txt', 'test2.txt'], ['test1_orig.txt', 'test2_orig.txt'])
test2c()
restore(['test1.txt', 'test2.txt'], ['test1_orig.txt', 'test2_orig.txt'])
test3a()
restore(['test1.txt', 'test3.txt'], ['test1_orig.txt', 'test3_orig.txt'])
test3b()
# restore(['test1.txt', 'test3.txt'], ['test1_orig.txt', 'test3_orig.txt'])
# test3c()
