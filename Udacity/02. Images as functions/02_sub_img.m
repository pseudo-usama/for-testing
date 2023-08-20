% Inspect image values
img = imread('dolphin.png');
imshow(img);
disp(size(img));

% TODO: Extract a 2D slice between rows 101 to 103 and columns 201 to 203 (inclusive)
disp(img(101:103, 201:203))