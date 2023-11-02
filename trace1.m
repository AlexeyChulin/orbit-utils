% trace1.m
% Построение трассы низкоорбитального КА с наклонением орбиты < 90 град
a = 7200;
e = 0;
n = sqrt(c_mju_e/a^3);
T = 2*pi/n;
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
    if (lambda(N) < 0)
        lambda(N) = lambda(N) + 2*pi;
    elseif (lambda(N) > 2*pi)
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
lambda1 = zeros(4,3000);
for k = 1:4
    if k==1
        N1(k) = 1500;
    else
        N1(k) = N1(k-1) + 1500;
    end
    while lambda(N1(k)) > lambda(N1(k)-1)
        N1(k) = N1(k)+1;
    end
end
figure
plot(lambda(1:(N1(1)-1)), phi(1:(N1(1)-1)), 'b', lambda(N1(1):N1(2)-1), phi(N1(1):N1(2)-1), 'b',...
     lambda(N1(2):N1(3)-1), phi(N1(2):N1(3)-1), 'b', lambda(N1(3):N1(4)-1), phi(N1(3):N1(4)-1), 'b')
grid