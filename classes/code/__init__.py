import base64
from string import ascii_lowercase
from random import choice
import os

vol = b'CicnJwogICAgVGhpcyBmdW5jdGlvbiBnZXQgZW52IHZhciBhbmQgZGVjb2RlIGl0LCByZXR1cm5pbmcgc3RyaW5nCiAgICBQYXJhbXM6IGVudiB2YXJpYWJsZSB0YWcKICAgIFJldHVybjogZGVzY3J5cHRlZCBzdHJpbmcKICAgIENPREUuZ2V0Q3JlZGVudGlhbHMoZW52X3Zhcl9uYW1lKQoKCgogICAgVGhpcyBmdW5jdGlvbiByZWN2aWVzIHN0cmluZyBhbmQgZW5jcnlwdAogICAgUGFyYW1zOiBzdHJpbmcKICAgIFJldHVybjogZW5jcnlwdGVkIHN0cmluZwogICAgQ09ERS5lbmNvZGVDcmVkZW50aWFscyhzdHJpbmcpCicnJwoKY2xhc3MgQ09ERTogCiAgICBAc3RhdGljbWV0aG9kICAKCiAgICAjVGhpcyBpcyBhbiBzaW1wbGUgZnVuY3Rpb24gdG8gZGVjb2RlIGVudiB2dmFycyEgYW5kIHRoaXMgY29tbWVudHMgaXMgCiAgICAjIGZvciBtYWtpbmcgbW9yZSBjYXJhY3RlcnMgaW4gY29udmVydGluZyB0byBjb21waWxlZCB0eXBlIChvYmZ1c2NhdGlvbiB0eXBlKQogICAgI2lmIHlvdSBjYW4gcmVhZCB0aGlzLCBjb25ncmF0dWxhdGlvbnMuIHlvdSdyZSBhIG1hY2hpbmUgKGl0YWxpYW4pLgoKICAgICNwbGVhc2UsIHVzZSB0aGUgc291cmNlIGNvZGUgdG8gYXBwZW5kIHlvdSBza2lsbHMgYW5kIE5PVCBmb3IgbWFsaWNpb3VzIHRyeWVzIQoKICAgICNUaGFua3MgaW4gYWR2YW5jZQoKICAgICNUaGUgZm9yY2UgYmUgd2l0aCB5b3UgKFN0YXIgV2FycykKCiAgICBkZWYgZW5jb2RlU3RyaW5nKHN0cl90b19iZV9lbmNyeXB0ZWQsIG1heF9yYW5kX2xlbiA9IDMyKToKICAgICAgICByZXR1cm4gInt9JHt9Ii5mb3JtYXQoCiAgICAgICAgICAgICAgICAnJy5qb2luKGNob2ljZShhc2NpaV9sb3dlcmNhc2UpIGZvciBpIGluIHJhbmdlKG1heF9yYW5kX2xlbikpLAogICAgICAgICAgICAgICAgYmFzZTY0LmI2NGVuY29kZShzdHIuZW5jb2RlKAogICAgICAgICAgICAgICAgICAgICAgICBzdHJfdG9fYmVfZW5jcnlwdGVkKSkuZGVjb2RlKCkKICAgICAgICApCiAgICAgICAgCiAgICBkZWYgZGVjb2RlU3RyaW5nKHN0cmluZ190b19iZV9kZWNyeXB0ZWQpOgogICAgICAgIHJldHVybiBiYXNlNjQuYjY0ZGVjb2RlKHN0ci5lbmNvZGUoCiAgICAgICAgICAgICAgICBsZW4oc3RyaW5nX3RvX2JlX2RlY3J5cHRlZC5zcGxpdCgiJCIpKSA9PSAxIGFuZCBzdHJpbmdfdG9fYmVfZGVjcnlwdGVkIG9yIAogICAgICAgICAgICAgICAgICAgIHN0cmluZ190b19iZV9kZWNyeXB0ZWQuc3BsaXQoIiQiKVsxXSkpLmRlY29kZSgpCgogICAgZGVmIGdldENyZWRlbnRpYWxzKHN0cmluZyk6IAogICAgICAgIHJldHVybiBDT0RFLmRlY29kZVN0cmluZyhvcy5lbnZpcm9uLmdldChzdHJpbmcpKQogICAgICAgICMgZW52X3ZhciA9IG9zLmVudmlyb24uZ2V0KHN0cmluZykgCiAgICAgICAgIyByZXR1cm4gKGVudl92YXIgPT0gTm9uZSBhbmQgJyAnIG9yIGJhc2U2NC5iNjRkZWNvZGUoc3RyLmVuY29kZShlbnZfdmFyKSkuZGVjb2RlKCkpIAogCiAgICBkZWYgZW5jb2RlQ3JlZGVudGlhbHMoc3RyaW5nKToKICAgICAgICByZXR1cm4gQ09ERS5lbmNvZGVTdHJpbmcoc3RyaW5nKQo='
eval(compile(base64.b64decode(vol).decode(), "<string>", 'exec'))