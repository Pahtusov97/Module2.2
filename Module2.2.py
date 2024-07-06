First, Second, Third = int(input()), int(input()), int(input())
print(First, Second, Third)
if First == Second == Third:
    print(str(3))
elif First == Second or First == Third or Second == Third:
    print(str(2))
else:
    print(str(0))