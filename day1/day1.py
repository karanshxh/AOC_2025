from pathlib import Path
import sys
from typing import List, Any


def solvePart1(lines: List[str]) -> Any:
	position = 50
	count = 0
	for move in lines:
		times = 1
		if move[0] == "L":
			times = -1
		position = (position + (times * int(move[1:]))) % 100
		if position == 0:
			count += 1
	return count

def solvePart2(lines: List[str]) -> Any:
	position = 50
	count = 0
	for move in lines:
		times = 1
		if move[0] == "L":
			times = -1
		movement = int(move[1:])
		
		count += movement // 100
		movement = movement % 100

		if times == 1:
			if position == 100:
				position = 0
			if position + movement >= 100:
				count += 1
			position = (position + movement) % 100
		else:
			if position == 0:
				position = 100
			if position - movement <= 0:
				count += 1
			position = (position - movement) % 100
	return count

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

