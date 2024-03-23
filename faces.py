s = input()
def main(s):
  s = s.replace(":)",'\N{Slightly Smiling Face}')
  s = s.replace(":(",'\N{Slightly Frowning Face}')
  return(s)

print(main(s))
