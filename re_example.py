import re

# 문자열 []
text = "apple, banana, cherry, date"
pattern = r"[aeiou]"  # 모음 문자를 찾는 패턴
matches = re.findall(pattern, text)
print(matches)  # 출력: ['a', 'e', 'a', 'a', 'e']

# 점 .
text = "apple, banana, cherry, date"
pattern = r"b.nana"  # b로 시작하고 n으로 끝나는 5글자 패턴
matches = re.findall(pattern, text)
print(matches)  # 출력: ['banana']

# 반복 (*)
text = "abbbbbc"
pattern = r"ab*c"  # a로 시작하고 b가 0개 이상 있는 패턴
matches = re.findall(pattern, text)
print(matches)  # 출력: ['abbbbbc']

# 반복 (+)
text = "abbbbbc"
pattern = r"ab+c"  # a로 시작하고 b가 1개 이상 있는 패턴
matches = re.findall(pattern, text)
print(matches)  # 출력: ['abbbbbc']

# 반복({m,n})
text = "abcdeee"
pattern = r"e{2,3}"  # e가 2개 또는 3개 있는 패턴
matches = re.findall(pattern, text)
print(matches)  # 출력: ['ee']

# ?
text = "color or colour?"
pattern = r"colou?r" # "color" 또는 "colour" 패턴
matches = re.findall(pattern, text)
print(matches) # 출력: ['color', 'colour']

# 문자열에서 특정 패턴 찾기
text = "Hello, my email address is 202145065@inhatc.ac.kr"
pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
match = re.search(pattern, text)
if match:
    email = match.group()
    print("Email found:", email)
else:
    print("No email found.")

# 문자열에서 패턴에 매칭되는 모든 결과 찾기
text = "apple, banana, cherry, date"
pattern = r"\b\w+\b"
matches = re.findall(pattern, text)
print("Matches found:", matches)

# 문자열에서 패턴에 매칭되는 부분 대체하기
text = "Hello, my name is Eunse"
pattern = r"Eunse"
new_text = re.sub(pattern, "Oh", text)
print("New text:", new_text)

# 문자열 분리하기
text = "apple,banana,cherry,date"
pattern = r","
tokens = re.split(pattern, text)
print("Tokens:", tokens)
