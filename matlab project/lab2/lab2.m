a = input('Enter quadratic equation coefficient a: ');
b = input('Enter quadratic equation coefficient b: ');
c = input('Enter quadratic equation coefficient c: ');

disc = b^2 - 4*a*c;

if disc > 0
  disp('Two real roots exist.')
elseif disc == 0
  disp('Double equal root exists.')
else
  disp('Two complex conjugate roots exist.')
end

disp('Two roots are:')
x1 = (-b + sqrt(disc)) / (2*a)
x2 = (-b - sqrt(disc)) / (2*a)
