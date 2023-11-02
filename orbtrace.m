function orbtrace(lambda0, i, omg, a, e, Nvit)
% Построение трассы КА 
% Вход:
% lambda0 - начальная географическая долгота восходящего узла, рад
% i - наклонение, рад
% a - большая полуось, км
% e - эксцентриситет
% Nvit - число витков
%
% Начало отсчета от восходящего узла
we = 2*pi*(1/86400);
n = sqrt(c_mju_e/a^3);
T = 2*pi/n;
p = a*(1-e^2); 
Nmax = Nvit*3600 - 1;
t = zeros(1,Nmax);
u = zeros(1,Nmax);
% Расчет времени перигея (так, чтобы начальное время совпало с восходящим узлом)
nju0 = 2*pi - omg;
E0 = nju2e(nju0,e);
t_pi = -(E0 - e*sin(E0))/n;

for N = 1:Nmax
	t(N) = (N - 0.5)*T/3600;
	%t(N) = (N - 1)*T/3600;
	[nju(N),cnju,snju] = t2nju(t(N),t_pi,e,n);
	if nju(N) < 0
	    nju(N) = nju(N) + 2*pi;
	end
    u(N) = nju(N) + omg; % аргумент широты
    [r,v] = elm2vec(i, p, e, 0, omg, nju(N));
    phi(N) = asin(sin(i)*sin(u(N)));
    d_lambda = atan2(r(2), r(1));
    lambda(N) = lambda0 + d_lambda - we*t(N);
    if (lambda(N) < 0)
        lambda(N) = lambda(N) + 2*pi;
    elseif (lambda(N) > 2*pi)
        lambda(N) = lambda(N) - 2*pi;
    end
end
close all

figure
subplot(311)
plot(t,lambda)
grid
subplot(312)
plot(t,phi)
grid
subplot(313)
plot(t,nju)
grid
figure
plot(lambda,phi)
grid
