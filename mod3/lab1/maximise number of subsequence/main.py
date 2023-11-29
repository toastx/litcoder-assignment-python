def maximize_subsequences(text, pattern):
        res,count1,count2 = 0,0,0
        for char in text:
            if char == pattern[1]:
                res += count1
                count2 += 1
            if char == pattern[0]:
                count1 += 1
        return res + max(count1, count2)

text1 = "ababc"
pattern1 = "ab"
result1 = maximize_subsequences(text1, pattern1)
print(result1) 

text2 = "ababab"
pattern2 = "ab"
result2 = maximize_subsequences(text2, pattern2)
print(result2)  
