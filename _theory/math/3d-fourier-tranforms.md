---
layout: theory_page
title: Ряды Фурье в трёхмерном пространстве
permalink: /math/3d-fourier-tranforms/
previous_page: /theory/
next_page: /theory/
---

$$
u(\vec{r}) = u(\vec{r} + n \vec{a} + m \vec{b} + k \vec{c}),
$$

$n, m, k$ - произвольные целые числа;
$\vec{a}, \vec{b}, \vec{c}$ - заданные векторы, такие что тройка $\vec{a}, \vec{b}, \vec{c}$ - правая, то есть:

$$
V = (\vec{a}, \vec{b}, \vec{c}) > 0.
$$

Введём новые координаты:

$$
\vec{r} = x_1 \vec{a} + x_2 \vec{b} + x_3 \vec{c}.
$$

Тогда:

$$
u(x_1, x_2, x_3) = u(x_1 \vec{a} + x_2 \vec{b} + x_3 \vec{c}) = u(x_1 + n, x_2 + m, x_3 + k).
$$

Перед нами периодическая функция. Раскладываем её в ряд Фурье:

$$
u(x_1, x_2, x_3) = \sum\limits_{-\infty \\ n,m,k}^\infty U_{nmk} \exp (2\pi i [n x_1 + m x_2 + k x_3])
$$

Найдём $x_1, x_2, x_3$. Введём вспомогательный базис:

$$
\vec{e}_1 = \frac{\vec{b}\times\vec{c}}{V}, \qquad 
\vec{e}_2 = \frac{\vec{c}\times\vec{a}}{V}, \qquad 
\vec{e}_1 = \frac{\vec{a}\times\vec{b}}{V},
$$

$$
x_1 = \vec{e}_1\cdot\vec{r}, \qquad
x_2 = \vec{e}_2\cdot\vec{r}, \qquad
x_3 = \vec{e}_3\cdot\vec{r}.
$$

Окончательно:

$$
u(\vec{r}) = \sum\limits_{-\infty}^{\infty} U_{nmk} \exp \left(2\pi i [n\vec{e}_1 + m\vec{e}_2 + k\vec{e}_3]\cdot\vec{r}\right).
$$

Введём обозначение:

$$
\vec{K} = 2\pi[n\vec{e}_1 + m\vec{e}_2 + k\vec{e}_3],
$$

$$
u(\vec{r}) = \sum\limits_{\vec{K}} U_\vec{K} \exp (i\vec{K}\cdot\vec{r}),
$$

$$
U_\vec{K} = U_{nmk} = \int\limits_0^1 \int\limits_0^1 \int\limits_0^1 u(x_1, x_2, x_3) \exp \left(-2\pi i [n x_1 + m x_2 + k x_3]\right) dx_1 dx_2 dx_3 = 
$$

$$
= \int\limits_V u(\vec{r}) \exp(-i \vec{K}\cdot\vec{r})) J dV = \\
$$

$$
= \left[J - \text{якобиан, }J = \frac{\partial(x_1, x_2, x_3)}{\partial(x, y, z)} = \frac{1}{V}\right] =
$$

$$
= \frac{1}{V} \int\limits_V u(\vec{r}) \exp(-i \vec{K}\cdot\vec{r})) dV
$$

Окончательно для трехмерных преобразований Фурье имеем:

$$
\begin{aligned}
& \vec{e}_1 = \frac{\vec{b}\times\vec{c}}{V}, \qquad 
\vec{e}_2 = \frac{\vec{c}\times\vec{a}}{V}, \qquad 
\vec{e}_1 = \frac{\vec{a}\times\vec{b}}{V}, \\
& \vec{K} = 2\pi[n\vec{e}_1 + m\vec{e}_2 + k\vec{e}_3], \\
& u(\vec{r}) = \sum\limits_{\vec{K}} U_\vec{K} \exp (i\vec{K}\cdot\vec{r}), \\
& U_\vec{K} = \frac{1}{V} \int\limits_V u(\vec{r}) \exp(-i \vec{K}\cdot\vec{r})) dV
\end{aligned}
$$

Получим ещё одно соотношение:

$$
u(\vec{r}) = \sum\limits_{\vec{K}} \frac{1}{V} \int\limits_V u(\vec{r}') \exp(-i \vec{K}\cdot\vec{r}')) dV' \exp (i\vec{K}\cdot\vec{r}) = 
$$

$$
= \int\limits_V u(\vec{r}') \left[\frac{1}{V} \sum\limits_{\vec{K}} \exp (i\vec{K}\cdot (\vec{r} - \vec{r}'))\right] dV'
$$

$$
\sum\limits_{n,m,k} \delta(\vec{r} - \vec{r}' - n \vec{a} - m \vec{b} - k \vec{c}) = \left[\frac{1}{V} \sum\limits_{\vec{K}} \exp (i\vec{K}\cdot (\vec{r} - \vec{r}'))\right]
$$
