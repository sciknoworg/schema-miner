<!-- image -->

## Supporting Information

for Adv. Mater. Interfaces, DOI: 10.1002/admi.202101085

Combining Experimental and DFT Investigation of the Mechanism Involved in Thermal Etching of Titanium Nitride Using Alternate Exposures of NbF5 and CCl4, or CCl4 Only

Varun Sharma,* Suresh Kondati Natarajan, Simon D. Elliott, Tom Blomberg, Suvi Haukka, Michael E. Givens, Marko Tuominen, and Mikko Ritala*

Supplementary Information: Combining Experimental and DFT Investigation of the Mechanism Involved in Thermal Etching of Titanium Nitride Using Alternate Exposures of NbF 5 and CCl , or CCl 4 4 only

Varun Sharma, ∗ , † Suresh Kondati Natarajan, ¶ Simon D. Elliott, § Suvi Haukka, † Marko Tuominen, † Tom Blomberg, ‖ and Mikko Ritala ∗ , ‡

† ASM Microchemistry Oy, Pietari Kalmin katu 3 F2, 00560 Helsinki, Finland ‡ Department of Chemistry, University of Helsinki, FI-00014 Helsinki, Finland ¶ Department of Electrical Engineering and Automation, Aalto University, Espoo 02156, Finland § Schrödinger, 120 West 45th Street, New York, NY 10036-4041, USA ‖ Department of Chemistry and Materials Science, Aalto University, Espoo, Uusimaa 02150,

## Finland

⊥ Currently at Picosun Oy, Masala, Finland

E-mail: varun.sharma@asm.com,varun.sharma@helsinki.fi; mikko.ritala@helsinki.fi

## S0: Computational details

In this supporting information, explicit atomistic mechanisms involved in the etching of TiN using NbF 5 and CCl 4 are provided. We have used TiN(2 1 1), a stepped surface for this study. Stepped surfaces are the most suitable for this type of analysis as they have high surface energy and they are

often more reactive than the flat surfaces. A 9.3 Å thick (2 × 2) supercell of the TiN (2 1 1) surface (Ti 96 N 96 ) with a surface area of 1.74 nm 2 and computed surface energy of 3.8 J/m 2 is chosen for the surface model, which consists of 4 Ti 24 N 24 layers with a rigid bottom layer. A Monkhorst-Pack K-point mesh of 2 × × 3 1 is used during the geometry relaxation.

Binding/adsorption energies ( E ads ) are given by

$$E _ { \text{ads} } = E _ { \text{int} } - \sum E _ { \text{non-int} },$$

in which E int is the energy of the interacting system where the molecule is adsorbed on the surface of the material and E non -int are the energies of the participating but non-interacting systems such as the energy of the molecule in gas phase and energy of the bare surface.

## S1: Fluorination pulse

In this section we present the results of first principles based adsorption simulations where NbF 5 molecules are reacting with the TiN(2 1 1) surface. Homolytic dissociation of NbF 5 in gas phase is very endoergic requiring 7.3 eV to remove one F ligand and 9.9 eV to remove F . 2 Thus, the TiN surface shown in Figure S1 has to satisfy this energy requirement and catalyse the NbF 5 dissociation. The step edge present in the TiN(2 1 1) surface is especially a favourable reactant binding spot.

In the minimum energy geometry of isolated NbF 5 molecule, three F ligands are bound along the equatorial plane of the molecule each with an Nb-F bond length of 1.85 Å and two F ligands are found in either sides of the polar axis of the molecule with an Nb-F bond length of 1.88 Å. Since the polar Nb-F bond length is longer, we adsorbed the molecule with a polar F ligand close to a Ti atom along the step edge of the surface. On adsorption, the NbF 5 molecule does not dissociate at 0 K, as shown in Figure S2, due to the presence of kinetic barriers for the Nb-F bond dissociation. However, the NbF 5 binding energy to the surface is about -0.9 eV and we see an extended bond length of Nb-F close to the surface (from 1.88 Å to 2.05 Å) which indicates that this bond will

Figure S1: Bare surface of TiN(2 1 1) with step edge marked by an arrow. Grey atoms are Ti and blue atoms are N. Step Edge

<!-- image -->

Nb break easily at elevated temperatures. The distance of the newly formed Ti-F bond on the surface is 2.05 Å.

-0.90 eV

Nb-F' = Ti-F'= 2.05 Å

Figure S2: Intact adsorption of NbF 5 molecule on TiN(2 1 1) surface. The red and green are niobium and fluorine atoms, respectively.

<!-- image -->

We performed a 5 ps MD simulation at 400 K at DFT level starting from the above local minimum geometry. Within 1.7 ps, 4 Nb-F bonds are dissociated consecutively from the NbF 5 molecule and the F atoms adsorb at the TiN surface. This very rapid dissociation suggests that barriers to the dissociation of NbF 5 can be overcome easily on the modelled TiN(2 1 1) surface at 400 K. We extracted a few geometries from the simulation and relaxed them to find unique minimum energy geometries as shown in Figure S3.

Figure S3: Minimum energy geometries of NbF 5 adsorbed on TiN(2 1 1) surface (at 0 K) which are extracted from an MD simulation at 400 K.

<!-- image -->

In the minimum energy geometries shown in Figure S3a-e we find a continuous decrease in the binding energy, from -0.90 eV up to -9.11 eV, as more Nb-F bonds get dissociated and Ti-F formed. The most favourable geometry is Figure S3e where the Nb is bound to the surface, coordinating with three surface N atoms, and it is left with one F ligand pointing away from the surface. This suggests that NbF , at 400 K, dissociates readily on the TiN(2 1 1) surface and the surface will be 5 covered by Nb-N and Ti-F terminations at the end of this pulse. Although not observed in the MD trajectory, we also studied full dissociation of NbF 5 molecule as shown in Figure S3f, however, this configuration was less favourable than the one in Figure S3e. In Figure S4, we have shown a NbF 5 saturated TiN surface model where the Nb atoms are trapped next to the step edge coordinated to surface N atoms while the F atoms are found atop the Nb atoms, at the 3 fold Ti sites and at the bridge sites connecting Ti and Nb atoms along the step edges. This geometry corresponds to a NbF 5 coverage of 2.3 molecules/nm 2 , a dissociated F coverage of 9.0 F/nm 2 and a net binding energy of -7.3 eV/NbF . The Nb and F that have this way been deposited on the surface will block 5 further reaction with NbF 5 , which must result in self-limiting reaction.

Figure S4: A minimum energy geometry showing a NbF 5 saturated surface of TiN(2 1 1). The Nb atoms can be seen trapped near the step edge. panels a) and b) show the top and side views, respectively. The green and red are niobium and fluorine atoms, respectively.

<!-- image -->

## S2: Chlorination pulse

We will use the above surface geometry for the CCl 4 adsorption in the next pulse. Before we look into those results we would like to validate our thermochemical prediction for the CCl 4 pulse (R9 in Table 2 of main text). From explicit surface adsorption calculations, we find that the CCl 4 molecule spontaneously dissociates on the bare TiN at 0 K, donates a Cl ligand to the surface, and drifts off in to the vacuum as CCl 3 fragment. This in contrast to the NbF 5 adsorption, which did not dissociate spontaneously. This is proof that CCl 4 reacts strongly with the bare TiN surface when compared to NbF 5 . We also performed a short 3 ps long MD simulation at DFT level of CCl 4 adsorbed on the bare TiN surface which resulted in a complete dissociation of CCl 4 molecule within just 0.74 ps and formation of three surface Ti-Cl and a surface bound CNCl, which is the proposed by-product of this reaction.

Figure S5: A minimum energy geometry of intact CCl 4 adsorbed at the Nb X F Y covered TiN surface at 0 K.

<!-- image -->

A CCl 4 molecule did not bind strongly to the Nb X F Y covered TiN surface at 0 K due to net repulsion between the Cl atoms and surface bound F ligands. The most favourable geometry found in our investigation with a binding energy of -0.07 eV is given in Figure S5a. In this configuration, one of the Cl atoms of CCl 4 is directed at the surface towards the Nb atoms. In all the other configurations where the C-Cl bond is directed towards the surface Ti/F atoms, the CCl 4 molecule did not physisorb on the surface but was pushed back into the vacuum. This suggests that Nb sites are important for CCl 4 to react with when the rest of the surface is covered with F. On the other hand, if the coverage of NbF 5 is sparse, then the CCl 4 molecule will readily dissociate on the Ti

21

rich surface region.

Since we have already established that CCl 4 spontaneously dissociated on the bare TiN surface, we now discuss the CCl 4 interaction with F-free Nb sites. We adsorbed a CCl 4 molecule close to the Nb atom in the geometries shown in Figures S3d and S3e and the resulting relaxed geometries are shown in Figures S5b and S5c, respectively. We find that a favourable binding (-0.1 eV) between the Cl atoms and Nb atom is possible (Figures S5b) even when the Nb atom is weakly bound to 2 F atoms, when they are simultaneously bound also to surface Ti atoms. A strong dissociative adsorption of CCl 4 (-3.2 eV) is possible when the Nb atom is free of Nb-F bonds (Figures S5b). Based on the above computational results, we propose that the ALE of TiN proceeds by self-limiting dissociative adsorption of NbF 5 in the first pulse followed by the dissociative adsorption of CCl 4 catalysed by the Nb sites in the second pulse leading to the etch of TiN.

Wedonot look at the mechanism of formation and desorption of all the possible volatile species in this paper as there are very many product combinations involved and computing all reaction pathways is not in the scope of this paper.

## S3: Adsorption of Cl and F onto TiN

Figure S6, reveals that on TiN surface F adsorbs more strongly than Cl at various surface coverages and this difference in binding is more pronounced at higher coverages. Although both F and Cl are halogens, F being in the second period in the periodic table as compared to Cl in the third period would naturally result in stronger binding due to small atomic radius and increased electronegativity of F. What this means is that, when F adsorbs on the TiN surface, the strong and highly polar Ti-F bonds 1 are formed on the surface. These strong surface bonds will in turn weaken the bonding of the surface Ti atoms with the sub-surface atoms, this effect is needed for the removal of the surface Ti atoms. Thus, in comparison to Cl covered TiN surface, F covered TiN surface will be favorable for etching. This could be the reason for the catalytic behavior of NbF 5 , especially due to its dissociation on TiN surface.

Figure S6: Binding energy of chlorine and fluorine atoms on TiN surface at varying halide atoms surface coverage at 0 K.

<!-- image -->

## S4: Change in the Gibbs free energy with temperature

Figure S7 shows a change in the Gibbs free energy at various temperatures for considered reactions R1 to R9 (see Tables 1 and 2 in the main article). From the figure it is clear that only reactions R3, R4, R5 and R9 are feasible atleast upto the experimented etch temperature i.e. 460°C. From these reactions, the volatile titanium-containing etch products are predicted to be TiCl 3 , TiCl 4 , and TiF 4 .

Figure S7: A change in the Gibbs free energy is plotted at various temperatures.

<!-- image -->

## References

- (1) Webb, S. P.; Gordon, M. S. Intermolecular Self-Interactions of the Titanium Tetrahalides TiX 4 (X = F, Cl, Br). Journal of the American Chemical Society 1999 , 121 , 2552-2560.
