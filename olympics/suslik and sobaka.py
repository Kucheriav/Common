x_s = int(input())
y_s = int(input())
u_s = int(input())
x_p = int(input())
y_p = int(input())
u_p = int(input())
x_n = int(input())
y_n = int(input())
# расстояние от суслика до норки
d_s = ((x_s - x_n) ** 2 + (y_s - y_n) ** 2) ** 0.5
# расстояние от собаки до норки
d_p = ((x_p - x_n) ** 2 + (y_p - y_n) ** 2) ** 0.5
if d_s // u_s > d_p // u_p:
    print('Не добежит')
else:
    print('Добежит')