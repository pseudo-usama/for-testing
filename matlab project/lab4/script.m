disp('For Cylinder')
fprintf('Radius  Height  Volume  Area\n')

for r=0.5:0.02:1
  h = 1 / (r^2);
  vals = cylinder(r, h);
  fprintf('%.4f\t%.4f\t%.4f\t%.4f\n', r, h, vals(1), vals(2));
end

fprintf('\n\n')
disp('For Sphere')
r = (3/4)^(1/3)
vals = sphere(r);
fprintf('Volumn : %.4f\nArea   : %.4f\n', vals(1), vals(2));

fprintf('\n\n')
fprintf('Cylinder has a area of 11.8752 when radius is 0.8000\nCompared to 10.3733 area of Sphere.\nSo Sphere always has minimum area\n');