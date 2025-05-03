<!-- image -->

<!-- image -->

www.acsami.org

<!-- image -->

## Mechanism of Thermal Atomic Layer Etch of W Metal Using Sequential Oxidation and Chlorination: A First-Principles Study

Suresh Kondati Natarajan, * Michael Nolan, Patrick Theofanis, Charles Mokhtarzadeh, and Scott B. Clendenning

<!-- image -->

Cite This: ACS Appl. Mater. Interfaces 2020, 12, 36670 -36680

<!-- image -->

## ACCESS

Metrics &amp; More

Article Recommendations

*

<!-- image -->

Supporting Information

<!-- image -->

ABSTRACT: Thermal atomic layer etch (ALE) of W metal can be achieved by sequential self-limiting oxidation and chlorination reactions at elevated temperatures. In this paper, we analyze the reaction mechanisms of W ALE using the /uniFB01 rst-principles simulation. We show that oxidizing agents such as O , 2 O3, and N2O can be used to produce a WO x surface layer in the /uniFB01 rst step of an ALE process with ozone being the most reactive. While the oxidation pulse on clean W is very exergonic, our study suggests that runaway oxidation of W is not thermodynamically favorable. In the second ALE pulse, WCl 6 and Cl2 remove the

<!-- image -->

oxidized surface W atoms by the formation of volatile tungsten oxychloride (W O Cl ) species. In this pulse, each adsorbed WCl x y z 6 molecule was found to remove one surface W atom with a moderate energy cost. Our calculations further show that the desorption of the additional etch products is endothermic by up to 4.7 eV. Our /uniFB01 ndings are consistent with the high temperatures needed to produce ALE in experiments. In total, our quantum chemical calculations have identi /uniFB01 ed the lowest energy pathways for ALE of tungsten metal along with the most likely etch products, and these /uniFB01 ndings may help guide the development of improved etch reagents.

KEYWORDS: atomic layer etching, transistor contacts, density functional theory, self-limiting reaction, atomistic simulations, /uniFB01 rst principles

## 1. INTRODUCTION

Atomic layer etch (ALE) processing has gained considerable attention in recent years within the semiconductor industry. 1 -4 The continued scaling of semiconductor devices demands the use of ever-thinner and higher-performing materials, which drives the development of gentle etch process technologies with atomic-level precision and high degrees of selectivity toward surrounding materials. ALE shares many similarities with the well-known atomic layer deposition (ALD), widely used in the semiconductor industry, and can be considered as the reverse of ALD. ALE permits the removal of thin /uniFB01 lms layer by layer exploiting atomic-scale precision inherent in the method using sequential and self-limiting surface reactions, 1 -3,5 -7 similar to ALD. Currently used ALE processes are anisotropic using directional high energy ion bombardment to drive the removal of the modi /uniFB01 ed surface layers. 2,8 On the other hand, a thermal ALE process relies on temperature and thermochemically favorable reactions to drive the removal of surface species. 9 There are a multitude of examples for thermal ALE of various materials, including oxides (HfO2, 3,7,10,11 ZrO2, 3,11 SiO2, 12 WO3, 13 ZnO, 14 and Al2 O3 9,11,15 -18 ), nitrides (including AlN, 19 GaN, 20 and TiN 21,22 ), /uniFB02 uorides (e.g., AlF3 23 ), and some work on W. 13,24 -26 Other ALE techniques include plasma ALE of SiO2, 27,28 ZnO, 29 and GaN, 30,31 and infrared annealing ALE of Si N4. 3 32 Despite this e /uniFB00 ort, the

<!-- image -->

atomistic details of the mechanism of thermal ALE processes are still not fully understood.

Tungsten, because of its low resistivity, resistance to electromigration, and ease of thin /uniFB01 lm growth by atomic layer and chemical vapor deposition, is often used in source/ drain contacts in CMOS devices. 33 Unlike ALD processes for W, which have received considerable attention, 34 -42 the utility of a complementary W atomic layer etch process has only recently emerged. 13,24 -26,43 Due to the continued scaling of critical dimensions in next-generation semiconductor devices and the incorporation of a more varied material palette in accordance with Moore s law, the need for novel digital etch ' methods to enable the precise removal of thin /uniFB01 lm materials is of extreme importance. 2,44

While there are anisotropic W ALE processing methodologies available, 45 isotropic thermal ALE techniques are required to perform conformal etch in high aspect ratio structures. Indeed, progress toward the isotropic thermal ALE of metallic W has been reported by the groups of George and

Received:

April 10, 2020

Accepted:

July 15, 2020

Published:

July 15, 2020

<!-- image -->

This is an open access article published under a Creative Commons Attribution (CC-BY) License, which permits unrestricted use, distribution and reproduction in any medium, provided the author and source are cited.

Parsons. The work reported by George et al. 13 has shown the quasi-ALE of metallic W via a conversion etch mechanism utilizing ozone (O3), BCl3, and anhydrous HF vapor. In this system, ozone was used to oxidize the W surface to WO3 in a di /uniFB00 usion-limited process, which then reacts with BCl3 to generate a volatile etch product in the form of WO Cl x y while tandemly generating a B2O3 surface layer, which is then susceptible to self-limiting etch by HF. Parsons and coworkers 24 have recently reported the ALE process of W with sequential use of O2 plasma or O3 and WF6. The oxidizing plasma produces a di /uniFB00 usion-limited WO3 surface layer, which can be removed by exposure to WF6 yielding WO2F2 as a volatile etch byproduct. They have also reported results on an oxidation plus WCl6-based W ALE process 25,26 in which they used a thermodynamic analysis to rationalize the experimental data. Despite these recent advances in atomic layer etch, however, mechanistic insight into the ALE processes remains limited. Computational investigations of a thermal ALE process for metal oxides with Al O 2 3 as an example have been reported previously, 46 but a similar investigation for metal ALE is lacking in the literature. This is due to an abundance of reactive transient species and etch products in a given ALE cycle and the di /uniFB03 culties related to in situ metrologies needed to identify and quantify these intermediates and products. Accordingly, to enable the rapid development of such processes, it is imperative that a mechanistic understanding of W ALE be established.

Herein, we report a /uniFB01 rst-principles computational study using density functional theory (DFT) to explore an oxidation/chlorination thermal ALE mechanism for W metal. In this study, the nature of the surface oxidation step to produce a WO x layer on tungsten is investigated using O , O , 2 3 and N2O as oxidants to uncover potential routes toward selflimiting oxidation of the W surface. Second, WCl6 and Cl2 were examined as potential etch reagents to generate volatile WO Cl etch species. Spin-polarized DFT coupled with density x y functional perturbation theory (DFPT) for a thermochemical analysis 47 were used to address self-limiting versus continuous etching pathways. At the same time, ground state spin polarized DFT was used to calculate the energies of surface species along several proposed reaction pathways. From these results, a full atomic layer etch chemical pathway for W metal can be mapped yielding a feasible reaction mechanism featuring sequential oxidation and chlorination steps.

## 2. COMPUTATIONAL SETUP

All calculations reported in this paper are based on spinpolarized DFT using VASP v5.4. 48 Core electrons are represented by projector augmented wave (PAW) potentials, 49,50 and valence electrons are treated explicitly by expanding their wave functions in a plane wave basis set with an energy cuto /uniFB00 of 400 eV. The exchange and correlation (XC) contributions are approximated by the generalized gradient approximation (GGA) using the Perdew -Burke -Ernzerhof (PBE) functional. 51 The total energies and forces of the geometries are converged within 1 × 10 -4 eV and -0.02 eV/Å, respectively. Methfessel -Paxton /uniFB01 rst-order smearing with 0.1 eV broadening is used for the scf calculations. The e /uniFB00 ect of dispersion correction on the structure and energies of bulk and surface geometries was found to be insigni /uniFB01 cant for this system, and thus dispersion corrections are not included (see section S0 of the Supporting Information).

The reported reaction free energies are computed as follows:

$$\mathfrak { e } \quad \Delta G = \Delta H - T \Delta S + R T \ln ( Q )$$

$$\text{is} \quad \Delta H = \Delta E + \Delta Z P E + \Delta W ( T )$$

$$\underset { \text{le} } { o } \quad \ Q = \prod p _ { \text{products} } ^ { \mu } / \prod p _ { \text{reactants} } ^ { \mu }$$

Here, Δ G , Δ H , and Δ S correspond to reaction free energy, reaction enthalpy, and reaction entropy, respectively. Δ E , Δ ZPE, and Δ W T ( ) refer to the electronic reaction energy at 0 K, zero point energy change, and temperature-dependent enthalpy change, respectively. Q is the reaction quotient used to include reactant and product pressures. A reactant pressure of 0.2 Torr and a product pressure of 0.01 Torr are used for the reported free energy calculations (see section S7 of the Supporting Information for other pressure combinations). Pressure contributions to the free energy are included only for the gas phase species. R and μ are the gas constant and stoichiometric coe /uniFB03 cient, respectively. The H and S values of the bulk and surface geometries are computed using the Phonopy code, 52 which requires accurate force constants obtained from DFPT calculations in VASP with a strict energy convergence threshold of 1.0 × 10 -08 eV. However, for convenience, the H and S values for gas phase molecules are obtained from the Turbomole package version 6.2 53 using the PBE XC functional and the def-TZVPP basis set.

W has a BCC crystal structure 54 with a calculated lattice constant of 3.17 Å, which agrees with the experimental value of 3.16 Å. 55 The cohesive energy of W is 9.1 eV/atom, which compares well to the experimental value of 8.9 eV/atom. 56 For the bulk W calculation, a 12 × 12 × 12 Monkhorst-Pack Kpoint sampling mesh is used and the lattice constant is obtained by simultaneously relaxing the ionic positions, cell shape, and cell volume at a larger plane wave energy cuto /uniFB00 of 550 eV. For the surface calculations, we have chosen the (2 × 3) supercell of a 10.8 Å thick stepped W(3 1 0) surface that has a computed surface energy of 3.77 J/m . The high index 2 high energy W stepped surface was chosen so as to maximize reactivity to incoming reagents as compared to the /uniFB02 at, less reactive low index surfaces. This metal slab consists of six W bilayers with 12 atoms each (72 W atoms in total) with a surface area of 0.955 nm . A vacuum of 19 Å separates the two 2 surfaces of the slab along the surface normal direction. A 3 × 3 × 1 Monkhorst-Pack K-point sampling mesh is used for all surface calculations to account for the supercell size used in this study. Atomistic models of bulk W and W(3 1 0) surface are shown in Figure S1 of the Supporting Information.

Tungsten sites are 8-fold coordinated in the bulk due to the BCC crystal structure. Each bulk W atom has six valence electrons shared between eight neighbors; therefore, threefourths of an electron is contributed to each metallic W W -bond. In the (2 × 3) supercell of W(3 1 0), there are 12 surface W atoms of which 6 are 4-fold coordinated and the other 6 are 6-fold coordinated. This amounts to 27 unpaired electrons on the surface. Therefore, we adsorbed 14 O atoms (coverage of 14.7 O/nm ) per supercell to the bare surface to 2 represent an oxidized W surface region, which is computationally tractable. The degree of oxidation will depend on processing conditions (Section 3.2), but this provides a reasonable model of partially oxidized W for our analysis. We considered di /uniFB00 erent arrangements of O species on the surface and relaxed the geometries (see Figure S2 of the Supporting Information). The most stable WO x structure we have found is shown in Figure 1a,b. This geometry represents

Figure 1. (a) Top and (b) side views of the most stable O-covered W(3 1 0) surface. The blue region indicates the atoms used in the DFPT calculation. The top W atoms coordinated by more than two O atoms, highlighted in the red region, are lifted out of their lattice positions due to the formation of W -O bonds. The color coding is as follows: W = gray, O = red.

<!-- image -->

<!-- image -->

the partially oxidized W surface that is present after the /uniFB01 rst ALE (oxidation) pulse. From Figure 1a,b, we /uniFB01 nd that the O atoms prefer to adsorb at the bridge and 3-fold sites on the surface. Moreover, the surface W -O bonds would weaken the underlying W W bonds, which is evident -from the out-oflattice positions of the surface W atoms highlighted in red.

## 3. RESULTS

3.1. Volatile Products of Interest. The proposed W-etch species, which originate from the surface for this ALE process, have been determined to be either WOCl4 or WO2Cl2 24 -26 depending on the etch gas stoichiometry. To etch a single atom of W from the surface (Ws) with a single molecule of WCl6, the incoming WCl6 molecule must react with the surface to generate a minimum of two volatile W species in the form of WOCl4 or WO2Cl2. In order to maintain proper ' bookkeeping ' of volatile species, it is important to note that the /uniFB01 rst volatile W species corresponds to the W atom originating from the incoming WCl6 molecule. Due to the origin of this W atom from the reactant gas, the resulting volatile W species (either WOCl4 or WO2Cl2) is considered a non-Ws etch species (NES), while the second W-containing species would be designated the /uniFB01 rst-Ws etch species (FES). In the most favorable case, one incoming WCl 6 could react with the surface to form 3 equiv of WO2Cl2, thereby e /uniFB00 ectively etching two surface W atoms. The /uniFB01 rst molecule of WO2Cl2 would be a NES, while the /uniFB01 rst and second W species that originate from the surface would be considered the /uniFB01 rst-Ws etch species (FES) and second-Ws etch species (SES), respectively. This nomenclature is used throughout the remainder of this paper. Alternatively, a second mechanism utilizing 2 equiv of WCl 6 to remove one surface W atom resulting in the formation three WOCl4 species is also considered. The /uniFB01 rst two W species, which originate from the incoming WCl6 molecule, would be considered NESs, while the last W species, which originates from the surface, would be a FES.

If we consider Cl2 as an etch gas, each molecule of Cl 2 has the potential to remove an oxidized surface W atom in the form of WO2Cl2 (a FES). Likewise, 2 equiv of Cl 2 could be used to form 1 equiv of WOCl4 originated from the surface (a FES). A schematic showing the described volatile byproducts is shown in Figure S3 of the Supporting Information. It is important to note that the formation energies for these proposed volatile species were very similar (WOCl : 4 -7.1 eV; WO2Cl2: -7.3 eV) using bulk W, O2, and Cl2 molecules as a reference. However, their formation and desorption energies with respect to a reactive surface di /uniFB00 er and will be addressed later in this text. We /uniFB01 rst study how the oxidizing agents interact with the bare surface to form the WO x surface shown in Figure 1a and then examine how WCl6 and Cl2 molecules interact with this oxidized W surface.

3.2. Mechanisms in the Oxidation Pulse. In the /uniFB01 rst ALE pulse, we modify the W surface by oxidizing it with O2, O3, and N2O. N2O interaction with the bare W surface is the weakest when compared to O2 and O3; therefore, the discussion on N2O -W interaction is moved to section S2 of the Supporting Information. Oxidation of W using O2 and O3 has been studied quite extensively, and it is known that bulk oxidation of W in an O 2 atmosphere is appreciable only above 500 ° C, which is well above the ALE processing temperature. 57 -59 An account on the temperature dependence of the oxidation of W using O2 and O3 relevant to atomic layer etching has been discussed by George and co-workers. 13 From the N-E analysis 47 given in section S3 of the Supporting Information, comparing the continuous and self-limiting reaction models of the /uniFB01 rst ALE pulse, we predicted a minimum (thermodynamic) energy barrier of about 2.3 eV to cause bulk oxidation. We could expect that the predicted thermodynamic barrier to be breached below 800 ° C as W oxide, formed on the surface, is reported to become volatile beyond that temperature. 60 Warren et al. 61 found that a 1 h exposure of polycrystalline W to O 2 below 200 ° C resulted in the formation of 1.0 -1.6 nm of WO3. Therefore, by keeping the temperature below 200 ° C or by controlling the exposure time and partial pressure of the reactants, a thin layer of oxide relevant for ALE can be formed. The temperature needed for the thermal ALE process will also be in /uniFB02 uenced by the activation energies required in the second ALE pulse.

On the clean W(3 1 0) surface, both O2 and O3 molecules dissociate spontaneously on adsorption and form surface W -O bonds as shown in Figure 1a,b by releasing -7.24 and -12.13 eV per adsorbed molecule, respectively. For comparison, the most favorable binding energy of a N O molecule is 2 -5.81 eV. O3 is a stronger oxidant than the O 2 molecule. Since the adsorption geometries and binding sites are similar for both molecules, we will only examine the adsorption of the O 2 molecule in detail. We considered di /uniFB00 erent binding sites for the dissociated O atoms on the W surface as shown in Figure 2a -e. The binding energies and shortest W -O bond distances from these geometries are listed in Table 1. The computed binding energy per O atom is in the range of -3.30 to -4.47 eV for on-surface adsorption, with the bridge sites being the most favorable followed by the atop, 3-fold, and 4-fold sites. The adsorption at subsurface sites is about 3 eV less favorable than the most favorable bridge site (Figure 2f). Clearly, at this coverage of 2 O/nm 2 , di /uniFB00 usion to subsurface sites is not as favorable as on-surface adsorption. The O atom in the subsurface site is at least 1.9 Å away from the neighboring Watoms. The shortest W -O bond length is found at the atop site followed by the bridge, subsurface, 3-fold, and 4-fold sites. Comparing with the most favorable oxygen-covered surface model shown in Figure 1a, we note that the O atoms are predominantly adsorbed at the bridge sites.

In this section, we saw the various adsorption sites preferred by the dissociated O atoms and that the O2 molecule indeed dissociates spontaneously. We have prepared the saturated surface models as described in the computational section. Any additional O2 molecule introduced in the system beyond a

Figure 2. The top and side views of dissociated O 2 molecules on the W(3 1 0) surface at atop sites, bridge sites, alternate bridge sites, 3fold sites, 4-fold sites, and subsurface sites are shown in (a), (b), (c), (d), (e), and (f), respectively. The color coding is as follows: W = gray, O = red.

<!-- image -->

Table 1. Binding Energies and Minimum W -O Bond Distance for O2 adsorption on the W(3 1 0) Surface a

| geometry   | E bind (eV/O)   | d (W - O) (Å)   |
|------------|-----------------|-----------------|
| atop       | - 3.80          | 1.7             |
| bridge     | - 4.47          | 1.9             |
| bridge2    | - 3.99          | 1.9             |
| 3-fold     | - 3.31          | 2.0             |
| 4-fold     | - 3.30          | 2.1             |
| subsurface | - 1.45          | 1.7 (1.9)       |

a For the subsurface geometry, the distance in parentheses correspond to the O atom in the subsurface site.

single O2 molecule described in this section will indeed dissociate (in an exoergic reaction) until the saturated surface is formed. Thus, the intermediate steps do not need to be discussed.

3.3. Mechanisms in the Chlorination Pulse. The primary mechanism of chlorination of the oxidized W surface by WCl6 is the dissociation of the molecule and subsequent exchange of Cl ligands from the reagent to the substrate, which requires elevated temperatures. These are complex dynamical processes unlike the simple dissociative adsorption of the reactant molecules in the /uniFB01 rst pulse. Before investigating the chlorination of the oxidized W surface, we /uniFB01 rst explored the possibility of uncontrolled etching of W metal by WCl6 and Cl2 . These results are discussed in detail in section S4 of the Supporting Information. The exposure of WCl6 and Cl2 on the bare W surface did not result in continuous etching of the substrate even at elevated temperatures. Deposition of W, when WCl6 is used, is also not thermodynamically favorable beyond room temperature.

WCl6 being an octahedral molecule interacts weakly with the O-covered W surface due to the net electrostatic repulsion between the O and Cl species. As a result of this net electrostatic repulsion, WCl 6 does not dissociate spontaneously after initial adsorption at low temperatures due to the presence of the kinetic energy barrier. Dissociation of the WCl6 molecule would need elevated temperatures to excite the W Cl bonds or O-free regions on the surface as WCl6 -readily dissociates on the bare W surface. Experiments suggest that a temperature of at least 200 ° C is needed for the ALE process to take place, 25,26 which means that the WCl6 molecules would have dissociated at this temperature. A short 2.5 ps duration ab initio molecular dynamics (MD) simulation at 800 K of the WO surface with two physisorbed WCl6 x molecules revealed a spontaneous donation of one of the Cl ligands by each of the reactant molecules to the surface W atoms as shown in Figure 3. A high temperature of 800 K is used to accelerate the MD simulation; otherwise, we would have needed a signi /uniFB01 cantly longer simulation time to observe this reaction step at lower temperatures.

The W atom in the WCl6 molecule is the donor W atom (Wd), while the acceptor W (Wa) is one of the oxidized surface W atoms. In the /uniFB01 rst 300 steps (750 fs) of the simulation, we can identify the high amplitude vibrational mode of the Cl atom from the /uniFB02 uctuations in the interatomic W d -Cl distances (see Figure 3). Moreover, an increase in the W d -Cl distance correlates with a decrease in the Wa -Cl distance. This large amplitude motion, a byproduct of the thermal energy contribution, results in the dissociation of one of the Cl ligands from the WCl6 molecule. After the crossover point at 837 fs (step 335), the dissociated Cl ligand did not attempt to bind back to the Wd atom, which is evident from the continuous increase in d (Wd -Cl) value beyond 1.25 ps (step 500). The inset graph in Figure 3 shows the distances and single-point energies of the system during the dissociation of WCl6. We see an energy change of 800 meV right before the dissociation takes place; this includes contribution from the motion of surface atoms as well. The dissociation of the Cl ligand from the second WCl6 molecule was similar to the above observation.

To compute the entire dissociation pathway, the formation of non-volatile species are considered when WCl 6 is adsorbed either as an intact or dissociated molecule, for which the geometries are shown in Figure 4A -E. While there are very many possibilities to arrange an intact and dissociated WCl6 molecule on the O-covered W surface, it is not practical to study them all; therefore, we have considered these /uniFB01 ve minimum geometries as a representative for further discussion. In Figure 4, geometry A shows a weak interaction between the WCl6 molecule and the O-covered W surface with a binding energy of just -0.09 eV. Geometry B shows the state where the weakly adsorbed WCl6 dissociates and a Cl ligand is adsorbed to a surface W atom. This reaction is not spontaneous and costs 0.48 eV. The potential energy surface cut along the pathway, obtained by a linear interpolation of the position of the dissociated Cl ligand from geometry A to B, is computed, and the computed dissociation barrier is 0.52 eV (graph and geometries in Figure S9 of the Supporting Information). The reverse barrier for the reformation of WCl6 is just 0.04 eV. However, this reaction is hindered by the di /uniFB00 usion of the WCl5 fragment into the vacuum immediately after the dissociation. It is possible that all impinged WCl6 molecules follow this process and chlorinates the WO surface without depositing x any W as WCl5. However, the WCl5 fragment in the gas phase can further adsorb on the surface by forming W -O bonds as shown in geometry C (WCl5 adsorbed), which is energetically favorable and releases -1.32 eV of energy in comparison to geometry B. Dissociation of a Cl ligand from the adsorbed

Figure 3. Snapshots (X1 -X3) from MD simulation of two WCl6 molecules adsorbed on the WO x surface along with the evolution of distances between the dissociated Cl atom and the donor/acceptor W atoms. The inset graph shows the distances and single-point DFT energies of the snapshots (relative to that of snapshot 322, X1) during the bond dissociation. The color coding is as follows: W = gray, O = red, and Cl = green.

<!-- image -->

Figure 4. Relaxed geometries showing the non-volatile (dissociative) adsorption of WCl6 on the O-covered W surface. The values in red indicate an energy cost, and the values in green indicate a gain in energy at 0 K. The values above (or left of) the arrow are the energy change with respect to the preceding con /uniFB01 guration, while the values below (or right of) the arrow are the energy change with respect to geometry A (cumulative energy change). In geometry A, WCl6 is intact, and in geometries B, C, D, and E, the molecule is in the dissociated state. The reference gas phase molecule used for the binding energy calculation is WCl . 6

<!-- image -->

Cl ligands from surface-adsorbed WCl5 has a large energy penalty. Dissociation of surface-bound WCl 5 is unfavorable at 0 K due to enthalpic loss, which will be compensated by entropic gain at elevated temperatures due to the formation of the volatile species (WOCl4). Another possibility for the WCl5 fragment in geometry B is to form geometry E by donating another Cl ligand in the gas phase to the surface and adsorb as WCl4 by forming a W -Obond (WCl4 hop). This results in the formation of WOCl4, one of the proposed volatile species, which spontaneously desorbs from the surface, as shown in geometry E. Once again, this step will see an entropic gain at elevated temperatures and compensate the enthalpic loss reported at 0 K. Only geometries A and C have favorable (negative) binding energies at 0 K.

WCl5 fragment in geometry C to form geometry D has an energy cost of 1.56 eV, suggesting that further dissociation of

Beginning from the most favorable non-volatile adsorption geometry C, step-by-step desorption of the proposed volatile etch products and their corresponding energetics are investigated as shown in Figure 5. Three cases in which the sequential removal of 1 WOCl4 + 1 WO2Cl2, 1 WO2Cl2 + 1 WOCl4, and 3 WO2Cl2 are considered. Note that the /uniFB01 rst volatile product removed in all three cases is the NES followed by FES and SES as discussed earlier. In the /uniFB01 rst case, WOCl4 was removed as the NES, with a desorption energy of 0.44 eV. Due to entropic gain, this step is favorable ( -1.73 eV gain) at 500 K. This however does not count toward etching of the

Figure 5. Energy requirements for the removal of volatile species from geometry C and E from Figure 4. The values in red indicate a moderate energy cost, and the values in green indicate a gain in energy. The values above the arrow are the desorption energies of the respective volatile species, while the values below are the free energy change of desorption at 500 K. The desorbed molecules are either WOCl4 or WO2Cl2.

<!-- image -->

substrate since the W atom removed is not a surface atom. Following this step, WO2Cl2 is removed as the FES with an additional desorption energy of 2.57 eV (which is also not favorable at 500 K). In the second case, WO2Cl2 is removed /uniFB01 rst as the NES with an energy cost of 0.57 eV, which is 0.13 eV more than WOCl4 in the /uniFB01 rst pathway. This is because a second W -O bond must be broken in forming WO2Cl2. The subsequent removal of WOCl4 in this sequence costs 2.72 eV of energy. We note that WOCl4 o /uniFB00 ers more entropy than WO2Cl2 due to the presence of an additional ligand, and it is evident from the reduced free energy gain in the /uniFB01 rst step ( -1.37 eV for WO2Cl2 against -1.73 eV for WOCl4) and reduced free energy loss in the second step (0.54 eV for WOCl4 against 0.64 eV for WO2Cl2) when compared with the previous case. In these two cases, the removal of the FES is not favorable even at 500 K. However, the cumulative enthalpic gain in the earlier steps of the ALE cycle could o /uniFB00 set this energy cost.

In the third case, three WO2Cl2 molecules were removed sequentially. While the removal of the NES costs 0.57 eV, the removal of the FES and SES becomes increasingly expensive with energy costs of 1.00 and 4.42 eV, respectively. In contrast to the /uniFB01 rst two cases, the removal of the FES in this case is favorable at 500 K ( -0.93 eV); however, the removal of the SES is not. This is due to the fact that a considerable number of surface W O and W --W bonds have to be broken to remove the second WO2Cl2 species. Similarly, from the minimum geometry E, the removal of the pre-formed nonWs etch WOCl4 is favorable by -0.29 eV. Further removal of the etch product WO2Cl2 costs an energy of 1.0 eV, but this step is entropically favorable at 500 K in contrast to the /uniFB01 rst case from geometry C. The free energy values for other reactant and product pressures for comparison is given in section S7 of the Supporting Information. It is to be noted that the in /uniFB02 uence of the reactant pressure to the free energy is very small compared to the contributions from enthalpy and entropy in this case.

From the above analysis, we /uniFB01 nd that each WCl6 molecule is capable of removing up to two surface W atoms and six surface

O atoms in the best case scenario (3 WO2Cl2). However, the removal of the W atoms from the surface costs anywhere between 1.00 and 4.42 eV. We also /uniFB01 nd that the removal of WOCl4 as a non-Ws etch product costs less energy when compared to WO2Cl2 since the former removed only one surface-bound O atom whereas the latter removes two, which costs more energy. This is further supported by the observation that, whenever a WOCl4 species is formed on the surface, it readily desorbs from the surface. In contrast, WO2Cl2 is bound to the surface primarily as a result of the strong W W and W --O bonds. Therefore, WO2Cl2 should become volatile only at elevated temperatures.

To consider other combinations of etch products, 2 WCl6 adsorption on the O-covered W surface is studied as shown in Figure 6. Similar to the low coverage case, the interaction

Figure 6. Minimum energy geometries showing the non-volatile adsorption of 2 WCl6 on the O-covered W surface and energies needed to remove volatile species from them. The values in red indicate energy loss, and the values in green indicate energy gain. The values above the arrow are the desorption energies of the respective volatile species, while the values below are the free energy change of desorption at 500 K.

<!-- image -->

between WCl6 and the substrate was weak with a binding energy of just -0.07 eV/WCl6 (geometry A). Dissociation of the adsorbed WCl6 molecules by donating one Cl atom to the surface (geometry B) costs about 0.27 eV/WCl6. Keeping geometry B as the starting point, we computed the desorption energies for the removal of three consecutive WOCl4 species. The removal of the /uniFB01 rst two volatile species (NESs) is exoergic, while the removal of the third WOCl 4 (FEP) has a cost of 1.08 eV. The removal of the above three volatile products was favorable at 500 K. In another desorption sequence, we studied the desorption of two consecutive WOCl4 as the NES followed by two WO2Cl2 as the FES and SES. While the removal of the /uniFB01 rst two WOCl4 species was essentially the same as in the previous case, the subsequent removal of the /uniFB01 rst WO2Cl2 species costs less energy compared to the energy cost for removal of WOCl4 in the other sequence. However, the removal of the second surface W atom in the form of WO2Cl2 has a huge energy penalty of 4.7 eV. We /uniFB01 nd that the removal of a surface atom as WOCl4 is not more energetically favorable than its removal as WO2Cl2, which is understandable as more surface W -O/W W bonds have to -be broken to form the former than the latter in this particular

Figure 7. Panel (A) shows a schematic representation of an idealized W ALE cycle. The energies of the individual steps are listed in Table 2. Atom color coding is as follows: W = gray, O = red, and Cl = green. Step 1 depicts the initial functionalization of the surface with the desired oxidant. Step 2 describes the purging of the excess oxidant from the reaction chamber. Step 3 describes the introduction of WCl , which exhibits no spontaneous 6 dissociation until elevated temperatures. Step 4 depicts the liberation of volatile WO Cl x y species as the most likely etch species. Step 5 in an idealized system results in the repassivation of the surface leading into the next cycle and is thus labeled as equivalent to step 1. Additional passivated surface post etch is shown in panel (B). WCl x terminated surface is discussed in detail in Figure 8.

<!-- image -->

case. On the other hand, it is more favorable to form WOCl 4 as a NES from the incoming WCl6 molecule when compared to WO2Cl2.

atures when compared to Cl2. Therefore, in the next section, we will discuss the full ALE cycle with WCl6 as the second pulse chemical.

Now, let us look at the chlorination pulse when Cl 2 is used as the gas phase reactant. Similar to WCl , Cl 6 2 did not adsorb strongly via dissociation at the O-rich region of the WO x surface. A binding energy of just -0.05 eV per Cl 2 molecule is obtained. A short MD simulation at 800 K also failed to capture Cl2 dissociation as the Cl2 molecule simply di /uniFB00 used away from the surface due to the repulsion between the Cl and surface O atoms. Therefore, we studied the dissociative adsorption of 1 and 2 Cl2 on the model WO x surface, which released an energy of -3.11 eV to -3.92 eV per adsorbed Cl2 . The corresponding geometries are schematically presented in section S8 of the Supporting Information. From the above structures, desorption energies of volatile species such as WO2Cl2 and WOCl4 are computed to be 1.33 and 0.73 eV, respectively. It is to be noted that there is no NES when Cl 2 is used in the chlorination pulse. Also, as mentioned earlier in Section 3.1, each Cl 2 molecule is capable of forming, at most, one etch product (WO2Cl2 as the FES), whereas two Cl2 molecules are needed to form one WOCl4 (as the FES) or two WO2Cl2 (as the FES and SES). On the bare W surface, Cl2 dissociates spontaneously at low temperatures (discussed in detail in section S4 of the Supporting Information). Homolytic dissociation of Cl2 is required on the WO surface so that x volatile species can be formed. Dissociation of Cl 2 in vacuum requires 3.1 eV, while the dissociation of one W -Cl bond from the WCl6 molecule in vacuum required a slightly lower 2.5 eV. Based on the above, WCl6 may dissociate at lower temper-

3.4. The Full Atomic Layer Etch Cycle. In this section, we discuss the full cycle of the W ALE process, with O , O , 2 3 and N2O as the s /uniFB01 rst pulse chemical and WCl6 as the second pulse chemical, which is summarized in Figure 7A. Steps 1, 2, 3, and 4 correspond to pulse-1, purge-1, pulse-2, and purge-2 of the W ALE cycle, respectively. Step 5 is also the step 1 of the second and subsequent ALE cycles, whereas steps 2, 3, and 4 are common for all ALE cycles. The /uniFB01 rst ALE pulse is the adsorption of the oxidizing agents (O , O , and N O). In the 2 3 2 oxidation step, step 1 of the /uniFB01 rst ALE cycle, energy is gained by the dissociative adsorption of the reactant molecules on the bare W surface. We will show later that subsequent ALE cycles do not start with a bare W surface but rather a WO Cl x y surface. We show in Table 2 and section S3 of the Supporting Information that this step realizes a signi /uniFB01 cant enthalpy gain by the formation of stable W O bonds, -but the associated entropic loss was comparatively too small to make the reaction unfavorable at ALE relevant temperatures.

An energy of -4.31 to -4.80 eV ( -3.61 to -4.63 eV at 500 K), depending on the /uniFB01 rst pulse reactant used, is gained per surface W atom in the supercell (W , note that there are 12 W s s in the supercell) in this step. This amounts to an energy of -3.69 to -4.11 eV released per O atom adsorbed. In step 2, unreacted reactant molecules are purged from the etch chamber along with any byproducts formed.

In step 3, the dissociative adsorption of WCl 6 is either mildly favorable energetically ( -0.08 eV/Ws) or costs energy (0.12

Table 2. Energy Requirements (Ranges with Most Favorable (MF) and Least Favorable (LF) Values in eV) for the Individual Steps of the ALE Cycle in Figure 7 a

|                       | Δ E (eV)   | Δ E (eV)   | Δ G (eV) 500 K   | Δ G (eV) 500 K   |     |
|-----------------------|------------|------------|------------------|------------------|-----|
| step                  | MF         | LF         | MF               | LF               | per |
| O 2 /O 3 /N 2 O pulse | - 4.80     | - 4.31     | - 4.63           | - 3.61           | W s |
| purge 1               | 0.00       | 0.00       | 0.00             | 0.00             | W s |
| WCl 6 pulse           | - 0.08     | 0.12       | 0.11             | 0.30             | W s |
|                       | - 4.88     | - 4.19     | - 4.52           | - 3.31           | W s |
| purge 2               | - 0.53     | 0.57       | - 2.70           | - 1.37           | NES |
|                       | 0.48       | 2.72       | - 1.45           | 0.64             | FES |
|                       | 4.42       | 4.74       | 2.48             | 2.80             | SES |

a Here, Ws refers to a surface W atom. NES, FES, and SES are acronyms for non-Ws etch, /uniFB01 rst-Ws etch, and second-Ws etch species, respectively. The values in bold refer to the cumulative values combining oxidation pulse and chlorination pulse. For the free energy values at 500 K, the contributions from surface models are not included as they were estimated to be less than 4% of the total value.

eV/Ws). Moreover, this step is endergonic at 500 K mainly due to the entropic loss. However, the cumulative energetic gain through steps 1 to 3 is still exoergic, -4.19 to -4.88 eV per Ws ( -3.31 to -4.52 eV per Ws at 500 K). We use the energy per Ws since it is convenient to compare to the energy required to desorb the etch products in the next step. As discussed earlier, we have also performed a short 2.5 ps MD study and observed spontaneous dissociation of the WCl6 molecule on the WO x surface at 800 K. We chose 800 K to accelerate the MD simulation. However, this process is also possible from simulations at temperatures close to the ALE relevant temperature, e.g., 500 K, provided long trajectories are computed, which are computationally expensive.

In step 4, the formation and desorption of the non-W s etch and Ws etch byproducts ( X number of WO2Cl2 and Y number of WOCl4) take place. The /uniFB01 rst product per incident WCl 6 is a NES, and depending on the stoichiometry of the byproduct, there could additionally be one (FES) or two (FES and SES) Ws etch species. We have determined the typical energy requirement for the removal of the volatile NES, FES, and SES as shown in Table 2. The NES required the least energy (sometimes this is exoergic) as evident from the negative free energies at 500 K. The removal of the FES requires between 0.48 and 2.72 eV, and it can even be spontaneous at higher temperatures (0.64 to -1.45 eV at 500 K) due to net entropic gain. However, the removal of a SES requires between 4.42 and 4.47 eV of energy and it is also not favorable at high temperatures. However, the cumulative enthalpic gain per surface W atom up to this point might compensate these energy requirements for the removal of the FES and the SES at elevated temperatures. Thus, the removal of the NES is spontaneous while the removal of the FES and the SES costs energy and is subject to free energy changes in the cycle, the latter more so than the former. Since we gain a free energy of -39.72 to -54.24 eV per supercell (12 W ) at 500 K from the s /uniFB01 rst three steps, the overall energy change for the entire cycle including the removal of NES, FES, and SES from a WCl6 molecule will still be favorable (negative free energy).

At this point, the second and subsequent ALE cycles will start from a surface that is potentially one of the four shown in Figure 7B, that is WO Cl , WCl , or x y y WO terminated or a x potentially bare W surface. The reason for this is that the surface geometry after the WCl6 pulse will be dependent on the process conditions and the reactions that take place in the second pulse and in the second purge steps. The W surface is not likely to be terminated with bare tungsten as this is only possible when all the adsorbed WCl6 species form volatile WO Cl x y species, thereby depleting the adsorbed Cl and all surface O atoms. WO x will only result if the WCl 6 molecules in the second pulse do not dissociatively react with the substrate and cause an etch delay, which is also not very probable. It is more likely that the surface will now be partially covered with Cl species (WCl ) x because the WCl6 and Cl2 molecules dissociate readily on the bare W surface, which is now exposed after volatile products are removed from the WO x surface, by releasing -4.5 and -5.9 eV, respectively. It is also possible that there are some O atoms remaining on the surface forming nonvolatile WO Cl x y species as suggested by Xie et al. 25,26 Our calculations also predict that the removal of the SES requires a very high energy, which indicate a O Cl x y termination of the W surface. Therefore, as subsequent ALE cycles proceed, the oxidizing agents will have to react with an (oxy)chloride termination of the W surface rather than a bare W surface and this may in /uniFB02 uence the overall etch rate. 25,26

To understand the potential impact of this, we studied a model system of six O 2 molecules per supercell interacting with a fully Cl-covered W surface that may be present after one etch cycle, as shown in Figure 8. When initially intact O 2 molecules are adsorbed on the Cl-covered W surface (Figure 8a), no spontaneous reaction is observed due to the repulsion between the Cl and O atoms. We note that O2 dissociates spontaneously on Cl-free regions on the W surface, though we cannot see that in our model because of the full surface passivation with Cl. We therefore examined two con /uniFB01 gurations

Figure 8. Interaction of O2 on the Cl-covered W surface, which is identi /uniFB01 ed as one of the possible surface terminations at the end of the ALE cycle in Figure 7. In case (a), six intact O2 molecules are adsorbed on the surface with 0 eV/O2. In (b) and (c), 12 O atoms (six dissociated O 2 molecules) are adsorbed close to surface W and close to Cl atoms with a release of -4.8 and -0.5 eV/O2, respectively. The color coding is as follows: W = gray, O = red, and Cl = green.

<!-- image -->

whereby dissociated O2 molecules are adsorbed on the Clcovered W surface (Figure 8b,c). In Figure 8b, the resulting O atoms are adsorbed close to the surface W atoms, which on relaxation resulted in the spontaneous formation of surfacebound WO2Cl2 species with a release of -2.4 eV per adsorbed O atom. In the second con /uniFB01 guration (Figure 8c), oxygen atoms are adsorbed close to the Cl atoms, and upon relaxation, we observe the spontaneous formation and desorption of oxychloride species such as ClO2, Cl2O2, and Cl3O2, with a gain of -1.0 eV/O. This suggests that the incoming O2 molecule in the second ALE cycle must /uniFB01 rst dissociate before adsorbing at the fully chlorinated surface in order to react with it. As mentioned earlier, this pre-dissociation of the O2 molecules is not needed when the Cl ligands are sparsely distributed on the surface.

## 4. CONCLUSIONS

A /uniFB01 rst-principles investigation of a thermal atomic layer etch process for metallic tungsten using sequential oxidation and chlorination is presented. O , O , and N O were examined as 2 3 2 the oxidizing agents to modify the oxidation state of the surface W atoms. WCl6 and Cl2 were examined as ligand exchange agents for the material removal pulse. The reactant molecules chosen for both ALE pulses meet the requirement of being stable in the gas phase at the ALE operating temperature. Runaway oxidation of W is possible when O2 and O3 are used in the /uniFB01 rst ALE pulse. However, a thin layer of WO x can be obtained by carefully controlling the reactant pressure, temperature, and exposure time. The most important aspect of the ALE process is the self-limiting nature of the reactions taking place in the two pulses. Qualitative predictions based on thermochemical analysis showed that bulk oxidation was hindered by thermodynamic barriers at ALE relevant temperatures and pressures. Similarly, spontaneous etching of W by WCl6 and Cl2 was predicted to be unfavorable, even though these molecules spontaneously react with the bare W surface.

The mechanisms of the dissociative adsorption of the oxidizing agents on the bare W surface were reported. Exposure to O2, O3, and N2O resulted in an O-covered surface with ozone being the most reactive chemical for the /uniFB01 rst pulse followed by O2 and N2O. To keep the computational e /uniFB00 ort tractable, we considered a monolayer oxidized surface model of W at the end of the /uniFB01 rst half ALE cycle. However, WCl6 molecules interacted weakly with the oxidized W surface due to net repulsion between the O and Cl atoms and also because of the kinetic barriers inhibiting the dissociation of WCl6 molecule. Thermal energy is required to dissociate the WCl6 molecule so that it can donate its Cl ligands to the surface leading to the formation of the target volatile species, primarily WOCl 4 and WO2Cl2. The incoming WCl6 molecule can form WOCl4 as a non-Ws etch species by exchanging two Cl ligands for one O atom from the surface. This also results in the formation of a WO Cl 2 2 species on the surface. The desorption of WO2Cl2 has a relatively higher energy cost as compared to WOCl4 due to the relatively high coordination of the W atom in surface-bound WO2Cl2. The other possibility for the incoming WCl6 molecule is to dissociate completely by donating all of the Cl ligands to the surface and form three WO2Cl2 molecules as volatile species. Therefore, each WCl6 molecule is capable of removing up to two surface W atoms with a maximum energy cost of 4.42 eV. The desorption of the /uniFB01 rst-Ws etch product costs between 0.48 and 2.72 eV, which is thermodynamically favorable in the overall energy cycle, whereas the desorption of the second etch product costs almost 5 eV and is unfavorable.

Due to the favorable reaction of WCl6 and Cl2 on the bare W surface, it will be covered with O and Cl ligands at the end of the /uniFB01 rst ALE pulse. In the second ALE cycle, the oxidizing agents must remove the Cl ligands /uniFB01 rst, either by forming volatile W oxychlorides or stable oxychloride chains, before accessing the surface W atoms, which might slow down the etch process. Computational investigations of such ALE processes provide the required understanding of the mechanism of etch reactions. Such understanding is vital to the design of new and robust ALE processes in the future.

## ■ ASSOCIATED CONTENT

## * s ı Supporting Information

The Supporting Information is available free of charge at https://pubs.acs.org/doi/10.1021/acsami.0c06628.

Atomic models of W bulk and surface, schematics of second ALE pulse, mechanism of N2O pulse, Natarajan -Elliott ' N-E ' analysis of the oxidation pulse, reaction of WCl6 and Cl2 on the bare W surface, dissociation pathway of WCl6, description of thermal ALE of metals, in /uniFB02 uence of reactant and product pressures, and Cl 2 in material removal pulse (PDF)

## ■ AUTHOR INFORMATION

## Corresponding Author

Suresh Kondati Natarajan -University College Cork, Tyndall National Institute, Cork T12 R5CP, Ireland; Department of Electrical Engineering and Automation, Aalto University, Espoo 02150, Finland; orcid.org/0000-0002-7018-5253; Email: suresh0807@gmail.com

## Authors

Michael Nolan -University College Cork, Tyndall National Institute, Cork T12 R5CP, Ireland; Nanotechnology and Integrated Bioengineering Centre, Ulster University, Co Antrim BT37 OQB, Northern Ireland; orcid.org/0000-0002-52248580

Corporation, Hillsboro, Oregon 97124, United States Charles Mokhtarzadeh -Intel Corporation, Hillsboro, Oregon 97124, United States Scott B. Clendenning -Intel Corporation, Hillsboro, Oregon 97124, United States

Patrick Theofanis -Intel

Complete contact information is available at: https://pubs.acs.org/10.1021/acsami.0c06628

## Notes

The authors declare no competing /uniFB01 nancial interest.

## ■ ACKNOWLEDGMENTS

Authors S.K.N. and M.N. thank Intel Corporation for funding. They also thank the Irish Centre for High-End Computing (project code: tiche081c) and Science Foundation Irelandfunded computing cluster at Tyndall for the computer time.

## ■ REFERENCES

(1) Oehrlein, G. S.; Metzler, D.; Li, C. Atomic Layer Etching at the Tipping Point: An Overview. ECS J. Solid State Sci. Technol. 2015 , 4 , N5041.

- (2) Kanarik, K. J.; Lill, T.; Hudson, E. A.; Sriraman, S.; Tan, S.; Marks, J.; Vahedi, V.; Gottscho, R. A. Overview of Atomic Layer Etching in the Semiconductor Industry. J. Vac. Sci. Technol., A 2015 , 33 , No. 020802.
- (3) Lee, Y.; Huffman, C.; George, S. M. Selectivity in Thermal Atomic Layer Etching Using Sequential, Self-Limiting Fluorination and Ligand-Exchange Reactions. Chem. Mater. 2016 , 28 , 7657 -7665.
- (4) Kanarik, K. J.; Tan, S.; Yang, W.; Kim, T.; Lill, T.; Kabansky, A.; Hudson, E. A.; Ohba, T.; Nojiri, K.; Yu, J.; Wise, R.; Berry, I. L.; Pan, Y.; Marks, J.; Gottscho, R. A. Predicting Synergy in Atomic Layer Etching. J. Vac. Sci. Technol., A 2017 , 35 , 05C302.
- (5) George, S. M.; Lee, Y. Prospects for Thermal Atomic Layer Etching Using Sequential, Self-Limiting Fluorination and LigandExchange Reactions. ACS Nano 2016 , 10 , 4889 -4894.
- (6) Yuan, G.; Wang, N.; Huang, S.; Liu, J. A Brief Overview of Atomic Layer Deposition and Etching in the Semiconductor Processing. 2016 17th International Conference on Electronic Packaging Technology (ICEPT) ; IEEE: 2016; pp 1365 -1368.
- (7) Lee, Y.; DuMont, J. W.; George, S. M. Atomic Layer Etching of HfO2 Using Sequential, Self-Limiting Thermal Reactions with Sn(acac)2 and HF. ECS J. Solid State Sci. Technol. 2015 , 4 , N5013.
- (8) Lim, W. S.; Park, J. B.; Park, J. Y.; Park, B. J.; Yeom, G. Y. Low Damage Atomic Layer Etching of ZrO2 by Using BCl3 Gas and Ar Neutral Beam. J. Nanosci. Nanotechnol. 2009 , 9 , 7379 -7382.
- (9) Lee, Y.; George, S. M. Atomic Layer Etching of Al2O3 Using Sequential, Self-Limiting Thermal Reactions with Sn(acac)2 and Hydrogen Fluoride. ACS Nano 2015 , 9 , 2061 -2070.
- (10) Lee, Y.; George, S. M. Thermal atomic layer etching of HfO2 using HF for fluorination and TiCl4 for ligand-exchange. J. Vac. Sci. Technol., A 2018 , 36 , No. 061504.
- (11) Lee, Y.; George, S. M. Thermal Atomic Layer Etching of Al O , 2 3 HfO2, and ZrO2 Using Sequential Hydrogen Fluoride and Dimethylaluminum Chloride Exposures. J. Phys. Chem. C 2019 , 123 , 18455 -18466.
- (12) DuMont, J. W.; Marquardt, A. E.; Cano, A. M.; George, S. M. Thermal Atomic Layer Etching of SiO2 by a ' Conversion-Etch ' Mechanism Using Sequential Reactions of Trimethylaluminum and Hydrogen Fluoride. ACS Appl. Mater. Interfaces 2017 , 9 , 10296 -10307.
- (13) Johnson, N. R.; George, S. M. WO3 and W Thermal Atomic Layer Etching Using ' Conversion-Fluorination ' and ' OxidationConversion-Fluorination ' Mechanisms. ACS Appl. Mater. Interfaces 2017 , 9 , 34435 -34447.
- (14) Zywotko, D. R.; George, S. M. Thermal Atomic Layer Etching of ZnO by a ' Conversion-Etch ' Mechanism Using Sequential Exposures of Hydrogen Fluoride and Trimethylaluminum. Chem. Mater. 2017 , 29 , 1183 -1191.
- (15) Lee, Y.; DuMont, J. W.; George, S. M. Mechanism of Thermal Al2 O3 Atomic Layer Etching Using Sequential Reactions with Sn(acac)2 and HF. Chem. Mater. 2015 , 27 , 3648 -3657.
- (16) Lee, Y.; DuMont, J. W.; George, S. M. Trimethylaluminum as the Metal Precursor for the Atomic Layer Etching of Al2O3 Using Sequential, Self-Limiting Thermal Reactions. Chem. Mater. 2016 , 28 , 2994 -3003.
- (17) Hennessy, J.; Moore, C. S.; Balasubramanian, K.; Jewell, A. D.; France, K.; Nikzad, S. Enhanced Atomic Layer Etching of Native Aluminum Oxide For Ultraviolet Optical Applications. J. Vac. Sci. Technol., A 2017 , 35 , No. 041512.
- (18) DuMont, J. W.; George, S. M. Competition Between Al2O3 Atomic Layer Etching And AlF3 Atomic Layer Deposition Using Sequential Exposures Of Trimethylaluminum and Hydrogen Fluoride. J. Chem. Phys. 2017 , 146 , 052819.
- (19) Johnson, N. R.; Sun, H.; Sharma, K.; George, S. M. Thermal Atomic Layer Etching of Crystalline Aluminum Nitride Using Sequential, Self-limiting Hydrogen Fluoride and Sn(acac) 2 Reactions and Enhancement by H2 and Ar Plasmas. J. Vac. Sci. Technol., A 2016 , 34 , No. 050603.
- (20) Johnson, N. R.; Hite, J. K.; Mastro, M. A.; Eddy, C. R., Jr.; George, S. M. Thermal Atomic Layer Etching of Crystalline GaN
- Using Sequential Exposures of XeF2 and BCl3. Appl. Phys. Lett. 2019 , 114 , 243103.
- (21) Lee, Y.; George, S. M. Thermal Atomic Layer Etching of Titanium Nitride Using Sequential, Self-Limiting Reactions: Oxidation to TiO2 and Fluorination to Volatile TiF . 4 Chem. Mater. 2017 , 29 , 8202 -8210.
- (22) Shinoda, K.; Miyoshi, N.; Kobayashi, H.; Izawa, M.; Ishikawa, K.; Hori, M. Rapid Thermal-Cyclic Atomic-Layer Etching of Titanium Nitride in CHF3/O2 Downstream Plasma. J. Phys. D: Appl. Phys. 2019 , 52 , 475106.
- (23) Lee, Y.; DuMont, J. W.; George, S. M. Atomic Layer Etching of AlF3 Using Sequential, Self-Limiting Thermal Reactions with Sn(acac)2 and Hydrogen Fluoride. J. Phys. Chem. C 2015 , 119 , 25385 -25393.
- (24) Xie, W.; Lemaire, P. C.; Parsons, G. N. Thermally Driven SelfLimiting Atomic Layer Etching of Metallic Tungsten Using WF6 and O2. ACS Appl. Mater. Interfaces 2018 , 10 , 9147 -9154.
- (25) Xie, W.; Lemaire, P.; Parsons, G. N. Self-Limiting Thermal Atomic Layer Etching of Tungsten Metal Using O 2 Oxidation and WCl6 or WF6: Role of Halogen Species in Temperature Dependence of ALE Reaction Rate , AVS ALE Workshop; 2018, Incheon, South Korea.
- (26) Xie, W.; Parsons, G. N. Thermal Atomic Layer Etching of Metallic Tungsten Via Oxidation and Etch Reaction Mechanism Using O2 or O3 for Oxidation and WCl6 as the Chlorinating Etchant. J. Vac. Sci. Technol., A 2020 , 38 , No. 022605.
- (27) Dallorto, S.; Goodyear, A.; Cooke, M.; Szornel, J. E.; Ward, C.; Kastl, C.; Schwartzberg, A.; Rangelow, I. W.; Cabrini, S. Atomic Layer Etching Of SiO2 With Ar and CHF3 Plasmas: A Self-limiting Process For Aspect Ratio Independent Etching. Plasma Processes Polym. 2019 , 16 , 1900051.
- (28) Koh, K.; Kim, Y.; Kim, C.-K.; Chae, H. Quasi atomic layer etching of SiO 2 using plasma fluorination for surface cleaning. J. Vac. Sci. Technol., A 2018 , 36 , 01B106.
- (29) Mameli, A.; Verheijen, M. A.; Mackus, A. J. M.; Kessels, W. M. M.; Roozeboom, F. Isotropic Atomic Layer Etching of ZnO Using Acetylacetone and O2 Plasma. ACS Appl. Mater. Interfaces 2018 , 10 , 38588 -38595.
- (30) Ohba, T.; Yang, W.; Tan, S.; Kanarik, K.; Nojiri, K. Atomic Layer Etching Of GaN and AlGaN Using Directional Plasmaenhanced Approach. Jpn. J. Appl. Phys. 2017 , 56 , No. 06HB06.
- (31) Kauppinen, C.; Khan, S. A.; Sundqvist, J.; Suyatin, D. B.; Suihkonen, S.; Kauppinen, E. I.; Sopanen, M. Atomic Layer Etching of Gallium Nitride (0001). J. Vac. Sci. Technol., A 2017 , 35 , No. 060603.
- (32) Miyoshi, N.; Kobayashi, H.; Shinoda, K.; Kurihara, M.; Watanabe, T.; Kouzuma, Y.; Yokogawa, K.; Sakai, S.; Izawa, M. Atomic Layer Etching Of Silicon Nitride Using Infrared Annealing for Short Desorption Time Of Ammonium Fluorosilicate. Jpn. J. Appl.
- Phys. 2017 , 56 , No. 06HB01.
- (33) Wang, G.; Xu, Q.; Yang, T.; Xiang, J.; Xu, J.; Gao, J.; Li, C.; Li, J.; Yan, J.; Chen, D.; Ye, T.; Zhao, C.; Luo, J. Application of Atomic Layer Deposition Tungsten (ALD W) as Gate Filling Metal for 22 nm and Beyond Nodes CMOS Technology. ECS J. Solid State Sci. Technol. 2014 , 3 , P82 -P85.
- (34) Klaus, J. W.; Ferro, S. J.; George, S. M. Atomic Layer Deposition of Tungsten Using Sequential Surface Chemistry With a Sacrificial Stripping Reaction. Thin Solid Films 2000 , 360 , 145 -153.
- (35) Elam, J. W.; Nelson, C. E.; Grubbs, R. K.; George, S. M. Nucleation and Growth During Tungsten Atomic Layer Deposition on SiO2 Surfaces. Thin Solid Films 2001 , 386 , 41 -52.
- (36) Kim, S.-H.; Hwang, E.-S.; Kim, B.-M.; Lee, J.-W.; Sun, H.-J.; Hong, T. E.; Kim, J.-K.; Sohn, H.; Kim, J.; Yoon, T.-S. Effects of B H 2 6 Pretreatment on ALD of W Film using a Sequential Supply of WF6 and SiH4. Electrochem. Solid-State Lett. 2005 , 8 , C155 -C159.
- (37) Henn-Lecordier, L.; Lei, W.; Anderle, M.; Rubloff, G. W. Realtime Sensing And Metrology for Atomic Layer Deposition Processes and Manufacturing. J. Vac. Sci. Technol., B: Nanotechnol. Microelectron.: Mater., Process., Meas., Phenom. 2007 , 25 , 130 -139.

- (38) Luoh, T.; Su, C.-T.; Yang, T.-H.; Chen, K.-C.; Lu, C.-Y. Advanced Tungsten Plug Process for Beyond Nanometer Technology. Microelectron. Eng. 2008 , 85 , 1739 -1747.
- (39) Yang, M.; Aarnink, A. A. I.; Kovalgin, A. Y.; Wolters, R. A. M.; Schmitz, J. Hot-wire Assisted ALD of Tungsten Films: In-situ Study of the Interplay Between CVD, Etching, and ALD Modes. Phys. Status Solidi A 2015 , 212 , 1607 -1614.
- (40) Kalanyan, B.; Lemaire, P. C.; Atanasov, S. E.; Ritz, M. J.; Parsons, G. N. Using Hydrogen to Expand the Inherent Substrate Selectivity Window During Tungsten Atomic Layer Deposition. Chem. Mater. 2016 , 28 , 117 -126.
- (41) Lemaire, P. C.; King, M.; Parsons, G. N. Understanding Inherent Substrate Selectivity During Atomic Layer Deposition: Effect of Surface Preparation, Hydroxyl Density, and Metal Oxide Composition on Nucleation Mechanisms During Tungsten ALD. J. Chem. Phys. 2017 , 146 , No. 052811.
- (42) Wang, G.; Luo, J.; Liu, J.; Yang, T.; Xu, Y.; Li, J.; Yin, H.; Yan, J.; Zhu, H.; Zhao, C.; Ye, T.; Radamson, H. H. pMOSFETs Featuring ALD W Filling Metal Using SiH4 and B2H6 Precursors in 22 nm Node CMOS Technology. Nanoscale Res. Lett. 2017 , 12 , 306.
- (43) Shinoda, K.; Miyoshi, N.; Kobayashi, H.; Hanaoka, Y.; Kawamura, K.; Izawa, M.; Ishikawa, K.; Hori, M. Isotropic Atomic Level Etching of Tungsten Using Formation and Desorption of Tungsten Fluoride. In Advanced Etch Technology for Nanopatterning
- VII ; International Society for Optics and Photonics: 2018, 105890I.
- (44) Lee, C. G. N.; Kanarik, K. J.; Gottscho, R. A. The Grand Challenges of Plasma Etching: A Manufacturing Perspective. J. Phys. D: Appl. Phys. 2014 , 47 , 273001.
- (45) Kim, D. S.; Kim, J. E.; Lee, W. O.; Park, J. W.; Gill, Y. J.; Jeong, B. H.; Yeom, G. Y. Anisotropic Atomic Layer Etching of W Using Fluorine Radicals/Oxygen Ion Beam. Plasma Processes Polym. 2019 , 1900081.
- (46) Natarajan, S. K.; Elliott, S. D. Modeling the Chemical Mechanism of the Thermal Atomic Layer Etch of Aluminum Oxide: A Density Functional Theory Study of Reactions during HF Exposure. Chem. Mater. 2018 , 30 , 5912 -5922.
- (47) Mullins, R.; Natarajan, S. K.; Elliott, S. D.; Nolan, M. Selflimiting Temperature Window for Thermal Atomic Layer Etching of HfO2 and ZrO2 Based on the Atomic-Scale Mechanism. Chem. Mater. 2020 , 32 , 3414 -3426.
- (49) Blochl, P. E. Projector Augmented-Wave Method. ̈ Phys. Rev. B 1994 , 50 , 17953.
- (48) Kresse, G.; Furthmuller, J. Efficient Iterative ̈ Schemes for Ab Initio Total-energy Calculations Using a Plane-wave Basis Set. Phys. Rev. B 1996 , 54 , 11169.
- (50) Kresse, G.; Joubert, D. From Ultrasoft Pseudopotentials to the Projector Augmented-wave Method. Phys. Rev. B 1999 , 59 , 1758.
- (51) Perdew, J. P.; Burke, K.; Ernzerhof, M. Generalized gradient approximation made simple. Phys. Rev. Lett. 1996 , 77 , 3865.
- (52) Togo, A.; Tanaka, I. First Principles Phonon Calculations in Materials Science. Scr. Mater. 2015 , 108 , 1 -5.
- (53) TURBOMOLE ; V6.2 2010, a development of University of Karlsruhe and Forschungszentrum Karlsruhe GmbH, 1989 -2007, TURBOMOLE GmbH, since 2007; available from http://www. turbomole.com last accessed 27/11/2019.
- (54) Persson, K. Electronic Structures ; 2016; URL: https:// materialsproject.org/materials/mp-91/, accessed on 11/11/2019.
- (55) Wycko /uniFB00 , R. W. G. Crystal Structures ; Crystal Structures v. 1; Wiley: 1963
- (56) Kittel, C.; McEuen, P. Introduction to Solid State Physics ; Wiley: 1996.
- (57) Gulbransen, E. A.; Andrew, K. F. Kinetics of the Oxidation of Pure Tungsten From 500 ° to 1300 C. ° J. Electrochem. Soc. 1960 , 107 , 619 -628.
- (58) Kellett, E. A.; Rogers, S. E. The Structure of Oxide Layers on Tungsten. J. Electrochem. Soc. 1963 , 110 , 502 -504.
- (59) Cifuentes, S. C.; Monge, M. A.; Perez, P. On the Oxidation ́ Mechanism of Pure Tungsten in the Temperature Range 600-800 ° C. Corros. Sci. 2012 , 57 , 114 -121.
- (60) King, D. A.; Madey, T. E.; Yates, J. T., Jr. Interaction of Oxygen With Polycrystalline Tungsten. Part 3.-Electron stimulated desorption. J. Chem. Soc., Faraday Trans. 1 1972 , 68 , 1347.
- (61) Warren, A.; Nylund, A.; Olefjord, I. Oxidation of Tungsten and Tungsten Carbide in Dry and Humid Atmospheres. Int. J. Refract. Hard Met. 1996 , 14 , 345 -353.