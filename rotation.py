import math
import numpy as np

new_coordinates = list(map(float, input("\nEnter the coordinates(final coordinates) : ").strip().split()))
check = 'y'


# rotation around X
def X_rotation_matrix(angle):
    angle=math.radians(angle)
    return np.array([[1, 0, 0], [0, math.cos(angle), -math.sin(angle)], [0, math.sin(angle), math.cos(angle)]])


# rotation around Y
def Y_rotation_matrix(angle):
    angle = math.radians(angle)
    return np.array([[math.cos(angle),0,math.sin(angle)],[0,1,0],[-math.sin(angle),0,math.cos(angle)]])


# rotation around Z
def Z_rotation_matrix(angle):
    angle = math.radians(angle)
    return np.array([[math.cos(angle),-math.sin(angle),0],[math.sin(angle),math.cos(angle),0],[0,0,1]])

rotation_matrix=[]
while (check == 'y'):
    # 0==X_axis,1==Y_axis,2==Z_axis
    # Angle in degrees

    angle, axis = list(map(int, input("\nEnter the angle and axis of rotation: ").strip().split()))
    if(axis == 0):
        matrix=X_rotation_matrix(angle)
        rotation_matrix.append(matrix)

    elif(axis == 1):
        matrix = Y_rotation_matrix(angle)
        rotation_matrix.append(matrix)

    elif(axis == 2):
        matrix = Z_rotation_matrix(angle)
        rotation_matrix.append(matrix)
    else:
        print("Invalid axis: ")

    check=input("Enter y to continue to add more rotations: ")

final_rotation_matrix = rotation_matrix[0]
for i in range(len(rotation_matrix)):
    if(i+1<len(rotation_matrix)):
        # post-multiplication multiple times
        final_rotation_matrix=np.matmul(final_rotation_matrix,rotation_matrix[i+1])

original_coordinates=np.matmul(final_rotation_matrix,np.transpose(new_coordinates))
# print(rotation_matrix)
print("Original coordinates(Before rotation) are: ",end='')
for i in original_coordinates:
    print(i,end=', ')
