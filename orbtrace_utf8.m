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
E0 = theta2e(nju0, e);
t_pi = -(E0 - e*sin(E0))/n;

for N = 1:Nmax
  fprintf("Шаг %d\n", N);
	t(N) = (N - 0.5)*T/3600;
	%t(N) = (N - 1)*T/3600;
	[nju(N), cnju, snju] = t2theta(t(N), t_pi, e, n);
	if nju(N) < 0
	    nju(N) = nju(N) + 2*pi;
	end
    u(N) = nju(N) + omg; % аргумент широты
    [r, v] = elem2vec(0, i, omg, p, e, nju(N));
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
ylabel("\lambda, рад")
grid
subplot(312)
plot(t,phi)
ylabel("\phi, рад")
grid
subplot(313)
plot(t,nju)
ylabel("\theta, рад")
xlabel('t, c')
grid
figure
plot(lambda,phi)
ylabel("\phi, рад")
xlabel('\lambda, рад')
grid
% Animation
figure
h = plot(NaN,NaN); %// initiallize plot. Get a handle to graphic object
axis([min(lambda) max(lambda) min(phi) max(phi)]); %// freeze axes
grid
%// to their final size, to prevent Matlab from rescaling them dynamically 
for ii = 1:length(lambda)
    pause(0.01)
    set(h, 'XData', lambda(1:ii), 'YData', phi(1:ii));
    drawnow %// you can probably remove this line, as pause already calls drawnow
end