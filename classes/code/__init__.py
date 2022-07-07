import base64
from string import ascii_lowercase
from random import choice
import os
import re


vol = b"""
        CgonJycKICAgIFRoaXMgZnVuY3Rpb24gZ2V0IGVudiB2YXIgYW5kIGRlY29kZSBpdCwgcm
        V0dXJuaW5nIHN0cmluZwogICAgUGFyYW1zOiBlbnYgdmFyaWFibGUgdGFnCiAgICBSZXR1
        cm46IGRlc2NyeXB0ZWQgc3RyaW5nCiAgICBDT0RFLmdldENyZWRlbnRpYWxzKGVudl92YX
        JfbmFtZSkKCgoKICAgIFRoaXMgZnVuY3Rpb24gcmVjdmllcyBzdHJpbmcgYW5kIGVuY3J5
        cHQKICAgIFBhcmFtczogc3RyaW5nCiAgICBSZXR1cm46IGVuY3J5cHRlZCBzdHJpbmcKIC
        AgIENPREUuZW5jb2RlQ3JlZGVudGlhbHMoc3RyaW5nKQonJycKCmNsYXNzIENPREU6IAog
        ICAgQHN0YXRpY21ldGhvZCAgCgogICAgI1RoaXMgaXMgYW4gc2ltcGxlIGZ1bmN0aW9uIH
        RvIGRlY29kZSBlbnYgdnZhcnMhIGFuZCB0aGlzIGNvbW1lbnRzIGlzIAogICAgIyBmb3Ig
        bWFraW5nIG1vcmUgY2FyYWN0ZXJzIGluIGNvbnZlcnRpbmcgdG8gY29tcGlsZWQgdHlwZS
        Aob2JmdXNjYXRpb24gdHlwZSkKICAgICNpZiB5b3UgY2FuIHJlYWQgdGhpcywgY29uZ3Jh
        dHVsYXRpb25zLiB5b3UncmUgYSBtYWNoaW5lIChpdGFsaWFuKS4KCiAgICAjcGxlYXNlLC
        B1c2UgdGhlIHNvdXJjZSBjb2RlIHRvIGFwcGVuZCB5b3Ugc2tpbGxzIGFuZCBOT1QgZm9y
        IG1hbGljaW91cyB0cnllcyEKCiAgICAjVGhhbmtzIGluIGFkdmFuY2UKCiAgICAjVGhlIG
        ZvcmNlIGJlIHdpdGggeW91IChTdGFyIFdhcnMpCgogICAgZGVmIGVuY29kZVN0cmluZyhz
        dHJfdG9fYmVfZW5jcnlwdGVkLCBzdHJpbmdfY2hhcmFjdGVyX3BhcnNlciA9ICIkIixtYX
        hfcmFuZF9sZW4gPSAzMik6CiAgICAgICAgcmV0dXJuICgKICAgICAgICAgICAgICAgICcn
        LmpvaW4oY2hvaWNlKGFzY2lpX2xvd2VyY2FzZSkgZm9yIGkgaW4gcmFuZ2UobWF4X3Jhbm
        RfbGVuKSkgCiAgICAgICAgICAgICAgICArIHN0cmluZ19jaGFyYWN0ZXJfcGFyc2VyIAog
        ICAgICAgICAgICAgICAgKyBiYXNlNjQuYjY0ZW5jb2RlKHN0ci5lbmNvZGUoc3RyX3RvX2
        JlX2VuY3J5cHRlZCkpLmRlY29kZSgpKQogICAgICAgIAogICAgICAgIAogICAgZGVmIGRl
        Y29kZVN0cmluZyhzdHJpbmdfdG9fYmVfZGVjcnlwdGVkLCBkZWZfcGFyc2VyID0gIiQiKT
        oKICAgICAgICByZXR1cm4gYmFzZTY0LmI2NGRlY29kZShzdHIuZW5jb2RlKAogICAgICAg
        ICAgICAgICAgbGVuKHN0cmluZ190b19iZV9kZWNyeXB0ZWQuc3BsaXQoZGVmX3BhcnNlci
        kpID09IDEgCiAgICAgICAgICAgICAgICBhbmQgc3RyaW5nX3RvX2JlX2RlY3J5cHRlZCAK
        ICAgICAgICAgICAgICAgIG9yIHN0cmluZ190b19iZV9kZWNyeXB0ZWQuc3BsaXQoZGVmX3
        BhcnNlcilbMV0pKS5kZWNvZGUoKQoKICAgIGRlZiBnZXRTdHJpbmdQYXJzZXIoc3RyaW5n
        X3RvX2FuYWx5emUsIGRlZl9wYXJzZXIgPSAiJCIpOgogICAgICAgIGdldFBhcnNlciA9IH
        JlLmZpbmRhbGwoJ1teYS16QS1aMC05XScsIHN0cmluZ190b19hbmFseXplKVswXQogICAg
        ICAgIHJldHVybiAob3JkKGdldFBhcnNlcikgIT0gNjEgYW5kIGdldFBhcnNlciBvciAoJy
        cpKQogICAgICAgIAogICAgZGVmIGdldENyZWRlbnRpYWxzKHN0cmluZyk6CiAgICAgICAg
        CiAgICAgICAgaWYoc3RyaW5nIG5vdCBpbiBvcy5lbnZpcm9uKToKICAgICAgICAgICAgcm
        V0dXJuIE5vbmUKCiAgICAgICAgZ2V0X2Vudl9zdHJpbmcgPSBvcy5lbnZpcm9uLmdldChz
        dHJpbmcpIAoKICAgICAgICByZXR1cm4gQ09ERS5kZWNvZGVTdHJpbmcoZ2V0X2Vudl9zdH
        JpbmcsICBDT0RFLmdldFN0cmluZ1BhcnNlcihnZXRfZW52X3N0cmluZykpCiAKICAgIGRl
        ZiBlbmNvZGVDcmVkZW50aWFscyhzdHJpbmcpOgogICAgICAgIHJldHVybiBDT0RFLmVuY2
        9kZVN0cmluZyhzdHJpbmcpCg=="""
eval(
        compile(
                base64.b64decode(vol).decode(), 
                "<string>", 
                'exec'
        )
)