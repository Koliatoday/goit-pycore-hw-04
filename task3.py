import sys
from pathlib import Path
from colorama import Fore, Back, Style

# 2 spaces indentation in the folder tree
INDENT = "  "

def show_dir(dir_str: str, level:int) -> None:
  """Display the directory structure in a tree-like format with colors.
  Args:
      dir_str (str): The path to the directory to display.
      level (int): The current indentation level.
    Returns: None
  """
  directory = Path(dir_str)
  if not directory.is_dir() or not directory.exists():
    print(f"{dir_str} is not a directory or does not exist")
    return

  print(Fore.BLUE + level*INDENT + directory.name + Style.RESET_ALL)
  level = level + 1

  for path in directory.iterdir():
    if path.is_file():
      print(Fore.GREEN + level*INDENT + path.name + Style.RESET_ALL)
    elif path.is_dir():
      show_dir(path, level)
    else:
      pass


if __name__ == "__main__":
  if len(sys.argv) < 2:
    print("Please provide a directory path as a command-line argument.")
    sys.exit(1)

  dir_path = sys.argv[1]
  show_dir(dir_path, 0)
