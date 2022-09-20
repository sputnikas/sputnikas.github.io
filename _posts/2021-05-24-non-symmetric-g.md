---
layout: page
title: К теории с несимметричным метрическим тензором
---

### Основные понятия и уравнения

*1. Исследуемое пространство.* Рассмотрим арифметическое $N$-мерное векторное пространство с элементами $\vec{A}$. Будем называть его пространством изотопического спина или изопространством. В данном векторном пространстве введём базис из каких-либо $N$-мерных арифметических векторов $\vec{e}_i$, $i = 1, 2, 3, \ldots N$, компоненты которых представляют собой функции $M$ координат $q^1, q^2, \ldots, q^M$ 

$$
\vec{e}_i = \left\{e_{i}^1(q^1, q^2, \ldots, q^M), e_i^2(q^1, q^2, \ldots, q^M),\ldots, e_i^N(q^1, q^2, \ldots, q^M)\right\}
$$

и будем полагать базис полным $\forall \vec{A} \,\exists A^i$:

$$
\vec{A} = A^i \vec{e}_i
$$

и линейно независимым $\nexists A^i \ne 0$:

$$
A^i \vec{e}_i = \vec{0}
$$

*2. Билинейная операция.* Введём операцию:

$$
\vec{X}\otimes\vec{Y} = c_{kl} X^k Y^l
$$

$c_{kl}$ - произвольная матрица, которая одинакова при любых преобразованиях базисов и не зависит от них и от точки координат.

*3. "Метрический" тензор.* 

$$
G_{ij} = \vec{e}_i \otimes \vec{e}_j = c_{kl} e_i^k e_j^l
$$

Контравариантным "метрическим" тензором назовём тензор обратный к нему:

$$
G^{ik}G_{kj} = \delta_j^i
$$

$\delta_j^i$ - символ Кронекера. В матричных обозначениях:

$$
\hat{G} = \hat{e}^T\hat{c}\hat{e}
$$

Элементы матриц $\{\hat{e}\}_{ij} = e^i_j$, $\{\hat{c}\}_{ij} = c_{ij}$, $\{\hat{G}\}_{ij} = G_{ij}$, $\{\hat{e}^T\}_{ij} = \{\hat{e}\}_{ji} = e^j_i$.

*4. Символы "Кристоффеля".* Рассмотрим $\partial \vec{e}_i / \partial q^j$, в силу свойства полноты:

$$
\frac{\partial \vec{e}_i}{\partial q^j} = \Gamma^k_{i, j} \vec{e}_k
$$

Коэффициенты данного разложения мы будем называть символами "Кристоффеля" 2 рода или коэффициентами "связности". Очевидно их $N^2 M$ штук. Далее:

$$
\frac{\partial G_{ij}}{\partial q^k} = c_{lm} e_j^m \frac{\partial e_i^l}{\partial q^k} + c_{lm} e_i^l \frac{\partial e_j^m}{\partial q^k} = \frac{\partial \vec{e}_i}{\partial q^k} \otimes \vec{e}_j  + \vec{e}_i \otimes \frac{\partial \vec{e}_j}{\partial q^k} =
$$

$$
= \Gamma^l_{i, k} \vec{e}_l \otimes \vec{e}_j + \vec{e}_i \otimes \Gamma^l_{j, k} \vec{e}_l = \Gamma^l_{i, k} G_{lj} + \Gamma^l_{j,k} G_{il}
$$

Окончательно для коэффициентов имеем систему:

$$
\frac{\partial G_{ij}}{\partial q^k} = \Gamma^l_{i, k} G_{lj} + \Gamma^l_{j,k} G_{il}
$$

Мы имеем $N^2 M$ линейных уравнений относительно $N^2 M$ линейных неизвестных. Система может быть разрешима, хотя условия разрешимости, как и сами решения требуют отдельного анализа. Её можно переписать в матричном виде. Обозначим $$\hat{\Gamma}_k$$ матрицу с элементами $$(\hat{\Gamma}_k)_{ij} = \Gamma^j_{i, k}$$. Тогда:

$$
\frac{\partial \hat{G}}{\partial q^k} = \hat{\Gamma}_k \hat{G} + \hat{G}\hat{\Gamma}^T_k
$$

Очевидно, что можно уравнение транспонировать:

$$
\frac{\partial \hat{G}^T}{\partial q^k} = \hat{G}^T \hat{\Gamma}_k^T  + \hat{\Gamma}_k \hat{G}^T
$$

Введём одно полезное обозначение $\hat{A}^{-T} = (\hat{A}^{-1})^T = (\hat{A}^T)^{-1}$:

$$
\hat{G}^{-1} \frac{\partial \hat{G}}{\partial q^k} - \hat{G}^{-T} \frac{\partial \hat{G}^T}{\partial q^k} = \hat{G}^{-1} \hat{\Gamma}_k \hat{G} - \hat{G}^{-T} \hat{\Gamma}_k \hat{G}^T
$$

Так как система уравнений линейна, мы введём ещё одну матрицу - будем полагать систему разрешимой:

$$
\hat{\Gamma}_k = \hat{T}(\hat{G}) \frac{\partial \hat{G}}{\partial q^k}, \qquad \Gamma^j_{i,k} = T^{j,lm}_i (\hat{G}) \frac{\partial G_{lm}}{\partial q^k}
$$

*5. Тензор "Римана".* Рассмотрим следующее соотношение:

$$
\frac{\partial^2 \vec{e}_i}{\partial q^j \partial q^k} - \frac{\partial^2 \vec{e}_i}{\partial q^k \partial q^j} = \frac{\partial \Gamma^l_{i, k}}{\partial q^j} \vec{e}_l + \Gamma^l_{i, k} \Gamma^p_{l, j} \vec{e}_p - \frac{\partial \Gamma^l_{i, j}}{\partial q^k} \vec{e}_l - \Gamma^l_{i, j} \Gamma^p_{l, k} \vec{e}_p =
$$

$$
= \left[\frac{\partial \Gamma^l_{i, k}}{\partial q^j} - \frac{\partial \Gamma^l_{i, j}}{\partial q^k} + \Gamma^p_{i, k} \Gamma^l_{p, j} - \Gamma^p_{i, j} \Gamma^l_{p, k} \right] \vec{e}_l = R^l_{i, kj} \vec{e}_l
$$

$R^l_{i,kj}$ обобщает понятие тензора Римана. 

*6. Инвариант относительно вращений.* В общей теории относительности (ОТО) размерности пространств совпадают $N = M$. Инвариантом относительно вращений является скалярная кривизна $R = g^{kj} R^l_{klj}$. Здесь $g^{kj}$ - метрический тензор пространства $M$ измерений. Но такое свойство может быть только у пространства с $N = M$. Можно показать, что другой инвариант относительно вращений в наших пространствах:

$$
g^{kj} R^l_{l, kj} = 0
$$

$$
R^l_{l, kj} = \frac{\partial \Gamma^l_{l, k}}{\partial q^j} - \frac{\partial \Gamma^l_{l, j}}{\partial q^k} + \Gamma^p_{l, k} \Gamma^l_{p, j} - \Gamma^p_{l, j} \Gamma^l_{p, k} = 0
$$

Это следует из свойства:

$$
\Gamma^i_{i, j} = \frac{N}{2} \frac{\partial \ln \det \hat{G}}{\partial q^j}
$$

И замены немых индексов: $l \leftrightarrow p$. Попытаемся построить все инварианты. К $R^l_{i,kj}$ можно подходить как к $M^2$ квадратным матрицам размера $N\times N$. У таких матриц существует $N$ собственных значений. Любая функция собственных значений будет инвариантом относительно преобразований базиса в изопространстве. Рассмотрим детерминант от матрицы для секулярного уравнения:

$$
\epsilon_{i_1 i_2 \ldots i_N} \epsilon^{j_1 j_2 \ldots j_{N}} (R^{i_1}_{j_1, kj} - \lambda \delta^{i_1}_{j_1}) (R^{i_2}_{j_2, kj} - \lambda \delta^{i_2}_{j_2}) \ldots (R^{i_N}_{j_N, kj} - \lambda \delta^{i_N}_{j_N})
$$

Здесь $\epsilon_{i_1 i_2 \ldots i_N}$, $\epsilon^{j_1 j_2 \ldots j_{N}}$ - символы Леви-Чивита. Его коэффициенты при $\lambda^m$ представляют собой инварианты - функции собственных значений. 

*6. Принцип наименьшего действия.* Введём последовательность пространств с размерностями $1, 2, 3, \ldots$ и для каждого из них введём скалярную кривизну (последовательность "римановых" тензоров и кривизны будем обозначать арабскими числами в скобках). В результате инвариантное относительно произвольных преобразований координат действие:

$$
S = \int_{M} \left[\alpha_0 + \alpha_1 R^{(1)} + \alpha_2 R^{(2)} + \alpha_3 R^{(3)} + \alpha_4 R^{(4)} + \ldots \right] \sqrt{-\det{\hat{g}}} \, dV_M
$$

Знак "-" под корнем особой роли не играет, и нужен для соблюдения неотрицательности подкоренного выражения в случае отрицательного определителя. В общем случае знак может быть и положительным. Осталось получить из принципа наименьшего действия все уравнения и найти их решения. Следует отметить, что данная система содержит в себе очень и очень многое. Как подмножество здесь есть ОТО. Вместо линейной функции скалярной кривизны вообще говоря должна стоять произвольная функция, но пока остановимся на линейном случае и будем рассматривать только его. 

*7. Принцип наименьшего действия в слабой форме.* В теории важную роль играет принцип наименьшего действия в слабой форме, когда лагранжева плотность, стоящая под знаком интеграла, зависит только от производных первого порядка. Достигается это методом интегрирования по частям и применением специальных граничных условий. Отметим, что дифференциальные уравнения Лагранжа для поля $\hat{G}^{(\alpha)}$ во всех случаях за исключением случая $\alpha = M$  будут связаны только со своей скалярной кривизной $R^{(\alpha)}$. Рассмотрим отдельное слагаемое суммы c $\alpha \ne M$, опустив индекс $\alpha$:

$$
\int_M R \sqrt{- \det \hat{g}} \, dV_M = \int_M g^{kj} R^l_{l, kj} \sqrt{-\det \hat{g}} dV_M =
$$

$$
= \int_M g^{kj} \left[\frac{\partial \Gamma^l_{l, k}}{\partial q^j} - \frac{\partial \Gamma^l_{l, j}}{\partial q^k} + \Gamma^p_{l, k} \Gamma^l_{p, j} - \Gamma^p_{l, j} \Gamma^l_{p, k} \right] \sqrt{-\det \hat{g}} dV_M =
$$

$$
= \int_M \left[ -\frac{\partial g^{kj} \sqrt{-\det \hat{g}}}{\partial q^j} \Gamma^l_{l, k} + \frac{\partial g^{kj} \sqrt{-\det \hat{g}}}{\partial q^k} \Gamma^l_{l, j} + \sqrt{-\det \hat{g}} \left(\Gamma^p_{l, k} \Gamma^l_{p, j} - \Gamma^p_{l, j} \Gamma^l_{p, k} \right)\right] dV_M
$$

Здесь мы положили, что поверхностные интегралы равны 0 - условие, которое позволяет получить принцип наименьшего действия в слабой форме.

Векторное пространство $M$ измерений, заданное над пространством $N$ измерений, по аналогии со Стандартной моделью будем называть изотопическим пространством или изопространством.

### Некоторые свойства

1. Коэффициенты "связности" не меняются при умножении "метрического" тензора на произвольное число.

2. Производная контравариантного "метрического" тензора:

   $$
   \frac{\partial G^{kj}}{\partial q^s} = - G^{km} \Gamma^j_{m,s} - G^{lj} \Gamma^k_{l,s}
   $$
   
   *Доказательство:*
   
   $$
   G^{kj} G_{jl} = \delta^k_l
   $$

   $$
   \frac{\partial G^{kj}}{\partial q^s} G_{jl} = - G^{kj} \frac{\partial G_{jl}}{\partial q^s}
   $$

   $$
   \frac{\partial G^{kj}}{\partial q^s} = - G^{lj} G^{km} \frac{\partial G_{ml}}{\partial q^s} = - G^{lj} G^{km} [\Gamma^r_{m, s} G_{rl} + \Gamma^r_{l,s}G_{mr}] =
   $$

   $$
   = - G^{km} \Gamma^j_{m,s} - G^{lj} \Gamma^k_{l,s}
   $$

3. Производная детерминанта "метрического" тензора:

   $$
   \frac{\partial \det \hat{G}}{\partial q^j} = \frac{2\det{\hat{G}}}{N} \Gamma^i_{i,j}
   $$
   
   *Доказательство:*
   
   $$
   \frac{\partial \det \hat{G}}{\partial q^j} = \begin{vmatrix}
   \dfrac{\partial G_{11}}{\partial q^j} & \dfrac{\partial G_{12}}{\partial q^j} & \ldots  & \dfrac{\partial G_{1N}}{\partial q^j} \\
   G_{21} & G_{22} & \ldots & G_{2N} \\
   \ldots & \ldots &  & \ldots \\
   G_{N1} & G_{N2} & \ldots & G_{NN} 
   \end{vmatrix} + \begin{vmatrix}
   G_{11} & G_{12} & \ldots & G_{1N} \\
   \dfrac{\partial G_{21}}{\partial q^j} & \dfrac{\partial G_{22}}{\partial q^j} & \ldots  & \dfrac{\partial G_{2N}}{\partial q^j} \\
   \ldots & \ldots &  & \ldots \\
   G_{N1} & G_{N2} & \ldots & G_{NN} 
   \end{vmatrix} + \ldots = \frac{1}{N} a^{ik} \frac{\partial G_{ik}}{\partial q^j}
   $$
   
   $a^{ik}$ - алгебраическое дополнение к $G_{ik}$. По теореме о структуре обратных матриц:
   
   $$
   a^{ik} = G^{ki} \det{\hat{G}}
   $$

   $$
   \frac{\partial \det \hat{G}}{\partial q^j} = \frac{\det{\hat{G}}}{N}G^{ki} \frac{\partial G_{ik}}{\partial q^j} = \frac{\det{\hat{G}}}{N}G^{ki} \left[\Gamma^r_{i,j} G_{rk} + \Gamma^r_{k,j} G_{ir}\right] =  \frac{2\det{\hat{G}}}{N} \Gamma^i_{i,j}
   $$

   В частности отсюда следует, что:
   
   $$
   \Gamma^i_{i, j} = \frac{N}{2} \frac{\partial \ln \det \hat{G}}{\partial q^j}
   $$
   
**Мне не мешало бы переработать этот материал в свете последних данных. Здесь есть и неявные нули, и то, что просто никуда не годится. И хотя уравнения криволинейных изопространств теперь есть в моём рукаве, они далеки от совершенства, а решать их, я тем более не умею...**

