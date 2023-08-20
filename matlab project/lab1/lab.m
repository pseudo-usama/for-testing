h = input('Initial height of water (ft.) = ');

inch_to_feet_constent = 0.083;

rt = 2;
ro = 0.3 * inch_to_feet_constent;
g = 32.2;

vavg = 0.5 * sqrt(2 * g * h);
time = ((rt / ro)^2) * (h / vavg);

time = time / 3600;

fprintf('The time to drain the tank is %.2f hours\n', time)
