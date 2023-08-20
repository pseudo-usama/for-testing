function vals = sphere(r)
  volumn = (4/3) * pi * (r^3);
  area = 4 * pi * (r^2);
  
  vals = [volumn, area];
end
