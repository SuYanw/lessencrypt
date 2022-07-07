import base64
from string import ascii_lowercase
from random import choice
import os
import re

vol = b'CicnJwogICAgVGhpcyBmdW5jdGlvbiBnZXQgZW52IHZhciBhbmQgZGVjb2RlIGl0LCByZX\
        R1cm5pbmcgc3RyaW5nCiAgICBQYXJhbXM6IGVudiB2YXJpYWJsZSB0YWcKICAgIFJldHVyb\
        jogZGVzY3J5cHRlZCBzdHJpbmcKICAgIENPREUuZ2V0Q3JlZGVudGlhbHMoZW52X3Zhcl9u\
        YW1lKQoKCgogICAgVGhpcyBmdW5jdGlvbiByZWN2aWVzIHN0cmluZyBhbmQgZW5jcnlwdAo\
        gICAgUGFyYW1zOiBzdHJpbmcKICAgIFJldHVybjogZW5jcnlwdGVkIHN0cmluZwogICAgQ0\
        9ERS5lbmNvZGVDcmVkZW50aWFscyhzdHJpbmcpCicnJwoKY2xhc3MgQ09ERTogCiAgICBAc\
        3RhdGljbWV0aG9kICAKCiAgICAjVGhpcyBpcyBhbiBzaW1wbGUgZnVuY3Rpb24gdG8gZGVj\
        b2RlIGVudiB2dmFycyEgYW5kIHRoaXMgY29tbWVudHMgaXMgCiAgICAjIGZvciBtYWtpbmc\
        gbW9yZSBjYXJhY3RlcnMgaW4gY29udmVydGluZyB0byBjb21waWxlZCB0eXBlIChvYmZ1c2\
        NhdGlvbiB0eXBlKQogICAgI2lmIHlvdSBjYW4gcmVhZCB0aGlzLCBjb25ncmF0dWxhdGlvb\
        nMuIHlvdSdyZSBhIG1hY2hpbmUgKGl0YWxpYW4pLgoKICAgICNwbGVhc2UsIHVzZSB0aGUg\
        c291cmNlIGNvZGUgdG8gYXBwZW5kIHlvdSBza2lsbHMgYW5kIE5PVCBmb3IgbWFsaWNpb3V\
        zIHRyeWVzIQoKICAgICNUaGFua3MgaW4gYWR2YW5jZQoKICAgICNUaGUgZm9yY2UgYmUgd2\
        l0aCB5b3UgKFN0YXIgV2FycykKCiAgICBkZWYgZW5jb2RlU3RyaW5nKHN0cl90b19iZV9lb\
        mNyeXB0ZWQsIHN0cmluZ19jaGFyYWN0ZXJfcGFyc2VyID0gIiQiLG1heF9yYW5kX2xlbiA9\
        IDMyKToKICAgICAgICByZXR1cm4gKAogICAgICAgICAgICAgICAgJycuam9pbihjaG9pY2U\
        oYXNjaWlfbG93ZXJjYXNlKSBmb3IgaSBpbiByYW5nZShtYXhfcmFuZF9sZW4pKSAKICAgIC\
        AgICAgICAgICAgICsgc3RyaW5nX2NoYXJhY3Rlcl9wYXJzZXIgCiAgICAgICAgICAgICAgI\
        CArIGJhc2U2NC5iNjRlbmNvZGUoc3RyLmVuY29kZShzdHJfdG9fYmVfZW5jcnlwdGVkKSku\
        ZGVjb2RlKCkpCiAgICAgICAgCiAgICAgICAgCiAgICBkZWYgZGVjb2RlU3RyaW5nKHN0cml\
        uZ190b19iZV9kZWNyeXB0ZWQsIGRlZl9wYXJzZXIgPSAiJCIpOgogICAgICAgIHJldHVybi\
        BiYXNlNjQuYjY0ZGVjb2RlKHN0ci5lbmNvZGUoCiAgICAgICAgICAgICAgICBsZW4oc3Rya\
        W5nX3RvX2JlX2RlY3J5cHRlZC5zcGxpdChkZWZfcGFyc2VyKSkgPT0gMSBhbmQgc3RyaW5n\
        X3RvX2JlX2RlY3J5cHRlZCBvciAKICAgICAgICAgICAgICAgICAgICBzdHJpbmdfdG9fYmV\
        fZGVjcnlwdGVkLnNwbGl0KGRlZl9wYXJzZXIpWzFdKSkuZGVjb2RlKCkKCiAgICBkZWYgZ2\
        V0U3RyaW5nUGFyc2VyKHN0cmluZ190b19hbmFseXplLCBkZWZfcGFyc2VyID0gIiQiKToKI\
        ]CAgICAgICBnZXRQYXJzZXIgPSByZS5maW5kYWxsKCdbXmEtekEtWjAtOV0nLCBzdHJpbmd\
        fdG9fYW5hbHl6ZSlbMF0KICAgICAgICByZXR1cm4gKG9yZChnZXRQYXJzZXIpICE9IDYxIG\
        FuZCBnZXRQYXJzZXIgb3IgKCcnKSkKICAgICAgICAKICAgIGRlZiBnZXRDcmVkZW50aWFsc\
        yhzdHJpbmcpOiAKICAgICAgICByZXR1cm4gQ09ERS5kZWNvZGVTdHJpbmcob3MuZW52aXJv\
        bi5nZXQoc3RyaW5nKSkKICAgICAgICAjIGVudl92YXIgPSBvcy5lbnZpcm9uLmdldChzdHJ\
        pbmcpIAogICAgICAgICMgcmV0dXJuIChlbnZfdmFyID09IE5vbmUgYW5kICcgJyBvciBiYX\
        NlNjQuYjY0ZGVjb2RlKHN0ci5lbmNvZGUoZW52X3ZhcikpLmRlY29kZSgpKSAKIAogICAgZ\
        GVmIGVuY29kZUNyZWRlbnRpYWxzKHN0cmluZyk6CiAgICAgICAgcmV0dXJuIENPREUuZW5j\
        b2RlU3RyaW5nKHN0cmluZyk='

eval(
        compile(
                base64.b64decode(vol).decode(), 
                "<string>", 
                'exec'
        )
)