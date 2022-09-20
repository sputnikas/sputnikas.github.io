---
layout: page
title: Разные уравнения
---

# Разные уравнения

Моя коллекция уравнений, которые нужно решить со временем только множится. Здесь для себя будущего  я бы хотел собрать некоторые из них, чтобы никогда не забывать о невыполненном (надо же чтобы меня весь остаток жизни терзала совесть - что я такой дебил, не смог решить такие простые задачи).

**Электронные пучки в пустоте между электродами произвольной формы - гидродинамический подход**. Ну вы конечно знаете эти замечательные уравнения, они так же прекрасны, как девушки, звёзды, огонь, вода и майское утро. Уравнения Максвелла + уравнения движения - всё просто, но я их не решил!

$$
\begin{aligned}
& \mathrm{div\,} \vec{E} = \frac{\rho}{\varepsilon_0}, \\
& \mathrm{rot\,} \vec{E} = - \frac{\partial \vec{B}}{\partial t}, \\
& \mathrm{div\,} \vec{B} = 0, \\
& \mathrm{rot\,} \vec{B} = \mu_0 \vec{j} +\frac{1}{c^2} \frac{\partial \vec{E}}{\partial t}, \\
& \gamma \frac{\partial \vec{u}}{\partial t} + \vec{u}\cdot \nabla \vec{u} = \frac{q}{m} [\gamma \vec{E} + \vec{u}\times\vec{B}], \\
& \gamma \frac{\partial \gamma}{\partial t} + \vec{u}\cdot \nabla \gamma = \frac{q}{m c^2} \vec{u}\cdot\vec{E}, \\
& \vec{j} = \rho \frac{\vec{u}}{\gamma}.
\end{aligned}
$$

Если ввести плотность в мгновенной системе координат, отнесённую к электрической постоянной, $\tilde{\rho} = \rho/(\varepsilon_0\gamma)$, магнитное поле измерять в вольтах на метр ($c\vec{B}$ заменить на $\vec{B}$) и импульс единицы массы отнести  к скорости света ($\vec{u}/c$  заменить на $\vec{u}$ )  уравнения принимают замечательный симметричный вид:

$$
\begin{aligned}
& \mathrm{div\,} \vec{E} = \tilde{\rho} \gamma, \\
& \mathrm{rot\,} \vec{E} = - \frac{1}{c} \frac{\partial \vec{B}}{\partial t}, \\
& \mathrm{div\,} \vec{B} = 0, \\
& \mathrm{rot\,} \vec{B} = \tilde{\rho} \vec{u} +\frac{1}{c} \frac{\partial \vec{E}}{\partial t}, \\
& \frac{\gamma}{c} \frac{\partial \vec{u}}{\partial t} + \vec{u}\cdot \nabla \vec{u} = \frac{q}{m c^2} [\gamma \vec{E} + \vec{u}\times\vec{B}], \\
& \frac{\gamma}{c} \frac{\partial \gamma}{\partial t} + \vec{u}\cdot \nabla \gamma = \frac{q}{m c^2} \vec{u}\cdot\vec{E}.
\end{aligned}
$$

Последнее уравнение можно не записывать, оно следствие релятивистского соотношения:

$$
\gamma^2 = 1 + u^2
$$

Уравнения непрерывности выполняются автоматически. Отсюда можно получить линейную релятивистскую теорию малого сигнала, справедливую в больших магнитных продольных полях, удивиться  тому, насколько она похожа на нерелятивистскую, сделать ещё массу других удивительных вещей, но, увы, не приблизиться к решению задачи при больших плотностях, когда образуется такая замечательная штука как ***виртуальный катод***. 

К сожалению, даже в случае линейной теории при самых простых граничных цилиндрического волновода для пучков с круглым сечением решить это чудо уже не просто. По крайней мере для меня! *Бесселя от корней и корней Бесселя веселят наши души и греют, их решения так ненавистны не зря, их анализ не прост, он чернее угля, и в студентах страдания сеет.*

У них есть обобщение. Первая идея появилась давно, развивается до сих пор и приводит к ***двухпучковой неустойчивости***, ну помните такое, берём и говорим, что вместо одной скорости в каждой точке существует две - туда и обратно, и две плотности - туда и обратно. Так можно поступить только, если есть некоторое условие, как в данном случае на скорость. Но в общем виде задача всё же может быть записана. Проще всего записать уравнения Максвелла:

$$
\begin{aligned}
& \mathrm{div\,} \vec{E} = \tilde{\rho}_+ \gamma_+ + \tilde{\rho}_- \gamma_-, \\
& \mathrm{rot\,} \vec{E} = - \frac{1}{c} \frac{\partial \vec{B}}{\partial t}, \\
& \mathrm{div\,} \vec{B} = 0, \\
& \mathrm{rot\,} \vec{B} = \tilde{\rho}_+ \vec{u}_+ + \tilde{\rho}_- \vec{u}_- +\frac{1}{c} \frac{\partial \vec{E}}{\partial t}.
\end{aligned}
$$

Сложнее всё будет с уравнениями движения и уравнениями непрерывности. Особенность в том, что один тип частиц ("движущихся туда") при определённых условиях переходит в другой тип частиц ("движущихся обратно"). Этот факт, а главное точный вид зависимости одних функций от других необходимо как-то учесть. Вариант заключается в том, чтобы ввести некоторые функции $$Q_+(\tilde{\rho}_+, \vec{u}_+, \gamma_+) $$ и $$ Q_-(\tilde{\rho}_-, \vec{u}_-, \gamma_-) $$, которые имели бы смысл числа частиц в единицах $$\tilde{\rho}$$ в единицу времени, переходящих в другую группу. Тогда:

$$
\begin{aligned}
& \frac{1}{c} \frac{\partial \tilde{\rho}_+ \gamma_+}{\partial t} + \mathrm{div\,} (\tilde\rho_+ \vec{u}_+) = Q_-(\tilde{\rho}_-, \vec{u}_-, \gamma_-) - Q_+(\tilde{\rho}_+, \vec{u}_+, \gamma_+), \\
& \frac{1}{c} \frac{\partial \tilde{\rho}_- \gamma_-}{\partial t} + \mathrm{div\,} (\tilde\rho_- \vec{u}_-) = Q_+(\tilde{\rho}_+, \vec{u}_+, \gamma_+) - Q_-(\tilde{\rho}_-, \vec{u}_-, \gamma_-) .
\end{aligned}
$$

Тогда сумма двух данных уравнений даст правильный вид уравнения непрерывности. Отметим, что переход частиц из одного вида в другой приводит также к изменению импульса единицы объёма. Чтобы учесть это изменение, перейдём к уравнению, описывающее изменение импульса и энергии в однокомпонентной системе:

$$
\begin{aligned}
& \frac{\tilde{\rho}\gamma}{c} \frac{\partial \vec{u}}{\partial t} + \tilde{\rho}\vec{u}\cdot \nabla \vec{u} = \frac{q \tilde{\rho}}{m c^2} [\gamma \vec{E} + \vec{u}\times\vec{B}], \\
& \frac{\tilde{\rho} \gamma}{c} \frac{\partial \gamma}{\partial t} + \tilde{\rho} \vec{u}\cdot \nabla \gamma = \frac{q \tilde{\rho}}{m c^2} \vec{u}\cdot\vec{E}.
\end{aligned}
$$

Отдельно в данном случае выпишем уравнение непрерывности

$$
\frac{1}{c} \frac{\partial \tilde{\rho} \gamma}{\partial t} + 
\nabla \cdot (\tilde{\rho} \vec{u}) = 0
$$

умножаем последовательно на $\vec{u}$ и $\gamma$, и складываем с каждым из уравнений выше, получаем  закон сохранения для величин импульса в единицах $\tilde{\rho}$ и энергии в тех же единицах, суммируем - в результате мы получаем закон сохранения в форме:

$$
\begin{aligned}
& \frac{1}{c} \frac{\partial (\tilde{\rho}\gamma \vec{u})}{\partial t} + \nabla\cdot(\tilde{\rho}\vec{u}\vec{u}) = \frac{q \tilde{\rho}}{m c^2} [\gamma \vec{E} + \vec{u}\times\vec{B}], \\
& \frac{1}{c} \frac{\partial (\tilde{\rho} \gamma^2)}{\partial t} + \nabla\cdot(\tilde{\rho} \gamma \vec{u}) = \frac{q \tilde{\rho}}{m c^2} \vec{u}\cdot\vec{E}.
\end{aligned}
$$

Так как физический смысл $ Q_\pm $ - число частиц в единицах $ \tilde{\rho} $ переходящих из типа "+" в тип "-" в единицу времени в данной точке, то изменение  импульса связанное с этим переходом можно представить в эквивалентном виде, аналогичном по форме закону сохранения числа частиц в единицах $\tilde{\rho}$ выше. 

$$
\begin{aligned}
& \frac{1}{c} \frac{\partial (\tilde{\rho}_\pm \gamma_\pm \vec{u}_\pm)}{\partial t} + \nabla\cdot(\tilde{\rho}_\pm\vec{u}_\pm\vec{u}_\pm) = \frac{q \tilde{\rho}_\pm}{m c^2} [\gamma_\pm \vec{E} + \vec{u}_\pm\times\vec{B}] \pm [Q_-(\tilde{\rho}_-, \vec{u}_-, \gamma_-) \vec{u}_- - Q_+(\tilde{\rho}_+, \vec{u}_+, \gamma_+) \vec{u}_+], \\
& \frac{1}{c} \frac{\partial (\tilde{\rho}_\pm \gamma^2_\pm)}{\partial t} + \nabla\cdot(\tilde{\rho}_\pm \gamma_\pm \vec{u}_\pm) = \frac{q \tilde{\rho}_\pm}{m c^2} \vec{u}_\pm\cdot\vec{E} \pm [Q_-(\tilde{\rho}_-, \vec{u}_-, \gamma_-) \gamma_- - Q_+(\tilde{\rho}_+, \vec{u}_+, \gamma_+) \gamma_+].
\end{aligned}
$$

Данные уравнения с учётом соотношений непрерывности могут быть упрощены:

$$
\begin{aligned}
& \frac{\tilde{\rho}_\pm \gamma_\pm }{c} \frac{\partial \vec{u}_\pm}{\partial t} + \tilde{\rho}_\pm\vec{u}_\pm\cdot\nabla\vec{u}_\pm 
\pm [ Q_-(\tilde{\rho}_-, \vec{u}_-, \gamma_-) - Q_+(\tilde{\rho}_+, \vec{u}_+, \gamma_+) ]  \vec{u}_\pm
= \\ 
& \qquad = \frac{q \tilde{\rho}_\pm}{m c^2} [\gamma_\pm \vec{E} + \vec{u}_\pm\times\vec{B}] \pm [Q_-(\tilde{\rho}_-, \vec{u}_-, \gamma_-) \vec{u}_- - Q_+(\tilde{\rho}_+, \vec{u}_+, \gamma_+) \vec{u}_+], \\
& \frac{\tilde{\rho}_\pm \gamma_\pm }{c} \frac{\partial \vec{u}_\pm}{\partial t} + \tilde{\rho}_\pm\vec{u}_\pm\cdot\nabla\vec{u}_\pm = \frac{q \tilde{\rho}_\pm}{m c^2} [\gamma_\pm \vec{E} + \vec{u}_\pm\times\vec{B}] \pm Q_\mp(\tilde{\rho}_\mp, \vec{u}_\mp, \gamma_\mp) [\vec{u}_- -\vec{u}_+], \\
& \frac{\tilde{\rho}_\pm \gamma_\pm}{c} \frac{\partial \gamma_\pm}{\partial t} + \tilde{\rho}_\pm \vec{u}_\pm \cdot \nabla \gamma_\pm = \frac{q \tilde{\rho}_\pm}{m c^2} \vec{u}_\pm\cdot\vec{E} \pm Q_\mp(\tilde{\rho}_\mp, \vec{u}_\mp, \gamma_\mp) [\gamma_- -\gamma_+].
\end{aligned}
$$

Главный вопрос заключается в виде функции $Q_\pm$.  Так, например, можно рассмотреть равенство:

$$
Q_\pm = r_\pm(\vec{r}, t) \tilde{\rho}_\pm \gamma_\pm \delta(\vec{u}_\pm\cdot\vec{n})
$$

Здесь $\vec{n}$ - нормаль к некоторой поверхности в данной точке. Переход происходит только при нулевой скорости на данной поверхности. Вид коэффициента ещё предстоит установить. Для этого обратим внимание на свойства дельта-функции:

$$
Q_\pm = r_\pm \tilde{\rho}_\pm \gamma_\pm \sum\limits_{k,\,\,\, t_k: \vec{u}(\vec{r}, t_k)\cdot\vec{n} = 0} \frac{\delta(t - t_k)}{|\partial (\vec{u}_\pm \cdot \vec{n})/\partial t|_{t_k}}
$$

Проинтегрировав в окрестности $$t_k$$, мы автоматически получим физический смысл коэффициента $$\tilde{r}_\pm = r_\pm/(\lvert\partial (\vec{u}_\pm \cdot \vec{n})/\partial t\rvert_{t_k})$$  - он показывает долю частиц типа $$\pm$$ переходящих в тип $$\mp$$. Таким образом, число частиц данного типа в некоторой окрестности данной точки определяется потоком частиц данного типа из-за пределов окрестности данной точки и переходами частиц из одного типа в другой. Разделяя эти два процесса, можно положить, что вплоть до момента равенства 0 скорости движения частиц выполняется уравнение непрерывности с нулевой правой частью, а после происходит скачкообразное изменение плотности частиц в единицах $$\tilde{\rho}$$:

$$
\tilde{\rho}_\pm \gamma_\pm \rvert_{t_k + 0} = 
\left[ \tilde{\rho}_\pm \gamma_\pm \pm (\tilde{r}_- \tilde{\rho}_- \gamma_- - \tilde{r}_+ \tilde{\rho}_+ \gamma_+) \right]_{t_k - 0}
$$

Сами коэффициенты $$\tilde{r}_\pm$$ представляют собой, таким образом, коэффициенты отражения частиц данного типа от соответствующей поверхности. Величина коэффициентов в рамках данного подхода остаётся неизвестной.

## Одномерная модель потока - сеточные методы

Рассмотрим одномерный случай - случай широких электронных пучков. Будем исследовать уравнения до образования виртуального катода сеточными методами. Уравнения:

$$
\begin{aligned}
& E_x = E_y = B_x = B_y = 0, B_z = const, \\
& \frac{\partial}{\partial x},  \frac{\partial}{\partial y} = 0, \\
& \frac{\partial E_z}{\partial z} = \tilde{\rho} \gamma, \\
& 0 = \tilde{\rho} u_z +\frac{1}{c} \frac{\partial E_z}{\partial t}, \\
& \frac{\gamma}{c} \frac{\partial u_z}{\partial t} + u_z \frac{\partial u_z}{\partial z} = \frac{q}{m c^2} \gamma (E_z + E_z^{ex}), \\
& \frac{\gamma}{c} \frac{\partial \gamma}{\partial t} + u_z \frac{\partial \gamma}{\partial z} = \frac{q}{m c^2} u_z (E_z + E_z^{ex}).
\end{aligned}
$$

Здесь $E_z^{ex}$ - внешнее электрическое поле, определяемое потенциалами на обкладках. Мы будем полагать, что начальная скорость электронов пучка $u_z\rvert_{z=0} = u_{0z}(t)$, длина пространства взаимодействия $l$. Следует также учесть, что $q$ - есть функция координаты, равная заряду частицы внутри потока, и равная 0 вне потока. Наконец зададим величину плотности $\tilde{\rho}\rvert_{z=0}=\tilde{\rho}_0(t)$. Очевидно, что в плоскости влёта мы имеем для $E_z$ выражение:

$$
E_z|_{z=0} = - \int\limits_{-\infty}^t \tilde{\rho}(t')u_{0z}(t') dt'
$$


