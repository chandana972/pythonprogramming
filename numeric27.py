s = input()
try:
    i = float(s)
    print("Yes")
except (ValueError, TypeError):
    print('No')
