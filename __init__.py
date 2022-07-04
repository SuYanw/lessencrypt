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