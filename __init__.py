from classes.code import CODE

if __name__ == "__main__":

    '''
        This is a string to be encrypted
    '''
    string_to_encrypt = "agua"

    # Encrypt process
    string_encrypted = CODE.encodeString(string_to_encrypt, "-")

    # Get parse string
    string_parser = CODE.getStringParser(string_encrypted)

    # descrypting process
    string_decrypted = CODE.decodeString(string_encrypted, string_parser)

    #Testing results
    print("""
            String Original: {}
            Encrypted: {}
            Decrypted: {}
            Parser: {}""". format(
                        string_to_encrypt,
                        string_encrypted,
                        string_decrypted,
                        string_parser
                    )
        )