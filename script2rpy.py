#!/usr/bin/env python

"""
This script parses the WGP-script (non renpy code, human readable) into
code for the renpy script starting and ending at specified lines.
The produced code will go to standard out so it can be used by other tools (e.g., sed).

Usage: script2rpy -n NUMBER[ANOTHER_NUMBER...] FILE
       script2rpy -n START-END FILE
       script2rpy FILE

START is the line number to begin parsing the file.
END is the last line to parse.

NUMBER is a line number to parse.
Multiple lines can be specified with no spaces in between and
separated with commas (e.g., 1,3,5).

FILE is the file to parse and should be in plain text (e.g., .txt).
This file should be the human readable script, not renpy code.

If the only argument is FILE, then the script will
parse FILE completely.

Examples:
Parse lines 5-10 of the script.
script2rpy -n 5-10 wgp-script.txt

Parse lines 5, 8, and 10 of the script.
script2rpy -n 5,8,10 wgp-script.txt

Parse line 23 of the script.
script2rpy -n 23 wgp-script.txt
"""

import argparse
import re
import sys

# Dictionary to translate the characters' names into their
# brief forms for renpy.
character = {
    "mc"        : "mc",
    "geisha"    : "gei",
    "haruka"    : "har",
    "kirara"    : "krr",
    "scarlet"   : "sca",
    "scotlyn"   : "sco",
    "brandon"   : "bra",
    "brianne"   : "bri",
    "fumika"    : "fum",
    "kaori"     : "kao",
    "nekome"    : "nek",
    "shoko"     : "sho",
    "rin"       : "rin",
    "toge"      : "tog",
    "nadeshiko" : "nad",
    "atsuko"    : "ats",
    "kanou"     : "kan",
    "scott jk"  : "sjk",
    "sora"      : "sor",
    "tamashii"  : "tam",
    "yuri"      : "yur",
    "alfred"    : "alf",
    "asmund"    : "asm",
    "dad"       : "dad",
    "mayor"     : "may",
    "sams"      : "sam",
    "mari"      : "mar",
    "otto"      : "oto"
    }

parser = argparse.ArgumentParser()
parser.add_argument("file", help="the file to parse")
parser.add_argument("-n", "--numbers", help="the line numbers to parse")

args = parser.parse_args()

"""
RE matches
43
15-48
1,2,3
1,2,3,4
"""
# RE pattern to exclusively match with valid arguments.
num_re = r"^(\d+-\d+)$|^(\d+,)+\d+$|^\d+$"

"""
RE matches
mc: "Some text." -- "mc:"
mc "Some text."  -- "mc "
"""
# RE pattern to match with the character thinking/talking from the text.
char_re = r"^\w+(\s{1}|:)"

# Make the script work if FILE is the only argument.
try:
    num = re.match(num_re, args.numbers)
except TypeError:
    num = None
    print("Parse all of FILE, maybe use a generator")
    exit()

# if RE did not match and -n ARGUMENT is provided,
# the argument has letters and/or bad formatting (e.g., 4,2,hm).
if num == None and args.numbers != None:
    sys.stderr.write(f"'{args.numbers}' is not valid for the option '-n'")
    exit()

# if RE matches
if num != None:
    if "-" in num.group(0):
        print(num)
        print("Handle the range of numbers")
    elif "," in num.group(0):
        print("Put the numbers in a list")
    else:
        num = [int(num.group(0))]
        print(num)

print("Parse specified lines of FILE, maybe use a generator")
