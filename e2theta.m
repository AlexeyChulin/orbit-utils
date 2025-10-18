function theta = e2theta(e, E)
    % Пересчет эксцентрической аномалии в истинную
    % Вход:
    % E - эксцентрическая аномалия, рад
    % e - эксцентриситет
    % Выход:
    % theta - истинная аномалия, рад
    while E >= 2 * pi
        E = E - 2 * pi;
    end
    while E < 0
        E = E + 2 * pi;
    end
    if abs(E - pi) < 1e-7
        theta = pi;
    elseif abs(E + pi) < 1e-7
        theta = -pi;
    else
        theta = 2 * atan(sqrt((1 + e)/(1 - e)) * tan(E / 2));
    end
    if theta < 0
        theta = theta + 2 * pi;
    end
endfunction
