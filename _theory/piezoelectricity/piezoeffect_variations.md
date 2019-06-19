---
layout: theory_page
title: Вариационный принцип для пьезоэффекта
permalink: /piezoelectricity/piezoeffect_variations/
previous_page: /piezoelectricity/piezoeffect_tensors_and_equations/
next_page: /piezoelectricity/piezoeffect_variations_in_cylindrical_coordinates/
---

Умножим на $\delta u_i$ первое уравнение и просуммируем по $i$, умножим на $\delta \varphi$ второе уравнение, а затем проинтегриуем по $dVdt$:

$$
\rho \delta u_i \frac{\partial^2 u_i}{\partial t^2} = 
\frac{c^E_{ijkl}}{2} \delta u_i \left(\frac{\partial^2 u_k}{\partial x_l \partial x_j} + \frac{\partial^2 u_l}{\partial x_k \partial x_j}\right) + e^t_{ij,k} \delta u_i \frac{\partial^2 \varphi}{\partial x_k \partial x_j}
$$

$$
\delta \varphi \frac{\partial}{\partial x_j} \left( \varepsilon^{u}_{ij} \frac{\partial \varphi}{\partial x_i} \right)= \delta \varphi \frac{e_{k,ij}}{2} \left( \frac{\partial^2 u_i }{\partial x_j \partial x_k} + \frac{\partial^2 u_j }{\partial x_i \partial x_k} \right)
$$

После интегрирования по частям и пренебрегая всеми нелинейными слагаемыми ($\partial \rho/\partial t$ и т.д.):

$$
- \int\limits_{t_1}^{t_2} \int\limits_V \rho \frac{\partial \delta u_i}{\partial t} \frac{\partial u_i}{\partial t} dV dt =  - \int\limits_{t_1}^{t_2} \int\limits_{V} \frac{c^E_{ijkl}}{2} \frac{\partial \delta u_i}{\partial x_j} \left(\frac{\partial u_k}{\partial x_l} + \frac{\partial u_l}{\partial x_k}\right) dV dt - 
\int\limits_{t_1}^{t_2} \int\limits_{V} e^t_{ij,k} \frac{\partial \delta u_i}{\partial x_j} \frac{\partial \varphi}{\partial x_k} dV dt
$$

В силу симметрии упругих коэффициентов получаем:

$$
\int\limits_{t_1}^{t_2} \int\limits_V 
\left[
    \rho \frac{\partial \delta u_i}{\partial t} \frac{\partial u_i}{\partial t} - 
    c^E_{ijkl} \frac{\partial \delta u_i}{\partial x_j} \frac{\partial u_k}{\partial x_l}  - 
    e^t_{ij,k} \frac{\partial \delta u_i}{\partial x_j} \frac{\partial \varphi}{\partial x_k}
\right] dV dt = 0
$$

$$
\int\limits_{t_1}^{t_2} \int\limits_V  \varepsilon^{u}_{ij} \frac{\partial \delta \varphi}{\partial x_j} \frac{\partial \varphi}{\partial x_i} dV dt - \int\limits_{t_1}^{t_2} \int\limits_V e_{k,ij} \frac{\partial \delta \varphi}{\partial x_k } \frac{\partial u_i }{\partial x_j} dV dt = 0
$$

Отсюда следует общий вариационный принцип для пьезоэлектриков:

$$
\delta 
\int\limits_{t_1}^{t_2} \int\limits_V 
\left[
    \frac{\rho}{2} \left(\frac{\partial u_i}{\partial t} \right)^2 - 
    \frac{c^E_{ijkl}}{2} \frac{\partial u_i}{\partial x_j} \frac{\partial u_k}{\partial x_l}  - 
    e^t_{ij,k} \frac{\partial u_i}{\partial x_j} \frac{\partial \varphi}{\partial x_k} +
    \frac{\varepsilon^{u}_{ij}}{2} \frac{\partial \varphi}{\partial x_j} \frac{\partial \varphi}{\partial x_i}
\right] dV dt = 0
$$

Отметим, что последние вариационные принципы получены так, что остаются справедливы и для неоднородной среды. Это многое упрощает в задаче об упругих колебаниях твёрдых тел. Ведь граничные условия для тензора напряжений и вектора $\vec{D}$ теперь должны вытекать из непрерывности вектора перемещений и потенциала на границе раздела сред и данного вариационного принципа.

Симметрии пьезокристалла с поляризацией вдоль оси $z$ позволяют свести слагаемые с $c_{ijkl}$ для первого вариационного принципа к слагаемым содержащим следующие коэффициенты (далее $u_i = \{u_x, u_y, u_z\}, \delta u_i = \{v_x, v_y, v_z\}$):

|$c_{xxxx} = c_{yyyy} = c_{11}$|
|:-:|
|$c_{xxyy} = c_{yyxx} = c_{12}$|
|$c_{xxzz} = c_{zzxx} = c_{zzyy} = c_{yyzz} = c_{13}$|
|$c_{zzzz} = c_{33}$|
|$c_{yzyz} = c_{yzzy} = c_{zyyz} = c_{zyzy} = c_{44}$|
|$c_{xzxz} = c_{xzzx} = c_{zxxz} = c_{zxzx} = c_{55} = c_{44}$|
|$c_{xyxy} = c_{xyyx} = c_{yxxy} = c_{yxyx} = c_{66} = 0.5(c_{11} - c_{12})$|

В результате слагаемые вида:

$$
c_{ijkl} \frac{\partial v_i}{\partial x_j} \frac{\partial u_k}{\partial x_l} = [(*)]
$$

Перейдут в:

$$
c_{11} \left[
    \frac{\partial v_x}{\partial x} \frac{\partial u_x}{\partial x}
    +
    \frac{\partial v_y}{\partial y} \frac{\partial u_y}{\partial y}
\right] = c_{11} \left[(1)\right]
$$

$$
c_{12} \left[
    \frac{\partial v_x}{\partial x} \frac{\partial u_y}{\partial y}
    +
    \frac{\partial v_y}{\partial y} \frac{\partial u_x}{\partial x}
\right] = c_{12} \left[(2)\right]
$$

$$
c_{13} \left[
    \frac{\partial v_x}{\partial x} \frac{\partial u_z}{\partial z}
    +
    \frac{\partial v_z}{\partial z} \frac{\partial u_x}{\partial x}
    +
    \frac{\partial v_y}{\partial y} \frac{\partial u_z}{\partial z}
    +
    \frac{\partial v_z}{\partial z} \frac{\partial u_y}{\partial y}
\right]
= c_{13} \left[(3)\right]
$$

$$
c_{33} \left[
    \frac{\partial u_z}{\partial z} \frac{\partial v_z}{\partial z}
\right]
= c_{33} \left[(4)\right]
$$

$$
c_{44} \left[
    \frac{\partial v_y}{\partial z} \frac{\partial u_y}{\partial z}
    +
    \frac{\partial v_y}{\partial z} \frac{\partial u_z}{\partial y}
    +
    \frac{\partial v_z}{\partial y} \frac{\partial u_y}{\partial z}
    +
    \frac{\partial v_z}{\partial y} \frac{\partial u_z}{\partial y}
    +
    \frac{\partial v_x}{\partial z} \frac{\partial u_x}{\partial z}
    +
    \frac{\partial v_x}{\partial z} \frac{\partial u_z}{\partial x}
    +
    \frac{\partial v_z}{\partial x} \frac{\partial u_x}{\partial z}
    +
    \frac{\partial v_z}{\partial x} \frac{\partial u_z}{\partial x}
\right]
= c_{44} \left[(5)\right]
$$

$$
c_{66} \left[
    \frac{\partial v_x}{\partial y} \frac{\partial u_x}{\partial y}
    +
    \frac{\partial v_x}{\partial y} \frac{\partial u_y}{\partial x}
    +
    \frac{\partial v_y}{\partial x} \frac{\partial u_x}{\partial y}
    +
    \frac{\partial v_y}{\partial x} \frac{\partial u_y}{\partial x}
\right]
= c_{66} \left[(6)\right]
$$

Откуда:

$$
(*) = c_{11} [(1) + (2) - (2)] + c_{12} (2) + c_{13} (3) + c_{33} (4) + c_{44} (5) + c_{66} (6) =  
$$

$$ = c_{11} [(1) + (2)] + [ c_{12} - c_{11} ](2) + c_{13} (3) + c_{33} (4) + c_{44} (5) + c_{66} (6) = 
$$

$$ = c_{11} [(1) + (2)] + c_{13} (3) + c_{33} (4) + c_{44} (5) + c_{66} [(6) - 2(2)] = 
$$

$$ = c_{11} [(1) + (2)] + c_{13} (3) + c_{33} (4) + c_{44} (5) + c_{66} [(6) - \{(1) + (2)\} + \{(1) - (2)\}]
$$

Учитывая:

$$
\nabla_\perp \cdot \vec{u}_\perp = \frac{\partial u_x}{\partial x} +  \frac{\partial u_y}{\partial y}
$$

$$
\nabla_\perp \times (\vec{e}_z \times \vec{u}_\perp) = \vec{e}_z (\nabla_\perp \cdot \vec{u}_\perp) - (\vec{e}_z \cdot \nabla_\perp) \vec{u}_\perp = 
\vec{e}_z (\nabla_\perp \cdot \vec{u}_\perp)
$$

$$
\nabla_\perp \cdot (\vec{e}_z \times \vec{u}_\perp) = \nabla_\perp \cdot \{- u_y, u_x\} = - \frac{\partial u_y}{\partial x} + \frac{\partial u_x}{\partial y}
$$

И:

$$
(1) + (2) = (\nabla_\perp \cdot \vec{u}_\perp)(\nabla_\perp \cdot \vec{v}_\perp)
$$

$$
(1) - (2) = \left(
    \frac{\partial u_x}{\partial x}
    -
   \frac{\partial u_y}{\partial y}
\right) \left(
    \frac{\partial v_x}{\partial x}
    -
   \frac{\partial v_y}{\partial y}
\right)
$$

$$
(3) = \frac{\partial u_z}{\partial z} \nabla_\perp \cdot \vec{v}_\perp + \frac{\partial v_z}{\partial z} \nabla_\perp \cdot \vec{u}_\perp
$$

$$
(5) = 
\frac{\partial \vec{v}_\perp}{\partial z} \cdot 
\frac{\partial \vec{u}_\perp}{\partial z}
+
\frac{\partial \vec{v}_\perp}{\partial z} \cdot \nabla_\perp u_z
+
\frac{\partial \vec{u}_\perp}{\partial z} \cdot \nabla_\perp v_z
+
\nabla_\perp v_z \cdot \nabla_\perp u_z =
$$

$$
= \left(\frac{\partial \vec{v}_\perp}{\partial z} + \nabla_\perp v_z\right) \cdot
\left(\frac{\partial \vec{u}_\perp}{\partial z} + \nabla_\perp u_z\right)
$$

$$
(6) = \left(
    \frac{\partial u_x}{\partial y}
    +
   \frac{\partial u_y}{\partial x}
\right) \left(
    \frac{\partial v_x}{\partial y}
    +
   \frac{\partial v_y}{\partial x}
\right)
$$
