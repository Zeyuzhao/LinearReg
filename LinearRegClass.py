import numpy as np
import matplotlib.pyplot as plt
class LinearReg:
    def __init__(self, X, y, a = 0.01, initTheta = None, iter = 5000):
        m = X.shape[0]
        self.m = m
        if type(X) is np.ndarray:
            X.shape = (m, 1)
        y.shape = (m, 1)
        if not np.sum(X[:, 0]) == m: # check if column are all ones
            o = np.ones(m)
            o.shape = (m,1)
            X = np.hstack((o, X)) # append column if needed

        self.n = X.shape[1] - 1

        self.X = X
        self.y = y
        self.a = a

        if initTheta == None:
            initTheta = np.ones(self.n + 1)
        initTheta.shape = (self.X.shape[1],1)

        self.theta = initTheta
        self.iter = iter

        plt.ion()




    def hThetaFunction(self, theta = None):
        if theta is None:
            theta = self.theta
        return np.dot(self.X, theta)


    def costFunction(self, theta = None):
        h = self.hThetaFunction(theta)
        y = self.y
        m = self.m

        diff = h - y

        j = np.dot(diff.T, diff) / (2 * m)
        return j

    def gradientCost(self, theta = None):
        h = self.hThetaFunction(theta)
        y = self.y
        m = self.m
        X = self.X
        diff = h - y

        thetaGradient = np.dot(X.T, diff) / m;
        return thetaGradient

    def gradientDescent(self):

        T = self.theta
        X = self.X
        m = self.m
        a = self.a
        iter = self.iter
        samples = 100 # take a total of 500 samples
        div = np.floor(iter / samples) # every 'div' will get sampled


        plt.subplot(211)
        costGraph = plt.plot([],[])[0]
        xmin = 1
        ymin = 4
        xmax = samples
        ymax = 50
        plt.axis([xmin,xmax,ymin,ymax])

        plt.subplot(212)
        plt.plot(self.X[:,1],self.y, 'bo')

        pX = np.linspace(0, 30, 1000)

        pY = T[0] + T[1] * pX
        linRegPlot = plt.plot(pX, pY)[0]


        for i in xrange(iter):

            g = self.gradientCost(T)
            print(T)
            T = T - a * g

            if i % div == 0:

                c = self.costFunction(T)
                costGraph.set_xdata(np.append(costGraph.get_xdata(), i/div))

                costGraph.set_ydata(np.append(costGraph.get_ydata(), c))

                pY = T[0] + T[1] * pX
                linRegPlot.set_ydata(pY)
                plt.pause(0.01)
                plt.draw()





        self.theta = T
        plt.pause(0)

if __name__ == 'main':
    pass;











