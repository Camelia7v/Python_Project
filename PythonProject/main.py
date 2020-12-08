import grep
import argparse
import os
import sys

# print(grep.regex_search_in_a_file("t{2,3}", "test.txt"))
# print(grep.ignore_case_search("Its", "test.txt"))
# print(grep.count_regex_match("t{2,3}", "test.txt"))
# print(grep.regex_recursive_search_in_a_director("t{2,3}", "test"))
# print(grep.regex_not_matching("t{2,3}", "test.txt"))

# Creare parser
my_parser = argparse.ArgumentParser(description="Utilitar similar lui grep")

# Adaugare argumente
my_parser.add_argument("regex",
                       metavar="regex",
                       type=str,
                       help="Expresia regulata sau cuvantul dupa care se face cautarea.")
my_parser.add_argument("path",
                       metavar="path",
                       type=str,
                       help="Fisierul sau directorul in care se face cautarea.")
my_parser.add_argument("-i", "-ignoreCase", "--ignoreCase",
                       action="store_true",
                       help="Nu se tine cont de case.")
my_parser.add_argument("-c", "-count", "--count",
                       action="store_true",
                       help="De cate ori se face match.")
my_parser.add_argument("-n", "-not", "--noot",
                       action="store_true",
                       help="Nu se face match.")

args = my_parser.parse_args()

input_path = args.path
to_find = args.regex

if not os.path.isdir(input_path) and not os.path.isfile(input_path):
    print("!!! CALE INVALIDA !!!")
    sys.exit()

if os.path.isdir(input_path):
    print(grep.regex_recursive_search_in_a_director(to_find, input_path))

if os.path.isfile(input_path):
    if args.ignoreCase:
        print(grep.ignore_case_search(to_find, input_path))
    elif args.count:
        print(grep.count_regex_match(to_find, input_path))
    elif args.noot:
        print(grep.regex_not_matching(to_find, input_path))
    else:
        print(grep.regex_search_in_a_file(to_find, input_path))
