dolphin = imread('dolphin.png');
bicycle = imread('bicycle.png');

imshow((bicycle - dolphin) + (dolphin - bicycle))
