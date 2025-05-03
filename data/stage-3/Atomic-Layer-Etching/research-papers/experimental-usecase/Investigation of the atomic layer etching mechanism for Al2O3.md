## Journal of Materials Chemistry C

## PAPER

<!-- image -->

C

ite this: J. Mater. Chem. C , 2025, 13 , 1345

Received 23rd August 2024, Accepted 14th November 2024

DOI: 10.1039/d4tc03615h rsc.li/materials-c

<!-- image -->

View Article Online View Journal | View Issue

## Investigation of the atomic layer etching mechanism for Al2O3 using hexafluoroacetylacetone and H2 plasma †

Nicholas J. Chittock, ab

Joost F. W. Maas,

a

Ilker Tezsevin,

<!-- image -->

Marc J. M. Merkx,

a

Harm C. M. Knoops,

<!-- image -->

Wilhelmus M. M. (Erwin) Kessels

<!-- image -->

<!-- image -->

and Adriaan J. M. Mackus

*

a

Atomic layer etching (ALE) is required to fabricate the complex 3D structures for future integrated circuit scaling. To enable ALE for a wide range of materials, it is important to discover new processes and subsequently understand the underlying mechanisms. This work focuses on an isotropic plasma ALE process based on hexafluoroacetylacetone (Hhfac) doses followed by H2 plasma exposure. The ALE process enables accurate control of Al2O3 film thickness with an etch rate of 0.16 /C6 0.02 nm per cycle, and an ALE synergy of 98%. The ALE mechanism is investigated using Fourier transform infrared spectroscopy (FTIR) and density functional theory (DFT) simulations. Different diketone surface bonding configurations are identified on the Al2O3 surface, suggesting that there is competition between etching and surface inhibition reactions. During the Hhfac dosing, the surface is etched before becoming saturated with monodentate and other hfac species, which forms an etch inhibition layer. H2 plasma is subsequently employed to remove the hfac species, cleaning the surface for the next half-cycle. On planar samples no residue of the Hhfac etchant is observed by FTIR after H2 plasma exposure. DFT analysis indicates that the chelate configuration of the diketone molecule is the most favorable surface species, which is expected to leave the surface as volatile etch product. However, formation of the other configurations is also energetically favorable, which explains the buildup on an etch inhibiting layer. The ALE process is thus hypothesized to work via an etch inhibition and surface cleaning mechanism. It is discussed that such a mechanism enables thickness control on the sub-nm scale, with minimal contamination and low damage.

## 1. Introduction

alternating between these self-limiting steps, the etch depth is accurately controlled by the number of cycles.

Isotropic atomic layer etching (ALE) is attracting increasing attention due to its ability to accurately control etch thickness with minimal damage or contamination of the film, qualities which are vital for advanced integrated circuit manufacturing. 1-5 ALE achieves these requirements through sequentially self-limiting half-cycles, which constitute an ALE cycle. 1-3 A typical ALE process involves the modification of a thin surface layer in half-cycle A, as shown in Fig. 1(a). This modified layer is then selectively removed in half-cycle B, stopping once the bulk material is reached. 6 By

a Department of Applied Physics, Eindhoven University of Technology, P.O. Box 513, 5600 MB Eindhoven, The Netherlands. E-mail: A.J.M.Mackus@tue.nl

b Oxford Instruments Plasma Technology, Severn Beach, Bristol, BS35 4GG, UK

† Electronic supplementary information (ESI) available: Additional details on the continuous etch component in half-cycle A, temperature dependence of EPC, roughness reduction, simulated bond vibrational frequencies for Hhfac on Al2O3, total Hhfac absorbance spectra, rotation of dihedral Hhfac bond, and adsorption energies of Hhfac on a bare-Al2O3 slab. (PDF). See DOI: https://doi.org/10.1039/ d4tc03615h

T

Already many ALE processes have been developed based on the approach of surface modification and removal. 7-22 The most investigated isotropic ALE mechanism is that of fluorination and ligand-exchange, for example for ALE of Al2O3. 7,17-22 In such a process, typically hydrogen fluoride (HF) or a Fcontaining plasma is dosed in half-cycle A until a saturated thickness of metal fluoride is formed at the surface. In halfcycle B a metal-organic etchant molecule, for example trimethylaluminum (TMA, Al(CH3)3), removes the modified layer. Volatile species are formed through a ligand-exchange reaction, where ligands are transferred from the etchant to the surface. One of the challenges for the use of such a process in device fabrication is contamination of the surface after ALE, either because of incomplete removal of the modified layer leaving behind an oxyfluoride surface, or because the metal etchant molecule introduces undesired metal atoms to the sample surface. 16 Additionally, high halide exposure can impact stability/performance of reactors, which then requires cleaning,

Fig. 1 (a) General schematic of an ALE cycle relying on surface modification and ligand exchange, which often leads to a very thin residual contaminated layer at the surface. (b) Etch inhibition and surface clean mechanism, where the etching process self-limits due to formation of an etch inhibition layer. The inhibition layer can then be cleaned away to enable etching in the next cycle.

<!-- image -->

leading to tool down-time. 6,23,24 As an alternative, some processes based on modification and ligand-addition have been investigated. 25,26 Rather than dosing a metal-organic molecule as in ligand-exchange, ligand-addition involves dosing the desired ligands directly onto the surface. The mechanism relies on the surface first being modified in half-cycle A, for example by chlorination. In half-cycle B an organic ligand is used to volatilize the modified surface, such as trimethylphosphine (P(CH3)3) or tetramethylethylenediamine (TMEDA). The mechanism of modification and ligand addition has been shown to be effective for Ni, NiO, CoO, ZnO and Fe2O3. 25,26 Although this approach avoids contamination of the etch surface or reactor from a metal-organic etchant, modification of the film is necessary, which may still leave undesired residues.

A group of molecules that is being researched as the etchant for ligand-addition ALE is diketones. The general structure of a diketone molecule is shown in Fig. 2(a). The modification and ligand-addition chemistry with diketones is effective for ALE of metallic films, where typically the first half-cycle is an oxidation or chlorination step to change the oxidation state from the zero state. Once the metal atom is in a higher oxidation state, volatile species can be formed by chelation ( i.e. forming two coordinate bonds with a metal atom) in the second halfcycle. 8,10,13,27-29 Furthermore, diketones are tunable molecules, and by adjusting R groups as shown in Fig. 2, the etch rate or selectivity could be tailored in three ways: (i) larger R-groups limit the density of molecules that can bind on the surface due to steric effects. 30 (ii) More/less electrophilic R-groups affect how strongly bound the H of the hydroxyl group is, adjusting how acidic the molecule behaves. 30-32 (iii) The volatility of the diketone can be enhanced by increasing intermolecular repulsion between the R-groups, which may promote higher etch rates and lower operating temperatures due to formation of more volatile reaction products. 30,33 Previously, diketones have been researched as atomic layer deposition (ALD) precursor

## Journal of Materials Chemistry C

## (a) General diketone structure

R1,2 =

<!-- image -->

## (b) Hexafluoroacetylacetone (Hhfac)

Fig. 2 (a) The general structure of a diketone molecule, where R1 and R2 can be the same or different terminal groups. The molecule is a keto-enol tautomer; in gas phase enol is the more stable configuration for many diketones. 32 (b) Structure of the hexafluoroacetylacetone (Hhfac) molecule used in this work. Hhfac exists nearly exclusively in the enol form, as shown in the figure. 32

<!-- image -->

ligands, as chemical etchants for metal oxide films, and as inhibitor molecules for area-selective ALD (AS-ALD). 7,8,27,33-43 This large knowledge base can be leveraged to better understand the surface reactions and mechanism for ALE, and to identify materials for which an ALE process will be viable. Previous AS-ALD work has shown that diketones preferentially react with alkaline OH groups on surfaces, and do not readily react with acidic OH groups, potentially helping to predict selectivity of a diketone ALE process. 36,38,44,45 Additionally, diketones can bind to surfaces in multiple configurations. 44 For AS-ALD, the different surface bonding configurations were found to play an important role in determining the effectiveness of precursor blocking. 36,44

Previous work has shown that continuous etching of metal oxides can be achieved by dosing the diketone at high pressure, 40-42 suggesting that diketones cannot be used for ALE of metal oxides directly. There have, however, been reports in the literature of ALE processes for ZnO and CoO based on diketone etching. 34,46 The mechanism for metal oxide ALE is hypothesized to follow an etch inhibition and surface cleaning chemistry, as shown in Fig. 1(b). Mameli et al. demonstrated that alternating doses of the diketone acetylacetone (Hacac) and O2 plasma can isotropically etch ZnO. 34 Al2O3 was also found to be etched by this chemistry, resulting in an etch per cycle (EPC) of 0.015 nm at 250 1 C. 34 The ALE mechanism was not investigated in detail, but it was suggested that the Hacac first etches the surface and then forms a carbon-containing layer that needs to be removed by an O2 plasma half-cycle. Similarly, Partridge et al. showed that CoO ALE is possible using alternating Hacac and ozone (O3) exposures. The selflimiting etching behavior was associated with the formation of a carbon layer on the CoO surface, which is then removed by O3 exposure. Dosing only Hacac results in a slow etch rate of

0.008 nm per dose, but an EPC of 0.043 nm is achieved when cycling Hacac and O3 doses. After O3 exposure, the CoO had an oxidized surface of Co3O4 which is reduced back to CoO by Hacac exposure. The removal of the oxidized surface layer is suggested to contribute to the self-limiting nature. 46 The controlled ALE behavior reported in these studies is interesting to investigate further as previous metal oxide etching literature suggests continuous etching should occur. 28,40-42

The goal of this work is to outline an ALE process for metal oxides relying on diketone exposure and surface cleaning. An ALE chemistry of alternating hexafluoroacetylacetone (Hhfac) and H2 plasma exposures is investigated. 34 Hhfac is utilized instead of Hacac due to the lower melting point and higher vapor pressure of Al(hfac)3 compared to Al(acac)3, which are possible volatile reaction products for each diketone, respectively. 30 The structure of Hhfac is shown in Fig. 2(b), where the acronym Hhfac denotes the full molecule and hfac the deprotonated form. As previous AS-ALD work has shown that a H2 plasma is more effective for the removal of diketone species than an O2 plasma, 45 the suitability of H2 plasma for diketone ALE is also tested. Development of this ALE chemistry is performed with the intention to understand the mechanism focusing on two main research questions. Firstly, how does Hhfac adsorb on an Al2O3 substrate during the ALE process? Secondly, what is the mechanism for self-limiting etching using diketone species on a metal oxide surface? These questions were explored through in situ Fourier transform infrared (FTIR) spectroscopy studies and density functional theory (DFT) simulations.

## 2. Method

## 2.1. ALE process development

An Oxford Instruments FlexAL reactor with an inductively coupled plasma source, as shown in Fig. 3(a), was used for both ALD and ALE in this work. Al2O3 samples were grown on

4-inch Si wafers by plasma ALD using trimethylaluminium (TMA) and O2 plasma as reactants, with a table temperature of 300 1 C and wall temperature of 150 1 C. Further details of the reactor and Al2O3 plasma ALD process can be found in previous reports. 47,48 ALD was performed for 200 cycles, after which the wafer was diced into approximately 2 /C2 2 cm 2 coupons and placed on a 4-inch carrier wafer for ALE processing. Prior to both ALD and ALE processing, samples were heated for 10 minutes while maintaining the chamber pressure at 300 mTorr with Ar gas. After the preheat, all samples were exposed to O2 plasma for 2 minutes at 50 mTorr with 200 W ICP power. The ALE process was performed at a table temperature of 350 1 C and wall temperature of 150 1 C. It is expected that the actual sample temperature is lower than 350 1 C due to limited heat transfer from the heated table, through the carrier wafer and to the sample at low pressure. The relationship between the table set point temperature and sample temperature during low-pressure plasma processing has been discussed in more depth elsewhere. 49 A relatively high table temperature of 350 1 C was used to facilitate etching, as previously etching with diketones has been shown to proceed more easily at high temperature. 28,40 Based on continuous etching studies, 350 1 C is near the decomposition temperature of Hhfac, 31,40 which may be beneficial for the self-limiting behavior as is discussed in more detail later in this work.

The ALE process consists of a Hhfac dose/hold half-cycle followed by a H2 plasma half-cycle, as shown in Fig. 4, with the chamber continuously pumped by a turbo molecular pump. Plasmas are increasingly being used for isotropic ALE, offering low temperature etch processes, higher etch rates, and the ability to etch materials that are typically more resistant to etching. 16-19,29,34,50-52 For the plasma step to be isotropic in nature, there should be no substrate biasing during the plasma exposure such that only ions with a low ion energy arrive at the substrate. 16,19 The H2 plasma used in this work for the surface

<!-- image -->

Fig. 3 Schematic representations of the reactors used in this work: (a) an Oxford Instruments FlexAL reactor and (b) a home-built ALD reactor equipped with an in situ FTIR setup, shown here in transmission mode for powder samples. The angle of the IR mirrors on the detector and source side can be adjusted such that planar samples can be studied in reflection mode. Both systems are pumped with turbo pumps and use an inductively coupled plasma source supplied with 13.56 MHz RF power.

<!-- image -->

|

Fig. 4 Schematic of the ALE process used in this work. Half-cycle A consists of Hhfac dose/hold steps, which are repeated 15 times per cycle (unless stated otherwise). Half-cycle B is the H2 plasma at a pressure of 300 mTorr and 600 W power. Each half-cycle is followed by a 10 s Ar purge with the APC fully open for maximum pumping efficiency.

<!-- image -->

cleaning half-cycle is based on previous AS-ALD literature where the plasma step is used to remove acac ligands from an Al2O3 surface. 45 The chamber pressure in the FlexAL is controlled by an automated pressure controller (APC). The angle of the butterfly valve in the APC is automatically adjusted such that the pressure in the chamber is maintained at a set value. Use of an APC enables high chamber pressures with low gas flows, which helps maximize residence time of reactant species. 34,53 Hhfac (Sigma-Aldrich, 98%) was held in a stainlesssteel bubbler at room temperature and then vapor-drawn into the reaction chamber. Hhfac is dosed into the reactor for 50 ms with the chamber pressure set to 400 mTorr. The Hhfac hold is then 2 s with the chamber pressure kept at 400 mTorr before the next 50 ms Hhfac pulse. The hold step is implemented to increase the exposure of the etchant Hhfac to the surface and facilitate the etching reaction. To prevent backflow of the Hhfac into the ICP tube during the hold step, there is a constant 10 sccm Ar flow through the ICP tube. As such, the butterfly valve remains partially open, leading to some of the Hhfac being pumped away during the hold step. Saturation of the Hhfac step is measured as a function of dose/hold pulses rather than as a function of the dose time. After the dose/hold pulses, the reactor is purged for 10 s with an Ar flow of 200 sccm through the ICP tube, with the APC fully open for maximum pumping efficiency. Before the plasma exposure, a 5 s preplasma step is included to stabilize the gas flow of 100 sccm H2 through the ICP at a pressure of 300 mTorr. The plasma is then struck at an ICP power of 600 W, with the on time varied to determine saturation of the plasma half-cycle. Following the H2 plasma, the reactor is purged with 200 sccm Ar with the APC fully open for 5 s.

During ALD and ALE cycles the film thickness was monitored in situ using a M-2000 J. A. Woollam spectroscopic ellipsometer (SE) with a photon energy range 1.2-4.9 eV installed at a 70 1 angle. A Cauchy model was used to fit the Al2O3 film thickness. After a short exposure of Hhfac an increase in film thickness is observed ( B 0.04 nm) which is attributed to adsorbed hfac species. The adsorbed hfac layer was not defined as a separate layer in the model as the optical properties of the adsorbed diketone layer are not known. Atomic force microscopy (AFM) measurements were performed on the Dimension Icon AFM manufactured by Bruker in ScanAsyst mode using a PeakForce-Air tip. The scan frequency was set to 1 Hz and the scan area was 1 /C2 1 m m 2 .

## 2.2. FTIR studies

Infrared spectroscopy studies were performed on a homebuilt ALD reactor, shown in Fig. 3(b), which is described in detail in ref. 51 and 54. The set-up is equipped with an Invenio S Bruker Fourier transform IR spectrometer with Globar IR source and a liquid N2 cooled mercury cadmium telluride (MCT) detector with a spectral range of 12000-800 cm /C0 1 . For transmission studies SiO2 powder was pressed into a W mesh and heated by passing a DC current through the mesh, with the temperature measured by a thermocouple wire bonded to the mesh. The SiO2 powder sample is then coated with Al2O3 by thermal ALD for 30 cycles, using TMA and H2O at 300 1 C. Further details on the FTIR set-up and sample preparation can be found in ref. 36. As the powder is directly heated in the mesh, a colder temperature of 300 1 C is used for the FTIR ALE study, comparable to the actual sample temperature during process development studies. Hhfac was dosed in static conditions for 20 ms with the gate valves at the top and bottom of the reactor vessel closed. Hhfac was then held in the reactor for 2 s before opening the gate valve to the pump. The top gate valve is then opened, and the chamber is purged with Ar for 10 s before an FTIR measurement was taken. H2 gas flow was controlled via a needle valve to give a chamber pressure of 100 mTorr with both gate valves open. After 5 s of gas stabilization, the H2 plasma was struck using an ICP power of 300 W. A lower ICP power is utilized on the homebuilt system, due to differences between the homebuilt system and the FlexAL system. The chamber is then purged for 10 s with Ar. During an FTIR measurement the chamber was pumped without gas flow. Spectra presented in this work are difference spectra referenced either to a common starting surface, or to the previous

measurement to investigate changes in surface bound species. In FTIR analysis of a surface, the presence of a positive peak in the spectrum indicates the addition of species to the surface, while a negative peak denotes removal of species from the surface.

Planar samples were also employed for FTIR studies, utilizing the FTIR set-up on the homebuilt system in reflection mode. Samples were prepared on a planar Al substrate using the same thermal Al2O3 ALD process as for the powder samples. Here the sample is placed directly onto the substrate table, which is heated to 300 1 C. A lower temperature is employed as the heat is transferred directly from the table to the sample, instead of through a carrier wafer. 49

## 2.3. Computational methods

The Vienna ab initio Simulation Package (VASP, version 5.4.4) was used to perform all density functional theory (DFT) calculations reported in this study. 55-57 The projector augmented wave (PAW) method was employed to describe electron-ion interactions. 58,59 Calculations were performed based on Perdew-Burke-Ernzerhof (PBE) exchange-correlation functional of the generalized gradient approximation (GGA), and the influence of the van der Waals interactions were considered by the dispersion correction D3 and the Becke-Johnson (BJ) damping function. 60-62 A kinetic energy cutoff of 400 eV was used for the plane-wave basis set. The convergence criteria for structural optimizations were set such that the total forces acting on each atom must be smaller than 0.01 eV Å /C0 1 . Convergence criteria for the self-consistent-field cycle was set to 10 /C0 5 eV. Gaussian smearing of 0.01 eV was used throughout the study. The Brillouin zone of crystalline Al2O3 bulk was integrated using an automatically generated G centered 11 /C2 11 /C2 5 k -point mesh, whereas a G centered 2 /C2 2 /C2 1 MonkhorstPack grid was used for the surface calculations. 63 A 4-layer 3 /C2 3 supercell of a -Al2O3(0001) was modeled following the same procedure as our previous works. 36,45,64 Periodicity of the slab in the direction perpendicular to the surface was avoided by adding a vacuum spacing of 15 Å. The resultant supercell has the a , b , c lattice dimensions of 14.21 Å, 14.21 Å, and 26 Å, respectively with y = 120 . To achieve a hydroxylated Al2O3 1 (0001) surface, the Al2O3 surface is partially hydroxylated by locating hydroxyl groups on all 9 top layer Al atoms, resulting in a 1 monolayer OH coverage (corresponding to 5.1 OH nm /C0 2 ). This is slightly less than the experimentally observed value of 7.1 OH nm /C0 2 65 , which is due to the difference between an amorphous surface and the perfectly crystalline surface employed for simulations. In order to balance the negative charge from the addition of OH, 9 out of the 18 exposed O atoms neighboring the top layer Al atoms are hydrogenated. The bottom two Al2O3 layers were kept frozen at their bulk positions. More than 20 different starting configurations were studied for the Hhfac adsorption of which the resulting unique configurations are reported here. The Hhfac adsorption energies were calculated using

$$\Delta E _ { a d s } = E _ { s l a b + H h f a c } - ( E _ { s l a b } + E _ { H h f a c } ).$$

where E slab+Hhfac is the total energy of the (hydroxylated) Al2O3 (0001) slab with adsorbed Hhfac at its lowest energy position on the surface, E slab is the total energy of a clean slab, and E Hhfac is the energy of an isolated Hhfac molecule. The energy of the isolated Hhfac molecule was computed via spin relaxed calculations in 20 Å cubic cells at the gamma point. The inputs for the adsorption geometries were prepared using Maestro Materials Science 5.0.122, Release 2023-2, whereas all visual representations of the computed geometries were prepared using Vesta v.3.5.7. 66,67

## 3. Results

## 3.1. ALE process development

The self-limiting nature of the half-cycles is investigated on planar samples using in situ SE to assess whether controlled etching can be achieved. Saturation curves for both half-cycles at 350 1 C table temperature can be seen in Fig. 5. For each data point, 25 cycles of ALE were performed, and the film thickness was measured every 5 cycles. Hhfac saturation is shown in Fig. 5(a) as a function of the number of 50 ms Hhfac pulses per cycle, while using a 25 s H2 plasma in half-cycle B. Initially, the EPC increases quickly and then appears to saturate after 15 pulses per cycle. Slight softsaturation of the Hhfac step may be occurring as is discussed in Section 3.2. Similar soft-saturation behavior has been observed previously for etching with diketones. 41,46 The H2 plasma saturation curve (for 15 /C2 50 ms pulses of Hhfac per cycle) in Fig. 5(b) shows that saturation occurs at 25 s H2 plasma. The combination of soft-saturation for the Hhfac half-cycle and saturation for the H2 plasma half-cycle gives controlled etching of Al2O3 with an EPC of 0.16 /C6 0.02 nm at 350 1 C.

To confirm the controlled nature of this ALE process, a synergy test is performed, as shown in Fig. 6. Synergy is an

Fig. 5 Saturation curves at 350 1 C for (a) Hhfac pulses using a 25 s H2 plasma and (b) H2 plasma exposure using 15 /C2 50 ms pulses of Hhfac per cycle. The lines are guides to the eye.

<!-- image -->

J. Mater. Chem. C

13

, 1345GLYPH&lt;129&gt;1358

|

important parameter for ALE, demonstrating that etching should only occur when alternating between the two reactants. 1 The synergy parameter, S , is defined as

$$S = \frac { E P C - ( \alpha + \beta ) } { E P C } \times 1 0 0$$

where EPC is the ALE etch per cycle, and a and b the continuous etch components from half-cycle A and B, respectively. 1 Fig. 6(a) shows the change in film thickness when only exposing the substrate to Hhfac half-cycles (half-cycle A). Over the 25 steps there is a small thickness decrease of 0.08 nm, corresponding to an a value of 0.003 /C6 0.001 nm per step. This small continuous etch component is shown more clearly in Fig. S1 (ESI † ), and can explain why there is soft-saturation of the Hhfac exposure in Fig. 5(a). Additionally, a small increase (0.04 nm) in film thickness is observed after the first Hhfac pulse which is due to adsorption of Hhfac on the surface. Repeated exposure to the H2 plasma step, shown in Fig. 6(b), gives a negligible thickness change after 25 pulses of H2 plasma, yielding a b value of 0.001 /C6 0.001 nm per step. Fig. 6(c) shows the change in thickness when performing full ALE cycles. A linear fit through the points gives an EPC value of 0.17 /C6 0.01 nm, in agreement with the saturation curves in Fig. 5. Using the etch rates determined from Fig. 6(a)-(c), a synergy value of 98% is calculated. The high synergy value highlights that this ALE process is near ideal, with minimal continuous etching components.

Furthermore, the effect of table temperature was investigated as reported in Fig. S2 (ESI † ), demonstrating that high process temperatures result in a higher EPC. For table temperatures of 250 1 C and 300 1 C the EPC is 0.04 /C6 0.01 nm and 0.08 /C6 0.01 nm, respectively. Similar temperature-dependent etch behavior has been observed using diketones for continuous etching, 40 ALE of metals, 7,8,10 and metal oxide ALE. 34,46 Interestingly, the EPC for the Hhfac ALE process at 250 1 C (0.04 /C6 0.01 nm) is higher than the 0.015 nm reported for a similar Hacac/O2 plasma process at the same temperature. 34

Fig. 6 Thickness evolution as a function of pulses/cycles for (a) only Hhfac dosing, (b) only H2 plasma exposure and (c) ALD cycles with Hhfac and H2 plasma pulses. Experiments were performed at 350 1 C table temperature.

<!-- image -->

## Journal of Materials Chemistry C

This higher EPC could be attributed to some combination of different aspects such as enhanced surface cleaning by the H2 plasma, higher volatility of the etch product, or in situ F radical production from dissociation of hfac ligands. More effective surface cleaning by H2 plasma compared to O2 plasma has been observed in AS-ALD. 45 Enhanced removal of the surface inhibiting layer reduces steric hinderance during the next Hhfac dose, thus facilitating etching. 45 Additionally, the higher volatility of the proposed etch product (Al(hfac)3 compared to Al(acac)3) may enable the etch product to leave the surface more easily, allowing for more etching to occur before surface inhibition. 30,33 Potential fluorination of the surface to AlF x can increase the etch rate as will be discussed further in Section 3.4.

Important characteristics of an ALE process are the abilities to smooth surfaces and to etch selectively. These two qualities are often required for integration into device fabrication flows. 1-6 The roughness of the Al2O3 film was observed to decrease with the etched thickness. After 3 nm of ALE the RMS roughness decreased from 0.50 /C6 0.07 nm to 0.24 /C6 0.07 nm, with the roughness value approaching that of the Si substrate underneath (0.20 /C6 0.05 nm), as shown in Fig. S3 (ESI † ). 1,2,68 Selectivity is desired such that the ALE process does not etch masks or other functional layers of the device. The selectivity of the Hhfac/H2 plasma ALE chemistry for etching Al2O3 with respect to SiO2 was tested at 300 1 C. Fig. 7(a) shows the etched thickness as a function of ALE cycles for SiO2 and Al2O3 films exposed to the Hhfac/H2 plasma ALE process. There is negligible change in the SiO2 film thickness after 10 ALE cycles, highlighting that the Hhfac/H2 plasma ALE process allows for near perfect selectivity between SiO2 and Al2O3. The high selectivity is attributed to a lack of Hhfac adsorption on the SiO2 surface.

To support our hypothesis for selective etching, FTIR spectra for SiO2 and Al2O3 films after exposure to Hhfac are compared. Both films are exposed to a 100 ms Hhfac dose and referenced to their respective as-deposited surface, as shown in Fig. 7(b). The graph highlights the selective adsorption: Al2O3 has peaks indicating hfac adsorption, as well as a reduction in absorbance around the Al-O bond region. In contrast, on the SiO2 film no change is observed after the Hhfac exposure. For the Al2O3 surface there is also a decreased absorbance at 2940 cm /C0 1 and 3700 cm /C0 1 , which are attributed to the removal of CH3 and OH groups, respectively. The CH3 groups are likely coming from unreacted ligands from the ALD process that are removed by the H2 plasma half-cycle, while OH groups are consumed due to the diketone reaction with the surface, as is discussed in Sections 3.2 &amp; 3.3. There is no change in the spectrum in these regions for the SiO2 surface, which is further evidence that the diketone Hhfac is not reacting with the surface. The selectivity observed here for Hhfac is similar to results from AS-ALD studies, where the diketone Hacac was shown not to adsorb on an acidic SiO2 surface, while strongly bonding to more alkaline surfaces like Al2O3. 36,38,44 The spectra in Fig. 7(b) support the hypothesis that the selective etching in this work is enabled by a lack of Hhfac adsorption on SiO2. Furthermore, these observations suggest that a diketonebased ALE chemistry would not etch materials with acidic OH groups, such as GeO2 and WO , while selectively etching materials x with alkaline OH groups like CoO x and CuO . x 38,43

Fig. 7 (a) Etched thickness as a function of ALE cycles using 15 pulses of Hhfac dose/hold and 25 s H2 plasma each cycle. Experiments were performed at 300 1 C table temperature, yielding an EPC of 0.08 /C6 0.01 nm per cycle. (b) Reflection mode absorbance spectra for Al2O3 and SiO2 planar films exposed to a 100 ms Hhfac dose, referenced to their as-deposited surfaces. The Al-O and hfac absorbance regions are highlighted in the figure.

<!-- image -->

Reduced surface contamination post etching is an anticipated benefit of ALE compared to conventional etch techniques. 1,2 The potential surface contamination from the ALE process is investigated by performing FTIR measurements on planar samples. An FTIR spectrum was taken after each full ALE cycle, with the spectrum of the as-deposited Al2O3 acting as the reference as illustrated in Fig. 8(a). The spectra taken over the 5 ALE cycles shows evidence of etching as the Al-O bond absorbance decreased with each cycle. The lack of peaks in the spectra between 1900-1200 cm /C0 1 , which are indicative of hfac ligands, demonstrates that the 25 s H2 plasma is sufficient for the removal of hfac species from a planar sample. As the only change in the absorbance spectrum over the ALE cycles is removal of Al-O bonds, it can be concluded from Fig. 8 that the ALE process leads to minimal contamination of the film.

## 3.2. Mechanism studies

While the process enables the controlled etching of Al2O3, there is an open question of what the self-limitation mechanism is for the Hhfac half-reaction. To study the ALE mechanism in

Fig. 8 (a) Schematic of the performed experiment to determine whether there is any build-up of Hhfac residue on the Al2O3 surface post ALE. FTIR spectra are referenced to the spectrum for the as-deposited Al2O3 planar film. (b) Spectra taking in reflection mode after full ALE cycles. A cyclic decrease in absorbance for the Al-O bond region is observed. For the rest, the spectrum shows minimal change over the 5 ALE cycles.

<!-- image -->

detail, FTIR studies were performed looking at both the Hhfac and H2 plasma exposures at 300 1 C.

To monitor how the Hhfac binds to the surface during ALE, FTIR measurements were taken for sequential doses of Hhfac as illustrated in Fig. 9(a). The difference spectra for increasing total Hhfac dose times are shown in Fig. 9(b). A decrease in absorbance is observed at 3700 cm /C0 1 , which is attributed to OH consumption during the initial Hhfac adsorption. As Hhfac adsorbs, it is expected that an H atom is transferred from the Hhfac molecule to the surface which may then react with a surface OH group to form volatile H2O. The absorbance in the OH region is not observed to change after 80 ms of Hhfac dosing. There is also a small negative peak at 2940 cm /C0 1 attributed to C-H bonds, which could indicate removal of surface carbon species. At 2163 cm /C0 1 a small positive peak from a surface ketene structure (C QQ C O) is present, perhaps due to decomposition of the hfac species. 31,69 Previously, Hhfac has been shown to decompose and form similar ketene structures on ZnO powder at temperatures of 427 1 C (700 K). 31

Between 1900-1200 cm /C0 1 there is a significant increase in absorbance for the first Hhfac dose, which can be seen in more detail in Fig. 9(d). This absorbance increase suggests many hfac molecules are adsorbed onto the surface in the first pulse. Based on simulated bond vibrational frequencies (Table S1, ESI † ) and literature studies, the contributions of the different diketone bonding configurations were determined. 36 The largest hfac peak at 1656 cm /C0 1 is attributed to hfac bound in monodentate configuration. In contrast, for AS-ALD studies utilizing the diketone Hacac at 150 1 C the dominant bonding configuration is observed to be the chelate configuration. 36 The different surface bonding configurations are shown in Fig. 9(c). For Hhfac adsorption in this study there is a relatively small

.

C

h

e

m

e

r

t

M

a

J

|

## Journal of Materials Chemistry C

<!-- image -->

Fig. 9 FTIR difference spectrum for adsorption of Hhfac on the Al2O3-coated powder. (a) Illustration of the performed experiment. The arrows indicate the reference spectrum for each measurement. (b) The spectra between 4000-900 cm /C0 1 for different dosing times, listing the peaks discussed in the main text. (c) Schematic of the monodentate and chelate bonding configurations of hfac on the surface. (d), (e) Zoom in on the region 1900-1200 cm /C0 1 from panel (a) for (d) the first 20 ms Hhfac pulse and (e) for increasing cumulative Hhfac dose times. In (d) and (e) the main monodentate and chelate peaks are highlighted in the figure.

<!-- image -->

peak at 1571 cm /C0 1 related to the chelate configuration after the first 20 ms pulse. Difference spectra in Fig. 9(e) show that each subsequent Hhfac pulse results in a smaller increase in absorbance between 1900-1200 cm /C0 1 , suggesting each pulse is adding fewer hfac species to the surface. This behavior indicates that the surface is becoming saturated, and that the reaction of Hhfac with the surface is self-limiting. The small change observed after 500 ms total dose time could be due to reorganization of hfac ligands on the Al2O3 surface. Such reorganization may enable the small continuous etch component observed for planar samples (Fig. 6(a)).

Fig. 10 (a) Representation of the procedure performed to analyze the integrated total area in the region 1900-1200 cm /C0 1 . The data is the same as Fig. 9, however all the FTIR spectra are reference to the starting surface, such that the total change in the surface can be measured. (b) Integrated absorbance area between 1900-1200 cm /C0 1 (red, open circles), and the peak area ratio of monodentate (1656 cm /C0 1 ) to chelate (1571 cm /C0 1 ) hfac (blue, closed squares) as a function of Hhfac dose time.

,

2

0

5

,

1

3

4

5

GLYPH&lt;129&gt;

8

The saturation behavior can also be seen by tracking the integrated area of the spectra between 1900-1200 cm /C0 1 as a function of Hhfac dose time. For these measurements the spectra are referenced to the starting surface as shown in Fig. 10(a). The full spectra used as a reference can be seen in Fig. S4 (ESI † ). Initially there is a large increase in the integrated area, suggesting that many hfac ligands are being adsorbed onto the surface. As Hhfac dose time increases, the increase in integrated area after each Hhfac pulse is less than the one before. The increase in integrated area between 450 ms and 500 ms Hhfac dosing is minimal, as can be seen in Fig. 10(b), which indicates that the surface has become saturated with hfac ligands. Determination of the peak area at 1656 cm /C0 1 and 1571 cm /C0 1 allows for comparison of the monodentate and chelate bonding configurations as a function of total Hhfac dose time. The monodentate peak is initially significantly larger than the chelate peak, suggesting that there is a larger amount of monodentate species on the surface after 20 ms. As the total

5

0

2

y

r

t

s

i

m

h

C

f

o

y

t

e

i

c

S

l

a

y

o

R

e

h

T

GLYPH&lt;128&gt;

s

i

l

a

n

r

u

o

j

s

i

h

T

Hhfac dose time increases, the relative amount of monodentate and chelate on the surface changes, with relatively more chelate present as the total dose time increases. Eventually the hfac coverage starts to saturate, with the monodentate configuration remaining to be the dominant surface species once saturation is reached.

For the ALE process to continue, the hfac surface species must be removed by a surface cleaning step, which in this work is performed by H2 plasma. Spectra for increasing H2 plasma exposure time are shown in Fig. 11(b), in which a negative absorbance indicates removal of species from the surface. After 1 minute of H2 plasma, there is a decrease in the absorbance spectra in the 1900-1200 cm /C0 1 wavenumber range, which is due to the removal of hfac ligands from the surface. A decrease in absorbance at 2163 cm /C0 1 is also observed, indicating that the ketene structures are removed. No other significant changes were observed in the spectra recorded during the H2 plasma exposure.

As the H2 plasma exposure time increases there is continued removal of the hfac species from the Al2O3 surface, in agreement with observations from AS-ALD studies. 45 Removal of the hfac species from the Al2O3-coated powder is observed to saturate after 140 minutes of H2 plasma exposure, which is significantly longer than the 25 s used on planar samples. As shown in Fig. 8, a 25 s H2 plasma left no residue on a planar sample. The long plasma exposure time required for the

Fig. 11 (a) Schematic of the performed experiment investigating the effectiveness of H2 plasma at removing hfac ligands adsorbed on the Al2O3 surface. The surface is first functionalized by carrying out a 500 ms Hhfac exposure. The arrows indicate the reference spectrum that is used for each measurement. (b) Spectrum for Al2O3 exposed to 500 ms Hhfac dosing, which is shown such that a comparison to the removal spectra can easily be made. (c) The difference spectra for increasing H2 plasma exposure times referenced to the spectrum in (b).

<!-- image -->

high-surface-area powder sample can be explained by the difference in penetration depth of the Hhfac molecules and H radicals. The Hhfac molecules penetrate deeper, while the H radicals recombine at the surface of the powder. The smaller negative absorbance feature for the H2 plasma removal spectra as compared to the positive peaks from Hhfac adsorption suggests that some hfac species have remained on the powder sample, likely beyond the penetration depth of the H radicals.

As some applications may not be compatible with H2 plasma exposure, alternative plasma chemistries for the surface cleaning half-cycle should be explored. Previous AS-ALD literature suggests that O2 plasma can be used for surface cleaning, however it is not as effective as H2 plasma in completely removing ligands bound to the surface. 45 Additionally, isotropic ALE of ZnO using alternating exposures of Hacac and O2 plasma has been demonstrated. 34 Thus, it is expected that O2 plasma could be a viable alternative for H2 plasma. Removal of hfac ligands from an Al2O3 surface with O2 plasma is tested in the work, as shown in Fig. S5 (ESI † ). The FTIR data indicates that O2 plasma can remove the hfac ligands from the Al2O3 surface and would therefore likely be a viable alternative reactant to H2 plasma.

## 3.3. Simulation results on Hhfac adsorption

DFT studies were employed to understand the surface reactions and bonding configurations of hfac on Al2O3 in more detail. Considering an OH-functionalized Al2O3 surface, it was observed that physisorption of the Hhfac is energetically favorable, agreeing with the experimental observation that Hhfac adsorbs on an Al2O3 surface. Physisorption can occur with both Oatoms pointing toward the surface as in Fig. 12(a), or with the C-chain twisted and only one O pointing towards the surface, Fig. 13(a). Both routes are energetically favorable, however the configuration in Fig. 12(a) is more favorable ( D E ads = /C0 0.60 eV vs. D E ads = /C0 0.18 eV).

Considering the more favorable physisorption configuration in Fig. 12(a), there are two possible pathways which both lead to the H from the Hhfac being transferred to the surface, generating H2O as shown in Fig. 12(b) and 12(c). The molecule can directly bind in the monodentate configuration ( D E ads = /C0 0.87 eV) as shown in Fig. 12(c), or it can take a more energetically favorable configuration ( D E ads = /C0 0.96 eV) with both O atoms pointing at the surface as in Fig. 12(b). In the lower energy configuration shown in Fig. 12(b), the surface bound H2O helps to stabilize the de-protonated hfac through hydrogen bonds. 44 From the configuration in Fig. 12(b) the hfac molecule can bind to a surface Al atom, either by transitioning through a monodentate configuration (Fig. 12(c)) with a minimum thermodynamic barrier of 0.09 eV, or directly to the chelate configuration (exothermic, D E = /C0 0.45 eV) shown in Fig. 12(d). The monodentate configuration may thereby act as a transition state with an activation barrier of D E = 0.09 eV towards forming the chelate bound species.

The energetically favorable conversion from the physisorbed to the chelate configuration suggests that if there is space on the surface, the hfac ligands will bind in the chelate configuration. The DFT analysis however does not consider potential

.

C

h

e

m

e

r

t

M

a

J

|

Fig. 12 Adsorption pathway for Hhfac on a hydroxylated Al2O3 surface. (a) Hhfac molecule initially physisorbs to the surface. (b) Donation of H from Hhfac to the surface, forming H2O on the surface. (c) The hfac ligand bound in monodentate configuration, with the H2O still bound to the surface. (d) Chelate configuration of the hfac ligand, with both O atoms bound to the same surface Al atom. Adsorption energies for each configuration are shown beneath the images. The arrows indicate potential transitions on the surface and the difference in energy between two configurations.

<!-- image -->

Fig. 13 (a) Physisorption of a Hhfac molecule onto an OH-terminated Al2O3 surface where only one O atom is directed towards the surface. From configuration (a) the Hhfac can transition into (b) a monodentate bound configuration with an OH group directed away from the surface.

<!-- image -->

steric hinderance of neighboring hfac surface species or detailed investigation of the energy barriers, which would require nudged elastic band analysis. It is interesting that experimentally the dominant configuration in the FTIR spectrum during the initial doses is monodentate bound hfac, as simulations suggest that chelate is more favorable. The implication of these observations are discussed in Section 3.4.

The pathway shown in Fig. 12 can lead to the formation of chelate bound species, which are hypothesized to be important for the etching reaction in the first half-cycle. 34 However, to enable the controlled nature of ALE the etching reaction must also eventually self-limit. Thus, it is interesting to look at potential pathways for generating other hfac bonding configurations during the Hhfac half-cycle. Considering Hhfac adsorption where only one of the O atoms is pointing towards the surface, a less energetically favorable physisorption configuration is found, as shown in Fig. 13(a). The molecule can transition from the physisorbed to an adsorbed configuration (exothermic, D E = /C0 0.07 eV) by transferring a H atom to a surface OH group and forming H2O, as can be seen in Fig. 13(b). From the monodentate configuration in Fig. 13(b) it is unlikely that the molecule will transition into a chelate configuration, as it would require a 180 1 rotation of the C chain. Rotation of the C chain in the gas-phase has an energy barrier of 4 1 eV, as shown in Fig. S6 (ESI † ), and is therefore unlikely to occur when the molecule is adsorbed on the surface. The monodentate configuration shown in Fig. 13(b) is expected to remain in this configuration and contribute solely to surface inhibition. By not having a viable pathway to the chelate configuration, the configuration in Fig. 13(b) may facilitate the formation of an etch-inhibition layer on the Al2O3 surface, and thus enable the self-limiting behavior.

## 3.4. Discussion

The main goals of this work were to determine if Hhfac and H2 plasma can be used to perform ALE of Al2O3, to understand how diketones bind to metal oxide surfaces, and to investigate the self-limiting mechanism of the diketone half-cycle. These first two research goals were achieved in Sections 3.1 and 3.2, 3.3, respectively. In this section, we discuss the possible etch products and present the hypothesized self-limiting mechanisms of both half-cycles.

The proposed etch product for this ALE chemistry is Al(hfac)3, similar to etch products proposed for continuous etching, 39,41,42 and ALE. 7,28 It may however be sterically difficult to form such a product at the surface. 46 Another possibility is that AlH(hfac)2 or AlF(hfac)2 are formed as etch products. Formation of these species would be sterically easier as only two ligands need to bind around the Al atom. AlH(hfac)2 is a possible product considering that after the H2 plasma exposure

i

h

T

there will likely be some H atoms bonded directly to surface Al atoms. Previous work has shown AlH3 to be highly volatile, 70 and therefore substituting one of the hfac ligands from Al(hfac)3 with a H atom will likely also yield a volatile molecule. AlH3 formation does not appear to occur in this work as no continuous etching was observed when dosing only the H2 plasma half-cycle (Fig. 6(b)). As discussed earlier, there is a possibility that reactive fluorine-containing species such as CF3 /C15 or F /C15 radicals are formed near the surface during the H2 plasma removal step, as a result of dissociation of hfac species in the H2 plasma. It is expected that recombination of F /CF3 /C15 /C15 with H /C15 will occur to form HF/CHF3, due to the presence of H /C15 radicals in the plasma. HF can fluorinate the Al2O3 surface to form AlF3, which has been shown to facilitate etching with Sn(acac)2 through the formation of volatile AlF (acac) x y species. 7,71 Similar reactions may occur in this work to form AlF(hfac)2 as the etch product. Further studies are required to identify the reaction products of the ALE chemistry.

simulations this is likely due to the de-protonation of the Hhfac, which forms volatile H2O at the surface. Therefore, saturation of the Hhfac adsorption could occur once all the surface OH groups are consumed. However, with further Hhfac dosing there is still an increase in hfac absorbance in the wavenumber range 1900-1200 cm /C0 1 (Fig. 9). From 80 ms to 500 ms of total Hhfac dosing time, the hfac absorbance increases without any change in the OH absorbance, suggesting that OH groups are not vital for hfac adsorption. Additionally, DFT analysis in the ESI † show that Hhfac binding to bare Al2O3 surfaces is energetically favorable (Fig. S7, ESI † ). These results from experiments and simulations suggests that the presence of OH groups is not necessary for the adsorption of hfac ligands onto an Al2O3 surface, and therefore the mechanism of having limited reaction sites does not explain the self-limiting behavior.

From ALD literature there are two main mechanisms by which a reaction can saturate on a surface: having a limited number of reactive surface sites, or steric hinderance between the precursor ligands. 72,73 In this study, a decrease in OH group absorbance was observed during the first 80 ms of Hhfac dosing in Fig. 9, which suggests that the OH groups are consumed during the initial Hhfac doses. Based on the DFT

The alternative pathway to a saturating surface reaction is that of steric hinderance, where reactive species are prevented from accessing the surface, thus preventing a continuous reaction. Evidence for such surface inhibition reactions during the diketone exposure can be seen in Fig. 10. Over consecutive Hhfac pulses the hfac absorbance increases and then saturates in the FTIR spectrum. For the saturated surface (after 500 ms total dose time) the hfac is primarily bound in monodentate configuration on the surface, with some contribution from the chelate configuration. The adsorbed hfac surface layer prevents

Fig. 14 Proposed mechanism for ALE of metal oxides using diketone etch-inhibition and surface cleaning. (a) Adsorption of the Hhfac ligands onto the Al2O3 surface. Initial binding is in the chelate configuration, where both O atoms bind to the same surface atom, leading to the formation of volatile species. Over time, steric hinderance on the surface leads to the adsorption of more molecules in the monodentate and isolated chelate configurations, which eventually inhibit the etching. (b) The hfac species on the surface must then be cleaned away to reset the surface such that more etching can occur in the next ALE cycle. H2 plasma is used in this work to remove the surface inhibition layer.

<!-- image -->

.

C

h

e

e

r

t

M

a

J

|

## Paper

additional Hhfac from reacting with the surface, inhibiting etching and thus explaining the self-limiting behavior of the first half-cycle as shown in Fig. 14(a). H2 plasma can then be used to remove the hfac surface layer as shown in Fig. 14(b), enabling etching in the next Hhfac half-cycle. Removal of Al atoms from the surface is thought to occur predominately during the initial doses of Hhfac, before the formation of the surface inhibition layer. In the first Hhfac doses, the adsorbed hfac species measured on the Al2O3 surface by FTIR are primarily in monodentate configuration. The initially high monodentate coverage is surprising considering that the simulations reported in this work and in AS-ALD literature suggest that the chelate configuration should be the most favorable surface species. 36 This observation can be explained by a survivorship bias towards the monodentate configuration. On the initial Al2O3 surface, hfac can easily bind in the preferred chelate configuration and volatilize surface Al atoms, thereby leaving the surface and not appearing in the FTIR spectra. 7,27 Some hfac species may bind in monodentate configuration as steric effects prevent them from transitioning into the chelate configuration (Fig. 12(c) and (d)), or they bind directly in monodentate through the less energetically favorable path (Fig. 13). As the surface becomes more crowded, steric hindrance will be more pronounced, and more Hhfac species will bind to the surface in monodentate configuration. Each Hhfac pulse adds more hfac in monodentate configuration to the surface, until the surface is saturated with monodentate bound hfac, which enables self-limitation of the Hhfac half-cycle. Additionally, some hfac species may bind in chelate configuration, but are surrounded by hfac ligands in monodentate configuration. Due to steric effects the monodentate ligands cannot transition into the chelate configuration. These isolated chelate species will not be able to form volatile Al-containing species as it is anticipated at least two chelate bound hfac ligands are required to make a volatile product. Thus, some chelate hfac ligands can contribute to the surface inhibition. Decomposition of the Hhfac into ketene structures may further contribute to the surface inhibition, accelerating the selflimiting behavior. These structures are not expected to be driving the mechanism as they only constituent a small part of the FTIR signal (Fig. 9). Taken together, it is hypothesized that during the Hhfac dose there is a competition between the etching and surface inhibition reaction. 33,44

Once the etch-inhibition layer has formed, it can be cleaned away using a H2 plasma as demonstrated in Fig. 11. H radicals react with the hfac surface species to form volatile carboncontaining fragments, or reforming Hhfac which is volatile. Over repeated ALE cycles no buildup of hfac species was observed on the surface from FTIR measurements (Fig. 8), suggesting it is a good alternative to O2 plasma. By alternating between the etch/inhibition and surface cleaning half-cycles, the film thickness of Al2O3 can be controlled with sub-nm precision.

A small continuous etching component (0.003 /C6 0.001 nm per step, Fig. 6(a)) is observed for this ALE chemistry. It is hypothesized that continuous etching occurs due to surface

|

J

,

2

0

5

,

1

3

4

5

GLYPH&lt;129&gt;

8

re-organization of the adsorbed hfac species. With continuous Hhfac dosing there is the possibility that some species may reconfigure on the surface or desorb, which could open up space on the Al2O3 surface for new species to bind. If there is enough space at the newly available surface site, and the hfac ligand binds in chelate configuration to an Al atom that already had some chelate ligands bound to it, then it may be etched from the surface. As this relies on many factors lining up, the contribution to etching from this effect is minimal, as is reflected in the high synergy of this ALE process (98%). Further investigation is required to optimize Hhfac dosing conditions that lead to selflimiting etching and minimize the continuous etching. Based on previous literature and the work in this study, it is expected that high partial pressures of Hhfac will cause the reaction to favor a continuous etching regime, 39-42 while repeated low exposure doses may favor the self-limiting regime. 34,44,45

## 4. Conclusions

An ALE chemistry based on alternating doses of Hhfac and H2 plasma is developed, allowing for sub-nm control of film thickness with a high ALE synergy of 98%. The EPC was found to be strongly temperature-dependent, with higher temperatures leading to increased etch rates. High selectivity to SiO2 was demonstrated and shown to be due to the lack of adsorption of Hhfac on the SiO2 surface. Additionally, the EPC measured in this work was higher than the EPC of a comparable process using Hacac/O2 plasma. 34 These observations highlight that Hhfac is a useful etchant for ALE, and that H2 plasma is an effective surface cleaning step which can be used as a substitute for O2 plasma. Etch-inhibition and surface cleaning ALE chemistries offer a good alternative to fluorination and ligand-exchange ALE, providing a route towards ALE with minimal surface contamination.

The mechanism of the Hhfac etching was explored in detail through FTIR and DFT analysis. It was observed that the selflimiting behavior of this process is dictated by the competitive adsorption of different diketone bonding configurations. Initially, species bind preferentially in the chelate configuration which leads to etching of the film. However, over multiple pulses the monodentate configurations build up on the Al2O3 surface, and sterically block adsorption of more Hhfac species on to the surface, thereby also inhibiting the etch reaction. A H2 plasma half-cycle can then be employed to remove the hfac species from the surface, exposing the Al2O3 surface and thus allowing for etching in the next Hhfac half-cycle. FTIR data shows no build-up of hfac species on the surface over multiple ALE cycles, further supporting H2 plasma as a suitable alternative to O2 plasma for surface cleaning.

For the development of other etch-inhibition and surface cleaning ALE processes, three required properties can be identified for the ALE etch/inhibitor molecule based on this work: Firstly, the molecule should be able to form volatile species with the film to be etched. Secondly, to enable self-limiting etching the molecule should have an alternative bonding

5

0

2

y

r

t

s

i

m

h

C

f

o

t

e

i

c

S

l

a

y

o

R

e

h

T

GLYPH&lt;128&gt;

s

i

l

a

n

r

u

o

j

s

i

h

T

configuration/surface reaction which leads to the formation of a stable surface inhibition layer. Finally, the inhibition should be easily removable, such that the surface is not poisoned over time. Diketones can be used as both etchants and surface inhibitors and can be easily removed by plasma or thermal reactants, making them an interesting group of molecules to explore for isotropic ALE.

## Data availability

The data that support the findings of this study are openly available in 4TU. ResearchData at https://data.4tu.nl/ (DOI: https://doi.org/10.4121/f2555371-5b4f-470a-b9ae-93ef5c8118ae ).

## Conflicts of interest

There are no conflicts to declare.

## Acknowledgements

This work is part of the research program HTSM with project no. 17124, which is financed by the Netherlands Organization for Scientific Research (NWO). A. J. M. M. acknowledges support from European Research Council (ERC) under the European Union's Horizon 2020 Research and Innovation Programme (Grant Agreement 949202), and from Vidi project 18363 which is financed by NWO. The authors would like to thank J. J. A. Zeebregts, C. A. A. van Helvoirt, C. van Bommel, J. J. L. M. Meulendijks, and B. Krishnamoorthy for technical support. We would also like to thank Schrodinger for providing ¨ access to their software which is utilized in this work, and to Dr Simon Elliott for useful discussions on the DFT simulations.

## References

- 1 K. J. Kanarik, S. Tan and R. A. Gottscho, J. Phys. Chem. Lett. , 2018, 9 , 4814-4821.
- 2 K. J. Kanarik, T. Lill, E. A. Hudson, S. Sriraman, S. Tan, J. Marks, V. Vahedi and R. A. Gottscho, J. Vac. Sci. Technol., A , 2015, 33 , 020802.
- 3 A. Fischer, R. Janek, J. Boniface, T. Lill, K. J. Kanarik, Y. Pan, V. Vahedi and R. A. Gottscho, in Advanced Etch Technology for Nanopatterning VI , ed. S. U. Engelmann and R. S. Wise, American Vacuum Society, 2017, vol. 10149, p. 101490H.
- 4 C. T. Carver, J. J. Plombon, P. E. Romero, S. Suri, T. A. Tronic and R. B. Turkot, ECS J. Solid State Sci. Technol. , 2015, 4 , N5005-N5009.
- 5 R. Clark, K. Tapily, K.-H. Yu, T. Hakamata, S. Consiglio, D. O'Meara, C. Wajda, J. Smith and G. Leusink, APL Mater. , 2018, 6 , 058203.
- 6 A. Fischer and T. Lill, Phys. Plasmas , 2023, 30 , 080601.
- 7 J. C. Gertsch, A. M. Cano, V. M. Bright and S. M. George, Chem. Mater. , 2019, 31 , 3624-3635.
- 8 M. Konh, Y. Wang, H. Chen, S. Bhatt, J. Q. Xiao and A. V. Teplyakov, Appl. Surf. Sci. , 2022, 575 , 151751.
- 9 E. Mohimi, X. I. Chu, B. B. Trinh, S. Babar, G. S. Girolami and J. R. Abelson, ECS J. Solid State Sci. Technol. , 2018, 7 , P491-P495.
- 10 M. Konh, C. He, X. Lin, X. Guo, V. Pallem, R. L. Opila, A. V. Teplyakov, Z. Wang and B. Yuan, J. Vac. Sci. Technol., A , 2019, 37 , 021004.
- 11 X. Sang, Y. Xia, P. Sautet and J. P. Chang, J. Vac. Sci. Technol., A , 2020, 38 , 043005.
- 12 X. Lin, M. Chen, A. Janotti and R. Opila, J. Vac. Sci. Technol., A , 2018, 36 , 051401.
- 13 M. Konh, A. Janotti and A. Teplyakov, J. Phys. Chem. C , 2021, 125 , 7142-7154.
- 14 A. Fischer, A. Routzahn, S. M. George and T. Lill, J. Vac. Sci. Technol., A , 2021, 39 , 030801.
- 15 Y. Kim, S. Chae, H. Ha, H. Lee, S. Lee and H. Chae, Appl. Surf. Sci. , 2023, 619 , 156751.
- 16 N. J. Chittock, Y. Shu, S. D. Elliott, H. C. M. Knoops, W. M. M. (Erwin) Kessels and A. J. M. Mackus, J. Appl. Phys. , 2023, 134 , 075302.
- 17 C.-W. Chen, W.-H. Cho, C.-Y. Chang, C.-Y. Su, N.-N. Chu, C.-C. Kei and B.-R. Li, J. Vac. Sci. Technol., A , 2023, 41 , 012602.
- 18 J. Kim, D. Shim, Y. Kim and H. Chae, J. Vac. Sci. Technol., A , 2022, 40 , 032603.
- 19 N. J. Chittock, M. F. J. Vos, T. Faraz, W. M. M. (Erwin) Kessels, H. C. M. Knoops and A. J. M. Mackus, Appl. Phys. Lett. , 2020, 117 , 162107.
- 20 S. M. George and Y. Lee, ACS Nano , 2016, 10 , 4889-4894.
- 21 A. M. Cano, A. E. Marquardt, J. W. DuMont and S. M. George, J. Phys. Chem. C , 2019, 123 , 10346-10355.
- 22 S. M. George, Acc. Chem. Res. , 2020, 53 , 1151-1160.
- 23 D. Dictus, D. Shamiryan, V. Paraschiv, W. Boullart, S. De Gendt and C. Vinckier, J. Vac. Sci. Technol., B: Nanotechnol. Microelectron.: Mater., Process., Meas., Phenom. , 2010, 28 , 789-794.
- 24 M. Kawakami, D. Metzler, C. Li and G. S. Oehrlein, J. Vac. Sci. Technol., A , 2016, 34 , 040603.
- 25 J. A. Murdzek, A. Lii-Rosales and S. M. George, Chem. Mater. , 2021, 33 , 9174-9183.
- 26 J. L. Partridge, J. A. Murdzek, V. L. Johnson, A. S. Cavanagh, A. Fischer, T. Lill, S. Sharma and S. M. George, Chem. Mater. , 2023, 35 , 2058-2068.
- 27 A. H. Basher, M. Krstic, ´ K. Fink, T. Ito, K. Karahashi, W. Wenzel and S. Hamaguchi, J. Vac. Sci. Technol., A , 2020, 38 , 052602.
- 28 H. Ohtake, N. Miyoshi, K. Shinoda, S. Fujisaki and Y. Yamaguchi, Jpn. J. Appl. Phys. , 2023, 62 , SG0801.
- 29 S. Fujisaki, Y. Yamaguchi, H. Kobayashi, K. Shinoda, M. Yamada, H. Hamamura, K. Kawamura and M. Izawa, Appl. Phys. Lett. , 2022, 121 , 122102.
- 30 B. D. Fahlman and A. R. Barron, Adv. Mater. Opt. Electron. , 2000, 10 , 223-232.
- 31 H. Kung and A. Teplyakov, J. Catal. , 2015, 330 , 145-153.
- 32 S. L. Wallen, C. R. Yonker, C. L. Phelps and C. M. Wai, J. Chem. Soc., Faraday Trans. , 1997, 93 , 2391-2394.
- 33 J. Li, G. Chai and X. Wang, Int. J. Extreme Manuf. , 2023, 5 , 032003.

J

|

## Paper

- 34 A. Mameli, M. A. Verheijen, A. J. M. Mackus, W. M. M. Kessels and F. Roozeboom, ACS Appl. Mater. Interfaces , 2018, 10 , 38588-38595.
- 35 C. Zhang, E. Tois, M. Leskela and M. Ritala, ¨ Chem. Mater. , 2022, 34 , 8379-8388.
- 36 M. J. M. Merkx, T. E. Sandoval, D. M. Hausmann, W. M. M. Kessels and A. J. M. Mackus, Chem. Mater. , 2020, 32 , 3335-3345.
- 37 Y. Xia and P. Sautet, Chem. Mater. , 2021, 33 , 6774-6786.
- 38 J. Yarbrough, A. B. Shearer and S. F. Bent, J. Vac. Sci. Technol., A , 2021, 39 , 021002.
- 39 F. Rousseau, A. Jain, L. Perry, J. Farkas, T. T. Kodas, M. J. Hampden-Smith, M. Paffett and R. Muenchausen, MRS Proc. , 1992, 268 , 57.
- 40 S. R. Droes, T. T. Kodas and M. J. Hampden-Smith, Adv. Mater. , 1998, 10 , 1129-1133.
- 41 S. R. Droes, A. Jain, T. T. Kodas, M. J. Hampden-Smith and R. Muenchausen, MRS Proc. , 1993, 300 , 471.
- 42 F. Rousseau, A. Jain, T. T. Kodas, M. Hampden-Smith, J. D. Farr and R. Muenchausen, J. Mater. Chem. , 1992, 2 , 893-894.
- 43 M. A. George, D. W. Hess, S. E. Beck, J. C. Ivankovits, D. A. Bohling and A. P. Lane, J. Electrochem. Soc. , 1995, 142 , 961-965.
- 44 A. Mameli, M. J. M. Merkx, B. Karasulu, F. Roozeboom, W. (Erwin), M. M. Kessels and A. J. M. Mackus, ACS Nano , 2017, 11 , 9303-9311.
- 45 M. J. M. Merkx, R. G. J. Jongen, A. Mameli, P. C. Lemaire, K. Sharma, D. M. Hausmann, W. M. M. Kessels and A. J. M. Mackus, J. Vac. Sci. Technol., A , 2021, 39 , 012402.
- 46 J. L. Partridge, A. I. Abdulagatov, V. Sharma, J. A. Murdzek, A. Cavanagh and S. M. George, Appl. Surf. Sci. , 2023, 638 , 157923.
- 47 S. B. S. Heil, J. L. van Hemmen, C. J. Hodson, N. Singh, J. H. Klootwijk, F. Roozeboom, M. C. M. van de Sanden and W. M. M. Kessels, J. Vac. Sci. Technol., A , 2007, 25 , 1357-1366.
- 48 J. L. van Hemmen, S. B. S. Heil, J. H. Klootwijk, F. Roozeboom, C. J. Hodson, M. C. M. van de Sanden and W. M. M. Kessels, J. Electrochem. Soc. , 2007, 154 , G165.
- 49 H. C. M. Knoops, E. M. J. Braeken, K. de Peuter, S. E. Potts, S. Haukka, V. Pore and W. M. M. Kessels, ACS Appl. Mater. Interfaces , 2015, 7 , 19857-19862.
- 50 T. Imamura, I. Sakai, H. Hayashi, M. Sekine and M. Hori, Jpn. J. Appl. Phys. , 2021, 60 , 036001.
- 51 H. Wang, A. Hossain, D. Catherall and A. J. Minnich, J. Vac. Sci. Technol., A , 2023, 41 , 032606.

J

- 52 A. A. Hossain, H. Wang, D. S. Catherall, M. Leung, H. C. M. Knoops, J. R. Renzas and A. J. Minnich, J. Vac. Sci. Technol., A , 2023, 41 , 1-17.
- 53 H. C. M. Knoops, K. de Peuter and W. M. M. Kessels, Appl. Phys. Lett. , 2015, 107 , 014102.
- 54 S. B. S. Heil, E. Langereis, F. Roozeboom, M. C. M. van de Sanden and W. M. M. Kessels, J. Electrochem. Soc. , 2006, 153 , G956.
- 55 G. Kresse and J. Furthmuller, ¨ Comput. Mater. Sci. , 1996, 6 , 15-50.
- 56 G. Kresse and J. Furthmuller, ¨ Phys. Rev. B: Condens. Matter Mater. Phys. , 1996, 54 , 11169-11186.
- 57 G. Kresse and J. Hafner, Phys. Rev. B: Condens. Matter Mater. Phys. , 1993, 48 , 13115-13118.
- 58 P. E. Blochl, ¨ Phys. Rev. B: Condens. Matter Mater. Phys. , 1994, 50 , 17953-17979.
- 59 D. Joubert, Phys. Rev. B: Condens. Matter Mater. Phys. , 1999, 59 , 1758-1775.
- 60 J. P. Perdew, K. Burke and M. Ernzerhof, Phys. Rev. Lett. , 1996, 77 , 3865-3868.
- 61 S. Grimme, J. Antony, S. Ehrlich and H. Krieg, J. Chem. Phys. , 2010, 132 , 154104.
- 62 S. Grimme, S. Ehrlich and L. Goerigk, J. Comput. Chem. , 2011, 32 , 1456-1465.
- 63 H. J. Monkhorst and J. D. Pack, Phys. Rev. B: Solid State , 1976, 13 , 5188-5192.
- 64 J. Li, I. Tezsevin, M. J. M. Merkx, J. F. W. Maas, W. M. M. Kessels, T. E. Sandoval and A. J. M. Mackus, J. Vac. Sci. Technol., A , 2022, 40 , 062409.
- 65 R. L. Puurunen, M. Lindblad, A. Root, A. Outi and I. Krause, Phys. Chem. Chem. Phys. , 2001, 3 , 1093-1102.
- 66 Maestro Materials Science 5.0.122 Based on Maestro Core 13.6.122, MMshare Version 6.2.122, Release 2023-2, Schrodinger Inc., https://www.schrodinger.com .
- 67 K. Momma and F. Izumi, J. Appl. Crystallogr. , 2011, 44 , 1272-1276.
- 68 S. H. Gerritsen, N. J. Chittock, V. Vandalon, M. A. Verheijen, H. C. M. Knoops, W. M. M. Kessels and A. J. M. Mackus, ACS Appl. Nano Mater. , 2022, 5 , 18116-18126.
- 69 M. A. McAllister and T. T. Tidwell, Can. J. Chem. , 1994, 72 , 882-887.
- 70 M. Hara, K. Domen, T. Onishi and H. Nozoye, Appl. Phys. Lett. , 1991, 59 , 1793-1795.
- 71 Y. Lee, J. W. DuMont and S. M. George, J. Phys. Chem. C , 2015, 119 , 25385-25393.
- 72 R. L. Puurunen, Chem. Vap. Deposition , 2003, 9 , 249-257.
- 73 S. Kim, S. Lee, S. Ham, D. Ko, S. Shin, Z. Jin and Y. Min, Appl. Surf. Sci. , 2019, 469 , 804-810.