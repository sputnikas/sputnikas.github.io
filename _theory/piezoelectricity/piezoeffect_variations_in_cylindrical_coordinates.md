---
layout: theory_page
title: Вариационный принцип для пьезоэффекта и цилиндрические координаты
permalink: /piezoelectricity/piezoeffect_variations_in_cylindrical_coordinates/
previous_page: /piezoelectricity/piezoeffect_variations/
next_page: /piezoelectricity/piezoeffect_equations_in_vector_form/
---

В цилиндрических координатах:

$$
\frac{\partial}{\partial x} = \cos \alpha \frac{\partial}{\partial r} - \frac{\sin \alpha}{r} \frac{\partial}{\partial \alpha}
$$

$$
\frac{\partial}{\partial y} = \sin\alpha \frac{\partial}{\partial r} + \frac{\cos \alpha}{r} \frac{\partial}{\partial \alpha}
$$

$$
\vec{A} = A_x \vec{e}_x + A_y \vec{e}_y = A_r \vec{e}_r
+ A_\alpha \vec{e}_\alpha
$$

$$ 
\begin{cases} 
    \vec{e}_r = \vec{e}_x \cos \alpha + \vec{e}_y \sin \alpha, \\ 
    \vec{e}_\alpha =  - \vec{e}_x \sin \alpha + \vec{e}_y \cos \alpha.
\end{cases}
$$

Откуда:

$$
\begin{cases}  
    A_x = A_r \cos \alpha - A_\alpha \sin \alpha, \\  
    A_y = A_r \sin \alpha + A_\alpha \cos \alpha.
\end{cases}
$$

$$
\begin{aligned} 
\frac{\partial u_x}{\partial x} - \frac{\partial u_y}{\partial y} = 
&
\left(\cos \alpha \frac{\partial}{\partial r} - \frac{\sin \alpha}{r} \frac{\partial}{\partial \alpha}\right)\left(u_r \cos \alpha - u_\alpha \sin \alpha\right) -
\\ & 
- \left(\sin\alpha \frac{\partial}{\partial r} + \frac{\cos \alpha}{r} \frac{\partial}{\partial \alpha}\right) \left(u_r \sin \alpha + u_\alpha \cos \alpha\right) =
\\ &
= 
\cos^2 \alpha \frac{\partial u_r}{\partial r} - \sin \alpha \cos \alpha \frac{\partial u_\alpha}{\partial r} -
\\ &
- \frac{\sin \alpha \cos \alpha}{r} \frac{\partial u_r}{\partial \alpha} + \frac{\sin^2 \alpha }{r} u_r + \frac{\sin^2 \alpha }{r} \frac{\partial u_\alpha}{\partial \alpha} + \frac{\sin \alpha \cos \alpha}{r} u_\alpha
\\ &
- 
\sin^2 \alpha \frac{\partial u_r}{\partial r} - \sin \alpha \cos \alpha \frac{\partial u_\alpha}{\partial r} -
\\ &
- \frac{\sin \alpha \cos \alpha}{r} \frac{\partial u_r}{\partial \alpha} - \frac{\cos^2 \alpha }{r} u_r - \frac{\cos^2 \alpha }{r} \frac{\partial u_\alpha}{\partial \alpha} + \frac{\sin \alpha \cos \alpha}{r} u_\alpha
\\ &
= \cos 2\alpha \left(\frac{\partial u_r}{\partial r} - \frac{1}{r} \frac{\partial u_\alpha}{\partial \alpha} - \frac{u_r}{r} \right) - \sin 2\alpha 
\left(\frac{\partial u_\alpha}{\partial r} + \frac{1}{r} \frac{\partial u_r}{\partial \alpha} - \frac{u_\alpha}{r}\right)
\end{aligned}
$$

$$
\begin{aligned}
\frac{\partial u_y}{\partial x} + \frac{\partial u_x}{\partial y} = &
\left(\cos \alpha \frac{\partial}{\partial r} - \frac{\sin \alpha}{r} \frac{\partial}{\partial \alpha}\right)
\left(u_r \sin \alpha + u_\alpha \cos \alpha\right) +
\\ &
+ \left(\sin\alpha \frac{\partial}{\partial r} + \frac{\cos \alpha}{r} \frac{\partial}{\partial \alpha}\right) \left(u_r \cos \alpha - u_\alpha \sin \alpha\right) 
=
\\ & =
\cos \alpha \sin \alpha \frac{\partial u_r}{\partial r} + \cos^2 \alpha \frac{\partial u_\alpha}{\partial r} - 
\\ & -
\frac{\sin^2 \alpha}{r} \frac{\partial u_r}{\partial \alpha} -
\frac{\sin \alpha \cos \alpha}{r} u_r - 
\\ & -
\frac{\sin \alpha \cos \alpha}{r} \frac{\partial u_\alpha}{\partial \alpha} +
\frac{\sin^2 \alpha}{r} u_\alpha +
\\ & + 
\sin\alpha \cos \alpha \frac{\partial u_r}{\partial r} -
\sin^2\alpha \frac{\partial u_\alpha}{\partial r} +
\\ & +
\frac{\cos^2 \alpha}{r} \frac{\partial u_r}{\partial \alpha} -
\frac{\sin\alpha \cos \alpha}{r} u_r -
\\ & -
\frac{\sin\alpha \cos \alpha}{r} \frac{\partial u_\alpha}{\partial \alpha} -
\frac{\cos^2 \alpha}{r} u_\alpha = 
\\ & =
\sin 2\alpha \left(\frac{\partial u_r}{\partial r} - \frac{1}{r} \frac{\partial u_\alpha}{\partial \alpha} - \frac{u_r}{r} \right) + \cos 2\alpha 
\left(\frac{\partial u_\alpha}{\partial r} + \frac{1}{r} \frac{\partial u_r}{\partial \alpha} - \frac{u_\alpha}{r}\right)
\end{aligned}
$$

Введём обозначения:

$$
\begin{aligned}
& 
U_a = \frac{\partial u_r}{\partial r} - \frac{1}{r} \frac{\partial u_\alpha}{\partial \alpha} - \frac{u_r}{r} 
\\ &
U_b = \frac{\partial u_\alpha}{\partial r} + \frac{1}{r} \frac{\partial u_r}{\partial \alpha} - \frac{u_\alpha}{r}
\\ &
V_a = \frac{\partial v_r}{\partial r} - \frac{1}{r} \frac{\partial v_\alpha}{\partial \alpha} - \frac{v_r}{r} 
\\ &
V_b = \frac{\partial v_\alpha}{\partial r} + \frac{1}{r} \frac{\partial v_r}{\partial \alpha} - \frac{v_\alpha}{r}
\end{aligned}
$$

Тогда

$$
\begin{aligned}
(6) + (1) - (2) = &
\left(
    U_a \sin 2 \alpha + U_b \cos 2\alpha 
    \right) \left(
    V_a \sin 2 \alpha + V_b \cos 2\alpha 
\right) + 
\\ & +
\left(
    U_a \cos 2 \alpha - U_b \sin 2\alpha 
    \right) \left(
    V_a \cos 2 \alpha - V_b \sin 2\alpha 
\right) =
\\ & =
U_a V_a + U_b V_b
\end{aligned}
$$

Завершим теорию с вариационным принципом. Найдём в цилиндрических координатах:

$$
e_{k,ij} \frac{\partial \varphi}{\partial x_k} \frac{\partial u_j}{\partial x_i} = (**)
$$

Как и выше здесь будет несколько слагаемых с различными коэффициентами:

$$
(**) = e_{31} \frac{\partial \varphi}{\partial z} \left(\frac{\partial u_x}{\partial x} + \frac{\partial u_y}{\partial y}\right) + 
$$
$$
+ e_{33} \frac{\partial \varphi}{\partial z} \frac{\partial u_z}{\partial z} + e_{15} \left(\frac{\partial \varphi}{\partial x} \left[\frac{\partial u_z}{\partial x} + \frac{\partial u_x}{\partial z}\right] + \frac{\partial \varphi}{\partial y} \left[\frac{\partial u_z}{\partial y} + \frac{\partial u_y}{\partial z}\right]\right) =
$$

$$
= e_{31} \nabla_\perp \cdot \vec{u}_\perp + e_{33} \frac{\partial \varphi}{\partial z} + e_{15} \nabla_\perp \varphi \cdot  \left(\nabla_\perp u_z + \frac{\partial \vec{u}_\perp}{\partial z}\right)
$$