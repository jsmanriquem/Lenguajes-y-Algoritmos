import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Definitions
Ke = 8.987*pow(10,15) #[N][mm^2][C^-2]
qe = 1.6*pow(10,-19) #C
mp = 1.6726*pow(10,-27) #kg
me = 9.109*pow(10,-31) #kg
t = 0.02
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
O1 = [-14.2,20,11.2,4*mp,2*qe] #[x,y,z,m,q] [mm,mm,mm,kg,C] [0,0,0,4*mp,2*qe]
V1 = [23.1,12.4,-4.1] #[vx,vy,vz] [mm][s^-1] [20,-10,0]
O2 = [18.9,-13.6,16.4,1*mp,-1*qe] #[x,y,z,m,q] [mm,mm,mm,kg,C] [-15,-10,30,1*mp,-1*qe]
V2 = [22.8,-10.7,-23.9]#[vx,vy,vz] [mm][s^-1] [50,-20,-5]
#O1 = [0,0,0,1*mp,1*qe] #[-14.20425898414694, 20.014689133979722, 11.189752936045409, 6.6904e-27, 3.2000000000000003e-19]
#V1 = [0,0,0] #[vx,vy,vz] #[23.08780822084985, 12.426020005944679, -4.102007123884992]
#O2 = [100,0,5,1*me,-1*qe] #[18.906962655879596, -13.616540303232588, 16.391123783983346, 6.6904e-27, 3.2000000000000003e-19]
#V2 = [500,-1000,2] #[22.825001078257877, -10.682051587849378, -23.90572949807635]

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
         print(i,'  r: ',round(r_mag,2),'mm   F: ',round(np.sqrt((F[0]**2)+(F[1]**2)+(F[2]**2))*(10**21),3),'zN')
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
     #ax.view_init(elev = camera[0][k], azim = camera[1][k])
     
     if k < (len(O1_Vec[0])-50):
         L = k+50
         F = 0
         if k >= 50:
             F = k - 50
         lim[0] = [min((min(O1_Vec[0][F:L])+O1_Vec[0][k])/2,(min(O2_Vec[0][F:L])+O2_Vec[0][k])/2),
                   max((max(O1_Vec[0][F:L])+O1_Vec[0][k])/2,(max(O2_Vec[0][F:L])+O2_Vec[0][k])/2)]
         lim[1] = [min((min(O1_Vec[1][F:L])+O1_Vec[1][k])/2,(min(O2_Vec[1][F:L])+O2_Vec[1][k])/2),
                   max((max(O1_Vec[1][F:L])+O1_Vec[1][k])/2,(max(O2_Vec[1][F:L])+O2_Vec[1][k])/2)]
         lim[2] = [min((min(O1_Vec[2][F:L])+O1_Vec[2][k])/2,(min(O2_Vec[2][F:L])+O2_Vec[2][k])/2),
                   max((max(O1_Vec[2][F:L])+O1_Vec[2][k])/2,(max(O2_Vec[2][F:L])+O2_Vec[2][k])/2)]
         ax.set_xlim(lim[0])
         ax.set_ylim(lim[1])
         ax.set_zlim(lim[2])
     return (Graph, Path1, Path2)


#ask variables
fr = int(input('Frames: '))
for i in range(2):
        Ipt = input('Use default (Y/N): ')
        if Ipt == 'N':
            x = (np.random.random()*50)-25
            y = (np.random.random()*50)-25
            z = (np.random.random()*50)-25
            Vx = (np.random.random()*50)-25
            Vy = (np.random.random()*50)-25
            Vz = (np.random.random()*50)-25
            print('Object ',str(i + 1))
            print([x,y,z,O1[3],O1[4]])
            print([Vx,Vy,Vz])
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

ax.view_init(elev = 15, azim = -30)
ax.set_xlabel('mm')
ax.set_ylabel('mm')
ax.set_zlabel('mm')
Graph = ax.scatter(
     [CoM_Vec[0][0],O1_Vec[0][0],O2_Vec[0][0]],
     [CoM_Vec[1][0],O1_Vec[1][0],O2_Vec[1][0]],
     [CoM_Vec[2][0],O1_Vec[2][0],O2_Vec[2][0]],
     c = [[0,0,0],[0,0,1],[1,0,0]]
    )
Path1 = ax.plot(O1_Vec[0][0],O1_Vec[1][0],O1_Vec[2][0],'b-')[0]
Path2 = ax.plot(O2_Vec[0][0],O2_Vec[1][0],O2_Vec[2][0],'r-')[0]
camera = [[15],[-30]]

for i in range(1,fr):
     if (i > fr/4) and (i <= ((fr/4) + 25)):
         Cx = 0
         Cy = 1.2
     elif (i > fr/2) and (i <= ((fr/2) + 25)):
         Cx = 3
         Cy = 0
     elif (i > (3*fr)/4) and (i <= ((3*fr)/4 + 25)):
         Cx = -3
         Cy = -1.2
     else:
         Cx = 0
         Cy = 0
     camera[0].append(camera[0][i-1] + Cx)
     camera[1].append(camera[1][i-1] + Cy)

if rep != 'N':
     L = 50
     lim = [[min(min(O1_Vec[0][:L]),min(O2_Vec[0][:L])),max(max(O1_Vec[0][:L]),max(O2_Vec[0][:L]))],
            [min(min(O1_Vec[1][:L]),min(O2_Vec[1][:L])),max(max(O1_Vec[1][:L]),max(O2_Vec[1][:L]))],
            [min(min(O1_Vec[2][:L]),min(O2_Vec[2][:L])),max(max(O1_Vec[2][:L]),max(O2_Vec[2][:L]))]]
     ax.set_xlim(lim[0])
     ax.set_ylim(lim[1])
     ax.set_zlim(lim[2])
     anim = animation.FuncAnimation(fig,animator,repeat = True,frames = len(O1_Vec[0]), interval = int(t*10000))
     plt.show()
     #anim.save(writer = 'pillow', filename = 'TwoBodyAnimC.png',fps = 25)

#.avi   .mov