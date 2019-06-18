---
layout: theory_page
title: Уравнения пьезоэффекта в векторной форме
permalink: /piezoelectricity/piezoeffect_equations_in_vector_form/
previous_page: /piezoelectricity/piezoeffect_variations_in_cylindrical_coordinates/
next_page: /piezoelectricity/piezoeffect_first_example/
---

К сожалению, но моделирование с учётом вариационного принципа не прокатило. FreeFem++ не может найти спектр, а решения при заданной частоте имеют слишком странный вид и больше похожи на шумы. Чтобы понять в чём здесь причина, получим уравнения в векторной форме. Найдём:

$$
c_{ijkl} \frac{\partial^2 u_k}{\partial x_l \partial x_j}
$$

с учётом всех сделанных замечаний относительно коэффициентов. Сгруппируем все слагаемые суммы в таблицы:

|$x$|$y$|$z$|
|:-:|:-:|:-:|
|$c_{xxxx} = c_{11}$|$c_{yyyy} = c_{11}$|$c_{zzzz} = c_{33}$|
|$c_{xxyy} = c_{12}$|$c_{yyxx} = c_{12}$|$c_{zzxx} = c_{13}$|
|$c_{xxzz} = c_{13}$|$c_{yyzz} = c_{13}$|$c_{zzyy} = c_{13}$|
|$c_{xyxy} = c_{66}$|$c_{yxyx} = c_{66}$|$c_{zxzx} = c_{44}$|
|$c_{xyyx} = c_{66}$|$c_{yxxy} = c_{66}$|$c_{zxxz} = c_{44}$|
|$c_{xzxz} = c_{44}$|$c_{yzyz} = c_{44}$|$c_{zyzy} = c_{44}$|
|$c_{xzzx} = c_{44}$|$c_{yzzy} = c_{44}$|$c_{zyyz} = c_{44}$|

Откуда следует, что сумма:

$$
c_{xjkl} \frac{\partial^2 u_k}{\partial x_l \partial x_j} = 
c_{11} \frac{\partial^2 u_x}{\partial x^2} +
c_{12} \frac{\partial^2 u_y}{\partial x \partial y} +
c_{13} \frac{\partial^2 u_z}{\partial x \partial z} +
c_{66} \left(\frac{\partial^2 u_x}{\partial y^2} + \frac{\partial^2 u_y}{\partial x \partial y} \right) +
c_{44} \left(\frac{\partial^2 u_x}{\partial z^2} + \frac{\partial^2 u_z}{\partial x \partial z} \right)
$$

$$
c_{yjkl} \frac{\partial^2 u_k}{\partial x_l \partial x_j} = 
c_{11} \frac{\partial^2 u_y}{\partial y^2} +
c_{12} \frac{\partial^2 u_x}{\partial y \partial x} +
c_{13} \frac{\partial^2 u_z}{\partial y \partial z} +
c_{66} \left(\frac{\partial^2 u_y}{\partial x^2} + \frac{\partial^2 u_x}{\partial y \partial x} \right) +
c_{44} \left(\frac{\partial^2 u_y}{\partial z^2} + \frac{\partial^2 u_z}{\partial y \partial z} \right)
$$

$$
c_{zjkl} \frac{\partial^2 u_k}{\partial x_l \partial x_j} = 
c_{33} \frac{\partial^2 u_z}{\partial z^2} +
c_{13} \frac{\partial^2 u_x}{\partial x \partial z} +
c_{13} \frac{\partial^2 u_y}{\partial y \partial z} +
c_{44} \left(\frac{\partial^2 u_z}{\partial x^2} + \frac{\partial^2 u_x}{\partial x \partial z} + \frac{\partial^2 u_z}{\partial y^2} + \frac{\partial^2 u_y}{\partial y \partial z}\right)
$$

Далее вспомним про соотношение:

$$
c_{12} = c_{11} - 2 c_{66}
$$

Умножаем на орты, складываем первое со вторым и получаем:

$$
c_{11} \nabla_\perp (\nabla_\perp \cdot \vec{u}_\perp) + 
(c_{13} + c_{44}) \nabla_\perp \frac{\partial u_z}{\partial z} +
c_{44} \frac{\partial^2 \vec{u}_\perp}{\partial z^2} +
$$

$$
+ c_{66} 
\left[ 
    \vec{e}_x \frac{\partial}{\partial y} 
    \left(
        \frac{\partial u_x}{\partial y} - \frac{\partial u_y}{\partial x} 
    \right) +
    \vec{e}_y \frac{\partial}{\partial x} 
    \left(
        \frac{\partial u_y}{\partial x} - \frac{\partial u_x}{\partial y} 
    \right)
\right] =
$$

$$
= c_{11} \nabla_\perp (\nabla_\perp \cdot \vec{u}_\perp) + 
(c_{13} + c_{44}) \nabla_\perp \frac{\partial u_z}{\partial z} +
c_{44} \frac{\partial^2 \vec{u}_\perp}{\partial z^2} +
$$

$$
+ c_{66} 
\left[ 
    \vec{e}_y\times\vec{e}_z \frac{\partial}{\partial y} 
    \left(
        \frac{\partial u_x}{\partial y} - \frac{\partial u_y}{\partial x} 
    \right) +
    \vec{e}_x\times\vec{e}_z \frac{\partial}{\partial x} 
    \left(
         \frac{\partial u_x}{\partial y} - \frac{\partial u_y}{\partial x}
    \right)
\right] =
$$

$$
= c_{11} \nabla_\perp (\nabla_\perp \cdot \vec{u}_\perp) + 
(c_{13} + c_{44}) \nabla_\perp \frac{\partial u_z}{\partial z} +
c_{44} \frac{\partial^2 \vec{u}_\perp}{\partial z^2} - c_{66} \nabla_\perp \times (\nabla_\perp \times \vec{u}_\perp)
$$

Аналогично третье соотношение:

$$
c_{33} \frac{\partial^2 u_z}{\partial z^2} +
(c_{13} + c_{44}) \frac{\partial}{\partial z} (\nabla_\perp\cdot\vec{u}_\perp) +
c_{44} \Delta_\perp u_z
$$

Далее перепишем в векторной форме:

$$
- e^t_{ij,k} \frac{\partial^2 \varphi}{\partial x_k \partial x_j} = - e_{k,ij} \frac{\partial^2 \varphi}{\partial x_k \partial x_j}
$$

Начнём опять с таблицы, в которой перечислим ненулевые коспоненты тензора $\hat{e}$:

|$x$|$y$|$z$|
|:-:|:-:|:-:|
|$e_{x,xz} = e_{15}$|$e_{y,yz} = e_{15}$|$e_{x,zx} = e_{15}$|
|$e_{z,xx} = e_{31}$|$e_{z,yy} = e_{31}$|$e_{y,zy} = e_{15}$|
|-|-|$e_{z,zz} = e_{33}$|

Теперь суммируем по осям:

$$
(e_{15} + e_{31}) \frac{\partial^2 \varphi}{\partial x \partial z}$$

$$
(e_{15} + e_{31}) \frac{\partial^2 \varphi}{\partial y \partial z}
$$

$$
e_{15} \left(
    \frac{\partial^2 \varphi}{\partial x^2} + 
    \frac{\partial^2 \varphi}{\partial y^2}
\right)
+
e_{33} \frac{\partial^2 \varphi}{\partial z^2} = 
e_{15} \Delta_\perp \varphi + 
e_{33} \frac{\partial^2 \varphi}{\partial z^2} 
$$

Умножаем первое и второе на соответствующие орты и снова складываем:

$$
(e_{15} + e_{31}) \nabla_\perp \frac{\partial\varphi}{\partial z}
$$

Также найдём:

$$
e_{k,ij} \frac{\partial^2 u_i }{\partial x_j \partial x_k} 
= 
e_{15} \left(
    \frac{\partial^2 u_x }{\partial z \partial x} +
    \frac{\partial^2 u_z }{\partial x^2} +
    \frac{\partial^2 u_y }{\partial z \partial y} +
    \frac{\partial^2 u_z }{\partial y^2}
\right)
+
e_{31} \left(
    \frac{\partial^2 u_x }{\partial z \partial x} +
    \frac{\partial^2 u_y }{\partial z \partial y}
\right)
+
e_{33} \frac{\partial^2 u_z }{\partial z^2} =
$$

$$
= (e_{15} + e_{31}) \frac{\partial}{\partial z} (\nabla_\perp\cdot\vec{u}_\perp) +
e_{31} \Delta_\perp u_z +
e_{33} \frac{\partial^2 u_z }{\partial z^2}
$$

Собираем теперь всё вместе, чтобы получить уравнение в векторной форме для $x, y$ компонент:

$$
\begin{aligned}
&
\rho \frac{\partial^2 \vec{u}_\perp}{\partial t^2} 
= 
c_{11} \nabla_\perp (\nabla_\perp \cdot \vec{u}_\perp) + 
(c_{13} + c_{44}) \nabla_\perp \frac{\partial u_z}{\partial z} +
c_{44} \frac{\partial^2 \vec{u}_\perp}{\partial z^2} - c_{66} \nabla_\perp \times (\nabla_\perp \times \vec{u}_\perp) 
-
(e_{15} + e_{31}) \nabla_\perp \frac{\partial\varphi}{\partial z}
\\
&
\rho \frac{\partial^2 u_z}{\partial t^2} 
=
c_{33} \frac{\partial^2 u_z}{\partial z^2} +
(c_{13} + c_{44}) \frac{\partial}{\partial z} (\nabla_\perp\cdot\vec{u}_\perp) +
c_{44} \Delta_\perp u_z
-
e_{15} \Delta_\perp \varphi - 
e_{33} \frac{\partial^2 \varphi}{\partial z^2}
\end{aligned}
$$

Недостающее уравнение для потенциалов аналогично принимает вид:

$$
\varepsilon_{11} \Delta_\perp \varphi +
\varepsilon_{33} \frac{\partial^2 \varphi}{\partial z^2}
= 
- (e_{15} + e_{31}) \frac{\partial}{\partial z} (\nabla_\perp\cdot\vec{u}_\perp) -
e_{31} \Delta_\perp u_z -
e_{33} \frac{\partial^2 u_z }{\partial z^2}
$$