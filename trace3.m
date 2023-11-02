% trace3.m
% Построение трассы КА на геосинхронной орбите
T = 86400;
e = 0;
n = 2*pi/T;
lambda0 = 0;
i = 63/180*pi;
we = 2*pi*(1/86400);
Nmax = 9000;
t = zeros(1,Nmax);
u = zeros(1,Nmax);
for N = 1:Nmax
    t(N) = T/1800*N;
    u(N) = n*t(N);
    while(u(N) > 2*pi)
        u(N) = u(N) - 2*pi;
    end
    d_lambda = atan(cos(i)*tan(u(N)));
    if(u(N) > pi/2) & (u(N) <= 3*pi/2)
        d_lambda = d_lambda + pi;
    elseif(u(N) > 3*pi/2) 
        d_lambda = d_lambda + 2*pi;
    end
    lambda(N) = lambda0 + d_lambda - we*t(N);
    while (lambda(N) < -pi)
        lambda(N) = lambda(N) + 2*pi;
    end
    while (lambda(N) > pi)
        lambda(N) = lambda(N) - 2*pi;
    end
    phi(N) = asin(sin(i)*sin(u(N)));
end
close all
subplot(311)
plot(t,lambda)
grid
subplot(312)
plot(t,phi)
grid
subplot(313)
plot(t,u)
grid
figure
plot(lambda)
grid
figure
plot(lambda, phi, 'b')
grid