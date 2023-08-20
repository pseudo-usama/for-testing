disp('Time to Drain Water Tank')
disp('h       vavg    time')

for i=1:10
  vals = calc_time(i);
  fprintf('%d\t%.2f\t%.2f\n', i, vals(1), vals(2))
end

function output = calc_time(h)
  inch_to_feet_constent = 0.083;

  rt = 2;
  ro = 0.3 * inch_to_feet_constent;
  g = 32.2;

  vavg = 0.5 * sqrt(2 * g * h);
  time = ((rt / ro)^2) * (h / vavg);

  time = time / 3600;

  output = [vavg, time];
end
