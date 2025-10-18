function [r, v] = elem2vec(OMG, i, omg, p, e, theta)
  % Вычисление вектора состояния по элементам орбиты и истинной аномалии
  % Вход:
  % OMG - долгота восходящего узла, рад
  % i - наклон орбиты, рад
  % omg - аргумент перицентра, рад
  % p - фокальный параметр, км
  % e - эксцентриситет
  % theta - истинная аномалия, рад
  % Выход
  % r - радиус-вектор, км
  % v - вектор скорости, км/с
  u = omg + theta; % Аргумент широты
  norm_r = p / (1 + e * cos(theta)); % модуль радиус-вектора
  root = sqrt(c_mju_e / p); 
  v_r = root * e * sin(theta); % радиальная проекция скорости
  v_n = root * (1 + e * cos(theta)); % трансверсальная проекция скорости
  e_r = [cos(u)*cos(OMG) - sin(u)*sin(OMG)*cos(i);
         cos(u)*sin(OMG) + sin(u)*cos(OMG)*cos(i);
         sin(u)*sin(i)]; % орт радиали
  e_n = [-sin(u)*cos(OMG) - cos(u)*sin(OMG)*cos(i);
         -sin(u)*sin(OMG) - cos(u)*cos(OMG)*cos(i);
         cos(u)*sin(i)]; % орт трансверсали
  r = norm_r * e_r; % радиус-вектор
  v = v_r * e_r + v_n * e_n; % вектор скорости
endfunction
