try:
    d={"name":"arun","age":23,"place":"ekm"}
    key=input("enter a key:")
    print(d[key])
except KeyError:
    print("key not found")
