# Less Encrypt
The useful and basic encrypt tool, it's base64 baseaded  and easy to use.


### Usage
Actually has two way to use it, you can encrypt and decrypt, baseaded in base64 convertion!

### Functions
Actually as an four application, Encode and Decode strings, getCredentials and encodeCredentials.
```python
CODE.encodeString(string) # Encrypt string (return string)
CODE.decodeString(string) # Decrypt String (return string)
CODE.getStringParser(string) # Get parser of hash string

CODE.getCredentials(var_env) # get and decrypt specified enviromnent variable
CODE.encodeCredentials(string) # encrypt string (not create enviroment var)
```

## Exemple usage script 
```python
from classes.code import CODE

if __name__ == "__main__":
    '''
        This is a string to be encrypted
    '''
    string_to_encrypt = "agua"

    # Encrypt process
    string_encrypted = CODE.encodeString(string_to_encrypt)

    # descrypting process
    string_decrypted = CODE.decodeString(string_encrypted)


    #Testing results
    print("""
            String Original: {}
            Encrypted: {}
            Decrypted: {}""". format(
                        string_to_encrypt,
                        string_encrypted,
                        string_decrypted
                    )
        )

```

Code results:
```
            String Original: agua
            Encrypted: uqqnvgobziluvofpnmlacpubutcajfvv$YWd1YQ==
            Decrypted: agua
```

Best regards
