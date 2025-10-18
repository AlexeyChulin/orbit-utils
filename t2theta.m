function [theta, cos_theta, sin_theta] = t2theta(t, t_pi, e, n)
    % Вычисление истинной аномалии по времени
    % Вход:
    % t - текущее время, с
    % t_pi - время прохождения через перицентр, с
    % e - эксцентриситет
    % n - среднее движение, рад/с
    % Выход:
    % theta - истинная аномалия, рад
    dt = t - t_pi;
    M = n*dt;
    while M >= 2 * pi
        M = M - 2 * pi;
    end
    while M < 0
        M = M + 2 * pi;
    end
    E = M;
    theta = e2theta(e, E);
    while 1
        Eprev = E;
        E = M + e * sin(E);
        theta_prev = theta;
        theta = e2theta(e, E);
        if abs(theta - theta_prev) <= 1e-5
            break
        end
    end
    cos_theta = cos(theta);
    sin_theta = sin(theta);
endfunction
