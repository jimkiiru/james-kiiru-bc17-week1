def data_type(n):
  if type(n) is int:
    if n < 100:
        print('less than 100')
    elif n == 100:
        print('equal to 100')
    else:
        print('more than 100')
  elif type(n) is None:
    print('no value')
  elif type(n) is bool:
    print(bool(n))
  elif type(n) is str:
    print(len(n))
  elif type(n) is list:
    if not n:
        print("None")
    else:
        print(n[2])
data_type(None)
