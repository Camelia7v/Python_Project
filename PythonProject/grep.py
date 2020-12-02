import re
import os


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


def count_regex_match(regex, file):
    """
    Opțiunea de tipul “COUNT” care sa spuna de cate ori se face sau match la o expresie regulată într-un fișier.

    :param regex: expresia regulata dupa care se face cautarea
    :param file: fisierul in care se face cautarea
    :return: numarul de substringuri care respecta expresia regulata regex in fisierul file
    """
    try:
        count = 0
        r = re.compile(regex)
        for line in open(file):
            if r.search(line):
                count += 1
        return count
    except Exception as e:
        print(str(e))


def regex_recursive_search_in_a_director(regex, director):
    """
    Cautare recursiva intr-un folder a unui expresii regulate.

    :param regex: expresia regulata dupa care se face cautarea
    :param director: folderul in care se face cautarea
    :return: afișează toate liniile care au un substring care respecta expresia regulată regex si numele fisierelor
     din director in care le-a gasit
    """
    r = re.compile(regex)
    for (root, directories, files) in os.walk(director):
        for file_name in files:
            try:
                full_path = open(os.path.join(root, file_name), "r")
                for line in full_path:
                    if r.search(line):
                        print("%s: %s" % (file_name, line))
            except Exception as e:
                print(str(e))


def regex_not_matching(regex, file):
    """
    Opțiunea de tipul “NOT” care să verifice ca o anumită expresie regulată NU face match într-un fișier.

    :param regex: expresia regulata dupa care se face cautarea
    :param file: fisierul in care se face cautarea
    :return: afișează toate liniile din file in care NU se gaseste un substring care respecta expresia regulată regex
    """
    try:
        r = re.compile(regex)
        for i, line in enumerate(open(file)):
            if not r.search(line):
                print("NOT found on line %s: %s" % (i + 1, line))
    except Exception as e:
        print(str(e))
