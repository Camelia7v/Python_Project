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
    found = []
    try:
        for i, line in enumerate(open(file)):
            if text.lower() in line.lower():
                found.append("Found on line %s: %s" % (i + 1, line))
    except Exception as e:
        print(str(e))
    return found


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
    except Exception as e:
        print(str(e))
    return count


def regex_not_matching(regex, file, *options):
    """
    Opțiunea de tipul “NOT” care să verifice ca o anumită expresie regulată NU face match într-un fișier.

    :param regex: expresia regulata dupa care se face cautarea
    :param file: fisierul in care se face cautarea
    :param options: poate contine ignoreCase sau count
    :return: afiseaza rezultatele in functie de ce contine options
     Daca options nu contine nimic, afișează toate liniile din file in care NU se gaseste un substring care respecta
     expresia regulată regex
    """
    count = 0
    if len(options) > 0:
        if len(options) == 2:
            if options[0] == "ignoreCase" and options[1] == "count":
                try:
                    for line in open(file):
                        if regex.lower() not in line.lower():
                            count += 1
                except Exception as e:
                    print(str(e))
                return count
        else:
            if options[0] == "ignoreCase":
                try:
                    for i, line in enumerate(open(file)):
                        if regex.lower() not in line.lower():
                            print("NOT found on line %s: %s" % (i + 1, line))
                except Exception as e:
                    print(str(e))
            elif options[0] == "count":
                try:
                    count = 0
                    r = re.compile(regex)
                    for line in open(file):
                        if not r.search(line):
                            count += 1
                except Exception as e:
                    print(str(e))
                return count
    else:
        try:
            r = re.compile(regex)
            for i, line in enumerate(open(file)):
                if not r.search(line):
                    print("NOT found on line %s: %s" % (i + 1, line))
        except Exception as e:
            print(str(e))
