---
layout: page
title: Задача о проводящем тетраэдре
---

Требуется найти сопротивление участка цепи 1-2 $R_0$ в схемах с тетраэдром (Рисунок 1, 2).

<table align="center">
<tr>
<td align="center"><img src="/img/conductive-tetrahedra1.svg"></td>
<td align="center"><img src="/img/conductive-tetrahedra2.svg"></td>
</tr>
<tr>
<td align="center">Рисунок 1</td>
<td align="center">Рисунок 2</td>
</tr>
</table>

Первая задача (Рисунок 1) решается просто. Из симметрии сразу следует, что потенциалы точек 3 и 4 совпадают. Это приводит к тому, что по участку 3-4 ток не течёт. Две эквивалентные схемы представлены на рисунках 3 и 4.

<table align="center">
<tr>
<td align="center"><img src="/img/conductive-tetrahedra11.svg"></td>
<td align="center"><img src="/img/conductive-tetrahedra12.svg"></td>
</tr>
<tr>
<td align="center">Рисунок 3</td>
<td align="center">Рисунок 4</td>
</tr>
</table>

В случае рисунка 3:

$$
R_{0} = \dfrac{R \dfrac{4 R^2}{2R + 2R}}{R + \dfrac{4 R^2}{2R + 2R}} = \dfrac{R}{2}
$$

В случае рисунка 4:

$$
R_{0} = \dfrac{R \left(\dfrac{R}{2} + \dfrac{R}{2}\right)}{R + \dfrac{R}{2} + \dfrac{R}{2}} = \dfrac{R}{2}
$$

Вторая задача допускает множество способов решения. Часть из них - стандартные. Но есть и не очень обычный путь. Начнём со стандартного пути. Эквивалентная схема рисунка 2 представлена на рисунке 5.

<div align="center"><img src="/img/conductive-tetrahedra21.svg"><br>Рисунок 5</div>

По правилам Кирхгофа:

$$
\begin{aligned}
& i_{13} R_1 + i_{34} R_4 - i_{14} R_2 = 0, \\
& - i_{23} R_2 + i_{24} R_1 - i_{34} R_4 = 0, \\
& i_{14} R_2 - i_{24} R_1 - i_{12} R_3 = 0, \\
& i_{34} - i_{23} - i_{13} = 0, \\
& i_{14} + i_{34} + i_{24} = 0, \\
& i_{13} + i_{14} + i_{12} = I
\end{aligned}
$$

$$
\begin{pmatrix}
1 & 1 & 1 & 0 & 0 & 0 \\
0 & 0 & 1 & 0 & 1 & 1 \\
0 & -1 & 0 & -1 & 0 & 1 \\
-R_3 & 0 & R_2 & 0 & -R_1 & 0 \\
0 & 0 & 0 & - R_2 & R_1 & - R_4 \\
0 & R_1 & -R_2 & 0 & 0 & R_4
\end{pmatrix}
\begin{pmatrix}
i_{12} \\
i_{13} \\
i_{14} \\
i_{23} \\
i_{24} \\
i_{34}
\end{pmatrix} = 
\begin{pmatrix}
I \\
0 \\
0 \\
0 \\
0 \\
0
\end{pmatrix}
$$

$$
\begin{pmatrix}
1 & 1 & 1 & 0 & 0 & 0 & | & I \\
0 & 0 & 1 & 0 & 1 & 1 & | & 0 \\
0 & -1 & 0 & -1 & 0 & 1 & | & 0 \\
-R_3 & 0 & R_2 & 0 & -R_1 & 0 & | & 0 \\
0 & 0 & 0 & - R_2 & R_1 & - R_4 & | & 0 \\
0 & R_1 & -R_2 & 0 & 0 & R_4 & | & 0 \\
\end{pmatrix} \sim
$$

$$
\sim\begin{pmatrix}
1 & 1 & 1 & 0 & 0 & 0 & | & I \\
0 & 0 & 1 & 0 & 1 & 1 & | & 0 \\
0 & -1 & 0 & -1 & 0 & 1 & | & 0 \\
0 & R_3 & R_2 + R_3 & 0 & -R_1 & 0 & | & R_3 I \\
0 & 0 & 0 & - R_2 & R_1 & - R_4 & | & 0 \\
0 & R_1 & -R_2 & 0 & 0 & R_4 & | & 0 \\
\end{pmatrix} \sim
$$

$$
\sim
\begin{pmatrix}
1 & 1 & 1 & 0 & 0 & 0 & | & I \\
0 & -1 & 0 & -1 & 0 & 1 & | & 0 \\
0 & 0 & 1 & 0 & 1 & 1 & | & 0 \\
0 & R_3 & R_2 + R_3 & 0 & -R_1 & 0 & | & R_3 I \\
0 & 0 & 0 & - R_2 & R_1 & - R_4 & | & 0 \\
0 & R_1 & -R_2 & 0 & 0 & R_4 & | & 0 \\
\end{pmatrix} \sim 
$$

$$
\sim
\begin{pmatrix}
1 & 1 & 1 & 0 & 0 & 0 & | & I \\
0 & -1 & 0 & -1 & 0 & 1 & | & 0 \\
0 & 0 & 1 & 0 & 1 & 1 & | & 0 \\
0 & 0 & R_2 + R_3 & -R_3 & -R_1 & R_3 & | & R_3 I \\
0 & 0 & 0 & - R_2 & R_1 & - R_4 & | & 0 \\
0 & 0 & -R_2 & -R_1 & 0 & R_4 + R_1 & | & 0 \\
\end{pmatrix} \sim 
$$

$$
\sim
\begin{pmatrix}
1 & 1 & 1 & 0 & 0 & 0 & | & I\\
0 & -1 & 0 & -1 & 0 & 1 & | & 0\\
0 & 0 & 1 & 0 & 1 & 1 & | & 0\\
0 & 0 & 0 & -R_3 & -R_1- R_2 - R_3 & -R_2 & | & R_3 I\\
0 & 0 & 0 & - R_2 & R_1 & - R_4 & | & 0 \\
0 & 0 & 0 & -R_1 & R_2 & R_4 + R_1 + R_2 & | & 0
\end{pmatrix}\sim
$$

Нам не требуются все токи, достаточно знать только пару. Детерминант матрицы:

$$
\begin{gathered}
- (R_4 + R_1 + R_2) R_1 R_3 - (R_1 + R_2 + R_3) R_4 R_1 + R_2^3 - \\- R_2 R_1^2 + R_2 R_3 R_4 - R_2 (R_1 + R_2 + R_3)(R_1 + R_2 + R_4) = \\ = 
- (R_4 + R_1 + R_2) R_1 R_3 - (R_1 + R_2 + R_3) R_4 R_1 + \underline{R_2^3} - R_2 R_1^2 - R_2 R_3 R_4 - \\- R_2 (R_1^2 + \underline{R_2^2} + 2 R_1 R_2 + R_3 R_1 + R_3 R_2 + R_4 R_1 + R_4 R_2 + R_3 R_4) = \\ =
- 2 R_1 R_3 R_4 - 2 R_2 R_3 R_4 - \underline{R_1^2 R_3 - 2 R_1 R_2 R_3 - R_1^2 R_4 - 2 R_1 R_2 R_4 }- 2 R_2 R_1^2 - \\ - 2 R_1 R_2^2 - \underline{R_2^2 R_3 - R_2^2 R_4} = \\ = 
-2 (R_1 + R_2) R_3 R_4 - (R_1 + R_2)^2 (R_3 + R_4) - 2 R_1 R_2 (R_1 + R_2) = \\ =
- (R_1 + R_2) (2 R_3 R_4 + 2 R_1 R_2 + R_1 R_3 + R_1 R_4 + R_2 R_3 + R_2 R_4)
\end{gathered}
$$

По формулам Крамера:

$$
i_{23} = \dfrac{R_3 I (R_1 R_4 + R_1 (R_1 +R _2) + R_2 R_4)}{- (R_1 + R_2) (2 R_3 R_4 + 2 R_1 R_2 + R_1 R_3 + R_1 R_4 + R_2 R_3 + R_2 R_4)} =
$$

$$
= -\dfrac{R_3 I (R_1 + R_4)}{2 R_3 R_4 + 2 R_1 R_2 + R_1 R_3 + R_1 R_4 + R_2 R_3 + R_2 R_4}
$$

$$
i_{24} = \dfrac{- R_3 I (-R_2(R_1 + R_2 + R_4) - R_1 R_4)}{- (R_1 + R_2) (2 R_3 R_4 + 2 R_1 R_2 + R_1 R_3 + R_1 R_4 + R_2 R_3 + R_2 R_4)} = 
$$

$$
= - \dfrac{R_3 I (R_1 + R_4)}{2 R_3 R_4 + 2 R_1 R_2 + R_1 R_3 + R_1 R_4 + R_2 R_3 + R_2 R_4} 
$$

$$
i_{34} =  \dfrac{I (-R_1 + R_2) R_3             }{2 R_1 R_2 + R_1 R_3 + R_2 R_3 + R_1 R_4 + R_2 R_4 + 2 R_3 R_4 }
$$

Если воспользоваться теперь выражениями для токов, то можно получить все токи:

$$
\begin{aligned}
& i_{12} =  \dfrac{I (2 R_1 R_2 + R_1 R_4 + R_2 R_4)}{2 R_1 R_2 + R_1 R_3 + R_2 R_3 + R_1 R_4 + R_2 R_4 + 2 R_3 R_4 }, \\
& i_{13} =  \dfrac{I R_3 (R_2 + R_4)              }{2 R_1 R_2 + R_1 R_3 + R_2 R_3 + R_1 R_4 + R_2 R_4 + 2 R_3 R_4 }, \\
& i_{14} =  \dfrac{I R_3 (R_1 + R_4)              }{2 R_1 R_2 + R_1 R_3 + R_2 R_3 + R_1 R_4 + R_2 R_4 + 2 R_3 R_4 }, \\
& i_{23} = -\dfrac{I R_3 (R_1 + R_4)              }{2 R_1 R_2 + R_1 R_3 + R_2 R_3 + R_1 R_4 + R_2 R_4 + 2 R_3 R_4 }, \\
& i_{24} = -\dfrac{I R_3 (R_2 + R_4)              }{2 R_1 R_2 + R_1 R_3 + R_2 R_3 + R_1 R_4 + R_2 R_4 + 2 R_3 R_4 }, \\
& i_{34} =  \dfrac{I (-R_1 + R_2) R_3             }{2 R_1 R_2 + R_1 R_3 + R_2 R_3 + R_1 R_4 + R_2 R_4 + 2 R_3 R_4 }
\end{aligned}
$$

Для полного сопротивления имеем:

$$
R_{0} = \dfrac{U}{I} = \dfrac{i_{12} R_3}{I} = \dfrac{R_3 (2 R_1 R_2 + R_1 R_4 + R_2 R_4)}{2 R_1 R_2 + R_1 R_3 + R_2 R_3 + R_1 R_4 + R_2 R_4 + 2 R_3 R_4 }
$$

Как легко видеть данный путь приводит к весьма громоздким вычислениям. Существует другой путь - более аккуратный, но и менее общий. Поступим так, как поступали выше. Построим две схемы - одну замкнутую накоротко, а другую - с разрывом вместо резистора на участке 3-4. Так как система линейна, то суперпозиция всех потенциалов и токов для двух данных схем даст нужное решение при условии, что разность потенциалов между точками 3-4 и ток на данном участке цепи будут связаны нужным соотношением.

<table align="center">
<tr>
<td align="center"><img src="/img/conductive-tetrahedra32.svg"></td>
<td align="center"><img src="/img/conductive-tetrahedra31.svg"></td>
</tr>
<tr>
<td align="center">Рисунок 6</td>
<td align="center">Рисунок 7</td>
</tr>
</table>

В случае рисунка 6:

$$
U_s = \dfrac{R_3 \dfrac{R_2 + R_1}{2}}{R_3 + \dfrac{R_2 + R_1}{2}} I_s = \dfrac{R_3 (R_1 + R_2)}{2 R_3 + R_1 +R_2} I_s
$$

В случае рисунка 7:

$$
U_c = \dfrac{R_3 \cdot 2 \cdot \dfrac{R_1 R_2}{R_1 +R_2}}{R_3 + 2 \cdot \dfrac{R_1 R_2}{R_1 +R_2}} I_c = \dfrac{2 R_1 R_2 R_3}{R_1 R_3 + R_2 R_3 + 2 R_1 R_2} I_c
$$

Результат:

$$
U = U_c + U_s, \qquad I = I_c + I_s
$$

Условие:

$$
\varphi_3 - \varphi_4 = i_{31} R_1 - i_{41} R_2 = - \dfrac{U_s}{R_1 + R_2} (R_1 - R_2)
$$

$$
i_{34} = I_{c1} - I_{c2} = \dfrac{U_c}{2 R_1} - \dfrac{U_c}{2 R_2} = \dfrac{U_c}{2} \dfrac{R_2 - R_1}{R_1 R_2}
$$

$$
\varphi_3 - \varphi_4 = i_{34} R_4
$$

Откуда:

$$
U_s = U_c \dfrac{R_1 + R_2}{2 R_1 R_2} R_4
$$

$$
R_{0} = \dfrac{U}{I} = \dfrac{U_c}{I_c} \dfrac{1 + \dfrac{R_1 + R_2}{2 R_1 R_2} R_4}{1 + \dfrac{I_s}{U_s} \dfrac{U_c}{I_c} \dfrac{U_s}{U_c}} =
$$

$$
= \dfrac{2 R_1 R_2 R_3}{R_1 R_3 + R_2 R_3 + 2 R_1 R_2} \dfrac{\dfrac{2 R_1 R_2 + R_1 R_4 + R_2 R_4}{2 R_1 R_2}}{1 + \dfrac{2 R_1 R_2 R_3}{R_1 R_3 + R_2 R_3 + 2 R_1 R_2}\dfrac{2 R_3 + R_1 +R_2}{R_3 (R_1 + R_2)} \dfrac{R_1 + R_2}{2 R_1 R_2} R_4} = 
$$

$$
= \dfrac{R_3}{R_1 R_3 + R_2 R_3 + 2 R_1 R_2} \dfrac{\dfrac{2 R_1 R_2 + R_1 R_4 + R_2 R_4}{1}}{1 + \dfrac{1}{R_1 R_3 + R_2 R_3 + 2 R_1 R_2}\dfrac{2 R_3 + R_1 +R_2}{1} \dfrac{1}{1} R_4} = 
$$

$$
= \dfrac{(2 R_1 R_2 + R_1 R_4 + R_2 R_4) R_3}{R_1 R_3 + R_2 R_3 + 2 R_1 R_2 + 2 R_3 R_4 + R_1 R_4 + R_2 R_4}
$$

Убеждаемся в полном совпадении результатов. 

А теперь попробуем решить задачу с любыми сопротивлениями.

<table align="center">
<tr>
<td align="center"><img src="/img/conductive-tetrahedra42.svg"></td>
<td align="center"><img src="/img/conductive-tetrahedra41.svg"></td>
</tr>
<tr>
<td align="center">Рисунок 8</td>
<td align="center">Рисунок 9</td>
</tr>
</table>

В случае рисунка 8:

$$
U_s = \dfrac{R_{12} \dfrac{(R_{13} + R_{23})(R_{14} + R_{24})}{R_{13} + R_{23} + R_{14} + R_{24}}}{R_{12} + \dfrac{(R_{13} + R_{23})(R_{14} + R_{24})}{R_{13} + R_{23} + R_{14} + R_{24}}} I_s
$$

В случае рисунка 9:

$$
U_c = \dfrac{R_{12} \cdot \left(\dfrac{R_{13} R_{14}}{R_{13} + R_{14}} + \dfrac{R_{23} R_{24}}{R_{23} + R_{24}}\right)}{R_{12} + \dfrac{R_{13} R_{14}}{R_{13} + R_{14}} + \dfrac{R_{23} R_{24}}{R_{23} + R_{24}}} I_c
$$

Результат:

$$
U = U_c + U_s, \qquad I = I_c + I_s
$$

Условие:

$$
\varphi_3 - \varphi_4 = i_{31} R_{13} - i_{41} R_{14} = - \dfrac{U_s}{R_{13} + R_{23}} R_{13} + \dfrac{U_s}{R_{14} + R_{24}} R_{14} = 
$$

$$
= U_s \left(\dfrac{R_{14}}{R_{14} + R_{24}} - \dfrac{R_{13}}{R_{13} + R_{23}} \right)
$$

$$
i_{34} = I_{c1} - I_{c2} = \dfrac{U_c}{\dfrac{R_{13} R_{14}}{R_{13} + R_{14}} + \dfrac{R_{23} R_{24}}{R_{23} + R_{24}}} \left(\dfrac{R_{14}}{R_{13} + R_{14}} - \dfrac{R_{24}}{R_{23} + R_{24}}\right)
$$

$$
\varphi_3 - \varphi_4 = i_{34} R_{34}
$$

Откуда:

$$
U_s = \dfrac{U_c}{\dfrac{R_{13} R_{14}}{R_{13} + R_{14}} + \dfrac{R_{23} R_{24}}{R_{23} + R_{24}}} \dfrac{\dfrac{R_{14}}{R_{13} + R_{14}} - \dfrac{R_{24}}{R_{23} + R_{24}}}{\dfrac{R_{14}}{R_{14} + R_{24}} - \dfrac{R_{13}}{R_{13} + R_{23}} } R_{34}
$$

$$
R_{0} = \dfrac{U}{I} = \dfrac{U_c}{I_c} \dfrac{1 + \dfrac{R_{34}}{\dfrac{R_{13} R_{14}}{R_{13} + R_{14}} + \dfrac{R_{23} R_{24}}{R_{23} + R_{24}}} \dfrac{\dfrac{R_{14}}{R_{13} + R_{14}} - \dfrac{R_{24}}{R_{23} + R_{24}}}{\dfrac{R_{14}}{R_{14} + R_{24}} - \dfrac{R_{13}}{R_{13} + R_{23}} } }{1 + \dfrac{I_s}{U_s} \dfrac{U_c}{I_c} \dfrac{U_s}{U_c}} =
$$

$$
= \dfrac{R_{12} \cdot \left(\dfrac{R_{13} R_{14}}{R_{13} + R_{14}} + \dfrac{R_{23} R_{24}}{R_{23} + R_{24}}\right)}{R_{12} + \dfrac{R_{13} R_{14}}{R_{13} + R_{14}} + \dfrac{R_{23} R_{24}}{R_{23} + R_{24}}} \cdot
$$

$$
\cdot \dfrac{1 + \dfrac{R_{34}}{\dfrac{R_{13} R_{14}}{R_{13} + R_{14}} + \dfrac{R_{23} R_{24}}{R_{23} + R_{24}}} \dfrac{\dfrac{R_{14}}{R_{13} + R_{14}} - \dfrac{R_{24}}{R_{23} + R_{24}}}{\dfrac{R_{14}}{R_{14} + R_{24}} - \dfrac{R_{13}}{R_{13} + R_{23}} } }{1 + \dfrac{R_{12} + \dfrac{(R_{13} + R_{23})(R_{14} + R_{24})}{R_{13} + R_{23} + R_{14} + R_{24}}} {R_{12} \dfrac{(R_{13} + R_{23})(R_{14} + R_{24})}{R_{13} + R_{23} + R_{14} + R_{24}}}\dfrac{R_{34}}{\dfrac{R_{13} R_{14}}{R_{13} + R_{14}} + \dfrac{R_{23} R_{24}}{R_{23} + R_{24}}} \dfrac{\dfrac{R_{14}}{R_{13} + R_{14}} - \dfrac{R_{24}}{R_{23} + R_{24}}}{\dfrac{R_{14}}{R_{14} + R_{24}} - \dfrac{R_{13}}{R_{13} + R_{23}} } \dfrac{R_{12} \cdot \left(\dfrac{R_{13} R_{14}}{R_{13} + R_{14}} + \dfrac{R_{23} R_{24}}{R_{23} + R_{24}}\right)}{R_{12} + \dfrac{R_{13} R_{14}}{R_{13} + R_{14}} + \dfrac{R_{23} R_{24}}{R_{23} + R_{24}}}} =
$$

$$
= R_{12} 
\dfrac{
	\dfrac{R_{13} R_{14}}{R_{13} + R_{14}} + \dfrac{R_{23} R_{24}}{R_{23} + R_{24}} + \dfrac{R_{34}}{1} \dfrac{\dfrac{R_{14}}{R_{13} + R_{14}} - \dfrac{R_{24}}{R_{23} + R_{24}}}{\dfrac{R_{14}}{R_{14} + R_{24}} - \dfrac{R_{13}}{R_{13} + R_{23}} } }
{
	R_{12} + 
	\dfrac{R_{13} R_{14}}{R_{13} + R_{14}} + \dfrac{R_{23} R_{24}}{R_{23} + R_{24}} + \left(\dfrac{R_{12}(R_{13} + R_{23} + R_{14} + R_{24})} {(R_{13} + R_{23})(R_{14} + R_{24})} + 1\right)
	\dfrac{R_{34}}{1} \dfrac{\dfrac{R_{14}}{R_{13} + R_{14}} - \dfrac{R_{24}}{R_{23} + R_{24}}}{\dfrac{R_{14}}{R_{14} + R_{24}} - \dfrac{R_{13}}{R_{13} + R_{23}} } 
} =
$$

$$
= R_{12} 
\dfrac{
	\left(\dfrac{R_{13} R_{14}}{R_{13} + R_{14}} + \dfrac{R_{23} R_{24}}{R_{23} + R_{24}}\right) \left(\dfrac{R_{14}}{R_{14} + R_{24}} - \dfrac{R_{13}}{R_{13} + R_{23}}\right) + \left(
	\dfrac{R_{34} R_{14}}{R_{13} + R_{14}} - \dfrac{R_{34} R_{24}}{R_{23} + R_{24}} \right) }
{
	\left(R_{12} + 
	\dfrac{R_{13} R_{14}}{R_{13} + R_{14}} + \dfrac{R_{23} R_{24}}{R_{23} + R_{24}} \right) \left(\dfrac{R_{14}}{R_{14} + R_{24}} - \dfrac{R_{13}}{R_{13} + R_{23}}\right) + \left(\dfrac{R_{12}(R_{13} + R_{23} + R_{14} + R_{24})} {(R_{13} + R_{23})(R_{14} + R_{24})} + 1\right) \left(
	\dfrac{R_{34} R_{14}}{R_{13} + R_{14}} - \dfrac{R_{34} R_{24}}{R_{23} + R_{24}} \right)
}
$$

Умножаем и числитель и знаменатель на $(R_{13} + R_{14})(R_{23}+R_{24})(R_{14}+R_{24})(R_{13}+R_{23})$. Числитель:

$$
\begin{gathered}
\left((R_{23}+R_{24})R_{13} R_{14} + (R_{13} + R_{14})R_{23} R_{24}\right) 
\left((R_{13}+R_{23})R_{14}- (R_{14}+R_{24})R_{13}\right) + \\ +
(R_{14}+R_{24})(R_{13}+R_{23})\left(
	(R_{23}+R_{24})R_{34} R_{14}- (R_{13} + R_{14})R_{34} R_{24} \right)
	= \\ =
\left(R_{23}R_{13} R_{14}+R_{24}R_{13} R_{14} + R_{13} R_{23} R_{24}+ R_{14}R_{23} R_{24}\right) 
\left(R_{23}R_{14}- R_{24} R_{13}\right) + \\ +
(R_{14}+R_{24})(R_{13}+R_{23})R_{34} \left(
	R_{23}R_{14}- R_{13}R_{24} \right) = \\ =
\left[R_{23}R_{13} R_{14}+R_{24}R_{13} R_{14} + R_{13} R_{23} R_{24}+ R_{14}R_{23} R_{24} + \right. \\
+ \left. R_{14} R_{13} R_{34} + R_{14} R_{23} R_{34} +  R_{24} R_{13} R_{34} + R_{24} R_{23} R_{34}\right] 
\left(R_{23}R_{14}- R_{24} R_{13}\right)
\end{gathered}
$$

Знаменанатель:

$$
\begin{gathered}
\left(R_{12}(R_{13} + R_{14})(R_{23}+R_{24})  + 
	R_{13} R_{14}(R_{23}+R_{24}) + R_{23} R_{24}(R_{13} + R_{14}) \right) \left(R_{23}R_{14} - R_{24}R_{13}\right) + \\ 
+ \left(R_{12}(R_{13} + R_{23} + R_{14} + R_{24}) + (R_{13} + R_{23})(R_{14} + R_{24})\right) R_{34} \left(
	R_{23}R_{14}- R_{13}R_{24}\right) = \\ =
\left[
	R_{12} R_{13} R_{23} + R_{12} R_{13} R_{24} + R_{12} R_{14} R_{23} + R_{12} R_{14} R_{24}  + \right. \\ \left. +
	R_{13} R_{14} R_{23} + R_{13} R_{14} R_{24} + 
	R_{13} R_{23} R_{24} + R_{14} R_{23} R_{24} + \right. \\ \left. +
	R_{12} R_{13} R_{34} + R_{12} R_{23} R_{34} + R_{12} R_{14} R_{34} + R_{12} R_{24} R_{34}  \right. \\ \left. + 
	R_{13} R_{14} R_{34} + R_{13} R_{24} R_{34} + R_{14} R_{23} R_{34} + R_{23} R_{24} R_{34}
\right] \left(R_{23}R_{14} - R_{24}R_{13}\right)
\end{gathered}
$$

Ответ:

$$
R_0 = R_{12} \dfrac{
	R_{13} R_{14} R_{23} + R_{13} R_{14} R_{24} + 
	R_{13} R_{14} R_{34} + R_{13} R_{23} R_{24} + 
	R_{13} R_{24} R_{34} + R_{14} R_{23} R_{24} + 
	R_{14} R_{23} R_{34} + R_{23} R_{24} R_{34}
}{
	R_{12} R_{13} R_{23} + R_{12} R_{13} R_{24} + 
	R_{12} R_{13} R_{34} + R_{12} R_{14} R_{23} + 
	R_{12} R_{14} R_{24} + R_{12} R_{14} R_{34} +
	R_{12} R_{23} R_{34} + R_{12} R_{24} R_{34} +
	R_{13} R_{14} R_{23} + R_{13} R_{14} R_{24} + 
	R_{13} R_{14} R_{34} + R_{13} R_{23} R_{24} + 
	R_{13} R_{24} R_{34} + R_{14} R_{23} R_{24} + 
	R_{14} R_{23} R_{34} + R_{23} R_{24} R_{34}
}
$$
