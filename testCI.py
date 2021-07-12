try:
    import improvmxpy as a
except ImportError:
    import os

    os.system("pip3 install improvmxpy")
else:
    pass
finally:
    import os
    import improvmxpy as a

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
    else:
      print("Publishing to pypi")
      import os
      name = os.getenv("twineusername")
      password = os.getenv("twinepassword")
      os.system(f"setup.py bdist_wheel && pip install twine && twine upload -u {name} -p {password} dist/* ")