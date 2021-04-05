# 문자열 검색 abcdef ab

def brute_force_search(text, start, pattern):
    if (type(text) == str and type(pattern) == str):
        text_size = len(text)
        pattern_size = len(pattern)
        print(text_size , pattern_size)

    for i in range(start, text_size - pattern_size):
        for j in range(0, pattern_size):
            if (text[i+j] != pattern[j]):
                break

            if (j >= pattern_size-1):
                return i
    
    return -1


print(brute_force_search("abcde", 0, "bc"))






    
