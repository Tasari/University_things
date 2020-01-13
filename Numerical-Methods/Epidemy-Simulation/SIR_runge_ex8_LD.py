import matplotlib.pyplot  as plt
from numpy import array,zeros,arange

def SIR(state,t):
    S=state[0]
    I=state[1]
    R=state[2]
    IT=state[3]
    TR=state[4]
    NR=state[5]
    ds=omega*R-beta*S*I/Npop*(1-resistant_rate)-beta*S*I/Npop*resistant_rate+I*death_rate+R*death_rate+IT*death_rate+TR*death_rate+NR*death_rate
    di=beta*S*I/Npop*(1-resistant_rate)-gamma*I-getting_treated*I - I*death_rate
    dr=gamma*I-omega*R+treat_effect*IT+gamma*NR+TR*resistant_treat - R*death_rate
    dit=getting_treated*I-treat_effect*IT-resistant_rate*I*getting_treated-IT*death_rate
    dtr=NR*getting_treated-TR*resistant_treat-TR*death_rate
    dnr=beta*S*I/Npop*resistant_rate-gamma*NR-NR*getting_treated-NR*death_rate
    return array([ds,di,dr, dit, dtr, dnr])

def Runge_Kutta(y,t,dt,derivative):
    k1=dt*derivative(y,t)
    k2=dt*derivative(y+k1/2.,t+0.5*dt)
    k3=dt*derivative(y+k2/2.,t+0.5*dt)
    k4=dt*derivative(y+k3,t+dt)
    y_next=y+1/6.*(k1+2*k2+2*k3+k4)
    return y_next

bety = [1, 1, 2, 3, 5, 10]
gammy = [2, 1, 1, 1, 1, 1]
for betat, gammat in zip(bety, gammy):
    global beta,gamma,Npop
    beta=betat #illness getting rate
    gamma=gammat #recorvery rate
    resistant_rate=0.1 #rate of resistant 
    omega=0#immunity losing rate
    getting_treated = 2 #rate of getting treatment
    resistant_treat = 1.5*gamma
    treat_effect = gamma*3
    death_rate = 0.2
    Npop=4*10**7 #population

    Io=10**4  #initial ill
    So=Npop-Io #initial susceptible
    ITo=0 #initial treated ill
    TRo=0 #initial treated resistant
    NRo=0 #initial nontreated resistant
    Ro=0 #initial recorvered
    illsum = Io #initial 
    dt=0.1 #check ratio
    to=0 #start
    te=11#end
    t=arange(to,te,dt) #points from start to end in given ratio

    #creating initial data
    N=len(t)
    y=zeros([N,6])
    y[0,0]=So
    y[0,1]=Io
    y[0,2]=Ro
    y[0,3]=ITo
    y[0,4]=TRo
    y[0,5]=NRo

    #creating rest of the data
    for i in range(N-1):
        y[i+1]=Runge_Kutta(y[i],t[i],dt,SIR)

    #making data usable in plt
    St=[y[j,0] for j in range(N)]
    It=[y[j,1] for j in range(N)]
    Rt=[y[j,2] for j in range(N)]
    ITt=[y[j,3] for j in range(N)]
    TRt=[y[j,4] for j in range(N)]
    NRt=[y[j,5] for j in range(N)]

#sum of all ill people
    for amount in range(1, len(Rt)):
        illsum += Rt[amount]-Rt[amount-1]


    #creating plot
    plt.title("R = {}, Sum of ill = {}".format(beta/gamma, int(illsum)))
    plt.plot(t,St, label="Susceptible")
    plt.plot(t,It, label="Ill")
    plt.plot(t,Rt, label="Recorvered")
    plt.plot(t, ITt, label="Treated Ill")
    plt.plot(t, NRt, label="Nontreated Resistant")
    plt.plot(t, TRt, label="Treated Resistant")
    plt.ylabel("People")
    plt.xlabel("Time")
    plt.legend()
    plt.show()
