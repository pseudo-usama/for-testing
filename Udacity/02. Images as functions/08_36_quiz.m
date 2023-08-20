img = im2double(imread('dolphin.png'));

sigma = 0.3;
noise = randn(size(img)) .* sigma;
img = img + noise;

%imshow(img);
subplot(1, 2, 1); imshow(img+noise);
subplot(1, 2, 2); imshow(noise+img);
