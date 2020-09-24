---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

title: Потенциальные ямы
layout: theory_page
permalink: /potential_pits/
---

Здесь мы будем решать стационарное уравнение Шрёдингера для одной частицы с данным потенциалом:

$$
\Delta \psi + \frac{2m}{\hbar^2} (E - U(\vec{r})) \psi = 0
$$

## Одномерная прямоугольная потенцальная яма с бесконечно высокими стенками

Уравнение принимает вид:

$$
\frac{d^2\psi}{dx^2} + \frac{2m E}{\hbar^2} \psi = 0, \qquad x = (0, l), \psi(0) = 0, \psi(l) = 0
$$

Очевидное решение:

$$
\psi = A \sin (kx)
$$

$$
k^2 = \frac{2mE}{\hbar^2}
$$

$$
kl = \pi n, \qquad n = 1, 2, 3, \ldots
$$

В результате:

1. Спектр дискретный и бесконечный:

$$
E_n = \frac{\pi^2 \hbar^2 n^2}{2m l^2}
$$

2. Волновые функции - суперпозиция двух волн де Бройля:

$$
\psi_n = \sqrt{\dfrac{2}{l}} \sin \left(\dfrac{\pi n x}{l}\right)
$$

<div style="text-align:center"><img src="/problems/potential_pits_img_001.png" /></div>

## Трёхмерная прямоугольная потенцальная яма с бесконечно высокими стенками

Теперь нам дан ящик со сторонами $l_x, l_y, l_z$. Сквозь грани частица также пройти не может. Найдём спектр для данного случая. Очевидно, что задача разрешима методом Фурье (разделения переменных):

$$
\psi_{n_x, n_y, n_z} (x, y, z) = \sqrt{\dfrac{8}{l_x l_y l_z}} 
\sin \left(\dfrac{\pi n_x x}{l_x}\right)
\sin \left(\dfrac{\pi n_y y}{l_y}\right)
\sin \left(\dfrac{\pi n_z z}{l_z}\right)
$$

$$
E_{n_x, n_y, n_z} = \frac{\pi^2 \hbar^2}{2m} \left(\dfrac{n_x^2}{l_x^2} + \dfrac{n_y^2}{l_y^2} + \dfrac{n_z^2}{l_z^2}\right)
$$

При этом хотя бы одно из чисел $n_x, n_y, n_z$ должно быть отлично от нуля.

## Сферическая потенциальная яма с бесконечно высокими стенками

Пусть задана сфера радиуса $a$ за пределами которой потенциальная энергия бесконечна. Частица через потенциальный барьер проникнуть не может. Уравнение Шрёдингера:

$$
\frac{1}{r^2} \frac{\partial}{\partial r} \left(r^2 \frac{\partial \psi}{\partial r}\right) + 
\frac{1}{r^2 \sin \theta} \frac{\partial}{\partial \theta} \left(\sin \theta \frac{\partial \psi}{\partial \theta}\right) +
\frac{1}{r^2 \sin^2 \theta} \frac{\partial^2 \psi}{\partial \alpha^2} + \frac{2mE}{\hbar^2} \psi = 0
$$

Соответственно решение можно представить в виде:

$$
\psi = R(r) Y_l^m(\theta, \alpha)
$$

$l, m$ - соответственно орбитальное и магнитное квантовые числа. Найдём уравнение для $R(r)$, учитывая, что:

$$
\frac{1}{\sin \theta} \frac{\partial}{\partial \theta} \left(\sin \theta \frac{\partial Y_l^m}{\partial \theta}\right) +
\frac{1}{\sin^2 \theta} \frac{\partial^2 Y_l^m}{\partial \alpha^2}
=
- l(l + 1) Y_l^m
$$

Тогда:

$$
\frac{1}{r^2} \frac{d}{d r} \left(r^2 \frac{d R}{d r}\right) -
\frac{l(l+1)}{r^2} R + \frac{2mE}{\hbar^2} R = 0
$$

Раскрываем первое слагаемое, умножаем на $r^2$:

$$
r^2 \frac{d^2 R}{d r^2} + 2 r \frac{d R}{d r} +
\left(\frac{2mE}{\hbar^2} r^2 - l(l + 1)\right) R = 0
$$

Видно, что задача легко масштабируется:

$$
x = \sqrt{\frac{2mE}{\hbar^2}} r
$$

$$
x^2 \frac{d^2 R}{d x^2} + 2 x \frac{d R}{d x} +
\left(x^2 - l(l + 1)\right) R = 0
$$
