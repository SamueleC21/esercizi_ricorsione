
def palindroma(parola):
    if len(parola)==1 or len(parola)==0:
        return True
    else:
        return parola[0] == parola[-1] and palindroma(parola[1:-1])

def palindrome_banale(parola):
    return parola[::-1] == parola

if __name__ == '__main__':
    print(palindroma('casa'))
    print(palindroma('civic'))

    print(palindrome_banale('casa'))
    print(palindrome_banale('civic'))