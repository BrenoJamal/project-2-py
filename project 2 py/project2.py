#!/usr/bin/env python3
"""
The longest word

@author: Your Name
@date: 2024-11-18
"""

from typing import Union


def longest_word(filename: str) -> Union[str, list[str]]:
  """Find and return the longest word(s) in the file"""
  open = (f"project_2/{filename}")
  text = file.read()
  words = text.replace("—", " ").split()
  long = [""]
  for i in range(len(words)):
        words[i] = words[i].strip(".,")
        if len(words[i]) == len(long[0]):
            long.append(words[i])
        elif len(words[i]) > len(long[0]):
            long = [words[i]]
if len(long) > 1:
   return sorted(long)
else:
   return long[0]
    
        


def main():
  """Main function"""
  for filename, expected in [
      ("simple.txt", ["CS150", "Hello"]),
      ("preamble.txt", "Constitution"),
      ("gettysburg.txt", "battle-field"),
  ]:
    try:
      result = longest_word(filename)
      print(f"The longest word in {filename} is {result}")
      assert (
          result == expected
      ), f"The longest word in {filename} is {expected}, but {result} was returned instead"
    except AssertionError as a_err:
      print(a_err)


if __name__ == "__main__":
  main()

def main():
    """Main function"""
    for filename, expected in [
        ("simple.txt", ["CS150", "Hello"]),
        ("preamble.txt", "Constitution"),
        ("gettysburg.txt", "battle-field"),
    ]:
        try:
            result = longest_word(filename)
            print(f"The longest word in {filename} is {result}")
            assert (
                result == expected
            ), f"The longest word in {filename} is {expected}, but {result} was returned instead"
        except AssertionError as a_err:
            print(a_err)


if __name__ == "__main__":
    main()
