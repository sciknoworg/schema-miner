Electronic Supplementary Material (ESI) for Physical Chemistry Chemical Physics.

This journal is © the Owner Societies 2019

## Supporting Information for

## Computational Modelling of Atomic Layer Etching of Chlorinated Germanium Surfaces by Argon

Shenli Zhang, a+  Yihan Huang,  a  Gulcin Tetiker  b , Saravanapriyan Sriraman b , Alex Paterson b  and

Roland Faller*  c

a. Department of Materials Science &amp; Engineering, University of California, Davis, One shields Avenue, Davis, 95616, CA, USA.

b. Lam Research Corporation, Fremont, CA 94538.

c. Department of Chemical Engineering, University of California, Davis, One shields Avenue, Davis, 95616, CA, USA.

+ Current address: Institute for Molecular Engineering, University of Chicago, 5640 S Ellis Ave, Chicago, IL, 60637, USA

## 1. Tersoff force field training

## 1.1. Discussion on the choice of the force field

Tersoff force field has been selected to describe the Ge-Cl interaction, because this bond order potential was originally calibrated for covalent elements including C, Si and Ge, 1-3  which have  similar  structural  and  chemical  properties. Improved  versions  of  Tersoff  have  been developed and used widely in C and Si reaction studies, 4-7  however we stick to the original version here for several reasons. First, some improvements are to achieve a better description for double and  conjugation  bond,  such  as  the  Brenner's  correction  terms  in  REBO  potential. 5   This  is important for carbon system. However, for either Si or Ge, due to their increased metallicity, double and conjugation bonds rarely form, and such corrections can be unnecessary. Second, previous studies noticed the Si-F bond energy trend has an abnormal value in SiF3 structure 4 similar to our GeCl3 case due to hybridization states(shown in section 1.3). A correction term in bond order bij can be added for better fitting the bond energies. 4, 8  However, due to our limited training data, the addition of such correction term leads to an overfitting problem, such that the bond energy change can be fit accurately, while the fitting accuracy of bond length and bond force constant both decrease. Since each property weighs differently based on the purpose of a simulation study, here we choose to lower the total fitting error (eq.1 in Fig. S1) instead of the bond energy term only. Further optimizations can be certainly made with more training data, and a different weighing on the target terms.

## 1.2.  The format

We used the following format as implemented in LAMMPS:

$$& \text{We used the following format as impleme} \\ E = \frac { 1 } { 2 } \sum _ { i \ j \neq i } V _ { i j } \\ V _ { i j } = f _ { c } ( r _ { i j } ) [ f _ { R } ( r _ { i j } ) + b _ { i j } f _ { A } ( r _ { i j } ) ] \\ f _ { c } ( r ) = \left \{ \frac { 1 } { 2 } - \frac { 1 } { 2 } \sin \left ( \frac { \pi r - R } { 2 } \right ) \colon R - D < r < R + D \right \} \\ 0 \colon r > R + D \right \} \\ f _ { R } ( r ) = A e x p ( - \lambda _ { 1 } r ) \\ f _ { A } ( r ) = - B e x p ( - \lambda _ { 2 } r ) \\ b _ { i j } = ( 1 + \beta ^ { n } \zeta _ { i j } ^ { n } ) ^ { - \frac { 1 } { 2 n } } \\ \zeta _ { i j } = \sum _ { k \neq i, j } f _ { c } ( r _ { i k } ) g ( \theta _ { i j k } ) e x p ^ { m } _ { i j } [ \lambda _ { 3 } ^ { 3 } ( r _ { i j } - r _ { i k } ) ^ { m } ] \\ g ( \theta ) = \gamma _ { i j k } ( 1 + \frac { c ^ { 2 } } { d ^ { 2 } } - \frac { c ^ { 2 } } { [ d ^ { 2 } + ( \cos \theta - \cos \theta _ { 0 } ) ^ { 2 } ] } \\ \\ \text{where } f _ { R } \text{ is a two-body repulsion term and } f _ { A }$$

$$\begin{matrix} \\ \end{matrix}$$

where fR is a two-body repulsion term and fA the attraction term. The bond order term bij is a three-body term added to the attraction part, which includes all neighbors j and k of atom i. fC is the interaction cutoff function to smoothly transit full interaction to zero. R-D and R+D is the inner and outer cutoff distance.

## 1.3. Training the parameters

Interaction parameters for Ge-Ge and Cl-Cl atom pairs are available from previous literature. 2, 4 So only Ge-Cl interaction terms need to be trained. To do this, two-body parameters A, , B 𝜆 1 and are first optimized against bond energy, force and force constant of several GeCln species 𝜆 2

(Table S1 and S2) from DFT calculation using the annealing algorithm similar to previous studies, as shown in Fig. S1 and S2.

Table S1 Training data for Cl-Ge-Cl configurations.

| Species     | Cl-Ge-Cl angle ( ) °   |   Ge-Cl bond distance ( ) Å |   Ge-Cl bond energy (eV) |   Force constant (N/m) |
|-------------|------------------------|-----------------------------|--------------------------|------------------------|
| Ge 2 Cl 6   | 109.47                 |                        2.23 |                     4.21 |                 117.72 |
| GeCl 4      | 109.47                 |                        2.22 |                     4.23 |                 163.41 |
| GeCl 3      | 108.69                 |                        2.27 |                     1.47 |                 109    |
| GeCl 2      | 101.09                 |                        2.3  |                     4.16 |                 141.26 |
| GeCl        | N/A                    |                        2.31 |                     3.28 |                 122.6  |
| Ge 4 H 9 Cl | N/A                    |                        2.32 |                     4.08 |                 131.67 |

Table S2 Training data for Ge-Ge-Cl configurations.

Figure S1 Annealing algorithm training scheme for two-body parameters.

| Species     |   Ge-Ge-Cl angle ( ) ° |   Ge-Ge distance ( ) Å | bond   | Ge-Ge energy (eV)   | bond   |
|-------------|------------------------|------------------------|--------|---------------------|--------|
| Ge 2 Cl 6   |                 109.78 |                   2.5  |        | 2.91                |        |
| Ge 4 H 9 Cl |                 104.21 |                   2.49 |        | /                   |        |

<!-- image -->

Figure S2 Local minimization scheme as mentioned in the annealing algorithm.

<!-- image -->

Eq.1 in Fig. S1 is our error function, which tries to minimize the difference in bond energy (E), force (which=0 as we require it to be during local minimization) and force constant (K) in multiple structures at their bond length (DFT value). The fitted results for the two-body parameters are shown in Table S3.

Table S3 Fitted two-body parameters using annealing algorithm. Rmin=R-D and Rmax=R+D are set to be the average value from Ge-Ge and Cl-Cl cutoff distances.

| Fitted Parameters   |    Ge-Cl |
|---------------------|----------|
| A (eV)              | 521.834  |
| B (eV)              |  62.9673 |
| 𝜆 1 ( Å - 1 )       |   2.3248 |
| 𝜆 2 ( Å - 1 )       |   0.9857 |
| 𝑟 𝑚𝑖𝑛 (Å)           |   2.53   |
| 𝑟 𝑚𝑎𝑥 (Å)           |   2.83   |

Bond energy and force constant calculated using the above fitted value are shown in Fig. S3 and Fig.  S4.  Notice  in  Fig.  S3,  GeCl 3 (bond  length  2.27 )  has  an  abnormal  shallow  bond strength Å comparing to other GeCln case, which is hard to capture with the basic Tersoff formalism.  Its low bond energy indicates its instability, as this product also seems hard to detect in reality. So one consequence of our current fitting is we overestimated the bond energy of GeCl3 and will make it one of the possible etching products.

Figure S3 Bond energy fitting curve.

<!-- image -->

Figure S4 Force constant fitting curve.

<!-- image -->

Once these two-body term parameters are fixed, the bond order value bij can be calculated (by setting force F=0) and used to train its parameters. Following previous literatures, 6  i-j-k atom type combinations can be categorized in the way shown in Table S4.

Table S4 Data set for different i-j-k atom type combinations.

| Ge   | Ge   | Ge       | Ge Tersoff a                    | Ge Tersoff a                   |
|------|------|----------|---------------------------------|--------------------------------|
| Ge   | Ge   | Cl       | Ge Tersoff a                    | Ge Tersoff a                   |
| Cl   | Cl   | Cl or Ge | Cl with others & Cl- Cl David b | Cl with others & Cl- ClDavid b |
| Cl   | Ge   | Cl       | Fitting data                    | Ge Tersoff a                   |
| Cl   | Ge   | Ge       | Fitting data                    | Ge Tersoff a                   |
| Ge   | Cl   | Ge       | Fitting data                    | Cl with others & Cl- ClDavid b |
| Ge   | Cl   | Cl       | Fitting data                    | Cl with others & Cl- ClDavid b |

- a Tersoff, PRB, 39.8 (1989):5566-5568
- b David Humbird and David B. Graves, JCP, 120, 2405 (2004)
- * The three-body term parameters in g( , along with m and , are approximated to the values in 𝜃 ) 𝜆 3 either Ge-Ge-Ge or Cl-Cl-Cl case, depending on the central atom type, since their angles are within 10 ° difference  and  bij  values  within  0.2  difference.  Also,  the  number  of  training  data  is  far  less  than  the number of parameters, so some of the parameters need be fixed and this is a reasonable approximation.

<!-- image -->

Least square optimization is used to fit the different parameter sets. Training results are shown in the following.

Figure S5 Training results for Cl-Ge-Cl case.

<!-- image -->

-  Training results for Ge-Ge-Cl case

Target bij: 0.9507, trained bij:0.9879

-  Training results for Cl-Ge-Ge case

Target bij: 0.8188, trained bij: 0.7978

Table S5 Fitted parameters in bond order bij term.

| j-i-k Parameters   |       Cl-Ge-Cl |        Cl-Ge-Ge |   Ge-Cl-Ge |   Ge-Cl-Cl |      Ge-Ge-Cl |
|--------------------|----------------|-----------------|------------|------------|---------------|
| m                  |      3         |      3          |          1 |          1 |      3        |
| 𝛾 𝑖𝑗𝑘              |      1         |      1          |          4 |          4 |      1        |
| 𝜆 3                |      0         |      0          |          6 |          6 |      0        |
| 𝑐                  | 106430         | 106430          |          0 |          0 | 106430        |
| 𝑑                  |     15.652     |     15.652      |          1 |          1 |     15.652    |
| 𝑐𝑜𝑠𝜃 0             |     -0.43884   |     -0.43884    |          1 |          1 |     -0.43884  |
| n                  |      2.23669   |      0.67543    |          1 |          1 |      0.75627  |
| 𝛽                  |      0.0001234 |      1.0273e-05 |          1 |          1 |      9.02e-07 |

## 2. Ge surface relaxation at room temperature

The Ge surface was equilibrated under NPT condition (T=300 K, anisotropic zero pressure in x and y direction (the surface plane)). As shown in Fig. S6 a) and b), the original minimization leads to a Ge lattice constant of 5.657 Å (exp: 5.652 Å, 9  DFT: 5.668 Å). At 300 K, some surface dimers  appear  to  form  (2x1)  reconstruction  (Fig.  S6  c)  and  d)),  consistent  to  experimental observations. 10  The simulated average dimer bond length is 2.53 Å (averaged over 15 dimers, with standard deviation=0.077 Å ), fits well to the DFT value of 2.53 Å and experimental value between 2. 42 Å 10 and 2.55 Å 11

Figure S6 Ge surface minimization a) top view b) side view. Ge surface equilibration at 300 K c) top view d) side view. Green atoms represent top Ge surface layer, red is for other layer Ge. x: [110], y:[-110], z:[001].

<!-- image -->

- 3. Other characterizations in chlorination and bombardment process

Figure S7 Etched products percentage (GeCl, GeCl2 and GeCl3) and element etched number change with Ar bombardment cycle for 10 eV and 25 eV chlorinated surface. The insets number on etched number graph shows the total etched Ge and Cl number. Sample 1 is used as an example here.

<!-- image -->

Figure S8 Product fraction (only consider GeCln products) of a) GeCl, b) GeCl2 and c) GeCl3, averaged from 3 samples with error bars added.

<!-- image -->

Table S6 Total etched product numbers after 200 Ar bombardment cycles under each condition

| 5 eV chlorination   | Ar 25 eV   | Ar 50 eV   | Ar 75 eV   | Ar 100 eV   |
|---------------------|------------|------------|------------|-------------|
| GeCl                | 13 7 ±     | 15 9 ±     | 49 6 ±     | 47 11 ±     |
| GeCl 2              | 2 1 ±      | 5 2 ±      | 8 3 ±      | 9 3 ±       |
| GeCl 3              | 0.3 0.5 ±  | 1 0.5 ±    | 2 ±0.5     | 2 ±0.5      |
| 10 eV chlorination  |            |            |            |             |
| GeCl                | 11 2 ±     | 26 5 ±     | 41 6 ±     | 44 2 ±      |
| GeCl 2              | 4 0.5 ±    | 9 0 ±      | 11 2 ±     | 9 3 ±       |
| GeCl 3              | 1 1 ±      | 1.3 1 ±    | 1 0 ±      | 1 0 ±       |
| 25 eV chlorination  |            |            |            |             |
| GeCl                | 21 8 ±     | 33 7 ±     | 48 7 ±     | 60 3 ±      |
| GeCl 2              | 13 2 ±     | 15 3 ±     | 18 4 ±     | 21 4 ±      |
| GeCl 3              | 2 0.5 ±    | 1 0 ±      | 3 0 ±      | 3 2.5 ±     |
| 50 eV chlorination  |            |            |            |             |
| GeCl                | 34 3 ±     | 49 ±4      | 55 8 ±     | 69 9 ±      |
| GeCl 2              | 12 1 ±     | 21 3 ±     | 22 2 ±     | 24 2 ±      |
| GeCl 3              | 2 1.6 ±    | 3 0.5 ±    | 4 0.5 ±    | 3 1.2 ±     |

(averaged from 3 samples with standard deviation).

Figure S10 Density profile of Ge and Cl element evolution under different Ar bombardment energy on 10 eV chlorinated surface.

<!-- image -->

Figure S11 Density profile of Ge and Cl element evolution under different Ar bombardment energy on 50 eV chlorinated surface. Sample 1 is used.

<!-- image -->

## References

- 1. J. Tersoff, Physical Review B , 1988, 37 , 6991.
- 2. J. Tersoff, Physical Review B , 1989, 39 , 5566-5568.
- 3. P. C. Kelires and J. Tersoff, Physical Review Letters , 1989, 63 , 1164-1167.
- 4. D. Humbird and D. B. Graves, The Journal of Chemical Physics , 2004, 120 , 2405-2412.
- 5. W. B. Donald, A. S. Olga, A. H. Judith, J. S. Steven, N. Boris and B. S. Susan, Journal of Physics: Condensed Matter , 2002, 14 , 783.
- 6. C. F. Abrams and D. B. Graves, Journal of Applied Physics , 1999, 86 , 5938-5948.
- 7. M. V. Ramana Murty and H. A. Atwater, Physical Review B , 1995, 51 , 4889-4893.
- 8. S. P. Walch, Surface Science , 2002, 496 , 271-286.
- 9. M. T. Yin and M. L. Cohen, Physical Review B , 1982, 26 , 5668-5687.
- 10. S. Pflanz, R. Buchtler, W. Moritz and H. Over, Physical Review B , 1996, 54 , R8313-R8316.
- 11. X. Torrelles, H. A. van der Vegt, V. H. Etgens, P. Fajardo, J. Alvarez and S. Ferrer, Surface Science , 1996, 364 , 242-252.