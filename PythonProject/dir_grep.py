import file_grep
import re
import os


def regex_recursive_search_in_a_director(regex, director, options):
    """
    Cautare recursiva intr-un folder a unui expresii regulate tinand cont de optiunile primite.
     Daca options contine False pe toate pozitiile, se vor afișa toate liniile care au un substring care respecta
     expresia regulată regex si numele fisierelor din director in care le-a gasit

    :param regex: expresia regulata dupa care se face cautarea
    :param director: folderul in care se face cautarea
    :param options: lista de optiuni (poate contine: ignoreCase, count, not sub forma de True sau False)
    :return: afișează rezultatele pentru toate fisierele gasite in director, in functie de optiunile primite in options
    """
    r = re.compile(regex)
    for (root, directories, files) in os.walk(director):
        for file_name in files:
            if any(options):
                print("In file %s: " % file_name)
                if options[0] and options[1] and options[2]:
                    print(file_grep.regex_not_matching(regex, os.path.join(root, file_name), "ignoreCase", "count"))
                elif options[0] and options[1]:
                    result = file_grep.ignore_case_search(regex, os.path.join(root, file_name))
                    if len(result) > 0:
                        print(len(result))
                elif options[0] and options[2]:
                    print(file_grep.regex_not_matching(regex, os.path.join(root, file_name), "ignoreCase"))
                elif options[1] and options[2]:
                    print(file_grep.regex_not_matching(regex, os.path.join(root, file_name), "count"))
                elif options[0]:
                    print(file_grep.ignore_case_search(regex, os.path.join(root, file_name)))
                elif options[1]:
                    print(file_grep.count_regex_match(regex, os.path.join(root, file_name)))
                elif options[2]:
                    print(file_grep.regex_not_matching(regex, os.path.join(root, file_name)))
            else:
                try:
                    full_path = open(os.path.join(root, file_name), "r")
                    for line in full_path:
                        if r.search(line):
                            print("%s: %s" % (file_name, line))
                except Exception as e:
                    print(str(e))
