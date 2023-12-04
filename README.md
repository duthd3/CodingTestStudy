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

### 1차원 배열(리스트) 입력받기
- map(int, input().split()): 한 줄 입력받아 공백으로 나눈 문자열 리스트를 int형으로 변환
- list(): 괄호안의 데이터를 리스트로 묶음
```python
arr = list(map(int, input().split()))
>>> 1 2 3 4 5 #입력
print(arr)
[1, 2, 3, 4, 5] #숫자형 리스트로 입력을 받아 arr변수에 저장
```

### 이어진 숫자를 한자리씩 나눠서 리스트에 저장: 문자열 리스트로 저장
- input(): 한줄을 읽어옴(구분문자가 없다/ 문자열로 읽어옴)
```python
print(input())
>>> 12345 # 입력
12345 # 출력
```

### 이어진 숫자를 한자리씩 나눠서 리스트에 저장: 숫자형 리스트로 저장
- map() 함수를 이용해서 문자열을 숫자로 변환한 후 list() 함수를 이용해서 리스트로 변환해준다.
```python
arr = list(map(int, input()))
>>> 12345 #입력
print(arr)
[1, 2, 3, 4, 5] #숫자형리스트로 입력됨
```

### 한줄을 읽고 공백으로 구분된 문자를 정수로 변환
- map(형식, 리스트): 리스트에 있는 데이터를 형식에 맞춰 변환함
```python
N, M = map(int, input().split())
# 1 2 #입력
print(N, M)
# 1 2 #출력
```

### N행으로 이뤄진 2차원 배열 입력받기
- 리스트 내포: 리스트를 생성할 때 반복문을 사용할 수 있도록 해줌
- list = [반복내용 for _ in range(반복횟수)]
- 이렇게 쓰면 반복횟수만큼 반복할 내용 수행
```python
N = int(input())

arr = list [list(map(int,input().split())) for _ in range(N)]
>>> 1 2 3
>>> 4 5 6
>>> 7 8 9
print(arr)
[[1, 2, 3], [4, 5, 6], [7, 8, 9]] #출력하면 2차원리스트로 입력된 것 확인됨
```
