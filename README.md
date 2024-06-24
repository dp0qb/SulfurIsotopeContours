## 热液系统硫同位素等值线计算过程
**注：由于网页对Latex公式支持不完整，部分公式无法正常显示。要查看正确内容请点击"README.pdf"文件下载。**

author:郭荣强

date:2023.06.26

email:guorq22@mails.jlu.edu.cn

### 1.硫同位素分馏

~~个人理解~~：在化学反应中，同种元素不同同位素会表现出不同性质。性质的差异对轻、重同位素进入各种物质中的比例产生影响，称为**同位素分馏**。

更为官方的解释：某元素的同位素在物理、化学、生物等反应过程中以不同比例分配于不同物质之中的现象称为**同位素分馏**。

### 2. 同位素分馏系数($\alpha$)

两种物质之间同位素分馏程度用$\alpha$表示，如氧同位素在A、B的分馏系数：
$$\rm \alpha_{A-B} = \frac{R_A}{R_B} = \frac{(\frac{^{18}O}{^{16}O})_A}{(\frac{^{18}O}{^{16}O})_B}$$

式中，A和B表示两种物质或同一物质两种相态。同位素分馏系数表示了**同位素分馏的程度**，它反映了两种物质之间同位素相对富集或亏损的大小。

1. $\rm \alpha _{A-B} > 1 \Rightarrow \quad$ A物质比B物质富集重同位素；
2. $\rm \alpha _{A-B} < 1 \Rightarrow \quad$ A物质比B物质富集轻同位素；
3. $\rm \alpha _{A-B} = 1 \Rightarrow \quad$ 两种物质之间没有同位素分馏。

稳定同位素组成常用$\delta$值表示，$\delta$值指样品中某元素的稳定同位素比值相对标准（标样）相应比值的千分偏差。其公式为：
$$\rm \delta_x = 1000(\frac{R_x - R_{std}}{R_{std}})$$

$\delta$值能清楚地反映同位素组成的变化，样品的$\delta$值愈高，反映重同位素愈富集。

样品的$\delta$值总是相对于某个标准而言的，同一个样品，对比的标准不同得出的$\delta$值各异。所以必须采用同一标准；或者将各实验室的数据换算成国际公认的统一标准，这样获得的$\delta$值才有实际套用价值。比较普遍的国际公认标准为：

1. **SMOW**，即标准平均海洋水，作为氢和氧的同位素的国际统一标准；
2. **PDB**，是美国南卡罗来纳州白垩系皮狄组地层内的似箭石，一种碳酸钙样品，用作碳同位素的国际统一标准，有时也作为沉积碳酸盐氧同位素的标准；
3. **CDT**,是美国亚利桑纳州迪亚布洛峡谷铁陨石中的陨硫铁，用作硫同位素的国际统一标准。

稳定同位素实验研究表明，大多数矿物对体系（矿物-矿物）或矿物-水体系，在有地质意义的温度范围内,$10 ^ 3 \ln \alpha$值与$T ^ 2$成反比,T为绝对温度。

$10 ^ 3 \ln \alpha$值可以近似地用两种物质的$\delta$差值表示,存在:

$$\rm \Delta_{A-B} = \delta_A - \delta_B \approx 10 ^ 3 \ln \alpha _{A-B}$$


其中：
1. $\rm \Delta _{A-B} > 0 \Rightarrow \quad$ A物质比B物质富集重同位素；
2. $\rm \Delta _{A-B} < 0 \Rightarrow \quad$ A物质比B物质富集轻同位素；
3. $\rm \Delta _{A-B} = 0 \Rightarrow \quad$ 两种物质之间没有同位素分馏。

因此,只要测得样品的$\delta$值,就可直接计算出$10 ^ 3 \ln \alpha$值。它同样表示物质间同位素分馏程度的大小，利用它可绘制同位素分馏曲线，计算同位素平衡温度(见地质温度计)。在稳定同位素地球化学研究中，H、C、O、S等研究较深入。它们在天然物质中分布广泛，可形成多种化合物，由于它们的同位素质量数都比较小，相对质量差别大，因而同位素分馏更明显，这对确定地质体的成因及其物质来源和判明地质作用特征具有重要意义。

### 分馏系数与温度的关系

从理论和实践上都已证明，地质体中共生矿物之间，其同位素分馏系数是温度的函数。根据大量理论和实验测定，得出其关系式为：
$$\rm 10^3 \ln \alpha _{a-b} = A * 10^6 / T^2 + B$$
其中：
$\alpha$：同位素分馏系数（a和b为两种物质或同一物质两种相态）；
T：绝对温度；
A,B：常数，随矿物对类型变化，一般用实验方法求得。

在上式中，只要测出$\rm \delta _a$和$\rm \delta _b$，并且已知常数A和B，就可算出温度T，即作为地质温度计使用。
反之，假设地质温度T，则可以得到对应的$\rm \delta _a$和$\rm \delta _b$，进而进行对应条件下的模拟。

### 热液系统中的硫同位素分馏

在低于$\rm 500\degree C$的热液系统中，稳定的含硫组分主要包含$\rm H_2S_{(aq)}$，$\rm S^{2-}$，$\rm HS^-$，$\rm HSO_4^-$，$\rm SO_4^{2-}$，$\rm KSO_4^{2-}$，$\rm NaSO_4^{2-}$，$\rm CaSO_4$及其他硫酸盐.

以上组分之间存在如下反应：

$$\ce{H2S(aq) <=> H+ + HS-}\\
\ce{HS- <=> H+ + S^2-}\\
\ce{2H+ + SO4^2- <=> H2S(aq) + 2O2}\\
\ce{HSO4- <=> H+ + SO4^2-}\\
\ce{KSO4- <=> K+ + SO4^2-}\\
\ce{NaSO_4^- <=> Na+ + SO4^2-}\\
\ce{CaSO_4 <=> Ca^2+ + SO4^2-}$$

由上述反应可以得到：
$\rm m_{HS^-} = m_{H_2S} * \frac{K_{H_2S} * \gamma_{H_2S}}{\gamma_{HS^- * a_{H^+}}} = m_{H_2S} * A$

$\rm m_{S^{2-}} = m_{HS^-} * \frac{K_{HS^-}*\gamma_{HS^-}}{a_{H^+} * \gamma_{S^{2-}}} = m_{H_2S} * A * B$

$\rm m_{SO_4^{2-}} = m_{H_2S} * \frac{(f_{O_2})^2 * \gamma_{H_2S}}{K_{SO_4^{2-}} * (a_{H^+})^2 * \gamma_{SO_4^{2-}}} = m_{H_2S} * C * D$

$\rm m_{HSO_4^-} = m_{SO_4^{2-}} * \frac{a_{H^+}}{K_{HSO_4^-}*\gamma_{HSO4^-}} = m_{H_2S} * C * E$

$\rm m_{KSO_4^-} = m_{SO_4^{2-}} * \frac{m_{K^+} * \gamma_{K^+}}{K_{KSO_4^-}*\gamma_{KSO4^-}} = m_{H_2S} * C * F$

$\rm m_{NaSO_4^-} = m_{SO_4^{2-}} * \frac{m_{Na^+} * \gamma_{Na^+}}{K_{NaSO_4^-}*\gamma_{NaSO4^-}} = m_{H_2S} * C * G$

$\rm m_{CaSO_4} = m_{SO_4^{2-}} * \frac{m_{Ca^{2+}} * \gamma_{Ca^{2+}}}{K_{CaSO_4}*\gamma_{CaSO4}} = m_{H_2S} * C * H$

其中：

$\rm A = \frac{K_{H_2S} * \gamma_{H_2S}}{\gamma_{HS^- * a_{H^+}}}$

$\rm B = \frac{K_{HS^-}*\gamma_{HS^-}}{a_{H^+} * \gamma_{S^{2-}}}$

$\rm C = \frac{(f_{O_2})^2 * \gamma_{H_2S}}{K_{SO_4^{2-}} * (a_{H^+})^2}$

$\rm D = \frac{1}{\gamma_{SO_4^{2-}}}$

$\rm E = \frac{a_{H^+}}{K_{HSO_4^-}*\gamma_{HSO4^-}}$

$\rm F = \frac{m_{K^+} * \gamma_{K^+}}{K_{KSO_4^-}*\gamma_{KSO4^-}}$

$\rm G = \frac{m_{Na^+} * \gamma_{Na^+}}{K_{NaSO_4^-}*\gamma_{NaSO4^-}}$

$\rm H = \frac{m_{Ca^{2+}} * \gamma_{Ca^{2+}}}{K_{CaSO_4}*\gamma_{CaSO4}}$

K为对应反应的平衡常数，可通过查表或软件计算获得。$\gamma$值为活度系数，可以用Debye-Huckel公式计算，也可查表获得。$\rm mK^+$、$\rm mNa^+$和$\rm mCa^+$一般根据需要设定。$\rm aH^+$为氢离子浓度，和pH有如下关系：
$$\rm pH = -\log aH^+$$

因为：
$$\rm m_{\sum S}= m_{H_2S}+m_{HS^-}+m_{S^{2-}}+m_{SO_4^{2-}}+m_{HSO_4^-}+m_{KSO_4^-}+m_{NaSO_4^-}+m_{CaSO_4}$$

且其它组分均可用$\rm m_{H_2S}$表示，所以上式可表示为：
$$\rm m_{\sum S}= m_{H_2S} * [1 + A *(1+B)+ C *(D + E + F + G + H)]$$

即：
$$\rm m_{H_2S}= \frac{m_{\sum S}}{1 + A *(1+B)+ C *(D + E + F + G + H)}$$

而各组分摩尔分数X满足：
$$\rm X_i = \frac{m_i}{\sum S}$$

所以：
$\rm X_{H_2S}= \frac{1}{1 + A *(1+B)+ C *(D + E + F + G + H)}$

$\rm X_{HS^-}= \frac{A}{1 + A *(1+B)+ C *(D + E + F + G + H)}$

$\rm X_{S^{2-}}= \frac{A*B}{1 + A *(1+B)+ C *(D + E + F + G + H)}$

$\rm \begin{aligned}
X_{\sum SO_4^{2-}} = & X_{SO_4^{2-}} + X_{HSO_4^-} + X_{KSO_4^-} + X_{NaSO_4^-} + X_{CaSO_4^-}\\
= & \frac{C *(D + E + F + G + H)}{1 + A *(1+B)+ C *(D + E + F + G + H)}
\end{aligned}$

该系统中硫同位素和分馏系数之间的关系为：
$$\rm \begin{aligned}
        \delta S _{\sum S} ^{34} = &(\delta S _{H_2S} ^{34} \cdot X _{H_2S}) + (\delta S _{HS^-} ^{34} \cdot X _{HS^-}) + (\delta S _{S^{2-}} ^{34} \cdot X _{S^{2-}})\\
        & + (\delta S _{SO_4^{2-}} ^{34} \cdot X _{SO_4^{2-}}) + (\delta S _{HSO_4^-} ^{34} \cdot X _{HSO_4^-}) + (\delta S _{KSO_4^-} ^{34} \cdot X _{KSO_4^-})\\
        & + (\delta S _{NaSO_4^-} ^{34} \cdot X _{NaSO_4^-}) + (\delta S _{CaSO_4} ^{34} \cdot X _{CaSO_4})
\end{aligned}$$

在**分馏系数与温度的关系**中提到的公式：
$$\rm \Delta_{A-B} = \delta_A - \delta_B \approx 10 ^ 3 \ln \alpha _{A-B}$$

为方便表示，将其它组分i和$\rm H_2S$之间的分馏系数简写为$\rm \Delta _i$，例如：
$$\rm \Delta_{HS^-} = \delta S_{HS^-} ^{34} - \delta S _{H_2S} ^{34}$$

也即：
$$\rm \delta S_{HS^-} ^{34}  = \Delta_{HS^-} + \delta S _{H_2S} ^{34}$$

由前人经验，有：
$$\rm \Delta_{SO_4^{2-}} \approx \Delta_{HSO_4^-} \approx \Delta_{KSO_4^-} \approx \Delta_{NaSO_4^-} \approx \Delta_{CaSO_4}$$

于是硫同位素和分馏系数又可表示为：
$$\rm \begin{aligned}
\delta S _{\sum S} ^{34} = &(\delta S _{H_2S} ^{34} \cdot X _{H_2S}) + [(\Delta_{HS^-} + \delta S _{H_2S} ^{34}) * X_{HS^-}]\\
& + [(\Delta_{S^{2-}} + \delta S _{H_2S} ^{34}) * X_{S^{2-}}] + [(\Delta_{\sum SO_4^{2-}} + \delta S _{H_2S} ^{34}) * X_{\sum SO_4^{2-}}]
\end{aligned}$$

因为：
$$\rm X _{H_2S} + X_{HS^-} + X_{S^{2-}} + X_{\sum SO_4^{2-}} = 1$$

所以：
$$\rm \delta S _{\sum S} ^{34} = \delta S _{H_2S} ^{34} + (\Delta_{HS^-} * X_{HS^-}) + (\Delta_{S^{2-}}  * X_{S^{2-}}) + (\Delta_{\sum SO_4^{2-}} * X_{\sum SO_4^{2-}})$$

在该式中，$\rm \delta S _{\sum S} ^{34}$一般设为0，即标准值，$\rm \delta S _{H_2S} ^{34}$可以设定不同的值。$\rm \Delta_{HS^-}$、$\rm \Delta_{S^{2-}}$、$\rm \Delta_{\sum SO_4^{2-}}$都是关于温度的函数，可以通过公式计算或查表获得。再将$\rm X_{HS^-}$、$\rm X_{S^{2-}}$、$\rm X_{\sum SO_4^{2-}}$代入，即可得到特定温度下$\rm f_{O_2}$和aH的关系式。经过整理可得：
$$\rm \log f_{O_2} = log \sqrt{
    \frac
    {(\delta S _{\sum S} ^{34} - \delta S _{H_2S} ^{34}) * [1 + A*(1+B)] - \Delta_{HS^-} * A - \Delta_{S^{2-}} * A * B}
    {[\Delta_{SO_4^{2-}} - (\delta S _{\sum S} ^{34} - \delta S _{H_2S} ^{34})] * (D + E + F + G + H)}
}$$

由该式即可绘制$\rm \log f_{O_2} - pH$等值线。

### 等值线绘制

**安装依赖**
```
    pip install -r requirements.txt
```

**运行**

```
    import CalcDeltaS as cds

    T_c = 250
    delta_totalS = 5.0
    plot_species = "FeS2"
    delta_list = [-5, 1.8, 2.9, 3.6, 3.9, 6.0]
    ranges = {
        "pH": {
                350: (5.085, 6.400),
                300: (5.113, 6.517),
                250: (5.751, 6.621),
                0: (2, 12)
        },
        "log_fo2" : {
            350: (-36, -18),
            300: (-40, -22),
            250: (-46, -28)
        }
    }
    # default_ph_range的取值范围和底图一致即可
    default_ph_range = (2, 12)
    # use_default_ph_range为True时，将会取default_ph_range的ph范围，适合用来画图；
    # 该值为False时，ph范围会随着ranges里的ph改变，适合用来计算精确log_fO2值。
    use_default_ph_range = True
    print(f"{T_c} degree")
    cds.main(T_c, delta_totalS, plot_species, delta_list, ranges["log_fo2"][T_c], ranges["pH"][T_c], default_ph_range=default_ph_range, use_default_ph_range=use_default_ph_range)
```

T_c为系统的温度（摄氏度/°C）;
delta_totalS为体系的$\rm\delta S _{\sum S} ^{34}$值；
plot_species为要绘制等值线的矿物或气体、离子等，附带的数据支持:'H2S', 'HS', 'S', 'HSO4', 'SO4', 'KSO4', 'NaSO4', 'CaSO4', 'FeS', 'ZnS', 'FeS2', 'PbS'；
delta_list中为等值线每条线对应的值。


**注：** 部分认识尚未完善，待续。