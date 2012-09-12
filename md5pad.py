import md5py,sys
import struct

if len(sys.argv)<3:
    print "Usage: ",sys.argv[0]," <md5string> <string_to_append> [length of plaintext of md5string]"
    sys.exit()

h = sys.argv[1]
s = sys.argv[2]
length = 64
pad = ''
if len(sys.argv)>3:
    length = int(sys.argv[3])
    n0 = ((56 - (length+1)%64) % 64)

    pad+= '\x80' #pad 1
    pad+= '\x00'*n0 + struct.pack('L', length*8)
    length+= 1 + n0 + 8

    print "Payload: ", (repr(pad+s))
    import urllib
    print "Payload urlencode:",urllib.quote_plus(pad+s)
else:
    print "No length input, cannot determine payload but still can continue.."

#print "Length after pad: ",length
md5_special = md5py.MD5(h, length)
md5_special.update(s)

print "MD5 after padding: " + md5_special.hexdigest()
