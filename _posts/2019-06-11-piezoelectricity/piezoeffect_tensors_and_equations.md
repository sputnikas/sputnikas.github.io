---
layout: page
title: Уравнения пьезоэффекта в тензорной форме
---

Начнём с общих уравнений:

$$
\begin{aligned}
& \begin{cases}
\hat{u} = s^E \hat{\sigma} + d^t \vec{E}, \\
\vec{D} = d \hat{\sigma} + \varepsilon^\sigma \vec{E},
\end{cases}
&& \begin{cases}
\hat{\sigma} = c^E \hat{u} - e^t \vec{E}, \\
\vec{D} = e \hat{u} + \varepsilon^u \vec{E},
\end{cases}
\\ &
\begin{cases}
\hat{u} = s^D \hat{\sigma} + g^t \vec{D}, \\
\vec{E} = - g \hat{\sigma} + \beta^\sigma \vec{D},
\end{cases}
&& \begin{cases}
\hat{\sigma} = c^D \hat{u} - h^t \vec{D}, \\
\vec{E} = - h \hat{u} + \beta^u \vec{D}.
\end{cases}
\end{aligned}
$$

Здесь $\hat{\sigma}$ - механическое напряжение, $\hat{u}$ - тензор деформаций - симметричные тензоры 2 ранга, $s^E$, $c^E$, $s^D$, $c^D$ - тензоры 4 ранга, $e$, $h$, $g$ $d$ - тензоры 3 ранга. Симметрия позвоялет представить данные уравнения через 6-векторы.

$$
\hat{\sigma} = \begin{pmatrix}
\sigma_{11} \\
\sigma_{22} \\
\sigma_{33} \\
\sigma_{23} \\
\sigma_{13} \\
\sigma_{12}
\end{pmatrix}, \qquad
\hat{u} = \begin{pmatrix}
u_{11} \\
u_{22} \\
u_{33} \\
u_{23} \\
u_{13} \\
u_{12}
\end{pmatrix}.
$$

Вводят следующие индексы:

|11|22|33|23|32|13|31|12|21|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|2|3|4|4|5|5|6|6|

В такой индексации при направлении оси поляризации пьезокристалла 3, ненулевыми будут только компоненты матриц:

$$
\begin{aligned} &
\begin{pmatrix}
11 & 12 & 13 & & & \\
21 = 12 & 22 = 11 & 23 = 13 & & & \\
31 = 13 & 32 = 13 & 33 & & & \\
& & & 44 & & \\
& & & & 55 = 44 & \\
& & & & & 66 
\end{pmatrix}^{\begin{aligned}s^{E,D} \\ c^{E,D}\end{aligned}}
&& \begin{pmatrix}
& & 13 = 31 \\
& & 23 = 31 \\
& & 33 \\
& 42 = 15 & \\
51 = 15 & & \\
& & 
\end{pmatrix}^{\begin{aligned}d^t \\ g^t \\ e^t \\ h^t \end{aligned}}
\\ &
\begin{pmatrix}
& & & & 15\quad & \quad \\
& & & 24 = 15 & &\\
\quad 31\quad & 32 = 31 & \quad 33 \quad  & & & \\
\end{pmatrix}
&& \begin{pmatrix}
\quad\,\, 11 \quad & & \\
& 22 = 11& \\
& & \quad\, 33\quad  \\
\end{pmatrix}^{\begin{aligned}\varepsilon^{u,\sigma} \\ \beta^{u, \sigma} \end{aligned}}
\end{aligned}
$$

Тензор деформации в линейном приближении имеет вид:

$$
u_{ij} = \frac{1}{2} \left( \frac{\partial u_i}{\partial x_j} + \frac{\partial u_j}{\partial x_i} \right)
$$

К сожалению, но эти уравнения статические. То есть они получены в предположении термодинамического равновесия. Динамические уравнения записывают через вектор перемещений $u_i$:

$$
\rho \frac{\partial^2 u_i}{\partial t^2} = 
\frac{\partial \sigma_{ij}}{\partial x_j}
$$

Далее отметим, что скорость распространения ЭМ колебаний существенно выше скорости звука. Поэтому можно считать, что электромагнитное поле (потенциал) меняется мгновенно и подчиняется уравнению:

$$
\mathrm{div\,} \vec{D} = 0
$$

В результате получаем систему уравнений:

$$
\rho \frac{\partial^2 u_i}{\partial t^2} = 
\frac{c^E_{ijkl}}{2} \left(\frac{\partial^2 u_k}{\partial x_l \partial x_j} + \frac{\partial^2 u_l}{\partial x_k \partial x_j}\right) - e^t_{ij,k} \frac{\partial^2 \varphi}{\partial x_k \partial x_j}
$$

$$
\frac{\partial}{\partial x_j} \left( \varepsilon^{u}_{ij} \frac{\partial \varphi}{\partial x_i} \right)= - \frac{e_{k,ij}}{2} \left( \frac{\partial^2 u_i }{\partial x_j \partial x_k} + \frac{\partial^2 u_j }{\partial x_i \partial x_k} \right)
$$