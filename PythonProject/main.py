import file_grep
import dir_grep
import argparse
import os
import sys

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
options = [args.ignoreCase, args.count, args.noot]

if not os.path.isdir(input_path) and not os.path.isfile(input_path):
    print("!!! CALE INVALIDA !!!")
    sys.exit()

if os.path.isdir(input_path):
    print(dir_grep.regex_recursive_search_in_a_director(to_find, input_path, options))

if os.path.isfile(input_path):
    if any(options):
        if options[0] and options[1] and options[2]:
            result = file_grep.regex_not_matching(to_find, input_path, "ignoreCase", "count")
            print(result)
        elif options[0] and options[1]:
            result = file_grep.ignore_case_search(to_find, input_path)
            if len(result) > 0:
                print(len(result))
        elif options[0] and options[2]:
            print(file_grep.regex_not_matching(to_find, input_path, "ignoreCase"))
        elif options[1] and options[2]:
            print(file_grep.regex_not_matching(to_find, input_path, "count"))
        elif options[0]:
            print(file_grep.ignore_case_search(to_find, input_path))
        elif options[1]:
            print(file_grep.count_regex_match(to_find, input_path))
        elif options[2]:
            print(file_grep.regex_not_matching(to_find, input_path))
    else:
        print(file_grep.regex_search_in_a_file(to_find, input_path))
