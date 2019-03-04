def genpass(pwds_amount=1, paswd_length=8):
    """ Returns a list of 'pwds_amount' random passwords, having length of 'paswd_length' """
    import random 
    return [ ''.join([chr(random.randint(32, 126)) for _ in range(paswd_length)]) for _ in range(pwds_amount)]


if __name__ == "__main__":
    print(genpass(6, 10))