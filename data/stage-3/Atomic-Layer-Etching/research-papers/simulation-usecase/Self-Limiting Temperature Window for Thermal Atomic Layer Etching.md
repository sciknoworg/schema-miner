<!-- image -->

pubs.acs.org/cm

<!-- image -->

## Self-Limiting Temperature Window for Thermal Atomic Layer Etching of HfO2 and ZrO2 Based on the Atomic-Scale Mechanism

Rita Mullins, ∥ Suresh Kondati Natarajan, ∥ Simon D. Elliott, and Michael Nolan *

<!-- image -->

ABSTRACT: HfO2 and ZrO2 are two highk materials that are important in the downscaling of semiconductor devices. Atomiclevel control of material processing is required for the fabrication of thin /uniFB01 lms of these materials at nanoscale device sizes. Thermal atomic layer etching (ALE) of metal oxides, in which up to one monolayer of the material can be removed, can be achieved by sequential self-limiting (SL) /uniFB02 uorination and ligand-exchange reactions at elevated temperatures. However, to date, a detailed atomistic understanding of the mechanism of thermal ALE of these technologically important oxides is lacking. In this paper, we investigate the hydrogen /uniFB02 uoride (HF) pulse in the /uniFB01 rst step in the thermal ALE process of HfO2 and ZrO2 using /uniFB01 rst-principles simulations. We introduce Natarajan -Elliott analysis, a thermodynamic methodology, to compare reaction models representing the self-limiting (SL) and continuous spontaneous etching (SE) processes taking place during an ALE pulse. Applying this method to the /uniFB01 rst HF pulse on HfO2 and ZrO2, we found that thermodynamic barriers impeding continuous etching are present at ALErelevant temperatures. We performed explicit HF adsorption calculations on the oxide surfaces to understand the mechanistic details of the HF pulse. A HF molecule adsorbs dissociatively on both oxides by forming metal -F and O -H bonds. HF coverages ranging from 1.0 ± 0.3 to 17.0 ± 0.3 HF/nm 2 are investigated, and a mixture of molecularly and dissociatively adsorbed HF molecules is present at higher coverages. Theoretical etch rates of -0.61 ± 0.02 Å/cycle for HfO2 and -0.57 ± 0.02 Å/cycle for ZrO2 were calculated using maximum coverages of 7.0 ± 0.3 and 6.5 ± 0.3 M -F bonds/nm 2 , respectively (M = Hf, Zr).

## ■ INTRODUCTION

The scaling of semiconductor devices means that features are required at the nanometer scale. As a result of the shrinking of device feature sizes, SiO 2 gate dielectrics would be so thin that electron tunneling through the dielectric layer, which leads to high leakage currents, 1 is impossible to avoid. Materials with high dielectric constant, k , allow a high drive current to be maintained, while minimized leakage current and a low equivalent oxide thickness can be achieved. 1 HfO2 and ZrO2 are highk dielectric materials with dielectric constants of 22 -23, 1,2 which are used in semiconductor devices. HfO2 and ZrO2 are also thermodynamically stable when interfaced with silicon in semiconductor applications. 3 However, conformal nanometer-scale feature sizes in high-aspect-ratio structures are di /uniFB03 cult to achieve with traditional wet and dry chemical etching methods, which do not permit the level of control required. Recently, atomic layer etching (ALE) has gained

<!-- image -->

signi /uniFB01 cant interest for the controlled etching of thin /uniFB01 lms, in particular, for nanoelectronic devices. ALE shares many features with atomic layer deposition (ALD) and can be considered as the reverse of ALD. ALE permits the removal of thin /uniFB01 lms with atomic-scale precision using sequential and selflimiting (SL) surface reactions, 4 -9 similar to ALD.

Traditional ALE processes are anisotropic as they use directional high-energy ion bombardment to remove the modi ed surface layer. /uniFB01 6 Thermal ALE relies on temperature

Received:

December 5, 2019

Revised:

April 1, 2020

Published:

April 2, 2020

<!-- image -->

Figure 1. Schematic model of the thermal ALE process.

<!-- image -->

and thermochemically favorable reactions to remove surface species. 10 While there have been many examples of thermal ALE of a range of materials, including HfO2, 4,9,11,124,9,11,12 ZrO2, 4,12 SiO2, 13 Al2 O3, 12,14 -18 AlN, 19 AlF3, 20 TiO2, 21 TiN, 22,23 W, 24,25 WO3, 25 ZnO, 26 and GaN 27 and for other ALE techniques including Ar neutral beam ZrO2, 28 plasma ALE SiO2, 29,30 ZnO, 31 GaN, 32,33 and ALE of Si3N4 34 using infrared annealing, the details of the mechanism of the ALE process still require signi /uniFB01 cant work to understand.

The /uniFB01 rst step in ALE is the formation of a reactive but nonvolatile layer on the initial /uniFB01 lm, which is followed by a material removal step to take o /uniFB00 only the modi ed layer as /uniFB01 indicated schematically in Figure 1. The key aspect of the ALE process is the self-limiting modi /uniFB01 cation of the pristine /uniFB01 lm with the /uniFB01 rst precursor to produce a thin nonvolatile surface layer. The purpose of this modi /uniFB01 cation step is to form a reactive, but nonvolatile, layer that can be easily removed in the subsequent ligand-exchange step. 6,35 To date, reactions during thermal ALE are based on gas-phase /uniFB02 uorination that converts the metal-containing /uniFB01 lm into a layer of the corresponding nonvolatile metal /uniFB02 uoride. 4,7,11 For metal oxides, thermal ALE processes generally use HF for the /uniFB02 uorination step. 22 HF is a useful nucleophilic /uniFB02 uorination reactant in which the /uniFB02 uoride anion serves as the active reaction species. 36 This modi cation step in thermal ALE is the focus of this paper. /uniFB01

The other half of the thermal ALE cycle consists of a ligand exchange between a metal precursor and the newly formed /uniFB02 uoride layer at elevated temperatures, 4,7,11 for which examples include Sn(acac)2, 4 Al(CH3)3, 4,37 Al(CH3)2Cl, 4 SiCl4, 4 TiCl4, 11 BCl3, 21 and WF6. 24 This second reaction produces stable etch products, which are now volatile 36 and can be easily removed, leaving behind a /uniFB01 lm from which one layer or a fraction of a layer has been removed as shown schematically in Figure 1. Repeating this cycle results in controlled removal of layers from the original /uniFB01 lm. Other applications of thermal ALE include surface cleaning for the removal of metal impurities in semiconductor fabrication, conformal etching in high-aspect-ratio structures, and smoothing of surfaces to obtain /uniFB02 at and damage-free layers, which are also important in the semiconductor industry. 7,38 Therefore, thermal ALE is a strong candidate as a processing technology in current and future semiconductor device fabrication. 37

Given that it is di /uniFB03 cult to investigate the ALE reactions directly using experimental techniques, /uniFB01 rst-principles-based atomic-level simulations using density functional theory (DFT) can give deep insights into the precursor chemistry and the reactions that drive the etch of metal oxides. In this paper, the hydrogen /uniFB02 uoride (HF) pulse in the /uniFB01 rst step in thermal ALE of HfO2 and ZrO2 using DFT calculations will be examined. HF molecules adsorb at the surfaces of metal oxides by forming metal -F bonds, and there can also be hydrogen bonds between HF molecules. In addition, adsorbed HF may remain intact or dissociate. In the latter case, Hf -F/Zr -F and O H are formed on HfO2 -and ZrO2, similar to that in recent work on Al2O3 etch modeling. 39 The amount etched (etch rate) is determined by how much of the oxide surface is /uniFB02 uorinated and how much of the metal /uniFB02 uoride can be removed in the ligand exchange for one ALE cycle. 4

In addition to investigating HF adsorption, we introduce Natarajan -Elliott analysis (N -E analysis, in short) to predict the conditions at which a self-limiting (SL) or continuous spontaneous etch (SE) reaction becomes thermodynamically favorable, subject to kinetic barriers. This information is useful for directing experimental studies of thermal ALE. Self-limiting reactions are a necessary part of thermal ALE and allow the degree of etching to be well controlled and de /uniFB01 ned. We /uniFB01 nd that SL reactions are more favorable than the competing SE reactions for the HF pulse on HfO2 and ZrO2 at 0 K. The temperatures above which spontaneous etching is favored are 657 and 534 K for HfO2 and ZrO2, respectively, at typical thermal ALE reactant pressures. Introducing one HF molecule to the bare surfaces of HfO 2 and ZrO2 results in dissociative adsorption irrespective of the binding site. We determine the maximum coverage of metal -F bonds on the surface and use this coverage to calculate a theoretical etch rate. We also determine the maximum etch rate computed from the lattice constants of HfO2 and ZrO2 for one monolayer (ML) removal of Hf/Zr. We compare this maximum etch rate to experimental etch rates to calculate the number of Hf/Zr removed per surface area. We study the spontaneous formation of water that resulted from some of our relaxed geometries. This combined thermodynamic and mechanistic investigation using the /uniFB01 rstprinciples simulation allows us to understand and design novel ALE processes for other technologically relevant materials. We /uniFB01 rst present a thermodynamic analysis that shows that the /uniFB02 uorinated surface is preferred over the oxygen /uniFB02 uoride and then present a detailed analysis of the adsorption coverage of HF molecules at HfO2 and ZrO2, which allows us to also predict etch rates and number of metal atoms removed in a cycle.

## ■ COMPUTATIONAL METHODS

All reported surface slab calculations in this paper are performed using spin-polarized density functional theory as implemented in the VASP 40 5.4 package. The calculations are based on the generalized gradient approximation (GGA) using the Perdew -Burke -Ernzerhof (PBE) exchange -correlation (XC) functional. 41 The self-consistent energy for the electronic minimization is converged within 1 × 10 -4 eV, and the forces for ionic relaxation are converged within -2 × 10 -2 eV/Å. The default smearing method of Methfessel -Paxton /uniFB01 rst order is used with 0.1 eV broadening for electronic relaxation. The core

electrons are described by projector-augmented wave (PAW) potentials, 42 and the valence electrons (Hf: 6s 2 5d 2 , Zr: 5s 2 4d 2 , O: 2s 2 2p 4 , F: 2s 2 2p 5 , and H: 1s ) are treated using plane-wave basis sets 1 with a kinetic energy cuto /uniFB00 of 400 eV. For con /uniFB01 gurations 2HF B for HfO2 and ZrO2, we include the tag IVDW = 20 for the Tkatchenko -Sche /uniFB04 er scheme in our INCAR. We found that their adsorption energies were increased only by ≈ 0.05 eV by including this dispersion method and therefore we do not include it in the below analysis.

Relating SL and SE Processes: N -E Analysis. The relationship between SE and SL processes of a substrate exposed to a single gaseous reactant is described schematically in Figure 2. In an SL

Figure 2. Schematic representation of the relationship between continuous spontaneous etch (SE, red) and self-limiting (SL, green) processes. Δ G represents the reaction free energy.

<!-- image -->

reaction, represented by the solid green arrow in Figure 2, the reactant molecules passivate the material surface and form a nonvolatile layer that resists further reaction. Such a reaction is referred to as a ' surf → surf ' reaction

$$\text{SL} \colon A _ { \text{surf} } + B _ { \text{gas} } \to C _ { \text{surf} } & & ( 1 ) & & \text{cont}$$

with the reaction free energy de /uniFB01 ned as Δ G = X . Here, the starting surface A is necessarily di /uniFB00 erent from the /uniFB01 nal surface C . It is possible that byproducts are released into the gas phase during this reaction

$$\text{SL} \colon A _ { \text{surf} } + B _ { \text{gas} } \to C _ { \text{surf} } + D _ { \text{gas} } & & ( 2 ) \quad \text{overa}$$

Conversely, in a SE reaction (represented by the solid red arrow in Figure 2), the reactant molecules etch away units of bulk material continuously by forming stable and volatile etch byproducts. This continues until the supply of the reactant gas molecules is stopped or the substrate material is exhausted (e.g., an etch stop is reached). Such a reaction is referred to as a ' bulk → gas ' reaction

A negative value of Δ G means that the corresponding reaction is exergonic (favorable); otherwise, it is endergonic (unfavorable). The Δ G values are based on the SE and SL reactions as thermochemically isolated processes. However, we /uniFB01 nd it useful to consider also the overall energetics of the reaction pathway that theoretically links SL to SE (the green dotted line in Figure 2). It may be possible to form SE reaction products from the SL reaction products by overcoming one or several energetic barriers. While it is possible to compute kinetic barriers at the /uniFB01 rst-principles level, we omit this in favor of developing a computational approach that allows rapid screening. Balancing the energies in Figure 2 shows that these unknown barriers must be of magnitude at least Y -X (free energy di /uniFB00 erence of SL and SE

Figure 3. Schematic energy pro /uniFB01 les representing (a) preferred self-limiting, (b) purely self-limiting, (c) preferred etching, and (d) purely etching.

<!-- image -->

$$\Phi ^ { \prime } ) \quad \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \
 \quad \Phi ^ { \prime } \quad \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \
 \ \Phi ^ { \prime } \quad \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \

\Phi ^ { \prime } \quad \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \

\Phi ^ { \prime \prime } \quad \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \\ \Phi ^ { \prime } \quad \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \\ \Phi ^ { \prime } \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \\ \Phi ^ \prime } \quad \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \$$

$$\underset { \ \ \ } { s } \quad \ \text{SE} \colon A _ { \text{bulk} } + B _ { \text{gas} } \to E _ { \text{gas} }$$

with the reaction free energy Δ G = Y . Clearly, Y is independent of

A

surf

.

The reaction free energy Δ G at temperature T is computed as

$$\inf _ { i \mathfrak { p } } \Delta G = \Delta H - T \Delta S + R T \ln ( Q )$$

$$\stackrel { \cdot \cdot } { L } \quad \Delta H = \Delta E + \Delta Z P E + \Delta W ( T )$$

$$\Delta E = \sum _ { p } \mu E _ { p } - \sum _ { t } \mu E _ { t }$$

$$Q = \prod p _ { \text{products} } ^ { \mu } / \prod p _ { \text{reactants} } ^ { \mu }$$

In eq 5, Δ H and Δ S represent the changes in reaction enthalpy and reaction entropy, respectively. Since the partial pressures of the reactants and products are variable in the reaction chamber, the RT ln( Q ) term is included. Δ H in eq 6 includes three contributions, namely, electronic reaction energy Δ E , zero-point energy change Δ ZPE, and a temperature-dependent enthalpic contribution Δ W T ( ). While the reaction energy ( Δ E ) in eq 7 includes only the bonding information at temperature T = 0 K, the reaction free energy ( Δ G ) provides /uniFB01 nite temperature and pressure behavior of a particular reaction. In eq 7, μ refers to the stoichiometric coe /uniFB03 cient of the corresponding species and indices r and p indicate reactant and product species, respectively. The reaction quotient Q includes partial pressures of the gas-phase reactant and product molecules only. If the reactant and product pressures are the same, then ln Q becomes 0. A negative Δ S increases the free energy and tends to make the reaction more endergonic. Via the translational entropy, the value of Δ S is strongly dependent on the di /uniFB00 erence in molecularity between the products and the reactants. For example, if the number of gaseous molecules in the products is considerably smaller than in the reactants, then the Δ S value is likely to be negative and to result in an increase in the reaction free energy. In this work, we also evaluate the contribution from changes in surface entropy.

Table 1. Reaction Energies Δ E at 0 K and Reaction Free Energies Δ G at 500 K of the Model SE and SL Reactions Representing the HF Pulse on HfO2 and ZrO2 a

|       | reactions                                           | Δ E (eV/M)    | Δ G (eV/M)    |
|-------|-----------------------------------------------------|---------------|---------------|
| HfO 2 | HfO 2                                               | HfO 2         | HfO 2         |
| SE1   | 1HfO 2(b) + 4HF (g) → 1HfF 4(g) + 2H 2 O (g)        | - 0.91        | - 0.65        |
| SL1   | 1HfO 2(surf) + 4HF (g) → 1HfF 4(surf) + 2H 2 O (g)  | - 3.27 (2.36) | - 1.20 (0.55) |
| SE2   | 1HfO 2(b) + 2HF (g) → 1HfOF 2(g) + 1H 2 O (g)       | 3.87          | 3.10          |
| SL2   | 1HfO 2(surf) + 2HF (g) → 1HfOF 2(surf) +1 H 2 O (g) | - 1.64 (5.51) | - 0.60 (3.70) |
| ZrO 2 | ZrO 2                                               | ZrO 2         | ZrO 2         |
| SE1   | 1ZrO 2(b) + 4HF (g) → 1ZrF 4(g) + 2H 2 O (g)        | - 1.14        | - 0.89        |
| SL1   | 1ZrO 2(surf) + 4HF (g) → 1ZrF 4(surf) + 2H 2 O (g)  | - 3.04 (1.90) | - 1.00 (0.11) |
| SE2   | 1ZrO 2(b) + 2HF (g) → 1ZrOF 2(g) + 1H 2 O (g)       | 2.96          | 2.19          |
| SL2   | 1ZrO 2(surf) + 2HF (g) → 1ZrOF 2(surf) + 1H 2 O (g) | - 1.52 (4.48) | - 0.50 (2.69) |

a The value within parenthesis corresponds to the minimum barrier between the respective SE and SL reactions. The product state of SL1 and SL2 reactions is the 8O/16F surface of MO2 (M = Hf/Zr) as described in the previous section, and the reaction energy is listed per the modi /uniFB01 ed M atom.

reactions) in energy units. This term Y -X will be referred to as the ' minimum barrier ' in this paper.

Based on the values of X and Y , we can distinguish the four possible scenarios for the precursor pulse shown in Figure 3. Each pro /uniFB01 le in Figure 3 depicts a set of SL and SE reaction free energies separated by unknown energetic barriers, which in reality may consist of many barriers in the con /uniFB01 gurational space of the system. Computing all of the reaction pathways and barriers separating the SL and SE product states would be computationally demanding. The aim of this methodology is to form useful conclusions without computing these pathways, thus accelerating process design. The minimum possible barrier to drive the etch reaction from the SL to SE product state is Y -X in energy units as mentioned earlier. In the energy pro /uniFB01 les, the SL reaction appears on the left-hand side of the horizontal axis since the precursor molecules must /uniFB01 rst react with the surface before accessing the bulk. To cause etching from there onward, the precursor molecules may have to lift the surface atoms out of their lattice positions or di /uniFB00 use into the subsurface region and /uniFB01 nally form volatile products. Therefore, the SE reaction is shown to the right of the SL reaction in these energy pro /uniFB01 les.

Depending on whether the SL reaction or the SE reaction is the most favorable (based on their Δ G values), the energy pro /uniFB01 les in Figure 3 are classi /uniFB01 ed broadly as self-limiting or etching. The energy pro /uniFB01 le in Figure 3a is termed as ' preferred self-limiting ' since the SL reaction is more thermodynamically favored than the SE reaction, even though both SL and SE reactions are exergonic. Here, there is a possibility of etching if the collective barrier (at least Y -X ) could be overcome under the reactor conditions. If the energy pro /uniFB01 le in Figure 3a is shifted along the vertical axis such that the SL reaction is exoergic and the SE reaction is endergonic, we obtain the energy pro /uniFB01 le in Figure 3b termed as ' purely self-limiting . This is the ideal ' energy pro /uniFB01 le for the surface modi /uniFB01 cation pulse in an ALE process since unlimited etching is energetically unfavorable. The energy pro /uniFB01 le in Figure 3c is the reverse of that in Figure 3a since the SE reaction is energetically more favorable than the SL reaction ( Y -X &lt; 0). The collective barrier, if any, for etching would be comparatively lower than in the preferred self-limiting state, and it may be easily breached under the reactor conditions. Therefore, the energy pro /uniFB01 le in Figure 3c is termed as ' preferred etching . Figure 3d is obtained by ' shifting the energy pro /uniFB01 le in Figure 3c such that the SL reaction is endergonic and the SE reaction is exergonic. This pro /uniFB01 le is termed as ' purely etching ' since the precursor molecules should readily volatilize the surface atoms and proceed to the subsurface region to cause bulk etching without signi /uniFB01 cant barriers. This is the ideal energy pro /uniFB01 le for a SE pulse. Thus, the shape of the energy pro /uniFB01 le at any given temperature and pressure will allow us to predict the net e /uniFB00 ect of the precursor -substrate interaction. We refer to this computational approach as the N -E analysis.

To summarize, by comparing the energetics and thermodynamics of the SE (bulk → gas) and SL (surf → surf) reactions, along with the minimum energetic barrier separating them, we can predict whether the gas of a particular precursor pulse will spontaneously etch the substrate material at the temperatures and pressures of interest.

Bulk and Slab Models. We have optimized the bulk unit cell of monoclinic HfO2 (space group: P 21 / ) and ZrO2 c (space group: P 21 / c ) by simultaneously relaxing the ionic positions, cell shape, and cell volume with an energy cuto /uniFB00 of 550 eV and a Monkhorst -Pack k -point sampling mesh of (6 × 6 × 6). The bulk monoclinic unit cells of HfO2 and ZrO2 have four metal atoms and eight O atoms. The optimized lattice constants of HfO 2 from this setup are a = 5.142 Å, b = 5.195 Å, and c = 5.326 Å, while the lattice constants of ZrO 2 are a = 5.140 Å, b = 5.189 Å, and c = 5.239 Å. Comparing our values to the experimental values for the baddeleyite phase, 43 the deviations for HfO2 are a = 0.43%, b = 0.48%, and c = 0.96% and for ZrO2 are a = 0.58%, b = 0.78%, and c = 1.89%.

A surface slab of monoclinic HfO2 and ZrO2 with a (111) orientation is used for the surface calculations as this is the most stable facet at low temperatures and has the lowest surface energy. 43,44 A surface supercell of HfO 2 and ZrO2 with a (2 × 2) expansion of the hexagonal unit cell and 16 Å of vacuum separating the slabs is used for the surface models; this has a stoichiometry of Hf80/Zr80 O160 per supercell. It consists of /uniFB01 ve layers of 16 HfO2/ZrO2 units, and a k -point sampling mesh of (2 × 2 × 1) is used for geometry optimization. The product states of the SL reactions needed for the N E analysis -are obtained by adding two F atoms per surface O removed (for brevity, we denote this ratio 1O/2F) from the top layer of the slab models. We consider three product states for our analysis: 8O/16F, 12O/24F, and 16O/32F. For the surface slabs, enthalpy H and entropy S are computed using the Phonopy code by considering only the /uniFB01 rst layer of atoms. 45 The calculations for the reactant molecules and gas-phase byproducts are performed in VASP with a large periodic box of dimensions 15.0 Å × 16.0 Å × 15.5 Å and 400 eV plane-wave energy cuto /uniFB00 . The enthalpy and entropy for the gasphase molecules were calculated from the freeh program in the Turbomole suite 46 at 1 atm pressure. The above calculations are performed with the PBE exchange -correlation functional 41 and a polarized triple ζ basis set (def-TZVPP) 47,48 and default medium grid.

For the HF adsorption studies, the molecules are introduced at various surface sites and at di /uniFB00 erent coverages on the (111) surface slabs of HfO2 and ZrO2. The absorbate coverages and binding energies are computed, and a surface model with maximum coverage of metal -F is then used to derive the theoretical etch rate for the HF pulse on HfO2 and ZrO2.

The VASP data can be found at the GitHub repository https:// github.com/RitaMull/Thermal-ALE-HfO2-and-ZrO2-with-HF.

## ■ RESULTS

In the /uniFB01 rst part of this section, we will perform the N E -analysis and compare self-limiting with spontaneous etch

reaction models. In the next part, the adsorption mechanism of HF at a range of coverages on HfO2 and ZrO2 will be studied, together with analysis of H O formation. Finally, a theoretical 2 etch rate is predicted based on the maximum possible coverage of dissociated HF on the material surfaces.

Self-Limiting vs Spontaneous Etch. Comparing the energetics and thermodynamics of the SL and SE model reactions for the /uniFB02 uorination of HfO2 and ZrO2 using HF, we can predict whether the HF pulse will spontaneously etch or result in a self-limiting reaction at the given conditions. Model reactions representing the HF pulse on HfO2 and ZrO2 are listed in Table 1 together with the corresponding reaction (free) energies at 0 and 500 K, with a reactant pressure of 0.2 Torr and a product pressure of 0.01 Torr, as computed from DFT calculations.

This table also includes the minimum barrier to cause spontaneous etch as already discussed. Negative minimum barriers indicate that spontaneous etch is thermodynamically favorable and is hindered only by kinetic barriers, if any. Two SE reactions and two SL reactions are postulated for HF exposure on both HfO2 and ZrO2. The SE reactions involve the complete conversion of the bulk metal oxide into volatile metal /uniFB02 uoride (SE1) or metal oxy /uniFB02 uoride (SE2) and water, while the corresponding SL reactions involve conversion of the outermost surface layer of the metal oxide into the nonvolatile metal (oxy) /uniFB02 uoride (terminating the metal oxide), releasing water molecules. For the SE1 reaction of Hf/ZrO2, four HF molecules are needed to etch away one unit of bulk Hf/ZrO2 to form Hf/ZrF4 and H2O. For the SE2 reaction for Hf/ZrO2, two HF molecules are required to etch a unit of Hf/ZrO2 to form Hf/ZrOF2 and H2O. In the SE reactions, the surface of the material before and after each precursor pulse will be identical and therefore their contributions are ignored from the reaction model. For the SL reactions, the surfaces are not identical before and after the pulse and their contributions have to be included. In Table 1, the SL product state of the surfaces is 8O/16F (refer to Supporting Information (SI) for the geometry).

A negative reaction (free) energy ( Δ G ) means that the reaction is exergonic (favorable), and a positive Δ G means that the reaction is endergonic (unfavorable). The SE2 reactions forming volatile metal oxy /uniFB02 uorides are unfavorable at 0 and 500 K as the reaction (free) energy is positive (unfavorable), whereas the SE1 reactions forming volatile metal /uniFB02 uorides are favorable. For all of the SL -SE combinations at 0 K, for both materials, the minimum barrier to etch was positive, suggesting that self-limiting reaction is the most favorable energetically. At 500 K, the thermodynamic barrier is reduced considerably, which means high temperatures favor SE reactions. In any case, below 500 K, the minimum barrier is positive, suggesting that SL reactions are preferred for both metal oxides. Therefore, up to 500 K, the reactions are in preferred self-limiting state for both materials. Therefore, we can propose that the reaction of HF in the /uniFB01 rst step will self-limit on both metal oxides at least up to 500 K.

As the SE1 reactions forming the volatile metal /uniFB02 uoride are more favorable than the SE2 reactions that form the oxy /uniFB02 uoride, we will consider only the SE1 reactions for further analysis. Moreover, the barrier to etch was very high for the SL2 -SE2 reactions as compared to the SL1 -SE1, even at 500 K, suggesting that spontaneous formation of oxy /uniFB02 uoride is not probable at ALE-relevant temperatures.

Reaction Free Energy Pro /uniFB01 les (FEPs). The free energy pro /uniFB01 les (FEPs) of the reactions in Table 1 are discussed in this section. Comparing the reaction FEPs of the SE and SL reactions, we can determine at a given temperature and reactant pressure whether the HF pulse will favor spontaneous etching or self-limited conversion of HfO2 and ZrO2 into a nonvolatile metal /uniFB02 uoride layer. Here, we use a reactant pressure of 0.2 Torr and a product pressure of 0.01 Torr within a temperature range of 0 -1000 K. The various contributions to the free energy for the example of the SE1 reaction for HfO 2 are plotted in Figure 4.

Figure 4. Contributions to the reaction FEP of the SE1 reaction of HfO2 shown in Table 1. RT ln( Q ) in gold accounts for the partial pressures of the reactants and products, enthalpic contribution ( Δ W ) is given in dark blue, entropy term ( T Δ S ) in gray, reaction energy ( Δ E ) in light blue, the sum of reaction energy and zero-point energy change ( Δ E + Δ ZPE) in brown, and reaction free energy ( Δ G ) in green.

<!-- image -->

In Figure 4, the Δ E and Δ ZPE contributions are temperature independent. T Δ S is the entropy contribution and is 0 eV at 0 K and -0.5 eV at 1000 K. The entropy term decreases with increasing temperature because four gaseous reactant molecules result in the formation of three product molecules only. The RT ln( Q ) and Δ W contributions are clearly smaller in comparison to the entropy term. They decrease the free energy at high temperatures and compete against the entropy term that increases the free energy with temperature. The FEP of this reaction at the reactant and product pressures stated above is exergonic up to 1000 K. The other reactions show similar contributions.

The FEPs of the SE1 and SL1 reactions of HfO2 and ZrO2 are compared in Figure 5. For HfO2, the self-limiting reaction is preferred up to 656 K. At 657 K, the SE1 and SL1 reactions are isoenergetic, with the minimum barrier becoming zero, and beyond this, the SE1 reaction is more favorable. Finally, at 813 K, the self-limiting reaction becomes endergonic and continuous etching dominates. We see similar trends for ZrO2, with self-limiting reactions preferred up to 533 K, while at 770 K, the self-limiting reaction becomes endergonic and continuous etching remains exergonic.

In Figure 5, the FEP is computed using the 8O/16F model as the SL product state. For completeness, we also determine the FEPs for two other SL product models, namely, 12O/24F and 16O/32F. Both surfaces of HfO2 and ZrO2 have 16 topmost O atoms (oxygen) in the supercell that could react with the HF molecules. For the 12O/24F product state, threefourths of surface O are removed and 24 F ( /uniFB02 uorine) are

Figure 5. Free energy pro /uniFB01 les for the SE1 (blue) and SL1 (orange) reactions of (a) HfO 2 and (b) ZrO2 from 0 to 1000 K at the pressures given in the text. T 1 is where the self-limiting and spontaneous etch reactions cross over for the 8O/16F model, and T 2 is where spontaneous etching is preferred.

<!-- image -->

<!-- image -->

added to replace them. For the 16O/32F, all surface O are removed and 32 F are added to replace them. All oxygen atoms were removed as H2O molecules. Basically, the M -O(M=Hf, Zr) coordination numbers of the surface metal atoms are decreasing from 8O/16F to 16O/32F. Note that the more O atoms are removed, the easier it would be to remove the surface metal atoms in the second pulse due to the reduced metal -O interaction. Therefore, we use the 12O/24F and 16O/32F product states merely as extreme test cases to compare their thermodynamic stability with the more reasonable 8O/16F model. The geometries used for the SL thermochemical calculations of both metal oxides are shown in Section S1 of the Supporting Information. Table 2 shows the energetics for the SL reactions including 12O/24F and 16O/ 32F models.

At 0 K, all SL reactions are more favorable than the SE reaction for both oxides and the minimum barriers are positive. For both oxides, we /uniFB01 nd the minimum barrier to decrease with the number of surface O atoms removed, with the lowest barriers for ZrO2. At 500 K, the SL1 and SL2 reactions continue to be more favorable than the SE reaction, whereas the SL3 reaction is not. This means that an aggressive removal of surface O by HF during the /uniFB01 rst pulse would also enhance etching of the surface Hf/Zr atoms at ALE-relevant temperatures, say 500 K.

Experimental work showed that the HF reaction is selflimiting on HfO2 at 200 ° C (473 K), 9 250 ° C (523 K), 11 and 300 ° C (573 K). 11 Compared to Figure 6, this is true for partial surface O removal (8O/16F), where self-limiting is preferred up to 618 K for three-fourths of surface O removal

Table 2. Reaction (Free) Energies and Minimum Barriers within Parenthesis at 0 and 500 K for the Model SL Reactions Representing the HF Pulse on HfO2 and ZrO2 for 8O/16F, 12O/24F, and 16O/32F SL Product States (M = Hf, Zr)

|       | SL product state   | Δ E (0 K) (eV/M)   | Δ G (500 K) (eV/M)   |
|-------|--------------------|--------------------|----------------------|
| HfO 2 | HfO 2              | HfO 2              | HfO 2                |
| SE1   | HfF 4              | - 0.91             | - 0.65               |
| SL1   | 8O/16F             | - 3.27 (2.36)      | - 1.20 (0.55)        |
| SL2   | 12O/24F            | - 3.05 (2.14)      | - 1.04 (0.39)        |
| SL3   | 16O/32F            | - 2.45 (1.54)      | - 0.41 ( - 0.24)     |
| ZrO 2 | ZrO 2              | ZrO 2              | ZrO 2                |
| SE1   | ZrF 4              | - 1.14             | - 0.89               |
| SL1   | 8O/16F             | - 3.04 (1.90)      | - 1.00 (0.11)        |
| SL2   | 12O/24F            | - 2.91 (1.77)      | - 0.90 (0.01)        |
| SL3   | 16O/32F            | - 2.17 (1.03)      | - 0.11 ( - 0.78)     |

Figure 6. Free energy pro /uniFB01 les of the continuous etching and selflimiting reactions for HfO . 2 T 1 , T 2 , and T 3 are where the self-limiting and spontaneous etch reactions cross over for 16O/32F, 12O/24F, and 8O/16F models, respectively.

<!-- image -->

and up to 657 K for one half of surface O removal. The same analysis holds for ZrO 2 (Figure 7). Therefore, N -E analysis is

Figure 7. Free energy pro /uniFB01 les of the continuous etching and selflimiting reactions for ZrO . 2 T 1 , T 2 , and T 3 are where the self-limiting and spontaneous etch reactions cross over for 16O/32F, 12O/24F, and 8O/16F models, respectively.

<!-- image -->

a simple and relatively inexpensive method to predict the structure of the surface after the /uniFB01 rst ALE pulse. We will further validate this methodology on experimental results for di /uniFB00 erent ALE processes in a future publication.

Adsorption of One HF Molecule at HfO2 and ZrO2. Kondati Natarajan and Elliott 39 studied the adsorption of HF on the bare surface of Al O 2 3 and found that Al -F bonding is

Figure 8. Relaxed adsorption structures for one HF molecule interacting with the bare surfaces of HfO 2 and ZrO2. The color coding is yellow = Hf, green = Zr, red = O, white = H, and blue = F.

<!-- image -->

crucial for HF dissociation. To /uniFB01 nd whether the same holds for HfO2 and ZrO2, we adsorb one HF molecule to the optimized bare surfaces of both oxides at di /uniFB00 erent binding sites (which we term A, B, and C). These sites were chosen to test whether molecular or dissociative adsorption of HF is sensitive to the adsorption site. The di /uniFB00 erent binding sites for one HF are shown in Section S2 of the Supporting Information.

Table 3. Adsorbate Coverages and Binding Energies for the HF Coverages on the HfO2 Surface Shown in Figure 9 and in Section S4 of the Supporting Information a

Figure 8 shows that the HF molecule is spontaneously dissociated at each binding site to form metal -F and O -H bonds on both oxides. No molecular HF adsorption was found. Similar to the Al2 O3 case, we /uniFB01 nd that the HF dissociation proceeds after a stable M -F (M = Hf, Zr) bond is formed. The computed adsorption energies for the dissociative adsorption of one HF molecule on the bare surface of HfO2 are -1.52, -1.95, and -1.63 eV at sites A, B, and C, respectively. The corresponding values for ZrO2 are -1.25, -1.74, and -1.48 eV. The interaction between HfO2 and HF is 0.15 -0.21 eV stronger than between ZrO2 and HF. The Hf -F, Zr -F, and O H bond lengths are shown for each adsorption mode in -Figure 8. The surface O atoms are either 2-fold or 3-fold coordinated by surface Hf/Zr atoms on both surfaces. All of the surface Hf/Zr atoms are 6-fold coordinated by O atoms. Since the structures of HfO2 and ZrO2 are similar, the strongest adsorption mode (one HF B for HfO2 -1.95 eV and for ZrO2 -1.74 eV) involves the same 6-fold coordinated metal lattice site and 2-fold coordinated surface oxygen site.

Stability of Di /uniFB00 erent HF Coverages. The stability of di /uniFB00 erent HF coverages was examined by introducing up to 34 randomly oriented HF molecules per supercell ca. 3 Å from the bare monoclinic (111) surface of HfO2 and ZrO2; this results in coverages ranging from 1.0 ± 0.3 to 17.0 ± 0.3 HF/nm 2 (2 HF to 34 HF molecules per supercell). There are 16 topmost metal atoms on the surface of the (2 × 2) supercell that may form metal -F bonds on both oxides. There are also 16 surface oxygen atoms on the bare surface of each metal oxide that can form O -H bonds or, as seen in some simulations, H O, which 2 we discuss later. For each metal oxide, three di /uniFB00 erent con /uniFB01 gurations (A, B, and C) were examined for the range of HF coverages using 2, 3, 4, 5, and 8 molecules per supercell and two con /uniFB01 gurations (A and B) using 12 and 16 molecules per supercell and one con /uniFB01 guration for 30, 32, and 34 molecules per supercell. The computed energies of adsorption for the above-mentioned geometries are shown in Tables 3 and

| HfO 2          | coverage              | coverage                          | E bind   | E bind   |
|----------------|-----------------------|-----------------------------------|----------|----------|
| geometry       | adsorbed HF (nm - 2 ) | (Hf - F, dissociated F) (nm - 2 ) | eV/HF    | eV/nm 2  |
| 2HF A (2, 2)   | 1.0                   | (1.0, 1.0)                        | - 1.5    | - 1.5    |
| 2HF B (1, 1)   | 1.0                   | (0.5, 0.5)                        | - 0.8    | - 0.8    |
| 2HF C (1, 1)   | 1.0                   | (0.5, 0.5)                        | - 1.0    | - 1.0    |
| 3HF A (2, 2)   | 1.5                   | (1.0, 1.0)                        | - 1.1    | - 1.7    |
| 3HF B (2, 2)   | 1.5                   | (1.0, 1.0)                        | - 1.1    | - 1.6    |
| 3HF C (3, 3)   | 1.5                   | (1.5, 1.5)                        | - 1.7    | - 2.6    |
| 4HF A (3, 3)   | 2.0                   | (1.5, 1.5)                        | - 1.3    | - 2.6    |
| 4HF B (3, 3)   | 2.0                   | (1.5, 1.5)                        | - 1.3    | - 2.7    |
| 4HF C (4, 4)   | 2.0                   | (2.0, 2.0)                        | - 1.6    | - 3.2    |
| 5HF A (5, 5)   | 2.5                   | (2.5, 2.5)                        | - 1.8    | - 4.6    |
| 5HF B (4, 4)   | 2.5                   | (2.0, 2.0)                        | - 1.4    | - 3.4    |
| 5HF C (5, 5)   | 2.5                   | (2.5, 2.5)                        | - 1.5    | - 3.7    |
| 8HF A (5, 4)   | 4.0                   | (2.5, 2.0)                        | - 1.1    | - 4.6    |
| 8HF B (6, 6)   | 4.0                   | (3.0, 3.0)                        | - 1.3    | - 5.2    |
| 8HF C (6, 5)   | 4.0                   | (3.0, 2.5)                        | - 1.1    | - 4.4    |
| 12HF A (10, 7) | 6.0                   | (5.0, 3.5)                        | - 1.3    | - 7.7    |
| 12HF B (10, 7) | 6.0                   | (5.0, 3.5)                        | - 1.2    | - 7.3    |
| 16HF A (12, 8) | 8.0                   | (6.0, 4.0)                        | - 1.1    | - 9.0    |
| 16HF B (13, 9) | 8.0                   | (6.5, 4.5)                        | - 1.2    | - 9.6    |
| 30HF (12, 7)   | 15.0                  | (6.0, 3.5)                        | - 0.8    | - 11.8   |
| 32HF (12, 6)   | 16.0                  | (6.0, 3.0)                        | - 0.8    | - 12.1   |
| 34HF (14, 7)   | 17.0                  | (7.0, 3.5)                        | - 0.9    | - 12.9   |

a The /uniFB01 rst number in parenthesis within the /uniFB01 rst column corresponds to the total number of Hf -F bonds, and the second number corresponds to the number of dissociated HF molecules. The most stable con /uniFB01 gurations, when more than one con /uniFB01 guration is studied for a coverage, are highlighted in bold.

For HfO2, spontaneous complete dissociation of the adsorbed HF molecules was observed for some con /uniFB01 gurations with coverages of two, three, four, and /uniFB01 ve HF molecules, as shown in Figure 9. Similarly, for ZrO , complete dissociation of 2 adsorbed HF was seen for some con /uniFB01 gurations with coverages of two and four HF molecules only as shown in Figure 10. However, for the adsorption of three, /uniFB01 ve, and eight HF molecules on the ZrO2 surface, upon relaxation, there were two, four, and seven dissociated HF molecules present for each con /uniFB01 guration (A, B, or C); see Section S4 of the Supporting Information.

Table 4. Adsorbate Coverages and Binding Energies for the HF Coverages on the ZrO2 Surface Shown in Figure 10 and in Section S4 of the Supporting Information a

| ZrO 2          | coverage              | coverage                          | E bind   | E bind   |
|----------------|-----------------------|-----------------------------------|----------|----------|
| geometry       | adsorbed HF (nm - 2 ) | (Zr - F, dissociated F) (nm - 2 ) | eV/HF    | eV/nm 2  |
| 2HF A (1, 1)   | 1.0                   | (0.5, 0.5)                        | - 0.9    | - 0.9    |
| 2HF B (1, 1)   | 1.0                   | (0.5, 0.5)                        | - 1.0    | - 1.0    |
| 2HF C (2, 2)   | 1.0                   | (1.0, 1.0)                        | - 1.2    | - 1.2    |
| 3HF A (2, 2)   | 1.5                   | (1.0, 1.0)                        | - 1.0    | - 1.6    |
| 3HF B (3, 2)   | 1.5                   | (1.5, 1.0)                        | - 1.2    | - 1.9    |
| 3HF C (2, 2)   | 1.5                   | (1.0, 1.0)                        | - 0.8    | - 1.2    |
| 4HF A (4, 4)   | 2.0                   | (2.0, 2.0)                        | - 1.4    | - 2.6    |
| 4HF B (4, 4)   | 2.0                   | (2.0, 2.0)                        | - 1.5    | - 3.1    |
| 4HF C (3, 3)   | 2.0                   | (1.5, 1.5)                        | - 1.1    | - 2.2    |
| 5HF A (5, 4)   | 2.5                   | (2.5, 2.0)                        | - 1.3    | - 3.2    |
| 5HF B (4, 4)   | 2.5                   | (2.0, 2.0)                        | - 1.1    | - 2.8    |
| 5HF C (4, 4)   | 2.5                   | (2.0, 2.0)                        | - 1.3    | - 3.3    |
| 8HF A (7, 7)   | 4.0                   | (3.5, 3.5)                        | - 1.2    | - 5.0    |
| 8HF B (7, 7)   | 4.0                   | (3.5, 3.5)                        | - 1.3    | - 5.1    |
| 8HF C (7, 7)   | 4.0                   | (3.5, 3.5)                        | - 1.2    | - 4.9    |
| 12HF A (9, 6)  | 6.0                   | (4.5, 3.0)                        | - 1.0    | - 6.0    |
| 12HF B (9, 7)  | 6.0                   | (4.5, 3.5)                        | - 1.0    | - 6.3    |
| 16HF A (10, 8) | 8.0                   | (5.0, 4.0)                        | - 1.0    | - 7.9    |
| 16HF B (11, 7) | 8.0                   | (5.5, 3.5)                        | - 1.1    | - 8.6    |
| 30HF (13, 8)   | 15.0                  | (6.5, 4.0)                        | - 0.8    | - 11.5   |
| 32HF (12, 6)   | 16.0                  | (6.0, 3.0)                        | - 0.7    | - 11.5   |
| 34HF (13, 8)   | 17.0                  | (6.5, 4.0)                        | - 0.7    | - 12.3   |

a The /uniFB01 rst number in parenthesis within the /uniFB01 rst column corresponds to the total number of Zr -F bonds, and the second number corresponds to the number of dissociated HF molecules. The most stable con /uniFB01 gurations, when more than one con /uniFB01 guration is studied for a coverage, are highlighted in bold.

In all other HF adsorption con /uniFB01 gurations for HfO2 and ZrO2, we /uniFB01 nd a mixture of molecular and dissociative adsorption of the HF molecules. We have computed binding energies per HF and per unit surface area of the material as listed in Tables 3 and 4.

For both metal oxides, the binding energy is more favorable as the extent of metal -F bonding increases on the bare surface. This can be seen for HfO 2 in Table 3 and Figure 11c with Hf -F coverage from 1.0 ± 0.3 to 7.0 ± 0.3 nm -2 with surface binding energies -1.5 to -12.9 eV/nm . Similar trends are also 2

Plot (a) in Figures 11 and 12 show scatter plots for metal -F coverage versus adsorbed HF coverage from the data in Tables 3 and 4 for HfO2 and ZrO2, respectively. The dashed line shows a linear correlation between HF adsorption and metal -F coverage, which indicates the cases where all adsorbed HF molecules form metal -F bonds. The square data points along the dashed lines are those geometries where adsorbed HF coverage equals metal -F coverage. For HF adsorption at HfO2, this corresponds to the most stable con /uniFB01 gurations at coverages of 1.0, 1.5, 2.0, and 2.5 HF/nm 2 . For ZrO2, this corresponds to the most stable con /uniFB01 gurations at coverages of 1.0 and 2.0 HF/nm . Note that the data points of (2HF B and 2 2HF C), (3HF A and 3HF B), (4HF A and 4HF B), (5HF A and 5HF C), (8HF B and 8HF C), and (12HF A and 12HF B) overlap in Figure 11a as their adsorbed HF and Hf -F coverages are the same. Similarly, the data points of (2HF A and 2HF B), (3HF A and 3HF C), (4HF A and 4HF B), (5HF B and 5HF C), (8HF A and 8HF B and 8HF C), and (12HF A and 12HF B) overlap in Figure 12a. The points at higher HF coverages correspond to those geometries in which partially dissociated HF molecules are present, and hence, the points lie below the correlation line. As the HF coverage increases, the metal -F coverage starts to plateau, suggesting maximal coverages of (6.0 ± 0.3) -(7.0 ± 0.3) metal -F/nm 2 . Lee et al. 9 found that for low HF coverages during etching of HfO2 using HF and Sn(acac)2, there was a lack of self-limiting behavior as the HF reaction had not reached saturation. We

Figure 9. Relaxed geometries for HF coverages 2A, 3C, 4C, 5A, and 5C of HfO 2 where complete dissociation of HF occurred spontaneously. Color coding is the same as in Figure 8.

<!-- image -->

seen for ZrO2 in Table 4 and Figure 12c with Zr -F coverage from 1.0 ± 0.3 to 6.5 ± 0.3 nm -2 with surface binding energies -0.9 to -12.3 eV/nm 2 . The HF molecules that did not dissociate in the relaxed geometries shown in Section S4 of the Supporting Information form hydrogen bonds with the remaining HF molecules and dissociated F atoms. For higher HF coverages, a more extensive hydrogen-bonded HF network is expected. There are intact HF molecules forming M F -bonds as well (M = Hf, Zr), whose coverage is found by subtracting the two numbers within parenthesis in Tables 3 and 4. These metal-bound HF molecules (M -FH) are not likely to be purged away in the next ALE step as they form strong bonds (Hf -F 6.7 eV and Zr -F 6.5 eV), 49 and these HF molecules should likely dissociate when the kinetic barriers are overcome inside the reactor. Therefore, we will use the total number of M -F bonds for the etch rate prediction in a later section.

<!-- image -->

Figure 10. Relaxed geometries for HF coverages 2C, 4A, and 4B of ZrO2 where complete dissociation of HF occurred spontaneously. Color coding is the same as in Figure 8.

<!-- image -->

Figure 11. (a) Scatter plot for Hf -F coverage versus total HF coverage for the surface coverage values in Table 3. Note that some HF coverages resulted in partial or complete Hf -F coverage for di /uniFB00 erent con /uniFB01 gurations, for example, the coverage of 1.0 HF/nm . The square data points are 2 where the adsorbed HF coverage equals Hf -F coverage. The circular data points are where partially dissociated HF molecules are present. Plots (b) and (c) show the change in binding energy per square nanometer with an increase in HF and Hf -F coverage, respectively.

Figure 12. (a) Scatter plot for Zr -F coverage versus total HF coverage for the surface coverage values in Table 4. Note that some HF coverages resulted in partial or complete Zr -F coverage for di /uniFB00 erent con /uniFB01 gurations, for example, the coverage of 1.0 HF/nm . The square data points are 2 where the adsorbed HF coverage equals Zr -F coverage. The circular data points are where partially dissociated HF molecules are present. Plots (b) and (c) show the change in binding energy per square nanometer with an increase in HF and Zr -F coverage, respectively.

<!-- image -->

Figure 13. Relaxed /uniFB02 uorination geometries for HfO2 that resulted in H O forming spontaneously. Color coding is the same as in Figure 8. 2

<!-- image -->

<!-- image -->

also /uniFB01 nd from plots (b) and (c) of Figures 11 and 12 that a saturation in the binding energy is not reached even at high HF coverages. Therefore, the highest adsorbed HF coverage of 34 HF with M -F coverages (M = Hf, Zr) of 7.0 ± 0.3 and 6.5 ± 0.3 metal -F/nm 2 will be used as the maximum coverage for the HfO2 and ZrO2 etch rate prediction, respectively. We added an exponential /uniFB01 t to the data in plot (b) of Figures 11

and 12 in Section S6 of SI along with its derivative, which provides HF addition energy indirectly.

Water Formation. The spontaneous formation of H2O was observed in some of our relaxed geometries for the examples of 8C (3.0 ± 0.3 Hf -F/nm 2 ) on HfO2 and 16A (5.0 ± 0.3 Zr -F/nm 2 ) on ZrO2. The atomic structures are shown in Figure 13, where dissociation of at least two HF molecules provides the hydrogen atoms required to form H2O as a

<!-- image -->

Figure 14. Relaxed /uniFB02 uorination geometries for ZrO 2 that resulted in H O forming spontaneously. Color coding is the same as in Figure 8. 2

<!-- image -->

reaction product, which removes oxygen from HfO2, as discussed in ref 9, but not discussed to date for ZrO2. H2O formation on the HfO2 surface was observed on geometries 8HF C and 32HF, in which the H -O Hbond angle is 104.2 . -° Similarly, H O formation on the ZrO 2 2 surface was observed on geometries 12HF B and 16HF A HF as shown in Figure 14. The H -O H bond angle is 110.2 -° for 12HF B, and for 16HF A, it is 109.4 and 110.8 . °

The energy to remove H2O (energy of desorption) from the /uniFB02 uorinated surfaces of 8HF C and 32HF for HfO2 and 12HF B and 16HF A for ZrO2 was calculated using eq 9

$$E _ { \text{des} } = ( E _ { \text{HfO} _ { 2 ( \text{surf} ) } / \text{HF} _ { ( \text{ads} ) } } + E _ { \text{H} _ { 2 } O _ { ( \text{s} ) } } ) - ( E _ { \text{HfO} _ { 2 ( \text{surf} ) } / \text{HF} _ { ( \text{ads} ) } / \text{H} _ { 2 } O _ { ( \text{ads} ) } } ) \quad \text{adso} \\ ( 9 ) \quad \text{and}$$

The term ' E HfO2(surf) /HF(ads)/H2O(ads) ' is the total energy of HF adsorbed on HfO2 with spontaneous H2O formation. H2O was removed from the /uniFB02 uorinated metal oxide surface with unbound HF molecules, and the resulting geometry was relaxed. The term ' E HfO2(surf) /HF(ads) ' is the total energy of HF adsorbed on HfO2 after removing H2O from the surface, and ' E H2O(g) ' is the energy of a gas-phase H2O molecule. The desorption energies of H2O are presented in Table 5. These energies are relatively low and can be achievable at process conditions to remove surface-bound H2O.

oxy /uniFB02 uoride. The self-limiting nature of the /uniFB02 uorination reaction is due to the formation of a passivated layer during HF exposure. 26 The HfFx layer formed on HfO2 after /uniFB02 uorination is self-limiting because this surface layer forms a di /uniFB00 usion barrier to subsequent /uniFB02 uorination by HF. 11 Multiple coverages of HF molecules starting from 1.0 ± 0.3 to 17.0 ± 0.3 HF/nm 2 resulted in mixed dissociated and molecular adsorption of HF to the surfaces of HfO 2 and ZrO2. We found maximal coverages of (6.0 ± 0.3) -(7.0 ± 0.3) metal -F/nm 2 at higher HF coverages. Water forms spontaneously on relaxation from some of the geometries for multiple HF adsorption for both HfO2 and ZrO2. The computed desorption energies to remove H2 O from our /uniFB02 uorinated surfaces of HfO 2 and ZrO2 are low enough to be overcome at process conditions.

Table 5. List of Con /uniFB01 gurations That Resulted in Barrierless H2O Formation and the Energy Required to Remove H2O from Their Surface

| con /uniFB01 guration   | no. H 2 O formed   | E (des) (eV/H 2 O)   |
|-------------------------|--------------------|----------------------|
|                         | HfO 2              |                      |
| 8C HF                   | 1                  | 0.70                 |
| 32 HF                   | 2                  | 1.32                 |
|                         | ZrO 2              |                      |
| 12B HF                  | 1                  | 1.30                 |
| 16A HF                  | 2                  | 0.50                 |

## ■ DISCUSSION

From the N -E analysis, at all T &lt; 500 K using reactant and product pressures of 0.2 and 0.01 Torr, respectively, and an 8O/16F surface model as the SL product state, the HF pulse on HfO2 and ZrO2 is self-limiting in nature, as the reaction energies for the self-limiting reactions were more favorable than the spontaneous etching reactions. Therefore, we suggest that the /uniFB01 rst precursor pulse using HF, at these conditions, will produce a stable and nonvolatile layer of metal /uniFB02 uorides and H2O as byproducts. We also found that at elevated temperatures, the formation of the volatile metal /uniFB02 uoride is more favorable than the formation of the volatile metal

For both HfO2 and ZrO2, the surfaces with an initial coverage of 17.0 ± 0.3 HF/nm 2 that resulted in 7.0 ± 0.3 Hf -F/nm 2 and 6.5 ± 0.3 Zr -F/nm 2 , respectively, are used to calculate a theoretical etch rate. Both (2 × 2) supercells of monoclinic (111) HfO2 and ZrO2 have surface areas of 1.98 nm 2 with 16 metal atoms on the surface that can form metal -F bonds that correspond to coverages of 8.0 ± 0.3 Hf/nm 2 and 8.0 ± 0.3 Zr/nm , respectively. As the maximum coverage of 2 Hf -F is 7.0 ± 0.3 F/nm , there will be approximately 0.88 F 2 atoms per surface Hf. The maximum coverage of Zr -F is 6.5 ± 0.3 F/nm 2 , so there will be approximately 0.81 F atoms per surface Zr. The SE1 reactions showed that four F atoms lead to the etching of one Hf/Zr atom as volatile metal tetra /uniFB02 uoride. Similar to the analysis done by Kondati Natarajan et al., 39 the coverage of Hf/Zr that can be etched is one-quarter of the M -F coverage (M = Hf, Zr), 1.8 ± 0.1 Hf/(nm 2 cycle) for HfO2 and 1.6 ± 0.1 Zr/(nm 2 cycle) for ZrO2. As the surface concentration of metal atoms is 8.0 ± 0.3 Hf or Zr/nm , this 2 etch rate corresponds to 0.2 monolayer/cycle. For HfO , this 2 corresponds to -61.2 ± 0.8 ng/(cm 2 cycle) and using the mass density of bulk HfO 2 (10.0 g/cm ), 3 -0.61 ± 0.02 Å/cycle. For ZrO2, this corresponds to -33.3 ± 0.8 ng/(cm 2 cycle) and using the mass density of bulk ZrO 2 (5.9 g/cm ), 3 -0.57 ± 0.02 Å/cycle. It is important to note that these computed etch rates do not take into account kinetic e /uniFB00 ects that would be included in experimental etch rates. Therefore, we also compute the maximum etch rate for the removal of a complete monolayer of material from HfO2 and ZrO2. We used 16 metal atoms for one ML removal, which requires a Hf -F/Zr -F coverage of 32.32 ± 0.3 F/nm . An etch rate of 2 -2.82 ± 0.02 Å/cycle was computed for one ML removal using the same method for calculating the theoretical etch rate. Therefore, if the etch rate is greater than -2.82 ± 0.02 Å/cycle, then it suggests that subsurface metal atoms are being etched.

A summary of experimental etch rates for HfO2 and ZrO2 using HF and a metal precursor is shown in Section S5 of the

Figure 15. Experimental etch rates for the thermal ALE of HfO2 and ZrO2 using precursors HF and Sn(acac)2, 4,9 Al(CH3)3, 4 AlCl(CH3)2, 4,12 SiCl , 4 4 and TiCl4. 1111 (a) Etch rates for the thermal ALE of HfO 2 using HF and Sn(acac)2 for the temperature range of 150 -250 ° C. (b) Etch rates for the thermal ALE of HfO2 and ZrO2 using HF and Sn(acac)2/AlCl(CH3)2/Al(CH3)3/SiCl4 at the temperatures shown. (c) Etch rates for the thermal ALE using HF and TiCl4 of HfO2 for the temperature range 200 -300 ° C and ZrO2 at 250 ° C. (d) Etch rates for the thermal ALE of HfO 2 and ZrO2 using HF and AlCl(CH3)2 for the temperature range 200 -300 ° C.

<!-- image -->

Supporting Information and also in Figure 15. The /uniFB01 rst thing we observe is that for a speci /uniFB01 c reactant combination, the etch rate increases with temperature for both materials and the etch rate for ZrO2 is larger than that of HfO2. We have predicted this from N E -analysis that the minimum barrier to continuous etching decreases considerably with an increase in temperature, more so in the case of ZrO 2 when compared to HfO2. Between 150 and 350 ° C, for di /uniFB00 erent reactant combinations, the etch rates can be anywhere between 0.05 and 1.24 Å/cycle for HfO2 and between 0.01 and 1.59 Å/cycle for ZrO2. The computed etch rate prediction given earlier based on the maximal M -F coverage (M = Hf, Zr) should be taken carefully as the experimental etch rate varies greatly with temperature and the reactant, in the second pulse. Moreover, the maximal experimental etch rate reported is much larger than the predicted etch rate, suggesting that further reaction of adsorbed HF with the substrate is possible and this reaction surmounts the kinetic barriers, which we have not included in this simple adsorption study. However, comparing the maximal etch rate of -2.82 ± 0.02 Å/cycle for one ML removal of Hf/ ZrO2 along with experimental etch rates, we can calculate the number of Hf/Zr removed/nm 2 in those experiments. Our surface model contains 8.0 ± 0.3 M/nm 2 (M = Hf, Zr) as mentioned earlier. Therefore, an etch rate of -2.82 ± 0.02 Å/ cycle corresponds to a removal of 8.0 ± 0.3 M/nm 2 of the surface. Thus no. of metal atoms removed/nm 2

$$\dots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \\ = \exp t. \ e t c h r a t e \times \left ( - \frac { 8. 0 } { 2. 8 } \pm 0. 1 \right ) \quad & \text{from} \\ ( 1 0 ) \quad & - 2. \cdot \\ \text{For example, 4.5} \pm 0. 1 \, Z r \, \text{atoms/nm} ^ { 2 } \, \text{are removed as volatile} \quad \text{to} \ \, \mathfrak { c } \\ - \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \cdot \,.$$

For example, 4.5 ± 0.1 Zr atoms/nm 2 are removed as volatile ZrF4 per cycle for an experimental etch rate of 1.59 Å/cycle using HF and DMAC at 300 ° C. These results are also listed in Section S5 of the Supporting Information. It is clear that in all of these experiments, less than a monolayer of material is removed per ALE cycle. This computational approach detailed in this paper provides a general guideline to safely examine the in /uniFB02 uence of any reactant species on the substrate materials of interest.

## ■ CONCLUSIONS

We present DFT calculations to understand the nature of the HF pulse on the bare surfaces of monoclinic HfO2 and ZrO2 for thermal ALE. N E -analysis of the self-limiting and spontaneous (continuous) etching using simple reaction models representing the HF exposure on HfO2 and ZrO2 allowed us to predict whether SL or SE reaction is favorable at a given temperature and at a given pressure. At T &lt; 500 K, the HF reaction with both oxides is found to be in the preferred self-limiting state. This is a relatively inexpensive way to screen the reactant molecules for ALE, also equally applicable to ALD, of any given substrate. We studied the adsorption of HF molecules on HfO2 and ZrO2 for HF coverages ranging from 1.0 ± 0.3 to 17.0 ± 0.3 HF/nm 2 along with analysis of H O 2 formation. From this analysis, we predict a theoretical etch rate based on the maximum possible coverage of surface-bound HF for HfO2 and ZrO2. The maximal computed metal -F coverage on both surfaces is from 6.0 ± 0.3 to 7.0 ± 0.3 metal -F/nm 2 . The spontaneous formation of water was also seen at some HF coverages on both oxides. We calculated theoretical etch rates of -0.61 ± 0.02 Å/cycle for HfO2 and -0.57 ± 0.02 Å/cycle for ZrO2, which are lower than the maximal etch rates reported from experiments. The etch rate for a complete ML removal, -2.82 ± 0.02 Å/cycle, was used with experimental etch rates to compute the number of metal atoms removed from the surface per square nanometer per cycle. We can use the presented methodology for the /uniFB01 rst pulse on HfO2 and ZrO2 to examine other reagents such as HCl and HBr with a similar analysis as well as examine the interaction of HF on hydroxylterminated surfaces of HfO2 and ZrO2.

## ■ ASSOCIATED CONTENT

## * s ı Supporting Information

The Supporting Information is available free of charge at https://pubs.acs.org/doi/10.1021/acs.chemmater.9b05021.

Self-limiting surface models used for thermochemical analysis, binding sites of one HF molecule at HfO 2 and ZrO2 in HF adsorption studies, summary of bond dissociation energies, mixed molecular and dissociative adsorption of HF molecules from HF adsorption studies, experimental etch rates of HfO2 and ZrO2 with the corresponding number of metal atoms removed per square nanometer, and addition energy from increasing HF coverages (PDF)

## ■ AUTHOR INFORMATION

## Corresponding Author

Michael Nolan -Tyndall National Institute, University College Cork, Cork T12 R5CP, Ireland; orcid.org/0000-00025224-8580; Email: michael.nolan@tyndall.ie

## Authors

Rita Mullins -Tyndall National Institute, University College Cork, Cork T12 R5CP, Ireland; orcid.org/0000-00023898-7328

- Simon D. Elliott -Schrodinger Inc., New York, New York ̈ 10036-4041, United States; orcid.org/0000-0001-55735694
- Suresh Kondati Natarajan -Tyndall National Institute, University College Cork, Cork T12 R5CP, Ireland; Department of Electrical Engineering and Automation, Aalto University, Espoo 02150, Finland; orcid.org/0000-0002-7018-5253

Complete contact information is available at:

https://pubs.acs.org/10.1021/acs.chemmater.9b05021

## Author Contributions

R.M. and S.K.N. contributed equally to this manuscript.

## Notes

The authors declare no competing /uniFB01 nancial interest.

∥

## ■ ACKNOWLEDGMENTS

We acknowledge support for this work from LAM Research and the Science Foundation Ireland  NSF China Partnership Program, NITRALD Grant number: 17/NSFC/5279. We are grateful for access to Tyndall computing facilities supported by SFI and the Irish Centre for High-End Computing, www.ichec. ie.

## ■ REFERENCES

- (1) Raghu, P.; Yim, C.; Shadman, F.; Shero, E. Susceptibility of SiO , 2 ZrO2, and HfO2 dielectrics to moisture contamination. AIChE J. 2004 , 50 , 1881 -1888.
- (2) Raghu, P.; Rana, N.; Yim, C.; Shero, E.; Shadman, F. Adsorption of Moisture and Organic Contaminants on Hafnium Oxide, Zirconium Oxide, and Silicon Oxide Gate Dielectrics. J. Electrochem. Soc. 2003 , 150 , No. F186.
- (3) Hausmann, D. M.; Kim, E.; Becker, J.; Gordon, R. G. Atomic Layer Deposition of Hafnium and Zirconium Oxides Using Metal Amide Precursors. Chem. Mater. 2002 , 14 , 4350 -4358.
- (4) Lee, Y.; Huffman, C.; George, S. M. Selectivity in Thermal Atomic Layer Etching Using Sequential, Self Limiting Fluorination and Ligand-Exchange Reactions. Chem. Mater. 2016 , 28 , 7657 -7665.
- (5) Oehrlein, G. S.; Metzler, D.; Li, C. Atomic Layer Etching at the Tipping Point: An Overview. ECS J. Solid State Sci. Technol. 2015 , 4 , N5041.
- (6) Kanarik, K. J.; Lill, T.; Hudson, E. A.; Sriraman, S.; Tan, S.; Marks, J.; Vahedi, V.; Gottscho, R. A. Overview of atomic layer etching in the semiconductor industry. J. Vac. Sci. Technol., A 2015 , 33 , No. 020802.
- (7) George, S. M.; Lee, Y. Prospects for Thermal Atomic Layer Etching Using Sequential, Self-Limiting Fluorination and LigandExchange Reactions. ACS Nano 2016 , 10 , 4889 -4894.
- (8) Yuan, G.; Wang, N.; Huang, S.; Liu, J. In A Brief Overview of Atomic Layer Deposition and Etching in the Semiconductor Processing , 2016 17th International Conference on Electronic Packaging Technology (ICEPT), 2016; pp 1365 -1368.
- (9) Lee, Y.; DuMont, J. W.; George, S. M. Atomic Layer Etching of HfO2 Using Sequential, Self-Limiting Thermal Reactions with Sn(acac)2 and HF. ECS J. Solid State Sci. Technol. 2015 , 4 , N5013.
- (10) Lee, Y.; George, S. M. Atomic Layer Etching of Al2O3 Using Sequential, Self-Limiting Thermal Reactions with Sn(acac)2 and Hydrogen Fluoride. ACS Nano 2015 , 9 , 2061 -2070.
- (11) Lee, Y.; George, S. M. Thermal atomic layer etching of HfO2 using HF for fluorination and TiCl 4 for ligand-exchange. J. Vac. Sci. Technol., A 2018 , 36 , No. 061504.
- (12) Lee, Y.; George, S. M. Thermal Atomic Layer Etching of Al O , 2 3 HfO2, and ZrO2 Using Sequential Hydrogen Fluoride and Dimethylaluminum Chloride Exposures. J. Phys. Chem. C 2019 , 123 , 18455 -18466.
- (13) DuMont, J. W.; Marquardt, A. E.; Cano, A. M.; George, S. M. Thermal Atomic Layer Etching of SiO2 by a Conversion-etch Mechanism Using Sequential Reactions of Trimethylaluminum and Hydrogen Fluoride. ACS Appl. Mater. Interfaces 2017 , 9 , 10296 -10307.
- (14) Lee, Y.; DuMont, J. W.; George, S. M. Mechanism of Thermal Al2 O3 Atomic Layer Etching Using Sequential Reactions with Sn(acac)2 and HF. Chem. Mater. 2015 , 27 , 3648.
- (15) Lee, Y.; George, S. M. Atomic Layer Etching of Al2O3 Using Sequential, Self-Limiting Thermal Reactions with Sn(acac)2 and Hydrogen Fluoride. ACS Nano 2015 , 9 , 2061 -2070.
- (16) Lee, Y.; DuMont, J. W.; George, S. M. Trimethylaluminum as the Metal Precursor for the Atomic Layer Etching of Al2O3 Using Sequential, Self-Limiting Thermal Reactions. Chem. Mater. 2016 , 28 , 2994.
- (17) Hennessy, J.; Moore, C. S.; Balasubramanian, K.; Jewell, A. D.; France, K.; Nikzad, S. Enhanced atomic layer etching of native aluminum oxide for ultraviolet optical applications. J. Vac. Sci. Technol., A 2017 , 35 , No. 041512.
- (18) DuMont, J. W.; George, S. M. Competition between Al2O3 atomic layer etching and AlF 3 atomic layer deposition using sequential exposures of trimethylaluminum and hydrogen fluoride. J. Chem. Phys. 2017 , 146 , No. 052819.
- (19) Johnson, N. R.; Sun, H.; Sharma, K.; George, S. M. Thermal atomic layer etching of crystalline aluminum nitride using sequential, self-limiting hydrogen fluoride and Sn(acac) 2 reactions and enhancement by H2 and Ar plasmas. J. Vac. Sci. Technol., A 2016 , 34 , No. 050603.
- (20) Lee, Y.; DuMont, J. W.; George, S. M. Atomic Layer Etching of AlF3 Using Sequential, Self-Limiting Thermal Reactions with Sn(acac)2 and Hydrogen Fluoride. J. Phys. Chem. C 2015 , 119 , 25385 -25393.
- (21) Lemaire, P. C.; Parsons, G. N. Thermal Selective Vapor Etching of TiO2: Chemical Vapor Etching via WF6 and Self-Limiting Atomic Layer Etching Using WF6 and BCl3. Chem. Mater. 2017 , 29 , 6653 -6665.
- (22) Lee, Y.; George, S. M. Thermal Atomic Layer Etching of Titanium Nitride Using Sequential, Self-Limiting Reactions: Oxidation to TiO2 and Fluorination to Volatile TiF . 4 Chem. Mater. 2017 , 29 , 8202 -8210.
- (23) Shinoda, K.; Miyoshi, N.; Kobayashi, H.; Izawa, M.; Ishikawa, K.; Hori, M. Rapid thermal-cyclic atomic-layer etching of titanium

nitride in CHF3 /O2 downstream plasma. J. Phys. D: Appl. Phys. 2019 , 52 , No. 475106.

- (24) Xie, W.; Lemaire, P. C.; Parsons, G. N. Thermally Driven SelfLimiting Atomic Layer Etching of Metallic Tungsten Using WF6 and O2. ACS Appl. Mater. Interfaces 2018 , 10 , 9147 -9154.
- (25) Johnson, N. R.; George, S. M. WO3 and W Thermal Atomic Layer Etching Using Conversion-Fluorination and OxidationConversion-Fluorination Mechanisms. ACS Appl. Mater. Interfaces 2017 , 9 , 34435 -34447.
- (26) Zywotko, D. R.; George, S. M. Thermal Atomic Layer Etching of ZnO by a Conversion-Etch Mechanism Using Sequential Exposures of Hydrogen Fluoride and Trimethylaluminum. Chem. Mater. 2017 , 29 , 1183 -1191.
- (27) Johnson, N. R.; Hite, J. K.; Mastro, M. A.; Eddy, C. R.; George, S. M. Thermal atomic layer etching of crystalline GaN using sequential exposures of XeF 2 and BCl3. Appl. Phys. Lett. 2019 , 114 , No. 243103.
- (28) Lim, W. S.; Park, J. B.; Park, J. Y.; Park, B. J.; Yeom, G. Y. Low damage atomic layer etching of ZrO 2 by using BCl3 gas and ar neutral beam. J. Nanosci. 2009 , 9 , 7379 -7382.
- (29) Dallorto, S.; Goodyear, A.; Cooke, M.; Szornel, J. E.; Ward, C.; Kastl, C.; Schwartzberg, A.; Rangelow, I. W.; Cabrini, S. Atomic layer etching of SiO 2 with Ar and CHF3 plasmas: A self-limiting process for aspect ratio independent etching. Plasma Process Polym. 2019 , 16 , No. 1900051.
- (30) Koh, K.; Kim, Y.; Kim, C.-K.; Chae, H. Quasi atomic layer etching of SiO 2 using plasma fluorination for surface cleaning. J. Vac. Sci. Technol., A 2018 , 36 , No. 01B106.
- (31) Mameli, A.; Verheijen, M. A.; Mackus, A. J. M.; Kessels, W. M. M.; Roozeboom, F. Isotropic Atomic Layer Etching of ZnO Using Acetylacetone and O2 Plasma. ACS Appl. Mater. Interfaces 2018 , 10 , 38588 -38595.
- (32) Ohba, T.; Yang, W.; Tan, S.; Kanarik, K.; Nojiri, K. Atomic layer etching of GaN and AlGaN using directional plasma-enhanced approach. Jpn. J. Appl. Phys. 2017 , 56 , No. 06HB06.
- (33) Kauppinen, C.; Khan, S. A.; Sundqvist, J.; Suyatin, D. B.; Suihkonen, S.; Kauppinen, E. I.; Sopanen, M. Atomic layer etching of gallium nitride (0001). J. Vac. Sci. Technol., A 2017 , 35 , No. 060603. (34) Miyoshi, N.; Kobayashi, H.; Shinoda, K.; Kurihara, M.; Watanabe, T.; Kouzuma, Y.; Yokogawa, K.; Sakai, S.; Izawa, M. Atomic layer etching of silicon nitride using infrared annealing for short desorption time of ammonium fluorosilicate. Jpn. J. Appl. Phys. 2017 , 56 , No. 06HB01.
- (35) Lu, W.; Lee, Y.; Gertsch, J. C.; Murdzek, J. A.; Cavanagh, A. S.; Kong, L.; del Alamo, J. A.; George, S. M. In Situ Thermal Atomic Layer Etching for Sub-5 nm InGaAs Multigate MOSFETs. Nano Lett. 2019 , 19 , 5159 -5166.
- (36) Gertsch, J. C.; Cano, A. M.; Bright, V. M.; George, S. M. SF 4 as the Fluorination Reactant for Al O 2 3 and VO2 Thermal Atomic Layer Etching. Chem. Mater. 2019 , 31 , 3624 -3635.
- (37) Rahman, R.; Mattson, E. C.; Klesko, J. P.; Dangerfield, A.; Rivillon-Amy, S.; Smith, D. C.; Hausmann, D.; Chabal, Y. J. Thermal Atomic Layer Etching of Silica and Alumina Thin Films Using Trimethylaluminum with Hydrogen Fluoride or Fluoroform. ACS Appl. Mater. Interfaces 2018 , 10 , 31784 -31794.
- (38) Fang, C.; Cao, Y.; Wu, D.; Li, A. Thermal atomic layer etching: Mechanism, materials and prospects. Prog. Nat. Sci.: Mater. Int. 2018 , 28 , 667 -675.
- (39) Kondati Natarajan, S.; Elliott, S. D. Modeling the Chemical Mechanism of the Thermal Atomic Layer Etch of Aluminum Oxide: A Density Functional Theory Study of Reactions during HF Exposure. Chem. Mater. 2018 , 30 , 5912 -5922.
- (40) Kresse, G.; Furthmuller, J. Efficient iterative schemes for ab initio total-energy calculations using a plane-wave basis set. Phys. Rev. B 1996 , 54 , 11169.
- (41) Perdew, J. P.; Burke, K.; Ernzerhof, M. Generalized gradient approximation made simple. Phys. Rev. Lett. 1996 , 77 , 3865.
- (42) Kresse, G.; Joubert, D. From ultrasoft pseudopotentials to the projector augmented-wave method. Phys. Rev. B 1999 , 59 , 1758.
- (43) Lowther, J. E.; Dewhurst, J. K.; Leger, J. M.; Haines, J. Relative stability of ZrO2 and HfO2 structural phases. Phys. Rev. B 1999 , 60 , 14485 -14488.
- (44) Zhao, X.; Vanderbilt, D. First-principles study of structural, vibrational, and lattice dielectric properties of hafnium oxide. Phys. Rev. B 2002 , 65 , No. 233106.
- (45) Togo, A.; Tanaka, I. First principles phonon calculations in materials science. Scr. Mater. 2015 , 108 , 1 -5.
- (46) TURBOMOLE v6.2 2010, A Development of University of Karlsruhe and Forschungszentrum Karlsruhe GmbH, 1989-2007, TURBOMOLE GmbH, since 2007. Available from http://www. turbomole.com (last accessed 27 Nov, 2019).
- (48) Schafer, A.; Horn, H.; Ahlrichs, R. Fully optimized contracted ̈ Gaussian basis sets for atoms Li to Kr. J. Chem. Phys. 1992 , 97 , 2571 -2577.
- (47) Schafer, A.; Huber, C.; Ahlrichs, R. Fully optimized contracted ̈ Gaussian basis sets of triple zeta valence quality for atoms Li to Kr. J. Chem. Phys. 1994 , 100 , 5829 -5835.
- (49) Luo, Y. R. Comprehensive Handbook of Chemical Bond Energies ; CRC Press: Boca Raton, FL, 2007.