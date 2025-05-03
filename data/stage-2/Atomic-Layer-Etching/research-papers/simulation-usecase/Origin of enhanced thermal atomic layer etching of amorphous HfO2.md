<!-- image -->

RESEARCH ARTICLE |  FEBRUARY 28 2022

## Origin of enhanced thermal atomic layer etching of amorphous HfO 2

Special Collection: Atomic Layer Etching (ALE)

Rita Mullins ; José Julio Gutiérrez Moreno ; Michael Nolan

<!-- image -->

<!-- image -->

<!-- image -->

Check for updates

J. Vac. Sci. Technol. A

40, 022604 (2022)

https://doi.org/10.1116/6.0001614

 

<!-- image -->

<!-- image -->

## Articles You May Be Interested In

Surface reaction modelling of thermal atomic layer etching on blanket hafnium oxide and its application on high aspect ratio structures

J. Vac. Sci. Technol. A (December 2022)

Control of etch profiles in high aspect ratio holes via precise reactant dosing in thermal atomic layer etching

J. Vac. Sci. Technol. A (February 2022)

Effect of crystallinity on thermal atomic layer etching of hafnium oxide, zirconium oxide, and hafnium zirconium oxide

J. Vac. Sci. Technol. A (February 2020)

<!-- image -->

<!-- image -->

<!-- image -->

## Origin of enhanced thermal atomic layer etching of amorphous HfO2

Cite as: J. Vac. Sci. Technol. A 40 , 022604 (2022); doi: 10.1116/6.0001614 Submitted: 10 November 2021 · Accepted: 4 February 2022 · Published Online: 28 February 2022

<!-- image -->

<!-- image -->

Rita Mullins, 1

José Julio Gutiérrez Moreno, 2

and Michael Nolan 1,a)

<!-- image -->

<!-- image -->

## AFFILIATIONS

- 1 Tyndall National Institute, University College Cork, Cork T12 R5CP, Ireland

2 Barcelona Supercomputing Center (BSC), C/Jordi Girona 31, 08034 Barcelona, Spain

Note:

This paper is part of the 2022 Special Topic Collection on Atomic Layer Etching (ALE).

a) Electronic mail:

michael.nolan@tyndall.ie

## ABSTRACT

HfO2 is a highk material that is used in semiconductor devices. Atomic-level control of material processing is required for the fabrication of thin films of highk materials at nanoscale device sizes. Thermal atomic layer etching (ALE) of metal oxides, in which up to one monolayer of material can be removed, can be achieved by sequential self-limiting fluorination and ligand-exchange reactions at elevated temperatures. First-principles-based atomic-level simulations using density functional theory can give deep insights into the precursor chemistry and the reactions that drive the etching of metal oxides. A previous study examined the hydrogen fluoride (HF) pulse in the first step in the thermal ALE process of crystalline HfO2 and ZrO2. This study examines the HF pulse on amorphous HfO2 using first-principles simulations. The Natarajan -Elliott analysis, a thermodynamic methodology, is used to compare reaction models representing the selflimiting and spontaneous etch processes taking place during an ALE pulse. For the HF pulse on amorphous HfO2, we found that thermodynamic barriers impeding spontaneous etching are present at ALE relevant temperatures. HF adsorption calculations on the amorphous oxide surface are studied to understand the mechanistic details of the HF pulse. An HF molecule adsorbs dissociatively by forming Hf -F and O -H bonds. HF coverages ranging from 1.1 ± 0.3 to 18.0 ± 0.3 HF/nm 2 are investigated, and a mixture of molecularly and dissociatively adsorbed HF molecules is present at higher coverages. A theoretical etch rate of -0.82 ± 0.02 Å/cycle for amorphous HfO2 was calculated using a maximum coverage of 9.0 ± 0.3 Hf -F/nm 2 . This theoretical etch rate is greater than the theoretical etch rate for crystalline HfO 2 that we previously calculated at -0.61 ± 0.02 Å/cycle. Undercoordinated atoms and void regions in amorphous HfO2 allow for more binding sites during fluorination, whereas crystalline HfO2 has a limited number of adsorption sites.

© 2022 Author(s). All article content, except where otherwise noted, is licensed under a Creative Commons Attribution (CC BY) license (http://creativecommons.org/licenses/by/4.0/). https://doi.org/10.1116/6.0001614

## I. INTRODUCTION

Atomic layer processing has become increasingly important due to the continued downscaling of semiconductor devices, which necessitates the deposition of thinner materials films in complex structures. The control of film etch offered by thermal atomic layer etching (ALE) is necessary for state-of-the-art semiconductor devices. 1 Thermal ALE is a technique that removes thin layers of material using sequential, self-limiting surface reactions and can be viewed as the reverse of atomic layer deposition (ALD). 2 Thermal ALE is based on surface modification and volatilization reactions, where the modification step alters the surface layer into a nonvolatile later followed by the release of volatile etch products from the surface layer in the second reaction. 2 For metal oxides, thermal

ALE has been performed using fluorination and ligand exchange reactions as shown in Fig. 1 (Ref. 2). Fluorination converts the surface of the metal oxide to a surface fluoride layer, and ligand exchange can volatilize the metal fluoride layer to produce stable etch products. Thermal ALE relies on temperature and thermochemically favorable reactions to remove surface species 2 and etches at the same rate in all directions. 3 Many technologically important metal oxides have been etched using thermal ALE including HfO2, 4 ZrO2, 4 SiO2, 5 Al2O3, 4,6,7 TiO2, 8,9 VO2, 10 WO3, 11 ZnO, 12 Ga2O3, 13 as well as metal nitrides such as AlN, 14 TiN, 15,16 and GaN. 17,18 Thermal ALE of amorphous Al2O3 has also been reported using NbF5 to replace hydrogen fluoride (HF) as the fluorination agent and CCl4 for the halide-exchange reaction. 19

<!-- image -->

CrossMark

25 March 2025 10:19:29

<!-- image -->

<!-- image -->

Thermal ALE can also be performed by other processes such as conversion, 20 oxidation, 21 oxidation/chlorination, 22 and chlorinefluorine ligand exchange. 23 Plasma ALE consists of two halfreactions of surface adsorption and surface removal where Ar plasma bombardment is used for etching in the surface removal step. 24 Plasma ALE of Si3N4, 25 SiO2, 26 and SiN 27 can be achieved using a fluorocarbon polymer. Advantages of ALE include high uniformity, the ability to etch high-aspect-ratio features, selectivity, and smoothing. 28

Semiconductor devices have features at the nanometer scale due to Moore s law scaling. SiO2 ' gate dielectrics are so thin that electron tunneling through the dielectric layer, which leads to high leakage currents, is impossible to avoid. 29,30 HfO2 is a highk material with a dielectric constant of 22; it allows a high drive current to be maintained, while minimizing leakage current meaning that a low equivalent oxide thickness can be used. 31 HfO2 is thermodynamically stable when interfaced with silicon in semiconductor devices. 32,33 Amorphous HfO2 has a dielectric constant of ∼ 16 to 19. 34

In terms of mechanisms, thermal ALE processes generally use HF for the fluorination step 35 for metal oxides as it is a useful nucleophilic fluorination reactant 10 in which the fluoride anion serves as the active reaction species. For the ligand-exchange step, examples of metal precursors used are Sn(acac)2, 36 Al(CH3)3, 37 Al(CH3)2Cl, 36 SiCl4, 36 BCl3, 23 TiCl4, 38 and WF6. 39 The surface fluorination step in thermal ALE using HF is the focus of our work and the focus of this paper.

Experimental studies have shown that crystalline films have lower etch rates than amorphous films for thermal ALE of metal oxides such as HfO2, ZrO2, and HfZrO4 at 250 °C and Al2O3 at 300 °C. 40,41 Using HF as the fluorinating agent and TiCl4 as the ligand-exchange agent, the etch rate for amorphous HfO2 was 18 times higher than the etch rate for crystalline HfO2. 40 Using the same reagents, the etch rate for amorphous ZrO2 was 2.3 times higher than the etch rate for crystalline ZrO2. 40 Similarly using HF and dimethyl aluminum chloride [DMAC, Al(CH3)2Cl], the etch rate on amorphous HfO2 was 8.5 times higher than the etch rate on crystalline HfO2, whereas for ZrO2, the amorphous etch rate was 1.4 times higher than the crystalline etch rate. 40 This shows that the etch rates for HfO2 are strongly dependent on whether a crystalline or amorphous film is etched. 40 Amorphous materials have a lower density than their crystalline form, which may facilitate the fluorination that leads to an expansion of the metal oxide. 40 In wet HF etching, crystalline HfO2 is also etched more slowly than amorphous HfO2. 42 The differences in etch rates show potential for selective ALE, where two different materials have different etch rates under the same conditions. 40

Given that it is difficult to investigate thermal ALE reactions directly using experimental techniques, first-principles-based atomic-level simulations using density functional theory (DFT) can give deep insights into the precursor chemistry and the reactions that drive the etch of metal oxides. Our previous study examined the difference in thermal ALE for the fluorination step for crystalline HfO2 and ZrO2 using HF. 43 In the present paper, the HF pulse in the first step in thermal ALE of amorphous HfO2 is examined in detail with first-principles DFT calculations of the fluorination mechanism. HF molecules adsorb at the surfaces of metal oxides by forming metal -F bonds and may remain intact or dissociate. 44 If HF dissociates, it may form Hf -F and O -H bonds, and release water, similar to previous studies on etch modeling for crystalline HfO2, ZrO2, and Al2O3. 43,44 The amount etched (etch rate) is determined by how much of the oxide surface is fluorinated; a larger fluoride film thickness after fluorination can lead to more fluoride removed during the ligand-exchange step and high etch rates. 40

The Natarajan -Elliott analysis 43 (N E) is used to predict the -conditions at which a self-limiting (SL) or spontaneous etching (SE) reaction becomes thermodynamically favorable and can, therefore, be used to direct experimental studies of thermal ALE. Self-limiting reactions are a necessary part of thermal ALE and allow the degree of etching to be well controlled and defined. In this study, it is found that SL reactions are more favorable than the competing SE reaction for the HF pulse on amorphous HfO2 at 0 and 520 K; the latter corresponds to the temperature used in experimental studies of thermal ALE for HfO2 using HF as the fluorination agent. 43 The temperatures above which spontaneous etching is favored range from 718 to 1302 K at typical thermal ALE reactant pressures, depending on the degree of fluorination; these are significantly higher than on crystalline HfO2. Introducing HF molecules to the amorphous HfO2 surface results in dissociative HF adsorption. The maximum coverage of Hf F bonds -on the surface is used to calculate the theoretical etch rate. The spontaneous formation of water and hydrogen peroxide is also discussed. Combining the thermodynamic and mechanistic investigation using first-principles simulation demonstrates the origin of the large difference in etch rates for crystalline and amorphous HfO2 allowing the design of novel ALE processes for other technologically relevant materials.

## II. COMPUTATIONAL METHODS

All calculations reported in this paper were carried out using spin-polarized density functional theory implemented in VASP 5.4 (Ref. 45). The Perdew -Burke -Ernzerhof (PBE) generalized gradient approximation (GGA) to an exchange-correlation (XC) functional is used. 46 The convergence criteria for total energies and the forces

25 March 2025 10:19:29

FIG. 2. Distribution of coordination numbers for the bulk aHfO 2 model used in this study that was prepared using classical molecular dynamics.

<!-- image -->

<!-- image -->

for ionic relaxation are 1 × 10 -4 and 2 × 10 -2 eV/Å, respectively. The Methfessel -Paxton first order smearing method is used with a broadening of 0.1 eV for the electronic relaxations. The corevalance electron interactions are represented by projectoraugmented wave (PAW) potentials, 47 and the following valence electron configurations are used: Hf: 6s 2 5d , O: 2s 2 2 2p , F: 2s 4 2 2p , 5 and H: 1s . 1 The valence electrons are described with a periodic plane-wave basis set using a kinetic energy cutoff of 400 eV.

The Gibbs free energy, Δ G , at a temperature, T , is computed as follows:

$$\Delta G = \, \Delta H - T \Delta S + R T \ln ( Q ), \quad \quad ( 1 ) \quad \text{con} \,.$$

$$\Delta H = \, \Delta E + \, \Delta Z P E + \, \Delta W ( T ), \quad \quad ( 2 ) \quad \text{$\quad} \text{$\quad}$$

$$\Delta E = \, \sum _ { p } \mu E _ { p } - \sum _ { r } \mu E _ { r }, \quad \quad ( 3 ) \quad \text{ion} _ { \text{kin} }.$$

$$Q = \prod p _ { \text{products} } ^ { \mu } \Big / \prod p _ { \text{reactants} } ^ { \mu }. \quad \quad ( 4 ) \quad \text{is u} \\ \text{miz}$$

The Δ H and Δ S terms in Eq. (1) are the changes in reaction enthalpy and reaction entropy respectively, with the term RT ln(Q) included since the partial pressures of the reactants and products are variable in the reaction chamber. In Eq. (2), Δ H contains the electronic reaction energy at 0 K Δ E , zero-point energy change Δ ZPE , and a temperature-dependent enthalpy change Δ W T ( ). The stoichiometric coefficient of the corresponding species is μ and the reactant and product species are r and p , respectively, in Eq. (3). A reactant pressure of 0.2 Torr and a product pressure of 0.01 Torr are used for the free energy calculations. Of course, it is not possible to control the product pressure in an etch reactor. 16 It is, however, typically much lower than the reactant pressure, so a value of 0.01 Torr for our calculations is consistent with this and previous work of DFT investigation in thermal etching of TiN, 16 W, 22 TiO2, 9 and Co. 48

## A. Bulk and slab models

Bulk amorphous HfO2 (henceforth aHfO2) was prepared using classical molecular dynamics (MD) simulations with the LAMMPS package. 49 Atomic pair interactions were adopted from the Morse type potential developed by Broglia et al. 50 This potential is accurate for the simulation of glasses at high temperatures and pressures, and has been previously used for the study of aHfO2. 50 The Nosé -Hoover thermostat in its isothermal-isobaric form (NPT) was used to set the constant pressure at 1 atm and the temperatures during the simulation. The integration time step was set to 0.1 fs. The amorphous structure was produced using the melt-quenching method. Initially, a total of 216 atoms with a stoichiometric HfO2 composition (72 Hf and 144 O atoms) are randomly placed in a periodic cubic box. After an initial equilibration, the system is warmed up to 4000 K at a rate of 10 K/ps. The temperature was set well above the experimental melting point and equilibrated for 2 ns to assure the initially random distribution of the atomic species in our model. The melted structure is then quenched to 300 K in consecutive steps of 10 K/ps (i.e., every 10 4 time steps) and finally equilibrated for 1 ns at room conditions. The quenching rate was chosen to be quick enough to produce an amorphous structure at equilibrium; see supplementary material, 65 Sec. I for a pair distribution function of aHfO2. This procedure leads to an equilibrated cubic box with side dimensions of 13.72 Å. The density of the resulting simulation box is 9.62 g/cm , which is 3 in good agreement with other aHfO2 models generated by MD. 51 53 -The surface model is cleaved from the bulk at a plane parallel to one of the box sides, where a large vacuum layer is introduced. To moderate the likely abundance of uncoordinated species at the surface formed from a random cleavage of the amorphous bulk, a rapid melt-quenching was run for the slab model keeping constant volume and temperature (NVT ensemble). The surface model was warmed to 4000 K at 20 K/ps rate, relaxed for 50 ps, quenched to 300 K at 10 K/ps rate, and finally equilibrated for 1 ns. The slab model is then relaxed using DFT.

The aHfO2 bulk was relaxed by simultaneous relaxation of the ionic positions, cell volume, and cell with a higher plane wave kinetic energy cutoff of 550 eV to ensure an accurate description of the bulk. A Monkhorst -Pack k -point sampling mesh of (1 × 1 × 1) is used. The bulk aHfO2 has 72 Hf and 144 O atoms and the optimized lattice constants are a = 13.729 Å, b = 13.871 Å, and c = 13.796 Å, and angles alpha = 90.74°, beta = 89.14°, and gamma = 89.81°. The density of our bulk aHfO2 model is 9.62 g/ cm 3 which is smaller than the crystalline HfO2 (monoclinic and cHfO2) density from our previous study which was 10.01 g/cm . 3 43 The surface slab of aHfO2 with 16 Å of vacuum separating the slabs is used for the surface models with a stoichiometry of Hf72O144 per supercell. A k-point sampling mesh of (2 × 2 × 1) is used for geometry optimization.

For the N -E analysis, the self-limiting reaction product state models are obtained by replacing every oxygen removed from the surface of the slab model with two fluorine atoms, this ratio is shown as 1O/2F. 43 Three self-limiting product state models: 8O/ 16F, 10O/20F, and 16O/32F are examined. Enthalpy H and entropy S are computed using the Phonopy 54 code for only the top layers of fluorinated Hf atoms for the surface calculations. For the gas-phase

<!-- image -->

molecules, H and S were calculated from the free program in the Turbomole 55,56 suite at 1 atm pressure using the PBE exchangecorrelation functional 46 and a polarized triple basis set (def-TZVPP) 57,58 and default medium grid. The reactant molecules and gas-phase by-products calculations are performed in VASP with a large periodic box of dimensions 15.0 × 16.0 × 15.5 Å 3 and 400 eV plane-wave energy cutoff. Atomic structures in the VASP format of all systems studied in this work are available at the following link: https://github.com/RitaMull/Thermal-ALE-aHfO2using-HF.

Experimental studies have shown that the chemical composition of aHfO2 is essentially stoichiometric. 59 Theoretical studies of aHfO2 reported that the coordination numbers for the Hf atoms were five, six, seven, and eight with a preference for six and seven. For oxygen two, three, and four coordination are found, with a preference for three and four coordination. 51 The distribution of the coordination numbers for the Hf and O atoms of the bulk aHfO2 model used in this study is shown in Fig. 2. To determine the coordination number, a cutoff radius of 2.50 Å derived from the behavior of Hf O -bonds are used. 60 Three-coordinated O atoms and six-coordinated/seven-coordinated Hf atoms dominate the bulk aHfO2 model, which agrees with previous classical 61 and ab initio 62,63 molecular dynamic studies. Compared to the monoclinic phase, the coordination number for the Hf atoms can be seven or eightfold, and the O atoms can be either three or fourfold coordinated. 59

## III. RESULTS AND DISCUSSION

## A. Self-limiting vs spontaneous etch

To predict if the HF pulse will promote spontaneous etch (SE) or a self-limiting (SL) reaction on aHfO2, the energetics and thermodynamics under given conditions are compared. In a spontaneous etch process, the bulk material is fully converted to gaseous products HfF4 or HfOF2 and water. In the self-limiting etch process, the surface of aHfO2 is converted to HfF4 or HfOF2 (while the bulk is preserved), releasing water; this replaces surface oxygen with fluorine from HF. Table I shows two possible SE and two possible SL reactions for the HF pulse on aHfO2 as well as the reaction (free) energies at 0 K and at typical thermal ALE temperature of 520 K and the computed minimum barrier to spontaneous etching. A negative minimum barrier would indicate that spontaneous etching is thermodynamically favorable and is prevented only by potential kinetic barriers. The energies in Table I are computed as follows:

$$\tilde { \text{set} } \quad E ( \text{E} 1 ) = E ( \text{HfF} _ { 4 ( g ) } ) + 2 E ( \text{H} _ { 2 } O _ { ( g ) } ) - [ E ( \text{HfO} _ { 2 ( b ) } ) + 4 E ( \text{HF} _ { ( g ) } ) ],$$

$$\stackrel {.. a. } { 3 } \text{ and } \quad E (SL1) = E ( H f F _ { 4 (surface)} + 2 E ( H _ { 2 } O _ { ( g ) } ) = [ E ( H f O _ { 2 (surface)} ) + 4 E ( H F _ { ( g ) } ) ],$$

$$the \, \quad \, E ( SE 2 ) = E ( H f O F _ { 2 ( g ) } ) + E ( H _ { 2 } O _ { ( g ) } ) - [ E ( H f O _ { 2 ( b ) } ) + 2 E ( H F _ { ( g ) } ) ],$$

$$\ m o s i { - \quad E ( S L 2 ) = E ( H f O F _ { 2 ( s u r a c e ) } ) + E ( H _ { 2 } O _ { ( g ) } ) - [ E ( H f O _ { 2 ( s u r a c e ) } ) + 2 E ( H F _ { ( g ) } ) ] }.$$

The models are bulk aHfO2 and aHfO2 surface, while the reactant is gaseous HF and water is formed from the oxygen removed from aHfO2. The energies are computed at 0 K within the DFT setup described in Sec. II. The free energies are computed from

$$\Delta G = \, \Delta H - T \Delta S,$$

where the 0 K DFT energy is corrected by the change entropy at the chosen temperature; computation of the entropy contribution is described in Sec. II.

The SE1 and SE2 reactions convert the bulk aHfO2 into a volatile metal fluoride or metal oxyfluoride, respectively, and water. In reaction SE1, four HF molecules are required to etch one unit of bulk HfO2 forming HfF4 and water. In reaction SE2, two HF molecules are needed to etch one unit of HfO2 to form HfOF2 and H2O. In both SE reactions, the surface of the material before and after each precursor pulse is identical and, therefore, their contributions are not required in these models.

The SL1 and SL2 reactions involve the conversion of the outermost surface layer of aHfO2 into the nonvolatile metal fluoride and nonvolatile metal oxyfluoride respectively with the release of water molecules. The SL product state of a HfO2 has a composition of 8O/16F where 8 oxygen atoms originally present on the surface are removed and replaced by 16 fluorine. For both SL reactions, the surfaces are not identical before and after the pulse and their contributions have to be included. Negative free energy means that the corresponding reaction is exergonic (favorable), while positive free energy means that the corresponding reaction is endergonic (unfavorable). At 0 and 520 K, the SE1 reaction is favorable whereas the SE2 reaction is unfavorable. Table I shows that the barrier to spontaneous etch is positive for all the SE and SL reactions at 0 K, indicating that the self-limiting reaction is most favorable energetically and at 520 K this barrier to spontaneous etching, although reduced, remains positive. Therefore, up to 520 K, the reactions with HF in

TABLE I. Reaction energies at 0 K ( Δ E ) and free energies at 520 K ( Δ G ) from the model SE and SL reactions after the HF pulse on aHfO . For this table, the product state is 2 8O/16F, and the numbers in parenthesis are the minimum barriers to continuous etching.

|     | Reactions                                                 | Δ E (eV/M)    | Δ G (eV/M)    |
|-----|-----------------------------------------------------------|---------------|---------------|
| SE1 | 1HfO 2(b) + 4HF (g) → 1HfF 4(g) + 2H 2 O (g)              | - 1.44        | - 1.15        |
| SL1 | 1HfO 2(surface) + 4HF (g) → 1HfF 4(surface) + 2H 2 O (g)  | - 4.07 (2.63) | - 1.87 (0.72) |
| SE2 | 1HfO 2(b) + 2HF (g) → 1HfOF 2(g) + 1H 2 O (g)             | 3.35          | 2.58          |
| SL2 | 1HfO 2(surface) + 2HF (g) → 1HfOF 2(surface) + 1H 2 O (g) | - 2.04 (5.39) | - 0.94 (3.52) |

FIG. 3. Free energy profile for the SE1 (blue) and SL1 (orange) reactions of aHfO2 from 0 to 1000 K at the pressures given in the text. T1 is where the SL and SE reactions cross over for the 8O/16F model, and T2 is where spontaneous etching is preferred.

<!-- image -->

<!-- image -->

the first step will be preferentially self-limiting on aHfO , similar to 2 crystalline HfO2.

Only the SE1 reaction is considered for further analysis, as the SE2 reaction is unfavorable at 0 and 520 K, and the SL2 reaction is less favorable than the SL1 reaction at 0 and 520 K. In addition, the high barrier to etch for the SL2 and SE2 reactions suggests that the spontaneous formation of the metal oxyfluoride is not likely at ALE-relevant temperatures around 520 K. The reaction free energy profiles (FEPs) of the SE1 and SL1 reactions are shown in Fig. 3, and at a given temperature and reactant pressure, these show whether spontaneous etching or self-limited conversion of aHfO2 into a nonvolatile metal fluoride layer are preferred. A reactant pressure of 0.2 Torr and a product pressure of 0.01 Torr are used and the temperature range is 0 -1000 K.

In Fig. 3, the self-limiting reaction is preferred up to 717 K, at 718 K, the minimum barrier to etch is zero with SE1 and SL1 being isoenergetic, and at temperatures higher than 718 K, spontaneous etching becomes more favorable. At 973 K, the self-limiting reaction becomes unfavorable, while spontaneous etching remains favorable. Surface hafnium atoms are easier to remove in the ligand-exchange step when more oxygen atoms are removed due to the reduced hafnium -oxygen bond interaction. The surface of

TABLE II. Reaction (free) energies and minimum barriers at 0 and 520 K for the model self-limiting for 8O/16F , 10O/20F , and 16O/32F SL product states.

|     | SL product state   | Δ E (0 K) (eV/M)   | Δ G (520 K) (eV/M)   |
|-----|--------------------|--------------------|----------------------|
| SE1 | HfF 4              | - 1.44             | - 1.15               |
| SL1 | 8O/16F             | - 4.07 (2.63)      | - 1.87 (0.72)        |
| SL2 | 10O/20F            | - 4.02 (2.58)      | - 1.97 (0.82)        |
| SL3 | 16O/32F            | - 5.51 (4.07)      | - 3.48 (2.33)        |

FIG. 4. Free energy profiles of the spontaneous etching and self-limiting reactions for aHfO . T1, T2, and T3 are the temperatures where the self-limiting and 2 spontaneous etch reactions cross over for 8O/16F, 10O/20F, and 16O/32F models, respectively.

<!-- image -->

aHfO2 has 19 oxygen atoms in the supercell that could react with the HF molecules; therefore, we study the FEPs for two other SL product models, 10O/20F (SL2) and 16O/32F (SL3) as shown in Table II and Fig. 4 compares their thermodynamic stability with the 8O/16F model. For the 10O/20F model, 10 of the surface oxygen are removed and 20 fluorine are added to replace them. For 16O/32F, 16 oxygen are removed, and 32 fluorine are added to replace them. All three SL product states are more favorable than the SE reaction at 0 and 520 K with positive minimum barriers as shown in Table II. Experimental work showed that the HF reaction is self-limiting on amorphous HfO2 at 250 °C (523 K). 40 Figure 4 shows that the self-limiting product state models are more favorable than the spontaneous etch reaction at 523 K with the 16O/32F (SL3) being favorable up to 1302 K.

## B. Adsorption of one HF to the bare amorphous HfO2 surface

One HF molecule was adsorbed at the bare surface of aHfO2 on different binding sites (labeled A, B, and C) that were chosen at random as typical examples of possible binding sites on the aHfO2 surface. We computed the change in energy upon adsorption of the HF molecule at the aHfO2 surface,

$$E ( H F ^ { a d s } ) = E ( H f O _ { 2 } - H F ) { - [ E ( H f O _ { 2 } ) + E ( H F _ { ( g ) } ) ] },$$

where E(HfO2 -HF) is the total energy of the system with HF adsorbed and relaxed, E(HfO2) is the total energy of the bare aHfO2 surface, and E(HF(g)) is the gas-phase energy of a free HF molecule.

At each binding site, the HF molecule spontaneously dissociated to form Hf -F and O -H bonds as shown in Fig. 5. Similar to the crystalline HfO2 and ZrO2, 43 HF dissociation proceeds after a stable metal -fluorine bond is formed. The Hf -F and O H bond -

25 March 2025 10:19:29

<!-- image -->

<!-- image -->

lengths are shown for each binding site in Fig. 5. The computed adsorption energies for the dissociative adsorption of one HF molecule on the bare surface of aHfO2 are -2.17, -2.92, and -2.00 eV at sites A, B, and C, respectively. These adsorption energies are more negative than on cHfO2, most likely as a result of the surface disorder and range of coordination numbers of the surface atoms. This indicates that the fluorination steps in thermal self-limiting etch of aHfO2 would proceed faster than on cHfO2. The surface O atoms are l-fold, 2-fold, or 3-fold coordinated by surface Hf atoms with the 3-fold being dominant in the model used in this study. The surface Hf atoms are 5-fold, 6-fold, or 7-fold coordinated by surface O atoms with the 6-fold being dominant in the model used in this study. The lower coordination numbers in aHfO2 promote the interaction with HF and metal fluorination.

## C. Stability of higher HF coverages

Similar to our previous study on crystalline HfO2 and ZrO2, higher HF coverages were examined by introducing up to 34 randomly oriented HF molecules per supercell approximately 3 Å from the bare surface of aHfO2. This was studied to see if higher HF coverages would result in complete dissociation or a mixture of molecular and dissociative adsorption of the HF molecules. There are 18 topmost hafnium atoms on the surface of the supercell that may form Hf -F bonds and 19 surface oxygen atoms that can form O H bonds or as seen -in some cases H2O and H2O2. For HF

coverages using 2, 3, 4, 5, and 8 molecules per supercell three different configurations (labeled A, B, and C) were used, for the 16 HF coverages two configurations (A and B) were used, and one configuration for HF coverages of 28, 30, 32, and 34 molecules per supercell. Some configurations from HF coverages of 2, 3, 4, and 5 HF resulted in spontaneous complete dissociation of the adsorbed HF molecules as shown in Fig. 6. There was a mixture of molecular and dissociative adsorption of the HF molecules in all other HF adsorption configurations (see supplementary material, 65 Sec. II, at for the relevant geometries). The molecularly adsorbed HF molecules are likely to remain bonded to the surface in the next ALE step as they form strong bonds (Hf -F 6.7 eV) 64 and would likely dissociate when the kinetic barriers are reduced in the reactor during the ALE process. Similar to our previous study 43 on crystalline HfO2, the HF molecules that did not dissociate in the relaxed geometries form hydrogen bonds with the remaining HF molecules and dissociated F atoms, and at higher HF coverages, a more extensive hydrogen-bonded network is expected.

The binding energies per HF and per unit surface area of the material were computed as shown in Table III. As the number of Hf F bonds increases on the bare aHfO2 -surface with higher HF coverages, the binding energy per surface area becomes more favorable as shown in Table III and Fig. 7(c) with Hf -F coverage from 1.1 ± 0.3 to 9.0 ± 0.3 HF/nm 2 with surface binding energies from -5.3 to -20.0 eV/nm 2 (see the supplementary material, 65 Sec. III, for an explanation of the error bar).

<!-- image -->

25 March 2025 10:19:29

<!-- image -->

TABLE III. Adsorbate coverages and binding energies for the HF coverages on aHfO2.

| Geometry   |   Adsorbed HF (nm - 2 ) |   Hf - F (nm - 2 ) |   Dissociated HF (nm - 2 ) | Ebind (eV/ HF)   | Ebind (eV/ nm 2 )   |
|------------|-------------------------|--------------------|----------------------------|------------------|---------------------|
| 2HF A      |                     1.1 |                0.5 |                        0.5 | - 1.3            | - 1.4               |
| 2HF B      |                     1.1 |                1.1 |                        1.1 | - 2.2            | - 2.4               |
| 2HF C      |                     1.1 |                1.1 |                        1.1 | - 5.0            | - 5.3               |
| 3HF A      |                     1.6 |                1.1 |                        1.1 | - 1.7            | - 2.7               |
| 3HF B      |                     1.6 |                1.6 |                        1.6 | - 1.7            | - 2.8               |
| 3HF C      |                     1.6 |                1.6 |                        1.6 | - 2.3            | - 3.6               |
| 4HFA       |                     2.1 |                1.6 |                        1.6 | - 3.4            | - 7.2               |
| 4HFB       |                     2.1 |                2.1 |                        2.1 | - 1.8            | - 3.8               |
| 4HFC       |                     2.1 |                1.6 |                        1.6 | - 1.9            | - 3.9               |
| 5HFA       |                     2.7 |                2.7 |                        2.7 | - 3.4            | - 8.9               |
| 5HFB       |                     2.7 |                2.7 |                        2.7 | - 3.1            | - 8.1               |
| 5HFC       |                     2.7 |                2.1 |                        2.1 | - 1.7            | - 4.4               |
| 8HFA       |                     4.2 |                3.7 |                        3.2 | - 1.6            | - 6.6               |
| 8HFB       |                     4.2 |                3.7 |                        3.2 | - 1.6            | - 6.7               |
| 8HFC       |                     4.2 |                3.2 |                        2.7 | - 2.2            | - 9.4               |
| 16HFA      |                     8.5 |                6.4 |                        5.3 | - 1.7            | - 14.6              |
| 16HFB      |                     8.5 |                3.7 |                        3.7 | - 1.2            | - 9.9               |
| 28HF       |                    14.8 |                6.9 |                        6.4 | - 1.2            | - 17.7              |
| 30HF       |                    15.9 |                7.4 |                        5.3 | - 1.1            | - 17.9              |
| 32HF       |                    16.7 |                9   |                        8   | - 1.2            | - 19.8              |
| 34HF       |                    18   |                9   |                        8   | - 1.1            | - 20.0              |

Hf F coverage versus adsorbed HF coverage is shown in plot -(a) in Fig. 7 with the HF coverages that resulted in complete dissociation lying along the correlation line. This corresponds to coverages of 1.1, 1.6, 2.1, and 2.7 HF/nm . The remaining data points 2 are HF coverages that correspond to geometries where partially dissociated HF and molecular adsorbed HF molecules are present and, therefore, lie below the correlation line. The Hf -F coverage starts to plateau at higher HF coverages suggesting a maximum coverage of 9.0 ± 0.3 Hf -F/nm 2 . Also, note that the number of Hf -F/nm 2 is the same for HF coverages 32 and 34 HF. It is also shown that saturation in the binding energy is not reached at high HF coverages and Hf F coverages, respectively, as shown in plots (b) and (c) in Fig. 7. -

<!-- image -->

<!-- image -->

We use the highest adsorbed HF coverage of 34 HF with Hf -F coverage of 9.0 ± 0.3 Hf -F/nm 2 as the maximum coverage for the aHfO2 etch rate prediction.

## D. Spontaneous formation of H2O and H2O2

H2O spontaneously formed in some of the relaxed geometries such as 5HF C, 8HF C, and 16 HF A as shown in Fig. 8. The dissociation of at least two HF molecules provides the hydrogen atoms required to form H2O as a reaction product, which removes oxygen from aHfO2 during ALE. The H O H bond angles were 103.5°, --105.1°, and 108.0° for 5HF C, 8HF C, and 16 HF A as shown in Fig. 8. The energy to remove H2O (energy of desorption) from the fluorinated surfaces of 5HF C, 8HF C, and 16 HF A, as typical examples where water was formed, was calculated using Eq. (5):

$$E _ { \text{des} } = \left ( E _ { H f O _ { 2 ( \text{surf} ) } / H F _ { ( \text{ad} ) } } + E _ { H _ { 2 } O _ { ( g ) } } \right ) - \left ( E _ { H f O _ { 2 ( \text{surf} ) } / H F _ { ( \text{ad} ) } / H _ { 2 } O _ { ( \text{ad} ) } } \right ).$$

The total energy of HF adsorbed on aHfO2 with the spontaneous H2O formed is represented by the term ' E HfO2(surf)/HF(ads)/H2O(ads) ' . H2O was removed from the fluorinated surface and the resulting geometry was relaxed. The term ' E HfO2(surf)/HF(ads) ' is the total energy of HF adsorbed on aHfO2 after removing H2O from the surface and ' E H2O(g) ' is the energy of the gas-phase H2O molecule. The desorption energies of H2O on geometries 5HF C, 8HF C, and 16 HF A are 1.97, 1.47, and 1.67 eV, respectively. With the high energy gain from HF adsorption at aHfO2, we expect facile water desorption once it is formed.

The spontaneous formation of H2O2 was also observed at higher HF coverages such as 28HF as shown in Fig. 9. Similar to H2O, the dissociation of at least two HF molecules provides the hydrogen atoms required to form H2O2 as a reaction product which removes oxygen from aHfO2. H2O2 formed in Fig. 9 had an O O bond length -of 1.47 Å, O H bond lengths -of 1.05 Å and 1.02 Å, and H -O O bond angles of 100.3° and 104.5°. The energy -to remove H2O2 (energy of desorption) from the fluorinated surface of 28HF was calculated using Eq. (5), where the ' H2O ' terms were replaced with ' H2O2. ' The desorption energy was calculated to be 0.47 eV which is low and can be achievable under process conditions to remove H2O2. Only the spontaneous

<!-- image -->

FIG. 7. (a) Scatter plot for Hf -F coverage vs total HF coverage for the surface coverage values in Table III. Plots (b) and (c) show the change in binding energy per square nanometer with an increase in HF and Hf -F coverage, respectively.

<!-- image -->

<!-- image -->

FIG. 8. Relaxed geometries for HF coverages (a) 5HF C, (b) 8HF C, and (c) 16HF A were H2O formed spontaneously. Color coding is the same as in Fig. 5.

formation of H2O was observed in our previous study of HF coverages on crystalline HfO2 and ZrO2. 43

## E. Discussion

Comparing the spontaneous etch reaction to the self-limiting reaction for the 8O/16F SL product state model, at all temperatures less than 520 K using reactant and product pressures of 0.2 and 0.01 Torr, respectively, the HF pulse on aHfO2 is self-limiting in nature as the reaction energies for the self-limiting reaction were more favorable than the spontaneous etch reaction. From this, it is suggested that the first precursor pulse using HF will produce a stable and non-volatile layer of metal fluorides and H2O or H2O2 as byproducts. The reaction energies for the SL product state models 8O/16F and 10O/20F were similar up to 400 K due to the small difference in the degree of fluorination between the models. The 16O/32F SL product state model reaction energies were more favorable than the 8O/16F and 10O/20F reactions up to 1302 K. Compared to our previous study examining the fluorination step of crystalline HfO2, the reaction energies for the 16O/32F product state model were less favorable than the partially fluorinated SL product state models. 43 The greater the degree of fluorination on aHfO2, the more favorable the reaction energies are, showing aHfO2 favors higher fluorine content SL product states than less fluorinated SL product states, which will promote the self-limiting surface modification step. The replacement of oxygen with fluorine during fluorination may be easier due to the lower density of amorphous materials compared to crystalline materials. 40 The spontaneous etch reaction and the self-limiting reactions mentioned above were considered at a constant reactant (HF) pressure of 0.2 Torr and a by-product pressure of 0.01 Torr. The reactant gas pressure is adjustable in the reactor whereas the product pressure is not an experimentally adjustable parameter. 9 Examining the spontaneous

FIG. 9. Relaxed geometry for 28HF , where H O 2 2 formed spontaneously. Color coding is the same as in Fig. 5.

<!-- image -->

etch reaction and the self-limiting reactions at different reactant pressures at a constant product pressure was beyond the scope of this study. A previous study of the thermal ALE of TiO2 using HF by Natarajan et al. examined the influence of reactant and product pressures on the FEPs of the spontaneous etch and self-limiting reactions that are similar to this study. 9 It was found that the temperature at which the FEPs of the spontaneous etch and selflimiting reactions cross over is constant at 360 K with respect to an increase in the reactant pressure with a constant product pressure. 9

HF coverages on aHfO2 ranging from 1.1 ± 0.3 to 18.0 ± 0.3 HF/nm 2 resulted in complete dissociation or mixed dissociated and molecular HF adsorption. Water and hydrogen peroxide form spontaneously after relaxation and their computed desorption energies are low enough to be overcome under process conditions. Maximum coverage of 9.0 ± 0.3 Hf -F/nm 2 was found at higher HF coverages to be used to calculate a theoretical etch rate. The surface area of the aHfO2 supercell is 1.88 nm 2 with 18 Hf atoms that can form Hf -F bonds that correspond to a coverage of 9.5 ± 0.3 Hf/nm . 2 Using the maximum coverage of Hf F -9.0 ± 0.3 Hf -F/nm 2 , there will be about 0.95 F atoms per surface Hf. Similar to the analysis done in previous theoretical etch rate calculations for crystalline Al O , 2 3 44 HfO2, and ZrO2, 43 the amount of Hf that can be etched is one-quarter of the Hf F coverage which is -2.3 ± 0.1 Hf/(nm 2 cycle) for aHfO2. As the surface concentration of Hf atoms is 9.5 ± 0.3 Hf/nm , 2 this etch rate corresponds to 0.2 monolayer/cycle. This corresponds to -78.8 ± 0.8 ng/(cm 2 cycle) and using our DFT density of bulk aHfO2 (9.62 g/cm ), our theo3 retical etch rate for aHfO2 is -0.82 ± 0.02 Å/cycle. Our theoretical etch rate for cHfO2 is -0.61 ± 0.02 Å/cycle. 43 The theoretical etch rate for aHfO2 is greater than the theoretical etch rate for cHfO 2 by 0.21 Å/cycle. Etch rates calculated from the experiment can differ with temperature and the reactant used in the second pulse. It was found experimentally using HF as the fluorinating reagent and DMAC as the ligand-exchange reagent at 250 °C the etch rate was 0.68 Å/cycle for aHfO2 and 0.08 Å/cycle for cHfO2. 40 Using HF as the fluorinating reagent and TiCl4 as the ligand-exchange reagent at 250 °C the etch rate was 0.36 Å/cycle for aHfO2 and 0.02 Å/cycle for cHfO2. 40 We, therefore, qualitatively show the enhanced etch rate for aHfO2 compared to cHfO2 and provide origins of this enhanced etching on aHfO2.

Unlike experimental etch rates, theoretical etch rates do not take kinetic effects into account. Hence, the maximum etch rate to remove a monolayer (ML) of material from aHfO2 is also calculated. For one ML removal, 18 Hf atoms are used which requires a Hf F coverage of 38.2 ± 0.3 F/nm . -2 An etch rate of -3.47 Å/cycle was computed for one ML removal using the same method for calculating the theoretical etch rate. If an experimental etch rate was

25 March 2025 10:19:29

<!-- image -->

greater than -3.47 Å/cycle it would suggest that subsurface Hf atoms are being etched and the reaction is no longer self-limiting. The published etch rates for metal oxides 40 are much lower than this maximum etch rate further confirming that self-limiting etching is indeed observed.

The difference seen in thermal ALE etch rates of amorphous and crystalline HfO2 may be due to higher density crystalline materials having bond lengths and configurations that are more uniform than for amorphous materials. 40 Amorphous materials may have void regions and undercoordinated atoms that allows for more binding sites during fluorination. HF adsorption studies for crystalline HfO2 showed that every surface-bound F atom had a coordination number of one with surface Hf for Hf -F coverage of 7.0 ± 0.3 F/nm 2 43 . For amorphous HfO2, the coordination number for surface-bound F atoms range from one to three, for a Hf -F coverage of 9.0 ± 0.3 F/nm . 2 The greater the surface is fluorinated; the more material can be removed and a greater etch rate is obtained.

## IV. SUMMARY AND CONCLUSIONS

In this paper, we present DFT calculations to understand the nature of the HF pulse on amorphous HfO2 for thermal ALE. A thermodynamic analysis of the self-limiting and spontaneous etch reactions representing the fluorination on amorphous HfO2 allowed us to predict whether the SE or SL reaction is favorable at a given temperature and a given pressure. At temperatures less than 520 K, the HF reaction is found to be in the preferred selflimiting state. This is a relatively inexpensive way to screen the reactant molecules for ALE of any given substrate. The adsorption of HF molecules on amorphous HfO2 for HF coverages ranging from 1.1 ± 0.3 to 18.0 ± 0.3 HF/nm 2 along with analysis of H2O and H2O2 formation was studied. From this analysis, we predict a theoretical etch rate based on the maximum possible coverage of surface-bound HF for amorphous HfO2 which was calculated to be -0.82 ± 0.02 Å/cycle. This computed etch rate for amorphous HfO2 is greater than the etch rate computed for crystalline HfO2 from our previous study. We can use the presented methodology for the first pulse on crystalline and amorphous metal oxides to examine other reagents such as SF4 and XeF2 with a similar analysis.

## ACKNOWLEDGMENTS

We acknowledge support for this work from the LAM Research and the Science Foundation Ireland -NSF China Partnership Program, NITRALD Grant No. 17/NSFC/5279. We are grateful for access to Tyndall computing facilities supported by SFI and the Irish Centre for High-End Computing, www.ichec.ie. J.J.G.M. acknowledges financial support from the FusionCAT project (No. 001-P-001722) co-financed by the European Union Regional Development Fund within the framework of the ERDF Operational Program of Catalonia 2014 -2020 with a grant of 50% of total cost eligible, and the access to HPC resources at the National Supercomputing Center in Shenzhen, acquired with funding from the Postdoctoral Science Foundation of China (Grant No. 2018M643152).

## AUTHOR DECLARATIONS

## Conflict of interest

The authors have no conflicts of interest to declare.

## DATA AVAILABILITY

The data that support the findings of this study are openly available in GitHub at https://github.com/RitaMull/Thermal-ALEaHfO2-using-HF, Ref. 66.

## REFERENCES

- 1 K. J. Kanarik, T. Lill, E. A. Hudson, S. Sriraman, S. Tan, J. Marks, V. Vahedi, and R. A. Gottscho, J. Vac. Sci. Technol. A 33 , 020802 (2015).
- 3 A. Fischer, A. Routzahn, S. M. George, and T. Lill, J. Vac. Sci. Technol. A 39 , 030801 (2021).
- 2 S. M. George, Accounts Chem. Res. 53 , 1151 (2020).
- 4 Y. Lee and S. M. George, J. Phys. Chem. C 123 , 18455 (2019).
- 6 J. Hennessy, C. S. Moore, K. Balasubramanian, A. D. Jewell, K. France, and S. Nikzad, J. Vac. Sci. Technol. A 35 , 041512 (2017).
- 5 N. Miyoshi, H. Kobayashi, K. Shinoda, M. Kurihara, K. Kawamura, Y. Kouzuma, and M. Izawa, J. Vac. Sci. Technol. A 40 , 012601 (2021).
- 7 J. Hennessy, A. D. Jewell, J. P. Jones, G. M. Crouch, and S. Nikzad, ACS Appl. Mater. Interfaces 13 , 4723 (2021).
- 9 S. Kondati Natarajan, A. M. Cano, J. L. Partridge, S. M. George, and S. D. Elliott, J. Phys. Chem. C 125 , 25589 (2021).
- 8 P. C. Lemaire and G. N. Parsons, Chem. Mater. 29 , 6653 (2017).
- 10
- N. R. Johnson and S. M. George, ACS Appl. Mater. Interfaces 9 , 34435 (2017).
- J. C.Gertsch,A.M.Cano,V.M.Bright,andS.M.George,Chem.Mater. 31 , 3624(2019). 11
- 12 A. Mameli, M. A. Verheijen, A. J. M. Mackus, W. M. M. Kessels, and F. Roozeboom, ACS Appl. Mater. Interfaces 10 , 38588 (2018).
- 14 N. R. Johnson, H. Sun, K. Sharma, and S. M. George, J. Vac. Sci. Technol. A 34 , 050603 (2016).
- 13 Y. Lee, N. R. Johnson, and S. M. George, Chem. Mater. 32 , 5937 (2020).
- 15 K. Shinoda, N. Miyoshi, H. Kobayashi, M. Izawa, K. Ishikawa, and M. Hori, J. Phys. D: Appl. Phys. 52 , 475106 (2019).
- 18 C. Kauppinen, S. A. Khan, J. Sundqvist, D. B. Suyatin, S. Suihkonen, E. I. Kauppinen, and M. Sopanen, J. Vac. Sci. Technol. A 35 , 060603 (2017).
- 16 V. Sharma, S. Kondati Natarajan, S. D. Elliott, T. Blomberg, S. Haukka, M.E. Givens, M. Tuominen, and M. Ritala, Adv. Mater. Interfaces 8 , 2101085 (2021). 17 T. Ohba, W. Yang, S. Tan, K. J. Kanarik, and K. Nojiri, Jpn. J. Appl. Phys. 56 , 06HB06 (2017).
- 19 V. Sharma, S. D. Elliott, T. Blomberg, S. Haukka, M. E. Givens, M. Tuominen, and M. Ritala, Chem. Mater. 33 , 2883 (2021).
- 21 E. Mohimi, X. I. Chu, B. B. Trinh, S. Babar, G. S. Girolami, and J. R. Abelson, ECS J. Solid State Sci. Technol. 7 , P491 (2018).
- 20 D. R. Zywotko and S. M. George, Chem. Mater. 29 , 1183 (2017).
- 22 S. K. Natarajan, M. Nolan, P. Theofanis, C. Mokhtarzadeh, and S. B. Clendenning, ACS Appl. Mater. Interfaces 12 , 34959 (2020).
- 24 C. Fang, Y. Cao, D. Wu, and A. Li, Prog. Nat. Sci. Mater. 28 , 667 (2018).
- 23 S. K. Song, H. Saare and G. N. Parsons, Chem. Mater. 31 , 4793 (2019).
- 25 K.-Y. Lin, C. Li, S. Engelmann, R. L. Bruce, E. A. Joseph, D. Metzler, and G. S. Oehrlein, J. Vac. Sci. Technol. A 36 , 040601 (2018).
- 27 A. Hirata, M. Fukasawa, K. Kugimiya, K. Nagaoka, K. Karahashi, S. Hamaguchi, and H. Iwamoto, J. Vac. Sci. Technol. A 38 , 062601 (2020).
- 26 X. Wang, M. Wang, P. Biolsi, and M. J. Kushner, J. Vac. Sci. Technol. A 39 , 033003 (2021).
- 28 K. J. Kanarik, S. Tan, and R. A. Gottscho, J. Phys. Chem. Lett. 9 , 4814 (2018).
- 30 P. Raghu, C. Yim, F. Shadman, and E. Shero, AIChE J. 50 , 1881 (2004).
- 29 G. D. Wilk, R. M. Wallace, and J. M. Anthony, J. Appl. Phys. 89 , 5243 (2001).
- 31 P. Raghu, N. Rana, C. Yim, E. Shero, and F. Shadman, J. Electrochem. Soc. 150 , F186 (2003).

<!-- image -->

- 32 D. M. Hausmann, E. Kim, J. Becker, and R. G. Gordon, Chem. Mater. 14 , 4350 (2002).
- 34 P. R. Chalker et al. , Appl. Phys. Lett. 93 , 182911 (2008).
- 33 E. Cockayne, J. Appl. Phys. 103 , 084103 (2008).
- 35 Y. Lee and S. M. George, Chem. Mater. 29 , 8202 (2017).
- 37 R. Rahman, E. C. Mattson, J. P. Klesko, A. Dangerfield, S. Rivillon-Amy,
- 36 Y. Lee, C. Huffman, and S. M. George, Chem. Mater. 28 , 7657 (2016).
- D. C. Smith, D. Hausmann, and Y. J. Chabal, ACS Appl. Mater. Interfaces 10 , 31784 (2018).
- 39 W. Xie, P. C. Lemaire, and G. N. Parsons, ACS Appl. Mater. Interfaces 10 , 9147 (2018).
- 38 Y. Lee and S. M. George, J. Vac. Sci. Technol. A 36 , 061504 (2018).
- 40 J. A. Murdzek and S. M. George, J. Vac. Sci. Technol. A 38 , 022608 (2020).
- 42 J. Chen, W. Jong Yoo, and D. S. H. Chan, J. Electrochem. Soc. 153 , G483 (2006).
- 41 J. A. Murdzek, A. Rajashekhar, R. S. Makala, and S. M. George, J. Vac. Sci. Technol. A 39 , 042602 (2021).
- 43 R. Mullins, S. Kondati Natarajan, S. D. Elliott, and M. Nolan, Chem. Mater. 32 , 3414 (2020).
- 45 G. Kresse and J. Furthmüller, Phys. Rev. B 54 , 11169 (1996).
- 44 S. Kondati Natarajan and S. D. Elliott, Chem. Mater. 30 , 5912 (2018).
- 46 J. P. Perdew, K. Burke, and M. Ernzerhof, Phys. Rev. Lett. 77 , 3865 (1996).
- 48 S. K. Natarajan, M. Nolan, P. Theofanis, C. Mokhtarzadeh, and S. B. Clendenning, J. Vac. Sci. Technol. A 39 , 022603 (2021).
- 47 G. Kresse and D. Joubert, Phys. Rev. B 59 , 1758 (1999).
- 49 S. Plimpton, J. Comput. Phys. 117 , 1 (1995).
- 50 G. Broglia, G. Ori, L. Larcher, and M. Montorsi, Modell. Simul. Mater. Sci. Eng. 22 , 065006 (2014).
- 51 D. Ceresoli and D. Vanderbilt, Phys. Rev. B 74 , 125108 (2006).
- 53 J. Strand, M. Kaviani, V. V. Afanas ev, ' J. G. Lisoni, and A. L. Shluger, Nanotechnology 29 , 125703 (2018).
- 52 W. Shen, N. Kumari, G. Gibson, Y. Jeon, D. Henze, S. Silverthorn, C. Bash, and S. Kumar, J. Appl. Phys. 123 , 085113 (2018).
- 54 A. Togo and I. Tanaka, Scr. Mater. 108 , 1 (2015).
- 56 S. G. Balasubramani et al. , J. Chem. Phys. 152 , 184107 (2020).
- 55 TURBOMOLE v6.2 2010, A Development of University of Karlsruhe and Forschungszentrum Karlsruhe GmbH, 1989 -2007, TURBOMOLE GmbH, since 2007. Available from http://www.turbomole.com (accessed 27 Nov 2019).
- 57 A. Schäfer, H. Horn, and R. Ahlrichs, J. Chem. Phys. 97 , 2571 (1992).
- 59 T. V. Perevalov, V. A. Gritsenko, S. B. Erenburg, A. M. Badalyan, H. Wong, and C. W. Kim, J. Appl. Phys. 101 , 053704 (2007).
- 58 A. Schäfer, C. Huber, and R. Ahlrichs, J. Chem. Phys. 100 , 5829 (1994).
- 60 T. J. Chen and C. L. Kuo, J. Appl. Phys. 110 , 064105 (2011).
- 62 W. L. Scopel, A. J. R. da Silva, and A. Fazzio, Phys. Rev. B 77 , 172101 (2008).
- 61 Y. Wang, F. Zahid, J. Wang, and H. Guo, Phys. Rev. B 85 , 224110 (2012).
- 63 G. H. Chen, Z. F. Hou, and X. G. Gong, Appl. Phys. Lett. 95 , 102905 (2009).
- 65 See supplementary material at https://www.scitation.org/doi/suppl/10.1116/ 6.0001614 for the following (1) the pair distribution function of the amorphous HfO2 bulk model used in this study, (2) figures of the mixed molecular and dissociative adsorption of the HF molecules at the aHfO2 surface, and (3) explanation of the ±0.3 error bar.
- 64 Y. R. Luo, Comprehensive Handbook of Chemical Bond Energies (CRC, Boca Raton, FL, 2007).
- 66 R. Mull (2022). GitHub, https://github.com/RitaMull/Thermal-ALE-aHfO2using-HF.