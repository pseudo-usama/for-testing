% Apply a Gaussian filter to remove noise
img = imread('saturn.png');
imshow(img);

img = im2double(img);

% TODO: Add noise to the image
noise = randn(size(img)) .* 0.06;
noised_img = img + noise;

% TODO: Now apply a Gaussian filter to smooth out the noise
% Note: You may need to pkg load image;
filter = fspecial('gaussian', size(img), 2.5);
filtered_img = imfilter(noised_img, filter);

imshow(filtered_img);
