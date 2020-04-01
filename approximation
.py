import scipy as sp
import matplotlib.pyplot as plt


zx = 5
zy = 5
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot([-zx, zx], [zy, -zy], '.w')
plt.axhline(0, color='k', lw=0.5)
w1, = ax.plot([], [], 'xb', label='points')
w2, = ax.plot([], [], '-r', label='polynomial')
X = []
Y = []


def onclick(event):
    global X, Y, w1

    def xx():
        x = sp.sort(X)
        for i, s in enumerate(list(sp.asarray(X).argsort())):
            if x[i] == x[i - 1]:
                return X.remove(X[s]), Y.remove(Y[s]), xx()

    if event.button == 1 and event.inaxes:
        X.append(event.xdata)
        Y.append(event.ydata)
        w1.set_data(X, Y)
        fig.canvas.draw()
        plt.show()
    else:
        plt.disconnect(cid)

        xx()

        nx = len(X)
        x = sp.poly1d([1, 0])
        L = 0
        for i in sp.arange(nx):
            pom =1
            for j in sp.hstack((sp.arange(i), sp.arange(i+1, nx))):
                pom *= (x-X[j])/(X[i]-X[j])
            L += pom*Y[i]
        print("\nWielomian lagrange interpolujacy {} punkt ma postac:\n\tx\ty\n {}\n nL:\n {} ".format(nx,sp.stack((X,Y),axis=1),L))
        xw = sp.linspace(min(X), max(X), 1000)
        yw = L(xw)
        w2.set_data(xw,yw)
        ax.set_title("lagrange interpolacja {} pktow".format(nx))
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.axis('equal')
        ax.legend()
        fig.canvas.draw()


cid = fig.canvas.mpl_connect('button_press_event',onclick)
plt.show()