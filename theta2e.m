function E = theta2e(theta, e)
    % Пересчет истинной аномалии в эксцентрическую
    % Вход:
    % theta - истинная аномалия, рад
    % e - эксцентриситет
    % Выход:
    % E - эксцентрическая аномалия
    if abs(theta - pi) < 1e-7
        E = pi;
    elseif abs(theta + pi) < 1e-7
        E = -pi;
    else
        E = 2*atan(sqrt((1 - e) / (1 + e)) * tan(theta / 2));
    end
    if E < 0
        E = E + 2 * pi;
    end
endfunction
