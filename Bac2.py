import math
print('Đây là phương trình giải phương trình bậc 2')
print('Phương trình bậc 2 có dạng ax^2 + bx + c = 0')
a = float(input('Nhập giá trị a: '))
if a == 0:
    print('Đây không phải là phương trình bậc 2 mà là phương trình bậc 1 ')
else:
    b = float(input('Nhập giá trị b: '))
    c = float(input('Nhập giá trị c: '))
    delta = b*b-4*a*c
    if delta < 0:
        print('Phương trình này không có nghiệm thực')
    elif delta ==0:
        print('Phương trình này có một nghiệm duy nhất là: ', -b/2/a )
    else:
        print('Phương trình này có hai nghiệm: ')
        print('Nghiệm 1 là: ', (-b+math.sqrt(delta))/2/a)
        print('Nghiệm 2 là: ', (-b-math.sqrt(delta))/2/a)

