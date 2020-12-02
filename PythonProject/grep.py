import re


def regex_search_in_a_file(regex, file):
    """
    Căutare după expresii regulate într-un fișier.

    :param regex: expresia regulata dupa care se face cautarea
    :param file: fisierul in care se face cautarea
    :return: afișează toate liniile din file care au un substring care
     respecta expresia regulată regex
    """
    try:
        r = re.compile(regex)
        for i, line in enumerate(open(file)):
            if r.search(line):
                print("Found on line %s: %s" % (i + 1, line))
    except Exception as e:
        print(str(e))
