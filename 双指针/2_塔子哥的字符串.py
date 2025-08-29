from collections import defaultdict

def find_shortest(s):
    counter = defaultdict(int)
    left = right = 0
    diff_char = 0
    n = len(s)
    min_len = n + 1  # 初始设为比最大长度还大

    while right < n:
        # 扩展右指针
        counter[s[right]] += 1
        if counter[s[right]] == 1:  # 第一次出现
            diff_char += 1
        right += 1

        # 当窗口包含所有 26 个字母时，尝试收缩左指针
        while diff_char == 26:
            min_len = min(min_len, right - left)  # 更新最短长度

            # 移动左指针
            counter[s[left]] -= 1
            if counter[s[left]] == 0:  # 移走后该字母不在窗口中
                diff_char -= 1
            left += 1

    return min_len if min_len <= n else -1

# 测试
s = input().strip()
print(find_shortest(s))


