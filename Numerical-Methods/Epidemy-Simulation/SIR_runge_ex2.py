import matplotlib.pyplot  as plt
from numpy import array,zeros,arange

def SIR(state,t):
    S=state[0]
    I=state[1]
    R=state[2]
    ds=-beta*S*I/Npop
    di=beta*S*I/Npop-gamma*I
    dr=gamma*I
    return array([ds,di,dr])

def Runge_Kutta(y,t,dt,derivative):
    k1=dt*derivative(y,t)
    k2=dt*derivative(y+k1/2.,t+0.5*dt)
    k3=dt*derivative(y+k2/2.,t+0.5*dt)
    k4=dt*derivative(y+k3,t+dt)
    y_next=y+1/6*(k1+2*k2+2*k3+k4)
    return y_next

bety = [1, 2, 3, 5]
gammy = [1, 1, 1, 1]
for betat, gammat in zip(bety, gammy):
    global beta,gamma,Npop
    beta=betat #illness getting rate
    gamma=gammat #recorvery rate
    Npop=4*10**7 #population

    Ro=2.5*10**7 #initial recorvered
    Io=10**4  #initial ill
    So=Npop-Io-Ro #initial susceptible


    dt=0.1 #check ratio
    to=0 #start
    te=6 #end
    t=arange(to,te,dt) #points from start to end in given ratio

    #creating initial data
    N=len(t)
    y=zeros([N,3])
    y[0,0]=So
    y[0,1]=Io
    y[0,2]=Ro

    #creating rest of the data
    for i in range(N-1):
        y[i+1]=Runge_Kutta(y[i],t[i],dt,SIR)


    #making data usable in plt
    St=[y[j,0] for j in range(N)]
    It=[y[j,1] for j in range(N)]
    Rt=[y[j,2] for j in range(N)]

    #creating plot
    plt.title("R = {}".format(beta/gamma))
    plt.plot(t,St, label="Susceptible")
    plt.plot(t,It, label="Ill")
    plt.plot(t,Rt, label="Recorvered")
    plt.ylabel("People")
    plt.xlabel("Time")
    plt.legend()
    plt.show()