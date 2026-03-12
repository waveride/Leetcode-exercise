def longest_palindrome(s: str) -> str:

    # 处理小于2个字符的情况
    if len(s) < 2:
        return s

    start = 0
    max_len = 1

    #center expand
    def expand(left: int, right: int) -> int:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1

    for i in range(len(s)):
        len1 = expand(i, i)
        len2 = expand(i, i + 1)
        current_len = max(len1, len2)

        if current_len > max_len:
            max_len = current_len
            start = i - (current_len - 1) // 2
    return s[start:start + max_len]

if __name__ == '__main__':
    test_cases = [
        "babad",   # 输出 "bab" 或 "aba"（都正确）
        "cbbd",    # 输出 "bb"
        "afsfsfsdfa",       # 输出 "a"
        "ac"       # 输出 "a" 或 "c"（都正确）
    ]
    for case in test_cases:
        print(f"输入：{case}，输出：{longest_palindrome(case)}")
"""
中心扩展算法,枚举字符串中的每个字符,以该字符为中心,向两边扩展,找到最长的回文子串，时间复杂度：O(n 
2)，其中 n 是字符串的长度。长度为 1 和 2 的回文中心分别有 n 和 n−1 个，每个回文中心最多会向外扩展 O(n) 次。
"""  
    
