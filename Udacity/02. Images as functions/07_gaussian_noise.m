% Generate Gaussian noise
noise = randn([1 100000]);
[n x] = hist(noise, linspace(-3, 3, 21));
%disp([x; n]);
%plot(x, n);

% TODO: Try generating other kinds of random numbers.
%       How about a 2D grid of random Gaussian values?

noise = rand([1 1000000]);
[n x] = hist(noise, linspace(-1, 2, 200));
%plot(x, n);

noise = randi([1 1000000]);
[n x] = hist(noise, linspace(-10, 10, 1000));
plot(x, n);