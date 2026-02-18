def longestCommonPrefix(strs):
    if not strs:
        return ""
    
    first = strs[0]
    prefix = ""
    
    for i in range(len(first)):
        char = first[i]
        
        for s in strs[1:]:
            if i >= len(s) or s[i] != char:
                return prefix
        
        prefix += char
    
    return prefix
