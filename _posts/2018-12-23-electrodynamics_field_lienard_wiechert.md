---
layout: page
title: Поле произвольно движущейся заряженной частицы
---

## Потенциалы Лиенара-Вихерта

Наша задача найти потенциалы электромагнитного поля произвольно движущейся заряженной частицы. Они представляют собой решение системы уравнений:

$$
\begin{aligned}
& \Delta \varphi - \frac{1}{c^2} \frac{\partial^2 \varphi}{\partial t^2} = - \frac{q}{\varepsilon_0} \delta(\vec{r} - \vec{\xi}(t)) \\
& \Delta \vec{A} - \frac{1}{c^2} \frac{\partial^2 \vec{A}}{\partial t^2} = - \mu_0 q \vec{v}(t) \delta(\vec{r} - \vec{\xi}(t)) \\
\end{aligned}
$$

Решение данных уравнений в неограниченном пространстве дают запаздывающие потенциалы:

$$
\begin{aligned}
&
\varphi = \frac{1}{4\pi\varepsilon_0} \int \frac{\rho(\vec{r}', t - |\vec{r} - \vec{r}'|/c)}{|\vec{r} - \vec{r}'|} dV' \\
&
\vec{A} = \frac{\mu_0}{4\pi} \int \frac{\vec{j}(\vec{r}', t - |\vec{r} - \vec{r}'|/c)}{|\vec{r} - \vec{r}'|} dV' \\
\end{aligned}
$$

**Первый способ.** Ограничимся случаем первого уравнения и найдём его решение с помощью запаздывающего потенциала:

$$
\varphi(\vec{r}, t) = \frac{q}{\varepsilon_0} \int \frac{\delta(\vec{r}' - \vec{\xi}(t - |\vec{r} - \vec{r}'|/c))}{|\vec{r} - \vec{r}'|} dV' = (1)
$$

Перейдём в интеграле к новому времени интегрирования $t'$:

$$
(1) = \frac{q}{\varepsilon_0} \int\limits_{-\infty}^\infty \int \frac{\delta(\vec{r}' - \vec{\xi}(t'))}{|\vec{r} - \vec{r}'|} \delta(t' - t +  |\vec{r} - \vec{r}'|/c) dV' dt'
$$

Выполняем интегрирование по объёму:

$$
(1) = \frac{q}{\varepsilon_0} \int\limits_{-\infty}^\infty \frac{1}{|\vec{r} - \vec{\xi}(t')|} \delta(t' - t +  |\vec{r} - \vec{\xi}(t')|/c) dt'
$$

Введём следующие обозначения:

$$
\vec{R} = \vec{r} - \vec{\xi}(t'), \qquad 
R = |\vec{R}|, \qquad
\vec{n} = \vec{R}/R, \qquad
\vec{v} = \dot{\vec{\xi}}
$$

И воспользуемся следующим соотношением:

$$
\delta(f(t')) = \sum\limits_{t'_i} \frac{\delta(t' - t'_i)}{|f'(t'_i)|)}
$$

Здесь $t'_i$ - корни $f(t')$. В нашем случае $f(t') = t' - t + R(t')/c$. Покажем, что корень у данной функции, если он существует, - один. Действительно пусть существуют два корня. Тогда между корнями функции лежит корень производной:

$$
f'(t') = 1 - \vec{n}\cdot\vec{v}/c= 0
$$

Но это означает, что скорость $v > c$, что невозможно. Как доказать существование корня? Вопрос интересный. Отмечу только, что функция всюду возрастающая и корень действительно существует.

С учётом всего изложенного нетрудно получить:

$$
\begin{aligned}
& \varphi = \frac{q}{4\pi \varepsilon_0} \frac{1}{R - \dfrac{\vec{R}\cdot\vec{v}}{c}} \Big|_{t': c(t - t') = R} \\
& \vec{A} = \frac{\mu_0 q}{4\pi} \frac{\vec{v}}{R - \dfrac{\vec{R}\cdot\vec{v}}{c}} \Big|_{t': c(t - t') = R} \\
\end{aligned}
$$

**Второй способ.** Он использован, например, в книгах по теорфизике Ландау. Отметим, что потенциалы должны удовлетворять уравнению Пуассона в мгновенной системе отсчёта, но только в пределах одной единственной сферы для которой частица выглядит неподвижной и до которой дошло излучение со скоростью $c$. То есть:

$$
\varphi'' = \frac{q}{4\pi\varepsilon_0} \frac{1}{R''}, \qquad \vec{A}'' = 0
$$

Сфера определяется соотношением:

$$
R'' = c(t'' - t''_0)
$$

Учитываем преобразования Лоренца:

$$
t'' = \frac{t - \dfrac{\vec{r}\cdot\vec{v}}{c^2}}{\sqrt{1 - v^2/c^2}}, \qquad
t''_0 = \frac{t' - \dfrac{\vec{\xi}'\cdot\vec{v}}{c^2}}{\sqrt{1 - v^2/c^2}}
$$

Откуда:

$$
R'' = \frac{c(t - t') - \dfrac{\vec{R}\cdot\vec{v}}{c}}{\sqrt{1 - v^2/c^2}} = [\text{в силу инвариантности интервала } R = c(t - t')] = \frac{R - \dfrac{\vec{R}\cdot\vec{v}}{c}}{\sqrt{1 - v^2/c^2}}
$$

Далее вспоминаем преобразование для потенциалов:

$$
\varphi = \frac{\varphi'' + \vec{A}\cdot\vec{v}}{\sqrt{1 - v^2/c^2}}, \qquad
\vec{A} = \vec{A}'' - \frac{\vec{A}''\cdot\vec{v}}{v^2} \vec{v} + \frac{\dfrac{\vec{A}''\cdot\vec{v}}{v^2} \vec{v} + \dfrac{\varphi'' \vec{v}}{c^2}}{\sqrt{1 - v^2/c^2}}, \qquad
$$

И получаем формулы выше.

## Электромагнитное поле

Получим некоторые соотношения:

$$
\nabla R = \frac{\partial |\vec{r} - \vec{\xi}[t'(t, \vec{r})]|}{\partial x_i} \vec{e}_i = \frac{2(x_j - \xi_j(t'))(\delta_{ji} - v_j \dfrac{\partial t'}{\partial x_i})}{2 R} = \vec{n} - \vec{n}\cdot\vec{v} \nabla t'
$$

Отсюда

$$
\nabla t' = - \frac{\nabla R}{c} = \frac{\vec{n}\cdot\vec{v}}{c} \nabla t' - \frac{\vec{n}}{c}
$$

Далее

$$
\nabla t' = - \frac{1}{c}\frac{\vec{n}}{1 - \dfrac{\vec{n}\cdot\vec{v}}{c} }
$$

$$
\nabla R = \frac{\vec{n}}{1 - \dfrac{\vec{n}\cdot\vec{v}}{c} }
$$

Теперь получим соотношение для производных по времени:

$$
\frac{\partial t'}{\partial t} = 1 - \frac{1}{c}\frac{\partial R}{\partial t} = 1 + \frac{\vec{n}\cdot\vec{v}}{c} 
\frac{\partial t'}{\partial t}
$$

Отсюда 

$$
\frac{\partial t'}{\partial t} = \frac{1}{1 - \dfrac{\vec{n}\cdot\vec{v}}{c} }
$$

$$
\frac{\partial R}{\partial t} = - \frac{\vec{n}\cdot\vec{v}}{1 - \dfrac{\vec{n}\cdot\vec{v}}{c} }
$$

Теперь получим ещё два полезных соотношения:

$$
\nabla \frac{1}{R - \dfrac{\vec{R}\cdot\vec{v}}{c} } = -
\frac{1}{R^2 \left(1 - \dfrac{\vec{n}\cdot\vec{v}}{c} \right)^2} \nabla \left(R - \dfrac{\vec{R}\cdot\vec{v}}{c} \right) =
$$

$$ 
= - \frac{1}{R^2 \left(1 - \dfrac{\vec{n}\cdot\vec{v}}{c} \right)^3} \left(\vec{n} - \left(1 - \dfrac{\vec{n}\cdot\vec{v}}{c} \right)\dfrac{\vec{v}}{c} - \frac{v^2}{c^2} \vec{n} + \frac{\vec{R}\cdot\vec{a}}{c^2} \vec{n}\right)
$$

$$
\frac{\partial}{\partial t} \frac{1}{R - \dfrac{\vec{R}\cdot\vec{v}}{c} } = -
\frac{1}{R^2 \left(1 - \dfrac{\vec{n}\cdot\vec{v}}{c} \right)^2} \frac{\partial}{\partial t} \left(R - \dfrac{\vec{R}\cdot\vec{v}}{c} \right) =
$$

$$
= -
\frac{1}{R^2 \left(1 - \dfrac{\vec{n}\cdot\vec{v}}{c} \right)^3} \left(- \vec{n}\cdot\vec{v} + \frac{v^2}{c} - \frac{\vec{R}\cdot\vec{a}}{c}\right) =
$$

Дальнейшее легко:

$$
\vec{E} = \frac{q}{4\pi\varepsilon_0} \frac{1}{R^2 \left(1 - \dfrac{\vec{n}\cdot\vec{v}}{c} \right)^3} \left(
    - \frac{\vec{v}(\vec{n}\cdot\vec{v})}{c^2} +
    \vec{v}\frac{v^2}{c^3} -  \frac{\vec{R}\cdot\vec{a}}{c^3} \vec{v}
    \right. -
$$

$$
    - \left.    
     \left(1 - \dfrac{\vec{n}\cdot\vec{v}}{c} \right) \frac{R}{c^2}\vec{a} +
    \vec{n} - 
    \left(1 - \dfrac{\vec{n}\cdot\vec{v}}{c} \right)\dfrac{\vec{v}}{c} - 
    \frac{v^2}{c^2} \vec{n} + 
    \frac{\vec{R}\cdot\vec{a}}{c^2} \vec{n}
\right) =
$$

$$
= \frac{q}{4\pi\varepsilon_0} \frac{1}{R^2 \left(1 - \dfrac{\vec{n}\cdot\vec{v}}{c} \right)^3} \left(
        \left(1 - \frac{v^2}{c^2} + \frac{\vec{R}\cdot\vec{a}}{c^2}\right) \left(\vec{n} - \frac{\vec{v}}{c}\right)
        - \left(1 - \dfrac{\vec{n}\cdot\vec{v}}{c} \right) \frac{R}{c^2}\vec{a}
    \right)
$$

$$
\vec{B} = \mathrm{rot\,} \frac{\varphi \vec{v}}{c^2} = \nabla\varphi \times \frac{\vec{v}}{c^2} + \frac{\varphi}{c^2}  \nabla t' \times \vec{a} =
$$

$$
= \frac{q}{4\pi\varepsilon_0 c^2}
\frac{1}{R^2 \left(1 - \dfrac{\vec{n}\cdot\vec{v}}{c} \right)^3} 
\left[ -
\left(
    \vec{n} - 
    \left(1 - \dfrac{\vec{n}\cdot\vec{v}}{c} \right)\dfrac{\vec{v}}{c} - 
    \frac{v^2}{c^2} \vec{n} + 
    \frac{\vec{R}\cdot\vec{a}}{c^2} \vec{n}
\right) \times \vec{v} - 
    \left(1 - \dfrac{\vec{n}\cdot\vec{v}}{c} \right) \frac{R}{c} \vec{n} \times \vec{a}
\right] =
$$

$$
= -\frac{q}{4\pi\varepsilon_0 c^2}
\frac{1}{R^2 \left(1 - \dfrac{\vec{n}\cdot\vec{v}}{c} \right)^3} 
\vec{n}\times\left[
\left(
    1 - 
    \frac{v^2}{c^2} + 
    \frac{\vec{R}\cdot\vec{a}}{c^2}
\right) \vec{v} + 
    \vec{a}\left(1 - \dfrac{\vec{n}\cdot\vec{v}}{c} \right) \frac{R}{c}
\right] = \frac{\vec{n}\times\vec{E}}{c}
$$

## Замечания относительно потенциалов

### Проверка калибровки Лоренца

Проверим, что для потенциалов справедлива калибровка Лоренца, то есть:

$$
\frac{1}{c^2} \frac{\partial \varphi}{\partial t} + \mathrm{div\,} \vec{A} = 0
$$

$$
\frac{\partial \varphi}{\partial t} = - \frac{q}{4\pi \varepsilon_0} \frac{1}{R^2 \left(1 - \dfrac{\vec{n}\cdot\vec{v}}{c} \right)^3} \left(- \vec{n}\cdot\vec{v} + \frac{v^2}{c} - \frac{\vec{R}\cdot\vec{a}}{c}\right)
$$

$$
\mathrm{div\,} \vec{A} = \frac{\vec{v}\cdot\nabla\varphi + \varphi \vec{a} \cdot \nabla t'}{c^2} = 
$$

$$ = \frac{1}{c^2} \frac{q}{4\pi \varepsilon_0} 
\left[ 
    - \frac{1}{R^2 \left(1 - \dfrac{\vec{n}\cdot\vec{v}}{c} \right)^3}
    \left(\vec{n} - \left(1 - \dfrac{\vec{n}\cdot\vec{v}}{c} \right)\dfrac{\vec{v}}{c} - \frac{v^2}{c^2} \vec{n} + \frac{\vec{R}\cdot\vec{a}}{c^2} \vec{n}\right) \cdot \vec{v} - \frac{1}{c}\frac{\vec{n}\cdot\vec{a}}{R \left(1 - \dfrac{\vec{n}\cdot\vec{v}}{c} \right)^2 }
\right] =
$$

$$ = \frac{1}{c^2} \frac{q}{4\pi \varepsilon_0} \frac{1}{R^2 \left(1 - \dfrac{\vec{n}\cdot\vec{v}}{c} \right)^3}
\left[ 
    - \vec{n}\cdot \vec{v} + \dfrac{v^2}{c} - \dfrac{\vec{n}\cdot\vec{v}}{c} \dfrac{v^2}{c} + \frac{v^2}{c^2} \vec{n}\cdot \vec{v}  - \frac{\vec{R}\cdot\vec{a}}{c^2} \vec{n}\cdot\vec{v} - \left(1 - \dfrac{\vec{n}\cdot\vec{v}}{c} \right)\frac{\vec{R}\cdot\vec{a}}{c}
\right] =
$$

$$ 
= \frac{1}{c^2} \frac{q}{4\pi \varepsilon_0} \frac{1}{R^2 \left(1 - \dfrac{\vec{n}\cdot\vec{v}}{c} \right)^3}
\left[ 
    - \vec{n}\cdot \vec{v} + \dfrac{v^2}{c} - \frac{\vec{R}\cdot\vec{a}}{c}
\right]
$$

Таким образом калибровка Лоренца выполняется.

### Вектор Герца

Можно ли представить потенциалы через вектор Герца? Исследуем этот вопрос.

$$
\vec{A} = \frac{1}{c^2}\frac{\partial \vec{\Pi}}{\partial t}, \qquad
\varphi = - \mathrm{div\,} \vec{\Pi}
$$