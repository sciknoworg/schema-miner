<!-- image -->

RESEARCH ARTICLE |  MARCH 03 2021

## In silico design of a thermal atomic layer etch process of cobalt 

<!-- image -->

Special Collection: Atomic Layer Etching (ALE)

<!-- image -->

Suresh Kondati Natarajan ; Michael Nolan ; Patrick Theofanis; Charles Mokhtarzadeh; Scott B. Clendenning

<!-- image -->

Check for updates

J. Vac. Sci. Technol. A 39, 022603 (2021)

https://doi.org/10.1116/6.0000804

 

<!-- image -->

## Articles You May Be Interested In

Dynamics of propene adsorption on Ag ( 001 )

- J. Chem. Phys. (April 2005)

Investigation of valence orbitals of propene by electron momentum spectroscopy

- J. Chem. Phys. (June 2005)

Reference Correlations of the Thermal Conductivity of Ethene and Propene

- J. Phys. Chem. Ref. Data (August 2016)

<!-- image -->

<!-- image -->

<!-- image -->

## In silico design of a thermal atomic layer etch process of cobalt

Cite as: J. Vac. Sci. Technol. A 39 , 022603 (2021); doi: 10.1116/6.0000804 Submitted: 20 November 2020 · Accepted: 4 February 2021 · Published Online: 3 March 2021

<!-- image -->

<!-- image -->

<!-- image -->

Suresh Kondati Natarajan, 1,a) and Scott B. Clendenning 4

Michael Nolan, 2,3

Patrick Theofanis, 4 Charles Mokhtarzadeh, 4

## AFFILIATIONS

- 1 Department of Electrical Engineering and Automation, Aalto University, Espoo 02150, Finland
- 2 Tyndall National Institute, University College Cork, Lee Maltings, Dyke Parade, Cork T12 R5CP, Ireland
- 3
- Nanotechnology and Integrated Bioengineering Centre, Ulster University, Shore Road, Newtownabbey,

County Antrim BT37 0QB, Northern Ireland

- 4 Intel Corporation, 2501 NE Century Blvd., Hillsboro, Oregon 97124

Note: This paper is part of the 2021 Special Topic Collection on Atomic Layer Etching (ALE).

- a) Electronic mail:

suresh0807@gmail.com

## ABSTRACT

Thermal atomic layer etch (ALE), facilitating the removal of up to one monolayer of material per cycle, is growing in importance for thin-film processing. The number of available ALE processes is much smaller than for atomic layer deposition, its complementary growth process. Quantum chemical simulations are a key approach in the development of new thermal ALE processes, however, methodologies and workflows need to be developed. In this regard, the present paper reports a simulation-based approach toward the development of new thermal ALE processes using metallic cobalt as a test case. We demonstrate a predictive process discovery approach for ALE in which target volatile etch products and the corresponding gas phase reactants are chosen from the literature, an overall ALE cycle for each combination of reactant is investigated for thermochemical favorability, and the detailed mechanisms of the individual reaction steps in the proposed ALE processes are studied using density functional theory. From these results, we derive a temperature-pressure process window for each combination of reactants at typical reactant and product pressures allowing the selection of an ALE process window. For Co ALE, we investigated propene, butyne, silane, and trimethyl silane as a first pulse reactant and CO as the second pulse reactant. We propose propene and CO as the best combination of reactants for Co ALE. Propene adsorbs with sufficient strength to the target Co atom at temperatures below the CO decomposition temperature of 440 K, which results in the lowest energy etch species. This approach is equally relevant for the ALE process design of elemental, binary, and ternary materials.

Published under license by AVS.

https://doi.org/10.1116/6.0000804

## I. INTRODUCTION

One of the main bottlenecks in the down-scaling of modernday semiconductor architectures is identifying novel materials that meet the necessary performance requirements for next generation devices. Even then, effective thin-film processing techniques need to be developed to meet the stringent critical dimension (CD) requirements of these semiconductor devices. To this end, thermal atomic layer etching (ALE) has been introduced as an isotropic material removal technique that can accompany atomic layer deposition (ALD) in the processing of nano-architectures with targeted CDs below 10 nm. Thermal ALE is similar to ALD in that it is an '

iterative process made up of sequential self-limiting reactions enabling the conformal removal of up to one monolayer of material per cycle, even in high aspect-ratio structures. 1 -6 A minimum of two reactant pulses per cycle are required, the first pulse to chemically modify only the surface layers and the second pulse to introduce an ' etchant ' in order to generate volatile etch products that can be thermally desorbed from the surface.

While there have been experimental reports on the thermal ALE of a range of compound materials, 7 -23 such processes for elemental materials are less common, with only a handful of examples for materials such as for W, 24 -26 Fe, 27 Co, 28 Cu, 29 -31 Si, 32 and Ge. 33

<!-- image -->

CrossMark

25 March 2025 10:18:21

<!-- image -->

In the semiconductor industry, metals such as Cu, Co, and W are widely used as conducting materials in interconnects and transistor contacts while oxides (e.g., Al2O3, 34 HfO2, and ZrO2 35 ) and hard nitrides (e.g., TiN 36 and TaN 37,38 ) are used as dielectric and barrier materials, respectively. Designing an ALE cycle for pure metals, unlike metal oxides for which the metal atoms are typically fully oxidized, requires a chemical approach that must manage the chemical potential energy. Pure metals, especially reactive metals, have high chemical potential energy relative to their metal oxides. The challenge in metal ALE is to find a path down the free energy mountain to control the surface chemistry and achieve the desired result.

Cobalt has been identified as a potential substitute for copper local interconnects and tungsten transistor contacts due to the increased performance at thinner dimensions. 39 As such, ALD process technologies for Co thin-film materials have seen a great deal of development within recent years due to the increased performance of Co materials as the CD of semiconductor devices continue to shrink. 40 -45 However, unlike the surge in Co ALD process development, the complementary Co etch process development has seen very little development. Recently, Konh and co-workers reported an ALE process for metallic Co at 140 /C14 C using Cl2 and hfacH as reagents. 28 They propose that the ALE process proceeds by an initial chlorination of the Co surface in the first pulse followed by the introduction of hfacH which reacts with the CoClx surface at elevated temperatures and results in the formation of the etch product Co(hfac)2 along with the generation of a volatile HCl by-product. This process is strongly temperature dependent with a variable etch rate of 0.2 nm/cycle at 140 /C14 C to 1.6 nm/cycle at 185 /C14 C. Moreover, the presence of surface F species was also confirmed with XPS in this study. In a similar fashion, chemical vapor etch processes that have utilized acacH and hfacH have also been reported 46,47 but similarly the resulting thin films exhibit non-negligible amounts of fluorine contamination. This is an undesirable effect which has been shown to be detrimental to the performance of CMOS devices and a key attribute of these processes to be avoided. 48,49 Therefore, an efficient fluorine-free ALE process for Co metal is vital for the fabrication of next generation local interconnects and transistor contacts at thinner dimensions and presents an excellent test case for a quantum chemical analysis of the development of a Co ALE process.

The ALE of oxide or nitride materials typically requires the metal atoms to be in an almost fully oxidized state (M a þ ). In the case of elemental materials such as Co is in 0 oxidation state, it is necessary to facilitate a surface reaction that not only functionalizes the surface but also provides controlled oxidation of the surface. For metals, care must be taken so that the reaction self-limits and does not promote runaway oxidation of the metal which can produce a thick oxidized surface layer. The oxidizing agent must be carefully selected to drive the metal surface reactions toward the oxidation state of the metal in the desired etch product but not beyond it.

We have previously used density functional theory (DFT) based quantum chemical simulations to validate experimental findings such as etch rates and compute thermodynamic properties to estimate the reaction energy requirements of individual ALE steps and understand the underlying etch mechanisms of ALE processes for, e.g., Al2O3, 50 metallic W, 51 HfO2, and ZrO2. 52 Compared to experiments, computational studies offer a relatively inexpensive way to investigate a broad range of thermal ALE processes. However, very few rigorous computational studies of thermal ALE processes using quantum chemical calculations have been reported so far. Of note is the work of Ventzek and co-workers 53 who presented a DFT study focusing on the ALE of polymer surfaces using an oxygen flux and Hamaguchi and co-workers 54,55 who investigated the self-limiting behavior of hexafluoroacetylacetone (hfacH) on Ni and NiO. However, the above computational studies were based on known ALE processes. To date, no ALE process has been proposed exclusively from quantum chemical simulations.

In developing thermal ALE, we require a methodology that is general and applicable across multiple materials. This can be achieved by developing systems that are predisposed for the appropriate reactivity profiles such that precursors that produce volatile complexes as etch products can be quickly screened, a task for which density functional theory (DFT) is well positioned. Herein, we present a general computational approach for the prediction of a new ALE process as shown in Fig. 1, which we have employed for the development of a novel Co ALE process. In the first step of our computational approach, volatile etch products are identified from a survey of the literature based on the process requirements. It is to be mentioned that ALD precursors could be considered for the target etch species provided a synthetic route to their formation under ALE process conditions is feasible. The target etch species typically has one or more ligand types present. Bulkier etch products are associated with low etch rates, so care must be taken to choose targets with workable steric profiles to enable volatilization. In the second step, the gas phase coreagents are chosen to develop a reaction pathway capable of generating the desired etch product to complete the ALE cycle. In the third step, we use the reactants selected in the second step and compute the overall surface reaction energies from DFT to verify if the chosen reagents result in a thermodynamically viable ALE process. We also consider the thermochemistry of unwanted side reactions (such as undesired

FIG. 1. Graphical representation of the steps involved in the computer aided discovery of a new thermal atomic layer etch process.

<!-- image -->

25 March 2025 10:18:21

<!-- image -->

by-product formation or nonself-limiting nature of the reactantsubstrate interaction) that might occur during the ALE pulses and make sure that they do not affect the desired reaction path in the ALE pulses. Finally, in the fourth step, the energy requirements for the individual reaction steps in the ALE process in addition to any kinetic barriers are studied using quantum chemical simulations. From these results, we construct a map of the pressure-temperature process window for our proposed process.

Volatile organometallic Co compounds containing carbon monoxide and an organic ligand, such as (C3H5)Co(CO)3, (C4H6) Co(CO)6, (SiH3)Co(CO)4, and (Si(CH3)3)Co(CO)4, in which the central Co atom is mildly oxidized (+1 oxidation state) are chosen as suitable target etch products from the literature. In this work, we wanted to avoid higher oxidation states of Co. Higher oxidation states are usually induced by stronger reagents, and they may not be self-limiting and result in the formation of a thick modified layer, which is undesirable for ALE in general. For example, the use of O2 as first pulse chemical oxidized Co atoms to +2 or +3 states and can also promote runaway oxidation. Therefore, we only chose those complexes where the central Co atom has +1 as the highest oxidation state. Based on the above selection, propene (C3H6), butyne (C4H6), silane (SiH4), and trimethyl silane [TMS (SiH (CH3)3)] are the corresponding organic molecules selected as surface modifiers that upon reacting with the surface would lead to a single oxidation event per Co atom in the first ALE pulse and CO is selected as the second pulse reactant. Out of all the considered etch species, based on thermochemical analysis, (C3H5)Co(CO)3 is found to be the most suitable. Moreover, this complex is a Co ALD precursor which is stable and volatile at ALE relevant temperatures. 56,57 Therefore, propene and CO are chosen as the corresponding first and second pulse reactants. In fact, propene is favorable as a reagent for the first pulse due to its availability, thermal stability, and better vapor pressure control over the other reagents. Using the above reactant combination, we performed a detailed mechanistic study for direct simulation of the individual reactant pulses in Co ALE. Moreover, this proposed ALE process for Co avoids fluorine contamination as the reactants are fluorine free and it is suitable for industrial process integration.

This DFT based thermochemical analysis enables the prediction of the temperature-pressure process window for this proposed ALE process and showcases the role of quantum chemical modeling in ALE process development.

## II. METHODS AND COMPUTATIONAL SETUP

## A. DFT settings

Spin-polarized density functional theory implemented in Vienna Ab initio Simulation Package (VASP v5.4) 58 is the electronic structure method used in this work. Plane wave basis functions with an energy cutoff of 400 eV were used to represent valence electrons, while projector augmented wave (PAW) potentials 59,60 were used to represent the core electrons. The valence electronic configuration of the elements in the PAWs is Co: [Ar] 3d 8 4s , C: [He] 2s 1 2 2p 2 , O: [He] 2s 2 2p 4 , H: 1s , and Si: [Ne] 3s 1 2 3p 2 . Therefore, the valence charges of Co, C, O, H, and Si are 9, 4, 6, 1, and 4, respectively. Exchange-correlation (XC) contributions to the electronic energy are computed using generalized gradient approximated Perdew -Burke -Ernzerhof (PBE) potential. 61 Grimme s D3 dispersion correction ' 62 is also included to account for the Van der Waals interactions, which cannot be excluded when organic molecules interact with metallic surfaces. The convergence criteria for the electronic energy and the ionic relaxations are 10 /C0 4 eV and /C0 0.02 eV/Å. The energetic barriers discussed in this paper are computed using climbing image nudged elastic band approach with three to five images and a convergence criterion of /C0 0.02 eV/Å. 63,64

## B. Bader charge analysis

Oxidation state (or oxidation number) is calculated as the difference between the computed total valence charge of atoms in the interacting heterogeneous system and the corresponding atomic valence charge given in the PAW potentials. If the computed valence charge value is less than the atomic valence charge, then the target atom is being oxidized and vice versa. The computed valance charges are based on the Bader charge partitioning scheme using the Bader code. 65 The charge analysis is performed on the total charge density (valence + core) to account for the nonlocal charge distribution. Bader charge partitioning is based on the quantum theory of atoms in molecules (QTAIM) 66 and works directly on the charge density given by the electronic structure code. This is a more intuitive way to partition atoms using a zero flux surface and provides better prediction for atomic charges than other charge density partitioning schemes. The computed valence charges will be integers if the computed electronic density is localized and symmetric. Fractional Bader valence charges indicate that the electron density is not localized, is not symmetric, and is polarized along the bond directions and shared between the participating atoms.

## C. Validation of Bader charge analysis

Zunger and co-workers 67 found that DFT calculations may show only a small change in the valence charge while the oxidation state of a transition metal is altered. Goodenough and co-workers 68 found that the Bader valence charge of a V atom center in two different V containing materials was similar while they must clearly be in different oxidation states. This is due to the delocalization of the valence charge density of V atom within its local environment and Bader analysis can only provide a relative estimate of the charge, i.e., oxidation of V(III) to V(IV) might only result in a change in valence charge of 0.08e. Therefore, to validate the results obtained from Bader analysis, we computed the valence charges of Co atoms in bulk Co and bulk CoO (Materials project ID: mp-22408). The valence charge on an isolated Co atom is 9.0e based on our computational setup. Co atoms in bulk Co are at zero oxidation state, and the Bader analysis consistently predicts the valence charge as 9.0e. In CoO, the Co and O atoms form ionic bonds, and the Co atoms are in an oxidation state of +2. The computed Bader valence charge for the Co ions in CoO is 7.9e instead of 7.0e and for the O ions it was 7.1e instead of 8.0e. In the organometallic complexes of Co(I) introduced earlier, such as (C3H5)Co (CO)3, (C4H6)Co(CO)6, (SiH3)Co(CO)4, and [Si(CH3)3]Co(CO)4, the central Co atom has computed Bader valence charges of 8.45e, 8.5e, 8.38e, and 8.32e, respectively, instead of 8.0e. As discussed

<!-- image -->

earlier, charge partitioning schemes such as Bader s ' approach assume atom centered charge distributions; thus, they will not provide the absolute charge of an atom in a covalently bonded environment in which the charge distribution is nonlocal. A table with Bader valence charges of various Co containing materials and molecules is given in Table S1 of the SM.

## D. Bulk and surface models

Bulk Co has HCP symmetry with the computed lattice constant of a=b=2.46 Å, c=3.98 Å, α ¼ β ¼ 90 , /C14 and γ ¼ 120 . /C14 69 This matches well with the experimental lattice constant of a ¼ b ¼ 2 51 Å, : c ¼ 4 07 A , : /C14 α ¼ β ¼ 90 , /C14 and γ ¼ 120 . /C14 70 The bulk lattice constant was computed by simultaneously relaxing the cell volume and cell dimensions using a slightly increased plane wave energy cutoff of 550 eV and a 12 /C2 12 /C2 12 Monkhorst -Pack K-point mesh. Moreover, the calculated cohesive energy of bulk Co was found to be /C0 5 58 eV and the experimental value is : /C0 4.43 eV. PBE functional has been shown to overestimate the cohesive energy of Co. 71 The nearest Co -Co distance is computed at 2.46 Å, while the experimental value was 2.49 Å. 71 A five-layered high-index Co(2 0 1) surface with a surface area of 0.81 nm 2 is chosen for this study, and this surface has step edges that will make it more reactive to the reactant molecules as compared to the ideal flat (1 1 1) surface.

In each layer, there are 16 Co atoms which amounts to 80 Co atoms in the slab. A Monkhorst -Pack K-point mesh of 2 /C2 2 /C2 1 is used for all the geometry relaxation calculations. For all adsorption calculations, the entire slab is relaxed to arrive at the local minimum geometries. Models of Co bulk and the Co(2 0 1) surface are given in Sec. S2 of the supplementary material. 82

## E. Energy equations

Reaction energy Δ E is computed as

$$\Delta E = \sum _ { i } ^ { n P } n E _ { i } - \sum _ { j } ^ { n R } m E _ { j }. \quad \quad ( 1 ) \quad \underset { \text{and} \text{ } } \text{ } \underset { \text{and} \text{ } } \text{ } \text{ } \text{ } \text{ } \text{ } \text{ } \text{ } \text{ } \text{ } \text{ } \text{ } \text{ } \text{ } \text{ } \text{ } \text{ } \text{ } \text{ } \text{ } \text{ } \text{ } \text{ } \text{ } \text{ } \text{ } \text{ } \text{ } \text{ } \text{ } \text{ } \text{ } \text{ } \text{ } \text{ } \text{ } \text{ } \text{ } \text{ } \text{ } \text{ } \text{ } \text{ } \text{ } \text{ } \text{ } \text{ } \text{ } \text{ } \text{ } \text{ } \text{\ } \text{ } \text{ } \text{ } \text{ } \text{ } \text{ } \text{ } \text{ } \text{ } \text{ } \text{ } \text{ } \text{ } \text{ } \text{ } \text{ } \text{ } \text{ } \text{ } \text{ } \text{ } \text{ } \text{ } \text{ } \text{ } \text{ } \text{ } \text{ } \text{ } \text{ } \text{ } \text{ } \text{ } \text{ } \text{ } \text{ } \text{ } \text{ } \text{ } \text{ } \text{ } \text{ } \text{ } \text{ } \text{ } \text{ } \text{ } \text{ } \text{ } \text$$

Here, nP and nR are the number of product molecules and reactant molecules, respectively. n and m are the stoichiometric coefficients of the respective species. Reaction free energy is computed as

$$\Delta G = \sum _ { i } ^ { n P } n G _ { i } - \sum _ { j } ^ { n R } m G _ { j } + R T \ln ( Q ), \quad \ \ ( 2 ) \quad \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \$$

$$G = E + Z P E + W ( T ) - T S,$$

$$Q = \prod P _ { \text{products} } ^ { \mu } / \prod P _ { \text{reactants} } ^ { \mu }.$$

Here, R is the gas constant. ZPE, W T ( ), and S are the zero point energy, temperature dependent enthalpy contribution, and entropy, respectively. The RT ln( Q ) term introduces the reactant and product pressure contributions to the reaction free energy. We have used 0.2 Torr for reactant pressure and 0.01 Torr for the product pressure, the latter cannot be controlled in the etch reactor. An increase in reactant pressure would typically lower the free energy and make the forward reaction more favorable. Accurate force constants from density functional perturbation theory (DFPT) implemented in VASP are coupled with the Phonopy code 72 to compute ZPE, W T ( ) and S of slab models and only the top layer atoms of the slab are used for this. For convenience, ZPE, W T ( ), and S of molecules are computed using the TURBOMOLE package 73 with PBE XC functional and triple zeta basis set.

Binding energy of a molecule with a surface, E bind is computed as

$$\begin{smallmatrix} o \\ e \\ b \\ e \end{smallmatrix} = E _ { \text{interacting system} } - ( E _ { \text{isolated surface} } + E _ { \text{isolated molecule} } ), \quad ( 5 )$$

and the terms on the right hand side are the total energy of the molecule adsorbed on the surface (interacting system), the total energy of the bare surface, and the total energy of the isolated molecule.

## III. RESULTS

## A. Ideal Co ALE cycle

The four stages of an ideal Co ALE process, namely: (1) surface modification pulse, (2) purge, (3) material removal pulse, and (4) purge are schematically represented in Fig. 2.

The reactant chemical for the surface modification pulse (stage 1) must be chosen in such a way to ensure a self-limiting reaction and the formation of a thin modified layer leading to a sub-monolayer etch rate. The aim is to avoid the oxidation of Co to its +2 or +3 oxidation states (and we remind the reader that this discussion frames oxidation as a loss of electrons from the metal rather than metal oxide formation), which is typical when strong oxidants are used (e.g., O3 or N2O). This is to ensure favorable binding of second pulse reactant to the oxidized Co surface atoms.

For the above reasons, strong oxidizing agents such as O3, O2, N2O, Cl2, and F2 are avoided as the first pulse reagent. Instead, we identified propene as the chemical to functionalize the Co surface and act as a mild oxidizing agent in stage 1 that will modify the

FIG. 2. Schematic representation of the ideal thermal atomic layer etch process for Co.

<!-- image -->

<!-- image -->

oxidation state of Co to at most +1 without formation of thick modified layers. Following the chemical modification of the Co surface, the unreacted gases and any volatile by-products for the initial surface functionalization are purged from the system in stage 2. The modified Co layer is volatilized by the addition of a secondary etch ligand (Y) in stage 3 and subsequently removed in stage 4, which is a purge event.

## B. Step 1: Selection of target volatile species

In general, volatile metal complexes of the metal to be etched are a suitable initial choice as the target etch species. A thorough literature search on volatile compounds of the target material gives a wide selection of possible candidates. From the literature, 74 volatile compounds of cobalt where the metal atom exists in a low oxidation state, e.g., Co þ 1 , are selected for the reasons stated earlier. The selected volatile species include (C3H5)Co(CO)3, (C4H6)Co2 (CO)6, (SiH3)Co(CO)4, and [Si(CH3)3]Co(CO)4. As shown earlier, the central Co atom in these complexes has a computed Bader valence charge between 8.3e and 8.5e, which corresponds to Co 1 þ . All these complexes contain three to six carbonyl ligands that impart enhanced stability to the low valent metal center in the volatile etch product. CO functions as an L-type ligand as it does not oxidize or occupy a formal valence on the target Co metal atom. Moreover, further stability is imparted onto the volatile etch product by virtue of the strong metal /C0 ! ligand π -back bonding interaction between Co and CO which helps to accommodate the increased electron density found on low-valent metal centers when compared to higher valent etch products [e.g., Co(acac)2]. 75

## C. Steps 2: Selection of the reactant molecules

By identifying suitable volatile etch products in step 1 and by utilizing a molecular design approach, the corresponding oxidizing agents for the first pulse and subsequent pulses can be chosen to generate the desired etch products, as shown in Fig. 3. The first pulse reactants corresponding to the selected target species are C3H6 (propene), C4H6 (butyne), SiH4 (silane), and SiH(CH3)3 (trimethyl silane) shown in Fig. 3, while the second pulse reactant chosen is CO. Bulk conversion of Co to Co2(CO)8 during CO exposure is possible only at very high pressures of 100 atm (76 000 Torr) and 473 K; 74 therefore, this bulk conversion reaction should be avoided at the modest reactant pressures typically used in ALE processes. Moreover, CO molecules do not dissociate spontaneously on the Co surface at ALE relevant temperatures. However, they were found to desorb as CO above 350 K or form CO2 at 440 K. 76 These characteristics are ideal for the ALE process as they discourage oxide formation and restrict the deposition of carbon when the ALE temperature is set below 440 K.

## D. Step 3: Overall reaction energies

The model reactions of all reactant combinations (R1: propene +CO, R2: butyne+CO, R3: silane+CO, and R4: TMS+CO) for the full Co ALE cycle are given in Table I. In these reactions, we consider a bare surface of cobalt (Co(surf) ) exposed to one molecule of the first pulse reactant (1.23 molecules/nm ) and six CO molecules 2 (7.4 CO/nm 2 ), as identified in step 2. These reactions result in a bare surface of Co in which one or two Co atoms are removed, denoted as Co(surf /C0 1) or Co(surf /C0 2) , together with a molecule of the corresponding gas phase etch product identified in step 1. The number of CO molecules needed to volatilize a Co surface atom is different depending on the oxidizing agent used (R1 /C0 propene = 3; R2 /C0 butyne = 6; and R3,R4 /C0 silane/TMS = 4). However, we have considered six CO molecules in all the reactions even though not all of them are needed to form the volatile species in R1, R3, and R4. This is to ensure that the comparison of free energies between different reactant combinations is not biased toward the molecules with large number of CO ligands. In R1, R3, and R4 reactions, the product surfaces have 3, 2, and 2 CO molecules left adsorbed on them. For reference, the reaction energies without any CO residues left on the surface are given in Sec. S3 of the supplementary material. 82 The removed surface Co atoms could either be a highly coordinated surface atom (Cos) or an adatom (Coa).

Table I presents the computed reaction free energies of these model reactions at 0 K and at 500 K for the removal of the Coa ( Δ G a ), a Cos ( Δ G s ), and the energy difference between the two cases ( Δ G s /C0 Δ G a ). This energy difference provides a method to assess if the difference in reactivity of the target Coa and a Cos changes with temperature. The free energy estimates for R2 are higher than the other reactions because 1 butyne molecule needs all six CO molecules to form the volatile species that removes two Co atoms at once and we have only shown the free energy per Co removal for fair comparison. The corresponding free energy profiles spanning 0 K to 1000 K are shown in Fig. 4. For all reactant combinations, the removal of the Coa is always more favorable by ca. 1.7 eV -2.2 eV at all temperatures, Table I and Fig. 4. This is consistent with the recent work by Konh et al. 28 The origin of this result is that the Coa (adatom) has a lower coordination number of 3, compared to a coordination number of 9 for other Cos atoms, while bulk Co is 12-fold coordinated. The removal of a Cos atom involves breaking nine Co Co -bonds of which six are surface Co Co bonds while the other three are subsurface bonds. In con--trast, the Coa is bound to only three surface Co atoms, which allow the reactants to attach more favorably to it.

For all reactant combinations, the etch of both Coa and Cos atoms is favorable at 0 K, whereas the removal of the Cos atom is unfavorable only for R2 at 500 K. The Δ G s /C0 Δ G a values are similar for each reactant combinations at 0 K and 500 K. This implies that the entropic cost for the removal of both Coa and Cos atoms, with the studied reactant combinations, is roughly the same.

Reactions R1, R3, and R4 which incorporate propene, silane, and TMS as the first coreactant pulse show the most favorable reaction energies for Co etch in that order followed by R2. From Fig. 4, we find that all first pulse reactants result in favorable ALE process up to 600 K for removal of the Coa atom. Except butyne, all other first pulse reactants result in favorable removal of the Cos atom up to at least 500 K. Free energy profiles for the reactions without CO residues are given in Sec. S3 of the supplementary material. 82 Based on the above thermochemical results, the combination of propene and CO has a small energy advantage over the other reactant combinations. Taking this into account, we present a detailed investigation of the propene þ CO combination for ALE in Sec. III E. However, the other combinations were also studied, and the details are presented in Sec. S4 of the supplementary material. 82

25 March 2025 10:18:21

FIG. 3. Chemical formulas and structures of the target volatile species and first pulse chemicals.

<!-- image -->

<!-- image -->

TABLE I. Reaction free energies ( Δ G ) of the postulated overall ALE reactions at 0 K and 500 K. The energy values are given in eV and are given per Co removed. Δ G a and Δ G s refer to free energies when an adatom (Coa) and surface atom (Cos) are etched, respectively. Δ G s -Δ G a is the free energy difference between removing a Cos and the Coa. Cosurf refers to the clean (2 0 1) surface of Co and Co surf /C0 x refers to the same surface with x atoms removed from the top layer. Reactant pressure used is 0.2 Torr and product pressure used is 0.01 Torr.

|    |                                                                                                      | at 0 K   | at 0 K   |                   | at 500 K   | at 500 K   |                   |
|----|------------------------------------------------------------------------------------------------------|----------|----------|-------------------|------------|------------|-------------------|
|    | Reactions                                                                                            | Δ G a    | Δ G s    | ( Δ G s - Δ G a ) | Δ G a      | Δ G s      | ( Δ G s - Δ G a ) |
| R1 | Co (surf) + C 3 H 6(g) + 6CO (g) /C0 ! Co (surf - 1+3CO) + (C 3 H 5 )Co(CO) 3(g) + 0.5H 2(g)         | - 8.73   | - 6.60   | 2.13              | - 2.62     | - 0.40     | 2.19              |
| R2 | Co (surf) + C 4 H 6(g) + 6CO (g) /C0 ! Co (surf - 2) + (C 4 H 6 )Co 2 (CO) 6(g)                      | - 3.79   | - 2.09   | 1.70              | - 0.69     | 0.98       | 1.67              |
| R3 | Co (surf) + SiH 4(g) + 6CO (g) /C0 ! Co (surf - +2CO) + (SiH 3 )Co(CO) 4(g) + 0.5 H 2(g)             | - 8.26   | - 6.21   | 2.05              | - 2.53     | - 0.41     | 2.12              |
| R4 | Co (surf) + SiH(CH 3 ) 3(g) + 6CO (g) /C0 ! Co (surf - +2CO) + (Si(CH 3 ) 3 )CO(CO) 4(g) + 0.5H 2(g) | - 8.44   | - 6.39   | 2.05              | - 2.54     | - 0.42     | 2.12              |

<!-- image -->

<!-- image -->

## E. Step 4: Energy requirements of individual ALE steps: Propene+CO

In this section, we look at the mechanism involved in the ALE of Co using propene and CO as reactants.

Figure 5 shows a schematic representation of the proposed Co ALE process with propene and carbon monoxide (CO) as reactants. The free energy values of the individual reaction steps at 0 K, 500 K, and 800 K along with the cumulative free energy change are listed in Table II. The metal adatom on the Co surface is the targeted atom for removal.

## 1. Pulse 1

FIG. 4. Free energy profiles of the overall etch reactions given in Table I. Solid lines correspond to the etch of an adatom and dotted lines correspond to the etch of a surface atom.

In the first ALE pulse, the Co surface is exposed to propene gas. A propene molecule initially adsorbs nondissociatively at the low coordinated Co atom (reaction 1 in Fig. 5) with a Δ G of /C0 1.31 eV (this increases to /C0 0.15 eV at 500 K due to entropic loss -see Table II). The target Co adatom sits at a threefold site coordinated by three nearest surface Co atoms. On adsorption, the length of the C ¼ C bond in propene elongates slightly from 1.33 Å to 1.37 Å. The target cobalt atom is oxidized with a computed valence charge of 8.79e (see Sec. S1 of the supplementary material for the list of Bader charges). 82 For comparison, the valence charge of Co in the final etch product is 8.45e. As discussed earlier in the methods section, the partial valence charges are because of the nonlocal

FIG. 5. Schematic of the proposed full ALE cycle with propene and CO as first and second pulse chemicals, respectively. Red arrow (1) is for the adsorption of propene, blue arrow (2) for propene dissociation and H adsorption, orange arrow (3b) for H desorption, green arrow (4) for CO adsorption, and purple arrow (5) for etch product desorption.

<!-- image -->

<!-- image -->

TABLE II. Reaction free energies of the individual reactions of Co ALE cycle with propene and CO as reactants. a and b correspond to those reactions in which the dissociated H atom is adsorbed on and desorbed from the surface, respectively. For these calculations, the surface entropy contributions are assumed to be zero.

|                          | Δ G (eV/Co T )   | Δ G (eV/Co T )   | Δ G (eV/Co T )   | Δ G (eV/Co T )   | Δ G (eV/Co T )   | Δ G (eV/Co T )   |
|--------------------------|------------------|------------------|------------------|------------------|------------------|------------------|
|                          | T = 0 K          | T = 0 K          | T = 500 K        | T = 500 K        | T = 800 K        | T = 800 K        |
| Reaction                 | Δ G              | Δ G cum :        | Δ G              | Δ G cum :        | Δ G              | Δ G cum :        |
| 1: C 3 H 6 adsorption    | - 1.31           |                  | - 0.15           |                  | 0.50             |                  |
| 2: H dissociation        | 0.08             | - 1.23           | 0.06             | - 0.09           | - 0.01           | 0.49             |
| (H intact) 3a: Purge 1   | 0.00             | - 1.23           | 0.00             | - 0.09           | 0.00             | 0.49             |
| 4a: CO adsorption        | - 5.49           | - 6.72           | - 1.79           | - 1.88           | 0.47             | 0.96             |
| 5a: Purge 2              | 3.13             | - 3.59           | 1.29             | - 0.59           | 0.23             | 1.19             |
| (H desorbed) 3b: Purge 1 | 0.33             | - 0.90           | - 0.14           | - 0.23           | - 0.43           | 0.06             |
| 4b: CO adsorption        | - 5.15           | - 6.05           | - 1.52           | - 1.75           | 0.64             | 0.70             |
| 5b: Purge 2              | 2.98             | - 3.07           | 1.12             | - 0.63           | 0.07             | 0.77             |

distribution of charge density by the quantum chemical method. This type of adsorption study is well known and followed by computational surface science researchers. 77,78

As predicted from our molecular design principles, this result indicates that we do not induce a high oxidation state of this Co atom, which is desirable. A C -H bond from the /C0 CH3 fragment of the adsorbed propene molecule dissociates (reaction 2 in Fig. 5) with Δ G ¼ 0 08 eV : (0.06 eV at 500 K, decreases due to entropic gain). The average distance of the target Co atom from the three closest surface Co atoms on the bare Co(3 1 0) surface is 2.24 Å and it increases to 2.29 Å and 2.33 Å after C3H6 adsorption and H dissociation, respectively. This indicates weakening of the CoT -Co bonds.

A pathway for H dissociation from adsorbed propene to the Co surface is explored in a short 90 fs MD simulation with a time step of 0.5 fs at 300 K starting from the nondissociated geometry of propene adsorbed on the Co surface (MD snapshots and distance plots given in Sec. S5 of the supplementary material). 82 At 300 K, H dissociation (C1 -H1 bond in Fig. 5) is spontaneous and we estimate an activation free energy barrier of 0.23 eV at 300 K from the change in potential energy with respect to the C1 -H1 distance in the MD trajectory, which compares to 0.20 eV obtained from a CI-NEB calculation of the activation energy barrier for H dissociation (more details in Sec. S5 of the supplementary material). 82 Reference 77 shows that dehydrogenation of propene on Co surfaces is favorable at low temperatures, which is compatible with our results.

Dissociation of propene results in a small change in the Bader valence charge of the target Co atom to 8.74e (Sec. S1 of the supplementary material shows Bader charges of all participating atoms). 82 Hopping of hydrogen to different sites on the Co surface has activation energies between 0.04 eV and 0.64 eV depending on whether it diffuses via a bridge site (small barrier) or over the atop site (large barrier). The activation energy needed to desorb the H atom as gas phase H2 is computed as 0.7 eV which is consistent with the experimental range of 0.6 eV -0.8 eV. 79 The activation energy needed to dissociate the adsorbed propene and desorb the

H atom is, thus, ca. 0.7 eV, which allows them to proceed at reasonable temperatures.

## 2. Purge 1

In the first ALE purge, the unreacted propene molecules are removed from the etch chamber, with H remaining on the Co surface (reaction 3a in Fig. 5) or together with the removal of dissociated H atoms as H2 (reaction 3b in Fig. 5). The desorption of the H atom as H2 costs energy of about 0.33 eV/H at 0 K ( /C0 0 14 eV at : 500 K, entropic gain) which increases the cumulative free energy up to this step to Δ G cum : ¼ /C0 0 98 eV at 0 K ( : /C0 0 35 eV at 500 K, as a : result of the net entropic loss arising from propene adsorption and H desorption) per target Co atom in reaction 3b. In contrast, the Δ G cum : is about /C0 1.31 eV at 0 K in reaction 3a ( /C0 0 21 eV at 500 K, : here there is no entropic gain associated with desorption of H). Desorption of H is favored at high temperatures due to entropic gain. Thus, the Δ G cum : difference between reactions 3a and 3b is reduced at 500 K, while Δ G cum : becomes positive at 800 K for both reactions suggesting that a self-limiting propene adsorption step is not possible beyond this temperature, which in any case is well above typical ALE operating temperatures.

## 3. Pulse 2 and purge 2

In the second ALE pulse, carbon monoxide (CO) molecules are introduced into the etch chamber. A reactor temperature around 350 K is preferred as we have noted earlier that CO desorbs from the Co surface at this temperature. CO will saturate the Co surface at temperatures lower than 350 K. Above 350 K, the lifetime of CO molecules at the Co surface is decreased because they start desorbing and they will eventually be removed from the reactor during the purge step. This will prevent excess CO from passivating the Co surface after the completion of the first ALE cycle which will allow the propene molecules in subsequent cycles to adsorb at the Co surface without significant diffusion delays due to adsorbed CO.

The role of propene and CO are different in this proposed ALE cycle. Surface passivation as a limiting condition for selflimiting reaction is only valid if the chemical reacts with the surface and modifies it like in the case of propene pulse. It is sufficient if CO etches the propene-modified surface Co atoms as long as it does not decompose and modify the Co surface again by forming CoO. So, keeping the temperature below CO decomposition temperature takes care of this issue. CO reaction is selflimiting in the sense that it does not affect the surface continuously. Therefore at around 350 K, some CO will desorb from the surface and other CO in the gas phase will adsorb at the surface. The purge will remove the desorbing CO and leave sites for propene adsorption in the next cycle.

In our analysis of this step, given the target volatile species that result from the etch process, we consider the adsorption of three CO molecules bound to the target Co atom as shown in Fig. 5 (reactions 4a and 4b). This gives a coverage of 3.90 CO/nm . 2 There is a significant enthalpy gain of /C0 1.72 to /C0 1.83 eV per adsorbed CO in this step. This is because the binding energy of a CO molecule on a bare Co (3 1 0) surface is in the range of /C0 2.5 eV to /C0 2.8 eV, depending on the adsorption site, which is almost twice as strong as the binding energy of C3H6 at the Co surface.

<!-- image -->

The Bader valence charge of the target Co atom further decreases to 8.47e after the CO adsorption, which is very close to the Bader charge of Co atom in the target volatile species (8.45e). Table S2 in the supplementary material lists the Bader valence charges of all relevant participating atoms in this ALE cycle. 82 Bader valence charges of isolated CO molecule are C: 2.9e and O: 7.1e, whereas the Bader charges of CO in the volatile species are C: 3.1e and O: 7.1e. For comparison, the Bader charges of CO adsorbed to the Co surface in pulse 2 is C: 3.5e /C0 3.6e and O: 7.1e which suggest a gain in electron density around the surface bound C (in CO) centers with respect to their molecular counterparts. The average Co -Co distance from the target Co atom to the neighboring surface atom further increases to 2.57 Å (from 2.33 Å just after C1-H1 dissociation) when the three CO molecules are adsorbed. Upon increasing the CO coverage to about 15.6 CO/nm 2 (12 Co per supercell), although this is not likely to be possible under typical ALE conditions, this Co Co distance -increases to 4.1 Å. Thus, the strong Co -CO interaction weakens the binding of the target Co atom with the surface. We would like to note that we have not explicitly calculated any kinetic barriers involved in this pulse. This will be a topic of a future paper. Furthermore, adsorbed CO molecules do not interact with the dissociated H atoms that are present on the surface after the first purge. 80 Therefore, undesirable formation of compounds like HCOOH is also not likely on the Co surface. 81

reaction 5b (CO coverage of 3.9/nm , the desorption energy will be 2 lower at higher CO coverages). These energies indicate that the overall Co ALE cycle will be exoergic at 500 K. As the volatile species are desorbed into vacuum in our model, the desorption energy barrier is equal to the desorption energy given above.

The Co surface modification by propene results in both oxidation of target Co atoms and decreased bond strength (due to increasing Co -Co bond distances) between the target Co atom and the neighboring surface Co atoms. In the second pulse, the interaction via strong pi-back bonding between CO and surface Co atoms results in further reduction in bond strength (again due to increase in Co Co bond distances) -between the target Co atom and its neighbors. We also have shown that the higher the number of CO Co bonds on the surface, the lower the CoT --Co bond strength will be. This aspect of weakening of the surface metal bonds by the chemicals is key to volatilizing the Co etch product and to the successful ALE of the substrate metal.

## 4. Free energy profiles

The volatile species, (C3H5)Co(CO)3, that forms at the surface is desorbed with an energy cost of ca. 3.0 eV allowing the Δ G cum : for the entire ALE cycle to drop to /C0 3.67 eV at 0 K ( /C0 0 71 eV at : 500 K) for reaction 5a and /C0 3 15 eV at 0 K ( : /C0 0 75 eV at 500 K) for :

We now consider the prediction of a temperature-pressure window for a Co ALE process using the chemistry we have described. The free energy profiles of the individual reaction steps in our Co ALE model within the temperature range of 0 K -1000 K are plotted in Fig. 6(a), and the predicted pressure-temperature process window is displayed in Fig. 6(b). Solid lines in Fig. 6(a) represent the case where the dissociated H atom from propene molecule is not desorbed in purge 1, whereas the dotted lines represent case in which the H atom is desorbed. Comparing the two

FIG. 6. (a) Free energy profiles of the individual reaction steps for the ALE process with H desorption after propene adsorption (in dotted lines) or no desorption of H after propene adsorption (in solid lines) given in Fig. 5. (b) The pressure-temperature process window of the complete ALE cycle (H desorbed) computed by considering different ln(Q) values for each temperature. The red line indicated the CO decomposition temperature on the Co surface. The region marked by the black rectangle gives the Co ALE process window when propene and CO are used as reactants.

<!-- image -->

<!-- image -->

situations shows that there is no qualitative difference in the reaction free energy for the individual steps of both cases. A reactant pressure of 0.2 Torr and a product pressure of 0.01 Torr are used for the plots in Fig. 6(a). The full range of reactant and product pressure combinations can be seen in the variation of ln(Q) in Fig. 6(b). Adsorption of propene and CO on the Co surface [lines 1 and 4 in Fig. 6(a)] leads to the formation of strong bonds that increase the enthalpic contribution to the free energy at the expense of a net entropic loss, which arises as a result of hindering of the translational and rotational degrees of freedom of the molecule. The vibrational degrees of freedom are affected to a minor degree. At low temperatures the entropic loss is minimal since there is relatively less kinetic energy in the system, but as the temperature increases this loss becomes appreciable as can be seen from the positive slope of these profiles in Fig. 6(a). The dissociation and desorption of H atom from propene [lines 2 and 3 in Fig. 6(a)] and the desorption of the volatile metal etch species [line 5 in Fig. 6(a)] have the opposite effect to the adsorption of propene and CO discussed earlier (negative slope of the free energy profiles). In these cases, the surface bound molecule either dissociates into two or desorbs into the gas phase which requires energy to break bonds and leads to enthalpic loss. But the desorbed molecules enter into the gas phase and regain their translational and rotational degrees of freedom, which leads to a gain in entropy and this entropic gain is appreciable at elevated temperatures and compensates the enthalpic loss.

There are energy requirements for dissociation and desorption steps (0.2 eV for H dissociation, 0.33 eV for H desorption and 3.0 eV for the etch species desorption) and they can be breached at high temperatures. As a result of the significant gain in enthalpy of CO adsorption [line 4 in Fig. 6(a)], the overall ALE cycle [line 6 in Fig. 6(a)] is favorable up to 620 K. Due to undesirable CO decomposition on Co above 440 K, the process temperature needs to be maintained below 440, at which temperature the overall ALE cycle is favorable.

The next step is to select the reactant pressure, for which we have constructed a pressure-temperature contour plot from the computed free energy of the complete cycle [indicated as number 6 in Fig. 6(a)] with ln(Q) values ranging from 100 to /C0 100 in a temperature range of 0 K -1000 K in Fig. 6(b). For a fixed product pressure of 0.01 Torr, ln(Q) = 0 for the overall ALE reaction is achieved when the reactant pressure is about 0.177 Torr. Increasing the reactant pressure further will result in negative ln(Q) values that lead to free energy gain and vice versa. In this figure, the entire region below the contour line of Δ G ¼ 0 is favorable for ALE. By taking the temperature limit of 440 K and considering a realistic range of reactant and product pressures [ln(Q) values between 20 and /C0 20], the region within the black rectangle is predicted to be the most favorable process window for Co ALE when propene and CO are used as reactants. In this region, the free energy of the overall reaction is negative (favorable) and between /C0 5 eV and /C0 1 eV and negative ln(Q) values enhance the reaction free energy.

## IV. CONCLUSION

In this work, we described a simple four step approach for the in silico design of a thermal ALE process using density functional theory, which has allowed the prediction of suitable precursors, a process temperature range and a process pressure.

These steps are

- (1) Selection of target volatile species.
- (2) Selection of reactant chemicals for each ALE pulse.
- (3) Thermochemical evaluation of the proposed overall reactions.
- (4) Computing energy requirements, reaction mechanism for each step and a temperature/pressure window for the ALE process.

With Co ALE as the test case, a set of organometallic complexes of Co that contain CO were investigated as the candidates for the target volatile etch species. Based on the above targets, first and second pulse reactants are chosen. The first pulse reactant must serve to functionalize the surface while also serving as a mild oxidizing agent to increase the oxidation state of metal atoms to +1 so as to form the target volatile species in the second pulse but without runaway oxidation of the metal. CO adsorbed strongly to the Co surface without further oxidizing Co, as a result of π -back bonding. The above two steps release enough energy to offset the energy needed to desorb the volatile etch products at the end of the second ALE pulse.

Pressure-temperature process windows were derived for all reactant combinations, from which we observe that it is crucial to restrict the process temperature to below 440 K, which will prevent the decomposition of CO on a Co surface. All the reactant combinations considered in this study provide favorable free energies up to 440 K and lnQ between 20 and /C0 20 for the overall ALE process. Propene shows the strongest binding per Co atom, when compared to the other oxidizing agents such as butyne, silane, and TMS. Moreover, propenyl containing volatile species required the least energy to desorb from the Co surface. Thus, we propose propene +CO as a favorable reactant combination for fluorine-free ALE of Co metal at reasonable temperatures and pressure. With this paper, we provide a framework for the rational design of an ALE process, constrained by the formation of known species with known chemical transformations under realistic process conditions, and supported by quantum chemical calculations of the reaction cycle thermodynamics. Such studies will improve our understanding of the reaction mechanisms in the ALE processes and help us preserve valuable resources used in the lab.

## ACKNOWLEDGMENTS

S.K.N. and M.N. thank Intel Corporation for funding. S.K.N. and M.N. also thank the Irish Centre for High-End Computing (project code: tiche081c) and Science Foundation Ireland-funded computing cluster at Tyndall for the computer time.

## DATA AVAILABILITY

The data that support the findings of this study are available from the corresponding author upon reasonable request.

## REFERENCES

1 K. J. Kanarik, T. Lill, E. A. Hudson, S. Sriraman, S. Tan, J. Marks, V. Vahedi, and R. A. Gottscho, J. Vac. Sci. Technol. A 33 , 020802 (2015).

25 March 2025 10:18:21

<!-- image -->

- 2 G. S. Oehrlein, D. Metzler, and C. Li, ECS J. Solid State Sci. Technol. 4 , N5041 (2015).
- 4 K. J. Kanarik, S. Tan, and R. A. Gottscho, J. Phys. Chem. Lett. 9 , 4814 (2018).
- 3 S. M. George and Y. Lee, ACS Nano 10 , 4889 (2016).
- 5 S. K. Song, H. Saare, and G. N. Parsons, Chem. Mater. 31 , 4793 (2019).
- 7 Y. Lee and S. M. George, ACS Nano 9 , 2061 (2015).
- 6 S. M. George, Acc. Chem. Res. 53 , 1151 (2020).
- 8 Y. Lee, J. W. DuMont, and S. M. George, ECS J. Solid State Sci. Technol. 4 , N5013 (2015).
- 11 N. R. Johnson, H. Sun, K. Sharma, and S. M. George, J. Vac. Sci. Technol. A 34 , 050603 (2016).
- 9 Y. Lee, J. W. DuMont, and S. M. George, J. Phys. Chem. C 119 , 25385 (2015). 10 Y. Lee, C. Huffman, and S. M. George, Chem. Mater. 28 , 7657 (2016).
- 12 J. W. DuMont, A. E. Marquardt, A. M. Cano, and S. M. George, ACS Appl. Mater. Interfaces 9 , 10296 (2017).
- 14 J. Hennessy, C. S. Moore, K. Balasubramanian, A. D. Jewell, K. France, and S. Nikzad, J. Vac. Sci. Technol. A 35 , 041512 (2017).
- 13 D. R. Zywotko and S. M. George, Chem. Mater. 29 , 1183 (2017).
- 15 J. W. DuMont and S. M. George, J. Chem. Phys. 146 , 052819 (2017).
- 17 Y. Lee and S. M. George, J. Vac. Sci. Technol. A 36 , 061504 (2018).
- 16 Y. Lee and S. M. George, Chem. Mater. 29 , 8202 (2017).
- 18 Y. Lee and S. M. George, J. Phys. Chem. C 123 , 18455 (2019).
- 20 N. R. Johnson, J. K. Hite, M. A. Mastro, C. R. Eddy, and S. M. George, Appl. Phys. Lett. 114 , 243103 (2019).
- 19 R. Rahman, E. C. Mattson, J. P. Klesko, A. Dangerfield, S. Rivillon-Amy, D. C. Smith, D. Hausmann, and Y. J. Chabal, ACS Appl. Mater. Interfaces 10 , 31784 (2018).
- 21 K. Shinoda, N. Miyoshi, H. Kobayashi, M. Izawa, K. Ishikawa, and M. Hori, J. Phys. D: Appl. Phys. 52 , 475106 (2019).
- 23 A. Fischer, A. Routzahn, Y. Lee, T. Lill, and S. M. George, J. Vac. Sci. Technol. A 38 , 022603 (2020).
- 22 W. Lu, Y. Lee, J. C. Gertsch, J. A. Murdzek, A. S. Cavanagh, L. Kong, J. A. del Alamo, and S. M. George, Nano Lett. 19 , 5159 (2019).
- 24 N. R. Johnson and S. M. George, ACS Appl. Mater. Interfaces 9 , 34435 (2017).
- W. Xie, P. C. Lemaire, and G. N. Parsons, ACS Appl. Mater. Interfaces 10 , 9147 (2018).
- 25
- 26 W. Xie and G. N. Parsons, J. Vac. Sci. Technol. A 38 , 022605 (2020).
- 28 M. Konh, C. He, X. Lin, X. Guo, V. Pallem, R. L. Opila, A. V. Teplyakov, Z. Wang, and B. Yuan, J. Vac. Sci. Technol. A 37 , 021004 (2019).
- 27 X. Lin, M. Chen, A. Janotti, and R. Opila, J. Vac. Sci. Technol. A 36 , 051401 (2018).
- 29 N. Toyoda and A. Ogawa, J. Phys. D: Appl. Phys. 50 , 184003 (2017).
- 31 E. Mohimi, X. I. Chu, B. B. Trinh, S. Babar, G. S. Girolami, and J. R. Abelson, ECS J. Solid State Sci. Technol. 7 , P491 (2018).
- 30 Y. Gong, K. Venkatraman, and R. Akolkar, J. Electrochem. Soc. 165 , D282 (2018).
- 32 A. I. Abdulagatov and S. M. George, Chem. Mater. 30 , 8465 (2018).
- 34 J. Acharya, J. Wilt, B. Liu, and J. Wu, ACS Appl. Mater. Interfaces 10 , 3112 (2018).
- 33 K. Ikeda, S. Imai, and M. Matsumura, Appl. Surf. Sci. 112 , 87 (1997).
- 35 D. M. Hausmann, E. Kim, J. Becker, and R. G. Gordon, Chem. Mater. 14 , 4350 (2002).
- 37 K. Min, K. Chun, and K. Kim, J. Vac. Sci. Technol. B 14 , 3263 (1996).
- 36 K.-C. Park and K.-B. Kim, J. Electrochem. Soc. 142 , 3109 (1995).
- 38 Y. Zhao and G. Lu, Phys. Rev. B 79 , 214104 (2009).
- 40 J. Kwon, M. Saly, M. D. Halls, R. K. Kanjolia, and Y. J. Chabal, Chem. Mater. 24 , 1025 (2012).
- 39 C. Auth, et al. , ' A 10 nm high performance and low-power CMOS technology featuring 3rd generation FinFET transistors, Self-Aligned Quad Patterning, contact over active gate and cobalt local interconnects, ' in 2017 IEEE International Electron Devices Meeting (IEDM) (IEEE, New York, 2017), pp. 29.1.1 -29.1.4.
- 41 H.-B.-R. Lee and H. Kim, Electrochem. Solid State Lett. 9 , G323 (2006).
- 42 H.-B.-R. Lee, W.-H. Kim, J. W. Lee, J.-M. Kim, K. Heo, I. C. Hwang, Y. Park, S. Hong, and H. Kim, J. Electrochem. Soc. 157 , D10 (2010).
- 44 B. S. Lim, A. Rahtu, and R. G. Gordon, Nat. Mater. 2 , 749 (2003).
- 43 J. P. Klesko, M. M. Kerrigan, and C. H. Winter, Chem. Mater. 28 , 700 (2016).
- 45 M. M. Kerrigan, J. P. Klesko, S. M. Rupich, C. L. Dezelah, R. K. Kanjolia, Y. J. Chabal, and C. H. Winter, J. Chem. Phys. 146 , 052813 (2017).
- 47 J. Zhao, M. Konh, and A. Teplyakov, Appl. Surf. Sci. 455 , 438 (2018).
- 46 J. K.-C. Chen, T. Kim, N. D. Altieri, E. Chen, and J. P. Chang, J. Vac. Sci. Technol. A 35 , 031304 (2017).
- 48 L. P. Méndez De Leo, L. Pirolli, and A. V. Teplyakov, J. Phys. Chem. B 110 , 14337 (2006).
- 50 S. Kondati Natarajan and S. D. Elliott, Chem. Mater. 30 , 5912 (2018).
- 49 L. Li-Jung, T. Chih-Pin, C.-W. Soong, J.-H. Chen, S.-H. Wang, and S.-H. Chang, ' Fluorine contamination control in semiconductor manufacturing process, ' U.S. patent application 20170352559 (2017). https://www.freepatentsonline.com/y2017/ 0352559.html.
- 51 S. Kondati Natarajan, M. Nolan, P. Theofanis, C. Mokhtarzadeh, and S. B. Clendenning, ACS Appl. Mater. Interfaces 12 , 36670 (2020).
- 53 R. C. Longo, A. Ranjan, and P. L. G. Ventzek, ACS Appl. Nano Mater. 3 , 5189 (2020).
- 52 R. Mullins, S. Kondati Natarajan, S. D. Elliott, and M. Nolan, Chem. Mater. 32 , 3414 (2020).
- 54 A. H. Basher, I. Hamada, and S. Hamaguchi, Jpn. J. Appl. Phys. 59 , 090905 (2020).
- 56 J. Kwon, M. Saly, M. D. Halls, R. K. Kanjolia, and Y. J. Chabal, Chem. Mater. 24 , 1025 (2012).
- 55 A. H. Basher, M. Krsti ć , T. Takeuchi, M. Isobe, T. Ito, M. Kiuchi, K. Karahashi, W. Wenzel, and S. Hamaguchi, J. Vac. Sci. Technol. A 38 , 022610 (2020).
- 57 T. Pugh, S. D. Cosham, J. A. Hamilton, A. J. Kingsley, and A. L. Johnson, Inorg. Chem. 52 , 13719 (2013).
- 59 P. Blochl, Phys. Rev. B 50 , 17953 (1994).
- 58 G. Kresse and J. Furthmuller, Phys. Rev. B 54 , 11169 (1996).
- 60 G. Kresse and D. Joubert, Phys. Rev. B 59 , 1758 (1999).
- 62 S. Grimme, J. Antony, S. Ehrlich, and H. Krieg, J. Chem. Phys. 132 , 154104 (2010).
- 61 J. P. Perdew, K. Burke, and M. Ernzerhof, Phys. Rev. Lett. 77 , 3865 (1996).
- 63 G. Henkelman and H. Jonsson, J. Chem. Phys. 113 , 9978 (2000).
- 65 G. Henkelman, A. Arnaldsson, and H. Jonsson, Comput. Mater. Sci. 36 , 354 (2006).
- 64 G. Henkelman, B. P. Uberuaga, and H. Jonsson, J. Chem. Phys. 113 , 9901 (2000).
- 66 R. F. Bader, Chem. Rev. 91 , 893 (1991).
- 68 M. Xu, P. Xiao, S. Stauffer, J. Song, G. Henkelman, and J. B. Goodenough, Chem. Mater. 26 , 3089 (2014).
- 67 H. Raebiger, S. Lany, and A. Zunger, Nature 453 , 763 (2008).
- 69 K. Persson, ' Materials data on Co (SG:194) by materials project ' (2016), see: https://materialsproject.org/materials/mp-54/; accessed 11 November 2019.
- 71 P. Janthon, S. Luo, S. M. Kozlov, F. Vines, J. Limtrakul, D. G. Truhlar, and F. Illas, J. Chem. Theor. Comput. 10 , 3832 (2014).
- 70 C. Kittel, Introduction to Solid State Physics (Wiley, New York, 2004).
- 72 A. Togo and I. Tanaka, Scr. Mater. 108 , 1 (2015).
- 74 D. Nicholls, The Chemistry of Iron, Cobalt and Nickel: Comprehensive Inorganic Chemistry (Elsevier, New York, 2013), Vol. 24.
- 73 ' TURBOMOLE V6.2 2010, a development of University of Karlsruhe and Forschungszentrum Karlsruhe GmbH, 1989-2007, TURBOMOLE GmbH, since 2007 ' see: http://www.turbomole.com last; accessed 27 November 2019.
- 75 G. K. K. Gunasooriya, A. P. van Bavel, H. P. Kuipers, and M. Saeys, Surf. Sci. 642 , L6 (2015).
- 76 R. Gopalakrishnan and B. Viswanathan, Surf. Technol. 23 , 173 (1984).

<!-- image -->

- 77 C. J. Weststrate, I. M. Ciobîca, /uniF6CA J. van de Loosdrecht, and J. W. Niemantsverdriet, J. Phys. Chem. C 120 , 29210 (2016).
- 79 K.-H. Ernst, E. Schwarz, and K. Christmann, J. Chem. Phys. 101 , 5388 (1994).
- 78 L. Nykänen and K. Honkala, J. Phys. Chem. C 115 , 9578 (2011).
- 80 M. Bridge, C. Comrie, and R. Lambert, J. Catal. 58 , 28 (1979).
- 81 J. J. Sims, C. A. Ould Hamou, R. Réocreux, C. Michel, and J. B. Giorgi, J. Phys. Chem. C 122 , 20279 (2018).

82 See the supplementary material at http://dx.doi.org/10.1116/6.0000804 for S1: Bader charge analysis, S2: Co bulk and surface models, S3: Reaction energies without CO residue, S4: Proposed ALE cycle for butyne+CO, silane+CO and TMS+CO, and S5: MD and CI-NEB analysis of propene dissociation.