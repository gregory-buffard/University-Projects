import matplotlib.pyplot as plt


def display2DPoints(*lstPoints: list):
    '''This function takes a list of Point2D as parameter and plot them by using the matplotlib module'''
    for lstPoint in lstPoints:
        xSet: list =[]
        ySet: list = []
        for p in lstPoint:
            xSet = xSet + [p.x]
            ySet = ySet + [p.y]    
        plt.plot(xSet, ySet, marker='.')
    plt.show()
