def longest_substring_length(s):
    hash_map = {} 
    start = 0 
    max_length = 0 

    for i in range(len(s)):
        if s[i] in hash_map and hash_map[s[i]] >= start:
            start = hash_map[s[i]] + 1

        hash_map[s[i]] = i
        current_length = i - start + 1

        max_length = max(max_length, current_length)

    return max_length