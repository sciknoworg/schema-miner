<!-- image -->

pubs.acs.org/cm

## Thermal Selective Vapor Etching of TiO2: Chemical Vapor Etching via WF6 and Self-Limiting Atomic Layer Etching Using WF6 and BCl3

Paul C. Lemaire and Gregory N. Parsons *

Department of Chemical &amp; Biomolecular Engingeering, North Carolina State University, Raleigh, North Carolina 27695, United States

ABSTRACT: Controlled thin /uniFB01 lm etching is essential for further development of sub-10 nm semiconductor devices. Vaporphase thermal etching of oxides is appealing for achieving highly conformal etching of high aspect ratio features. We show that tungsten hexa /uniFB02 uoride (WF6) can be used to selectively etch amorphous TiO 2 /uniFB01 lms versus other oxides including Al O . Chemical 2 3 vapor etching (CVE) of TiO2 by WF6 was studied with quartz crystal microbalance (QCM), spectroscopic ellipsometry, X-ray photoelectron spectroscopy (XPS), and thermodynamic modeling. The XPS results show evidence for a WO F x y layer that forms on of the TiO2 /uniFB01 lms during the etch process, which may act as a surfactant layer to help enable /uniFB02 uorination of the TiO . Direct 2 CVE of TiO2 by WF6 is strongly temperature dependent, where etching proceeds readily at 220 ° C, but not at T ≤ 170 ° C. This is consistent with thermodynamic modeling showing that the etching rate is determined by the volatilization of metal /uniFB02 uoride and WF2O2 product species. We also show that, at low temperature, BCl 3 can be used as a coreagent with WF 6 to achieve selflimiting atomic layer etching (ALE) of TiO . At 170 2 ° C, the rate of ALE saturates at ∼ 0.6 Å/cycle, which is ∼ 2 × the rate of TiO 2 ALD at the same temperature. Experimental QCM analysis shows selectivity for TiO2 ALE vs Al2 O3 as predicted by thermodynamic modeling. We also demonstrate and describe how etching reactions during initial cycles can di /uniFB00 er from those during steady-state ALE, and we draw a physical analogy between rate evolution in ALE and well-known rate evolution during nucleation in atomic layer deposition (ALD). This work expands understanding of surface reactions in CVE and ALE and the range of reactants and materials that can be active for advanced thermal ALE processing.

<!-- image -->

## 1. INTRODUCTION

The semiconductor industry foresees multiple challenges in designing and manufacturing transistor devices for the 7 and 5 nm nodes. For example, standard patterning techniques, such as lithography, become much less applicable because of challenges maintaining edge de /uniFB01 nition and alignment to the underlying features. In addition, semiconductor devices typically utilize three-dimensional designs, creating complex high-aspect-ratio features. Accordingly, the semiconductor industry is looking toward controllable etching techniques to supplement currently used thin /uniFB01 lm deposition techniques.

oxide, with signi /uniFB01 cantly lower etch rates in anhydrous conditions. 10 -13 In vapor phase etching, water creates a interfacial layer between the substrate and gas and acts as a proton donor and acceptor to catalytically activate the HF etch. 2,11,12 Although HF is a promising etchant, high HF concentrations can lead to uncontrolled etching.

Chemical vapor etching (CVE) of silicon (Si) native oxide is of interest to the semiconductor industry. Hydrogen /uniFB02 uoride (HF) liquid etching of Si native oxide 1 -3 is ubiquitously utilized in the semiconductor industry, but in situ vapor etching helps limit the reformation of an interfacial oxide layer between Si and a deposited /uniFB01 lm. 4 -9 For both solution and vapor phase etching, H O plays a signi 2 /uniFB01 cant role in HF etching of Si native

<!-- image -->

Extending the anhydrous HF vapor etch to other oxides is often limited, because unlike SiF , many of the formed metal 4 /uniFB02 uorides are nonvolatile at typical process temperatures and pressures. 14 Yet the nonvolatile product formation also creates an opportunity to create a more controlled etching process because the surface /uniFB02 uoride species passivate the substrate from additional /uniFB02 uorination. Surface /uniFB02 uorides or chlorides can then be removed anisotropically by a subsequent energy-enhanced

Received:

March 9, 2017

Revised:

July 3, 2017

Published:

July 4, 2017

DOI: 10.1021/acs.chemmater.7b00985 Chem. Mater. 2017, 29, 6653 - 6665

technique such as plasma exposure or Ar + bombardment or plasma species. Ideally, the two individual steps are self-limiting, creating a process known as atomic layer etching (ALE). But even with large control over the bias and the energy of the species, it is possible to get uncontrolled etching or damage to sensitive features. 15 -18

In order to limit the issues that arise from energy-enhanced techniques, there is interest in purely thermally driven chemical ALE processes. Such techniques would enable conformal isotropic etching, which has many applications for etching in high aspect ratio structures. 19 There has been considerable work by George et al. studying selective etching of oxides using HF in combination with di /uniFB00 erent metal coregents. 20 -23 Speci /uniFB01 cally, HF was used to /uniFB02 uorinate metal oxides including Al2 O3, HfO2, and ZrO2 creating a passivating metal /uniFB02 uoride layer. 20 -23 Exposing the metal /uniFB02 uoride layer to a coreagent such as trimethylaluminum (TMA), 20,23 tin acetylacetone (Sn(acac) ), 2 20 -22,24 diemthylaluminum chloride (DMAC), 20 or silicon tetrachloride (SiCl ) 4 20 can lead to a ligand-exchange reaction. Depending on the metal /uniFB02 uoride and the extent of the ligand- exchange, the modi /uniFB01 ed surface layer will be volatilized, reforming the original substrate surface termination. For example, an AlF3 surface layer is proposed to react with Sn(acac)2 to form volatile Al(acac) 3 and SnF(acac)2. 21,22 This etching approach bears similarities to earlier work in which zinc oxide and copper were etched with hexa /uniFB02 uoroacetonate (hHfac) 25 and hHfac and O3/H2O2 26,27 processes, respectively. Selective oxide etching has been achieved by adjusting the process temperature and selecting speci /uniFB01 c metal precursors that serve as ligand sources. For example, a HF/TMA ALE process was observed to etch Al O 2 3 but not ZrO2 at 300 ° C. 20 In place of HF, other chemicals could be considered for the surface modi cation step, such as BCl /uniFB01 3, 28 Cl2 , 24,25 and WF6.

WF6 is an appealing /uniFB02 uorinating agent and etchant. As a higher oxidation state covalently bound metal /uniFB02 uoride, WF6 is highly volatile at room temperature. 30 Tungsten is also among the most electronegative of the transition metals, 31 enabling selective /uniFB02 uoride transfer to other transition metals. 30 For example, WF6 was observed to undergo halogen exchange with TiCl4 and BCl3 but was considerably less reactive than MoF . 6 30 Yet despite being less reactive, /uniFB02 uorination of TiO2 with WF6 proceeds with a Gibbs free energy of -14.9 kcal/mol, whereas HF /uniFB02 uorination is endothermic with Δ G = 6.9 kcal/mol. The thermodynamic /uniFB02 uorination step by HF may in part explain why other reported thermally driven ALE processes that utilize HF are unable to etch TiN. 20 In addition, WF6 has been observed to etch SiO2 32 and WO3 /uniFB01 lms 33 and in an analogous system NbCl5 was observed to etch Nb2O5. 34 WF6 also has a zero net dipole moment, making it relatively easy to evacuate from a reaction chamber, an attractive feature for a cyclic ALE process. In contrast, HF is ' stickier ' because of its high dipole moment, which can lead to hydrogen bonding and long residence times. 19

In this paper, we demonstrate that WF6 can be used as an etchant for controlled removal of TiO 2 /uniFB01 lms in both chemical vapor etching and atomic layer etching sequences. We /uniFB01 nd that WF6 selectively etches TiO2 over Al2 O3, which we ascribe to the ability of TiO 2 to more readily form volatile products at low process temperatures. Using ex situ XPS analysis, we con /uniFB01 rm WF6 etching of TiO2 /uniFB01 lms and provide evidence that etching proceeds through TiO2 /uniFB02 uorination in the /uniFB01 lm bulk and formation of a low density WO F x y surface layer on the etching /uniFB01 lm. Thinner TiO2 /uniFB01 lms require less time to become fully

/uniFB02 uorinated, resulting in overall more rapid chemical vapor etching than thicker TiO 2 /uniFB01 lms.

We also /uniFB01 nd that by using a surface coupling agent the chemical etching via WF6 can be controlled to achieve a selflimiting ALE process. Speci /uniFB01 cally we /uniFB01 nd that coupling exposures of WF6 with Sn(acac)2 or BCl3 in a stepwise sequence acts to volatilize the WO F x y surface layer formed during WF6 etching, enabling etching of a fraction of a monolayer of TiO2 (i.e., ∼ 0.6 Å) per ALE cycle at 170 ° C.

## 2. EXPERIMENTAL SECTION

- a. List of Supplies and Materials. The 99.99% tungsten hexa /uniFB02 uoride (WF6) and 99.9% boron trichloride (BCl3) were purchased in stainless steel lecture bottles from Galaxy Chemical and Matheson, respectively. Trimethylaluminum (TMA) and titanium tetrachloride (TiCl4) were obtained from Strem Chemicals Inc. and used without further treatment. 99.9% tin acetylacetonate (Sn(acac) ) 2 was purchased from Sigma-Aldrich. The Si substrates were boron doped Si(100) 6 -10 Ω · cm (WRS Materials) and were used asreceived. For the carrier and purge gas, dry 99.999% argon (Ar) was passed through an Entegris GateKeeper inert gas puri /uniFB01 er to remove any residual water before entering the reactor.
- b. Reactor Design and Reaction Sequence. Depositions were carried out in two home-built tubular hot-wall isothermal ALD reactors described in previous publications. 35,36 The chambers were heated resistively using PID controllers. The reaction chamber for the chemical vapor etching (CVE) experiments was ∼ 60 cm long with a diameter of ∼ 10 cm. The reactor for atomic layer etching (ALE) was a similar design with the same reactor length but with a smaller diameter of ∼ 4 cm. Silicon substrates were loaded into the reactors and allowed to reach thermal equilibrium with the walls by /uniFB02 owing carrier gas for 30 min prior to deposition or etching.

In the larger CVE chamber, the baseline operating pressure was maintained at 1.5 Torr with an Ar carrier /uniFB02 ow rate of 210 standard cubic centimeters per minute (sccm). The WF6 /uniFB02 ow was restricted with a needle valve to generate a pressure increase of 300 mTorr over the baseline 1.5 Torr. The pulse sequence was WF6/Ar = 1/60 s, respectively. In some instances, Sn(acac)2 was used in a WF6/Ar/ Sn(acac)2 /Ar (1/60/1/60 s) sequence to increase the WF6 CVE etch rate. Sn(acac) 2 was heated to 105 ° C to produce a pressure changed of ∼ 75 mTorr during dosing. Immediately prior to etching experiments, Al2 O3 and TiO2 ALD /uniFB01 lms were deposited in the same reaction chamber using an x/Ar/H2O/Ar sequence where x is TMA and TiCl4 respectively, with a timing sequence of 0.25/45/0.25/45 s. In some cases, fresh ALD /uniFB01 lms were loaded into the reactor before etching. The data presented here were generally collected after preparing the surface with ALD metal oxide.

In the smaller ALE reactor, a N2 carrier /uniFB02 ow rate of 150 sccm produced a baseline pressure of 800 mTorr. For the ALE runs, the typical reaction sequence followed WF6/N2/BCl3/N2 = 0.2/45/1/45 s. During WF6 and BCl3 dosing, the pressure increase was approximately 600 and 800 mTorr, respectively. Under typical etch conditions, the short WF 6 dose time in the ALE reactor produced a smaller net WF6 exposure per cycle compared to that during typical CVE. Prior to ALE, Al2O3 and TiO2 ALD /uniFB01 lms were deposited using x/Ar/H2O/Ar of 0.1/45/0.1/45 s, where x is either TMA or TiCl4, respectively. The growth rate for the TiO 2 ALD /uniFB01 lm was ∼ 0.3 Å/cycle at 170 ° C. The WF6/BCl3 etching experiments were generally performed after preparing the reactor surface with ALD metal oxide.

- c. Sample Characterization. Film deposition and etching were characterized using ex situ and in situ analytical tools. Spectroscopic ellipsometry (SE) data were obtained with a J.A. Woollam alpha-SE ellipsometer at an incidence angle of 70 ° . Chemical analysis was done using a SPECS X-ray photoelectron spectroscopy (XPS) system with a PHOIBOS 150 analyzer. Spectra were generated using an Al K α X-ray source operated at 400 W. For all analyses, data reduction and /uniFB01 tting was carried out using CasaXPS software with charge compensation based on the C 1s (C -C, C -H) peak set to 285 eV. For some

Figure 1. QCM analysis at 220 ° C of (a) 200 cycles of Al O 2 3 or TiO2 followed immediately by 50 WF6/Ar exposures of 1/60 s each and (b) initial loading of 1 WF6 exposure of 50 s versus 50 WF6/Ar exposures of 1/60 s on TiO2 (200 cycles).

<!-- image -->

Figure 2. Thermodynamic modeling results showing the expected equilibrium species concentrations from 25 to 400 ° C for N2 -diluted WF6 exposed to TiO2 or Al O3 2 at P = 1.5 Torr: (a) 1 mol WF6 + 1 mol TiO2 and (b) 1 mol WF6 + 0.667 mol Al2O3.

<!-- image -->

analyses, we utilized the Ti 2p 3/2 XPS peak intensity to estimate the thickness of WO F x y /uniFB01 lms formed as a result of WF6 adsorption. For this analysis, we measured the attenuation of the Ti 2p3/2 peak and modeled the /uniFB01 lm thickness using parameters available from the NIST E ective /uniFB00 Attenuation Length Database, 37 coupled with electron inelastic mean-free path values determined using the TPP-2 M equation. 38 For this equation, we used a bandgap of 3.45 eV 39 and density of 3.58 g/cm 3 40 , consistent with reported values for amorphous low density WO3 /uniFB01 lms.

Process conditions were further characterized using in situ QCM analysis. For these tests, a 6 MHz gold coated QCM crystal sensor (In /uniFB01 con) was placed into the QCM housing. The crystal backside was purged with 45 sccm of Ar to prevent deposition on the back of the QCM crystal. Inclusion of a crystal back purge increased the operating pressure from 1.5 to 1.75 Torr. In the smaller ALE chamber, the QCM crystal backside was purged with 35 sccm of N , increasing the baseline 2 pressure from 0.8 to 1 Torr. The mass change signals were detected by an In /uniFB01 con SQM-160 monitor and recorded using a home designed LabVIEW program. The mass change reported from the QCM data provides reliable measurements of relative mass change under di /uniFB00 erent process conditions. The measured frequency shifts are not speci /uniFB01 cally calibrated for quantitative analysis of individual mass change values.

- d. Thermodynamic Modeling. Gibbs free energy values and equilibrium amounts in closed systems were calculated using HSC Chemistry 7.1 software. For the equilibrium composition calculations for the WF6 reaction, the starting input amounts were 5 mol of N , 1 2 mol of WF6, and 1 mol of oxide (TiO2, HfO2, ZrO2, SiO2 , and ZnO). The initial moles of Al2 O3 were set as 0.667 to compensate for reaction stoichiometry. For modeling the BCl 3 reaction with the WF6 modi ed surface, the starting concentrations were 5 mol of N , 1 mol /uniFB01 2 of metal /uniFB02 uoride (TiF4 , AlF3, ZrF , etc.), 1 mol of WO , and 3 mol of 4 3

BCl3. For each data set, 50 calculations were done from 25 to 400 ° C at 1.5 Torr (0.002 bar).

## 3. RESULTS AND DISCUSSION

## Selective Chemical Vapor Etching of TiO2 Using WF6.

The WF6 interaction with ALD metal oxide /uniFB01 lms at 220 ° C was assessed with in situ QCM analysis, where the layer to be etched (either Al O 2 3 or TiO2) is deposited in the reactor on the QCM crystal via ALD immediately before etching experiments. Deposition and etching were performed in the same reactor at the same temperature, without air exposure between ALD and etching. Figure 1a shows that immediately following steadystate Al2 O3 or TiO2 ALD at 220 ° C, the /uniFB01 rst 3 -5 WF6 dose steps result in an increase in the mass loading of 355 and 226 ng/cm 2 for Al2 O3 and TiO2, respectively. Additional WF6 exposures on the Al2 O3 surface lead to saturation, whereas additional WF6 exposures on the TiO 2 surface lead to mass loss. After ∼ 17 WF6 doses, the QCM begins to record a net overall mass loss, and further WF 6 dosing leads to additional mass loss, consistent with TiO 2 etching by the WF . We note that the etch 6 rate appears to increase as etching proceeds. For example, after 10 WF6 doses, the etch rate is ∼ 15 ng/cm 2 per WF6 dose but increases to ∼ 87 ng/cm 2 per WF6 dose at 25 WF6 doses. The increase in etch rate is attributed to the etch process transitioning through an incubation period before attaining steady state. This gives rise to an apparent thickness dependence in the etch rate, as discussed in detail in a further section below.

Figure 3. (a) QCM analysis of TiO2 ALD followed by 50 WF6 doses at 120 and 220 ° C and (b) an enlarged view of the mass loading during the WF6 doses, showing net mass loss during each WF6 step at 220 ° C and little to no change at 120 ° C.

<!-- image -->

Figure 4. High resolution XPS scans of (a) Ti 2p, (b) Si 2p, (c) W 4f, and (d) F 1s regions for ∼ 6.5 nm TiO2 /uniFB01 lms exposed to 0, 1, 5, and 15 WF 6 doses at 220 ° C.

<!-- image -->

Results in Figure 1b compare QCM mass response for a series of WF6/Ar = 1/60 s doses (as used in Figure 1a) with that for a single longer (50 s) WF6 dose step. In these experiments, the Ar carrier /uniFB02 ow rate was maintained at 210 sccm with a QCM back purge of 45 sccm for a baseline pressure of 1.75 Torr. The 50 s WF6 dose increased the pressure by 250 mTorr. This pressure change and dose time corresponds approximately to a net exposure that is equivalent to 50 WF6/Ar pulses of 1/60 s each. The 50 s WF6 pulse initially leads to a 360 ng/cm 2 mass increase, somewhat larger than for the individual dose steps (226 ng/cm ). As the WF6 2 dose continued, the measured mass decreased, but after 50 s, QCManalysis shows a net mass increase of 205 ng/cm 2 relative to the mass measured immediately following TiO2 ALD. On the basis of data and modeling presented below, the initial mass increase during the WF6 dosing period is ascribed to /uniFB02 uorine and tungsten uptake on the TiO2 surface, and the mass decrease during further exposure corresponds to etching via desorption of TiF 4 and WF2O2 vapor products. In this case, the 50 WF6/Ar pulses of 1/60 s leads to more etching than a single 50 s WF6 pulse because the purge provided time to promote etch product volatilization.

Thermodynamic Modeling of Metal Oxide Chemical Vapor Etching by WF6. Thermodynamic calculations based on minimizing free energy were performed to determine probable product species and to shed light on expected di /uniFB00 erences for etching of Al2 O3 and TiO2 by WF6. The (unbalanced) overall reaction follows:

$$\xi _ { 2 } \quad T i O _ { 2 } ( s ) + W F _ { 6 } ( g ) \to W O _ { 3 } ( s ) + W F _ { 2 } O _ { 2 } ( g ) + T i F _ { 4 } ( g )$$

Figure 2a shows the calculated equilibrium composition for a closed system initially consisting of 1:1 molar ratio of TiO 2 to WF6 as temperatures changes from 25 to 400 ° C. At room temperature WF6 reacts with TiO 2 to form solid WO3 and solid

Figure 5. Peak intensity of high resolution XPS scans of (a) Ti 2p (459.1 eV) and Si 2p (99.3 eV) and (b) W 4f and (38 eV) and F 1s (685.2 eV) for 5.5 nm TiO2 /uniFB01 lms exposed to 0, 10, 25, 50, and 100 WF 6 doses at 220 ° C. Lines are a guide for the eye. The decrease in the Ti 2p signal con /uniFB01 rms /uniFB01 lm etching.

<!-- image -->

Figure 6. (a) Thickness and (b) refractive index at 632.8 nm of samples with 5.5 nm TiO 2 followed by 0, 15, 25, 50, and 100 WF 6 doses at 220 ° C, measured with spectroscopic ellipsometry. Lines are a guide to the eye.

<!-- image -->

<!-- image -->

TiF4, and at ∼ 125 ° C the solid TiF 4 completely volatilizes. At ∼ 150 ° C, WF6 begins to etch the solid WO3 to form volatile WF2O2. Similar modeling also indicates that WF6 will etch SiO2, though SiO2 di /uniFB00 ers from TiO2 because, unlike TiF , SiF 4 4 is volatile even at room temperature. It should be noted that, in the calculations, when either the initial WF :oxide ratio or the 6 Ar partial pressure is increased, the temperature required to generate the volatile products decreases, indicating more favorable etching. This analysis is strictly accurate only for closed systems, where products are not purged.

response to the WF6 doses at 220 and 120 ° C, in which there are clear mass losses following the WF 6 doses at 220 ° C.

Similar modeling results for Al2 O3 shown in Figure 2b suggest that WF6 reacts at room temperature with Al2 O3 to form solid WO3 and solid AlF . At higher temperatures, like the 3 case of TiO2 , the solid WO3 reacts further with WF6 to form volatile WF2O2. However, the AlF3 remains nonvolatile up to 400 ° C. This solid AlF3 layer likely passivates the surface, preventing etching. 21,22,41 Similar models for ZnO, ZrO2, and HfO2 showed favorable free energy changes for /uniFB02 uorination by WF6, forming nonvolatile metal /uniFB02 uorides. This shows that favorable etching reactions require both favorable surface reactions as well as volatile product formation.

Process Temperature and WF6 Chemical Vapor Etching Behavior. The etching behavior of TiO2 by WF6 was assessed experimentally at di /uniFB00 erent temperatures to collaborate the thermodynamic analysis. Data from QCM analysis in Figure 3a shows that when the temperature was reduced from 220 to 120 ° C, the initial 1 -5 WF6 doses result in a mass gain on the TiO2 surface. Additional WF 6 doses are accompanied by relatively small mass increases, which plateau with time. The enlarged view in Figure 3b further shows the

Analysis of WF6 Chemical Vapor Etching of TiO2 by XPS and Ellipsometry. The composition of the TiO2 surfaces following the initial few WF6 cycles, i.e., prior to signi /uniFB01 cant TiO2 mass loss, was analyzed with ex situ XPS analysis. Figure 4 shows high resolution XPS scans of TiO2 surfaces after 0, 1, 5, and 15 WF6 doses. For this analysis, the initial TiO 2 /uniFB01 lm was su /uniFB03 ciently thin (i.e., ∼ 6.5 nm) to allow detection of the underlying Si substrate. In addition, the starting TiO2 shows evidence for /uniFB02 uorine at ∼ 690 eV, consistent with /uniFB02 uoride from the reactor, likely remaining from previous WF6 etch experiments. Figure 4a shows the Ti 2p signal decreases slightly following 1, 5, and 15 WF 6 doses, but the Si 2p signal intensity in Figure 4b stays relatively constant. The presence of surface tungsten and /uniFB02 uorides is con /uniFB01 rmed by results in Figure 4c,d, showing W 4f and F 1s peaks on the TiO2 surface after 1 WF6 dose. The tungsten signal stays relatively constant between 1 and 15 WF6 doses, whereas the F 1s peak at 685 eV (associated with metal /uniFB02 uorides) progressively increases. This is consistent with WF 6 /uniFB02 uorinating the TiO2 surface and with /uniFB02 uorine di /uniFB00 usion into the TiO2 subsurface. 42,43

The relative location of the XPS peaks provides additional information concerning the etching mechanisms. For example, after 15 WF6 doses, the Ti 2p doublet shifts by ∼ 0.4 eV to higher binding energy (i.e., the Ti 2p 3/2 peak shifts from 459.2 to 458.8 eV). This increase in binding energy is consistent with highly electronegative surface species on the TiO2 such as WO F x y or TiO F . Full y y titanium /uniFB02 uorination to TiF3 or TiF4 would produce a much larger shift in the Ti 2p 3/2 peaks to 462

Figure 7. (a) QCM analysis of WF6 etching following 50, 100, and 200 TiO 2 ALD cycles on a bare Au QCM crystal at 220 ° C and 1.75 Torr. (b) Enlarged view of WF6 etching showing an ' incubation ' period for the vapor etching that is dependent on the initial TiO 2 /uniFB01 lm thickness.

<!-- image -->

and 464 eV, respectively. 43 In addition, the W 4f doublet peaks at 37.9 and 36 eV are shifted ∼ 0.5 eV to higher binding energy compared to oxidized tungsten (37.6 and 35.5 eV), 35,44 again consistent with surface /uniFB02 uorides. 45

Figure 5a shows the Ti 2p and Si 2p peak intensity values collected from the high resolution XPS scans plotted versus number of WF6 dose steps (i.e., WF 6 exposure) after 0, 15, 25, 50, and 100 WF6 doses. More WF6 exposures lead to a linear decrease in the Ti signal and an increase in signal from the silicon substrate, as expected for etching of TiO . Some initial 2 decrease in the Ti 2p signal is ascribed to surface tungsten oxide. The W 4f signal associated with oxidized tungsten (Figure 5b) increases rapidly and stays constant, even up to 100 WF6 doses. Figure 5b also shows that the F 1s signal increases signi /uniFB01 cantly within the /uniFB01 rst 10 WF6 doses followed by saturating behavior with additional WF 6 exposure.

Note that the mass loading scale on the y -axis remains the same as in Figure 7a, allowing the relative rates of mass loss to be directly compared. Figure 7b clearly shows that, during the initial WF6 doses, the rate of mass loss is slow for the thickest (200 cycle) TiO2 /uniFB01 lm and relatively fast for the thin (50 cycle) ALD TiO2. For the 200 cycle TiO2 layer, after an initial mass gain of ∼ 250 ng/cm , the 2 /uniFB01 rst 25 etch cycles produce no mass loss, after which etching readily proceeds (as shown in Figure 7a), indicating etch ' incubation . For the 100 cycle TiO ' 2 /uniFB01 lm, the /uniFB01 rst WF6 dose also produces mass gain, and etching proceeds with less incubation time, attaining steady-state etching after several WF6/Ar doses. For the thinnest (50 cycle) TiO2 /uniFB01 lm, the mass gain is only 28 ng/cm 2 during the initial WF6 dose, and relatively fast etching proceeds after the /uniFB01 rst dose, slowing after ∼ 5 WF6/Ar doses, consistent with complete TiO2 removal.

The /uniFB01 lm thickness for the samples in Figure 5 was further analyzed by spectroscopic ellipsometry, and results are shown in Figure 6. Figure 6a shows that, for the /uniFB01 rst few WF6 cycles, the physical /uniFB01 lm thickness slightly increases, consistent with formation of a tungsten oxy/uniFB02 uoride surface layer. As WF6 dosing proceeds, the TiO2 /uniFB01 lm thickness decreases, consistent with etching observed by QCM and XPS in Figures 1, 3, and 5. Furthermore, the refractive index at 632.8 nm for the TiO2 /uniFB01 lms is ∼ 2.3 after 0 and 10 WF6 doses but decreases to ∼ 1.9 with 25 -100 WF6 doses. The decrease in refractive index can be correlated with a decrease in /uniFB01 lm density. The observed decrease suggests that the WF 6 exposure promotes formation of a porous WO3 /uniFB01 lm 40,46 or the formation of a low density WO F 32,33 x y surface layer.

Incubation of Chemical Vapor Etching and E /uniFB00 ect of TiO2 Film Thickness. The results in Figure 1a suggest that the etch rate increases as the etching proceeds. We hypothesized, therefore, that the WF 6 etch rate may depend on the thickness of the initial TiO2 layer. We tested this by monitoring QCM crystals coated with 50, 100, and 200 cycles of ALD TiO2 at 220 ° C (estimated to be 10, 25, 55 Å thick), each followed by 50 WF6/Ar dose steps. Results are given in Figure 7. In this data set, the trace for 200 TiO 2 ALD cycles + 50 WF6 doses is reproduced from Figures 1 and 3. Note that these experiments required continuous data collection over 3 -5 h, and in Figure 7a, the long-period /uniFB02 uctuations in the QCM data result from small instabilities in the controlled reactor temperature.

Figure 7b reproduces the results from Figure 7a on an expanded time scale, shifted to align the /uniFB01 rst WF6 dose step.

The apparent higher etch rate for the thinnest starting TiO 2 layer is ascribed, therefore, to a shorter incubation period for the thinner /uniFB01 lms to reach steady-state etching. This etch incubation arises because a thin starting /uniFB01 lm requires fewer WF6 doses to attain the surface /uniFB02 uorine concentration required to volatilize surface products. A thicker starting /uniFB01 lm can draw more /uniFB02 uorine into the /uniFB01 lm bulk, thereby needing more WF6 doses before etching begins.

Schematic of the WF6 Chemical Vapor Etch Reaction Process. Figure 8 shows the proposed WF6 chemical vapor etching mechanism of TiO2 /uniFB01 lms at 220 ° C based on QCM, XPS, and ellipsometry analysis. First, during the initial WF6 doses, WF6 adsorbs and reacts with the TiO 2 surface, forming a low density WO F /TiO F x y y z layer. Analysis of the XPS results con /uniFB01 rms mixing of metal oxides in this layer. If the top layer

Figure 8. Schematic of the chemical vapor etching mechanism for TiO2 /uniFB01 lms exposed to WF6 at 220 ° C: (1) WF6 adsorbs on thick TiO2 surface, forming surface-bound TiO F y z and WO F . x y (2) Additional WF6 exposure further /uniFB02 uorinates the TiO F y z and WO F , x y creating volatile WF2O2 and TiF4, etching the TiO2 /uniFB01 lm.

<!-- image -->

Figure 9. High resolution XPS scans of (a) Ti 2p, (b) F 1s, (c) W 4f, and (d) Sn 3d regions for 6.5 nm TiO 2 /uniFB01 lms following 0, 15, and 25 WF /Ar/ 6 Sn(acac)2 /Ar cycles at 220 ° C and 1.75 Torr.

<!-- image -->

consisted of only WO F , then (using a density of x y ∼ 3.6 g/cm 3 reported 40 for low density WO3) a mass increase of ∼ 250 nm/ cm 2 during the /uniFB01 rst WF6 dose (shown in Figure 1 at 220 ° C) would correspond to a WO F x y layer that is ∼ -4 6 Å thick. However, after 1 WF6 exposure, the attenuation of the Ti 2p 3/2 XPS signal is about 2 -3 times less than expected for an ∼ 6 Å WO F x y layer, consistent with the presence of nonvolatile TiF3 42,46 and TiOF2 47 with WO3. 32,33,46,48

## Co-Reagents To Modify TiO2 Chemical Vapor Etching.

During the initial WF , the observed net mass gain for thick 6 starting TiO2 indicates that the extent of surface /uniFB02 uorination within the mixed WO F /TiO F x y y z surface layer is not su /uniFB03 cient to produce a signi /uniFB01 cant amount of volatile products. Subsequent WF6 doses further /uniFB02 uorinate the surface-bound WO F and TiO F x y y z producing volatile etch products, including WO2F2 and TiF4, as indicated by the equilibrium thermodynamics results in Figure 2. Some surface /uniFB02 uorine will di /uniFB00 use and remain within the underlying oxide. 42,43,49,50 A relatively thick starting TiO2 layer provides a large ' sink ' for /uniFB02 uorine di /uniFB00 usion, whereas a thin TiO2 layer allows rapid surface /uniFB02 uorination. This results in a thickness-dependent incubation time for the onset of etching, displayed in the QCM results in Figure 7. We also note that, during the purge step at steady state, volatilization of metal /uniFB02 uorides and metal oxy/uniFB02 uorides reduces the /uniFB02 uoride concentration in the surface layer. Etching stops when the surface /uniFB02 uoride density is not su /uniFB03 cient to support further vaporization. This is supported by the QCM results in Figures 1, 3, and 7 where the mass loading reaches a steady plateau during the WF 6 purge step. This mechanism for etching is consistent with results from Kobayashi et al. 32 showing that WF6 reacts with SiO 2 to form volatile WOF4 and SiF4 . Furthermore, in similar systems, WF 6 has been shown to etch WO3 /uniFB01 lms 33 and NbCl5 was observed to etch Nb2 O5 /uniFB01 lms by forming volatile NbOCl3. 34

On the basis of the XPS analysis in Figures 4 and 5, the TiO 2 chemical vapor etching by WF 6 produces a thin layer of WO F x y on the etched TiO2 surface. To explore approaches to avoid or remove this layer, we performed several experiments. As one approach, Sn(acac)2 was incorporated into the CVE sequence at 220 ° C. Sn(acac)2 has been observed to assist in metal /uniFB02 uoride volatilization in similar atomic layer etching processes. 20 -22,24 For this experiment, we deposited 200 cycles of TiO2 at 220 ° C, and then etched at the same temperature using a WF6/Ar/Sn(acac)2/Ar sequence of 1/60/1/60 s. Figure 9 shows high resolution XPS scans collected after 6.5 nm of TiO 2 ALD (0 etch cycles) and after TiO 2 ALD followed by 15 and 25 WF6/Sn(acac)2 etch cycles. We /uniFB01 rst note that at 220 ° C, the WF6/Sn(acac)2 sequence leads to loss of the Ti 2p signal, indicating /uniFB01 lm etching. Comparing the measured XPS intensities in Figure 9 to those in Figure 5 (with only WF6 exposure steps), the addition of Sn(acac)2 signi /uniFB01 cantly increases the etch rate for an ∼ 6.5 nm TiO2 /uniFB01 lm, so that after 25 WF6/Sn(acac)2 cycles the Ti 2p signal is near the detection limit ( ∼ 0.5 atom %). We also note the presence of surface tin after 15 and 25 cycles at 220 ° C. After 25 WF6/ Sn(acac)2 cycles, the amount of surface /uniFB02 uorine and tungsten is less than observed in Figure 5 after 25 WF6 cycles. These results suggest that the addition of Sn(acac) 2 into the WF6/Ar sequential etch process increases the etch rate by creating additional volatile etch products such as TiO(acac)2 or TiF2(acac)2 . 20

Low Temperature TiO2 Atomic Layer Etching Using WF6/BCl3. As shown above in Figures 5 and 6, TiO2 CVE at 220 ° C proceeds nearly continuously without evidence for selflimiting behavior. A self-limiting atomic layer etching (ALE) process, consisting of self-limiting adsorption and activation steps, is more desirable in that it will allow the extent of etching

Figure 10. (a) QCM analysis at 170 ° C and 1.75 Torr of TiO2 ALD followed by 25 BCl3/Ar doses (pink), 50 WF6/Ar doses (red), 50 WF6/Ar/ Sn(acac)2/Ar cycles (black), or 50 WF /Ar/BCl3 6 /Ar cycles (blue). (b) Enlarged view of the WF /Ar/BCl /Ar etch sequence. (c) QCM of WF6/Ar/ 6 3 BCl3/Ar sequence at 110, 130, 150, 170, and 190 ° C.

<!-- image -->

to be well controlled and de /uniFB01 ned. Therefore, we worked to modify the WF6/Ar/Sn(acac)2/Ar reaction sequence to identify possible ALE conditions. Using the results in Figures 2, 3, and 8, we (1) reduced the process temperature from 220 to 170 ° C to prevent uncontrolled WF6 etching and (2) explored BCl 3 as an alternative coreagent in place of Sn(acac)2 to volatilize surface-adsorbed product species.

Figure 10c shows QCM results for process temperatures between 110 and 190 ° C for WF6/Ar/BCl3/Ar = 0.2/45/1/45 s. The etch rate is nearly independent of temperature between ∼ 110 ° and 150 ° C, consistent with an ' ALE temperature window ' in this range. This range corresponds to limited volatility of TiF4 , 51,52 suggesting that product elimination is a likely rate-limiting step for the ALE reaction mechanism. Higher temperature generally promotes /uniFB02 uorine di /uniFB00 usion during the WF6 dose,and increases the rate of etch product volatilization, leading to an overall faster etch rate.

Thermodynamic Modeling of WF6/BCl3 ALE of TiO2 and Al2O3. Thermodynamic modeling of the WF6/BCl3 ALE reaction was also performed. The expected etch stoichiometry and Gibbs free energy change at 170 ° C are given. The /uniFB01 rst WF6 dose leads to surface adsorption and /uniFB02 uorination:

$$\begin{smallmatrix} d \\ _ { 7 ^ { - } } & & 2 W F _ { 6 } ( g ) + 3 T i O _ { 2 } ( s ) \to 2 W O _ { 3 } ( s ) + 3 T i F _ { 4 } ( s ) \\ & & \Delta G = - 7 8 \, k J / \text{mol} \, T i O _ { 2 } & & ( 1 ) \end{smallmatrix}$$

Figure 10a shows QCM results collected at 170 ° C. For each run, TiO2 ALD was performed for at least 100 cycles, followed immediately by exposure to (i) BCl3/Ar doses; (ii) WF6/Ar doses; (iii) WF6/Ar/Sn(acac)2/Ar cycles; or (iv) WF6/Ar/ BCl3/Ar cycles. At 170 ° C, without the additional coreagent, WF6 shows initial mass gain consistent with surface adsorption, followed by a plateau indicting little to no TiO 2 etching. Dosing only BCl3 appears to initially etch the TiO , but like the WF , 2 6 additional BCl 3 does not lead to substantial etching. In contrast, the WF6/Sn(acac)2 sequence produces an initialization period in which the mass increases, followed by controlled layer-bylayer etching.

Figure 10a shows that the WF6/BCl3 sequence yields stepwise linear etching, but unlike the WF6/Sn(acac)2 sequence, it starts immediately from the /uniFB01 rst BCl3 exposure step. An expanded view of the steady-state WF6/BCl3 etching process is shown in Figure 10b. The mass gain during the WF 6 dose at steady state is ∼ 29 ng/cm 2 . A larger mass uptake is observed during the /uniFB01 rst WF6 dose. After one complete WF6/ BCl3 cycle, the mass change is ∼ 53 ng/cm /cycle, indicating an 2 etch rate that is larger than the 26 ng/cm 2 per cycle mass gain measured during TiO2 ALD at the same process temperature.

The stoichiometric solid products, WO 3 and TiF4, are used in the Δ G analysis to represent the expected solid WO F /TiO F x y v z surface layer. At 170 ° C, TiF4 vapor is also an expected product. The BCl3 dose then allows ligand exchange that activates and volatizes the solid reaction products:

$$4 B C l _ { 3 } ( g ) + 3 T i F _ { 4 } ( s ) \rightarrow 3 T i C l _ { 4 } ( g ) + 4 B F _ { 3 } ( g )$$

$$\Delta G = - 1 6 6 \, k J / \text{mol} \, T i F _ { 4 }$$

$$( 2 )$$

Figure 11. Thermodynamic modeling results showing the expected equilibrium species concentrations from 25 to 400 ° C for (a) reactions 2 and 3, exposing N2-diluted BCl 3 at 1.5 Torr to TiF /WO3: 3 mol of BCl (g) + 1 mol of TiF (s) + 1 mol of WO (s); and (b) the analogous reactions for the 4 3 4 3 Al2 O3 system: 3 mol of BCl (g) + 1 mol of AlF (s) + 1 mol of WO (s). At equilibrium at 170 3 3 3 ° C, BCl3 + TiF4/WO3 produces predominantly volatile BF3, TiCl4 , and WOCl4 and solid B O3. 2

<!-- image -->

Figure 12. (a) QCM analysis of Al O3 2 and TiO2 ALD followed by 50 WF6/BCl3 ALE cycles at 170 ° C. The ALE sequence follows WF6/Ar/BCl3/Ar (0.2/45/2.5/60 s). (b) Enlarged view of (a).

<!-- image -->

$$4 \text{BCI} _ { 3 } ( g ) + 3 \text{WO} _ { 3 } ( s ) & \to 2 \text{B} _ { 2 } \text{O} _ { 3 } ( s ) + 3 \text{WOCI} _ { 4 } ( g ) & \quad \text{react} \\ \Delta G = - 8 3 \, k J / \text{mol} \, \text{WO} _ { 3 } & \quad \text{(3)} & \quad \text{(3)} & \quad \text{smal} \\ \quad \quad \quad$$

Some surface /uniFB02 uorine also remains as a TiF O (s) product. y z 47 Subsequent WF6 doses repeat the TiO 2 surface adsorption and /uniFB02 uorination shown in (1) (repeated here as 4) and also activate and volatilize the surface boron oxide:

reaction 5 also shows consistent results. Although not included in the /uniFB01 gure, the model suggests that at low temperatures a small amount of solid WO Cl x y species may also form via elimination of Cl2 . Additionally, other modeling studies (not shown) indicate that the WF6/BCl3 process is thermodynamically favorable for etching HfO2 and ZrO2, but a somewhat higher process temperature is needed because HfCl 4 and ZrCl4 are less volatile than TiCl . 4

$$2 W F _ { 6 } ( g ) + 3 T i O _ { 2 } ( s ) & \to 2 W O _ { 3 } ( s ) + 3 T i F _ { 4 } ( s ) & \quad \text{In} \\ \Delta G = - 7 8 \, k J / \text{mol} \, T i O _ { 2 } & \quad \text{(4)} & \quad \text{(3)} & \quad \text{indic} \\ \quad \text{$\quad.1$}$$

$$W F _ { 6 } ( g ) + B _ { 2 } O _ { 3 } ( s ) \to 2 B F _ { 3 } ( g ) + W O _ { 3 } ( s ) & \quad \text{$\alpha \, \upsilon$} \\ \Delta G = - 2 0 3 \, k J / \text{mol } B _ { 2 } O _ { 3 } & \quad \text{$\text{read}$} \\ \Delta G = - 2 0 3 \, k J / \text{mol } B _ { 2 } O _ { 3 } & \quad \text{$\text{react$$

The expected equilibrium thermodynamics for the WF6 activation step (reaction 1 or reaction 4) was previously given in Figure 2. That /uniFB01 gure also shows the case of WF6 reaction with Al O . At 170 2 3 ° C in Figure 2, the main surface species are solid WO 3 and metal /uniFB02 uorides, i.e., AlF3 on Al2 O3, and TiO F y z on TiO2. Figure 11 shows the thermodynamic results for the second half-reaction in the ALE sequence (e.g., reactions 2 and 3), when BCl3 is exposed to solid WO3 and metal /uniFB02 uoride (TiF4 or AlF3). Figure 11a shows that, at low temperature, BCl3 reacts with TiF4 and WO3 to form volatile TiCl4, WOCl4, and BF3, along with solid B O , consistent with 2 3 the reaction stoichiometry in eqs 2 and 3. Similar modeling of

In contrast to the favorable etching of TiO 2 or other oxides with WF6/BCl3, modeling results in Figures 2b and 11b indicate that Al O 2 3 etching is not thermodynamically favorable at low temperature. With Al O , Figure 2b shows that WF 2 3 6 will readily form tungsten oxides, and in Figure 11b, the BCl 3 will react with WO3 to form volatile WOCl4. However, the solid AlF3 remains stable up to ∼ 300 ° C where it then reacts to form the AlCl3 vapor. Other modeling results indicate that low oxidation state metal oxides such as ZnO, CoO, and CuO are also not etched by WF6/BCl3 until T &gt; 350 ° C because of the low volatility of the corresponding metal chloride. Overall, these results indicate that the WF6/BCl3 etch sequence is overall thermodynamically favorable for etching TiO 2 at 170 ° C but not favorable for etching Al2 O3 at the same process temperature. The data in the following section test this expectation experimentally.

Experimental Analysis of WF6/BCl3 ALE Selectivity. The selectivity of WF6/BCl3 ALE for TiO2 versus Al2 O3 was assessed with QCM at 170 ° C, and results are given in Figure

Figure 13. Etch rates at 170 ° C for TiO2: (a) BCl 3 with a constant WF6 dose time of 0.2 s and (b) WF 6 dose time with a constant BCl 3 exposure time of 1 s. The ALE reactor was conditioned with 200 TiO2 ALD cycles after every 3 subsequent ALE runs.

<!-- image -->

Figure 14. Saturation study of WF /BCl3 6 ALE process at 170 ° C using QCM: (a) 1 WF6 dose of 0.2 s per 10 BCl 3 doses of 0.2 s each and (b) 10 WF6 doses of 0.1 s each per 1 BCl3 dose of 1.0 s.

<!-- image -->

<!-- image -->

12. In this experiment, the QCM crystal was exposed to more than 100 cycles of TiO2 or Al2 O3 ALD at 170 ° C, followed immediately by WF6/BCl3 etching. For TiO , data in Figure 12 2 (repeated from Figure 10) show linear mass loss during WF6 / BCl3 exposures, consistent with ALE. For Al O , however, no 2 3 etching is observed. As in Figure 2, the /uniFB01 rst WF6 exposure leads to mass gain, but the mass does not change substantially during subsequent WF6 and BCl3 exposures. This result is consistent with the thermodynamic analysis where WF6 reacts with Al O 2 3 to form a solid passivating AlF3 surface layer, which will not react with BCl 3 to form volatile AlCl . 3 20

Self-Limiting Behavior of WF6/BCl3 ALE. To determine if WF6/BCl3 etching of TiO2 proceeds through self-limiting reactions, Figure 13 shows results of experiments at 170 ° C in the ALE reactor on predeposited TiO2 /uniFB01 lms where the change in /uniFB01 lm thickness was measured by ellipsometry after di /uniFB00 erent extents of WF6 or BCl3 dosing. For these tests, we /uniFB01 rst deposited 100 cycles of ALD TiO2 ( ∼ 45 Å) on a set of samples and removed them from the ALD reactor. Individual samples were then exposed to 50 cycles of ALE under di /uniFB00 erent exposure conditions, and the etch rate was determined by ellipsometry. Keeping the WF6 exposure at 0.2 s, increasing the BCl3 exposure to 1 s or larger showed etch saturation at ∼ 0.6 -0.7 Å/cycle. Similarly, keeping the BCl 3 exposure /uniFB01 xed at 1 s, the etch rate saturated with a WF 6 exposure greater than ∼ 0.2 s/ cycle. These etch rate values correspond to the average steadystate etch rate and are consistent with the QCM results in Figure 10b showing the steady-state etch rate is somewhat larger than the ALD growth rate per cycle.

is important to note that whereas the ellipsometry results in Figure 13 show the average steady-state etch rates, the QCM data in Figure 14 were collected during the /uniFB01 rst few ALE cycles immediately after ALD. We /uniFB01 nd that, under self-limiting saturated conditions, vide infra, the initial etch rates can be di /uniFB00 erent from those determined during steady-state ALE. For the data in Figure 14a, a fresh ALD TiO 2 surface was exposed to 0.2 s of WF 6 followed by 10 BCl 3 subdoses of 0.2 s each. The WF6 produced a mass gain followed by mass loss during the BCl3 step. After the /uniFB01 rst WF6 dose, the mass loss during BCl 3 saturates after 3 or 4 subdoses. After the second and third WF 6 doses, saturation is achieved within 10 BCl3 subdoses, demonstrating self-limiting etching in the BCl3 step. This condition corresponds to WF6/BCl3 = 0.2/1.0 s, which is consistent with saturation conditions in Figure 13.

The saturation behavior for the WF /BCl3 6 ALE process was further assessed with QCM, and data are given in Figure 14. It

Likewise, Figure 14b shows results when a fresh TiO 2 surface is exposed to 10 WF6 subdoses of 0.1 s each, followed by 1.0 s of BCl3 . On the fresh TiO2 surface, the /uniFB01 rst WF6 dose leads to a relatively large mass gain followed by mass loss during the BCl 3 dose. In the second cycle, the /uniFB01 rst WF6 subdose shows a much smaller mass gain, and subsequent WF 6 subdoses lead to no net mass change, indicating WF6 reaction saturation. The overall dose conditions correspond to WF6/BCl3 = 1.0/1.0 s. This is also consistent with saturation in Figure 13, but the net 1.0 s WF6 dose/cycle substantially exceeds the 0.1 -0.2 s/cycle required for steady-state saturation. This excess WF 6 leads to a di /uniFB00 erent etch rate during the /uniFB01 rst few ALE cycles than that measured at steady state, but the overall reaction remains selflimiting. The ellipsometry (at steady state) and QCM analysis (during initial etch cycles) both con /uniFB01 rm that the WF6/BCl3 reaction sequence gives rise to self-limiting etching half-

Figure 15. High resolution XPS scans of (a) Ti 2p and (b) F 1s regions for 4 nm TiO 2 /uniFB01 lm following 0, 25, 50, 100, 150, and 200 WF /BCl 6 3 cycles in the ALE reactor at 170 ° C.

<!-- image -->

Figure 16. Schematic diagram describing the proposed etch mechanism for the TiO 2 ALE process using WF6 and BCl3 at 170 ° C: (1) WF6 adsorbs on the thick TiO2 surface, forming surface-bound TiO F y z and WO F . (2) BCl3 x y volatilizes the surface metal oxy /uniFB02 uoride species, forming TiCl , 4 WCl2O2, and BF3.

<!-- image -->

reactions, thereby validating that the process follows a thermal ALE sequence.

Mass Uptake and Etch Rates during Initial WF6/BCl3 Exposures versus Steady-State ALE. In the CVE experiments at 220 ° C shown in Figure 1, we noted that the mass gain during the /uniFB01 rst WF6 exposure was larger than that during subsequent dose steps. The QCM results in Figures 12 and 14 for the WF6/BCl3 process show the WF6 mass uptake is also larger during the /uniFB01 rst dose than during the steady state ALE process. In this case, the mass loss during the /uniFB01 rst BCl 3 dose is also larger than at steady state. The di /uniFB00 erences between the initial and the steady state behavior re /uniFB02 ects di /uniFB00 erences in the surface condition. On the fresh TiO 2 surface, the WF 6 will react readily to yield surface tungsten oxides and /uniFB02 uorine that di /uniFB00 use into the /uniFB01 lm. During steady-state etching, however, some of the WF6 is also consumed to volatilize surface boron oxide, creating a more well-de /uniFB01 ned etch rate per cycle. The di /uniFB00 erent reactions and reaction rates during the /uniFB01 rst cycles will lead to ALE rate transitions, where the etch rate during early cycles could be faster or slower than at steady state.

data presented here were generally collected after preparing our isothermal hot-wall reactor surface with ALD metal oxide. In our reactors, we noted that the ALE rate could be reduced when a series of ALE runs was performed in sequence, possibly resulting from excess boron oxide present on the reactor walls. We found performing a long WF6 exposure to remove boron oxide in the ALE chamber before loading samples acted to mitigate the e /uniFB00 ect.

It is interesting to note that rate evolution during ALE can be viewed as physically analogous to growth incubation commonly observed in ALD. Delayed nucleation in ALD occurs when the ALD precursors react di /uniFB00 erently on the growth substrate than on the growth surface. Likewise, in ALE, it is reasonable to expect the etch reactants will react di /uniFB00 erently with the fresh material being etched, i.e., the ' etch substrate , compared to the ' ' etch surface , i.e., the surface that is present following multiple ' etch cycles. This suggests, therefore, that early ALE rate inhibition or enhancement is a general phenomenon in thermal ALE processes, not limited to the WF /BCl 6 3 process. Likewise, like growth incubation in ALD, the ALE rate transitions are expected to depend on the material being etched, the etch reactants, the process temperature, reactor wall preparation, and other conditions. Regarding reactor wall preparation, the

Analysis of WF6/BCl3 ALE by XPS. The WF6/BCl3 ALE etching process was further characterized using XPS. For this data, a set of recently deposited TiO 2 samples were etched with di /uniFB00 erent numbers of WF6/BCl3 ALE cycles and then removed from the reactor for analysis. Figure 15a shows that the intensity of the Ti 2p signal decreases with increasing number of WF6/BCl3 ALE cycles, consistent with /uniFB01 lm etching. Figure 15b shows the F 1s signal under the same conditions. The peaks near 685 and 690 eV are assigned to /uniFB02 uorine bound to metal and carbon, respectively, 53 indicating metal /uniFB02 uorides and trace organic /uniFB02 uorine on the TiO2 surface. The metal /uniFB02 uorides are consistent with the expected ALE reactions. The organic /uniFB02 uorides are ascribed to reaction with adventitious carbon during sample transfer. Furthermore, the boron, chlorine, and tungsten content are also below the XPS detection limit. After 200 ALE cycles, the Ti 2p signal is below the detection limit con /uniFB01 rming that the TiO2 /uniFB01 lm was completely etched, leaving trace amounts of halogen on the Si substrate surface.

Schematic of the WF6/BCl3 ALE Reaction Process. Figure 16 shows a schematic for the proposed WF6/BCl3 ALE reaction sequence consistent with the thermodynamic modeling, as well as the QCM, ellipsometry, and XPS data. First, like the chemical vapor etching mechanism, the initial WF 6 adsorbs and /uniFB02 uorinates the TiO2 surface producing solid WO F x y and TiO F . This is shown in the XPS results in Figure 4, as well as y z QCM in Figures 10 and 12. At T &lt; 200 ° C, the solid WO F x y layer is not su /uniFB03 ciently volatile to allow CVE.

After WF6, the subsequent BCl3 exposure then leads to ligand exchange 43 yielding volatile TiCl4 and WOCl4, as indicated by equilibrium thermodynamics in Figure 12. Thermodynamic models also suggest solid B2O3 is a surface product. However, XPS analysis after BCl 3 exposure showed no evidence for surface boron. The lack of B signal is expected because the samples are transferred in air for XPS, allowing surface B2O3 to react with ambient moisture to form volatile boric acid, H BO . 3 3 54 The XPS data in Figure 15 show that, after BCl3 exposure, some /uniFB02 uorine remains on the TiO2 surface, denoted as TiO F . Also during the BCl y z 3 exposure step at 170 ° C, BCl3 is expected to react with TiO 2 to form TiCl 4 and B2O3 ( Δ G = -109 kJ/mol TiO2). The solid B O3 2 passivates the TiO 2 surface, thereby self-limiting the BCl 3 etching.

After BCl , the subsequent WF 3 6 exposure reacts with B O 2 3 to form volatile BF3 and TiF4, and surface WO3, WO F x y and TiO F . Some surface TiO F y z y z is present from previous cycles, and this impedes /uniFB02 uorine di /uniFB00 usion, 20 -23,49,50 thereby leading to less WF6 reaction than on fresh TiO2. Upon establishing steady-state conditions, the WF6/BCl3 atomic layer etch sequence continues until the TiO2 /uniFB01 lm is consumed. As shown in Figure 15, after 200 ALE cycles, no evidence for Ti 2p is observed by XPS. Moreover, the silicon substrate remaining after ALE shows a relatively small F 1s signal, indicating this ALE sequence leaves a clean surface after etching. 29

## ■ SUMMARY AND CONCLUSIONS

In this article, we demonstrated and described mechanisms for thermally driven selective chemical vapor etching (CVE) of TiO2 using WF6 at T &gt; 200 ° C and selective atomic layer etching (ALE) of TiO2 using WF6/BCl3 reactant exposures at T &lt; 190 ° C. Other reactants, including WF6/Sn(acac)2, also provided routes for low-temperature ALE. Using XPS and ellipsometry analysis, we physically con /uniFB01 rm TiO2 etching and provide evidence that etching proceeds through TiO2 /uniFB02 uorination and formation of a low density WO F x y region. We also showed that the chemical selectively for etching of TiO2 over other oxides including Al O 2 3 is due to the relative volatility of the metal /uniFB02 uoride product species.

For etching of TiO 2 using WF6 and BCl3, modeling con /uniFB01 rms that the process proceeds through two complementary thermodynamically favorable half-reaction steps, indicating creation of volatile TiCl4, BF3, and WOCl4. Film thickness measurements after etching under a range of exposure conditions con /uniFB01 rm steady-state self-limiting etch saturation, con /uniFB01 rming thermal atomic layer etching, with an etch rate of ∼ 0.6 -0.7 Å/cycle at 170 ° C. At slightly lower temperatures, between 130 ° and 150 ° C, the process is more temperature independent, with an etch rate of ∼ 0.3 Å/cycle. We show that the ALE process is selective for etching TiO 2 over Al O3, and 2 modeling further suggests this process will be favorable for ALE of HfO2 and ZrO2. Analysis by XPS shows complete removal of TiO2 /uniFB01 lms on silicon, resulting in a clean substrate with trace amounts of surface /uniFB02 uorination. We also describe and demonstrate how the rate of ALE during initial etch cycles may be di /uniFB00 erent from that observed at steady state, and we conclude that rate evolution during initiation of thermal ALE may be a general phenomenon that is physically analogous to well-known rate transitions during substrate-dependent nucleation in ALD.

## ■ AUTHOR INFORMATION

## Corresponding Author

*

(G.N.P.) E-mail: gnp@ncsu.edu.

## ORCID

Paul C. Lemaire: 0000-0002-2077-8114

Gregory N. Parsons: 0000-0002-0048-5859

## Author Contributions

All authors have given approval to the /uniFB01 nal version of the manuscript.

## Notes

The authors declare no competing /uniFB01 nancial interest.

## ■ ACKNOWLEDGMENTS

The authors acknowledge support from Lam Research and EMD Performance Materials. They also acknowledge the use of the Analytical Instrumentation Facility (AIF) at North Carolina State University, which is supported by the State of North Carolina and the National Science Foundation.

## ■ REFERENCES

- (1) Trucks, G. W.; Raghavachari, K.; Higashi, G. S.; Chabal, Y. C. Mechanism of HF Etching of Silicon Surfaces: A Theoretical Understanding of Hydrogen Passivation. Phys. Rev. Lett. 1990 , 65 , 504 -507.
- (2) Kang, J. K.; Musgrave, C. B. The Mechanism of HF/H[sub 2]O Chemical Etching of SiO[sub 2]. J. Chem. Phys. 2002 , 116 , 275.
- (3) Hoshino, T.; Nishioka, Y. Etching Process of SiO[sub 2] by HF Molecules. J. Chem. Phys. 1999 , 111 , 2109.
- (4) Ritala, M. Atomic Layer Deposition of Oxide Thin Films with Metal Alkoxides as Oxygen Sources. Science (Washington, DC, U. S.) 2000 , 288 , 319 -321.
- (5) Atanasov, S. E.; Kalanyan, B.; Parsons, G. N. Inherent SubstrateDependent Growth Initiation and Selective-Area Atomic Layer Deposition of TiO2 Using ' water-Free ' Metal-Halide/metal Alkoxide Reactants. J. Vac. Sci. Technol., A 2016 , 34 , 01A148.
- (6) Liu, J.; Lennard, W. N.; Goncharova, L. V.; Landheer, D.; Wu, X.; Rushworth, S. A.; Jones, A. C. Atomic Layer Deposition of Hafnium Silicate Thin Films Using Tetrakis(diethylamido)hafnium and Tris(2Methyl-2-Butoxy)silanol. J. Electrochem. Soc. 2009 , 156 , G89.
- (7) Frank, M. M.; Chabal, Y. J.; Green, M. L.; Delabie, A.; Brijs, B.; Wilk, G. D.; Ho, M.-Y.; da Rosa, E. B. O.; Baumvol, I. J. R.; Stedile, F. C. Enhanced Initial Growth of Atomic-Layer-Deposited Metal Oxides on Hydrogen-Terminated Silicon. Appl. Phys. Lett. 2003 , 83 , 740.
- (8) Chaukulkar, R. P.; Agarwal, S. Atomic Layer Deposition of Titanium Dioxide Using Titanium Tetrachloride and Titanium Tetraisopropoxide as Precursors. J. Vac. Sci. Technol., A 2013 , 31 , 031509.
- (9) Park, K. J.; Terry, D. B.; Stewart, S. M.; Parsons, G. N. In Situ Auger Electron Spectroscopy Study of Atomic Layer Deposition: Growth Initiation and Interface Formation Reactions during Ruthenium ALD on Si -H, SiO2, and HfO2 Surfaces. Langmuir 2007 , 23 , 6106 -6112.
- (10) Holmes, P. J.; Snell, J. E. A Vapour Etching Technique for the Photolithography of Silicon Dioxide. Microelectron. Reliab. 1966 , 5 , 337 -341.
- (11) McIntosh, R.; Kuan, T.-S.; Defresart, E. Hydrogen Fluoride Vapor Etching for Pre-Epi Silicon Surface Preparation. J. Electron. Mater. 1992 , 21 , 57 -60.
- (12) Helms, C. R.; Deal, B. E. Mechanisms of the HF/H2O Vapor Phase Etching of SiO2. J. Vac. Sci. Technol., A 1992 , 10 , 806.
- (13) Miki, N.; Kikuyama, H.; Kawanabe, I.; Miyashita, M.; Ohmi, T. Gas-Phase Selective Etching of Native Oxide. IEEE Trans. Electron Devices 1990 , 37 , 107 -115.
- (14) Lee, Y.; Sun, H.; Young, M. J.; George, S. M. Atomic Layer Deposition of Metal Fluorides Using HF-Pyridine as the Fluorine Precursor. Chem. Mater. 2016 , 28 , 2022.

DOI: 10.1021/acs.chemmater.7b00985 Chem. Mater. 2017, 29, 6653 - 6665

- (15) Oehrlein, G. S.; Metzler, D.; Li, C. Atomic Layer Etching at the Tipping Point: An Overview. ECS J. Solid State Sci. Technol. 2015 , 4 , N5041 -N5053.
- (16) Kanarik, K. J.; Lill, T.; Hudson, E. A.; Sriraman, S.; Tan, S.; Marks, J.; Vahedi, V.; Gottscho, R. A. Overview of Atomic Layer Etching in the Semiconductor Industry. J. Vac. Sci. Technol., A 2015 , 33 , 020802.
- (17) Faraz, T.; Roozeboom, F.; Knoops, H. C. M.; Kessels, W. M. M. Atomic Layer Etching: What Can We Learn from Atomic Layer Deposition? ECS J. Solid State Sci. Technol. 2015 , 4 , N5023 -N5032.
- (18) Carver, C. T.; Plombon, J. J.; Romero, P. E.; Suri, S.; Tronic, T. A.; Turkot, R. B., Jr. Atomic Layer Etching: An Industry Perspective. ECS J. Solid State Sci. Technol. 2015 , 4 , N5005 -N5009.
- (19) George, S. M.; Lee, Y. Prospects for Thermal Atomic Layer Etching Using Sequential, Self-Limiting Fluorination and LigandExchange Reactions. ACS Nano 2016 , 10 , 4889 -4894.
- (20) Lee, Y.; Huffman, C.; George, S. M. Selectivity in Thermal Atomic Layer Etching Using Sequential, Self-Limiting Fluorination and Ligand-Exchange Reactions. Chem. Mater. 2016 , 28 , 7657.
- (21) Lee, Y.; George, S. M. Atomic Layer Etching of Al2O3 Using Sequential, Self-Limiting Thermal Reactions with Sn(acac)2 and Hydrogen Fluoride. ACS Nano 2015 , 9 , 2061 -2070.
- (22) Lee, Y.; DuMont, J. W.; George, S. M. Mechanism of Thermal Al 2 O 3 Atomic Layer Etching Using Sequential Reactions with Sn(acac) 2 and HF. Chem. Mater. 2015 , 27 , 3648 -3657.
- (23) Lee, Y.; DuMont, J. W.; George, S. M. Trimethylaluminum as the Metal Precursor for the Atomic Layer Etching of Al 2 O 3 Using Sequential, Self-Limiting Thermal Reactions. Chem. Mater. 2016 , 28 , 2994 -3003.
- (24) Lee, Y.; DuMont, J. W.; George, S. M. Atomic Layer Etching of HfO2 Using Sequential, Self-Limiting Thermal Reactions with Sn(acac)2 and HF. ECS J. Solid State Sci. Technol. 2015 , 4 , N5013 -N5022.
- (25) Droes, S. R.; Kodas, T. T.; Hampden-Smith, M. J. Etching of ZnO Films with Hexafluoroacetylacetone. Adv. Mater. 1998 , 10 , 1129 -1133.
- (26) Steger, R.; Masel, R. Chemical Vapor Etching of Copper Using Oxygen and 1,1,1,5,5,5-Hexafluoro-2,4-Pentanedione. Thin Solid Films 1999 , 342 , 221 -229.
- (27) Jain, A.; Kodas, T. T.; Hampden-Smith, M. J. Thermal DryEtching of Copper Using Hydrogen Peroxide and Hexafluoroacetylacetone. Thin Solid Films 1995 , 269 , 51 -56.
- (28) Min, K. S.; Kang, S. H.; Kim, J. K.; Jhon, Y. I.; Jhon, M. S.; Yeom, G. Y. Atomic Layer Etching of Al2O3 Using BCl3/Ar for the Interface Passivation Layer of III -V MOS Devices. Microelectron. Eng. 2013 , 110 , 457 -460.
- (29) Ikeda, K.; Imai, S.; Matsumura, M. Atomic Layer Etching of Germanium. Appl. Surf. Sci. 1997 , 112 , 87 -91.
- (30) O Donnell, T. A.; Stewart, D. F. Reactivity of Transition Metal ' Fluorides. I. Higher Fluorides of Chromium, Molybdenum, and Tungsten. Inorg. Chem. 1966 , 5 , 1434 -1437.
- (31) Koutsospyros, A.; Braida, W.; Dermatas, D.; Strigul, N.; Christodoulatos, C. A Review of Tungsten: From Environmental Obscurity to Scrutiny. J. Hazard. Mater. 2006 , 136 , 1 -19.
- (32) Kobayashi, N.; Nakamura, Y.; Goto, H.; Homma, Y. In Situ Infrared Reflection and Transmission Absorption Spectroscopy Study of Surface Reactions in Selective Chemical-Vapor Deposition of Tungsten Using WF6 and SiH4. J. Appl. Phys. 1993 , 73 , 4637.
- (33) Tagtstrom, P. Atomic Layer Epitaxy of Tungsten Oxide Films ̈ ̈ Using Oxyfluorides as Metal Precursors. J. Electrochem. Soc. 1999 , 146 , 3139.
- (34) Knapas, K.; Rahtu, A.; Ritala, M. Etching of Nb 2 O 5 Thin Films by NbCl 5. Chem. Vap. Deposition 2009 , 15 , 269 -273.
- (35) Kalanyan, B.; Lemaire, P. C.; Atanasov, S. E.; Ritz, M. J.; Parsons, G. N. Using Hydrogen To Expand the Inherent Substrate Selectivity Window During Tungsten Atomic Layer Deposition. Chem. Mater. 2016 , 28 , 117 -126.
- (36) Kalanyan, B.; Losego, M. D.; Oldham, C. J.; Parsons, G. N. LowTemperature Atomic Layer Deposition of Tungsten Using Tungsten
- Hexafluoride and Highly-Diluted Silane in Argon. Chem. Vap. Deposition 2013 , 19 , 161 -166.
- (37) Powell, C. J.; Jablonski, A. NIST Standard Reference Database 82; 2011.
- (38) Fuentes, G. G.; Elizalde, E.; Yubero, F.; Sanz, J. M. Electron Inelastic Mean Free Path for Ti, TiC, TiN and TiO2 as Determined by Quantitative Reflection Electron Energy-Loss Spectroscopy. Surf. Interface Anal. 2002 , 33 , 230 -237.
- (39) Vasilopoulou, M.; Kostis, I.; Vourdas, N.; Papadimitropoulos, G.; Douvas, A.; Boukos, N.; Kennou, S.; Davazoglou, D. Influence of the Oxygen Substoichiometry and of the Hydrogen Incorporation on the Electronic Band Structure of Amorphous Tungsten Oxide Films. J. Phys. Chem. C 2014 , 118 , 12632 -12641.
- (40) Mouat, A. R.; Mane, A. U.; Elam, J. W.; Delferro, M.; Marks, T. J.; Stair, P. C. Volatile Hexavalent Oxo-Amidinate Complexes: Molybdenum and Tungsten Precursors for Atomic Layer Deposition. Chem. Mater. 2016 , 28 , 1907 -1919.
- (41) Lee, Y.; DuMont, J. W.; George, S. M. Atomic Layer Etching of AlF 3 Using Sequential, Self-Limiting Thermal Reactions with Sn(acac) 2 and Hydrogen Fluoride. J. Phys. Chem. C 2015 , 119 , 25385 -25393.
- (42) Ramanath, G.; Greene, J. E.; Carlsson, J. R. A.; Allen, L. H.; Hornback, V. C.; Allman, D. J. W Deposition Titanium FluorideFormation during WF[sub 6] Reduction by Ti: Reaction Path and Mechanisms. J. Appl. Phys. 1999 , 85 , 1961.
- (43) Fracassi, F.; d Agostino, R. Chemistry of Titanium Dry Etching ' in Fluorinated and Chlorinated Gases. Pure Appl. Chem. 1992 , 64 , 703 -707.
- (44) Lemaire, P. C.; King, M.; Parsons, G. N. Understanding Inherent Substrate Selectivity during Atomic Layer Deposition: Effect of Surface Preparation, Hydroxyl Density, and Metal Oxide Composition on Nucleation Mechanisms during Tungsten ALD. J. Chem. Phys. 2017 , 146 , 052811.
- (45) Bestwick, T. D.; Oehrlein, G. S. Tungsten Etching Mechanisms in CF4/O2 Reactive Ion Etching Plasmas. J. Appl. Phys. 1989 , 66 , 5034.
- (46) Lee, Y. J.; Park, C.-O.; Kim, D.-W.; Chun, J. S. The Effects of Deposition Temperature on the Interfacial Properties of SiH4 Reduced Blanket Tungsten on TiN Glue Layer. J. Electron. Mater. 1994 , 23 , 1075 -1080.
- (47) Louvain, N.; Karkar, Z.; El-Ghozzi, M.; Bonnet, P.; Guerin, K.; ́ Willmann, P. Fluorination of Anatase TiO 2 towards Titanium Oxyfluoride TiOF 2: A Novel Synthesis Approach and Proof of the LiInsertion Mechanism. J. Mater. Chem. A 2014 , 2 , 15308.
- (48) Baxter, D. V.; Chisolm, M. H.; Doherty, S.; Gruhn, N. E. Chemical Vapour Deposition of Electrochromic Tungsten Oxide Films Employing Volatile tungsten(VI) Oxo Alkoxide/?-Diketonate Complexes. Chem. Commun. 1996 , 1129.
- (49) Ortega, Y.; Lamiel-Garcia, O.; Hevia, D. F.; Tosoni, S.; Oviedo, J.; San-Miguel, M. A.; Illas, F. Theoretical Study of the Fluorine Doped Anatase Surfaces. Surf. Sci. 2013 , 618 , 154 -158.
- (50) Tosoni, S.; Lamiel-Garcia, O.; Fernandez Hevia, D.; Illas, F. Theoretical Study of Atomic Fluorine Diffusion through Bulk TiO 2 Polymorphs. J. Phys. Chem. C 2013 , 117 , 5855 -5860.
- (52) Pilvi, T.; Puukilainen, E.; Munnik, F.; Leskela, ̈ M.; Ritala, M. ALD of YF 3 Thin Films from TiF 4 and Y(thd) 3 Precursors. Chem. Vap. Deposition 2009 , 15 , 27 -32.
- (51) Mantymaki, M.; Heikkila, M. J.; Puukilainen, E.; Mizohata, K.; ̈ ̈ ̈ Marchand, B.; Raisanen, ̈ ̈ J.; Ritala, M.; Leskela, ̈ M. Atomic Layer Deposition of AlF 3 Thin Films Using Halide Precursors. Chem. Mater. 2015 , 27 , 604 -611.
- (53) Thermo Scienti /uniFB01 c XPS: Fluorine. http://xpssimpli /uniFB01 ed.com/ elements/ /uniFB02 uorine.php (accessed May 28, 2017).
- (54) Putkonen, M.; Niinisto, L. Atomic Layer Deposition of B2O3 ̈ Thin Films at Room Temperature. Thin Solid Films 2006 , 514 , 145 -149.
