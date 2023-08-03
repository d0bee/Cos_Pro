# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean


def solution(commands):
	answer = [0,0]
	dx = 0
	dy = 0
	for i in commands:
		if i == 'L':
			dx -= 1
		elif i == 'R' :
			dx += 1
		elif i == 'U':
			dy += 1
		elif i == 'D':
			dy -= 1
	answer[0] = dx
	answer[1] = dy
	return answer

commands = "URDDL"
ret = solution(commands)

print("solution 함수의 반환 값은", ret, "입니다.")