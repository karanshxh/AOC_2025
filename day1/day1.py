from pathlib import Path
import sys
from typing import List, Any


def solve(lines: List[str]) -> Any:
	"""
	Implement this function to solve the puzzle.

	`lines` is a list of strings where each string corresponds to a row in
	`input.txt` (trailing newlines removed). Return a value that can be
	printed (string, number, or a list/tuple of printable items).
	"""
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

def main() -> None:
	here = Path(__file__).resolve().parent
	input_path = here / "input.txt"

	if not input_path.exists():
		print(f"Error: {input_path} not found.", file=sys.stderr)
		sys.exit(1)

	with input_path.open("r", encoding="utf-8") as f:
		lines = [line.rstrip("\n") for line in f]

	result = solve(lines)
	print(result)


if __name__ == "__main__":
	main()

