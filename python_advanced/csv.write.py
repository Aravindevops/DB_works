import csv
f=open("data.csv","w",newline="")
content=[{"name":"Alice","age":30},{"name":"Bob","age":25}]
w=csv.writer(f)
w.writerow(content)
f.close()