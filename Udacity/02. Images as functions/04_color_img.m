% Color planes
img = imread('fruit.png');
imshow(img);

disp(size(img));

% TODO: Select a color plane, display it, inspect values from a row
g = img(:,:,2);
imshow(g);
plot(g(100, :));