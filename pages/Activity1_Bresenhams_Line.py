import streamlit as st
import matplotlib.pyplot as plt
st.title("Activity1\nGroup6\nBresenhamsLine")


def BresenhamLine(x1, y1, x2, y2, color):
    
    x, y = x1, y1
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    
    grad = dy/float(dx)
    
    x3 = (x2 + x1) / 2
    y3 = (y2 + y1) / 2
   

    if grad > 1:
        dx, dy = dy, dx
        x, y = y, x
        x1, y1 = y1, x1
        x2, y2 = y2, x2

    p = 2 * dy - dx
    xcoordinates = [x]
    ycoordinates = [y]

    
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
        xcoordinates.append(x)
        ycoordinates.append(y)
        
    plt.plot(xcoordinates, ycoordinates)
    plt.plot(x3, y3, marker = "o", markersize = 5, markerfacecolor = "red")
    
    plt.show()
    st.pyplot(fig)
    
    st.write("Midpoint: ", int(x3), "&", int(y3))

def main():
    
    x = st.slider('X1: ', 0, 100, 1)
    y = st.slider('Y1: ', 0, 100, 1)

    x2 = st.slider('X2: ', 0, 100, 1)
    y2 = st.slider('Y2: ', 0, 100, 1)
    
    color = "g." 
    BresenhamLine(x, y, x2, y2, color)


if __name__ == '__main__':
    main()
            
