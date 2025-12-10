
#!/usr/bin/env python3
from pathlib import Path
from typing import Any


def solvePart1(batteries) -> Any:
	rsum = 0
	for b in batteries:
		first = 0
		second = 0
		for i in range(len(b)-1):
			num = int(b[i])
			if num > first:
				first = num
				second = 0
			elif num > second:
				second = num
		if int(b[-1]) > second:
			second = int(b[-1])
		rsum += (first * 10) + second
	return rsum

def solvePart2(batteries):
	rsum = 0
	for b in batteries:
		number = ""
		leftMargin = 0
		for i in range(12):
			chosen = max(b[leftMargin:len(b) - (11 - i)])
			number += chosen
			while b[leftMargin] != chosen:
				leftMargin += 1
			leftMargin+=1
		rsum += int(number)
	return rsum



def main() -> None:
	here = Path(__file__).resolve().parent
	input_path = here / "input.txt"

	if not input_path.exists():
		print(f"Error: {input_path} not found.", file=sys.stderr)
		sys.exit(1)

	with input_path.open("r", encoding="utf-8") as f:
		lines = [line.rstrip("\n") for line in f]
	result = solvePart2(lines)
	print(result)
if __name__ == "__main__":
	main()

