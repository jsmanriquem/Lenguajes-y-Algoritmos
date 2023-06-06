import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Definitions
Ke = 8.987*pow(10,15) #[N][mm^2][C^-2]
qe = 1.6*pow(10,-19) #C
mp = 1.6726*pow(10,-27) #kg
me = 9.109*pow(10,-31) #kg
t = 0.01
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
O1 = [0,0,0,1*mp,1*qe] #[x,y,z,m,q] [mm,mm,mm,kg,C]
V1 = [12.5,-15,1] #[vx,vy,vz] [mm][s^-1]
O2 = [-1,2,25,1*mp,-1*qe] #[x,y,z,m,q] [mm,mm,mm,kg,C]
V2 = [12.5,15,0.002]#[vx,vy,vz] [mm][s^-1]

def GUpdater(CoM,n):
     Obj1 = [[O1[0]],[O1[1]],[O1[2]]]
     Obj2 = [[O2[0]],[O2[1]],[O2[2]]]
     #miu = (O1[3]*O2[3])/(O1[3]+O2[3])
     #C1 = O2[3]/(O1[3]+O2[3])
     #C2 = O1[3]/(O1[3]+O2[3])
     M = abs(Ke*O1[4]*O2[4])
     F = [0,0,0]
     CoM_h = [[CoM[0]],[CoM[1]],[CoM[2]]]
     for i in range(1,n):
         r = [(O1[0]-O2[0]),(O1[1]-O2[1]),(O1[2]-O2[2])]
         r_mag = np.sqrt((r[0]**2)+(r[1]**2)+(r[2]**2))
         for k in range(3):
             CoM[k] = ((O1[k]*O1[3])+(O2[k]*O2[3]))/(O1[3]+O2[3])
             F[k] = (M/(r_mag**3))*r[k]
             CoM_h[k].append(CoM[k])
         print('r: ',round(r_mag,2),'    F: ',round(np.sqrt((F[0]**2)+(F[1]**2)+(F[2]**2)),3))
         for j in range(3):
             V1[j] = V1[j] + (-F[j]*t*0.5)/O1[3]
             O1[j] = O1[j] + (V1[j]*t)
             Obj1[j].append(O1[j])
             V2[j] = V2[j] + (F[j]*t*0.5)/O2[3]
             O2[j] = O2[j] + (V2[j]*t)
             Obj2[j].append(O2[j])
     return [Obj1,Obj2,CoM_h]

def animator(k):
     Graph.set_offsets([[CoM_Vec[0][k],CoM_Vec[1][k]],[O1_Vec[0][k],O1_Vec[1][k]],[O2_Vec[0][k],O2_Vec[1][k]]])
     Graph.set_3d_properties([CoM_Vec[2][k],O1_Vec[2][k],O2_Vec[2][k]],'z')
     Path1.set_data_3d(O1_Vec[0][:k],O1_Vec[1][:k],O1_Vec[2][:k])
     Path2.set_data_3d(O2_Vec[0][:k],O2_Vec[1][:k],O2_Vec[2][:k])
     if k < (len(O1_Vec[0])-20):
         L = k+20
         ax.set_xlim([min(min(O1_Vec[0][:L]),min(O2_Vec[0][:L])),max(max(O1_Vec[0][:L]),max(O2_Vec[0][:L]))])
         ax.set_ylim([min(min(O1_Vec[1][:L]),min(O2_Vec[1][:L])),max(max(O1_Vec[1][:L]),max(O2_Vec[1][:L]))])
         ax.set_zlim([min(min(O1_Vec[2][:L]),min(O2_Vec[2][:L])),max(max(O1_Vec[2][:L]),max(O2_Vec[2][:L]))])
     return (Graph, Path1, Path2)


#ask variables
fr = int(input('Frames: '))
for i in range(2):
        Ipt = input('Use default (Y/N): ')
        if Ipt == 'N':
            print('Object ',str(i + 1))
            x = (np.random.random()*50)-25
            y = (np.random.random()*50)-25
            z = (np.random.random()*50)-25
            Vx = (np.random.random()*50)-25
            Vy = (np.random.random()*50)-25
            Vz = (np.random.random()*50)-25
            if i == 0:
                O1 = [x,y,z,O1[3],O1[4]]
                V1 = [Vx,Vy,Vz]
            else:
                O2 = [x,y,z,O2[3],O2[4]]
                V2 = [Vx,Vy,Vz]


#Start
CoM = [0,0,0]
for i in range(3):
     CoM[i] = ((O1[i]*O1[3])+(O2[i]*O2[3]))/(O1[3]+O2[3])

Unv = GUpdater(CoM,fr)
O1_Vec = Unv[0]
O2_Vec = Unv[1]
CoM_Vec = Unv[2]


rep = input('Start(Y/N): ')
frame = input('Reference(C/I): ')


if (frame == "C") and (rep != 'N'):
     for j in range(len(O1_Vec[0])):
         for i in range(3):
             O1_Vec[i][j] = (CoM_Vec[i][j] - O1_Vec[i][j])
             O2_Vec[i][j] = (CoM_Vec[i][j] - O2_Vec[i][j])
             CoM_Vec[i][j] = 0

Graph = ax.scatter(
     [CoM_Vec[0][0],O1_Vec[0][0],O2_Vec[0][0]],
     [CoM_Vec[1][0],O1_Vec[1][0],O2_Vec[1][0]],
     [CoM_Vec[2][0],O1_Vec[2][0],O2_Vec[2][0]],
     c = [[0,0,0],[0,0,1],[1,0,0]]
    )
Path1 = ax.plot(O1_Vec[0][0],O1_Vec[1][0],O1_Vec[2][0],'b-')[0]
Path2 = ax.plot(O2_Vec[0][0],O2_Vec[1][0],O2_Vec[2][0],'r-')[0]

if rep != 'N':
     L = 20
     ax.set_xlim([min(min(O1_Vec[0][0:L]),min(O2_Vec[0][0:L])),max(max(O1_Vec[0][0:L]),max(O2_Vec[0][0:L]))])
     ax.set_ylim([min(min(O1_Vec[1][0:L]),min(O2_Vec[1][0:L])),max(max(O1_Vec[1][0:L]),max(O2_Vec[1][0:L]))])
     ax.set_zlim([min(min(O1_Vec[2][0:L]),min(O2_Vec[2][0:L])),max(max(O1_Vec[2][0:L]),max(O2_Vec[2][0:L]))])
     anim = animation.FuncAnimation(fig,animator,repeat = True,frames = len(O1_Vec[0]), interval = int(t*20000))
     plt.show()