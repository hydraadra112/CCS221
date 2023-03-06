import streamlit as st
import matplotlib.pyplot as plt
st.title("Activity1\nGroup6\nMidpointLine")
def DDALine (x1,x2,y1,y2):

    x = [x1, x2]
    y = [y1, y2]
    
    x3 = (x1+x2) / 2 #Midpoint of X
    y3 = (y1 + y2) / 2 # Midpoint of Y
    print("Midpoint Line:", x3,"&", y3)
    
    plt.plot(x,y)
    plt.plot(x3,y3,marker="o", markersize=5, markerfacecolor="red")
    plt.show()

def main():
    x1 = int (input ( "Enter X1: "))
    y1 = int (input ( "Enter Y1: "))
    x2 = int (input ( "Enter X2: ")) 
    y2 = int (input ("Enter Y2: "))
    DDALine (x1,x2,y1,y2)
    
    
if __name__ == '__main__':
    main()
    
            