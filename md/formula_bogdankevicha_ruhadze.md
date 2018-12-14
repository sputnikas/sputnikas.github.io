# Формула Богданкевича-Рухадзе

Рассмотрим систему, представленную на рисунке 1. Трубчатый поток с внутренним радиусом $r_b$ и внешним радиусом $r_a$ находится в идеально проводящей заземлённой трубе радиуса $R$. Ток потока равен $I$, поток будем считать однородным. Продольное магнитное поле пусть будет бесконечным. Тогда поперечные скорости для электронов будут приводить к наличию бесконечных сил в поперечном сечении. Поэтому будем считать их равными нулю.

Поток однороден. Симметрия задачи приводит к уравнению Пуассона:

$$
\Delta \varphi = \frac{1}{r} \frac{\partial}{\partial r} \left( r\frac{\partial \varphi}{\partial r} \right) = - \frac{\rho}{\varepsilon_0}
$$

Его решения в областях 1, 2, 3 имеют вид:

$$
E_r^{(1)} = - \frac{C_1^{(1)}}{r}, 
\qquad 
\varphi^{(1)} = C_1^{(1)} \ln \frac{r}{R} 
$$
$$
E_r^{(2)} = \frac{\rho}{\varepsilon_0} \frac{r}{2} - \frac{C_1^{(2)}}{r}, 
\qquad
\varphi^{(2)} = - \frac{\rho}{\varepsilon_0} \frac{r^2}{4} + C_1^{(2)} \ln \frac{r}{R} + C_2^{(2)} 
$$
$$
E_r^{(3)} = 0, 
\qquad
\varphi^{(3)} = C_2^{(3)}
$$

Воспользуемся непрерывностью потенциала и поля на границах $r_a$, $r_b$, получим:

$$
C_1^{(2)} - C_1^{(1)} = \frac{\rho}{\varepsilon_0} \frac{r_a^2}{2}
$$
$$
\frac{\rho}{\varepsilon_0} \frac{r^2_a}{4} = (C_1^{(2)} - C_1^{(1)}) \ln \frac{r_a}{R} +C_2^{(2)}
$$
$$
C_1^{(2)} = \frac{\rho}{\varepsilon_0} \frac{r^2_b}{2}
$$

Отсюда следует:

$$
C_1^{(1)} = \frac{\rho}{\varepsilon_0} \frac{r^2_b - r^2_a}{2}
$$
$$
C_1^{(2)} = \frac{\rho}{\varepsilon_0} \frac{r^2_b}{2}
$$
$$
C_2^{(2)} = \frac{\rho}{\varepsilon_0} \frac{r^2_a}{4} (1 - 2 \ln \frac{r_a}{R})
$$

Потенциал достигает экстремума на границе $r = r_b$:

$$
\varphi_{ext} = - \frac{\rho}{\varepsilon_0} \frac{r^2_b}{4} + \frac{\rho}{\varepsilon_0} \frac{r^2_b}{2} \ln \frac{r_b}{R} + \frac{\rho}{\varepsilon_0} \frac{r^2_a}{4} (1 - 2 \ln \frac{r_a}{R}) =
$$
$$
= \frac{\rho}{\varepsilon_0} \frac{r_a^2 - r^2_b}{4} + \frac{\rho}{2 \varepsilon_0} \left( r^2_b \ln \frac{r_b}{R} - r^2_a \ln \frac{r_a}{R} \right) = \frac{\alpha \rho}{4\varepsilon_0}
$$

Здесь $\alpha$ некоторая константа, зависящая только от геометрических параметров потока и системы, но не зависящая от тока или $\rho$. Запишем закон сохранения энергии для одного электрона потока, считая, что он начинает своё движение с заземлённого катода и обладает лоренц-фактором $\gamma$:

$$
mc^2 \gamma = \frac{mc^2}{\sqrt{1 - \frac{v_z^2}{c^2}}} + q\varphi
$$

Введём обозначение для сокращения выкладок $\varphi' = q\varphi/mc^2 > 0$ и выразим отсюда $v_z$:

$$
\frac{1}{1 - \frac{v_z^2}{c^2}} = (\varphi' - \gamma)^2
$$
$$
\frac{1}{(\varphi' - \gamma)^2} = 1 - \frac{v_z^2}{c^2}
$$
$$
v_z = c \sqrt{1 - \frac{1}{(\varphi' - \gamma)^2}} = c \frac{\sqrt{(\varphi' - \gamma)^2 - 1}}{\gamma - \varphi' }
$$

Далее рассмотрим выражение для тока через потенциал:

$$
I = \rho v_z \pi (r^2_a - r^2_b) = \frac{4\varepsilon_0 mc^3}{q \alpha} \pi (r^2_a - r^2_b) \varphi' \frac{\sqrt{(\varphi' - \gamma)^2 - 1}}{\gamma - \varphi' }
$$

Можно показать, что для него существует экстремум. Действительно:

$$
\frac{\partial I}{\partial \varphi'} \sim \frac{\sqrt{(\varphi' - \gamma)^2 - 1}}{\gamma - \varphi' } + \frac{\sqrt{(\varphi' - \gamma)^2 - 1}}{(\gamma - \varphi')^2} \varphi' + \varphi'\frac{\varphi' - \gamma}{(\gamma - \varphi' )\sqrt{(\varphi' - \gamma)^2 - 1}} =
$$
$$
= \frac{\sqrt{(\varphi' - \gamma)^2 - 1}}{(\gamma - \varphi')^2} \gamma - \frac{\varphi'}{\sqrt{(\varphi' - \gamma)^2 - 1}} = 
$$
$$
= \frac{(\varphi' - \gamma)^2 \gamma - \gamma - \varphi'(\gamma - \varphi')^2}{(\gamma - \varphi')^2\sqrt{(\varphi' - \gamma)^2 - 1}} = 0
$$

Отсюда:

$$
\gamma - \varphi' = \gamma^{1/3}
$$

$$
\varphi' = \gamma - \gamma^{1/3}
$$

Подставляя данное значение в выражение для тока получаем:

$$
I = \rho v_z \pi (r^2_a - r^2_b) = \frac{4\varepsilon_0 mc^3}{q \alpha} \pi (r^2_a - r^2_b) (\gamma - \gamma^{1/3}) \frac{\sqrt{\gamma^{2/3} - 1}}{\gamma^{1/3} } = 
\frac{4\varepsilon_0 mc^3}{q \alpha} \pi (r^2_a - r^2_b) (\gamma^{2/3} - 1)^{3/2}
$$

Разберёмся теперь с константой $\alpha$. Прежде всего нас интересует не сама $\alpha$, а выражение:

$$
\frac{r^2_a - r^2_b}{\alpha} = \frac{r^2_a - r^2_b}{(r_a^2 - r^2_b) + 2 \left( r^2_b \ln \frac{r_b}{R} - r^2_a \ln \frac{r_a}{R} \right)} = \frac{1}{1 - \cfrac{\left( r^2_a \ln \cfrac{r_a^2}{R^2} -  r^2_b \ln \cfrac{r_b^2}{R^2}\right)}{r^2_a - r^2_b}} = (1)
$$

Предположим теперь, что $r_a = r_b + d$. Заметим, что в знаменателе стоит выражение вида:

$$
\frac{f(b) - f(a)}{b - a} = f'(a) + f''(a) \frac{b - a}{2} + f'''(a) \frac{(b - a)^2}{6} + \ldots
$$

Для функции:

$$
f(x) = x \ln \frac{x}{R^2}
$$

$$
f'(x) = \ln \frac{x}{R^2} + 1
,\qquad
f''(x) = \frac{1}{x}, \qquad \ldots
$$

В результате получаем:

$$
(1) = \frac{1}{1 - \ln \cfrac{r_b^2}{R^2} - 1 - \cfrac{r_a^2 - r_b^2}{2 r_b^2} - \ldots} = 
$$
$$
 = - \frac{1}{2 \ln \cfrac{r_b}{R} + \cfrac{2 d r_b + d^2}{2 r_b^2} + \ldots} = 
$$
$$
 \approx - \frac{1}{\cfrac{d}{r_b} + 2 \ln \cfrac{r_b}{R}} = 
 \frac{1}{- \cfrac{d}{r_b} + 2 \ln \cfrac{R}{r_b}}
$$

Представляет интерес также получить разложение в окрестности $r = r_a$. В данном случае ряд Тейлора не изменится, но:

$$
(1) = \frac{1}{1 - \ln \cfrac{r_a^2}{R^2} - 1 - \cfrac{r_b^2 - r_a^2}{2 r_a^2} - \ldots}
$$
$$
 = \frac{1}{2 \ln \cfrac{R}{r_a} + \cfrac{2 d r_a - d^2}{2 r_a^2} + \ldots} \approx 
$$
$$
 = \frac{1}{\cfrac{d}{r_a} + 2 \ln \cfrac{R}{r_a}}
$$

Интересно отметить, что в оригинальном выражении (1) замена $r_a \to r_b$ выражения не меняла, в то время как в результате замена видоизменяет знаки в знаменателе. Именно с последней формой выражения (1) формула и получила название формулы Богданкевича-Рухадзе:

$$
I = 
\frac{4\pi\varepsilon_0 mc^3}{q} \frac{(\gamma^{2/3} - 1)^{3/2}}{\cfrac{d}{r_a} + 2 \ln \cfrac{R}{r_a}} 
$$