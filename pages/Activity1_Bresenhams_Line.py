import streamlit as st
import matplotlib.pyplot as plt
st.title("Activity1\nGroup6\nBresenhamsLine")


def BresenhamLine(x1, y1, x2, y2, color):
    
    fig = plt.figure()
    x,y = x1,y1
    dx = abs(x2 - x1)
    dy = abs(y2 -y1)
    
    gradient = dy/float(dx)

    if gradient > 1:
        dx, dy = dy, dx
        x, y = y, x
        x1, y1 = y1, x1
        x2, y2 = y2, x2

    p = 2*dy - dx
    
    xcords = [x]
    ycords = [y]

    for k in range(2, dx + 2):
        if p > 0:
            y = y + 1 if y < y2 else y - 1
            p = p + 2 * (dy - dx)
        else:
            p = p + 2 * dy

        x = x + 1 if x < x2 else x - 1
        
        xcords.append(x)
        ycords.append(y)
    
    plt.plot(xcords, ycords, color, marker='s', markersize=5)
    plt.plot(round(dx/2 + x1), round(dy/2 + y1), markersize=5)

    plt.show()
    st.pyplot(fig)
    
    st.write("Midpoint: ", float(x3), "&", float(y3))

def main():
    
    x = st.slider('X1: ', 0, 100, 1)
    y = st.slider('Y1: ', 0, 100, 1)

    x2 = st.slider('X2: ', 0, 100, 1)
    y2 = st.slider('Y2: ', 0, 100, 1)
    
    color = "b." 
    BresenhamLine(x, y, x2, y2, color)


if __name__ == '__main__':
    main()
            
