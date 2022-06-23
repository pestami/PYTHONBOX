// auto scaling with previous plots + style
clf();

T0=0        // x m
T1=100   // y m
DT= 5

T=2  // Wave Length m


//print('file-name',x1,[x2,...xn])
disp('=====PAREMETRIC 3D===========')
disp('Hello World')

//print(%io(1),T0,T1,DT)

t=[T0:T1:DT]';
z=sin(2*%pi*t/T)*cos(2*%pi*t/T);

disp('=============================')

plot3d(t,t,z)
