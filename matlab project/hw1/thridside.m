b = input('Enter the first side: ');
c = input('Enter the second side: ');
beta = input('Enter the angle between them in degrees: ');

a = sqrt(b^2 + c^2 - 2*b*c*cosd(beta));

fprintf('\nThe third side is %.3f\n', a)