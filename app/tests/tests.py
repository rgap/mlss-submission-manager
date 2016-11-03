#"^/*robots\.txt$" => "/robots.txt",

# -*- coding: UTF-8 -*-



import codecs

# open(s, 'rb').read()

#########

s = u"ñ"
s = s.encode('utf-8')
open(s, 'rb').read()

#remove_non_ascii = lambda s: "".join(i for i in s if ord(i)<128)
#s = remove_non_ascii(s)

#open(s, 'rb').read()