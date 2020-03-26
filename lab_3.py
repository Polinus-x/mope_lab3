import random
import numpy as np
import math

koh =  [0, 9065, 7679, 6841, 6287, 5892, 5598, 5365, 5175, 5017, 4884]
student = {8: 2.306, 12: 2.179, 16: 2.120, 20: 2.086, 14: 2.064, 28: 2.048}

x1 = [20, 70]
x2 = [30, 80]
x3 = [30, 35]
x_min_aver = int((x1[0] + x2[0] + x3[0]) / 3)
x_max_aver = int((x1[1] + x2[1] + x3[1]) / 3)
y_min = 200 + x_min_aver
y_max = 200 + x_max_aver

incrementation = True

m = 3
n = 4
while incrementation:
    f1 = m - 1
    f2 = n
    f3 = f1 * f2

    usual_matrix = [[20, 20, 30], [20, 80, 35], [70, 30, 35], [70, 80, 30]]
    norm_matrix = [[1, -1, -1, -1], [1, -1, 1, 1], [1, 1, -1, 1], [1, 1, 1, -1]]

    average_ys = []
    mx = []
    a = []
    a_duplicate = []

    dispersion = []
    b = []
    kohren_exp = 0
    beta = []
    t_kof = []


  # случайно сгенер.  у для матриц
    for i in range(4):
        for t in range(m):
            new_y = random.randint(y_min, y_max)
            usual_matrix[i].append(new_y)
            norm_matrix[i].append(new_y)


      # средние игрики
    for i in range(4):
        ay = 0
        for k in range(m):
            ay += usual_matrix[i][k + 3]
        average_ys.append(ay / m)



    for i in range(3):
        t = 0
        k = 0
        d = 0
        for k in range(4):
            d += usual_matrix[k][i] * average_ys[k]
            t += usual_matrix[k][i]
            k += usual_matrix[k][i] ** 2
        mx.append(t / n)
        a_duplicate.append(k / n)
        a.append(k / n)

    a12 = (usual_matrix[0][0] * usual_matrix[0][1] + usual_matrix[1][0] * usual_matrix[1][1] + usual_matrix[2][0] * usual_matrix[2][1] + usual_matrix[3][0] * usual_matrix[3][1]) / 4
    a13 = (usual_matrix[0][0] * usual_matrix[0][2] + usual_matrix[1][0] * usual_matrix[1][2] + usual_matrix[2][0] * usual_matrix[2][2] + usual_matrix[3][0] * usual_matrix[3][2]) / 4
    a23 = (usual_matrix[0][1] * usual_matrix[0][2] + usual_matrix[1][1] * usual_matrix[1][2] + usual_matrix[2][1] * usual_matrix[2][2] + usual_matrix[3][1] * usual_matrix[3][2]) / 4

    my = sum(average_ys) / n


    arr0 = [[my, mx[0], mx[1], mx[2]], [a[0], a_duplicate[0], a12, a13], [a[1], a12, a_duplicate[1], a23], [a[2], a13, a23, a_duplicate[2]]]
    arr1 = [[1, my, mx[1], mx[2]], [mx[0], a[0], a12, a13], [mx[1], a[1], a_duplicate[1], a23], [mx[2], a[2], a23, a_duplicate[2]]]
    arr2 = [[1, mx[0], my, mx[2]], [mx[0], a_duplicate[0], a[0], a13], [mx[1], a12, a[1], a23], [mx[2], a13, a[2], a_duplicate[2]]]
    arr3 = [[1, mx[0], mx[1], my], [mx[0], a_duplicate[0], a12, a[0]], [mx[1], a12, a_duplicate[1], a[1]], [mx[2], a13, a23, a[2]]]
    b_m = [[1, mx[0], mx[1], mx[2]], [mx[0], a_duplicate[0], a12, a13], [mx[1], a12, a_duplicate[1], a23], [mx[2], a13, a23, a_duplicate[2]]]

    detb = np.linalg.det(b_m)

    b0 = np.linalg.det(arr0) / detb
    b1 = np.linalg.det(arr1) / detb
    b2 = np.linalg.det(arr2) / detb
    b3 = np.linalg.det(arr3) / detb
    b.append(b0)
    b.append(b1)
    b.append(b2)
    b.append(b3)


    for i in range(4):
        s = 0
        for t in range(m):
            s += (usual_matrix[i][t + 3] - average_ys[i]) ** 2
        dispersion.append(s / m)



    kohren_exp = max(dispersion) / sum(dispersion)

    if kohren_exp < koh[m]/10000:
        incrementation = False
        print("Дисперсія однорідна")
        break
    else:
        m += 1
        print("Дисперсія неоднорідна")


    sb = sum(dispersion) / n
    sb_beta2 = sb / (n * m)
    sb_beta = math.sqrt(sb_beta2)

    for i in range(4):
        b_else = 0
        for k in range(4):
            b_else += average_ys[k] * norm_matrix[i][k]
        beta.append(b_else / n)
        t_kof.append(abs(b_else) / sb_beta)

    for i in range(4):
        if t_kof[i] < student[f3]:
            b[i] = 0

print(" m = ", m)
print("рівняння : y = {} + {} * x1 + {} * x2 + {} * x3".format(int(b[0]), int(b[1]), int(b[2]), (b[3])))