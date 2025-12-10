
#!/usr/bin/env python3
from pathlib import Path
from typing import Any


def solvePart1(input_str: str) -> Any:
	ranges = input_str.split(",")
	runningSum = 0
	for r in ranges:
		start, end = int(r.split("-")[0]), int(r.split("-")[1])
		for num in range(start, end + 1):
			strnum = str(num)
			if len(strnum) % 2 == 0:
				if strnum[:len(strnum)//2] == strnum[len(strnum)//2:]:
					runningSum += num
	return runningSum


def checkLen(num, curr):
	for i in range(curr, len(num), curr):
		if num[i:i+curr] != num[i-curr:i]:
			return False
	return True

def checkNum(num):
	curr = len(num) // 2
	while curr >= 1:
		if len(num) % curr == 0 and checkLen(num, curr):
			return True
		curr -= 1
	return False


def solvePart2(input_str: str) -> Any:
	ranges = input_str.split(",")
	runningSum = 0
	for r in ranges:
		start, end = int(r.split("-")[0]), int(r.split("-")[1])
		for num in range(start, end + 1):
			strnum = str(num)
			if checkNum(strnum):
				runningSum += num
	return runningSum


if __name__ == "__main__":
	# Read `input.txt` located in the same directory as this script
	input_path = Path(__file__).with_name("input.txt")
	try:
		input_text = input_path.read_text()
	except FileNotFoundError:
		raise SystemExit(f"Could not find input file at {input_path}")

	result = solvePart2(input_text)

	# Print result. If a tuple is returned, print each value on its own line.
	if isinstance(result, tuple):
		for r in result:
			print(r)
	else:
		print(result)

