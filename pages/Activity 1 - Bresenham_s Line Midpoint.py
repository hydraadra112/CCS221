import matplotlib.pyplot as plt

def DDALine (x1, y1, x2, y2, color):
    dx = abs(x1 - x2)
    dy = abs(y1 - y2)
    
    x3 = (x1+x2) / 2 #Midpoint of X
    y3 = (y1 + y2) / 2 # Midpoint of Y
    print("Midpoint Line:", x3,"&", y3)
    
    steps = abs(dx) if abs(dx) > abs(dy) else abs(dy)
    
    Xinc = float(dx / steps)
    Yinc = float(dy / steps)
    
    for i in range (0, int(steps+1)):
        plt.plot(int(x1), int(y1), color)
        x1 += Xinc
        y1 += Yinc
        
    plt.plot(x3,y3,marker="o", markersize=5, markerfacecolor="r")
    plt.show()
    
def main () :
    x1 = int (input ( "Enter X1: "))
    y1 = int (input ( "Enter Y1: "))
    x2 = int (input ( "Enter X2: ")) 
    y2 = int (input ("Enter Y2: "))
    color = "b."
    DDALine (x1, y1, x2, y2, color)
    
    #Enter X1: 10
    #Enter Y1: 15
    #Enter X2: 45
    #Enter Y2: 67 
    
if __name__ == '__main__':
    main()
            