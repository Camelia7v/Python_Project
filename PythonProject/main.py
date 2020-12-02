import grep

# print(grep.regex_search_in_a_file("t{2,3}", "test.txt"))
# print(grep.ignore_case_search("Its", "test.txt"))
# print(grep.count_regex_match("t{2,3}", "test.txt"))
# print(grep.regex_recursive_search_in_a_director("t{2,3}", "test"))
print(grep.regex_not_matching("t{2,3}", "test.txt"))
