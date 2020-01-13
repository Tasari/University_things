import matplotlib.pyplot  as plt
from numpy import array,zeros,arange

def SIR(state,t):
    S=state[0]
    I=state[1]
    R=state[2]
    IT=state[3]
    ds=omega*R-beta*S*I/Npop
    di=beta*S*I/Npop-gamma*I-getting_treated*I
    dr=gamma*I-omega*R+treat_effect*IT
    dit=getting_treated*I-treat_effect*IT
    return array([ds,di,dr, dit])

def Runge_Kutta(y,t,dt,derivative):
    k1=dt*derivative(y,t)
    k2=dt*derivative(y+k1/2.,t+0.5*dt)
    k3=dt*derivative(y+k2/2.,t+0.5*dt)
    k4=dt*derivative(y+k3,t+dt)
    y_next=y+1/6.*(k1+2*k2+2*k3+k4)
    return y_next

bety = [1, 1, 2, 3, 5]
gammy = [2, 1, 1, 1, 1]
for betat, gammat in zip(bety, gammy):
    global beta,gamma,Npop
    beta=betat #illness getting rate
    gamma=gammat #recorvery rate
    omega=2 #immunity losing rate
    getting_treated= 0.5 #rate of getting treatment
    treat_effect = gamma*2
    Npop=4*10**7 #population

    Io=10**4  #initial ill
    So=Npop-Io #initial susceptible
    ITo=0 #initial treated ill
    Ro=0 #initial recorvered
    illsum = Io #initial 
    dt=0.1 #check ratio
    to=0 #start
    te=6 #end
    t=arange(to,te,dt) #points from start to end in given ratio

    #creating initial data
    N=len(t)
    y=zeros([N,4])
    y[0,0]=So
    y[0,1]=Io
    y[0,2]=Ro
    y[0,3]=ITo

    #creating rest of the data
    for i in range(N-1):
        y[i+1]=Runge_Kutta(y[i],t[i],dt,SIR)

    #making data usable in plt
    St=[y[j,0] for j in range(N)]
    It=[y[j,1] for j in range(N)]
    Rt=[y[j,2] for j in range(N)]
    ITt=[y[j,3] for j in range(N)]

#sum of all ill people
    for amount in range(1, len(Rt)):
        illsum += Rt[amount]-Rt[amount-1]


    #creating plot
    plt.title("R = {}, Sum of ill = {}".format(beta/gamma, int(illsum)))
    plt.plot(t,St, label="Susceptible")
    plt.plot(t,It, label="Ill")
    plt.plot(t,Rt, label="Recorvered")
    plt.plot(t, ITt, label="Treated Ill")
    plt.ylabel("People")
    plt.xlabel("Time")
    plt.legend()
    plt.show()
