## Supporting Material A Molecular Dynamics Study of Silicon Atomic Layer Etching by Chorine Gas and Argon Ions

Joseph R. Vella, † David Humbird, ‡ and David B. Graves ∗ , ¶

† Princeton Plasma Physics Laboratory, Princeton, NJ 08540 USA ‡ DWH Consulting, Centennial, CO 80112 USA

¶ Princeton Plasma Physics Laboratory, Princeton, NJ 08540 USA and Department of Chemical and Biological Engineering,Princeton University, Princeton, NJ 08540 USA

E-mail: dgraves@pppl.gov

January 12, 2022

## SI. REBO Force Field

Si-Si, Si-Cl, and Cl-Cl interactions are described using the REBO potential. The REBO potential describes the total potential energy of a collection of atoms by a sum over bond energies,

$$U = \sum _ { i } \sum _ { j > i } \phi _ { i j }.$$

In this equation, U is the total potential energy and φ ij is the bond energy between atoms i and j . The bond energy is described as a sum of a repulsive component ( V ij R ) and attractive component, ( V ij A ):

$$\phi _ { i j } = V _ { R } ^ { i j } - \overline { b _ { i j } } V _ { A } ^ { i j }.$$

b ij is the bond order term used to scale the attractive component. The repulsive contribution is described by the functional form:

$$V _ { R } ^ { i j } ( r _ { i j } ) = \left \lceil \begin{array} { c c } \frac { z _ { i } z _ { j } e ^ { 2 } } { 4 \pi \varepsilon _ { 0 } r _ { i j } } \left ( \sum _ { i = 1 } ^ { 3 } c _ { i } \exp \left ( - \frac { d _ { i } r _ { i j } } { a } \right ) \right ) + s \\ c _ { R } + \exp \left ( a _ { R } r _ { i j } + b _ { R } \right ) & r _ { a } < r _ { i j } \leq r _ { b } \\ f _ { i j } ( r _ { i j } ) A _ { i j } \exp ( - \lambda _ { i j } r _ { i j } ) & r > r _ { b }, \end{array}$$

where r ij is the distance between atoms i and j , f ij is a switching function that smoothly turns interactions off near the cut-off, s, a R , b R , and x R , λ ij , A ij , r a , and r b are two-body fitting parameters. Z i is the nuclear charge of atom i , e is the elementary charge, ε 0 is the permittivity of free space. a is the screening length (in ˚ ) given by: A

$$a = 0. 8 3 \left ( \frac { 9 \pi ^ { 2 } } { 1 2 8 } \right ) ^ { 1 / 3 } ( 0. 5 2 9 2 ) \left ( Z _ { i } ^ { 0. 5 } + Z _ { j } ^ { 0. 5 } \right ) ^ { - 2 / 3 }.$$

c i values are (0.35,0.55,0.1) and d i values are (0.3,1.2,6.0). The two-body fitting parameters for the repulsive portion of the potential are given in Table S0.

Table S1: Two-body Parameters for the Repulsive Potential.

| Interaction    |       Si-Si |      Si-Cl |      Cl-Cl |
|----------------|-------------|------------|------------|
| r a , ˚ A      |    0.286968 |    0.3     |    0.3     |
| r b , ˚ A      |    0.6522   |    0.8     |    0.8     |
| a R , ˚ A - 1  |   -7.15538  |   -7.10844 |   -5.09352 |
| b R            |    9.50221  |    9.62296 |    9.51683 |
| c R , eV       |  237.362    |   77.7667  |   62.4821  |
| s , eV         |  296.793    |  106.164   |  948.059   |
| A ij , eV      | 1830.8      | 1234.01    | 7248.25    |
| λ ij , ˚ A - 1 |    2.4799   |    2.8229  |    4.0088  |

The attractive contribution is given by:

$$V _ { A } ^ { i j } ( r _ { i j } ) = f _ { i j } ( r _ { i j } ) B _ { i j } \exp ( - \mu _ { i j } r _ { i j } ),$$

where B ij and µ ij are two-body fitting parameters. The two-body fitting parameters for the attractive portion of the potential are given in Table S2.

Table S2: Two-body Parameters for the Attractive Potential.

| Interaction    |    Si-Si |    Si-Cl |    Cl-Cl |
|----------------|----------|----------|----------|
| B ij , eV      | 471.18   | 142.606  | 269.71   |
| µ ij , ˚ A - 1 |   1.7322 |   1.4114 |   2.0044 |

The switching function is given by:

$$f _ { i j } ( r _ { i j } ) = S \left ( \frac { r _ { i j } - r _ { i j } ^ { m i n } } { r _ { i j } ^ { m a x } - r _ { i j } ^ { m i n } } \right ) = S ( t ) = \begin{cases} \ 1 & \ t \leq 0 \\ 1 - t ^ { 3 } ( 6 t ^ { 2 } - 1 5 t + 1 0 ) & 0 < t < 1 \\ 0 & \ t \geq 1, \end{cases} \\ \i. \cdots \ m i n \, \cdots \, \cdots \, \cdots \, \cdots \, \cdots \, \cdots \, \cdots \, \cdots \, \cdots \, \cdots \, \cdots \, \cdots \, \cdots \, \cdots \, \cdots \, \cdots \, \cdots \, \cdots \, \cdots \, \cdots \, \cdots \, \cdots \, \cdots \, \cdots \, \cdots \, \cdots \, \cdots \, \cdots \, \cdots \, \cdots \, \cdots \, \cdots \, \cdots \, \cdots \, \cdots \, \cdots \, \cdots \, \cdots \, \cdots \, \cdots \, \cdot \end{cases}$$

where r min ij and r max ij are pair-wise specific cut-off parameters. The cut-off parameters for the switching function are given in Table S3.

Table S3: Cut-Off Parameters for the Switching Function.

| Interaction    |   Si-Si |   Si-Cl |   Cl-Cl |
|----------------|---------|---------|---------|
| r min ij , ˚ A |     2.7 |    2.32 |   2.284 |
| r max ij , ˚ A |     3   |    2.62 |   2.584 |

We now focus on the bond order, b ij , term introduced in Equation S2. This term is calculated as the average of the i j -and j i -bond orders:

$$\overline { b _ { i j } } = \frac { 1 } { 2 } [ b _ { i j } + b _ { j i } ],$$

where b ij is calculated by considering the contributions of atoms that neighbor atom i with:

$$b _ { i j } = \left \lceil 1 + \left [ \zeta _ { i j } + H _ { i j } \left ( N _ { i j } ^ { ( C l ) }, N _ { i j } ^ { ( S i ) } \right ) \right ] ^ { \eta _ { i j } } \right \rceil ^ { - \delta _ { i j } }.$$

η ij and δ ij are fitting parameters. ζ ij is calculated using the equation:

$$\zeta _ { i j } = \sum _ { k \neq j } f _ { i k } ( r _ { i j } ) \left [ c _ { i j } ^ { b } + d _ { i j } ^ { b } [ H _ { i j } ^ { b } + \cos ( \theta _ { i j k } ) ] \right ] \exp \left [ \alpha _ { i j } \left [ ( r _ { i j } - R _ { i j } ^ { ( e ) } ) - ( r _ { i k } - R _ { i k } ^ { ( e ) } ) \right ] ^ { \beta _ { i j } } \right ].$$

θ ijk is the angle between atoms i , j , and k . R ( e ) ij is the equilibrium dimer bond length between the atom types of atom i and j . c b ij , d b ij , h b ij , α ij , and β ij are all fitting parameters. The fitting parameters for the bond order term are given in Table S4.

Table S4: Fitting Parameters for the Bond Order Term.

| Interaction      |    Si-Si |    Si-Cl |   Cl-any |
|------------------|----------|----------|----------|
| η ij             |  0.78734 |  1       |   1      |
| δ ij             |  0.63505 |  0.80469 |   0.5    |
| c b ij           |  0       |  0.0216  |   4      |
| d b ij           |  0.16    |  0.27    |   0      |
| h b ij           | -0.59826 | -0.047   |   0      |
| α ij , ˚ A - 3   |  5.19749 |  4       |   6      |
| β ij             |  3       |  3       |   1      |
| R ( e ) ij , ˚ A |  2.35    |  2.019   |   1.9878 |

Finally, H ij is the Brenner correction function. Values of the function at specified nodes are given in Table S5.

Table S5: Values of Brenner correction function at integer points. All values not given are 0. Derivatives (not shown but required for bicubic interpolation) are found by 2nd order finite differences.

|   x |   y |   H SiCl ( x, y ) |
|-----|-----|-------------------|
|   0 |   2 |            -0.05  |
|   0 |   3 |            -0.11  |
|   1 |   0 |            -0.088 |
|   1 |   2 |            -0.06  |
|   2 |   0 |             1.09  |
|   2 |   1 |             0.015 |
|   3 |   0 |            -0.068 |
