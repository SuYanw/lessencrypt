from classes.code import CODE

if __name__ == "__main__":

    '''
        This is a string to be encrypted
    '''
    string_to_encrypt = "agua"
    default_parser = "/"

    # Encrypt process
    string_encrypted = CODE.encodeString(string_to_encrypt, default_parser)

    # descrypting process
    string_decrypted = CODE.decodeString(string_encrypted, default_parser)

    string_parser = CODE.getStringParser("twjuzltmvzmxznhiut%jzorrcgqokdkbvYWd1YQ==")

    #Testing results
    print("""
            String Original: {}
            Encrypted: {}
            Decrypted: {}
            Parser: {}
            Caracter: {}""". format(
                        string_to_encrypt,
                        string_encrypted,
                        string_decrypted,
                        string_parser,
                        chr(61)
                    )
        )