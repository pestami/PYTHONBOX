// auto scaling with previous plots + style
//clf();
//clc(); // clear console window
//clear; // kills variables
//xdel(0); // delete the first graphic
//x=[-100:1:100];  // start step end 
//----------------------------------------------------
function [yi] = MyBead(xi)
a=1;
b=10;

    //y=(a*x) * (2.17^(-x))

    //yi=(a*xi) .* (exp(-xi/b))
     yi=100-(a*xi) 
    
endfunction
//---------------------------------------------------
function [yi] = MySin(xi)

     yi=50*sin(1/1*xi*3.1415/100) 
    
endfunction
//---------------------------------------------------
//We can use the linspace function in order to produce 50 values in the interval [1,10].

//xdata = linspace ( 0 , 10 , 5 );
//xdata1 = [0,1,2,3,4,5,6,7,8,9,10];
res=1
xdata1=[0:res:100]; 
ydata1=[100:-res:0]; 

//ydata = MyQuadratic (xdata);
disp('=====MyDECAY===========')
ydata2 = MyBead (xdata1);
ydata3 = MySin(xdata1);
ydata4 = ydata2 -  ydata3;
//ydata = MyQuadratic (xdata);
//---------------------------------------------------
//print('file-name',x1,[x2,...xn])

//disp(xdata)
//gda().grid = [5 5]*color("grey70");
//title(gda(), "fontsize", 3, "color", "lightseagreen", "fontname", "helvetica bold");

//====================================================================================

f = scf(0); // Create a new figure or select an existing figure with an id of 0.
    subplot(1,2,1) // 1 row 1 column
    plot(xdata1,ydata2,"g");   
    plot(xdata1,ydata3,"b");   title("Paths in meter") ;
    subplot(1,2,2) // 1 row 2 column
    plot(xdata1,ydata4,"r");   title("Path y1 + y2") ;

    xs2jpg(0, 'BeadPath.jpg'); // Export to a JPG file

//====================================================================================

Node_X=xdata1
Node_Y=ydata4

DS= [1:100]
// elements , points = n then elements = n-1
nodes=100
elements=nodes-1

ELEMENT_nr=[1:elements] // Interval
ELEMENT_E=[1:elements]
ELEMENT_V=[1:elements]
ELEMENT_DE=[1:elements]
ELEMENT_DS=[1:elements] 
ELEMENT_DY=[1:elements] 
ELEMENT_DE(1)=0 
ELEMENT_V(1)=0 

ELEMENT_T=[1:elements] 

Nodes=100
Elements=Nodes -1

ELEMENT_V_start=[1:elements] 
ELEMENT_V_end=[1:elements] 
ELEMENT_V_start(1)=0

ELEMENT_Estart=[1:elements]
ELEMENT_Eend=[1:elements]

for i = 1:Elements  // Intervals , points = n then intervals = n-1
    ELEMENT_nr(i)=i
    ELEMENT_DS(i) = sqrt((Node_X(i)-Node_X(i+1))^2+(Node_Y(i)-Node_Y(i+1))^2)
    ELEMENT_DY(i) = Node_Y(i)-Node_Y(i+1)    
    
    if i== 1 then
        ELEMENT_V_start(i)=0;
    else
        ELEMENT_V_start(i)=ELEMENT_V_end(i-1);
    end  
    
    ELEMENT_Estart(i)= 1/2 * (ELEMENT_V_start(i))^2  // 1/2
    ELEMENT_Eend(i)=(ELEMENT_DY(i))*9.81 + ELEMENT_Estart(i)
    ELEMENT_V_end(i)=sqrt(2*ELEMENT_Eend(i))
    
    
    if i== 1 then
        ELEMENT_T(i)=0 + ELEMENT_DS(i) /(ELEMENT_V_end(i)/2+ELEMENT_V_start(i)/2)
    else
        ELEMENT_T(i)=ELEMENT_T(i-1) + ELEMENT_DS(i) /(ELEMENT_V_end(i)/2+ELEMENT_V_start(i)/2)
    end  
end



//subplot(1,3,3) // 1 row 3 column

// plot(ELEMENT_nr,ELEMENT_V_end,"b");
//====================================================================================
f = scf(1); // Create a new figure or select an existing figure with an id of 0.
    plot(ELEMENT_nr,ELEMENT_T,"b");  title("Time Taken (seconds)") ;
    
    xs2jpg(1, 'BeadTime.jpg'); // Export to a JPG file

    //gcf(1).children.grid = color("grey70")*[1 1]; // grids
    //xs2jpg(1, 'BeadTime.jpg'); // Export to a JPG file

//====================================================================================













