# str -> 특정 숫자 치환
# comprehension과 join 사용법 숙지
import math

def solution(num):
	num += 1
	# for
	# for x in str(num):
	#	if x == '0': x = '1'
	#	answer += x
	
	# comprehension
	answer = ''.join('1' if x == '0' else x for x in str(num))
	
	return answer
    
num = 9949999;
ret = solution(num)
 
print("solution 함수의 반환 값은", ret, "입니다.")