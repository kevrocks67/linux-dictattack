# Linux Dictionary Attack Tool
This is a python3 tool to bruteforce the password hash of a linux system using a dictionary attack.
The idea and inspiration of this project comes from the python2 script in the book Violent Python
by TJ Oconnor.

The only requirements are to have python 3 installed. This script was tested with python 3.7.2,
but it should work with older versions of python 3.

Feel free to test the script using the [rockyou dictionary list]() and the provided file named
"shadow".

## Usage
    USAGE: python3 linux_dict_attack.py -l [--list] <word_list> -f [--file] <hash_file>

    Example: python3 linux_dict_attack.py -l rockyou -f shadow

word\_list - A file with different words on each line. If you need a wordlist check out
[SecLists](https://github.com/danielmiessler/SecLists)

hash\_file - A file with hashes on each line. This file can be a /etc/shadow file you copied.
However, remove any lines which contain users without hashed passwords to prevent errors.

## Legal Notice
The usage of this tool on hashes obtained in an illegal/illicit or otherwise unethical manner
can lead to serious legal consequences. Obtaining hashes from a computer without the explicit
permission of the owner is highly illegal and unethical. This tools primary purpose is for legal
penetration testing, CTF's/wargames, and lab environments. Any actions taken using this tool
is at your own risk and I am not to be held liable for any repercussions which may occur.

If you are unsure of what constitutes unethical behavior, refer to the [EC-Council: Code of
Ethics](https://www.eccouncil.org/code-of-ethics/)

## License
    kevrocks67/linux-dictattack
    Copyright (C) <2019> <Kevin Diaz>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

