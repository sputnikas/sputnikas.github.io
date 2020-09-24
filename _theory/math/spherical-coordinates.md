---
layout: theory_page
title: Сферические координаты в N-мерном случае
permalink: /math/spherical_coordinates/
previous_page: /theory/
next_page: /theory/
---

Определение:

$$
	\begin{aligned}
	& x_1 = r \cos \theta_1 
	& x_1 \in (-\infty, \infty) \Rightarrow \theta_1 \in (0, \pi)\\
	& x_2 = r \sin \theta_1 \cos \theta_2 
	& x_2 \in (-\infty, \infty) \Rightarrow \theta_2 \in (0, \pi)\\
	& \ldots \\
	& x_{N - 1} = r \sin \theta_1 \sin \theta_2 \cdot \ldots \cdot \sin \theta_{N - 2} \cos \theta_{N-1} 
	& x_{N - 1} \in (-\infty, \infty) \Rightarrow \theta_{N - 1} \in (0, \pi)\\
	& x_{N} = r \sin \theta_1 \sin \theta_2 \cdot \ldots \cdot \sin \theta_{N - 2} \sin \theta_{N-1} 
	& \text{ НО: } x_{N} \in (-\infty, \infty) \Rightarrow \theta_{N - 1} \in (0, 2 \pi)
	\end{aligned}
$$

$$
	r = \sqrt{x_1^2 + x_2^2 + \ldots + x_N^2} > 0
$$

Якобиан:

$$
	J = 
	\frac{\partial(x_1, x_2, \ldots, x_N)}{\partial(r, \theta_1, \theta_2, \ldots, \theta_{N- 1})} =
	\begin{vmatrix}
	\cos \theta_1 & 
	- r \sin \theta_1 & 
	0 & 
	0 & 
	\ldots & 
	0 \\
	\sin \theta_1 \cos \theta_2 &
	r \cos \theta_1 \cos \theta_2 &
	- r \sin \theta_1 \sin \theta_2 &
	0 &
	\ldots &
	0 \\
	\sin \theta_1 \sin \theta_2 \cos \theta_3 &
	r \cos \theta_1 \sin \theta_2 \cos \theta_3 &
	r \sin \theta_1 \cos \theta_2 \cos \theta_3 &
	- r \sin \theta_1 \sin \theta_2 \sin \theta_3 &
	\ldots &
	0 \\
	\ldots &
	\ldots &
	\ldots &
	\ldots &
	\ldots &
	\ldots \\
	\end{vmatrix}
$$

Выносим $r$ за знак определителя, раскладываем по первой строке и выносим всё, что можно вынести за знак определителя:

$$
	\begin{gathered}
	J = r^{N - 1} J_N(\theta_1, \ldots, \theta_{N - 1}) = 
	r^{N - 1} [\cos^2 \theta_1 \sin^{N - 2} \theta_1 J_{N - 1}(\theta_2, \ldots, \theta_{N - 1}) + \sin^N \theta_1 J_{N - 1}(\theta_2, \ldots, \theta_{N - 1})]  =  
	\\ =
	r^{N - 1} \sin^{N - 2} \theta_1 J_{N - 1}(\theta_2, \ldots, \theta_{N - 1})
	\\ =
	r^{N - 1} \sin^{N - 2} \theta_1 \sin^{N - 3} \theta_2 \cdot \ldots \cdot \sin \theta_{N - 2}
	\end{gathered}
$$

Площадь гиперсферы:

$$
	S_N = \int\limits_{\theta} r^{N - 1} \sin^{N - 2} \theta_1 \sin^{N - 3} \theta_2 \cdot \ldots \cdot \sin \theta_{N - 2} d\theta_1 \ldots d\theta_{N - 1}
$$

Воспользуемся соотношением:

$$
	\int\limits_0^\pi \sin^k x dx = \frac{\Gamma\left(\frac{k + 1}{2}\right)}{\Gamma\left(\frac{k + 2}{2}\right)} \pi^{1/2}
$$

$$
	S_N = 2 \pi r^{N - 1} \pi^{(N - 2)/2} \frac{\Gamma(1)}{\Gamma\left(\frac{N}{2}\right)} =
	\frac{2 \pi^{N/2}}{\Gamma\left(N/2\right)} r^{N - 1}
$$

Объём гипершара:

$$
	V_N = \int\limits_0^r S_N dr = \frac{2 \pi^{N/2}}{N\Gamma\left(N/2\right)} r^{N} =
	\frac{\pi^{N/2}}{\Gamma\left((N + 2)/2\right)} r^{N}
$$

Элемент площади в случае цилиндрической симметрии для гиперсферы:

$$
	\begin{gathered}
	dS_N = r^{N - 1} \sin^{N - 2} \theta \, d\theta \int\limits_{\theta} \sin^{N - 3} \theta_2 \cdot \ldots \cdot \sin \theta_{N - 2} d\theta_2 \ldots d\theta_{N - 1} 
	= \\ = 
	2 \pi \frac{\pi^{(N - 3)/2}}{\Gamma((N - 1)/2)} r^{N - 1} \sin^{N - 2} \theta \, d\theta =
	\frac{2 \pi^{(N - 1)/2}}{\Gamma((N - 1)/2)} r^{N - 1} \sin^{N - 2} \theta \, d\theta
	\end{gathered}
$$