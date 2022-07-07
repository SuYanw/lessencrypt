import base64
from string import ascii_lowercase
from random import choice
import os
import re


'''
    This function get env var and decode it, returning string
    Params: env variable tag
    Return: descrypted string
    CODE.getCredentials(env_var_name)



    This function recvies string and encrypt
    Params: string
    Return: encrypted string
    CODE.encodeCredentials(string)
'''

class CODE: 
    @staticmethod  

    #This is an simple function to decode env vvars! and this comments is 
    # for making more caracters in converting to compiled type (obfuscation type)
    #if you can read this, congratulations. you're a machine (italian).

    #please, use the source code to append you skills and NOT for malicious tryes!

    #Thanks in advance

    #The force be with you (Star Wars)

    def encodeString(str_to_be_encrypted, string_character_parser = "$",max_rand_len = 32):
        return (
                ''.join(choice(ascii_lowercase) for i in range(max_rand_len)) 
                + string_character_parser 
                + base64.b64encode(str.encode(str_to_be_encrypted)).decode())
        
        
    def decodeString(string_to_be_decrypted, def_parser = "$"):
        return base64.b64decode(str.encode(
                len(string_to_be_decrypted.split(def_parser)) == 1 
                and string_to_be_decrypted 
                or string_to_be_decrypted.split(def_parser)[1])).decode()

    def getStringParser(string_to_analyze, def_parser = "$"):
        getParser = re.findall('[^a-zA-Z0-9]', string_to_analyze)[0]
        return (ord(getParser) != 61 and getParser or (''))
        
    def getCredentials(string): 
        get_str_parser = CODE.getStringParser(string)
        return CODE.decodeString(os.environ.get(string), get_str_parser)
 
    def encodeCredentials(string):
        return CODE.encodeString(string)


# vol = b'CicnJwogICAgVGhpcyBmdW5jdGlvbiBnZXQgZW52IHZhciBhbmQgZGVjb2RlIGl0LCByZXR1cm5pbmcgc3RyaW5nCiAgICBQYXJhbXM6IGVudiB2YXJpYWJsZSB0YWcKICAgIFJldHVybjogZGVzY3J5cHRlZCBzdHJpbmcKICAgIENPREUuZ2V0Q3JlZGVudGlhbHMoZW52X3Zhcl9uYW1lKQoKCgogICAgVGhpcyBmdW5jdGlvbiByZWN2aWVzIHN0cmluZyBhbmQgZW5jcnlwdAogICAgUGFyYW1zOiBzdHJpbmcKICAgIFJldHVybjogZW5jcnlwdGVkIHN0cmluZwogICAgQ09ERS5lbmNvZGVDcmVkZW50aWFscyhzdHJpbmcpCicnJwoKY2xhc3MgQ09ERTogCiAgICBAc3RhdGljbWV0aG9kICAKCiAgICAjVGhpcyBpcyBhbiBzaW1wbGUgZnVuY3Rpb24gdG8gZGVjb2RlIGVudiB2dmFycyEgYW5kIHRoaXMgY29tbWVudHMgaXMgCiAgICAjIGZvciBtYWtpbmcgbW9yZSBjYXJhY3RlcnMgaW4gY29udmVydGluZyB0byBjb21waWxlZCB0eXBlIChvYmZ1c2NhdGlvbiB0eXBlKQogICAgI2lmIHlvdSBjYW4gcmVhZCB0aGlzLCBjb25ncmF0dWxhdGlvbnMuIHlvdSdyZSBhIG1hY2hpbmUgKGl0YWxpYW4pLgoKICAgICNwbGVhc2UsIHVzZSB0aGUgc291cmNlIGNvZGUgdG8gYXBwZW5kIHlvdSBza2lsbHMgYW5kIE5PVCBmb3IgbWFsaWNpb3VzIHRyeWVzIQoKICAgICNUaGFua3MgaW4gYWR2YW5jZQoKICAgICNUaGUgZm9yY2UgYmUgd2l0aCB5b3UgKFN0YXIgV2FycykKCiAgICBkZWYgZW5jb2RlU3RyaW5nKHN0cl90b19iZV9lbmNyeXB0ZWQsIHN0cmluZ19jaGFyYWN0ZXJfcGFyc2VyID0gIiQiLG1heF9yYW5kX2xlbiA9IDMyKToKICAgICAgICByZXR1cm4gKAogICAgICAgICAgICAgICAgJycuam9pbihjaG9pY2UoYXNjaWlfbG93ZXJjYXNlKSBmb3IgaSBpbiByYW5nZShtYXhfcmFuZF9sZW4pKSAKICAgICAgICAgICAgICAgICsgc3RyaW5nX2NoYXJhY3Rlcl9wYXJzZXIgCiAgICAgICAgICAgICAgICArIGJhc2U2NC5iNjRlbmNvZGUoc3RyLmVuY29kZShzdHJfdG9fYmVfZW5jcnlwdGVkKSkuZGVjb2RlKCkpCiAgICAgICAgCiAgICAgICAgCiAgICBkZWYgZGVjb2RlU3RyaW5nKHN0cmluZ190b19iZV9kZWNyeXB0ZWQsIGRlZl9wYXJzZXIgPSAiJCIpOgogICAgICAgIHJldHVybiBiYXNlNjQuYjY0ZGVjb2RlKHN0ci5lbmNvZGUoCiAgICAgICAgICAgICAgICBsZW4oc3RyaW5nX3RvX2JlX2RlY3J5cHRlZC5zcGxpdChkZWZfcGFyc2VyKSkgPT0gMSBhbmQgc3RyaW5nX3RvX2JlX2RlY3J5cHRlZCBvciAKICAgICAgICAgICAgICAgICAgICBzdHJpbmdfdG9fYmVfZGVjcnlwdGVkLnNwbGl0KGRlZl9wYXJzZXIpWzFdKSkuZGVjb2RlKCkKCiAgICBkZWYgZ2V0U3RyaW5nUGFyc2VyKHN0cmluZ190b19hbmFseXplLCBkZWZfcGFyc2VyID0gIiQiKToKICAgICAgICBnZXRQYXJzZXIgPSByZS5maW5kYWxsKCdbXmEtekEtWjAtOV0nLCBzdHJpbmdfdG9fYW5hbHl6ZSlbMF0KICAgICAgICByZXR1cm4gKG9yZChnZXRQYXJzZXIpICE9IDYxIGFuZCBnZXRQYXJzZXIgb3IgKCcnKSkKICAgICAgICAKICAgIGRlZiBnZXRDcmVkZW50aWFscyhzdHJpbmcpOiAKICAgICAgICByZXR1cm4gQ09ERS5kZWNvZGVTdHJpbmcob3MuZW52aXJvbi5nZXQoc3RyaW5nKSkKICAgICAgICAjIGVudl92YXIgPSBvcy5lbnZpcm9uLmdldChzdHJpbmcpIAogICAgICAgICMgcmV0dXJuIChlbnZfdmFyID09IE5vbmUgYW5kICcgJyBvciBiYXNlNjQuYjY0ZGVjb2RlKHN0ci5lbmNvZGUoZW52X3ZhcikpLmRlY29kZSgpKSAKIAogICAgZGVmIGVuY29kZUNyZWRlbnRpYWxzKHN0cmluZyk6CiAgICAgICAgcmV0dXJuIENPREUuZW5jb2RlU3RyaW5nKHN0cmluZyk='

# eval(
#         compile(
#                 base64.b64decode(vol).decode(), 
#                 "<string>", 
#                 'exec'
#         )
# )