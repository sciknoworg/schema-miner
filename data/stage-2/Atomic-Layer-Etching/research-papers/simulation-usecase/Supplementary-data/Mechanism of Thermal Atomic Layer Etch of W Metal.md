## Supporting Information

## for

## "Mechanism of Thermal Atomic Layer Etch of W Metal Using Sequential Oxidation and Chlorination: A First-Principles Study"

Suresh Kondati Natarajan, ∗ † ‡ , , Michael Nolan, † ¶ , Patrick Theofanis, § Charles Mokhtarzadeh, § and Scott B. Clendenning §

† University College Cork, Tyndall National Institute, Lee Maltings, Dyke Parade, Cork, T12 R5CP, Ireland.

- ‡ Department of Electrical Engineering and Automation, Aalto University, Espoo 02150, Finland
- ¶ Nanotechnology and Integrated Bioengineering Centre, Ulster University, Shore Road, Co Antrim, BT37 OQB, Northern Ireland.

§ Intel Corporation, 2501 NE Century Blvd., Hillsboro, Oregon, USA 97124

E-mail:

suresh0807@gmail.com

## S0: Models of W Bulk and W(3 1 0) Surface

## S0.1 Dispersion Correction

We used the Tkatchenko-Scheffler Scheme 1 (without iterative Hirschfeld partitioning, IVDW = 20 in VASP) on the bulk BCC W and found a cohesive energy of -10.3 eV/atom, which is much larger than the experimental value of -8.9 eV/atom and the PBE value of -9.1 eV/atom. On the other hand the lattice constant increased from the PBE value of 3.17 Å and experimental value of 3.16 Å to 3.12 Å. This also increases the surface energy of W(3 1 0) to 5.65 J/m 2 from the PBE value of 3.77 J/m 2 and the experiments also suggests surface energy values around 3.3 J/m . 2 2-4 Grimme's D3 dispersion correction, for bulk BCC W, gave a cohesive energy of -9.8 eV/atom and a lattice constant of 3.14 Å. For the (3 1 0) surface, the surface energy was 4.71 J/ . 2 While the description of PBE + D3 is better than the description of PBE + TS, it is still not as good as PBE when compared to experimental data.

We also computed the adsorption energy of an O 2 molecule on the W (3 1 0) surface with PBE + TS scheme to find the contribution from dispersion correction. O molecule adsorbed 2 at the atop site of W(310) (Figure 2a of the main text) with a binding energy of -7.76 eV and the dispersion energy contribution is -0.14 eV. Similarly, the vdW contribution for O 2 molecule adsorbed on bridge site was -0.18 eV. The PBE binding energy is much larger than the contribution from dispersion correction and we did not find a significant change in the geometry as well. Therefore, we decided to leave out dispersion correction as it did not significantly improve the system's description in this case.

## S0.2 Geometries of W Bulk and W/WOx Surface

Figure S1: Geometry of Bulk W with its computed lattice constant is shown in a). The computed total density of states of bulk W is shown in b). Top and side views of bare W(3 1 0) surface are given in c) and d), respectively. The blue region indicates the atoms used in the DFPT calculation.

<!-- image -->

W: Saturated Surface - 14 O atoms

(O2

/O3

)

<!-- image -->

1

5

Figure S2: Three surface geometries (A, B and C) with different arrangement of O atoms. Geometry A is chosen as the SL product state as it had the lowest surface binding energy. We could find most O atoms in A at bridge sites. W atoms are shown in blue and oxygen atoms in red.

## S1: Second ALE Pulse Schematics

Figure S3: A schematic representation of the sequential removal of etch species when WCl 6 and Cl 2 are used as the second pulse chemical.There are three pathways possible for WCl 6 and two possibilities for Cl . 2 Each WCl 6 is capable of removing 1-2 surface W atoms, whereas each Cl 2 can only remove one surface W atom.

<!-- image -->

<!-- image -->

## S2: N O Adsorption 2

N O is a linear molecule and it dissociates into N 2 2 and O 2 in gas phase by releasing an energy of -0.14 eV per N O at 0 K subject to energetic barriers. 2 This dissociation reaction is also exergonic with a release of -0.80 eV at 400 K. To study the interaction of N O with the 2 W(3 1 0) surface, we adsorbed a N O molecule at different orientations and different sites 2 on the surface and relaxed the geometries. Figure S4 shows the optimized geometries and Table S1 lists the corresponding binding energies and shortest W-O, W-N and N-N bond lengths.

Table S1: Binding energies and minimum W-O, W-N and N-N bond distances for N O adsorption on W(3 1 0) surface. 2

| Geo.   |   E bind [eV/N 2 O] |   d(W-O) [Å] |   d(W-N) [Å] |   d(N-N) [Å] |
|--------|---------------------|--------------|--------------|--------------|
| Ha     |               -5.27 |          1.9 |          2   |         1.22 |
| Hb     |               -2.44 |          2.1 |          2.1 |         1.24 |
| Hc     |               -5.81 |          2   |          2   |         1.31 |
| Hd     |               -2.34 |          3.2 |          2   |         1.32 |
| He     |               -4.71 |          1.8 |          2   |         1.15 |
| Va     |               -0.12 |          2.4 |          3.6 |         1.15 |
| Vb     |               -0.88 |          4.4 |          2.1 |         1.16 |

Figure S4: The top and side views of the optimized N O molecule on W(3 1 0) surface. 2 panels (a) to (e) corresponds to the geometries where the N O molecule is adsorbed with its 2 axis parallel to the surface (horizontal). Panels (f) and (g) show geometries where the N O 2 molecule is adsorbed with its axis perpendicular to the surface (vertical). The colour coding is as follows: W=grey, O = red and N = blue.

<!-- image -->

Clearly, the horizontal configurations of N O (denoted Ha-He in Figure 6) are favoured 2

over the vertical configurations (denoted Va and Vb and Figure 6) by at least -1.4 eV. Moreover, the dissociated state of the molecule is preferred by at least 2.3 eV as compared to the intact state. In three of the horizontal configurations (Ha, Hc, He) the N O molecule has 2 dissociated spontaneously into a N 2 molecule and O atom, out of which the Hc geometry was the most favourable. In geometries Hb and Hd, the N O molecule is not fully dissociated and 2 has relatively lower binding energies than the rest. The two vertical adsorption geometries did not result in spontaneous dissociation and the N down configuration (Vb) was more favourable than the O down configuration (Va). The N 2 dissociation product remains intact and does not dissociate spontaneously, which is consistent with published results on N 2 adsorption on low-index W surfaces. 5 However, the N-N bond length elongates from 1.11 Å in the gas phase to a maximum of 1.32 Å in the adsorbed state (reference geometry Hc). In that same publication 5 the author reported that the dissociated N atoms on the W(1 0 0) and W(1 1 0) surfaces are more favourable than the molecularly adsorbed state. Therefore, we tested if it is also true for the W(3 1 0) surface by dissociating the intact N 2 molecule in the geometry Ha in two ways: along and across the step edge as shown in Figure S5. The activation energies reported in this paper are computed using climbing image nudged elastic band approach, with 3 images and a convergence criterion of -0.02 eV/Å. 6,7 It can be seen that dissociation of N 2 molecule is preferred overall as compared to molecular adsorption. Moreover, the dissociation along the step is more preferable than the dissociation across the step. Molecular desorption of N 2 costs energy (about 1 eV), however, it is expected to become favourable at ALE operating temperatures (500 K) due to probable entropic gain.

Figure S5: The Energies of N 2 dissociation and desorption from the minimum geometry Ha given in Figure S4. The colour coding is as follows: W=grey, O = red and N = blue.

<!-- image -->

## S3: Natarajan-Elliott 'N-E' Analysis of Oxidation Pulse

In N-E analysis we compare two reaction models of the oxidation pulse. These reactions are bulk oxidation, denoted as bulk bulk and surface oxidation, denoted as surf surf. In the bulk bulk reaction tungsten is fully oxidized to bulk WO 3 using the chosen gas

Table S2: Reaction free energies at 0 K and 500 K for the postulated bulk bulk ( ∆ G B ) and surf surf ( ∆ G S ) reactions representing the oxidation pulse on W. ( ∆∆ G ) is the corresponding 'minimum barrier' for bulk oxidation. The reactant pressure is set to 0.2 Torr and product pressure to 0.01 Torr. The energy values are given per unit bulk (u.b.) material. (b) refers to bulk, (g) to gas-phase and (surf) to surface. The (·) indicates that that species is in bulk state in the bulk bulk reaction and it is in surface state in the surf surf reaction.

| Reactions   | Reactions                                      | 0 K [eV/u.b]   | 0 K [eV/u.b]   | 0 K [eV/u.b]   | 500 K [eV/u.b]   | 500 K [eV/u.b]   | 500 K [eV/u.b]   |
|-------------|------------------------------------------------|----------------|----------------|----------------|------------------|------------------|------------------|
|             |                                                | ∆ G B          | ∆ G S          | ∆∆ G           | ∆ G B            | ∆ G S            | ∆∆ G             |
| R1          | 1 W ( · ) + 1.5 O 2(g) 1 WO 3( · )             | -8.50          | -10.73         | 2.23           | -6.71            | -8.88            | 2.17             |
| R2          | 1 W ( · ) + 1 O 3(g) 1 WO 3( · )               | -9.80          | -12.03         | 2.23           | -8.45            | -10.62           | 2.17             |
| R3          | 1 W ( · ) + 3 N 2 O (g) 1 WO 3( · ) + 3 N 2(g) | -9.24          | -11.47         | 2.23           | -9.35            | -11.53           | 2.17             |

reactants. In the surf surf reaction, we model a self-limiting reaction where only the first layer of W atoms are oxidized (using the structure described in Figure 1 of main text as the product state). The free energies of the above reactions ( ∆ G B and ∆ G S ) at 0 K and 500 K are listed in Table S2 along with the minimum barrier ( ∆∆ G ) to cause runaway oxidation. This minimum barrier is computed by simply subtracting the free energies of the two reactions. We have also included the free energy contributions of the bulk and surface models, computed from first principles as described in the computational section, in this analysis to compare the bulk bulk and surf surf reactions on equal footing. Here, we have not included any kinetic barriers, which may be found by studying the minimum energy pathways and the associated activation energies of sub-surface oxygen diffusion process, which is possibly a rare event at low temperatures and low oxygen coverage. The ∆ G profiles of these reactions

spanning a temperature range of 0 K - 1000 K along with the change in minimum barrier are given further below.

From Table S2, we find that the surf surf reactions are energetically more favourable than the bulk bulk reactions, for all reactants, with a minimum energy difference of about 2.23 eV to cause bulk oxidation. Reaction R2 is the most favourable, followed by R3 and R1, i.e. O 3 &gt; N O 2 &gt; O . 2 One molecule of O 3 can completely oxidize a bulk W atom, whereas for O 2 and N O, 1.5 and 3 molecules are required, respectively. 2 Therefore, in terms of reactivity of the reactant gas molecules the order will be as follows: O 3 &gt; O 2 &gt; N O. 2

At 500 K, the ∆ G values of R1 and R2 are increased by about 1.8 eV and 1.4 eV respectively when compared to their ∆ G at 0 K mainly due to entropic loss as no gas phase by-products are formed in these reactions. In contrast the ∆ G value of R3 decreased by 0.1 eV. Compared to reactions R1 and R2, in reaction R3 the original linear N O molecule 2 results in formation of a linear N 2 molecule with negligible entropic loss and negligible change in ∆ G. In addition to that, the oxide surface offers more entropy than clean metal surface, further reducing the ∆ G for R3. For all reactions, the minimum energy difference between self-limiting and continuous etch changes insignificantly, from 2.23 eV at 0 K to 2.17 eV at 500 K. To summarize, all the reactions given in Table S2 have favourable ∆ G values even at high temperatures. Most importantly, the surf surf reactions are at least 2 eV more favourable than the bulk bulk reactions suggesting that runaway bulk oxidation is not thermodynamically favourable when compared to the self-limiting reaction at typical ALE process temperatures.

## Free Energy Profiles of Bulk Oxidation Reactions

The free energy profiles of the reactions given in Table S2 in the temperature range of 01000 K, at a reactant pressure of 0.2 Torr and product pressure of 0.01 Torr are given in Figure S6a. Please note that the product pressure cannot be controlled in a thermal etch reactor. All the considered reactions have favourable FEPs in the entire temperature range

First pulse precursors

Figure S6: a) FEPs of the reactions in given in Table S2. Here, B-B and S-S represent bulk bulk and surf surf reactions, respectively. b) change in the minimum barrier with temperature.

<!-- image -->

studied ( ∆ G &lt; 0). Overall, the S-S reactions are significantly more favourable than the corresponding B-B reactions. We find that FEPs of R1, R2 and R4 reactions have positive slope i.e. reactions become less favourable with temperature, whereas the FEPs of R3 reaction have a negative slope. R1 reaction has the largest slope followed by R2, R4 and R3 in that order. In R1 and R2 reactions, the positive slope is mostly attributed to the entropic loss as the combined gas and bulk(surface) reactant state results in a bulk(surface) product state. In Reaction R4, the relatively larger reactant H O 2 2 molecule results in a smaller H 2 molecule leading to a negative entropy change. On the other hand in reaction R3, the linear N O molecule result in a linear N 2 2 molecule without much entropic loss. In addition to that the oxide offers more entropy than pure metal, thus, the negative slope. The minimum barrier to cause bulk oxidation with respect to temperature is given in Figure S6b and we find that the minimum free energy barrier (ZPE change is now included to the minimum barrier) decreases mildly with temperature from 2.23 eV at 0 K to 2.12 eV at 1000 K. These minimum barriers when overcome would allow for the sub-surface diffusion of O atoms to

cause bulk oxidation. Moreover, over layers of precursors are not considered in this study and they might contribute positively or negatively towards the sub surface diffusion of precursors. As the next step we shall study the mechanism of adsorption of these precursors on bare W(3 1 0) surface.

## S4: Reaction of WCl 6 and Cl 2 on bare W surface

Both WCl 6 and Cl 2 molecules dissociated spontaneously on the bare W(3 1 0) surface by releasing an energy of -4.5 eV and -5.9 eV, respectively. These reactions are extremely favourable and Cl 2 reacts stronger than WCl . If the reaction self-limits after the removal of 6 the oxide layer in the second ALE pulse, it is probable that we will be left with a chlorinated Wsurface. It is also possible that other gas phase molecules of W and Cl such as WCl , WCl 5 4 and WCl 3 might form and leave the surface, which is undesirable. Therefore we performed an N-E analysis 8 to investigate the exposures of Cl 2 and WCl 6 on the bare W to understand the competition between chemical vapour etch (CVE) and self-limiting reactions. The postulated reactions and corresponding free energies are listed in Table S3.

When WCl 6 is used as the precursor, removal of a surface W atom by a single WCl 6 molecule is only possible by the formation of two WCl 3 species. In order to form larger etch products such as WCl 4 and WCl , at least two WCl 5 6 molecules are needed. On the other hand, Cl 2 is a much smaller molecule offering a higher Cl coverage on the substrate as compared to WCl 6 and only 1.5 molecules of Cl 2 are needed to form a volatile species. It can be seen that the CVE reactions using WCl 6 as the reagent are endergonic at 0 K and 500 K, whereas the CVE reactions using Cl 2 are mostly exergonic except for the R1 reaction at 500 K. This observation can be explained by entropic gain in the WCl 6 reactions and entropic loss in the Cl 2 reactions.

To make sure whether the etch reactions remain unfavourable at higher temperatures, we computed the thermochemical free energy profiles as shown in Fig. S7.

From the FEPs, we find that only the CVE reactions with WCl 6 as precursor decreases in free energy with increase in temperature, mainly due to the gain in entropy because of the formation of more gas phase products than the number of gas phase reactants. All other reactions become less favourable with increase in temperature. In the temperature range studied, all SL reactions are more favourable than the corresponding CVE reactions. Even though the minimum barrier to etch decreases with temperature, significantly in the case of

Table S3: Reaction free energies ( ∆ G ) of the postulated bulk gas ( ∆ G B ) and surf surf ( ∆ G S ) reactions at 0 K and 500 K representing the chlorination pulse on W along with the corresponding 'minimum barrier' ( ∆∆ G ) to cause etching. The energy values are in eV and are normalized per W atom. (b) refers to bulk, (g) to gas-phase and (surf) to surface. The (·) indicates that that species is in bulk/gaseous state in the bulk gas reaction and surface state in the surf surf reaction.

|    | Reactions                                                 | 0 K [eV/u.b]   | 0 K [eV/u.b]   | 0 K [eV/u.b]   | 500 K [eV/u.b]   | 500 K [eV/u.b]   | 500 K [eV/u.b]   |
|----|-----------------------------------------------------------|----------------|----------------|----------------|------------------|------------------|------------------|
|    |                                                           | ∆ G B          | ∆ G S          | ∆∆ G           | ∆ G B            | ∆ G S            | ∆∆ G             |
|    | WCl 6                                                     |                |                |                |                  |                  |                  |
| R1 | W ( · ) + WCl 6(g) 2 WCl 3( · )                           | 4.53           | -4.52          | 9.05           | 2.67             | -3.20            | 5.87             |
| R2 | W ( · ) + 2 WCl 6(g) 3 WCl 4( · )                         | 2.08           | -8.77          | 10.86          | 0.13             | -5.99            | 6.11             |
| R3 | W ( · ) + 2 WCl 6(g) WCl 3( · ) + WCl 4( · ) + WCl 5( · ) | 2.94           | -8.77          | 11.72          | 1.48             | -5.99            | 7.47             |
|    | Cl 2                                                      |                |                |                |                  |                  |                  |
| R1 | W ( · ) + 1.5 Cl 2(g) WCl 3( · )                          | -0.78          | -9.24          | 8.46           | 0.25             | -6.50            | 6.75             |
| R2 | W ( · ) + 2 Cl 2(g) WCl 4( · )                            | -3.36          | -11.36         | 8.00           | -1.40            | -7.73            | 6.32             |
| R3 | W ( · ) + 2.5 Cl 2(g) WCl 5( · )                          | -5.09          | -14.34         | 9.25           | -1.70            | -9.80            | 8.10             |

Figure S7: Panel a) shows the FEPs of the reactions in given in Table S3. Here, B-G and S-S represent bulk gas and surf surf reactions, respectively. Panel b) shows change in the minimum barrier with temperature.

<!-- image -->

WCl 6 and moderately in the case of Cl , it is still greater than at least 2 eV even at 1000 2 K. This confirms that the CVE reactions are not possible when WCl 6 and Cl 2 are used as precursors.

Using WCl 6 as the reagent, we performed a similar analysis comparing the self-limiting reactions to quantify the formation of the non-etch by-products such as WCl , WCl 5 4 and WCl from the interaction of a single WCl 3 6 molecule with the bare W surface. The postulated reactions and their free energies at 0 K and 500 K are given in Table S4. The reference selflimiting reaction used in this analysis is the same as that of R1-WCl 6 in Table S3.

In contrast to the CVE reactions listed in Table S3, the removal of the adsorbed WCl 6 as gaseous WCl , WCl 5 4 and WCl 3 is exergonic with the minimum thermodynamic barrier in the range of 2 - 3 eV for WCl 5 and WCl 4 and decreases to just 0.6 eV for WCl 3 at 0 K. With increase in temperature, the barrier decreases considerably for the R2 and R3 reactions (0.64 and -0.88) and moderately for the R1 reaction (1.75). Negative barrier indicates that the gaseous by-product formation is thermodynamically preferred to surface bound state. Figure S8 shows the free energy profiles of the reactions given in Table S3. These profiles show that all the reactions are exergonic in the entire temperature range considered. The

Table S4: Reaction free energies ( ∆ G ) of the postulated SL reactions at 0 K and 500 K representing the non-etch WCl 6 pulse on W along with the corresponding 'minimum barrier' (Y-X) to cause by-product formation. The energy values are in eV and are normalized per unit W. (g) refers to gas-phase and (surf) to surface.

|      | Reactions                                          |   ∆ G at 0 K | Barrier   |   ∆ G at 500 K | Barrier   |
|------|----------------------------------------------------|--------------|-----------|----------------|-----------|
| Ref. | 1 W (surf) + 1 WCl 6(g) 2 WCl 3(surf)              |        -4.52 |           |          -3.2  |           |
| R1   | 1 W (surf) + 1 WCl 6(g) 1 WCl (surf) + 1 WCl 5(g)  |        -1.84 | 2.68      |          -1.45 | 1.75      |
| R2   | 1 W (surf) + 1 WCl 6(g) 1 WCl 2(surf) + 1 WCl 4(g) |        -2.27 | 2.25      |          -2.56 | 0.64      |
| R3   | 1 W (surf) + 1 WCl 6(g) 1 WCl 3(surf) + 1 WCl 3(g) |        -3.93 | 0.59      |          -4.08 | -0.88     |

<!-- image -->

R1

R2

b)

8

6

4

2

0

-2

-4

0

Figure S8: FEPs of the reactions in given in Table S3.

Minimum barrier  [eV / W]

250

500

750

Temperature [K]

1000

non-etch W removal reaction R3 becomes thermodynamically favourable than the reference surface reaction beyond 220 K. Similarly, R2 becomes favourable beyond 730 K. Reaction R1 is unfavourable in the entire temperature range when compared to the reference reaction. There exists a delicate balance between the formation of gaseous by-products and stable WCl bonds on the surface which minimizes the free energy. The surface W-Cl bond provides enthalpic gain while the gas-phase products bring an entropic gain. The optimal gain in enthalpy and entropy is obtained in R3 when a WCl 6 molecule donated 3 Cl atoms to the surface and desorbed from the surface as WCl 3 at elevated temperatures.

In summary, the exposure of WCl 6 and Cl 2 on bare W surface did not result in continuous etching of the substrate even at elevated temperatures. Deposition of W, when WCl 6 is used, is also found not to be thermodynamically favourable beyond room temperature.

## S5: Dissociation pathway of WCl 6

Figure S9: Distance and energy of 5 configurations (a-e) connecting Fig.4a and Fig.4b in the main text. A dissociation barrier of 0.52 eV is computed. X axis is the distance between donor W atom (W in WCl ) and Cl atom, primary Y axis is potential energy relative to 6 geometry a and secondary Y axis shows W-Cl distance. The saddle point corresponds to a Wa-Cl bond distance of 2.71 Å.

<!-- image -->

## S6: Thermal ALE of Metals

Thermal ALE is a material removal technique where up to a monolayer of material can be etched away at a time using sequential self-limiting reactions at elevated temperatures. A typical thermal ALE cycle typically consists of two reactant gas pulses separated by purge events. The first pulse is the 'surface modification' pulse where the surface atoms of the material are chemically modified, for eg. fluorination. After purging away the un-reacted molecules and by-products, a second reagent is pulsed in to the etch chamber which volatilizes the modified surface atoms of the material at elevated temperatures referred to as 'material removal' pulse. The two ALE pulses must be 'self-limiting' in the sense that they should only react with the (modified) surface atoms of the material and not the bulk. This is the essence of atomic layer processing of materials and in each cycle only a thin layer of the material will be removed.

Figure S10: A schematic representation of the thermal atomic layer etch process for metals.

<!-- image -->

Figure S10 shows a schematic representation of the ideal thermal ALE process for metals. The main difference between the thermal ALE of metals and metal oxides/ metal nitrides is that the first pulse must oxidize the metal atoms to a higher oxidation state. The choice of the first pulse reagent also depends on the target volatile species and the corresponding

oxidation state of the metal atoms in it. In the figure, we start with a clean metal surface with metal atoms at 0 oxidation state. In the modification pulse a suitable oxidizing agent Z y is allowed to interact with the surface metal atoms and raise the oxidation state of these atoms from M 0 to M y+ . After the purge event, a thin layer of non-volatile M y+ Z y passivates the metal surface. In the second pulse, a suitable ligand exchange agent SX y is introduced which, at elevated temperatures, exchanges ligands with the M y+ Z y species on the surface and form volatile SZ y and MX . y After the second purge event, the modified surface metal atoms are, ideally, completely removed and a clean metallic surface is exposed for the next ALE cycle. However, in reality, some impurities may remain on the surface affecting the overall etch rate.

## S7: Influence of Reactant and Product Pressures

In Table S5 we show the computed adsorption free energy with respect to a change in reactant pressure when the product pressure is set to 0.01 Torr. The values for WCl6 adsorption are much higher than those presented in Figure 4 of main text, because in that figure we showed 0 K values only. This is due to the entropic loss at high temperatures. Three reactant pressure values, 0.05 Torr, 0.2 Torr and 2.0 Torr are chosen for this comparison test. In all these reactions the product state does not contain any gas phase species. It can be seen that the adsorption free energy decreases with increase in reactant pressure. However, this decrease is negligible when compared to the magnitude of the free energy. So, in this case, the contribution from the RTln(Q) term to the free energy change is negligible. Here, WS is bare W(310) surface, WOxS is the oxidized W surface model, WOCl-X are the geometries given in Figure 4 of main text and WOCl2-X are the geometries given in Figure 6 of the main text.

Table S5: Change in adsorption free energy at 500 K reported in the main text (Figure 4) with respect to a change in reactant pressure with the product pressure set at 0.01 Torr.

| Reaction                       | Pr [Torr]   |   Pr [Torr] |   Pr [Torr] |
|--------------------------------|-------------|-------------|-------------|
|                                | 0.05        |        0.2  |        2    |
| (1 WS + 7 O2 -> 1 WOxS )       | -6.12       |       -6.18 |       -6.27 |
| (1 WS + 4.666 O3 -> 1 WOxS )   | -10.95      |      -11.01 |      -11.11 |
| (1 WS + 14 N2O -> 1 WOxS )     | -3.91       |       -3.97 |       -4.07 |
| (1 WOxS + 1 WCl6 -> 1 WOCl-A ) | 2.15        |        2.09 |        2    |
| (1 WOxS + 1 WCl6 -> 1 WOCl-B ) | 2.63        |        2.57 |        2.48 |
| (1 WOxS + 1 WCl6 -> 1 WOCl-C ) | 1.31        |        1.25 |        1.16 |
| (1 WOxS + 1 WCl6 -> 1 WOCl-D ) | 2.87        |        2.81 |        2.72 |
| (1 WOxS + 1 WCl6 -> 1 WOCl-E ) | 3.64        |        3.58 |        3.49 |
| (1 WOxS + 2 WCl6 -> 1 WOCl2-A  | ) 4.36      |        4.24 |        4.05 |
| (1 WOxS + 2 WCl6 -> 1 WOCl2-B  | ) 4.90      |        4.78 |        4.59 |

In Table S6 we show the change in desorption free energy at 500 K with reactant pressure fixed at 0.2 Torr and the product pressure set to 0.001, 0.01 and 2.0 Torr. While the product pressure cannot be changed in an etch reactor and is usually much smaller compared to the

product pressure, we use this analysis for the sake of the comparison of the impact of product pressure. In all these reactions the reactant state does not contain any gas phase species and the product state contains only volatile species. It can be seen that the desorption free energy increases with increase in product pressure (the opposite of reactant pressure change). This implies that the product pressure needs to be low to allow desorption to take place which is ensured by the purge events in the ALE cycle. However, this increase is small when compared to the magnitude of the free energy even for unrealistic large product pressure value of 2.0 Torr. So, also in this case, the contribution from the RTln(Q) term to the free energy change is quite small. WOCl-X are the geometries given in Figure 4 and Figure 6 of the main text.

Table S6: Change in desorption free energy at 500 K reported in the main text in Figures 5 and 6 with respect to a change in product pressure with the reactant pressure set at 0.2 Torr.

| Reaction             |   Pp [Torr] |   Pp [Torr] |   Pp [Torr] |
|----------------------|-------------|-------------|-------------|
|                      |       0.001 |        0.01 |        2    |
| 1 WOCl C 1 WO 2 Cl 2 |      -1.46  |       -1.36 |       -1.13 |
| 1 WO 2 Cl 2          |      -1.02  |       -0.92 |       -0.69 |
| 1 WO 2 Cl 2          |       2.38  |        2.48 |        2.71 |
| 1 WOCl C 1 WO 2 Cl 2 |      -1.46  |       -1.36 |       -1.13 |
| 1 WOCl 4             |       0.44  |        0.54 |        0.77 |
| 1 WOCl C 1 WOCl 4    |      -1.82  |       -1.73 |       -1.5  |
| 1 WO 2 Cl 2          |       0.54  |        0.63 |        0.86 |
| 1 WOCl E 1 WOCl 4    |      -2.55  |       -2.46 |       -2.23 |
| 1 WO 2 Cl 2          |      -1.02  |       -0.92 |       -0.69 |
| 1 WOCl 2 B 1 WOCl 4  |      -2.79  |       -2.7  |       -2.47 |
| 1 WOCl 4             |      -2.6   |       -2.51 |       -2.28 |
| 1 WOCl 4             |      -1.19  |       -1.09 |       -0.86 |
| 1 WOCl 2 B 1 WOCl 4  |      -2.79  |       -2.7  |       -2.47 |
| 1 WOCl 4             |      -2.6   |       -2.51 |       -2.28 |
| 1 WO 2 Cl 2          |      -1.55  |       -1.45 |       -1.22 |
| 1 WO 2 Cl 2          |       2.7   |        2.8  |        3.03 |

## S8: Cl 2 in the Material Removal Pulse

Figure S11: Cl 2 adsorbs weakly with the WO x surface, due to net repulsion between the O and Cl atoms, with a binding energy of just -0.05 eV. On dissociation and adsorption at W sites, an energy of -3.11 eV to -3.92 eV is released per Cl 2 molecule. From the resulting WO Cl surface, the volatile species WOCl x y 4 and WO Cl 2 2 can be desorbed but require energies of 0.73 eV and 1.33 eV, respectively. The energy gained from Cl 2 dissociation clearly offsets this energy requirement. Wis shown in blue, O in red and Cl in green.

<!-- image -->

## References

- (1) Tkatchenko, A.; Scheffler, M. Accurate Molecular Van Der Waals Interactions from Ground-State Electron Density and Free-Atom Reference Data. Phys. Rev. Lett. 2009 , 102 , 073005.
- (2) Keene, B. Review of data for the surface tension of pure metals. International Materials Reviews 1993 , 38 , 157-192.
- (3) Mills, K. C.; Su, Y. Review of surface tension data for metallic elements and alloys: Part 1-Pure metals. Int. Mater. Rev. 2006 , 51 , 329-351.
- (4) Tran, R.; Xu, Z.; Radhakrishnan, B.; Winston, D.; Sun, W.; Persson, K. A.; Ong, S. P. Surface energies of elemental crystals. Scientific data 2016 , 3 , 1-13.
- (5) Allouche, A. First principles calculations on nitrogen reactivity on tungsten surfaces. J. Phys.: Condens. Matter 2015 , 28 , 015001.
- (6) Henkelman, G.; Jonsson, H. Improved tangent estimate in the nudged elastic band method for finding minimum energy paths and saddle points. J. Chem. Phys. 2000 , 113 , 9978-9985.
- (7) Henkelman, G.; Uberuaga, B. P.; Jonsson, H. A climbing image nudged elastic band method for finding saddle points and minimum energy paths. J. Chem. Phys. 2000 , 113 , 9901-9904.
- (8) Mullins, R.; Kondati Natarajan, S.; Elliott, S. D.; Nolan, M. Self-Limiting Temperature Window for Thermal Atomic Layer Etching of HfO2 and ZrO2 Based on the AtomicScale Mechanism. Chem. Mater. 2020 , 32 , 3414-3426.