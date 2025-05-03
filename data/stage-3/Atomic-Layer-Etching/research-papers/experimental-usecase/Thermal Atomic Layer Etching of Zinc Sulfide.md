<!-- image -->

pubs.acs.org/cm

Article

## Thermal Atomic Layer Etching of Zinc Sulfide Using Sequential Trimethylaluminum and Hydrogen Fluoride Exposures: Evidence for a Conversion Mechanism

Taewook Nam, Jonathan L. Partridge, and Steven M. George *

<!-- image -->

Cite This: Chem. Mater. 2023, 35, 6671-6681

Read Online

<!-- image -->

## ACCESS

Metrics &amp; More

Article Recommendations

<!-- image -->

ABSTRACT: Thermal atomic layer etching (ALE) of zinc sulfide (ZnS) was demonstrated using sequential exposures of Al(CH3)3 (trimethylaluminum (TMA)) and HF (hydrogen fluoride). ZnS is one of the first sulfide materials to be etched using thermal ALE techniques. In situ spectroscopic ellipsometry (SE) studies were performed on ZnS films grown at 100 ° C using atomic layer deposition (ALD) techniques. These studies revealed that the etch rate during ZnS ALE increased with temperature from 1.4 Å/cycle at 225 ° C to 2.1 Å/cycle at 300 ° C. ZnS ALE was also self-limiting at longer TMA and HF exposures. A possible mechanism for ZnS ALE is fluorination and ligand exchange where ZnS is fluorinated by HF and then ZnF2 undergoes ligand exchange with Al(CH3)3 to yield Zn(CH3)2. Because Al(CH3)3 may also have the ability to convert ZnS to Al2S3, a second possible mechanism for ZnS ALE is ligand exchange/ conversion by TMA together with fluorination by HF. To verify the conversion

<!-- image -->

mechanism, in situ quadruple mass spectrometry (QMS) studies revealed that Al(CH3)3 exposures on initial ZnS substrates released Zn(CH3)2 products, as expected for a conversion reaction. In addition, no H S products were observed by QMS analysis during HF 2 exposure on the initial ZnS substrates. However, after Al(CH ) 3 3 exposures on ZnS, QMS measurements monitored H2S from HF exposures, as expected if Al(CH ) 3 3 converts ZnS to Al2 S3. These QMS results provide direct evidence for the conversion of ZnS to Al2 S3 during ZnS ALE. Time-dependent QMS results also revealed that the conversion/ligand-exchange and fluorination reactions were self-limiting. In addition, QMS analysis observed Al F (CH3) x y z dimers and trimers as ligand-exchange products during the Al(CH3)3 exposures. Because the Al S 2 3 conversion layer thickness is dependent on Al(CH3)3 exposures, larger Al(CH3)3 pressures over equivalent times led to higher ZnS etch rates. In contrast, larger HF pressures over equivalent times had a small effect on the ZnS etch rate because HF is able to fluorinate only the converted Al S 2 3 layer thickness. The ZnS etch rate was slightly dependent on the ZnS ALD growth temperature. The ZnS etch rate at 300 ° C was 1.4, 1.0, and 0.8 Å/cycle for ZnS ALD films grown at 100, 200, and 300 ° C, respectively. The lower ZnS etch rates for the ZnS ALD films grown at higher temperatures were attributed to the larger density and higher sulfur content of ZnS ALD films grown at higher temperatures. The ZnS ALD films with a larger density may be more difficult to convert from ZnS to Al2S3 during the Al(CH3)3 reaction. The RMS roughness of the ZnS films was slightly decreased from 7.4 to 5.9 Å after 15 ALE cycles. However, after 30 ALE cycles, the RMS roughness gradually increased with the ALE cycles.

## I. INTRODUCTION

Atomic layer etching (ALE) is based on sequential, selflimiting surface modification and volatile release reactions. 1 The two main types of ALE are plasma ALE and thermal ALE. 2,3 Plasma ALE achieves anisotropic ALE based on energetic ion and neutral atoms to remove the modified surface by sputtering. 3 Thermal ALE obtains isotropic ALE using gaseous reactants. 2,4 Thermal ALE acts as the reverse of atomic layer deposition (ALD). 5 Many materials, such as various oxides, 6 -11 nitrides, 12 -14 metals, 15 -18 and semiconductors, 19,20 have been successfully etched using thermal ALE methods.

Almost no sulfide materials have been etched using ALE methods. The main exception is MoS2 because of its importance in nanoscale transition metal dichalcogenide

<!-- image -->

(TMD) devices. MoS2 ALE has been performed using mostly plasma ALE methods. These methods include plasma oxidation or chlorination for surface modification followed by volatile release of the modified surface layer using either annealing, 21 Ar + sputtering, 22,23 or dipping in H2O. 24 One thermal ALE method for MoS2 ALE was recently introduced based on sequential MoF6 and H2O exposures. 25 Apart from

Received:

March 19, 2023

Revised:

July 2, 2023

Published:

August 16, 2023

<!-- image -->

these plasma and thermal ALE investigations on MoS2, there are no other reported sulfide ALE processes.

In addition to MoS2 nanoscale transistors, 26 sulfides are important in photovoltaics, energy storage, and photonics. 27 In particular, zinc sulfide (ZnS) is a wide-bandgap II -VI semiconductor material that is useful for electroluminescent (EL) devices. 28 ZnS is also utilized as a transparent conductor, photodetector, and photocatalyst. 29,30 ZnS etching processes are required to fabricate the ZnS devices. Many plasma etching methods have been developed for ZnS etching based on chlorine, hydrogen, or hydrocarbon plasmas. 31 -33 ZnS etching has also been reported using spontaneous thermal etching with 1,1,1,5,5,5-hexafluoroacetylacetone (hfacH) at 200 ° C. 34 However, there have been no previous reports for thermal ZnS ALE that could provide much more precise control of ZnS etching.

The chemistry for thermal ZnS ALE could be defined using fluorination and ligand-exchange reactions using hydrogen fluoride (HF) and trimethylaluminum (TMA). HF could fluorinate ZnS to ZnF2. Subsequently, TMA could undergo ligand exchange with ZnF2 to form Zn(CH3)2 and AlF(CH3)2 ligand-exchange products. These fluorination and ligandexchange reactions can be written as

$$Z n S + 2 H F ( g ) \to Z n F _ { 2 } + H _ { 2 } S ( g )$$

$$Z n F _ { 2 } + 2 A l ( C H _ { 3 } ) _ { 3 } ( g ) \to 2 A l F ( C H _ { 3 } ) _ { 2 } ( g ) + Z n ( C H _ { 3 } ) _ { 2 } ( g ) \quad \dots \dots.$$

A schematic showing these fluorination and ligand-exchange reactions is given in Figure 1. However, the fluorination of ZnS

Figure 1. Proposed mechanism of ZnS ALE using HF and TMA as reactants based on (a) fluorination and (b) ligand-exchange reactions.

<!-- image -->

to ZnF2 is not expected to be a thermochemically favorable reaction. Equation 1 has a predicted standard free energy change of Δ ° G = +9.0 kcal at 300 ° C. 35 The fluorination and ligand-exchange mechanism could be restricted by the initial fluorination of ZnS to ZnF2.

Alternatively, thermal ZnS ALE could proceed by a conversion mechanism. 10 In previous studies, this conversion mechanism of ZnS or ZnO by TMA was considered to be etching because the amount of Zn measured by X-ray fluorescence or mass of ZnO by quartz crystal microbalance was decreased after TMA exposure. 36,37 However, a recent study using in situ analyses has revealed that ZnO was converted to Al2 O3 by TMA. 38 These studies suggest that other materials may also undergo conversion by TMA. 38

In the conversion mechanism, TMA can convert ZnS to Al2S3. Then HF could fluorinate Al2 S3 to form AlF3. Subsequently, TMA could undergo ligand exchange with AlF3 to form Zn(CH3)2 and AlF(CH3)2 ligand-exchange products. After volatilizing the AlF3 layer, the TMA could proceed to convert more underlying ZnS to Al2 S3 . The conversion, fluorination, and ligand-exchange reactions can be written as

$$\overset { n } { + } \quad 3 Z n S + 2 A l ( C H _ { 3 } ) _ { 3 } ( g ) \to A l _ { 2 } S _ { 3 } + 3 Z n ( C H _ { 3 } ) _ { 2 } ( g ) \quad ( 3 )$$

$$\frac { \text{al} } { 2 } \quad \text{Al} _ { 2 } S _ { 3 } + 6 H F ( g ) \to 2 A I F _ { 3 } + 3 H _ { 2 } S ( g ) \quad \text{(4)}$$

$$\Lambda _ { - } \quad \ A I F _ { 3 } + \Lambda ( \mathrm C H _ { 3 } ) _ { 3 } ( g ) \to \Lambda I F _ { 2 } ( \mathrm C H _ { 3 } ) + \Lambda I F ( \mathrm C H _ { 3 } ) _ { 2 } ( g ) \quad ( s )$$

A schematic showing these conversion, fluorination, and ligand-exchange reactions is given in Figure 2. However, the

Figure 2. Proposed mechanism of ZnS ALE using HF and TMA as reactants based on initial conversion followed by (a) fluorination and (b) ligand-exchange and conversion reactions.

<!-- image -->

conversion of ZnS to Al2 S3 is not expected to be a thermochemically favorable reaction. Equation 3 has a standard free energy change of Δ ° G = +53.4 kcal at 300 ° C. 35 In contrast, the fluorination of Al S 2 3 to AlF3 is predicted to be a thermochemically favorable reaction. Equation 4 has a standard free energy change of Δ ° G = -133.3 kcal at 300 ° C. 35 Based on the thermochemical predictions, the conversion, fluorination, and ligand-exchange mechanism could be prevented by the unfavorable conversion of ZnS to Al S . 2 3

In this paper, ZnS ALE was studied by in situ spectroscopic ellipsometry (SE) and quadruple mass spectrometry (QMS) using HF and TMA as the reactants. The etch rates of ZnS ALE were characterized by in situ SE at various process temperatures and reactant exposures. In situ QMS identified the volatile species that were produced during the sequential HF and TMA exposures. To clarify the chemical mechanism, QMS studied fresh ZnS powder initially exposed to either HF

or TMA. These QMS investigations with fresh ZnS powder determined whether HF alone could fluorinate ZnS or whether TMA must first convert ZnS to Al2S3. In addition, the surface roughness was measured by AFM to determine if surface smoothing could be achieved by ZnS ALE.

## II. EXPERIMENTAL SECTION

The thermal ALE experiments were conducted in a V-shaped viscous flow reactor. The reactor was enclosed in a ceramic heater to maintain the process temperature. A schematic of this V-shaped reactor has been presented earlier. 39 The reactor was pumped with a mechanical rotary vane pump (2010C1, Pfeiffer). The base pressure of the reactor was maintained at 1 Torr with a constant flow of ultrahigh-puritygrade (UHP) nitrogen (N2) gas (99.999%, Airgas).

The ZnS ALD films used for the ZnS ALE experiments were grown on p-type silicon (Si) wafer (Silicon Valley Microelectronics, Inc.) using diethylzinc (DEZ) ( ≥ 52 wt% Zn basis, MilliporeSigma) and hydrogen sulfide (H2S) ( ≥ 99.5%, MilliporeSigma) as the reactants. 40 -42 Both precursors were maintained at room temperature ( ∼ 25 ° C). Before loading into the reactor, the Si samples were rinsed by acetone, isopropanol (IPA), and deionized water sequentially to remove surface contaminants and then blown dry using UHP nitrogen (99.999%, Airgas). During ZnS ALD, the DEZ and H2S pressures were 100 mTorr and precursor exposure and purge times were 1 and 20 s, respectively.

ZnS ALE was performed using trimethylaluminum (TMA) (97%, MilliporeSigma) and hydrogen fluoride (HF), derived from HF -pyridine (HF ∼ 70 wt%, MilliporeSigma), as the reactants. The ZnS ALE was conducted after ZnS ALD without exposing the ZnS ALD films to ambient air. Both reactants were maintained at room temperature. The TMA and HF pressures were 40 and 45 mTorr, respectively. The ZnS ALE process started with HF exposures first and then with TMA exposures. All of the ZnS etch rates were obtained using ZnS ALD films grown at 100 ° C unless noted otherwise.

A spectroscopic ellipsometer (M-2000UI, J.A. Woollam) was utilized at an incident angle of 70 ° for in situ monitoring of the thin film thickness. The wavelength range for the ellipsometric measurements was 245 to 1690 nm. The data acquisition was performed 10 s after each reactant exposure. For the refractive index measurements, ex situ ellipsometric measurements were conducted on an automated stage by varying the incident angle from 65 ° to 70 ° and 75 . After ° data acquisition, the thickness and refractive index of the ZnS films were characterized using CompleteEASE software (J.A. Woollam) employing a Sellmeier model. 43

The QMS studies were performed in a custom-built reactor using ZnS powder samples. A detailed description of this reactor has been given previously. 44,45 The two reactant lines were isolated until the reactants reached the ZnS powder bed. 44 The ZnS powder (99.9%, average particle size ∼ 5 μ m, US Research Nanomaterials, Inc.) was housed in a stainless-steel enclosure with a stainless-steel mesh. Before the powder was loaded, the chamber was exposed to sequential cycles of HF and TMA to initialize the reactor walls. The etching of ZnS powder was conducted at 275 ° C. The ZnS powder was left in the reactor for at least 12 h to allow for removal of adsorbed water prior to the reactant exposures.

The volatile etch products were formed in a N 2 background gas at a pressure of ∼ 1.5 Torr in the sample holder. The partial pressure of each reactant was approximately 1 Torr. The N2, reactant, and product gases expanded through an aperture into a low-pressure differentially pumped region to form a molecular beam. 45 The products in the molecular beam then passed through a skimmer into a second differentially pumped region that housed the quadrupole mass spectrometer (Extrel, MAX-QMS Flanged Mounted System). 45 An electron ionization energy of 70 eV was used for the QMS experiments.

To characterize the crystallinity and density of the film, grazing incidence X-ray diffraction (GI-XRD) and X-ray reflectivity (XRR) were conducted using an X-ray diffractometer (Bede D1, Jordan

Valley Semiconductors). The XRD measurements employed radiation from Cu K α at λ = 1.54 Å. The X-ray tube filament voltage and current were 40 kV and 35 mA, respectively. The incident angle of the X-ray was 0.3 . The XRR scan range was 300 ° -7000 arcsec with a 5 arcsec step size. The REFS software package from Jordan Valley Semiconductors was used for the XRR fitting.

The surface roughness of ZnS before and after ALE was characterized using atomic force microscopy (AFM) (NX-10, Park Systems). For the surface roughness analysis, a 30 nm thick ZnS ALD film was grown at 100 ° C. The AFM image was recorded using noncontact mode (NCM) with a scan rate of 1 Hz and a stagemounted PPP-NCHR (Nanosensors) probe. The average RMS roughness was obtained using AFM images from three different positions for each sample.

## III. RESULTS AND DISCUSSION

A. Spectroscopic Ellipsometry Measurements. The ZnS thin film was sequentially exposed to HF and TMA precursors at 300 ° C. Figure 3 shows the ZnS thickness

Figure 3. Thickness of ZnS film versus number of ZnS ALE cycles using HF and TMA as reactants at 300 ° C. Initial ZnS ALD films were grown at 100 ° C.

<!-- image -->

measured by in situ ellipsometry after every exposure for 50 ALE cycles. The ZnS films were grown using ZnS ALD at 100 ° C. The initial ZnS film thickness was 203 Å. The film thickness decreased linearly versus the number of ALE cycles. The ZnS film thickness was 96 Å after 50 ALE cycles. The etch rate during this ZnS ALE process was 2.1 Å/cycle.

An expansion of Figure 3 during the first 5 ALE cycles is shown in Figure 4. No etch delay was observed for ZnS ALE. The last exposure during ZnS ALD was H2S. The first exposure during ZnS ALE was HF. Figure 4 shows that the main thickness reduction was observed for every HF exposure during ZnS ALE. However, the reaction mechanism cannot be easily determined from ellipsometer results. Ellipsometer modeling does not explicitly account for surface species that may have different polarizability and refractive index than the underlying thin film.

In this case, the thickness loss after the HF exposures is attributed to the removal of the -CH3 surface species. -CH3 groups are highly polarizable. One measure of their polarizability is their Raman cross sections. C -H bonds and -CH3 7 groups have one of the highest Raman cross sections. 46,4 Consequently, ellipsometry is sensitive to the addition or

Figure 4. Expansion showing thickness of ZnS film during the first 5 ZnS ALE cycles in Figure 3.

<!-- image -->

removal of -CH3 groups from the surface. Ellipsometry may interpret the addition of -CH3 groups as a gain of the film thickness and the loss of -CH3 groups as a loss of the film thickness.

Figure 5 shows the ZnS thickness change during every reactant exposure for ZnS ALE at different etching temper-

Figure 5. Thickness change of ZnS film vs number of ZnS ALE cycles at 225, 250, 275, and 300 ° C. Initial ZnS ALD films were grown at 100 ° C.

<!-- image -->

atures. The ZnS films were grown using ZnS ALD at 100 ° C. The ZnS etch rates were 1.4, 1.8, 2.0, and 2.1 Å/cycle at 225, 250, 275, and 300 ° C, respectively. As expected for a thermally activated process, higher etch rates are observed at higher temperatures. The lowest etching temperature was limited at 225 ° C because the TMA and HF reactants can produce AlF3 ALD when the process temperature is &lt;225 ° C. 48,49

Figure 6 investigates the self-limiting nature of ZnS ALE during HF and TMA exposures at 300 ° C. The ZnS films were grown using ZnS ALD at 100 ° C. Etch rates were measured versus HF and TMA exposure times by changing one

Figure 6. Etch rate during ZnS ALE vs precursor exposure time at 300 ° C. The HF pressure was 40 mTorr and the TMA pressure was 45 mTorr. Initial ZnS ALD films were grown at 100 ° C.

<!-- image -->

precursor exposure time while keeping the other precursor exposure time constant. The purge time after each reactant exposure was 30 s. The reaction sequence can be denoted as x -30-4-30 (s) for the experiments versus HF exposure time. The reaction sequence can be denoted as 1-30- -30 y (s) for the experiments versus TMA exposure time. The ZnS etch rate was saturated at 2.1 Å/cycle when HF and TMA exposure times were &gt;1 and &gt;3 s, respectively. This saturated etch rate indicates self-limiting surface reactions. There was no change in the etch rate when longer purge times were used from 25 to 50 s.

B. Mass Spectrometry Studies. QMS experiments were performed to examine the etching products during ZnS ALE of the ZnS powder. Figure 7 shows the ion signal intensities over three different m z / ranges: (a) 10 to 40, (b) 60 to 100, and (c) 100 to 215. These results were obtained for the TMA and HF exposures during the fourth ALE cycle at 275 ° C. The fourth ALE cycle was chosen to avoid etch products that could possibly be released from the native oxide on the initial ZnS powder.

Figure 7a displays the ion signals for m z / values from 10 to 40 during HF and TMA exposures. CH3 + ion signals at m z / 15 and CH4 + ion signals at m z / 16 were observed during both the HF and TMA exposures. These results indicate that -CH3 species must be present on the ZnS surface after TMA exposures. The HF exposure can then release these -CH3 species during surface fluorination. The CH + x ion signals during the TMA exposures are attributed to the fragmentation of the Al(CH3)3 + and Zn(CH3)2 + ions.

Ion signals for H S at 2 m z / 32, 33, and 34 were also observed in Figure 7a during the HF exposure. H2S is the expected product from the HF fluorination of a metal sulfide. The F + ion signal at m z / 19 is also monitored during the HF exposure. Likewise, Al + at m z / 27 is detected during the TMA exposure. These ion signals result from the fragmentation of the parent ions of the HF and TMA reactants.

Figure 7b shows the ion signals for m z / values from 60 to 100 during HF and TMA exposures. The ion signals are consistent with the production of Zn(CH3)2 as the primary etch product of ZnS ALE during TMA exposure. Zn(CH3) + is

Figure 7. QMS spectra during the fourth cycle of ZnS ALE at 275 ° C for HF and TMA exposures in three different mass regions: (a) m z / 10 to 40, (b) m z / 60 to 100, and (c) m z / 100 to 215.

<!-- image -->

the main ion signal in the mass spectrum of Zn(CH3)2. The main ion signals for Zn(CH3) + were observed at m z / 79, 81, and 83 during the TMA exposure. The main ion signals for the parent Zn(CH3)2 + were also observed at m z / 94, 96, and 98 during the TMA exposure. These ion signals result primarily from the natural isotopic abundance of Zn. Zinc has five stable isotopes: 64 Zn (48.63%), 66 Zn (27.90%), 67 Zn (4.10%), 68 Zn (18.75%), and 70 Zn (0.62%). These isotopes and their natural abundances together with the carbon isotopes and their natural abundances produce the observed ion intensities.

Ion signals from the higher mass region for m z / values from 100 to 215 nm are displayed in Figure 7c. This mass region reveals Al dimers and Al trimers that are formed by combinations of AlF(CH3)2 and Al(CH3)3. The main ion signals are observed at m z / 133, 137, 141, and 213. Nearly identical ion signals were reported earlier by mass spectrometer studies of the reaction of TMA with fluorinated Al2 O3 or AlF3. 45,50 These ion signals are the characteristic etch products during Al2 O3 ALE using HF and TMA as the reactants. 50,51 AlF(CH3)2 results from the ligand-exchange reaction between TMA and AlF3. 51 AlF(CH3)2 could also be produced by a ligand-exchange reaction between TMA and ZnF2.

The results in Figure 7 confirm that the TMA and HF exposures lead to the etching of ZnS. However, the mass spectra do not clearly reveal whether Zn(CH ) 3 2 was formed by TMA converting ZnS to Al2 S3 or whether Zn(CH3)2 was formed by TMA undergoing ligand exchange with ZnF2. To clarify the ZnS ALE mechanism, fresh ZnS powder was exposed only to HF to determine if H2S was released during the HF exposure.

Figure 8 shows time-resolved QMS spectra of HF and H2S during 5 HF exposures to fresh ZnS powder at 275 ° C. The

Figure 8. Intensities for HF + ion signal ( m z / 20) and H2S + ion signal ( m z / 34) during 5 exposures of HF to fresh ZnS powder at 275 ° C. No intensity is observed for the H S 2 + ion signal.

<!-- image -->

reaction sequence was 2 min for the HF exposure followed by 5 min for N2 purging. If ZnS is fluorinated by HF exposures, then the H2S signal at m z / 34 should be observed during HF exposures as expected by the mechanism in Figure 1. However, the H2S signal was not detected during the 5 HF exposures. These results indicate that HF is not able to fluorinate ZnS. This lack of fluorination is consistent with thermochemical predictions for the fluorination of ZnS by HF given in eq 1. This reaction has a positive standard free energy change of Δ ° G = +9.0 kcal at 300 ° C. 35 This positive free energy change implies a nonspontaneous reaction.

To further clarify the ZnS ALE mechanism, TMA and HF were sequentially exposed to fresh ZnS powder at 275 ° C. Figure 9 displays the time-resolved QMS spectra during 5 sequential exposures of TMA and HF. The reaction sequence was 2 min for each reactant exposure followed by 10 min for N2 purging. The time-resolved QMS spectra are consistent with a conversion reaction during the first TMA exposure. Two ion signals at m z / 83 and 98 were coincident with the first TMA exposure. These two ion signals correspond to 68 Zn(CH3) + and 68 Zn(CH3)2 + , respectively.

Because there was no fluorination prior to this TMA exposure, these two Zn(CH3) x + ion signal species must have been generated by the conversion of ZnS to Al2S3 during the TMA exposure. This conversion reaction is shown in the top panel of Figure 2. This conversion reaction is not consistent with thermochemical calculations for the conversion reaction given in eq 3. The thermochemical calculations yield a positive

Figure 9. Time-resolved QMS results during 5 cycles of ZnS ALE using HF and TMA as reactants at 275 ° C. ZnS ALE starts with TMA exposure. First TMA exposure produces intensity for the 68 Zn(CH3)2 + ion signal at m z / 98. HF exposure produces intensity for the H2S + ion signal at m z / 34. Subsequent TMA exposures also produce intensity for the Al (CH ) F 2 3 4 + ion signal at m z / 133.

<!-- image -->

standard free energy change of Δ ° G = +53.4 kcal at 300 ° C. 35 Although this positive free energy change predicts no reaction, the clear observation of Zn(CH3)2 by the QMS studies provides compelling evidence of a conversion reaction.

The standard free energy changes, Δ ° G , predicted by thermochemical calculations are based on equilibrium conditions, with the reactants and products in their standard states. These conditions may be very different than the experimental situation during ZnS ALE. The reactant and product pressures are not at their standard pressures during ZnS ALE. In particular, ZnS ALE is conducted under vacuum with continuous removal of the product pressure. This vacuum environment would facilitate the forward reaction given by eq 3. In addition, the values for solids in the thermochemical databases are based on bulk materials. These bulk values may be different from the values for the surfaces of these materials. The disagreement between the thermochemical predictions and experimental observations for ZnS conversion illustrates that different models may be needed for accurate free energy calculations under nonequilibrium conditions. 52

The subsequent HF exposure in Figure 9 produces an ion signal at m z / 34 that corresponds to H2S . This H2S product + results from the fluorination of Al S 2 3 to AlF3 as illustrated in Figure 2a. This fluorination reaction is consistent with the thermochemical calculations for the fluorination reaction given by eq 4. This reaction has a negative standard free energy change of Δ ° G = -133.3 kcal at 300 ° C. 35 This large negative standard free energy change indicates that fluorination of Al S 2 3 by HF should occur spontaneously.

After the surface is fluorinated, the next TMA exposure produces an ion signal at m z / 133 corresponding to an Al dimer, in addition to ion signals at m z / 83 and 98 from 68 Zn(CH3) + and 68 Zn(CH3)2 + . The Al dimer is consistent with the ligand-exchange reaction between TMA and the fluorinated AlF3 surface, as illustrated in Figure 2b. Additional Al dimer and trimer ion signals at m z / 137, 141, and 213 were also concurrent with the Al dimer ion signal at m z / 133. The ion signals from Zn(CH3)2 are attributed to the additional conversion of ZnS to Al2S3 by TMA.

The subsequent HF and TMA exposures in Figure 9 continue to produce the same products. A H2S + ion signal is observed during the second HF exposure. 68 Zn(CH3) + and 68 Zn(CH3)2 + ion signals together with the Al dimer and trimer ion signals are monitored during the third TMA exposure. The following HF and TMA exposures in Figure 9 release the same products with nearly identical ion intensities.

The time-resolved QMS spectra can reveal the self-limiting nature of the ALE reactions. Figure 10 shows the time evolution of the TMA exposure together with the 68 Zn(CH3) + and 68 Zn(CH3)2 + ion signals at m z / 83 and 98 produced by the conversion reaction in Figure 10a and the Al dimer ion

Figure 10. Time-resolved QMS results during the fourth TMA exposure in Figure 9. (a) Ion intensities for the 68 Zn(CH3)2 conversion product at m z / 83 and 98 appear rapidly in advance of the ion intensity for the TMA reactant at m z / 72. (b) Intensity for the Al2 (CH3)4F + ion signal at m z / 133 appears rapidly in advance of the ion intensity for the TMA reactant at m z / 72.

<!-- image -->

<!-- image -->

intensity at m z / 133 from the ligand-exchange reactions in Figure 10b. The 68 Zn(CH3) + , 68 Zn(CH3)2 + , and Al dimer ion signals increase rapidly on the rising edge of the TMA ion intensity at m z / 72. This coincidence indicates that the ligandexchange and conversion reactions take place at the same time. The 68 Zn(CH3) + , 68 Zn(CH3)2 + , and Al dimer ion signals then decrease rapidly and go down to baseline as the TMA ion signal intensity reaches a steady value. The 68 Zn(CH3) + and 68 Zn(CH3)2 + ion intensities were used to avoid overlap between 64 Zn(CH3) + and a chlorine-containing species, Al 37 Cl(CH3) + , at m z / 79.

Figure 11 displays the time evolution of the HF exposure together with the H2 S + ion signal at m z / 34 produced by the

Figure 11. Time-resolved QMS results during 4th HF exposure are shown in Figure 9. Intensity for the H S 2 + ion signal at m z / 20 appears rapidly in advance of intensity for the HF + reactant at m z / 20.

<!-- image -->

fluorination of Al2S3 as illustrated in Figure 2a. The fluorination of Al2 S3 is extremely rapid. The H2S + ion signal intensity occurs on the rising edge of the HF + ion signal intensity at m z / 20. The H2S + ion signal then drops rapidly, and the HF + ion signal intensity reaches a constant level. Because the QMS data acquisition time was ∼ 1 s per scan, the rapid evolution of the volatile H2S product produced by the fluorination reaction could not always be captured completely. This behavior may explain the fluctuation of the H S ion signal 2 intensities observed in Figure 9.

C. ZnS ALE versus Reactant Pressure and Different Film Thicknesses. ZnS ALE was also explored at different TMA and HF reactant pressures. Figure 12 shows the measured ZnS etch rates versus HF pressure at TMA pressures of 20 and 200 mTorr. The initial ZnS ALD films were grown at 100 ° C. For HF and TMA exposure times of 1 and 4 s, respectively, the etch rate saturated at an etch rate of 1.8 Å/ cycle for HF pressure above 150 mTorr when the TMA pressure was 20 mTorr. In comparison, the etch rate saturated at an etch rate of 2.5 Å/cycle for HF pressures above 150 mTorr when the TMA pressure was 200 mTorr.

The increase in the ZnS etch rate for higher TMA pressures is attributed to the higher conversion of ZnS to Al S 2 3 at higher TMA pressures. The conversion layer is known to form a diffusion barrier on the surface of the converted material. In this case, the Al S 2 3 conversion layer acts as a diffusion barrier for the conversion of additional ZnS. Similar results have been observed for the fluorination of Al2 O3 at different HF pressures. 53 The fluorination appears to self-limit at various

Figure 12. ZnS etch rates vs temperature for ZnS ALD films grown at different temperatures.

<!-- image -->

HF pressures because HF forms an AlF3 surface layer that acts as a diffusion barrier for further fluorination. The fluorination proceeds according to the HF exposure in units of Torr · s. 53 The kinetics of ZnS conversion to Al2 S3 are also similar to those of silicon oxidation. Silicon oxidation is limited by the formation of a SiO 2 diffusion barrier on the silicon surface. The oxidation layer thickness can be described by the Deal -Grove model. 54

The ZnS etch rate was also observed to be slightly dependent on the growth temperature during ZnS ALD. Figure 13 shows the ZnS etch rate versus temperature for ZnS

Figure 13. ZnS etch rates vs temperature for ZnS ALD films grown at different temperatures.

<!-- image -->

ALD films grown at 100, 200, and 300 ° C. The ZnS etch rate at 300 ° C was 1.4, 1.0, and 0.8 Å/cycle for ZnS ALD films grown at 100, 200, and 300 ° C, respectively. This dependence of the ZnS etch rate on ZnS ALD growth temperature is attributed to the higher ZnS film density at higher temperature.

The film density is proportional to refractive index through the Lorentz -Lorenz relationship. 55 The refractive index of the

ZnS films was characterized using ex situ ellipsometry. The ZnS refractive index at 632.8 nm increased versus the ZnS ALD temperature. The refractive indices increased from n = 2.198 at 100 ° C, to n = 2.211 at 200 ° C, and to n = 2.218 at 300 ° C. The mass densities of the ZnS ALD films grown at 100, 200, and 300 ° C measured by XRR were 3.98, 4.01, and 4.04 g/cm , respectively. The dependence of the etch rate on 3 the film density may result from the diffusion required for conversion. The Al(CH3)3 reactant needs to diffuse into the ZnS film for the conversion of ZnS to Al2S3. The ZnS films with a higher density may have slower diffusion rates.

Another possibility to explain the lower etch rates for the ZnS ALD films grown at higher temperatures could be related to the ZnS stoichiometry. The ZnS composition was characterized using X-ray spectroscopy (XPS). The Zn:S ratios for ZnS ALD films grown at 100 and 300 ° C were 52:48 and 45:55, respectively. Similar amounts of O and carbon were observed for both samples. This result for more S-rich ZnS ALD films at higher growth temperatures was also reported earlier. 56 The more S-rich ZnS films may have a lower etch rate.

The ZnS etch rates may also be dependent on the crystallinity of the ZnS film. The crystallinity of ZnS for different film thicknesses was examined using XRD. Figure 14

Figure 14. XRD spectra of ZnS ALD films grown at 100 ° C with thicknesses of 20 and 60 nm. Crystallinity is observed for the ZnS ALD film with a thickness of 60 nm.

<!-- image -->

shows XRD spectra of ZnS ALD films grown at 100 ° C for thicknesses of 20 and 60 nm. The ZnS films with a thickness of 20 nm may be amorphous because they have no diffraction peaks. In contrast, the ZnS films with a thickness of 60 nm show a very sharp diffraction peak at 28.6 . ° This diffraction peak may correspond to either h(002) or c(111) or both because the ZnS crystalline peaks of h(002) and c(111) overlap each other. 41 In addition to this main diffraction peak, three smaller peaks were also detected at 47.6 , ° 51.9 , ° and 56.6 . ° These diffraction peaks correspond to h(110)/c(220), h(103), and c(311), respectively. 41,56 From this XRD analysis, the ZnS ALD film with a thickness of 60 nm has a crystalline structure.

To determine if the ZnS etch rates were also dependent on ZnS ALD film thickness, the ZnS etch rates were measured for

ZnS ALD films grown at 100 ° C with different initial thickness. Figure 15 shows the ZnS ALE for ZnS films with initial

Figure 15. Thickness of ZnS films versus number of ZnS ALE cycles using HF and TMA as reactants at 300 ° C. Initial ZnS film thicknesses were 20, 40, and 60 nm. Initial ZnS ALD films were grown at 100 ° C.

<!-- image -->

thicknesses of 20, 40, and 60 nm. The etch rate was the same at 2.1 Å/cycle independent of the initial thickness of the ZnS ALD film. These results argue that either the ZnS etch rate is not dependent on film crystallinity or the ZnS films with thickness of 20 nm were too thin for sufficient sensitivity to determine their crystallinity. The etch rate is expected to be dependent on the film crystallinity based on earlier results for amorphous and crystalline Al2 O3, HfO2, and ZrO2 films. 9,57 The amorphous films of these materials displayed higher etch rates than the corresponding crystalline films. 9,57

Figure 16 shows the RMS roughness of the ZnS surface versus the number of ALE cycles. The roughness of asdeposited 30 nm thick ZnS films grown at 100 ° C was 7.4 Å.

Figure 16. Average RMS roughness of ZnS ALD films grown at 100 ° C and after ZnS ALE at 300 ° C. The ZnS film thickness before ZnS ALE was 30 nm.

<!-- image -->

After 15 ALE cycles, the roughness was slightly decreased to 5.9 Å. However, after 30 ALE cycles, the RMS roughness gradually increased and reached an RMS roughness of 24.7 Å at 100 ALE cycles. Previous ALE studies have reported surface smoothing versus number of ALE cycles. 7,10,11,58 -60 In this study, the surface roughness initially decreased and then increased after 30 ALE cycles. Similar behavior was observed during nickel ALE. 16

The increase in surface roughness with a larger number of ALE cycles could result from the polycrystalline nature of the ZnS ALD films. Although the XRD spectrum of 30 nm thick ZnS ALD films grown at 100 ° C did not show noticeable XRD peaks, the ZnS ALD film could form nanocrystals while the sample was annealing to 300 ° C for the subsequent ALE. Because etch rates have been shown to be dependent on crystallinity, 9,57 once the ZnS film forms crystallites, the etch rate may change depending on the crystallinity. Etching at grain boundaries between crystalline grains could also lead to a larger surface roughness.

## IV. CONCLUSIONS

ZnS thermal ALE was accomplished using sequential exposures of Al(CH3)3 and HF. In situ spectroscopic ellipsometry studies were employed to measure the ZnS etch rates for ZnS ALD films grown at 100 ° C. The etch rates increased with temperature from 1.4 at 225 ° C to 2.1 at 300 ° C. In addition, experiments at 300 ° C revealed that the etch rate for ZnS ALE was self-limiting at longer TMA and HF exposures.

Several mechanisms are possible for thermal ZnS ALE using TMA and HF. ZnS could be fluorinated by HF to produce ZnF2. Subsequently, ZnF2 could undergo ligand exchange with Al(CH3)3 to yield Zn(CH3)2 etch products. Alternatively, TMA could first convert ZnS to Al2 S3. Then HF could fluorinate Al2 S3 to produce AlF3 and H2S. Ligand exchange between AlF3 and TMA would then produce various AlF(CH3)2 etch products.

The conversion mechanism for ZnS ALE was confirmed using in situ QMS studies. The QMS investigations observed that TMA exposures on initial ZnS substrates released Zn(CH3)2 products as expected for the conversion of ZnS to Al2 S3. In addition, HF exposure on the initial ZnS substrates did not produce H2S products. However, after Al(CH3)3 exposures on ZnS, H2S was monitored during HF exposures because Al(CH3)3 converts ZnS to Al2 S3. Time-dependent QMS studies also showed that the conversion, ligandexchange, and fluorination reactions during ZnS ALE were self-limiting.

Larger Al(CH3)3 exposures led to higher ZnS etch rates because the Al2 S3 conversion layer thickness is dependent on Al(CH3)3 exposures. Because HF can fluorinate only the converted Al2 S3 layer thickness, larger HF pressures had a small effect on the ZnS etch rate. The ZnS etch rate was also observed to be dependent on the ZnS ALD growth temperature. The ZnS etch rate at 300 ° C was 1.4, 1.0, and 0.8 Å/cycle for ZnS ALD films grown at 100, 200, and 300 ° C, respectively.

These lower ZnS etch rates for ZnS ALD films grown at higher temperatures may result from the larger density or higher sulfur content of the ZnS ALD films grown at higher temperatures. The diffusion of TMA into ZnS during the conversion reaction may be more difficult at higher ZnS film densities. An increase in the ZnS surface roughness was also observed after a larger number of ALE cycles. This surface roughness may be related to different etch rates for various crystalline phases or grain boundaries between the crystalline grains.

## ■ AUTHOR INFORMATION

## Corresponding Author

Steven M. George -Department of Chemistry, University of Colorado Boulder, Boulder, Colorado 80309, United States; orcid.org/0000-0003-0253-9184;

Email: Steven.George@Colorado.edu

## Authors

- Taewook Nam -Department of Chemistry, University of

Colorado Boulder, Boulder, Colorado 80309, United States; orcid.org/0000-0001-9702-0873 Jonathan L. Partridge -Department of Chemistry, University of Colorado Boulder, Boulder, Colorado 80309, United States; orcid.org/0000-0002-0071-9854

Complete contact information is available at:

https://pubs.acs.org/10.1021/acs.chemmater.3c00616

## Notes

The authors declare no competing financial interest.

## ■ ACKNOWLEDGMENTS

This work was supported in part by the Joint University Microelectronics Program (JUMP) funded by the Semiconductor Research Corporation (SRC). The V-shaped viscous flow reactor was built and the spectroscopic ellipsometer was obtained using funding from Sierra Nevada Corporation. The authors thank Kenneth Smith and Don David from the University of Colorado Integrated Instrument Development Facility for their help in the construction of the V-shaped viscous flow reactor. Funding for the QMS reactor and the QMS investigations was provided by Lam Research. The authors also thank Dr. Andrew Cavanagh for the XPS analysis and Dr. Jessica Murdzek and Rebecca Hirsch for the XRD and XRR analyses.

## ■ REFERENCES

- (1) Carver, C. T.; Plombon, J. J.; Romero, P. E.; Suri, S.; Tronic, T. A.; Turkot, R. B. Atomic Layer Etching: An Industry Perspective. ECS J. Solid State Sci. Technol. 2015 , 4 , N5005 -N5009.
- (2) George, S. M. Mechanisms of Thermal Atomic Layer Etching. Acc. Chem. Res. 2020 , 53 , 1151 -1160.
- (3) Kanarik, K. J.; Lill, T.; Hudson, E. A.; Sriraman, S.; Tan, S.; Marks, J.; Vahedi, V.; Gottscho, R. A. Overview of Atomic Layer Etching in the Semiconductor Industry. J. Vac. Sci. Technol. A 2015 , 33 , No. 020802.
- (4) Fischer, A.; Routzahn, A.; George, S. M.; Lill, T. Thermal Atomic Layer Etching: A Review. J. Vac. Sci. Technol. A 2021 , 39 , No. 030801.
- (5) Faraz, T.; Roozeboom, F.; Knoops, H. C. M.; Kessels, W. M. M. Atomic Layer Etching: What Can We Learn from Atomic Layer Deposition? ECS J. Solid State Sci. Technol. 2015 , 4 , N5023 -N5032.
- (6) DuMont, J. W.; Marquardt, A. E.; Cano, A. M.; George, S. M. Thermal Atomic Layer Etching of SiO2 by a 'Conversion-Etch' Mechanism Using Sequential Reactions of Trimethylaluminum and Hydrogen Fluoride. ACS Appl. Mater. Interfaces 2017 , 9 , 10296 -10307.
- (7) Lee, Y.; George, S. M. Thermal Atomic Layer Etching of Al2O3, HfO2, and ZrO2 Using Sequential Hydrogen Fluoride and Dimethylaluminum Chloride Exposures. J. Phys. Chem. C 2019 , 123 , 18455 -18466.

- (8) Lee, Y.; Johnson, N. R.; George, S. M. Thermal Atomic Layer Etching of Gallium Oxide Using Sequential Exposures of HF and Various Metal Precursors. Chem. Mater. 2020 , 32 , 5937 -5948.
- (9) Murdzek, J. A.; George, S. M. Effect of Crystallinity on Thermal Atomic Layer Etching of Hafnium Oxide, Zirconium Oxide, and Hafnium Zirconium Oxide. J. Vac. Sci. Technol. A 2020 , 38 , No. 022608.
- (10) Zywotko, D. R.; George, S. M. Thermal Atomic Layer Etching of ZnO by a 'Conversion-Etch' Mechanism Using Sequential Exposures of Hydrogen Fluoride and Trimethylaluminum. Chem. Mater. 2017 , 29 , 1183 -1191.
- (11) Lee, Y.; George, S. M. Atomic Layer Etching of Al2O3 Using Sequential, Self-Limiting Thermal Reactions with Sn(acac)2 and Hydrogen Fluoride. ACS Nano 2015 , 9 , 2061 -2070.
- (12) Johnson, N. R.; Hite, J. K.; Mastro, M. A.; Eddy, C. R.; George, S. M. Thermal Atomic Layer Etching of Crystalline GaN Using Sequential Exposures of XeF2 and BCl3. Appl. Phys. Lett. 2019 , 114 , 243103.
- (13) Johnson, N. R.; Sun, H.; Sharma, K.; George, S. M. Thermal Atomic Layer Etching of Crystalline Aluminum Nitride Using Sequential, Self-limiting Hydrogen Fluoride and Sn(acac) 2 Reactions and Enhancement by H2 and Ar Plasmas. J. Vac. Sci. Technol. A 2016 , 34 , No. 050603.
- (14) Cano, A. M.; Lii-Rosales, A.; George, S. M. Thermal Atomic Layer Etching of Aluminum Nitride Using HF or XeF2 for Fluorination and BCl3 for Ligand Exchange. J. Phys. Chem. C 2022 , 126 , 6990 -6999.
- (15) Johnson, N. R.; George, S. M. WO3 and W Thermal Atomic Layer Etching Using 'Conversion-Fluorination' and 'OxidationConversion-Fluorination' Mechanisms. ACS Appl. Mater. Interfaces 2017 , 9 , 34435 -34447.
- (16) Murdzek, J. A.; Lii-Rosales, A.; George, S. M. Thermal Atomic Layer Etching of Nickel Using Sequential Chlorination and LigandAddition Reactions. Chem. Mater. 2021 , 33 , 9174 -9183.
- (17) Konh, M.; He, C.; Lin, X.; Guo, X.; Pallem, V.; Opila, R. L.; Teplyakov, A. V.; Wang, Z.; Yuan, B. Molecular Mechanisms of Atomic Layer Etching of Cobalt with Sequential Exposure to Molecular Chlorine and Diketones. J. Vac. Sci. Technol. A 2019 , 37 , No. 021004.
- (18) Mohimi, E.; Chu, X. Q. I.; Trinh, B. B.; Babar, S.; Girolami, G. S.; Abelson, J. R. Thermal Atomic Layer Etching of Copper by Sequential Steps Involving Oxidation and Exposure to Hexafluoroacetylacetone. ECS J. Solid State Sci. Technol. 2018 , 7 , P491 -P495.
- (19) Lu, W.; Lee, Y.; Gertsch, J. C.; Murdzek, J. A.; Cavanagh, A. S.; Kong, L.; del Alamo, J. A.; George, S. M. In Situ Thermal Atomic Layer Etching for Sub-5 nm InGaAs Multigate MOSFETs. Nano Lett. 2019 , 19 , 5159 -5166.
- (20) Abdulagatov, A. I.; George, S. M. Thermal Atomic Layer Etching of Silicon Using O2, HF, and Al(CH3)3 as the Reactants. Chem. Mater. 2018 , 30 , 8465 -8475.
- (21) Zhu, H.; Qin, X. Y.; Cheng, L. X.; Azcatl, A.; Kim, J.; Wallace, R. M. Remote Plasma Oxidation and Atomic Layer Etching of MoS2. ACS Appl. Mater. Interfaces 2016 , 8 , 19119 -19126.
- (22) Kim, K. S.; Kim, K. H.; Nam, Y.; Jeon, J.; Yim, S.; Singh, E.; Lee, J. Y.; Lee, S. J.; Jung, Y. S.; Yeom, G. Y.; et al. Atomic Layer Etching Mechanism of MoS2 for Nanodevices. ACS Appl. Mater. Interfaces 2017 , 9 , 11967 -11976.
- (23) Lin, T. Z.; Kang, B. T.; Jeon, M. H.; Huffman, C.; Jeon, J. H.; Lee, S. J.; Han, W.; Lee, J. Y.; Lee, S. H.; Yeom, G. Y.; et al. Controlled Layer-by-Layer Etching of MoS2. ACS Appl. Mater. Interfaces 2015 , 7 , 15892 -15897.
- (24) Chen, K. C.; Liu, C. W.; Chen, C.; Lin, S. Y. The Atomic Layer Etching of Molybdenum Disulfides Using Low-Power Oxygen Plasma. Semicond. Sci. Technol. 2019 , 34 , No. 045007.
- (25) Soares, J.; Mane, A. U.; Choudhury, D.; Letourneau, S.; Hues, S. M.; Elam, J. W.; Graugnard, E. Thermal Atomic Layer Etching of MoS2 Using MoF6 and H2O. Chem. Mater. 2023 , 35 , 927 -936.
- (26) Radisavljevic, B.; Radenovic, A.; Brivio, J.; Giacometti, V.; Kis, A. Single-Layer MoS2 Transistors. Nat. Nanotechnol. 2011 , 6 , 147 -150.
- (27) Dasgupta, N. P.; Meng, X.; Elam, J. W.; Martinson, A. B. F. Atomic Layer Deposition of Metal Sulfide Materials. Acc. Chem. Res. 2015 , 48 , 341 -348.
- (28) Smet, P. F.; Moreels, I.; Hens, Z.; Poelman, D. Luminescence in Sulfides: A Rich History and a Bright Future. Materials 2010 , 3 , 2834 -2883.
- (29) Chandrasekaran, S.; Yao, L.; Deng, L. B.; Bowen, C.; Zhang, Y.; Chen, S. M.; Lin, Z. Q.; Peng, F.; Zhang, P. X. Recent Advances in Metal Sulfides: From Controlled Fabrication to Electrocatalytic, Photocatalytic and Photoelectrochemical Water Splitting and Beyond. Chem. Soc. Rev. 2019 , 48 , 4178 -4280.
- (30) Xu, X.; Li, S.; Chen, J.; Cai, S.; Long, Z.; Fang, X. Design Principles and Material Engineering of ZnS for Optoelectronic Devices and Catalysis. Adv. Funct. Mater. 2018 , 28 , 1802029.
- (31) Orloff, G. J.; Elkind, J. L.; Koch, D. Hydrogen Based Reactive Ion Etching of Zinc Sulfide. J. Vac. Sci. Technol. A 1992 , 10 , 1371 -1374.
- (32) Pearton, S. J.; Ren, F. Plasma Etching of ZnS, ZnSe, CdS, and CdTe in Electron-Cyclotron Resonance CH4/H2/Ar and H2/Ar Discharges. J. Vac. Sci. Technol. B 1993 , 11 , 15 -19.
- (33) Saitoh, T.; Yokogawa, T.; Narusawa, T. Reactive Ion-Beam Etching of ZnSe and ZnS Epitaxial Films Using Cl2 ElectronCyclotron Resonance Plasma. Appl. Phys. Lett. 1990 , 56 , 839 -841.
- (34) Rousseau, F.; Jain, A.; Kodas, T. T.; Hampden-Smith, M.; Farr, J. D.; Muenchausen, R. Low Temperature Dry Etching of Metal Oxides and ZnS Via Formation of Volatile Metal Beta-Diketonate Complexes. J. Mater. Chem. 1992 , 2 , 893 -894.
- (35) HSC Chemistry 9.9.2.3, Outokumpu Research Oy, Pori, Finland.
- (36) Devloo-Casier, K.; Geiregat, P.; Ludwig, K. F.; van Stiphout, K.; Vantomme, A.; Hens, Z.; Detavernier, C.; Dendooven, J. A Case Study of ALD Encapsulation of Quantum Dots: Embedding Supported CdSe/CdS/ZnS Quantum Dots in a ZnO Matrix. J. Phys. Chem. C 2016 , 120 , 18039 -18045.
- (37) Elam, J. W.; George, S. M. Growth of ZnO/Al2O3 Alloy Films Using Atomic Layer Deposition Techniques. Chem. Mater. 2003 , 15 , 1020 -1028.
- (38) Myers, T. J.; Cano, A. M.; Lancaster, D. K.; Clancey, J. W.; George, S. M. Conversion Reactions in Atomic Layer Processing with Emphasis on ZnO Conversion to Al2O3 by Trimethylaluminum. J. Vac. Sci. Technol. A 2021 , 39 , No. 021001.
- (39) Junige, M.; George, S. M. Area-Selective Molecular Layer Deposition of Nylon 6,2 Polyamide: Growth on Carbon and Inhibition on Silica. J. Vac. Sci. Technol. A 2021 , 39 , No. 023204.
- (40) Bakke, J. R.; King, J. S.; Jung, H. J.; Sinclair, R.; Bent, S. F. Atomic Layer Deposition of ZnS via in situ Production of H2S. Thin Solid Films 2010 , 518 , 5400 -5408.
- (41) Kim, Y. S.; Yun, S. J. Studies on Polycrystalline ZnS Thin Films Grown by Atomic Layer Deposition for Electroluminescent Applications. Appl. Surf. Sci. 2004 , 229 , 105 -111.
- (42) Lancaster, D. K.; Sun, H. X.; George, S. M. Atomic Layer Deposition of Zn(O,S) Alloys Using Diethylzinc with H2O and H2S: Effect of Exchange Reactions. J. Phys. Chem. C 2017 , 121 , 18643 -18652.
- (43) Li, H. H. Refractive Index of ZnS, ZnSe, and ZnTe and Its Wavelength and Temperature Derivatives. J. Phys. Chem. Ref. Data 1984 , 13 , 103 -150.
- (44) Partridge, J. L.; Murdzek, J. A.; Johnson, V. L.; Cavanagh, A. S.; Fischer, A.; Lill, T.; Sharma, S.; George, S. M. Thermal Atomic Layer Etching of CoO, ZnO, Fe2O3, and NiO by Chlorination and Ligand Addition Using SO2Cl2 and Tetramethylethylenediamine. Chem. Mater. 2023 , 35 , 2058 -2068.
- (45) Lii-Rosales, A.; Cavanagh, A. S.; Fischer, A.; Lill, T.; George, S. M. Spontaneous Etching of Metal Fluorides Using Ligand-Exchange Reactions: Landscape Revealed by Mass Spectrometry. Chem. Mater. 2021 , 33 , 7719 -7730.

- (46) Burns, K. H.; Srivastava, P.; Elles, C. G. Absolute Cross Sections of Liquids from Broadband Stimulated Raman Scattering with Femtosecond and Picosecond Pulses. Anal. Chem. 2020 , 92 , 10686 -10692.
- (47) Colles, M. J.; Griffiths, J. E. Relative and Absolute Raman Scattering Cross-Sections in Liquids. J. Chem. Phys. 1972 , 56 , 3384 -3391.
- (48) Lee, Y.; DuMont, J. W.; Cavanagh, A. S.; George, S. M. Atomic Layer Deposition of AlF3 Using Trimethylaluminum and Hydrogen Fluoride. J. Phys. Chem. C 2015 , 119 , 14185 -14194.
- (49) DuMont, J. W.; George, S. M. Competition between Al2O3 Atomic Layer Etching and AlF3 Atomic Layer Deposition Using Sequential Exposures of Trimethylaluminum and Hydrogen Fluoride. J. Chem. Phys. 2017 , 146 , No. 052819.
- (50) Clancey, J. W.; Cavanagh, A. S.; Smith, J. E. T.; Sharma, S.; George, S. M. Volatile Etch Species Produced during Thermal Al2O3 Atomic Layer Etching. J. Phys. Chem. C 2020 , 124 , 287 -299.
- (51) George, S. M.; Lee, Y. Prospects for Thermal Atomic Layer Etching Using Sequential, Self-Limiting Fluorination and LigandExchange Reactions. ACS Nano 2016 , 10 , 4889 -4894.
- (52) Christ, C. D.; Mark, A. E.; van Gunsteren, W. F. Basic Ingredients of Free Energy Calculations: A Review. J. Comput. Chem. 2010 , 31 , 1569 -1582.
- (53) Cano, A. M.; Marquardt, A. E.; DuMont, J. W.; George, S. M. Effect of HF Pressure on Thermal Al O3 2 Atomic Layer Etch Rates and Al2 O3 Fluorination. J. Phys. Chem. C 2019 , 123 , 10346 -10355.
- (54) Deal, B. E.; Grove, A. S. General Relationship for Thermal Oxidation of Silicon. J. Appl. Phys. 1965 , 36 , 3770 -3778.
- (55) Wolf, E.; Born, M. Principles of Optics: Electromagnetic Theory of Propagation, Interference and Diffraction of Light , 5th ed.; Pergamon Press: Oxford, 1975.
- (56) Kuhs, J.; Dobbelaere, T.; Hens, Z.; Detavernier, C. Plasma Enhanced Atomic Layer Deposition of Zinc Sulfide Thin Films. J. Vac. Sci. Technol. A 2017 , 35 , No. 01B111.
- (57) Murdzek, J. A.; Rajashekhar, A.; Makala, R. S.; George, S. M. Thermal Atomic Layer Etching of Amorphous and Crystalline Al2O3 Films. J. Vac. Sci. Technol. A 2021 , 39 , No. 042602.
- (58) Abdulagatov, A. I.; George, S. M. Thermal Atomic Layer Etching of Silicon Nitride Using an Oxidation and 'Conversion Etch' Mechanism. J. Vac. Sci. Technol. A 2020 , 38 , No. 022607.
- (59) Lee, Y.; DuMont, J. W.; George, S. M. Atomic Layer Etching of HfO2 Using Sequential, Self-Limiting Thermal Reactions with Sn(acac)2 and HF. ECS J. Solid State Sci. Technol. 2015 , 4 , N5013 -N5022.
- (60) Zywotko, D. R.; Faguet, J.; George, S. M. Rapid Atomic Layer Etching of Al O3 2 Using Sequential Exposures of Hydrogen Fluoride and Trimethylaluminum with No Purging. J. Vac. Sci. Technol. A 2018 , 36 , No. 061508.