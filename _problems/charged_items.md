---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

title: Заряженные тела
layout: theory_page
permalink: /charged_items/
---

# Электростатика

## Однородно заряженный шар

$Q$ - заряд шара, $a$ - радиус. Сферическая симметрия задачи приводит к теореме Гаусса вне шара:

$$
E_r 4\pi r^2 = \frac{Q}{\varepsilon_0}
$$

внутри шара:

$$
E_r 4\pi r^2 = \frac{Q}{\varepsilon_0} \frac{r^3}{a^3}
$$

Линии поля, очевидно, - прямые выходящие из центра, эквипотенциали - сферы с центром в центре шара. Вне шара имеем закон Кулона, внутри шара поле меняется пропорционально расстоянию от центра:

$$
E_r = \begin{cases}
\dfrac{Q}{4\pi\varepsilon_0} \dfrac{1}{r^2}, \qquad r \geq a \\
\dfrac{Q}{4\pi\varepsilon_0} \dfrac{r}{a^3}, \qquad r < a
\end{cases}
$$

Потенциал полагаем равным 0 на бесконечности:

$$
\varphi = \int\limits_r^\infty E_r dr = \begin{cases}
\dfrac{Q}{4\pi\varepsilon_0} \dfrac{1}{r}, \qquad r \geq a \\
\dfrac{Q}{4\pi\varepsilon_0} \left(\dfrac{a^2}{2 a^3} - \dfrac{r^2}{2 a^3}\right) + \dfrac{Q}{4\pi\varepsilon_0} \dfrac{1}{a}, \qquad r < a
\end{cases} = 
$$

$$
= \begin{cases}
\dfrac{Q}{4\pi\varepsilon_0} \dfrac{1}{r}, \qquad r \geq a \\
\dfrac{Q}{4\pi\varepsilon_0} \dfrac{3 a^2 - r^2}{2 a^3}, \qquad r < a
\end{cases}
$$

Для анализа мы обозначим потенциал на поверхности шара $\varphi_0 = Q/4\pi\varepsilon_0a$, поле на поверхности шара $E_0 = \varphi_0/a$ и обезразмерим расстояние $x = r/a$:

$$
\frac{\varphi}{\varphi_0} =  \begin{cases}
\dfrac{1}{x}, \qquad x \geq 1 \\
\dfrac{3 - x^2}{2}, \qquad x < 1
\end{cases}
$$

$$
\frac{E_r}{E_0} = \begin{cases}
\dfrac{1}{x^2}, \qquad x \geq 1 \\
x, \qquad x < 1
\end{cases}
$$

<div style="text-align:center"><img src="/problems/charged_items_img_001.png" /></div>

## Однородно заряженная сфера

Очевидно, что все предположения относительно шара имеют место и для сферы:

$$
\frac{\varphi}{\varphi_0} =  \begin{cases}
\dfrac{1}{x}, \qquad x \geq 1 \\
1, \qquad x < 1
\end{cases}
$$

$$
\frac{E_r}{E_0} = \begin{cases}
\dfrac{1}{x^2}, \qquad x \geq 1 \\
0, \qquad x < 1
\end{cases}
$$

Разрыв поля, как и должно быть, приводит к поверхностной плотности:

$$
\sigma = \varepsilon_0(E_r|_{a+} - E_r|_{a-}) = \frac{Q}{4\pi a^2}
$$

<div style="text-align:center"><img src="/problems/charged_items_img_002.png" /></div>