
"""Helper function for tasks 1 and 2."""
def is_number(value: str) -> bool:
    """Check if the given value can be converted to a float.
    Args:
        value (str): The value to check.
    Returns:
        bool: True if the value can be converted to a float, False otherwise.
    """
    try:
        float(value)
        return True
    except ValueError:
        return False


#************************** Task 1 **************************#

def parse_salary_file(fh) ->tuple:
    """Parse the file and calculate total and average salary.
    Args:
        fh: File handle to read data from.
    Returns:
        tuple: A tuple containing total salary and average salary.
    """
    cnt = 0
    tot_salary = 0

    line = fh.readline()

    while line:
      lst = line.split(',')
      if len(lst) < 2 or not is_number(lst[1]):
        print("Wrong data format")
        line = fh.readline()
        continue
      else:
        tot_salary += float(lst[1])
        cnt += 1
      line = fh.readline()

    if cnt != 0:
      return (tot_salary, tot_salary/cnt)
    else:
      print("File is empty or contains data in wrong format")
      return (0,0)


def total_salary(path: str):
    """Calculate total and average salary from the given file.
    Args:
        path (str): The path to the file containing salary data.
    Returns:
        tuple: A tuple containing total salary and average salary."""
    try:
        with open(path, 'r', encoding='utf-8') as fh:
          return parse_salary_file(fh)

    except FileNotFoundError:
        print(f"The file '{path}' was not found.")
        return (0,0)


# Example usage
total, average = total_salary("./salary.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")


#************************** Task 2 **************************#

def parse_cats_info(fh) -> list:
    """Parse the file and extract cat information.
    Args:
        fh: File handle to read data from.
    Returns:
        list: A list of dictionaries containing cat information.
    """
    ret = []

    line = fh.readline()
    while line:
      lst = line.split(',')
      if len(lst) < 3 or not is_number(lst[2]):
        print("Wrong data format")
        line = fh.readline()
        continue
      else:
        ret.append({"id":lst[0], "name":lst[1], "age":lst[2].strip()})

      line = fh.readline()

    return ret


def get_cats_info(path: str) -> list:
    """Get cat information from the given file.
    Args:
        path (str): The path to the file containing cat data.
    Returns:
        list: A list of dictionaries containing cat information."""

    try:
      with open(path, 'r', encoding='utf-8') as fh:
        return parse_cats_info(fh)

    except FileNotFoundError:
        print(f"The file '{path}' was not found.")
        return []

# Example usage
cats_info = get_cats_info("./cats_file.txt")
print(cats_info)