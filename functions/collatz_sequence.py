def collatz(n):
  if n % 2 == 0:
     print(n // 2)
     return n // 2
  else:
    print(3 * n + 1)
    return 3 * n + 1

def main():
  while True:
    try:
      i = int(input("Enter number: "))
    except ValueError:
      continue
    else: 
      break
  while i != 1:
    i = collatz(i)

main()

