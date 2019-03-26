"""
Title: Linux Dictionary Attack
Author: Kevin Diaz
Date: 03/25/19
Description:

Modules:
    crypt   -- Used for hashing
    getopt  -- Used for getting args from user
    sys     -- Used for closing app
    time    -- Used to get duration of the cracking function
"""

import crypt
import getopt
import sys
import time

FOUND = {}
NOTFOUND = {}

# TODO If no crack, give user option to choose another list or exit
# TODO Allow input and check formatting of input file


def test_pass(word_list, crypt_pass, user):
    """Hashes words from the list and checks if they match the password hash

    Keyword arguments:
    word_list   -- The file location of the word list
    crypt_pass  -- The password hash to be cracked
    user        -- The linux username to which the password hash belongs
    """

    global FOUND
    global NOTFOUND

    salt = crypt_pass

    # Try user as password
    crypt_word = crypt.crypt(user, salt)

    if crypt_word == crypt_pass:
        #print("[+]Found Password: "+user)
        print("[+]Found password for %s: %s" % (user, user))
        FOUND[user] = user
        return
    print("[-]Password Not Found.\n"+user)

    # Try user backwards as password
    crypt_word = crypt.crypt(user[::-1], salt)

    if crypt_word == crypt_pass:
        print("[+]Found password for %s: %s" % (user, user[::-1]))
        FOUND[user] = user
        return
    print("[-]Password Not Found.\n"+user[::-1])

    # Load wordlist and begin trying those words
    with open(word_list) as dict_file:
        for word in dict_file.readlines():
            word = word.strip('\n')
            crypt_word = crypt.crypt(word, salt)

            if crypt_word == crypt_pass:
                print("[+]Found password for %s: %s" % (user, word))
                FOUND[user] = word
                return
            print("[-]Password Not Found.\n"+word)
    NOTFOUND[user] = crypt_pass


def results():
    """Prints results of the cracking function to the screen and optionally a file"""

    global FOUND
    global NOTFOUND

    if NOTFOUND:
        print("-"*70)
        print("The following passwords could not be cracked")
        for key, val in NOTFOUND.items():
            print("{0}: {1}".format(key, val))

    if FOUND:
        print("-"*70)

        print("The following passwords were cracked! :)\n")
        for key, val in FOUND.items():
            print("{0}: {1}".format(key, val))

        print("-"*70)

        response = input("Would you like to save cracked passwords to a file?(y/n) ")
        if response == "y":
            with open('CrackedPasswords.txt', 'a') as output:
                for key, val in FOUND.items():
                    output.write("User: {0}; Password: {1}\n".format(key, val))
        elif response == "n":
            pass
        else:
            print("Bad Input! Making a file anyways")
            with open('CrackedPasswords.txt', 'a') as output:
                for key, val in FOUND.items():
                    output.write("User: {0}; Password: {1}\n".format(key, val))
    else:
        print("No passwords were cracked :(")
        print("Try using a different password list or a different method")

    print("\nThank you for using my dictionary attack script!\n")


def main(argv):
    """Takes user args and loads the file with the hashed passwords for cracking"""

    word_list = ""
    try:
        opts, argv = getopt.getopt(argv, "hl:", ["list="])
    except getopt.GetoptError:
        print('USAGE: linux-dictAttack.py -l <word_list>')
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print('USAGE: linux-dictAttack.py -l <word_list> \n')
            print('You can provide a /etc/shadow file.')
            print('Make sure you have removed lines with no hashes\n')
            print('The delimiting character is a colon\n')
            print('If you create your own file, it should contain format user:hash\n')
            sys.exit()
        elif opt in ("-l", "--list"):
            word_list = arg

    if not word_list:
        print('Please provide a word list')
        print('USAGE: linux-dictAttack.py -l <word_list>')
        sys.exit()

    with open('shadow') as pass_file:
        for line in pass_file.readlines():
            if ":" in line:
                user = line.split(':')[0]
                crypt_pass = line.split(':')[1].strip(' ')
                print("[*]Cracking password for: "+user)
                origin_time = time.time()
                test_pass(word_list, crypt_pass, user)
                time_inter = time.time() - origin_time
                print("Elapsed time: "+str(time_inter)+'\n')
        results()


if __name__ == "__main__":
    main(sys.argv[1:])
