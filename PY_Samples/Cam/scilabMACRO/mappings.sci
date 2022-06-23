// auto scaling with previous plots + style
//clf();
//clc(); // clear console window
//clear; // kills variables
//xdel(0); // delete the first graphic
//x=[-100:1:100];  // start step end 
//----------------------------------------------------
getd('scilabMACRO')
// https://en.wikipedia.org/wiki/Rotation_matrix
function [yi] = TRANSFORMATION_MATRIX(anglei,scalei,xi)

Cx11=cos(angel(1)/2/%pi)
Cx11=-sin(angel(1)/2/%pi)
Cx11=cos(angel(1)/2/%pi)
Cx11=sin(angel(1)/2/%pi)

Cy11=cos(angel(2)/2/%pi)
Cy11=-sin(angel(2)/2/%pi)
Cy11=cos(angel(2)/2/%pi)
Cy11=sin(angel(2)/2/%pi)

Cz11=cos(angel(3)/2/%pi)
Cz11=-sin(angel(3)/2/%pi)
Cz11=cos(angel(3)/2/%pi)
Cz11=sin(angel(3)/2/%pi)

a=1.2
b=0
c=0
d=1.2
T=[a,b;c,d]

yi=T*xi
    
endfunction

//---------------------------------------------------
scalei = [1,0,1,0];
anglei = [0,0,0];   // thetaX  thetaY  thetaZ   DEGrees
//---------------------------------------------------
//We can use the linspace function in order to produce 50 values in the interval [1,10].

Yplane = [0,400,400,0];
Xplane = [0,0,400,400];

Yframe = [0,100,100,0,60] +200;
Xframe = [0,0,100,100,50] +200;



Yplane_camera = Yplane*2;
Xplane_camera = Xplane*2;

Yframe_camera = Yframe *2;
Xframe_camera = Xframe *2;

XY_frame=[1;0] * Xframe +[0;1]*Yframe;

// Yframe_camera=TRANSFORMATION_MATRIX(Yframe)
// Yframe_camera=TRANSFORMATION_MATRIX(Yframe)


disp('=====PHYSICAL PLANE===========')


f = scf(0); // Create a new figure or select an existing figure with an id of 0.
    subplot(1,3,1) // 1 row 1 column
    
    scatter(Xframe,Yframe); 
    scatter(Xplane,Yplane);   title("PHYSICAL PLANE mm") ;

disp('=====CAMERA PLANE===========')

f = scf(0); // Create a new figure or select an existing figure with an id of 0.
    subplot(1,3,2) // 1 row 1 column
    
    scatter(Xframe_camera,Yframe_camera); 
    scatter(Xplane_camera,Yplane_camera);   title("CAMERA PLANE pixel") ;    

disp('=====TRANSFORMATION 1===========')    
    
    subplot(1,3,3) // 1 row 2 column
    
    
    
    scatter(Xplane,Yplane); 
    scatter(Xframe,Yframe);    title("MONITOR pixel") ;
    
    XY_frame_transformed=zeros(2,1)
    
 disp('=====TRANSFORMATION x===========')   
    [row,column]=size(XY_frame)
    for i =1 : column
        xi= XY_frame(:,i)
        
        disp(XY_frame(:,i));
        
        yi=TRANSFORMATION_MATRIX(anglei,scalei,xi)
        disp(yi);
        XY_frame_transformed=[XY_frame_transformed, [yi]]  // d=[d;[ 8 9 10]] new row  d=[2 3 4; 5 6 7]
    end
    
    scatter(XY_frame_transformed(1,:),XY_frame_transformed(2,:), , "orange"); 
    tit = "scatter(x, y, ,""orange"")";
    title(tit, "fontsize",3)
    
    xs2jpg(0, 'transformation.jpg'); // Export to a JPG file

//====================================================================================

//====================================================================================













