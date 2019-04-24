def check(string):
    k = set(string) 
    s = {'0', '1'} 
    if s == k or k == {'0'} or k == {'1'}: 
        print("yes",end="") 
    else : 
        print("no",end="")
if __name__ == "__main__" : 
  string=input()
  check(string)
