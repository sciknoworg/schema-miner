## PCCP

<!-- image -->

## COMMUNICATION

View Article Online View Journal  | View Issue

<!-- image -->

## Computational modelling of atomic layer etching of chlorinated germanium surfaces by argon †

2

Cite this: Phys.Chem.Chem.Phys., 2019, , 5898

Received 8th January 2019, Accepted 19th February 2019

DOI: 10.1039/c9cp00125e

rsc.li/pccp

1

Shenli Zhang, ‡ a Yihan Huang, a Gulcin Tetiker, b Saravanapriyan Sriraman, b Alex Paterson b and Roland Faller * c

The atomic layer etching of chlorinated germanium surfaces under argon bombardment was simulated using molecular dynamics with a newly fitted Tersoff potential. The chlorination energy determines the threshold energy for etching and the number of etched atoms in the bombardment phase. Etch rate is determined by bombardment energy.

range of energy to remove the modified layers while avoiding physical sputtering of untreated materials.

With the decrease of electronic device size from the micro, via the nano, down to the atomic scale, the variability of the surface patterning needs to be controlled within dozens of atoms accordingly. 1,2 Plasma etching is an essential surface patterning technique. Conventionally, it is realized by ionizing non-reactive species such as Ar to transfer energy to the surface, and at the same time another reactive species such as Cl2 etches the surface either in its neutral or ionized state. 3-6 However, mixing of energetic and reactive flows leads to coupling of their transport, 1 which increases complexity and makes it hard to achieve highly defined low feature sizes. Moreover, this mixing can lead to the damage of the etching front, as high energy ions distort the surface structure and open a way for reactive species to penetrate deep into the substrate ( 4 20 nm). 1 Thus, new methods are needed to meet the requirement of precise etching control at the atomic scale, and atomic layer etching (ALE) has been proposed as one solution. 1,2,7,8 The basic idea is to separate the energetic and reactive flows to avoid the above problems. It removes thin layers of material based on a two-step self-limiting reaction: surface modification and removal. Surface modification makes a surface layer within a well-defined range more easily to be etched afterwards; for example, one can use halogen gas adsorption on the semiconductor surface to weaken the bonds; in the removal step, plasma ions are controlled within a certain

a Department of Materials Science &amp; Engineering, University of California, Davis, One Shields Avenue, Davis, 95616, CA, USA

b Lam Research Corporation, Fremont, CA 94538, USA

c

Department of Chemical Engineering, University of California,

Davis, One Shields Avenue, Davis, 95616, CA, USA. E-mail: rfaller@ucdavis.edu

† Electronic supplementary information (ESI) available. See DOI: 10.1039/c9cp00125e

‡ Current address: Institute for Molecular Engineering, University of Chicago, 5640 S Ellis Ave, Chicago, IL 60637, USA.

2

1

The first report of this technique is by Yoder et al. in 1988 on diamond. 9 Silicon and GaAs have been the most studied ALE materials since. 1 Germanium is another interesting material as a candidate to replace Si for application as transistor channels due to its superior hole mobility. 2 Several papers have been studied ALE of Ge experimentally, 8,10,11 but the microscopic understanding of the influence of the process variables on etching is still missing. Such a study is crucial to determine appropriate conditions for ALE to achieve optimal accuracy and efficiency. To bridge this gap, we report our results of an ALE simulation using molecular dynamics on a Ge surface. The surface modification step involves chlorine adsorption (chlorination) of the Ge(100) surface. Chlorine has been found to be non-reactive with Ge below 350 1 C, 2 and thus is suitable to be used for a self-limiting reaction at room temperature. Removal is then achieved by Ar + bombardment. In our simulation, neutral Ar is used instead of its charged state as the ion will become neutral when approaching the surface. 12

A new variation of the Tersoff potential based on DFT data was developed for the Ge-Cl interaction, the format used is shown in eqn (1)-(8) (see ESI, † Section S1 for discussion on the choice of potential and its training process).

XX

$$E = \frac { 1 } { 2 } \sum _ { i } \sum _ { j \neq i } V _ { i j }$$

$$V _ { i j } = f _ { \text{C} } ( r _ { i j } ) [ f _ { \text{R} } ( r _ { i j } ) + b _ { i j } f _ { \text{A} } ( r _ { i j } ) ] \quad \quad ( 2 )$$

0

1

$$\underset { \text{$\text{$\colon$} } { \max }, & \theta ^ { \gamma } \ J \smallsetminus \gamma \eta \Lambda \gamma \eta \cdot \gamma \eta \cdot \gamma \eta \Lambda \cdot \gamma \eta \Lambda \cdot \gamma \eta \Lambda \cdot \gamma \eta \Lambda \cdot \gamma \eta \Lambda \cdot \gamma \eta \Lambda \cdot \gamma \eta \Lambda \cdot \gamma \eta \Lambda \cdot \gamma \eta \Lambda \cdot \gamma \eta \Lambda \cdot \gamma \eta \Lambda \cdot \gamma \eta \Lambda \cdot \gamma \eta \Lambda \cdot \gamma \eta \Lambda \cdot \gamma \eta \Lambda \cdot \gamma \eta \Lambda \cdot \gamma \eta \Lambda \cdot \gamma \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \pi \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \gamma \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta \beta
 \\ \cdot$$

$$f _ { R } ( r ) = A \exp ( - \lambda _ { 1 } r )$$

$$f _ { \lambda } ( r ) = - B \exp ( - \lambda _ { 2 } r )$$

5

8

9

$$b _ { i j } = ( 1 + \beta ^ { n } \zeta _ { i j } ^ { n } ) ^ { - \frac { 1 } { 2 n } }$$

X

/C0

/C1

/C0

/C1

/C2

/C3

$$\zeta _ { i j } = \sum _ { k \neq i, j } f _ { C } ( r _ { i k } ) g ( \theta _ { i j k } ) \exp \left [ \lambda _ { 3 } ^ { m } ( r _ { i j } - r _ { i k } ) ^ { m } \right ] \quad \text{(7)}$$

/C18

/C19

$$g ( \theta ) = \gamma _ { i j k } \left ( 1 + \frac { c ^ { 2 } } { d ^ { 2 } } - \frac { c ^ { 2 } } { [ d ^ { 2 } + ( \cos \theta - \cos \theta _ { 0 } ) ^ { 2 } ] } \right ) \quad ( 8 )$$

where f R is a two-body repulsion term and f A the attraction term. The bond order term bij is a three-body term added to the attraction part, which includes all neighbors j and k of atom i . f C is the interaction cutoff function to smoothly transit full interaction to zero. R /C0 D and R + D is the inner and outer cutoff distance. Interaction parameters for Ge-Ge and Cl-Cl atom pairs are available from previous literature, so only Ge-Cl interaction terms were trained, as shown in Tables 1 and 2.

Fig. 1 shows the validation of this potential on a small Ge9Cl12 cluster, similar to a previous study in Si-F case. 13 The energy difference is obtained by energy minimization of the corresponding structure in both LAMMPS (Tersoff) and Gaussian (DFT). The B3LYP functional with the LanL2DZ basis set is used for DFT. Initial conditions with different Ge-Cl distance and angle were tested for each case, and consistent minimized structure was obtained. The bond length of the surface Ge-Ge in Ge9Cl12 was found to be 2.43 Å (DFT: 2.56 Å), and adsorbed Ge-Cl bond length to be 2.22 Å (DFT: 2.20 Å). The energy change calculated by the fitted Tersoff potential predicts exothermic (endothermic) nature for adsorption (desorption), and the desorption energy barrier is well above 350 1 C, although the energy difference is 1 eV lower than in DFT. ffiffi ffi p ffiffi ffi p

A Ge slab of surface dimension 64 Å /C2 64 Å ( 8 2 /C2 8 2 in lattice units, about 256 Ge atoms on the top surface) and 113 Å thick was first equilibrated at room temperature in LAMMPS 14 in the NPT ensemble (anisotropic zero pressure in surface xy plane),

Table 1 Fitted two-body parameters using annealing algorithm. R min = R /C0 D and R max = R + D are set to be the average value from Ge-Ge and Cl-Cl cutoff distances

| Fitted parameters                                               |    Ge-Cl |
|-----------------------------------------------------------------|----------|
| A (eV) B (eV) l 1 (Å /C0 1 ) l 2 (Å /C0 1 ) r min (Å) r max (Å) | 521.834  |
|                                                                 |  62.9673 |
|                                                                 |   2.3248 |
|                                                                 |   0.9857 |
|                                                                 |   2.53   |
|                                                                 |   2.83   |

Table 2 Fitted parameters in bond order bij term

Fig. 1 DFT and Tersoff calculated energy change during Clg adsorption and desorption from Ge9Cl12 cluster. Light green: Cl. Cyan: Ge. H(0,2) and H(0,3) marks the number of neighbour atoms k of Cl and Ge type for the surface Ge atom, not including its neighbour atom j . For example, H(0,2) means the surface Ge has zero Cl neighbours if not including the adsorbed Cl atom j , and has 2 other Ge atoms as its neighbours.

| j - i - k parameters   | Cl-Ge-Cl           | Cl-Ge-Ge            |   Ge-Cl- Ge |   Ge-Cl- Cl | Ge-Ge-Cl          |
|------------------------|--------------------|---------------------|-------------|-------------|-------------------|
| m                      | 3.0                | 3.0                 |           1 |           1 | 3.0               |
| g ijk                  | 1.0                | 1.0                 |           4 |           4 | 1.0               |
| l 3                    | 0.0                | 0.0                 |           6 |           6 | 0.0               |
| c                      | 1.0643 /C2 10 5    | 1.0643 /C2 10 5     |           0 |           0 | 1.0643 /C2 10 5   |
| d                      | 15.652             | 15.652              |           1 |           1 | 15.652            |
| cos y 0                | /C0 0.43884        | /C0 0.43884         |           1 |           1 | /C0 0.43884       |
| n                      | 2.23669            | 0.67543             |           1 |           1 | 0.75627           |
| b                      | 1.234 /C2 10 /C0 4 | 1.0273 /C2 10 /C0 5 |           1 |           1 | 9.02 /C2 10 /C0 7 |

<!-- image -->

with T damp = 0.1 ps and P damp = 10 ps. Dimers were found to form, consistent to both DFT and experimental results (see ESI, † Section S2 for details). 800 Cl atoms were then introduced with a flux normally incident onto the surface with a defined kinetic energy. One Cl atom at a time was introduced to the simulation box every 0.1 ps and the system was then equilibrated for 2 ns. Single Cl atoms instead of Cl2 molecules were used to shorten the equilibration time for the adsorption process, as with Cl2 it also involves the Cl-Cl bond breaking step when it is adsorbed. Charged Cl species were not considered similar to the reason that Ar was used instead of Ar . + Four different chlorination energies were tested: 5 eV, 10 eV, 25 eV and 50 eV, and simulation was repeated with different initial Cl positions to generate three chlorinated configurations for each condition. Non-adsorbed Cl atoms or Cl2 molecules (Cl2 can be formed from two Cl atoms) were removed from the simulation cell. The adsorption criteria are based on the Ge-Cl bond length 2.53 Å, which means a Cl atom is considered non-adsorbed if it is more than 2.53 Å away from a surface Ge atom. Only chemisorption is considered. Chlorinated configurations were then subjected to Ar bombardment with energies varying from 20 eV to 100 eV. The interaction between Ar and Ge/Cl is described by Ziegler-Biersack-Littmark (ZBL) potential, 15 which describes high-energy collisions between atoms. The Ge slab was coupled to a room-temperature thermostat. During a bombardment cycle, one Ar atom is introduced towards the surface and stays in the simulation box for 1.5 ps. Then the Ar atom is deleted and the system equilibrates for 0.5 ps. Etched products were then deleted before the start of a new bombardment cycle. Two hundred bombardment cycles were performed for each test condition, and each condition was repeated three times with different chlorinated configurations. The determination of etching products is again based on bond distance r ij . If rij o Rij (1) (which is the inner cutoff distance for the i , j interaction in Tersoff potential), then atoms i and j are considered to be in the same cluster.

During chlorination, Cl atoms quickly adsorb and partially penetrate beneath the surface due to the strong incident energy. Few single Ge atoms and GeCl products leave the surface. Fig. 2a shows the side view of Ge surface after chlorination,

Fig. 2 (a) Side view of Ge surface after chlorination with different energies. The layer thickness showing here is around 16 Å. Non-adsorbed Cl/ Cl2 away from surface have been deleted. (b) System energy (including both kinetic and potential energy) after equilibration (error bar smaller than the symbol) and Cl penetration depth change with chlorination energy. The dashed blue line represents the system energy in pure Ge surface structure, which is /C0 3.57 eV per atom. (c) Radial distribution function (RDF) of Ge-Ge atom pair within 10 Å from the chlorinated surface generated by different chlorination energy.

<!-- image -->

Fig. 3 Snapshots of Ge surface after 100 eV Ar bombardment (200 times). Light green: Cl. Cyan: Ge.

<!-- image -->

becomes highly distorted with increasing chlorination energy, as the radial distribution function in Fig. 2c shows the eventual formation of amorphous structures at 25 eV and 50 eV. It is also seen that the Ge-Ge bond length increases from 2.8 Å (in the perfect crystal) to 3.2 Å due to Cl penetration, as the first peak in RDF shifted towards longer bond distance with increasing energy.

where increasing Cl adsorption and penetration with Cl incident energy can be seen. The adsorbed/absorbed Cl number increases from 320 /C6 5 atoms (5 eV) to 616 /C6 4 atoms (50 eV). Defining Cl penetration depth as the full width at half maximum of Cl density peak, Fig. 2b demonstrates that the penetration depth increases with Cl incident energy. Notice the coverage on surface already reaches 100% at 5 eV (coverage is defined as the Cl-bonded Ge numbers to the number of top layer Ge). From Ge-Cl coordination number (CN) characterization (Table 3), most Ge are bonded to one Cl, however increasing chlorination energy will increase the bonded Cl number (from the increase of the average CN). Also, more Ge will bond with Cl (from the increase of the coverage). The high population of Ge-1Cl bonding is because the energy decrease from Ge-Ge to Ge-1Cl is much larger than that from Ge-1Cl to Gen Cl. It is worth noting that the result could be sensitive to force field training, if the bond energy change from GeCl to GeCl2 is larger than Ge-Ge to Ge-1Cl, then Ge-2Cl can be a more favorable configuration. The decrease of energy with Cl penetration can be also seen in the system energy (Fig. 2b). The system energy is defined as the total energy divided by the number of atoms in the system. It decreases with chlorination energy, or Cl numbers, as bonding between Ge and Cl is stronger than that among Ge. The Ge surface structure

The influence of chlorination energy extends to the Ar bombardment stage. During the bombardment, energy from Ar was transferred to the surface and the weakened Ge-Ge bonds break, allowing Ge-Cl clusters or single atoms to leave as etching products. Few residual Cl atoms remain on the surface (Fig. 3, also from the difference between the etched Cl number and total adsorbed Cl number during chlorination).

To compare the surface morphology with different chlorination energies before and after the bombardment, density profiles (Fig. 4a and b) are used to show the etching front evolution. The Z axis is the surface normal pointing from the bulk to the top surface. The Ge density profile starts with a plateau in the bulk phase and then decreases to zero, where the transition region represents the surface layers. Correspondingly, Cl shows a density peak in this transition region due to surface adsorption and penetration. For initial configurations, the 50 eV chlorinated case shows a wider Cl peak distribution than 5 eV and Cl penetrates deeper as the peak position moves towards bulk, consistent with Fig. 2b. After bombardment with 100 eV Ar, slightly more Ge layers have been etched away with the highly chlorinated configuration as the profile recedes more into the bulk region, while a similar amount of Cl residues stays on the surface. This could be understood by the fact that more Cl was adsorbed on the surface originally.

Next, to characterize the influence of chlorination energy on etching products, the product fraction, defined as the ratio of the number of a product to the total number of all the products (including physical sputtering products), is plotted for each Ar

Table 3 Percentage of different Ge-Cl coordination numbers (CN) at various chlorination energies, averaged from the three samples with standard deviation. Average CN and coverage are also calculated. Coverage is the ratio of Cl-bonded Ge numbers to the top layer Ge number (256) at the surface

|   Cl energy (eV) | Ge-Cl         | Ge-2Cl         | Ge-3Cl         | Ge-4Cl          | Average CN    | Coverage      |
|------------------|---------------|----------------|----------------|-----------------|---------------|---------------|
|                5 | 0.60 /C6 0.01 | 0.35 /C6 0.005 | 0.05 /C6 0.008 | 0 /C6 0         | 1.45 /C6 0.02 | 1.38 /C6 0.03 |
|               10 | 0.55 /C6 0.03 | 0.35 /C6 0.03  | 0.10 /C6 0.009 | 0.02 /C6 0.02   | 1.61 /C6 0.08 | 1.64 /C6 0.03 |
|               25 | 0.45 /C6 0.01 | 0.37 /C6 0     | 0.18 /C6 0.02  | 0.002 /C6 0.001 | 1.74 /C6 0.03 | 2.43 /C6 0.06 |
|               50 | 0.41 /C6 0.07 | 0.38 /C6 0.02  | 0.21 /C6 0.05  | 0.006 /C6 0.006 | 1.81 /C6 0.14 | 3.56 /C6 0.05 |

|

## Communication

Fig. 4 Number density change of 5 eV chlorinated and 50 eV chlorinated surface (a) before and (b) after 100 eV Ar bombardment. Etching products fraction (GeCl, GeCl2 and GeCl3) and element etched number change in each Ar bombardment cycle for (c) 5 eV and (d) 50 eV chlorinated surface. The insets number on etched number graph shows the total etched Ge and Cl number. Sample 1 is used as an example here. Characterizations for 10 eV and 25 eV chlorinated surface are shown in ESI, † Fig. S7.

<!-- image -->

bombardment cycle, as shown in Fig. 4c and d. Ge Cl x y (with x 4 y ) clusters and single Ge atoms also appear during bombardment cycles (not shown in the above figure, fraction higher than GeCl). They are likely due to physical sputtering of several atoms together. Cl2 was barely observed as an etching product in our case, almost all Cl were attached to Ge. GeCl was found to be the main chemical etching product, fluctuating around 55-85% depending on energy conditions (see ESI, † Fig. S8 and Table S6), if only GeCl n clusters are considered. GeCl2 is of between 15-35%, followed by a very small fraction of GeCl3 (below 10%). The latter may be due to a slight inaccuracy in the force field (see ESI † ). No GeCl4 is found under any condition. This distribution follows the Ge-Cl CN trend in the chlorination step, as Ge-1Cl has the highest fraction, followed by Ge-2Cl and Ge-3Cl. It's likely the chlorination morphology determines the etching product. Besides, for surface with low chlorination energy such as the 5 eV case (Fig. 4c), both Ge and Cl etched number decrease greatly after about hundred bombardment cycle, as the surface becomes deficient in Cl. This indicates two things: first, chlorination is necessary to weaken Ge-Ge bond strength and makes etching possible; second, amorphization of top Ge surface layers also weakens Ge-Ge bond strength such that physical sputtering is only possible within modified layers. With higher chlorination energy, the self-terminated etching process could require more Ar bombardment cycles.

By varying the Ar bombardment energy from 25 eV to 100 eV, we see that the chlorination energy influences the threshold

## PCCP

Fig. 5 (a) Density profile of Ge and Cl element change before and after 200 times Ar bombardment with different bombardment energy on 25 eV chlorinated surface. (b) Total etched number change (blue: Ge, red: Cl) with Ar bombardment energy for each chlorination condition, averaged from three samples with error bars calculated.

<!-- image -->

energy for etching. The density profile (Fig. 5a) indicates whether etching occurs. Fig. 5a shows the evolution of element density profile of 25 eV chlorinated surface under different bombardment condition (see ESI, † Fig. S9-S11 for other chlorinated conditions). At 25 eV Ar energy, Cl density peak already starts to decrease, and Ge surface recedes towards the bulk phase. With 50 eV Ar, the etching effect is more obvious, and most Cl has been etched away when Ar energy reaches 75 eV. Thus, the threshold energy should be below 25 eV Ar, matching well with the experimental operation window. 2 Similarly, the 5 eV chlorinated surface has a threshold energy between 50-55 eV. For the 10 eV chlorinated case, this threshold energy slightly decreases to 25-50 eV, and for 25 eV and 50 eV chlorinated surface, etching starts below 25 eV. Thus, a higher chlorination energy generally decreases the threshold energy for bombardment, possibly because the highly disordered surface structure makes it more vulnerable for detachment.

Meanwhile, we notice the complete etching (defined as when the Cl peak density approaches zero and no longer evolves) occurs between 60-75 eV bombardment energy for 5 eV chlorinated surface, while it increases to the 75-100 eV range for 10 and 25 eV chlorinated surfaces, and higher than 100 eV for the 50 eV case, possibly because the Cl atoms penetrate deeper into the surface for high chlorination energy. Besides, both chlorination energy and bombardment energy have an impact on the etching efficiency. Fig. 5b shows the change of the total etched number of Ge and Cl atoms with Ar energy for each chlorinated condition. Several things can be noticed here. First, both Ge and Cl etching increases with Ar energy. Since the etching time and bombardment flux is fixed,

this indicates a higher etching rate and efficiency at higher bombardment energy. Second, the etching numbers change of Ge and Cl are coupled. Both etched Cl and Ge number in 5 eV chlorinated case tend to reach a plateau with increasing Ar energy, due to the limited Cl number and modification layer in the system (self-limited etching process), which further proves the bond weakening by chlorination. Higher chlorination energy such as 50 eV postpones the appearance of the plateau, as more Cl are originally in the system. If the Ar energy is further increased beyond the plateau, the etched Ge number should increase quickly again due to pure physical sputtering. 1 This naturally leads to the third conclusion that this limit of chemically etched number depends on chlorination energy, or the number of Cl available in the system.

In conclusion, we used molecular dynamics with a newly improved and validated Ge-Cl Tersoff potential to understand the influence of operation energy on each stage in ALE of Ge and their synergy effect. The chlorination energy is the key factor in surface modification step. Increasing chlorination energy increases Cl adsorption and its penetration depth. It also increases Ge-Cl coordination number from Ge-1Cl to Ge-2Cl and turns the surface into amorphous layer after 25 eV. The configuration and composition of modified surface then dominates the etching results in Ar bombardment step. First, GeCl is the main chemical etching product in our case, as Ge-1Cl is also the main CN during chlorination. Second, the chlorination quantity determines the limit of chemically etched number in bombardment stage. This reflects the self-limiting characteristic in ALE, as the etching termination point is based on the number of Ge-Ge bonds that have been weakened. The more Cl atoms are bonded in the system, the more etched atoms leave. Third, the extent of chlorination determines the threshold for etching. Highly chlorinated surfaces lead to a lower threshold energy, and at the same time a higher energy or more Ar bombardment cycles for complete etching. The lowest threshold energy is below 25 eV for the 25 and 50 eV chlorinated cases. In terms of the influence of bombardment energy, the effective self-terminated etching would require a specific energy range, higher than the threshold energy but lower than spontaneous physical sputtering. And within this range, the increase of bombardment energy leads to an increase of etching rate.

Our work demonstrates the microscopic link between the surface modification and bombardment step in a Ge-Cl reaction system. Future work should focus on the improvement of the

|

Ge-Cl force field, a full characterization of the operation energy window, and experimental validation.

## Conflicts of interest

There are no conflicts to declare.

## Acknowledgements

We thank the Silicon Valley Community Foundation for a gift which partially supported this research.

## Notes and references

- 1 K. J. Kanarik, T. Lill, E. A. Hudson, S. Sriraman, S. Tan, J. Marks, V. Vahedi and R. A. Gottscho, J. Vac. Sci. Technol., A , 2015, 33 , 020802.
- 2 K. J. Kanarik, S. Tan, W. Yang, T. Kim, T. Lill, A. Kabansky, E. A. Hudson, T. Ohba, K. Nojiri, J. Yu, R. Wise, I. L. Berry, Y. Pan, J. Marks and R. A. Gottscho, J. Vac. Sci. Technol., A , 2017, 35 , 05C302.
- 3 J. W. Coburn and H. F. Winters, J. Appl. Phys. , 1979, 50 , 3189-3196.
- 4 R. A. Gottscho, C. W. Jurgensen and D. J. Vitkavage, J. Vac. Sci. Technol., B: Microelectron. Nanometer Struct.-Process., Meas., Phenom. , 1992, 10 , 2133-2147.
- 5 K. Nojiri, Dry etching technology for semiconductors , Springer, 2015.
- 6 V. M. Donnelly and A. Kornblit, J. Vac. Sci. Technol., A , 2013, 31 , 050825.
- 7 G. S. Oehrlein, D. Metzler and C. Li, ECS J. Solid State Sci. Technol. , 2015, 4 , N5041-N5053.
- 8 K. J. Kanarik, S. Tan and R. A. Gottscho, J. Phys. Chem. Lett. , 2018, 9 , 4814-4821.
- 9 M. N. Yoder, Atomic layer etching, US Pat. , 4756794, 1988.
- 10 T. Sugiyama, T. Matsuura and J. Murota, Appl. Surf. Sci. , 1997, 112 , 187-190.
- 11 K. Ikeda, S. Imai and M. Matsumura, Appl. Surf. Sci. , 1997, 112 , 87-91.
- 12 H. D. Hagstrum, Phys. Rev. , 1954, 96 , 325-335.
- 13 D. Humbird and D. B. Graves, J. Chem. Phys. , 2004, 120 , 2405-2412.
- 14 S. Plimpton, J. Comput. Phys. , 1995, 117 , 1-19.
- 15 J. F. Ziegler, J. P. Biersack and U. Littmark, The Stopping and Range of Ions in Matter, Pergamon, 1985, vol. 1.