import re

WEAK_PASSWORDS = [
    "123456", "password", "123456789", "12345678",
    "111111", "1234567", "qwerty", "123123",
    "abc123", "666666", "888888", "admin"
]


def check_length(pwd):
    if len(pwd) >= 12:
        return 2, ""
    elif len(pwd) >= 8:
        return 1, "建议长度至少12位"
    return 0, "长度不足8位，太短了"


def check_chars(pwd):
    score = 0
    tips = []
    if re.search(r'[A-Z]', pwd):
        score += 1
    else:
        tips.append("缺少大写字母")
    if re.search(r'[a-z]', pwd):
        score += 1
    else:
        tips.append("缺少小写字母")
    if re.search(r'[0-9]', pwd):
        score += 1
    else:
        tips.append("缺少数字")
    if re.search(r'[^A-Za-z0-9]', pwd):
        score += 1
    else:
        tips.append("缺少特殊字符")
    return score, tips


def check_weak(pwd):
    return pwd.lower() in WEAK_PASSWORDS


def get_level(score):
    if score >= 6:
        return "强"
    elif score >= 4:
        return "中"
    return "弱"


def main():
    print("=== 密码强度检测器 ===")
    print("输入密码查看强度，输入 q 退出\n")

    while True:
        pwd = input("请输入密码：")
        if pwd.lower() == "q":
            print("已退出")
            break

        if check_weak(pwd):
            print("结果：极弱（这是常见弱密码，请立即更换）\n")
            continue

        length_score, length_tip = check_length(pwd)
        char_score, char_tips = check_chars(pwd)
        total = length_score + char_score

        tips = []
        if length_tip:
            tips.append(length_tip)
        tips.extend(char_tips)

        print(f"强度等级：{get_level(total)}（{total}/6分）")
        if tips:
            print("改进建议：")
            for t in tips:
                print(f"  - {t}")
        print()


if __name__ == "__main__":
    main()