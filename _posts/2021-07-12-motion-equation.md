---
layout: page
title: Движение нерелятивистской заряженной частицы в кулоновском поле
---

1. Записать уравнения движения в кулоновском поле в цилиндрической системе координат и найти их общее решение, полагая, что начальная скорость не направлена вдоль отрезка, соединяющего подвижную и неподвижную частицы.

**Решение:**

$$
m \frac{d^2\vec{r}}{dt^2} = k \frac{q Q}{r^3} \vec{r}.
$$

$$
m \frac{d^2 (r \vec{e}_r)}{dt^2} = m \frac{d}{dt} \left(\frac{dr}{dt} \vec{e}_r - r \dot{\theta} \vec{e}_\theta\right) = m \left(\frac{d^2 r}{dt^2} - r \dot{\theta}^2\right) \vec{e}_r - m \left(r \ddot{\theta} + 2 \dot{r} \dot{\theta} \right) \vec{e}_\theta
$$

$$
\begin{cases}
\dfrac{d^2 r}{dt^2} - r\dot{\theta}^2 = k \dfrac{qQ}{m r^2}, \\
\dfrac{d(r^2 \dot{\theta})}{dt} = 0.
\end{cases}
$$

$$
r^2 \dot{\theta} = l, \quad \dot{\theta} = \frac{l}{r^2}. 
$$

$$
\dot{\theta} \frac{d}{d\theta} \left(\dot{\theta} \frac{dr}{d\theta}\right) - \frac{l^2}{r^3} = k \frac{qQ}{mr^2},
$$

$$
\frac{d^2}{d\theta^2} \frac{1}{r} + \frac{1}{r} = - \frac{kqQ}{ml^2} = - \gamma.
$$

$$
\begin{aligned}
& \frac{1}{r} = A \cos (\theta + \alpha) - \gamma, \\
& - \frac{\dot{r}}{r^2} = - A \dot{\theta} \sin (\theta + \alpha).
\end{aligned}
$$

Начальные: 

$$r(t_0) = r_0 \quad \theta(t_0) = \theta_0 \quad \dot{r} (t_0) = \dot{r}_0 \quad  \dot{\theta}(t_0) = \dot{\theta}_0$$​

В результате:

$$
\begin{cases}
\dfrac{1}{r_0} + \gamma = A \cos (\theta_0 + \alpha) = A \cos \beta, \\
\dot{r}_0 = A l \sin (\theta_0 + \alpha) = A l \sin \beta.
\end{cases}
$$

$$
\begin{cases}
\alpha = - \theta_0 + \mathrm{\,arctg\,} \dfrac{r_0 \dot{r}_0}{ l( 1 + \gamma r_0)} = \beta - \theta_0, \\
A = \sqrt{\left(\dfrac{1}{r_0} + \gamma\right)^2 + \left(\dfrac{\dot{r}_0}{l}\right)^2}.
\end{cases}
$$

$$
\frac{1}{r} - \frac{1}{r_0} = A (\cos (\theta + \alpha) - \cos (\theta_0 + \alpha)) = - 2 A \sin (\frac{\theta - \theta_0 }{2} + \beta) \sin (\frac{\theta - \theta_0}{2}) =
$$

$$
= - 2 \left(\dfrac{1}{r_0} + \gamma\right) \left[\sin^2 \frac{\theta - \theta_0 }{2} + \sin (\frac{\theta - \theta_0}{2}) \cos (\frac{\theta - \theta_0}{2}) \mathrm{\,tg\,} \beta \right]
$$

$$
t - t_0 = \int\limits_{\theta_0}^\theta \frac{r^2d\theta}{l} = 
$$

$$
= \int\limits_{\theta_0}^\theta \frac{d \theta}{4l \left(\dfrac{1}{r_0} + \gamma\right)^2 \left[\sin^2 \dfrac{\theta - \theta_0 }{2} + \sin (\dfrac{\theta - \theta_0}{2}) \cos (\dfrac{\theta - \theta_0}{2}) \mathrm{\,tg\,} \beta \right]^2} =
$$

$$
= \int\limits_{\theta_0}^\theta \frac{d \mathrm{\,tg\,} \left(\dfrac{\theta - \theta_0}{2}\right)}{2l \left(\dfrac{1}{r_0} - 2 \left(\dfrac{1}{r_0} + \gamma\right) \left[\mathrm{\,tg\,}^2 \dfrac{\theta - \theta_0 }{2} + \mathrm{\,tg\,} \dfrac{\theta - \theta_0}{2}\mathrm{\,tg\,} \beta \right]\right)^2} =
$$



1. Решить задачу 1, полагая, что частица движется из бесконечности с постоянной скоростью.

1. Рассмотреть случай движения вдоль линии, соединяющей центры частиц.
2. Проанализировать решение задач 1 и 2 и определить все возможные типы траекторий, которые можно наблюдать в системе.
3. Найти минимальное расстояние на которое может приблизиться частица при движении с данной начальной скоростью $v$ и данным прицельным параметром $b$​​ к отталкивающему центру.
4. Найти геометрическое место точек, в которые не может попасть частица частица при движении с данной начальной скоростью $v$ и данным прицельным параметром $b$ к отталкивающему центру.
5. Определить максимальную скорость, которая может быть достигнута при движении частицы из бесконечности с данной начальной скоростью $v$ и данным прицельным параметром $b$​​ в кулоновском поле притяжения. Найти условия при которых скорость равна скорости света.
6. Найти дифференциальное сечение рассеяния.
7. Определить плотность потока частиц при движении их из бесконечности, полагая, что частицы не взаимодействуют между собой.

Уравнения движения:

$$
\begin{aligned}
& \frac{d^2 r}{dt^2} - r \dot{\theta}^2 = k \frac{q_a q_b}{m_a r^2} = \frac{\gamma_{ab} l^2}{r^2}, \\
& r^2 \dot{\theta} = - v b = l.
\end{aligned}
$$

1. Преобразуем уравнение:

   $$
   \dot{\theta} = \frac{l}{r^2}
   $$

$$
\frac{d^2 r}{dt^2} - \frac{l^2}{r^3} = \frac{\gamma_{ab} l^2}{r^2}
$$

$$
\dot{\theta}\frac{d}{d\theta} \left(\dot{\theta} \frac{d r}{d\theta}\right) - \frac{l^2}{r^3} = \frac{\gamma_{ab} l^2}{r^2}
$$

$$
- \frac{l^2}{r^2} \frac{d^2}{d\theta^2} \frac{1}{r} - \frac{l^2}{r^3} = \frac{\gamma_{ab} l^2}{r^2}
$$

$$
\frac{d^2}{d\theta^2} \frac{1}{r} + \frac{1}{r} = - \gamma_{ab}
$$

2. Решение уравнения:

$$
\frac{1}{r} = A \cos (\theta + \alpha) - \gamma_{ab}
$$

3. Начальные:

$$
\begin{aligned}
& 0 = A \cos (\pi + \alpha) - \gamma_{ab}, \\
& - \frac{1}{r^2} \frac{dr}{dt} = - A \sin (\theta + \alpha) \dot{\theta}
\end{aligned}
$$

$$
\frac{dr}{dt} = A l \sin (\pi + \alpha) = - A l \sin \alpha = - v
$$

В результате получаем систему для начальных условий:

$$
\begin{aligned}
& A \cos \alpha = - \gamma_{ab}, \\
& A \sin \alpha = \frac{v}{l}.
\end{aligned}
$$

Откуда:

$$
\mathrm{tg\,} \alpha = - \frac{v}{\gamma_{ab} l} = \frac{1}{\gamma_{ab} b}, \qquad A = \sqrt{\gamma_{ab}^2 + \frac{v^2}{l^2}}.
$$

$$
\frac{1}{r} = - \gamma_{ab} \frac{\cos (\theta + \alpha) + \cos \alpha}{\cos \alpha} = - \gamma_{ab} \frac{2 \cos \left(\alpha + \frac{\theta}{2}\right) \cos \frac{\theta}{2}}{\cos \alpha} = - 2 \gamma_{ab} \left[\cos^2 \frac{\theta}{2} - \sin \frac{\theta}{2} \cos \frac{\theta}{2} \mathrm{\,tg\,} \alpha\right] =
$$

$$
=  2 \gamma_{ab}  \cos^2 \frac{\theta}{2} - \sin \frac{\theta}{2} \cos \frac{\theta}{2} \frac{2}{b}
$$

$$
b = \dfrac{r \sin \theta}{2 \gamma_{ab} r \cos^2 \frac{\theta}{2} - 1}
$$

|                 $ \theta = \pi - \delta $                  |                $ \theta = - \pi + \delta $                 |
| :----------------------------------------------------------: | :----------------------------------------------------------: |
| $ \frac{1}{r} = - \gamma_{ab} \frac{2 \sin \left(\frac{\delta}{2} - \alpha\right) \sin \frac{\delta}{2}}{\cos \alpha}, \qquad \delta > 0. $ | $ \frac{1}{r} = - \gamma_{ab} \frac{2 \sin \left(\frac{\delta}{2} + \alpha\right) \sin \frac{\delta}{2}}{\cos \alpha}, \qquad \delta > 0. $​ |

| $\gamma_{ab} > 0, b > 0$           | $\gamma_{ab} > 0, b < 0$ ​              | $\gamma_{ab} < 0, b > 0$ ​              | $\gamma_{ab} < 0, b < 0$ ​          |
| ---------------------------------- | -------------------------------------- | -------------------------------------- | ---------------------------------- |
| $\alpha \in (0, \pi/2)$            | $\alpha \in (-\pi/2, 0)$               | $\alpha \in (-\pi/2, 0)$               | $\alpha \in (0, \pi/2)$            |
| $\theta \in (\pi, \pi - 2 \alpha)$ | $\theta \in (- \pi, - \pi - 2 \alpha)$ | $\theta \in (- \pi, - \pi - 2 \alpha)$ | $\theta \in (\pi, \pi - 2 \alpha)$ |

$$
\theta \in (\pi \mathrm{\,sgn\,} \alpha, (\pi - 2 |\alpha|) \mathrm{\,sgn\,} \alpha), \quad \alpha \in (-\pi/2, \pi/2)
$$

Время в зависимости от угла:

$$
\frac{dt}{d\theta} = \frac{1}{\dot{\theta}} = \frac{r^2}{l} = \frac{1}{\gamma_{ab}^2 l} \frac{\cos^2 \alpha}{(\cos(\theta + \alpha) + \cos \alpha)^2} = \frac{1}{\gamma_{ab}^2 l} \frac{\cos^2 \alpha}{4 \cos^2 \left(\alpha + \frac{\theta}{2}\right) \cos^2 \frac{\theta}{2}}
$$

$$
dt = \frac{1}{2\gamma_{ab}^2 l} \frac{\left(1 + \mathrm{\,tg\,}^2 \frac{\theta}{2}\right)d \mathrm{\,tg\,} \frac{\theta}{2}}{\left(1 - \mathrm{\,tg\,} \alpha \mathrm{\,tg\,} \frac{\theta}{2}\right)^2}
$$

$$
\int \frac{1 + s^2}{(1 - a s)^2} ds = \int \frac{1 + \frac{(1 - as)^2}{a^2} + 2 \frac{s}{a} - \frac{1}{a^2}}{(1 - a s)^2} ds =
$$

$$
= \int \frac{1 + \frac{(1 - as)^2}{a^2} + 2 \frac{(a s - 1)}{a^2} + \frac{1}{a^2}}{(1 - a s)^2} ds = 
$$

$$
= \frac{s}{a^2} + \frac{1}{a^3} \frac{1 + a^2}{1 - a s} + \frac{2}{a^3} \ln (1 - as)
$$

$$
t = \frac{1}{2\gamma_{ab}^2 l} \left[\frac{\mathrm{tg\,}\frac{\theta}{2}}{\mathrm{tg\,}^2\alpha} + \frac{\cos^2 \alpha \cos \frac{\theta}{2}}{\sin^3\alpha \cos(\alpha + \frac{\theta}{2})} + \frac{2}{\mathrm{tg\,}^3 \alpha} \ln \frac{\cos(\alpha + \frac{\theta}{2})}{\cos \alpha \cos \frac{\theta}{2}}\right] + const
$$

$$
t = - \frac{\gamma_{ab}^3 b^3}{2 \gamma_{ab}^2 v b} \left[\frac{\mathrm{tg\,}\frac{\theta}{2}}{\gamma_{ab} b} + \frac{1}{1 - \dfrac{\mathrm{tg\,}\frac{\theta}{2}}{\gamma_{ab} b}} + 2 \ln \left(1 - \dfrac{\mathrm{tg\,}\frac{\theta}{2}}{\gamma_{ab} b}\right) \right] + const =
$$

$$
= - \frac{\gamma_{ab} b^2}{2 v} \left[\frac{\mathrm{tg\,}\frac{\theta}{2}}{\gamma_{ab} b} + \frac{1}{1 - \dfrac{\mathrm{tg\,}\frac{\theta}{2}}{\gamma_{ab} b}} + 2 \ln \left(1 - \dfrac{\mathrm{tg\,}\frac{\theta}{2}}{\gamma_{ab} b}\right) \right] + const
$$

Пусть из бесконечности к рассеивающему центру движется поток частиц. На бесконечности плотность потока $$n_0$$​, найдём, полагая, что частицы потока не взаимодействуют друг с другом плотность потока во всех точках пространства:

$$
2 \pi n_0 b v\,dt\,db = 2 \pi n r^2 \sin \theta \, d\theta \, dr
$$

$$
n = n_0 \frac{b v}{r^2} \frac{\partial (t , b)}{\partial (\theta, r)} = \frac{n_0 b v}{r^2} \begin{vmatrix} \left[\dfrac{\partial t}{\partial \theta} \right]_r & \left[\dfrac{\partial t}{\partial r} \right]_\theta \\ \left[\dfrac{\partial b}{\partial \theta}\right]_r & \left[\dfrac{\partial b}{\partial r}\right]_\theta\end{vmatrix} =
$$

$$
= \frac{n_0 b v}{r^2} \begin{vmatrix} \left[\dfrac{\partial t}{\partial \theta} \right]_b \left[\dfrac{\partial \theta}{\partial \theta} \right]_r + \left[\dfrac{\partial t}{\partial b} \right]_\theta \left[\dfrac{\partial b}{\partial \theta} \right]_r & \left[\dfrac{\partial t}{\partial \theta} \right]_b \left[\dfrac{\partial \theta}{\partial r} \right]_\theta + \left[\dfrac{\partial t}{\partial b} \right]_\theta \left[\dfrac{\partial b}{\partial r} \right]_\theta \\ \left[\dfrac{\partial b}{\partial \theta}\right]_r & \left[\dfrac{\partial b}{\partial r}\right]_\theta\end{vmatrix} =
$$

$$
= \frac{n_0 b v}{r^2} \begin{vmatrix} \left[\dfrac{\partial t}{\partial \theta} \right]_b \left[\dfrac{\partial \theta}{\partial \theta} \right]_r & \left[\dfrac{\partial t}{\partial \theta} \right]_b \left[\dfrac{\partial \theta}{\partial r} \right]_\theta \\ \left[\dfrac{\partial b}{\partial \theta}\right]_r & \left[\dfrac{\partial b}{\partial r}\right]_\theta\end{vmatrix} = \frac{n_0 b v}{r^2} \left[\dfrac{\partial t}{\partial \theta} \right]_b \begin{vmatrix} 1 & 0 \\ \left[\dfrac{\partial b}{\partial \theta}\right]_r & \left[\dfrac{\partial b}{\partial r}\right]_\theta\end{vmatrix} =
$$

$$
= \frac{n_0 b v}{r^2} \left[\dfrac{\partial t}{\partial \theta} \right]_b \left[\dfrac{\partial b}{\partial r}\right]_\theta = \frac{n_0 b v}{r^2 \dot{\theta}} \left[\dfrac{\partial}{\partial r} \left(\dfrac{r \sin \theta}{2 \gamma_{ab} r \cos^2 \frac{\theta}{2} - 1}\right)\right]_\theta =
$$

$$
= - n_0 \dfrac{\partial}{\partial r} \left(\dfrac{(2 \gamma_{ab} r \cos^2 \frac{\theta}{2} - 1) \sin \theta - 2 \gamma_{ab} r \cos^2 \frac{\theta}{2} \sin \theta }{(2 \gamma_{ab} r \cos^2 \frac{\theta}{2} - 1)^2}\right) =
$$

$$
= \frac{n_0 \sin \theta}{(2 \gamma_{ab} r \cos^2 \frac{\theta}{2} - 1)^2}
$$

**Ещё одна "недоделка", я хотел посчитать одно, а невесть сколько времени решал другое...**

