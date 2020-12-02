import re


def regex_search_in_a_file(regex, file):
    """
    Căutare după expresii regulate într-un fișier.

    :param regex: expresia regulata dupa care se face cautarea
    :param file: fisierul in care se face cautarea
    :return: afișează toate liniile din file care au un substring care respecta expresia regulată regex
    """
    try:
        r = re.compile(regex)
        for i, line in enumerate(open(file)):
            if r.search(line):
                print("Found on line %s: %s" % (i + 1, line))
    except Exception as e:
        print(str(e))


def ignore_case_search(text, file):
    """
    Căutare după un text/string într-un fișier fără a ține cont de case.

    :param text: stringul dupa care se face cautarea
    :param file: fisierul in care se face cautarea
    :return: afiseaza toate liniile din file care conțin textul text fără sa țină cont de case
    """
    try:
        for i, line in enumerate(open(file)):
            if text.lower() in line.lower():
                print("Found on line %s: %s" % (i + 1, line))
    except Exception as e:
        print(str(e))
