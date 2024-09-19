 # Lec 2



Q: data modality?

- Discrete vectorized data like stock, health, energy....







midterm * 2

final ?

more and more challenging






$$
y = {y_k, k \in \N}
\\
y_k = \phi y_{k-1} + \ q
$$







the course is first time, and prof is first to teach it 

all the notes are written by himself

lack of proper ways to suggests & hw submission?



propose the idea and request certain variation

don't spend too much time!





## Example 5: (Asymptotic) Autocovariance of AR(1)

这段课件讨论了一阶自回归过程（AR(1)）的**渐近自协方差（Asymptotic Autocovariance）**和**自相关性（Autocorrelation）**。

### 1. AR(1)过程定义：
AR(1)过程的定义为递推方程：
\[ Y_k = \phi Y_{k-1} + \epsilon_k \quad \text{with} \ |\phi| < 1 \]
其中，\( \epsilon_k \) 是均值为零、方差为 \( \sigma_{\epsilon}^2 \) 的白噪声。

### 2. 渐近性质：
- 在小 \( k \) 时，由于确定性的初始条件，AR(1)过程不是平稳的。此时，方差会增长。
- 当 \( k \) 变大时，AR(1)过程逐渐变为**宽平稳过程（WSS, Wide Sense Stationary）**，即均值为零，方差趋于一个常数：
  \[ \lim_{k \to \infty} \text{Var}(Y_k) = \frac{\sigma_{\epsilon}^2}{1 - \phi^2}. \]
  这表明初始条件的影响随着时间衰减，最终消失。

### 3. 自协方差推导：
AR(1)的自协方差表示为 \( \text{Cov}(Y_k, Y_{k-h}) \)，通过递推方程 \( Y_k \) 和 \( Y_{k-h} \) 的展开式，以及数学期望的计算，得到：
\[
\text{Cov}(Y_k, Y_{k-h}) = \phi^h \frac{\sigma_{\epsilon}^2}{1 - \phi^2}.
\]
这个结果表明，自协方差只与滞后 \( h \) 有关，且随着 \( h \) 的增加呈指数衰减。

### 4. 自相关函数：
自相关函数（Autocorrelation Function，ACF）是归一化后的自协方差：
\[ R_Y(h) = \phi^h, \]
这意味着当 \( |\phi| < 1 \) 时，AR(1)过程的自相关性随着 \( h \) 增加指数衰减，并趋于零，表明过程中的观测值随着时间间隔的增加变得不相关。

### 5. 图示解释：
- **左图**展示了AR(1)过程的一个样本路径，其中波动的特性符合白噪声的性质。
- **右图**展示了AR(1)过程的经验自相关函数与理论自相关函数的对比。可以看到，理论自相关函数（红线）呈指数衰减，与经验值（蓝点）有良好的一致性。

总结来说，这段课件主要讲解了AR(1)过程的渐近统计特性，特别是其自协方差和自相关函数随时间滞后呈现的指数衰减趋势。


$$
f_{Y_k | \mathcal{F}_{k-1}}(Y_k \mid Y_{k-1} = y_{k-1}, Y_{k-2} = y_{k-2}, Y_{k-3} = y_{k-3}, \dots) 

$$
