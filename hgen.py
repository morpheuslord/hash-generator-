import hashlib

print(' #    #   ##    #### #    # ')
print(' #    #  #  #   #    #    #  ')
print(' ###### #    #  #### ######  ')
print(' #    # ######     # #    #  ')
print(' #    # #    # #   # #    # ')
print(' #    # #    # ####  #    #  BY-MORPHOUSLORD')

x = input('enter ur password : ')
#stuf in here
#1-'blake2b'
#2-'sha1'
#3-'sha224'
#4-'shake_256'
#5-'shake_128'
#6-'md5'
#7-'sha512'
#8-'sha384'
#9-'sha3_224'
#10-'sha3_384'
#11-'sha256'
#12-'sha3_512'
#13-'blake2s'
#14-'sha3_256'

def foo(x):
    #md5
    print('=========================================================================================================================================')
    print('1) md5')
    print(hashlib.md5(x.encode('utf-8')).hexdigest())
    print('=========================================================================================================================================')
    #sha1
    print('=========================================================================================================================================')
    print('2) sha1')
    print(hashlib.sha1(x.encode('utf-8')).hexdigest())
    print('=========================================================================================================================================')
    #sha256
    print('=========================================================================================================================================')
    print('3) sha256')
    print(hashlib.sha256(x.encode('utf-8')).hexdigest())
    print('=========================================================================================================================================')
    #sha384
    print('=========================================================================================================================================')
    print('4) sha384')
    print(hashlib.sha384(x.encode('utf-8')).hexdigest())
    print('=========================================================================================================================================')
    #sha3_224
    print('=========================================================================================================================================')
    print('5) sha3_224')
    print(hashlib.sha3_224(x.encode('utf-8')).hexdigest())
    print('=========================================================================================================================================')
    #sha3_256
    print('=========================================================================================================================================')
    print('6) sha3_256')
    print(hashlib.sha3_256(x.encode('utf-8')).hexdigest())
    print('=========================================================================================================================================')
    #sha3_512
    print('=========================================================================================================================================')
    print('7) sha3_512')
    print(hashlib.sha3_512(x.encode('utf-8')).hexdigest())
    print('=========================================================================================================================================')
    #blake2b
    print('=========================================================================================================================================')
    print('8) blake2b')
    print(hashlib.blake2b(x.encode('utf-8')).hexdigest())
    print('=========================================================================================================================================')
    #blake2s
    print('=========================================================================================================================================')
    print('9) blake2s')
    print(hashlib.blake2s(x.encode('utf-8')).hexdigest())
    print('=========================================================================================================================================')
    #sha512
    print('=========================================================================================================================================')
    print('10) sha512')
    print(hashlib.sha512(x.encode('utf-8')).hexdigest())
    print('=========================================================================================================================================')
    #sha224
    print('=========================================================================================================================================')
    print('11) sha224')
    print(hashlib.sha224(x.encode('utf-8')).hexdigest())
    print('=========================================================================================================================================')
    #sha3_384
    print('=========================================================================================================================================')
    print('12) sha3_384')
    print(hashlib.sha3_384(x.encode('utf-8')).hexdigest())
    print('=========================================================================================================================================')
    #shake_128
    print('=========================================================================================================================================')
    print('13) shake_128')
    print(hashlib.shake_128(x.encode('utf-8')).hexdigest(68))
    print('=========================================================================================================================================')
    #shake_256
    print('=========================================================================================================================================')
    print('14) shake_256')
    print(hashlib.shake_256(x.encode('utf-8')).hexdigest(69))
    print('=========================================================================================================================================')
    #ends
    print('=========================================================================================================================================')
    print('=========================================================================================================================================')
    print('=========================================================================================================================================')
    print('these are all the possible hashes for ur passwords in the respective types !!!')
    print('=========================================================================================================================================')
    print('=========================================================================================================================================')
    print('=========================================================================================================================================')

foo(x)
