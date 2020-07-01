def main(list):
  result = ""
  for i, e in enumerate(list):
    if i < (len(list) -1):
      result += f"{e}, "
    else:
      result += f"and {e}"
  print(result)

spam = ['apples', 'bananas', 'tofu', 'cats']

main(spam)
