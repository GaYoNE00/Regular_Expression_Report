import re

#주어진 패턴을 문자열에서 찾고 매칭되는 첫번째 결과를 반환합니다.
re.search(pattern, string)
#문자열의 시작에서 주어진 패턴과 매칭되는지 검사합니다.
re.match(pattern, string)
#문자열에서 주어진 패턴과 매칭되는 모든 결과를 리스트로 반환합니다.
re.findall(pattern, string)
#문자열에서 주어진 패턴과 매칭되는 부분을 다른 문자열로 대처합니다.
re.sub(pattern, repl, string)
#주어진 패턴을 기준으로 문자열을 분리하여 리스트로 반환합니다.
re.split(pattern, string)
