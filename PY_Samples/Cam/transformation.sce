// auto scaling with previous plots + style
//clf();
//clc(); // clear console window
//clear; // kills variables
//xdel(0); // delete the first graphic
//x=[-100:1:100];  // start step end 
//----------------------------------------------------
//getd('scilabMACRO')
// https://en.wikipedia.org/wiki/Rotation_matrix
function [yi] = TRANSFORMATION_MATRIX(anglei,scalei,xi)
    
    //scalei = [1,0,0,1];
    //anglei = [0,0,0];   // thetaX  thetaY  thetaZ   DEGrees

// XY plane Z rotation
Cx11=cos(anglei(1)/180*%pi)
Cx12=-sin(anglei(1)/180*%pi)
Cx21=sin(anglei(1)/180*%pi)
Cx22=cos(anglei(1)/180*%pi)

Cy11=cos(anglei(2)/180*%pi)
Cy12=-sin(anglei(2)/180*%pi)
Cy21=sin(anglei(2)/180*%pi)
Cy22=cos(anglei(2)/180*%pi)

Cz11=cos(anglei(3)/180*%pi)
Cz12=-sin(anglei(3)/180*%pi)
Cz21=sin(anglei(3)/180*%pi)
Cz22=cos(anglei(3)/180*%pi)

Rxy=[Cz11,Cz12;Cz21,Cz22]  //
Rxz=[Cy11,Cy12;Cy21,Cy22]
Rzy=[Cx11,Cx12;Cx21,Cx22]
        //disp('Rxy:',Rxy);
a=scalei(1)
b=scalei(2)
c=scalei(3)
d=scalei(4)
T=[a,b;c,d]
disp('Txy:',T);
// Scaling and Sheer
//yi=T*xi
// Rot in XY
yi=Rxy*xi   //pertrans(yi)
// Rot in YZ
yi=Rxz*yi 
// Rot in XZ
yi=Rzy*yi 
endfunction

//---------------------------------------------------
scalei = [1,0,0,1]; //  [[a b] [C d]]
anglei = [0,60,0];   // thetaX  thetaY  thetaZ   DEGrees
//---------------------------------------------------
//We can use the linspace function in order to produce 50 values in the interval [1,10].
Xplane = [0,0,400,400] -200;
Yplane = [0,400,400,0] -200;

Xframe = [0,0,100,100,0,50] +0;
Yframe = [0,100,100,0,0,60] +0;  // frame is metal fixing plate
Zframe = [0,0,0,0,0,0] +0; 

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
    scatter(Xplane,Yplane);   title("PHYSICAL PLANE xy mm") ;

disp('=====CAMERA PLANE===========')

f = scf(0); // Create a new figure or select an existing figure with an id of 0.
    subplot(1,3,2) // 1 row 1 column
    
    scatter(Xframe_camera,Yframe_camera); 
    scatter(Xplane_camera,Yplane_camera);   title("CAMERA PLANE pixel") ;    

disp('=====TRANSFORMATION 1===========')    
    
    subplot(1,3,3) // 1 row 2 column
       
    //scatter(Xplane,Yplane); 
    //scatter(Xframe,Yframe);    title("MONITOR pixel") ;
    
    XY_frame_transformed=zeros(2,1)
    
 disp('=====TRANSFORMATION x===========')   
    [row,column]=size(XY_frame)
    for i =1 : column
        xi= XY_frame(:,i)
        
        disp('P :',XY_frame(:,i));
        
        yi=TRANSFORMATION_MATRIX(anglei,scalei,xi)
        disp('P Transformed:',yi);
        XY_frame_transformed=[XY_frame_transformed, [yi]]  // d=[d;[ 8 9 10]] new row  d=[2 3 4; 5 6 7]
    end
    scatter([-50,150],[-10,150], , "black"); 
    scatter(XY_frame_transformed(1,:),XY_frame_transformed(2,:), , "blue"); 
    plot2d(XY_frame_transformed(1,:),XY_frame_transformed(2,:)); 
    tit = "scatter(x, y, ,""orange"")";
    title(tit, "fontsize",3)
    
    xs2jpg(0, 'transformation.jpg'); // Export to a JPG file
    
disp('=====PROGRAM COMPLETED===========')  
//====================================================================================

//====================================================================================













