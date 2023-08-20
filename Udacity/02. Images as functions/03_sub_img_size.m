% Crop an image
img = imread('bicycle.png');
imshow(img);

disp(size(img));  % check size

cropped = img(110:310, 10:160);
imshow(cropped);

% TODO: Find out cropped image size
disp(310-110+1)
disp(160-10+1)