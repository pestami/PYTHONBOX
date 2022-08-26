
TF2 = all(A(:,2:5)==0,2) & A(:,6) ~= 0 
TF6 = A(:,2) == 0 & A(:,3) A ~= 0 
% combine them
TFall = TF1 & TF2 & TF6
% remove
A(TFall,:) = []
