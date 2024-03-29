import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Activity 1")

def BresenhamLine(x1, y1, x2, y2, color):
    
    x, y = x1, y1
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    gradient = dy/float(dx)
   

    if gradient > 1:
        dx, dy = dy, dx
        x, y = y, x
        x1, y1 = y1, x1
        x2, y2 = y2, x2

    p = 2 * dy - dx
    xcords = [x]
    ycords = [y]

    
    steps = abs(dx) if abs(dx) > abs(dy) else abs(dy)

    fig = plt.figure()
    for i in range(0, int(steps + 1)):
        
        if p > 0:
            y = y + 1 if y < y2 else y - 1
            p = p + 2 * (dy - dx)
        else:
            p = p + 2  * dy

        x = x + 1 if x < x2 else x - 1

        print('x = %s, y = %s' % (x, y))
        xcords.append(x)
        ycords.append(y)
        
    plt.plot(xcords, ycords)
    plt.show()
    st.pyplot(fig)
    
def BresenhamLineMidpoint(x1, y1, x2, y2, color):
    
    x, y = x1, y1
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    gradient = dy/float(dx)
    x3 = (x2 + x1) / 2
    y3 = (y2 + y1) / 2
   

    if gradient > 1:
        dx, dy = dy, dx
        x, y = y, x
        x1, y1 = y1, x1
        x2, y2 = y2, x2

    p = 2 * dy - dx
    xcords = [x]
    ycords = [y]

    
    steps = abs(dx) if abs(dx) > abs(dy) else abs(dy)

    fig = plt.figure()
    for i in range(0, int(steps + 1)):
        
        if p > 0:
            y = y + 1 if y < y2 else y - 1
            p = p + 2 * (dy - dx)
        else:
            p = p + 2  * dy

        x = x + 1 if x < x2 else x - 1

        print('x = %s, y = %s' % (x, y))
        xcords.append(x)
        ycords.append(y)
        
    plt.plot(x3,y3, marker="x", markersize=6, markerfacecolor="r")
    plt.plot(xcords, ycords)
    plt.show()
    st.pyplot(fig)
    
def DDALine(x1, y1, x2, y2, color):
    fig = plt.figure()
    dx = abs(x1 - x2)
    dy = abs(y1 - y2)
    
    x3 = (x1+x2) / 2 #Midpoint of X
    y3 = (y1 + y2) / 2 # Midpoint of Y
    
    if abs(dx) > abs(dy):
        steps = abs(dx)
    
    else:
        steps = abs(dy)
        
    
    Xinc = float(dx / steps)
    Yinc = float(dy / steps)
    
    for i in range (0, int(steps+1)):
        plt.plot(int(x1), int(y1), color)
        x1 += Xinc
        y1 += Yinc
    
    plt.plot(x3,y3,marker="x", markersize=5, markerfacecolor="r")
    plt.show()
    st.pyplot(fig)
    
def Midpoint(x1,x2,y1,y2):
    fig = plt.figure()

    x = [x1, x2]
    y = [y1, y2]
    
    x3 = (x1+x2) / 2 #Midpoint of X
    y3 = (y1 + y2) / 2 # Midpoint of Y
    
    plt.plot(x,y)
    plt.plot(x3,y3,marker="o", markersize=5, markerfacecolor="red")
    plt.show()
    st.pyplot(fig)


def main():
    
    st.sidebar.title('ACT 1 Controls')
    x = st.sidebar.slider('X1: ', 0, 100, 1)
    y = st.sidebar.slider('Y1: ', 0, 100, 1)

    x2 = st.sidebar.slider('X2: ', 0, 100, 1)
    y2 = st.sidebar.slider('Y2: ', 0, 100, 1)
    
    x3 = (x + x2) / 2 #Midpoint of X
    y3 = (y + y2) / 2 # Midpoint of Y
    
    st.sidebar.write("Midpoint: ", float(x3), "&", float(y3))
    
    color = "b." 
    st.write('Bresenhams Line')
    BresenhamLine(x, y, x2, y2, color)
    
    st.write('Bresenhams Line Midpoint')
    BresenhamLineMidpoint(x, y, x2, y2, color)

    st.write('DDA Line')
    DDALine(x, y, x2, y2, color)
    
    st.write('Midpoint Line')
    Midpoint(x,x2,y,y2)

if __name__ == '__main__':
    main()
