# 문자열 숫자 변환 계산기
# enumerate 0 1, 1 2, 2 3, 3 +, 4 1, 5 2 반환 방식 기억 

def func_a(numA, numB, exp):
	if exp == '+':
		return numA + numB
	elif exp == '-':
		return numA - numB
	elif exp == '*':
		return numA * numB

def func_b(exp):
	for index, value in enumerate(exp):
		if value == '+' or value == '-' or value == '*':
			return index

def func_c(exp, idx):
	numA = int(exp[:idx])
	numB = int(exp[idx + 1:])
	return numA, numB
    
expression = "123+12"
ret = solution(expression)

print("solution 함수의 반환 값은", ret, "입니다.")