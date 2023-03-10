import streamlit as st
import matplotlib.pyplot as plt
st.title("Activity1\nGroup6\nMidpointLine")
def DDALine (x1,x2,y1,y2):
    fig = plt.figure()

    x = [x1, x2]
    y = [y1, y2]
    
    x3 = (x1+x2) / 2 #Midpoint of X
    y3 = (y1 + y2) / 2 # Midpoint of Y
    st.write("Midpoint Line:", x3,"&", y3)
    
    plt.plot(x,y)
    plt.plot(x3,y3,marker="o", markersize=5, markerfacecolor="red")
    plt.show()
    st.pyplot(fig)

def main():
    x1 = st.slider('X1: ', 0, 100, 1)
    y1 = st.slider('Y1: ', 0, 100, 1)
    x2 = st.slider('X2: ', 0, 100, 1)
    y2 = st.slider('Y2: ', 0, 100, 1)
    
    DDALine (x1,x2,y1,y2)
    
    
if __name__ == '__main__':
    main()
    
            
