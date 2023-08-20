calc_len = @(b) 4 * sqrt((1/2)^2 + (1/2-b/2)^2) + b;

for i=0:0.001:1
  len = calc_len(i);
  fprintf('%.2f\t%d\n', i, len);
end
