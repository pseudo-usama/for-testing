function vals = cylinder(r, h)
  volumn = pi * (r^2) * h;
  area = 2 * pi * r * (r + h);
  
  vals = [volumn, area];
end
