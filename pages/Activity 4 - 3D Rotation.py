import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from scipy.spatial import Delaunay
import tensorflow as tf

# 3D Rotation by Carado, Molet & Pendon


def _plt_basic_object_(points):
    
    tri = Delaunay(points).convex_hull
    
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection='3d')
    S = ax.plot_trisurf(points[:,0], points[:,1], points[:,2],
                        triangles=tri,
                        shade=True, cmap=cm.rainbow, lw=0.5)
    
    ax.set_xlim3d(-8.5, 8.5)
    ax.set_ylim3d(-8.5, 8.5)
    ax.set_zlim3d(-8.5, 8.5)
    
    ax.set_xlabel ("X axis")
    ax.set_ylabel ("Y Axis")
    ax.set_zlabel ("Z Axis")
    plt.show()
    
    
def _90deg_(bottom_lower=(0, 0, 0)):
    
    bottom_lower = np.array(bottom_lower)
    
    points = np.vstack([
        bottom_lower + [-7.5, -7.5, -7.5],
        bottom_lower + [-7.5, -7.5, 7.5],
        bottom_lower + [7.5, -7.5, -7.5],
        bottom_lower + [-7.5, 7.5, 7.5],
        bottom_lower + [-7.5, 7.5, 7.5],
        bottom_lower + [7.5, 7.5, -7.5],
        bottom_lower + [-7.5, 7.5, -7.5],
    ])
    
    return points

def _pyramid_(bottom_lower=(0, 0, 0)):
    0
    bottom_lower = np.array(bottom_lower)
    
    points = np.vstack([
        bottom_lower,
        bottom_lower + [-5, -5, -5],
        bottom_lower + [5, -5, -5],
        bottom_lower + [5, 5, -5],
        bottom_lower + [-5, 5, -5],
        bottom_lower + [0, 0, 1]
    ])
    
    return points

def _diamond_(bottom_lower =(0, 0, 0)):

    bottom_lower = np.array(bottom_lower)

    points = np.vstack([
        bottom_lower,  
        bottom_lower + [0, 3, 0],
        bottom_lower + [0, 0, 5],
        bottom_lower + [3, 0, 0],
        bottom_lower + [0, 0, -5],
        bottom_lower + [3, 0, 0],
        bottom_lower + [0, 3, 0],
        bottom_lower
       
    ])
    
    return points

def _prism_(bottom_lower=(0, 0, 0)):
    
    bottom_lower = np.array(bottom_lower)
    
    points = np.vstack([
        bottom_lower + [5, -7.5, -2.5],
        bottom_lower + [5, 5, -2.5],
        bottom_lower + [0, 5, 2.5],
        bottom_lower + [0, -7.5, 2.5],
        bottom_lower + [-5, -7.5, -2.5],
        bottom_lower + [5, 5, -2.5],
        bottom_lower + [-5, 5, -2.5],
        bottom_lower,
    ])
    
    return points



def rotate_obj(points, angle):
    
    angle = float(angle)
    rotation_matrix = tf.stack([[tf.cos(angle), tf.sin(angle), 0],
                                [-tf.sin(angle), tf.cos(angle), 0],
                                [0, 0, 1]
                                ])

    return tf.matmul(tf.cast(points, tf.float32), tf.cast(rotation_matrix, tf.float32))

def main():
    
    print("1 Pyramid")
    print("2 90 Degree Angle Triangle")
    print("3 Diamond")
    print("4 Prism")
    choice = int(input("Input Shape: "))
    angle = float(input("Rotation Size : "))
    
    if choice == 1:
        init_shape_ = _pyramid_(bottom_lower=(0, 0, 0))
        with tf.compat.v1.Session() as session:
            rotated_object = session.run(rotate_obj(init_shape_, angle))
        
    elif choice == 2:
        init_shape_ = _90deg_(bottom_lower=(0, 0, 0))
        with tf.compat.v1.Session() as session:
            rotated_object = session.run(rotate_obj(init_shape_, angle))
        
    elif choice == 3:
        init_shape_ = _diamond_(bottom_lower=(0, 0, 0))
        with tf.compat.v1.Session() as session:
            rotated_object = session.run(rotate_obj(init_shape_, angle))
        
    elif choice == 4:
        init_shape_ = _prism_(bottom_lower=(0, 0, 0))
        with tf.compat.v1.Session() as session:
            rotated_object = session.run(rotate_obj(init_shape_, angle))
        
    _plt_basic_object_(rotated_object)
    
    
    
if __name__ == '__main__':
    main()