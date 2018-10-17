"""var1 = 20
var2 = 30

print("Hello {} World {}".format(var1, var2))"""

arr = [1, 2]

if "1" in (num for num in str(arr)):
    print("true")
else:
    print("false")


print(" ".join(str(x) for x in arr))

arr.append(3)
print(arr)
arr.remove(3) #remove will delete the first matching argument parsed. pop will delete the value at the index parsed
print(arr)




class A(object):
    h, z = 1, 2
    def __init__(self, x, y): #or remove constructor as not needed in this instance
        self.x = x
        self.y = y

    def increment(self):
        self.x+=1
        return self.x

    def add(self, a, b):
        return a+b

    def sub(self, a, b):
        return a-b

method = A(1, 2)
print("Addition of {} + {}: {}".format(method.x, method.y, method.add(method.x, method.y)))
print("Before: {} After: {}".format(method.x, method.increment()))
#access class variable as method.z
#print(method.add(1, 2))
#print(method.sub(1, 2))
