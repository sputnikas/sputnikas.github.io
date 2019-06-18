---
layout: theory_page
title: Пьезоэлектрическая бесконечная пластина на неподвижной подложке в воздушной среде
permalink: /piezoelectricity/piezoeffect_first_example/
previous_page: /piezoelectricity/piezoeffect_equations_in_vector_form/
next_page: /piezo/
---

Пусть пьезоэлектрическая пластина толщиной $l$ и неограниченная в плоскости $(x,y)$ лежит на неподвижной подложке и помещена в воздушную среду. Из-за наличия трансляционной симметрии $$\vec{u}_\perp = 0$$, $$\nabla_\perp = 0$$ . Соответствующие уравнения в пластине принимают вид:

$$
\begin{aligned}
&
\rho \frac{\partial^2 u_z}{\partial t^2} 
=
c_{33} \frac{\partial^2 u_z}{\partial z^2} - 
e_{33} \frac{\partial^2 \varphi}{\partial z^2}
\\
&
\varepsilon_{33} \frac{\partial^2 \varphi}{\partial z^2}
=  
- e_{33} \frac{\partial^2 u_z }{\partial z^2}
\end{aligned}
$$

В воздухе:

$$
\begin{aligned}
&
\rho' \frac{\partial^2 u_z}{\partial t^2} 
=
c_{33}' \frac{\partial^2 u_z}{\partial z^2}
\end{aligned}
$$

Где $c_{33}' = \gamma p_0$, $\gamma$ - показатель адиабаты, $p_0$ - атмосферное давление. Граничные условия для $u_z$:

$$
\begin{aligned}
& u_z \Big|_{l-} = u_z \Big|_{l+} \\
& u_z \Big|_{0} = 0
\end{aligned}
$$

Если рассмотреть маленький цилиндр, на границе $l$, то устремив толщину этого цилиндра к нулю, легко получить условие равенства давлений на границе $z = l$:

$$
p = -\sigma_{zz}
$$

Со стороны воздушной среды:

$$
p = -c_{33}' \frac{\partial u_z}{\partial z}
$$

Со стороны пьезоэлектрика:

$$
\sigma_{zz} = 
c_{zzxx} \frac{\partial u_x}{\partial x} + 
c_{zzyy} \frac{\partial u_y}{\partial y} +
c_{zzzz} \frac{\partial u_z}{\partial z} -
e_{zz,x}^t \frac{\partial \varphi}{\partial x} -
e_{zz,y}^t \frac{\partial \varphi}{\partial y} -
e_{zz,z}^t \frac{\partial \varphi}{\partial z} = [e^t_{zz,\perp} = 0]
$$

$$
= c_{13} \nabla_\perp\cdot\vec{u}_\perp +
c_{33} \frac{\partial u_z}{\partial z} -
e_{33} \frac{\partial \varphi}{\partial z}
$$

Отсюда следует, что в нашем случае на границе выполняется равенство:

$$
c_{33} \frac{\partial u_z}{\partial z} \Big|_{l-} -
e_{33} \frac{\partial \varphi}{\partial z} \Big|_{l-}
=
c_{33}' \frac{\partial u_z}{\partial z} \Big|_{l+}
$$

И, наконец, последнее условие - условие отсутствия отраженных волн в воздушной среде:

$$
\lim_{z\to\infty} \left( v' \frac{\partial u_z}{\partial z} + \frac{\partial u_z}{\partial t} \right) = 0
$$

Здесь $v' = \sqrt{c_{33}'/\rho'}$ - скорость звука в воздухе. Из симметрии задачи, полагая, что потенциал меняется по синусоидальному закону с постоянной частотой:

$$
\varphi \Big|_l= U e^{i\omega t}
$$

Мы получаем следующее решение в воздухе:

$$
u_z = u_{z}\Big|_{l+} e^{i\omega (t - (z- l)/v')} = u_{z}\Big|_{l-} e^{i\omega (t - (z- l)/v')}
$$

Легко видеть, что оно удовлетворяет условиям на бесконечности. Тогда внутри пластины мы имеем задачу:

$$
\begin{aligned}
&
\rho \frac{\partial^2 u_z}{\partial t^2} 
=
c_{33} \frac{\partial^2 u_z}{\partial z^2} - 
e_{33} \frac{\partial^2 \varphi}{\partial z^2}
\\
&
\varepsilon_{33} \frac{\partial^2 \varphi}{\partial z^2}
=  
- e_{33} \frac{\partial^2 u_z }{\partial z^2}
\\
& u_z \Big|_{0} = 0 \\
& c_{33} \frac{\partial u_z}{\partial z} \Big|_{l-} -
e_{33} \frac{\partial \varphi}{\partial z} \Big|_{l-}
=
- \frac{i\omega c_{33}'}{v'} u_{z}\Big|_{l-} e^{i\omega t} \\
& \varphi \Big|_{0} = 0 \\
& \varphi \Big|_l = U e^{i\omega t}
\end{aligned}
$$

Из второго уравнения следует, что:

$$
\frac{\partial \varphi}{\partial z} = - \frac{e_{33}}{\varepsilon_{33}} \frac{\partial u_z}{\partial z} - E
$$

$E$ - постоянная по $z$, но может быть (и будет) функцией времени $E = E_0 \exp (i\omega t)$. Подставляя данное соотношение в первое уравнение и в граничное условие, а также учитывая, что $u_z = u_z'(z) \exp (i\omega t)$,  $\varphi = \varphi'(z) \exp (i\omega t)$ получаем:

$$
\begin{aligned}
&
-\omega^2 u_z'
=
v^2 \frac{d^2 u_z'}{d z^2}
\\
& u_z' \Big|_{0} = 0 \\
& v^2 \frac{d u_z'}{\partial z} \Big|_{l-} + \frac{i\omega c_{33}'}{v'\rho} u_{z}'\Big|_{l-}
= - \frac{e_{33}}{\rho} E_0 \\
& \varphi' \Big|_{0} = 0 \\
& \varphi' \Big|_l = U \\
& \varphi' = - \frac{e_{33}}{\varepsilon_{33}} u_z' - E_0 z
\end{aligned}
$$

Здесь:

$$
v^2 = \frac{c_{33} \varepsilon_{33} + e_{33}^2}{\varepsilon_{33} \rho}
$$

Введём также обозначение $V^2 = c_{33}/\rho$. Из последнего выражаем $E_0$ и подставляем в третье выражение:

$$
E_0 = - \frac{e_{33}}{\varepsilon_{33} l} u_z'\Big|_l - \frac{U}{l}
$$

$$
\begin{aligned}
&
-\omega^2 u_z'
=
v^2 \frac{d^2 u_z'}{d z^2}
\\
& u_z' \Big|_{0} = 0 \\
& \frac{d u_z'}{\partial z} \Big|_l + \frac{1}{l} \left(\frac{i\omega l v'\rho'}{\rho v^2} + \frac{V^2}{v^2} - 1 \right) u_{z}'\Big|_l
=  \frac{e_{33} U}{\rho l v^2} 
\end{aligned}
$$

Легко видеть, что решение представляет собой:

$$
u_z' = A \sin \left(\frac{\omega z}{v}\right)
$$

Обозначая $k = \omega/v$:

$$
kA \cos (kl) - \frac{A}{l} \left(1 -\frac{V^2}{v^2} - i k l \frac{v'\rho'}{v \rho} \right) \sin (kl) = \frac{e_{33} U}{\rho l v^2} 
$$

Откуда находим $A$ при данной частоте:

$$
A = \frac{e_{33} U}{\rho v^2} \frac{1}{k l \cos (kl) - \left(1 -\dfrac{V^2}{v^2} - i k l \dfrac{v'\rho'}{v \rho} \right) \sin (kl)}
$$

$$
|A| = \frac{e_{33} U}{\rho v^2} \frac{1}{\sqrt{\left(k l \cos (kl)- \left(1 -\dfrac{V^2}{v^2}\right) \sin (kl) \right)^2 + \left(k l \dfrac{v'\rho'}{v \rho} \right)^2 \sin^2 (kl)}}
$$

$$
\arg A = - \arctan \frac{\dfrac{v'\rho'}{v \rho} \tan (kl)}{1 - \left(1 -\dfrac{V^2}{v^2}\right) \dfrac{\tan (kl)}{kl}}
$$

Следует отметить, что мы нашли таким образом частное решение, а не общее. Тем не менее именно оно обладает физическим смыслом, так как собственные частоты все комплексные, а значит возбуждение никогда не происходит на собственной частоте - собственные гармоники быстро затухают со временем. На рисунке представлена зависимость модуля $A$ от параметра $kl$ для ЦТСнв1 ($A_0 = e_{33} U/\rho v^2$). 

<div style="text-align:center"><img src="/img/piezoeffect_first_example_1.png"></div>

Видно, что имеют место резонансы. Первый резонанс $\omega = 0$ не рассматриваем, так как при этом меняется характер решения, второй приходится на значение $kl \approx 1.3$. Для толщины $l = 0.5$ мм, при скорости звука в материале $v = 3770$ м/c, это соответствует частоте возбуждения $f = \omega/2\pi \approx 1.56$ МГц. Очевидно, что такие большие частоты не соответствуют звуковой частоте. Это означает, что для звуковых устройств с пьезокерамикой в первую очередь играют роль неоднородности в поперечном сечении.