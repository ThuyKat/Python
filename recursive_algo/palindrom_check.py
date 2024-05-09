def rev(s):
    if(len(s) == 1):
        return s
    return s[len(s)-1] + rev(s[:len(s)-1])

def check_pal(s):
    rev_s = rev(s)
    return s == rev_s
    
print(check_pal("abbcbba"))

def solution(s,start,end):
    if start>=end:
        return True
    return (s[start] == s[end] and solution(s,start+1,end-1))
print(solution("abbcbba",0,len("abbcbba")-1))