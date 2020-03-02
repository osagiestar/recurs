def recurs(y):
    if (y > 1):
      result = y + recurs(y-1)
      print(result)
    else:
      result = 0
    return result

print("End of the recursive loop")
recurs(6)

