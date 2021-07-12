try:
  import improvmxpy as a
except ImportError:
  import os;os.system("pip3 install improvmxpy");import improvmxpy as a
else:
  pass
finally:
  import  os
  a.SetUp(os.getenv("testtoken"))
  try:
    a.Account().GetAccountDetail()
    exit(0)
  except a.TokenError:
    print("TOKEN IS WRONG OR NOT FOUND")
    exit(1)
  except a.ServerError:
    print("SERVER ERROR COUNT THAT IT IS WORKING")
    exit(0)
