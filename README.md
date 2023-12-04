# CodingTestStudy
코딩테스트 스터디입니다.
## 파이썬 입력처리 정리
### 파일로 입력받기
- sys 모듈 임포트
- 표준 입력을 파일/읽기로 설정
```python
import sys
sys.stdin = open("input.txt", "r")
```

### 한줄을 읽어서 정수로 변환
- input(): 한줄을 읽어옴
- int(): 정수로 변환
```python
N = int(input())
print(N)
```

### 한줄을 읽고 공백으로 구분된 문자를 입력받기
- input().split(구분문자): 한줄을 읽고 구분문자로 나눠서 문자로 이뤄진 리스트로 입력받음
```python
print(input().split())
# a b c #콘솔창에 입력하면
['a', 'b', 'c'] # 문자로 입력됨
```

### 한줄을 읽고 공백으로 구분된 문자를 정수로 변환
- map(형식, 리스트): 리스트에 있는 데이터를 형식에 맞춰 변환함
```python
N, M = map(int, input().split())
# 1 2 #입력
print(N, M)
# 1 2 #출력
```
