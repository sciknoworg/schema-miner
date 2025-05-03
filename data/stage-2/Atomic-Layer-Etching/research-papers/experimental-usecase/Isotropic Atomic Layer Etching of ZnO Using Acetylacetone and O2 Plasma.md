<!-- image -->

<!-- image -->

Research Article

Cite This: ACS Appl. Mater. Interfaces 2018, 10, 38588 - 38595

www.acsami.org

## Isotropic Atomic Layer Etching of ZnO Using Acetylacetone and O2 Plasma

A. Mameli, † M. A. Verheijen, † A. J. M. Mackus, † W. M. M. Kessels, † and F. Roozeboom * , † ‡ ,

† Department of Applied Physics, Eindhoven University of Technology, P.O. Box 513, Eindhoven 5600 MB, The Netherlands ‡ TNO-Holst Centre, High Tech Campus 21, Eindhoven 5656 AE, The Netherlands

- * S Supporting Information

ABSTRACT: Atomic layer etching (ALE) provides Ångstrom-level control over ̈ material removal and holds potential for addressing the challenges in nanomanufacturing faced by conventional etching techniques. Recent research has led to the development of two main classes of ALE: ion-driven plasma processes yielding anisotropic (or directional ) etch pro /uniFB01 les and thermally driven processes for isotropic material removal. In this work, we extend the possibilities to obtain isotropic etching by introducing a plasma-based ALE process for ZnO which is radical-driven and utilizes acetylacetone (Hacac) and O2 plasma as reactants. In situ spectroscopic ellipsometry measurements indicate self-limiting half-reactions with etch rates ranging from 0.5 to 1.3 Å/cycle at temperatures between 100 and 250 ° C. The ALE process was demonstrated on planar and three-dimensional substrates consisting of a regular array of semiconductor nanowires (NWs) conformally covered using atomic layer deposition of ZnO. Transmission electron microscopy studies conducted on the ZnO-covered NWs

<!-- image -->

before and after ALE proved the isotropic nature and the damage-free characteristics of the process. In situ infrared spectroscopy measurements were used to elucidate the self-limiting nature of the ALE half-reactions and the reaction mechanism. During the Hacac etching reaction that is assumed to produce Zn(acac)2, carbonaceous species adsorbed on the ZnO surface are suggested as the cause of the self-limiting behavior. The subsequent O 2 plasma step resets the surface for the next ALE cycle. High etch selectivities ( ∼ 80:1) over SiO2 and HfO2 were demonstrated. Preliminary results indicate that the etching process can be extended to other oxides such as Al O . 2 3

KEYWORDS: atomic layer etching, plasma etching, isotropic removal, ZnO, nanowires

## ■ INTRODUCTION

As the smallest features in semiconductor devices continue shrinking toward single-digit nanometer dimensions in order to enable ever-higher performance and cost-e /uniFB00 ective electronics, techniques for precise material deposition and/or removal are of paramount importance. 1 -4 Aggressive scaling of siliconbased devices has been enabled by the availability of advanced processing techniques. Here, an example is the so-called selfaligned multiple patterning that allows to pattern structures far below the limits of immersion lithography, and it is currently implemented during /uniFB02 ash memory and multigate [ /uniFB01 n /uniFB01 elde /uniFB00 ect transistor ( /uniFB01 nFET)] fabrication. 5 Looking further ahead, atomic-scale processing will become a necessity in order to enable technological leaps forward such as in the Internet of Things and arti /uniFB01 cial intelligence. 6 For example, the development of advanced computing methods such as neuromorphic and quantum computing requires to process atomically thin and other exotic materials into complex architectures. 7 -9 Here, precise deposition and etching techniques are imperative to create and manipulate low-dimensional structures such as twodimensional materials, nanowire (NW) arrays, or quantum dots into functional device structures. 6

<!-- image -->

In the past decades, atomic layer deposition (ALD) has become an established technique to provide unparalleled control over thin/uniFB01 lm deposition, even on the high-aspect ratio structures that are increasingly used in the semiconductor industry. On the other hand, its etching counterpart, that is, atomic layer etching (ALE), is only recently emerging as an enabling technique for advanced etch applications. ALE is still in its infancy, and further advancement in this research /uniFB01 eld will be necessary to expand the capabilities and the toolbox of atomic-scale processing. 5 In ALE, atomic-scale control during material removal is achieved through the use of alternated and self-limiting half-reactions that are interleaved by purge steps. Because of this characteristic, ALE allows to achieve Ångstrom-̈ level control, high uniformity, and extreme pattern /uniFB01 delity over material removal. 10 -14

ALE is usually classi /uniFB01 ed into two categories: anisotropic (directional) and isotropic etching, depending on the targeted application. Of these, anisotropic ALE is being largely investigated as it holds promise for pattern transferring,

Received:

July 27, 2018

Accepted:

October 4, 2018

Published:

October 4, 2018

DOI: 10.1021/acsami.8b12767 -

ACS Appl. Mater. Interfaces 2018, 10, 38588 38595

etching of sacri /uniFB01 cial layers during self-aligned multiple patterning, and patterning of gate spacers during /uniFB01 nFET fabrication. 13,15 -17 On the other hand, with the increasing number of complex three-dimensional (3D) structures that are created for device fabrication, the need for isotropic ALE is getting increasing attention. Isotropic ALE is deemed essential for patterning of the gate spacer in future gate-all-around FETs where highly selective and conformal material removal is required. 18 Moreover, isotropic ALE has been proposed for achieving high-resolution nanoimprint lithography 19 and lateral etching in 3D-NAND /uniFB02 ash memories fabrication. 20 ALE has also great potential in replacing wet etching processes where the liquid etchants with their critical surface tensions may cause capillary e /uniFB00 ects that make nanometer-sized patterns collapse. 20 Furthermore, ALE may also /uniFB01 nd applications in /uniFB01 ne-tuning the transport properties of NW -metal contacts by nanoscale removal of the native semiconductor material at the edge of the nanocontact. 21

Anisotropic ALE is generally associated with plasma-based processing. Here, the ionic component of a plasma is harnessed to provide directionality. This is typically achieved by applying an external bias voltage to the substrate table, during the plasma-based half-reaction. Because of the negative bias voltage applied, ions are accelerated in the plasma sheath and thus impinge normally to the surface (ion-driven plasmabased reaction). 22 During the /uniFB01 rst half-reaction (A), the surface of the target material is modi ed /uniFB01 in a self-limiting manner by the exposure to a reagent. In the second halfreaction (B), the modi ed material is removed by means of /uniFB01 ion-driven plasma-based reactions. Provided the ion energy is below the sputtering threshold, only subsurface bonds are broken and volatile products are released from the surface of the target material. 10,11,13,14,23,24

On the other hand, isotropic ALE is achieved by employing nondirectional species in both half-reactions. Recently, George and co-workers introduced thermal ALE, where sequential and self-limiting thermochemical (i.e., without the use of plasma species) half-reactions are alternated in a cyclic fashion. 2,12,25 -28 During half-reaction A, the surface of the target material is modi /uniFB01 ed in a self-limiting manner by the exposure to a reagent and subsequently removed by means of a suitable ' coreactant ' in the half-reaction B.

Isotropic ALE can also be carried out by using a plasmabased process, as long as the plasma is operated in a regime that harnesses the isotropic nature of reactive plasma radicals. In contrast to ions which are charged and are accelerated over the plasma sheath, neutral radical species di /uniFB00 use toward the surface, therefore initiating isotropic surface reactions (radicaldriven plasma-based reaction). This regime, which will be the focus of this work, has been less explored for ALE. 18,29,30

The possibilities for achieving ALE are manifold, and di /uniFB00 erent processing steps could also be combined (e.g., iondriven reactions, neutral beams, radical-driven reactions, t h e r m o c h e m i c a l r e a c t i o n s , a n n e a l i n g s t e p s , etc.) 2,6 -9,13,14,20 -28 to achieve the required etch pro /uniFB01 le, etch selectivity, and process compatibility. Figure 1 illustrates some of the possible ALE approaches which are categorized by the following:

- (i) the resulting etch pro /uniFB01 le: anisotropic or isotropic, and
- (ii) the employed surface reactions: plasma-based or purely thermally driven.

Figure 1. Schematic overview of several approaches for ALE categorized into anisotropic and plasma-based; isotropic and plasma-based; and isotropic and purely thermally driven. Anisotropic ALE can be obtained by employing (a) plasma radical-driven reaction to modify the material surface (half-reaction A) and plasma-generated ions or neutral beams to directionally remove the modi /uniFB01 ed layer (B); (b) thermochemical reaction to modify the material surface (A) and plasma-generated ions or neutral beams to directionally remove the modi ed /uniFB01 layer (B). Isotropic ALE can be obtained using (c) thermochemical reaction to remove the material, while surface modi cation /uniFB01 takes place (A), and a radical-driven plasma step to reset the surface (B); (d) plasma radical-driven reaction to modify the material surface (A) and a thermal annealing step to desorb the modi ed /uniFB01 layer (B); (e) thermochemical reaction to modify the surface (A) and a second thermochemical reaction to remove the modi ed surface layer (B); or (f) thermochemical reaction to modify /uniFB01 the surface (A) and a thermal annealing step to desorb the modi /uniFB01 ed layer (B). Examples of the approaches are given in refs 11, 13, 14 for (a); ref 24 for (b); this work for (c); refs 18, 20, 31 for (d); refs 13, 16 for (e); and ref 32 for (f).

<!-- image -->

In this work, we introduce a novel approach for isotropic ALE by combining a thermochemical half-reaction with a plasma radical-driven half-reaction (see Figure 1c). In particular, a thermochemical reaction (half-reaction A) that employs acetylacetone (Hacac) is used to remove the material.

This reaction appears to be self-terminating because of the formation of a carbonaceous surface layer that inhibits further etching. Next, a radical-driven O 2 plasma pulse (half-reaction B) is used to restore the surface for the next ALE cycle. The process concept is inspired by the use of Sn(acac) 2 in thermal ALE 2,26,33 and β -diketones in organic vapor-phase etching. 34 -39

ALD-grown polycrystalline ZnO layers were chosen for demonstrating the feasibility of our process. This plasma-based ALE process can serve as an alternative approach to thermal ALE of ZnO using trimethylaluminum (TMA) and /uniFB02 uorinebased chemistry, which was recently conducted on planar substrates by Zywotko et al. 27

We observed that alternating dosage of Hacac and O2 plasma led to a reproducible etch per cycle (EPC) of 1.3 Å. Furthermore, the isotropic nature of the ALE process presented in this work was demonstrated by etching ZnO that was predeposited on an array of vertical NWs. A reaction mechanism is proposed on the basis of in situ Fourier transform infrared (FTIR) measurements. Finally, we discuss the possibility of extending this process to other oxide /uniFB01 lms, such as Al O3, and show high etch selectivities ( 2 ∼ 80:1) over SiO2 and HfO2.

## ■ EXPERIMENTAL SECTION

ZnO Preparation by ALD. ZnO thin /uniFB01 lms were deposited on 2 × 2 cm 2 c-Si wafer coupons using ALD in an OpAL reactor from Oxford Instruments equipped with a 200 mm substrate table. Diethylzinc (DEZ) and water (H2O) were employed as the precursor and the coreactant, respectively, at a substrate temperature of 250 ° C. The recipe consisted of 40 ms of DEZ and 100 ms of H2O exposure interleaved by 5 s argon purges. The same recipe was also employed to deposit conformal layers of ZnO on substrates with GaP NWs, having a 7% Ge-doped Si (Si/Ge) shell.

From separate studies on the bare NWs, it is known that these wires exhibit atomically /uniFB02 at sidewall facets, making them an excellent substrate for etch pro /uniFB01 le studies. 40 The temperature was 150 ° C during the deposition on the NW samples.

ALE Process of ZnO. The etching experiments were carried out in an Oxford Instruments FlexAL reactor, equipped with a remote inductively coupled plasma (ICP) source (13.56 MHz), a 200 mm substrate table, a turbomolecular pump, and a loadlock. Prior to all etching experiments, the samples were subjected to a 3 min O 2 plasma cleaning step at a pressure of ∼ 10 mTorr and a power of 200 W.

Hacac ( ≥ 99% ReagentPlus; CAS 123-54-6) from Sigma-Aldrich was employed without further puri /uniFB01 cation. Hacac was kept at room temperature in a stainless-steel container and vapor-drawn into the chamber using multiple pulses of 2 s each and a 1 s hold step ( ∼ 400 mTorr), interleaved by 5 s long intermittent Ar purges (300 sccm). The ALE cycle was completed by a 5 s O2 plasma step at a pressure of ∼ 10 mTorr (stabilized by a preliminary 3 s O2 /uniFB02 ow in conjunction with a butter /uniFB02 y valve before the turbopump) and an ICP power of 200 W, followed by a separate 5 s Ar purge (100 sccm). For a schematic of the cycle, see the Supporting Information (Figure S1). The etching experiments were conducted at substrate temperatures of 100, 150, 200, or 250 ° C.

Analytical Methods. In situ and ex situ spectroscopic ellipsometry (SE) was performed using a J.A. Woollam M2000D ellipsometer. A Cauchy parameterization was used to model the ψ -and δ -values measured by SE. X-ray photoelectron spectroscopy measurements were carried out using a K-Alpha system from ThermoFisher Scienti /uniFB01 c. To study the resulting etch pro /uniFB01 le of this ALE process, an array of NWs were covered with ZnO layers using ALD (see above). Part of this array was subjected to the ALE process and compared with nonetched NW samples using transmission electron microscopy (TEM). Several NWs were taken and analyzed using TEM to determine the ZnO thickness before and after ALE.

The TEM measurements were conducted in high-angle annular dark/uniFB01 eld (HAADF) -scanning TEM (STEM) and high-resolution TEM modes using a probe-corrected TEM system (JEOL JEM ARM 200F). The ZnO thickness was measured at distinct regions separated by 1 μ malong the length of each NW sample using ImageJ software. 41 Twenty thickness measurements were taken at each region and averaged to account for the ZnO surface roughness.

In situ FTIR transmission spectroscopy experiments were carried out in a home-built ALD setup (which is similar to the reactor used for the ALE experiments), using a Bruker Vector FTIR spectrometer with a mid-infrared light source (Globar ≈ 10 000 -50 cm -1 ) and a liquid N -cooled mercury cadmium telluride detector with a spectral 2 range of 12 000 -550 cm -1 . FTIR measurements were performed on ZnO nanopowder (&lt;100 nm particle size) that was pellet-pressed on a tungsten mesh. The powder was heated to 150 ° C by passing a current through the mesh. The reaction chamber was pressurized with Hacac vapor and held at a constant pressure of ∼ 1 Torr for 30 s to ensure adsorption of Hacac on the powder. The pressure during the plasma step was ∼ 10 mTorr.

## ■ RESULTS AND DISCUSSION

ZnO ALE on Planar Substrates. The etching behavior was investigated using in situ SE by monitoring the ZnO /uniFB01 lm thickness upon exposure to three di /uniFB00 erent pulse sequences: (1) alternated pulses of Hacac and O2 gas, (2) alternated pulses of Hacac and O 2 plasma, and (3) multiple pulses of only O2 plasma. The O2 gas pulses in sequence 1 were included to keep the cycle time constant and as a control experiment to assess whether the O2 plasma is necessary to achieve etching. Figure 2 shows the ZnO thickness variation for pulse

Figure 2. ZnO thickness evolution as a function of the number of cycles for (a) sequence 1: Hacac and O 2 gas (circles); (b) sequence 2: Hacac and O2 plasma (squares); and (c) sequence 3: only O 2 plasma pulses (diamonds). Signi /uniFB01 cant ZnO thickness decrease was observed only for sequence 2. All of the experiments were carried out at a temperature of 250 ° C.

<!-- image -->

sequences 1, 2, and 3 for a process temperature of 250 ° C. Pulsing sequences 1 and 3 resulted in no signi /uniFB01 cant ZnO thickness change (Figure 2a,c), whereas sequence 2 induced a linear thickness decrease (Figure 2b). An EPC value of 1.31 ± 0.08 Å was calculated by linear regression of the data shown in Figure 2b. These results demonstrate the unique synergy of the alternated dosing of Hacac and O 2 plasma (sequence 2) that is required to achieve ZnO etching, whereas no signi /uniFB01 cant ZnO etching is observed when dosing only one of the two reactants. Looking in more detail at sequence 1 in Figure 2a, we note that upon exposure to Hacac an apparent thickness increase of ∼ 2 Å was detected after the /uniFB01 rst 10 cycles, whereas the thickness decreases slightly afterward. This apparent thickness increase

Figure 3. (a) EPC as a function of the Hacac exposure time for a /uniFB01 xed O2 plasma step of 5 s. Saturation (self-limiting behavior) was reached for a total Hacac exposure of 27 s, resulting in an EPC of 1.31 Å/cycle. (b) EPC as a function of the O 2 plasma exposure time for a /uniFB01 xed Hacac dose of 27 s. A saturated EPC value was measured for all the investigated O 2 plasma exposure times ( ≥ 2 s). The processing temperature was 250 ° C. The dashed lines serve as a guide to the eye.

<!-- image -->

can be attributed to the adsorption of Hacac molecules onto the ZnO surface, similarly to what has been observed on Al O 2 3 substrates for the ABC-type area-selective ALD of SiO . 2 42 The subsequent thickness decrease might be due to partial decomposition of acac species on the ZnO surface as will be discussed below. Note that the measured thickness does not decrease below the starting ZnO thickness during sequence 1.

To investigate the self-limiting nature of the ALE halfreactions, in situ SE was used to measure the EPC at a /uniFB01 xed exposure time of the /uniFB01 rst half-reaction, while varying the exposure time of the second half-reaction and vice versa. Figure 3a,b shows the measured EPC values as a function of the Hacac and O2 plasma exposures, respectively. The EPC as a function of the Hacac exposure was observed to saturate at a value of 1.31 ± 0.08 Å for a total Hacac exposure time of 27 s (including the hold steps as described in the Experimental Section). The EPC as a function of the O2 plasma exposure time shows saturation already after 2 s. Longer O2 plasma exposures result in EPC values that lie within the error range. Taken together, these data demonstrate the self-limiting nature of the two half-reactions employed.

Figure 4 displays the ZnO thickness as a function of the number of ALE cycles for temperatures in a range of 100 -250

Figure 4. ZnO thickness as a function of the number of ALE cycles for temperatures between 100 and 250 ° C, as measured by in situ SE.

<!-- image -->

° C. The ZnO thickness was found to decrease linearly with the number of ALE cycles for each temperature, in line with a layer-by-layer etching mechanism. The EPCs were determined to be 0.54 ± 0.05, 0.97 ± 0.07, 1.25 ± 0.08, and 1.31 ± 0.08 Å for processing temperatures of 100, 150, 200, and 250 ° C, respectively.

The surface of the ZnO thin /uniFB01 lms, before and after ALE, was investigated by ex situ XPS to check for possible stoichiometry alterations and for the presence of surface contamination (see the Supporting Information, Table S1). The stoichiometry, as in the ratio Zn/O, was found to be preserved over 100 ALE cycles. A comparable amount of carbon (12 -13 at. %) was measured on both surfaces, which can be attributed to the adsorption of adventitious carbon on the sample upon exposure to atmosphere.

ZnO ALE on 3D Substrates. The ALE process was also tested on a 3D substrate consisting of a regular array of vertical NWs (see the Supporting Information, Figure S2), conformally covered with a 60 ± 2 nm thick polycrystalline ZnO layer. The NWs were then subjected to 120 cycles of the ALE process at 250 ° C. Figure 5a,b shows the TEM images of a pair of 7 μ m long NWs, one before and one after ALE. For each of those NWs, high-magni /uniFB01 cation STEM images were acquired every 1 μ malong the length of the NW. For the complete set of STEM images, see the Supporting Information (Figure S3).

Figure 5a,b also displays high-magni /uniFB01 cation STEM images recorded at the top, center, and bottom regions of each NW. STEM images of an extra independent pair of NWs from the same array, before and after ALE, are shown in the Supporting Information (Figure S4), together with the measured ZnO thicknesses.

The STEM images reveal a decrease in ZnO thickness after the ALE process. The /uniFB01 lm thickness reduction (15 ± 2 nm) is comparable at all regions of the NW, as depicted in Figure 5c. From the STEM-measured thickness di /uniFB00 erences (before and after ALE), an averaged EPC of 1.3 ± 0.2 Å was obtained across the full length of the NW. This EPC value is in excellent agreement with the EPC measured by in situ SE (i.e., 1.31 Å/ cycle). The result clearly demonstrates the accurate etch control and the isotropic nature of the ALE process. Figure 5d shows a high-resolution TEM image of the top ZnO layers after the ALE process. Lattice fringes are visible up to the top surface layer, demonstrating that the ZnO surface retains its crystallinity upon ALE. 43 This result indicates that no signi /uniFB01 cant damage or amorphization occurs during the ALE process. The observed isotropic etch pro /uniFB01 le and the fact that the ZnO surface is not damaged or amorphized are in line with a negligible role of ions in the ALE mechanism, illustrating that the O2 plasma ALE half-reaction is predominantly driven by radicals. Indeed, for the employed plasma conditions described in the Experimental Section (ALE process of ZnO), ion

Figure 5. Low-magni /uniFB01 cation HAADF -STEM image of a ZnOcovered NW together with high-magni /uniFB01 cation images of the top, center, and bottom regions (a) before and (b) after ALE. (c) Averaged ZnO thicknesses as measured every micrometer along the NWs before and after ALE. The standard deviation of the measurements is taken as the error. (d) High-magni /uniFB01 cation TEM image of the ZnO layer after the ALE process. Lattice fringes are observable up to the top surface, indicating that no surface amorphization occurs during the ALE process.

<!-- image -->

energies of only ∼ 20 eV can be expected, 44 which makes sputtering of ZnO through ion-induced collisions unlikely.

Proposed Reaction Mechanism. In situ FTIR spectroscopy was used to elucidate the self-limiting behavior of the ALE process. Figure 6a,b shows the FTIR spectra after three consecutive Hacac or O2 plasma exposures on the pelletpressed ZnO powder at a temperature of 150 ° C. After the /uniFB01 rst Hacac dose, adsorption of Hacac is shown by the appearance of positive peaks between 900 and 1600 cm -1 (Figure 6a). These peaks can be assigned to acac species bonded to Zn 2+ sites. 45 -47 Most likely, Hacac adsorbs through a protontransfer reaction. 42

Figure 6a shows that the peak intensities remain constant after the /uniFB01 rst exposure, indicating saturation behavior for the Hacac adsorption on ZnO. The ZnO stretching modes ( ∼ 480 cm -1 ) fall outside the detection range of the setup and could not be monitored during the in situ measurements. Figure 6b reveals that upon O2 plasma exposure, acac species are removed from the ZnO surface. In this case, the spectra are referenced to the preceding Hacac exposure (third Hacac dose); therefore, the same absorption features show up as negative peaks, pointing at the removal of acac species from the surface. The removal most likely takes place through combustion reactions. Prolonged O2 plasma exposure caused a slight increase in the absorbance of the negative peaks, indicating further acac-species elimination. However, Figure 6c shows that complete removal is not achieved. This is probably

Figure 6. Di /uniFB00 erence infrared spectra for three consecutive exposures of (a) Hacac and (b) O2 plasma on ZnO powder at 150 ° C. The reference spectrum for the Hacac doses was the bare ZnO powder. For the O2 plasma pulses, the spectra were referenced to the preceding Hacac exposure (third Hacac dose); therefore, the removal of species shows up as negative peaks. The spectrum baselines have been equally shifted for clarity. (c) Di /uniFB00 erence spectrum between the third Hacac dose and the 15 min O2 plasma exposure, indicating the presence of residual acac species on the ZnO surface. Peak assignment, after ref 47: 1 ν (C  O); 2 ν (C  C) + ν (C  O), ν (C  O) + δ (C -H); 3 δ (C -H) + δ (CH3); 4 ν (C -C) + ν (C -CH3); 5 δ (CH3); 6 δ (C -CH3)+ ν (C  O), where ν and δ indicate stretching and bending, respectively.

<!-- image -->

due to the high surface area and complex topography of the ZnO powder that hamper the plasma reactions in the ' bulk ' of the powder.

The in situ FTIR data can be used to propose a reaction mechanism and hence an explanation for the self-limiting nature of the ALE process. As schematically depicted in Figure 7, volatile Zn(acac)2 is assumed to be the etching product of the /uniFB01 rst half-reaction (A), that is, ZnO starts to be etched. At the same time, the FTIR data in Figure 6a indicate that during this etching reaction, stable surface acac species build up on the ZnO surface. It can be speculated that acac-species binding in a chelate con /uniFB01 guration (the two oxygen atoms of the same Hacac binding to the same Zn atom) can lead to the formation of volatile Zn(acac) 2 upon further reaction with another Hacac molecule (see reaction pathway 1, Figure S5). On the contrary, acac species adsorbed in a bidentate con /uniFB01 guration (the two oxygen atoms of the same Hacac binding to neighboring Zn atoms at the surface) cannot form a volatile product (see reaction pathway 2, Figure S5). The bidental acac surface species can remain stable on the surface (and account for the surface acac species observed by FTIR, Figure 6a), or they may partially decompose into hydrocarbon fragments. These inhibiting species remaining after half-reaction A constitute a carbonaceous layer that e /uniFB00 ectively blocks continuous etching of ZnO, which explains the self-limiting nature of the process. Similar conclusions were also drawn by Lee et al. for the thermal ALE of AlF3 using Sn(acac)2 and hydrogen /uniFB02 uoride (HF). 12 They also ascribe the self-limiting etching of AlF 3 to the presence of acac-containing surface species that inhibit the

Figure 7. Schematic of the proposed reaction mechanism for ALE of ZnO. During half-reaction A, volatile Zn(acac) 2 is assumed to form from Hacac and ZnO, while leaving residual acac species and other possible carbonaceous fragments. During half-reaction B, an O2 plasma combusts the carbonaceous surface species and resets the ZnO surface for the next cycle.

<!-- image -->

main etching reaction. In addition, Helms et al. have proposed that part of the Hacac may decompose on the metal oxide surfaces and form a carbonaceous layer that can also contribute to inhibiting the etching reaction. 48

In the second half-reaction (B), acac groups and/or related carbonaceous inhibiting species are removed from the ZnO surface by the O2 plasma step, as corroborated by the FTIR data in Figure 6b. Therefore, the role of the O 2 plasma may be primarily to remove the carbonaceous inhibiting layer that is formed during the half-reaction A, thereby allowing etching in a cyclic fashion.

Extension to Other Materials and Etch Selectivity. The possibilities of extending this ALE process to other materials were also explored. To this end, substrates with ALDprepared ZnO, HfO2, and Al2 O3 thin /uniFB01 lms and a 90 nm thermally grown SiO2 layer were subjected to 120 cycles of the ALE process at a temperature of 250 ° C within the same run. Their thicknesses were measured by ex situ SE, before and after ALE. Virtually, no thickness reduction ( ∼ 0.2 nm) was observed for SiO2 and HfO2, whereas a decrease in the thickness of 1.8 nm was observed for Al O 2 3 and ∼ 16.0 nm for ZnO. These results translate into high etch selectivities ( ∼ 80:1) for ZnO over SiO2 and HfO2 at 250 ° C.

The absence of SiO2 etching can be explained by density functional theory simulations that we performed for the chemisorption reaction of Hacac on SiO2. 42 On this surface, the Hacac chemisorption was found to be thermodynamically unfavorable; therefore, SiO2 etching was not expected. The etching of HfO2 , on which Hacac does adsorb, 42 would require the formation of Hf(acac) , which we believe is unlikely on a 4 surface because of steric reasons.

On Al2O3, the measured thickness di /uniFB00 erence translates into a formal EPC value of 0.15 Å. Similar EPC values between 0.14 and 0.61 Å (at 150 and 250 ° C, respectively) have been reported for the thermal ALE of Al2O3 using Sn(acac)2 and HF. 3 Our results indicate that the ALE process introduced in this work may be explored and optimized (temperature, dosing time, etc.) to enable the etching of materials other than ZnO.

Considering the proposed reaction mechanism (Figure 7), it can be inferred that metal oxides that coordinate up to three acac -ligands may be etched using this process. As described by George et al., Al O , Sc O , Fe O , Ga O , and Co O3 2 3 2 3 2 3 2 3 2 can all form volatile compounds with Hacac having vapor pressures ranging from 1 to 4 Torr at 150 ° C. 2,49 Therefore, it should be possible to achieve etching of these materials. Conversely, no etching should be expected in the case of metal oxides in which the metal cation is in the 4 + oxidation state.

Merits and Opportunities Provided by the Approach. When comparing the plasma-based ALE process presented in this work with the complementary thermal ALE process of ZnO using TMA and HF, 27 several di /uniFB00 erences can be highlighted. Although the thermal ALE process was reported to leave residual Al and F impurities on the ZnO surface, 27 this plasma-based ALE approach shows no signi /uniFB01 cant surface contamination, thereby suggesting a cleaner etching chemistry. In the case of thermal ALE, no ZnO etching was observed for temperatures below 220 ° C; conversely, the plasma-based ALE can be used to etch ZnO at temperatures as low as 100 ° C. Furthermore, the two ALE processes allow for di /uniFB00 erent and complementary etch selectivities, thereby expanding the possibilities of ALE. For example, the thermal ALE process, using TMA and HF, can be used to achieve etching of ZnO, Al2 O3, SiO2, and HfO2. 27,50,51 Conversely, the plasma-based ALE process, using Hacac and O2 plasma, can be used to etch ZnO and Al2O3, with high etch selectivities over SiO2 and HfO2. This complementary di /uniFB00 erence in etch selectivity represents a valuable addition to the isotropic ALE toolbox.

In addition, the versatility of a plasma reactant can be used to tune the same etching chemistry from an isotropic to an anisotropic mode by carefully adjusting the plasma conditions. 29 During the plasma step, an external bias voltage can be applied to the substrate to provide directionality, if required. Alternatively, the ALE process can be extended by introducing a third step, consisting of a separate anisotropic plasma.

Finally, the use of di /uniFB00 erent plasma chemistries can pave the way to the processing of other materials than oxides, for example, nitrides, sul /uniFB01 des, and so forth.

## ■ CONCLUSIONS

A novel isotropic plasma-based approach for the ALE of ZnO was demonstrated. This process employs alternating exposures of the ZnO surface to Hacac and O2 plasma. The self-limiting behavior was veri /uniFB01 ed for both half-reactions using in situ SE measurements. Furthermore, the isotropic nature of this process was established by carrying out ALE on a ZnOcovered 3D nanostructured substrate consisting of a vertical NW array. Controlled and uniform decrease of the ZnO /uniFB01 lm thickness across the entire NW length was demonstrated. Damage-free (no amorphization) ALE was corroborated by showing that the uppermost ZnO layers remained crystalline after 120 cycles.

A reaction mechanism was proposed for the ZnO ALE process in which Hacac is assumed to produce volatile Zn(acac)2. In addition, the Hacac pulse also results in acac species adsorbed on the ZnO surface and possibly other carbonaceous species that quench the etching reaction. The O 2 plasma coreactant removes the adsorbed organic species and resets the ZnO surface, allowing for subsequent etching in the next cycle. Furthermore, etching of Al2 O3 and a high etch selectivity ( ∼ 80:1) over SiO2 and HfO2 were demonstrated.

When compared to isotropic thermal ALE processes in the literature, the isotropic plasma-based ALE process presented in this work exhibits di /uniFB00 erent etch selectivities and a wider temperature window. Therefore, we believe that this novel

plasma-based approach will provide additional pathways for achieving isotropic ALE and holds potential for future applications involving high surface area and complex 3D structures for which Ångstrom-level ̈ control over material removal is imperative.

## ■ ASSOCIATED CONTENT

## * S Supporting Information

The Supporting Information is available free of charge on the ACS Publications website at DOI: 10.1021/acsami.8b12767.

Schematic of the ZnO ALE cycle developed in this work; elemental analysis from XPS surface scans of ZnO samples before and after ALE; SEM cross-sectional image of the GaP NW substrate; low-magni /uniFB01 cation HAADF -STEM image of the ZnO-covered NW; highmagni /uniFB01 cation HAADF -STEM images; and schematic of possible reaction pathways (PDF)

## ■ AUTHOR INFORMATION

## Corresponding Author

E-mail: f.roozeboom@tue.nl.

## ORCID

A. Mameli: 0000-0001-9175-8965

A. J.

M. Mackus: 0000-0001-6944-9867

W. M. M. Kessels: 0000-0002-7630-8226

*

## Author Contributions

All authors have given approval to the /uniFB01 nal version of the manuscript.

## Notes

The authors declare no competing /uniFB01 nancial interest.

## ■ ACKNOWLEDGMENTS

This work was supported by TNO-Holst Centre. Solliance and the Dutch Province of Noord-Brabant are acknowledged for funding the TEM facility. The authors would like to thank Yizhen Ren and Erik Bakkers for providing the substrate samples with NWs and Valerio Di Palma, Bora Karasulu, and Tahsin Faraz for valuable discussions. Janneke Zeebregts, Caspar van Bommel, Joris Meulendijks, Jeroen van Gerwen, and Cristian van Helvoirt are acknowledged for technical assistance.

## ■ REFERENCES

- (1) Fang, M.; Ho, J. C. Area-Selective Atomic Layer Deposition: Conformal Coating, Subnanometer Thickness Control, and Smart Positioning. ACS Nano 2015 , 9 , 8651 -8654.
- (2) George, S. M.; Lee, Y. Prospects for Thermal Atomic Layer Etching Using Sequential, Self-Limiting Fluorination and LigandExchange Reactions. ACS Nano 2016 , 10 , 4889 -4894.
- (3) Lee, Y.; George, S. M. Atomic Layer Etching of Al2O3 Using Sequential, Self-Limiting Thermal Reactions with Sn(acac)2 and Hydrogen Fluoride. ACS Nano 2015 , 9 , 2061 -2070.
- (4) Kong, L.; Song, Y.; Kim, J. D.; Yu, L.; Wasserman, D.; Chim, W. K.; Chiam, S. Y.; Li, X. Damage-Free Smooth-Sidewall InGaAs Nanopillar Array by Metal-Assisted Chemical Etching. ACS Nano 2017 , 11 , 10193 -10205.
- (5) Pan, D. Z.; Liebmann, L.; Yu, B.; Xu, X.; Lin, Y. Pushing Multiple Patterning in Sub-10 nm. Proceedings of the 52nd Annual Design Automation Conference on  DAC 15 ' 2015, pp 1 -6.
- (6) Clark, R.; Tapily, K.; Yu, K.; Hakamata, T.; Consiglio, S.; Meara, D. O.; Wajda, C.; Smith, J.; Leusink, G. Perspective : New Process Technologies Required for Future Devices and Scaling. APL Mater. 2018 , 6 , 058203.
- (7) Veldhorst, M.; Eenink, H. G. J.; Yang, C. H.; Dzurak, A. S. Silicon CMOS Architecture for a Spin-Based Quantum Computer. Nat. Commun. 2017 , 8 , 1766.
- (8) Ryder, C. R.; Wood, J. D.; Wells, S. A.; Hersam, M. C. Chemically Tailoring Semiconducting Two-Dimensional Transition Metal Dichalcogenides and Black Phosphorus. ACS Nano 2016 , 10 , 3900 -3917.
- (9) Burr, G. W.; Shelby, R. M.; Sebastian, A.; Kim, S.; Kim, S.; Sidler, S.; Virwani, K.; Ishii, M.; Narayanan, P.; Fumarola, A.; Sanches, L. L.; Boybat, I.; Le Gallo, M.; Moon, K.; Woo, J.; Hwang, H.; Leblebici, Y. Neuromorphic Computing Using Non-Volatile Memory. Adv. Phys.: X 2017 , 2 , 89 -124.
- (10) Lill, T.; Kanarik, K. J.; Tan, S.; Shen, M.; Hudson, E.; Pan, Y.; Marks, J.; Vahedi, V.; Gottscho, R. A. Directional Atomic Layer Etching in Encyclopedia of Plasma Technology ; Shohet, J. L., Ed.; Taylor &amp; Francis Group, CRC Press: Boca Raton, FL, 2016; Ch. 13 for your reference; eBook ISBN 9781482214314.
- (11) Kanarik, K. J.; Lill, T.; Hudson, E. A.; Sriraman, S.; Tan, S.; Marks, J.; Vahedi, V.; Gottscho, R. A. Overview of Atomic Layer Etching in the Semiconductor Industry. J. Vac. Sci. Technol., A 2015 , 33 , 020802.
- (12) Lee, Y.; DuMont, J. W.; George, S. M. Atomic Layer Etching of AlF3 Using Sequential, Self-Limiting Thermal Reactions with Sn(acac)2 and Hydrogen Fluoride. J. Phys. Chem. C 2015 , 119 , 25385 -25393.
- (13) Faraz, T.; Roozeboom, F.; Knoops, H. C. M.; Kessels, W. M. M. Atomic Layer Etching: What Can We Learn from Atomic Layer Deposition? ECS J. Solid State Sci. Technol. 2015 , 4 , N5023 -N5032.
- (14) Oehrlein, G. S.; Metzler, D.; Li, C. Atomic Layer Etching at the Tipping Point: An Overview. ECS J. Solid State Sci. Technol. 2015 , 4 , N5041 -N5053.
- (15) Carver, C. T.; Plombon, J. J.; Romero, P. E.; Suri, S.; Tronic, T. A.; Turkot, R. B. J. Atomic Layer Etching: An Industry Perspective. ECS J. Solid State Sci. Technol. 2015 , 4 , N5005 -N5009.
- (16) Honda, M.; Katsunuma, T.; Tabata, M.; Tsuji, A.; Oishi, T.; Hisamatsu, T.; Ogawa, S.; Kihara, Y. Benefits of Atomic-Level Processing by Quasi-ALE and ALD Technique. J. Phys. D: Appl. Phys. 2017 , 50 , 234002.
- (17) Lee, C. G. N.; Kanarik, K. J.; Gottscho, R. A. The Grand Challenges of Plasma Etching: A Manufacturing Perspective. J. Phys. D: Appl. Phys. 2014 , 47 , 273001.
- (18) Shinoda, K.; Miyoshi, N.; Kobayashi, H.; Kurihara, M.; Izawa, M.; Ishikawa, K.; Hori, M. (Invited) Thermal Cyclic Atomic-Level Etching of Nitride Films: A Novel Way for Atomic-Scale Nanofabrication. ECS Trans. 2017 , 80 , 3 -14.
- (19) Khan, S. A.; Suyatin, D. B.; Sundqvist, J.; Graczyk, M.; Junige, M.; Kauppinen, C.; Kvennefors, A.; Huffman, M.; Maximov, I. HighDefinition Nanoimprint Stamp Fabrication by Atomic Layer Etching. ACS Appl. Nano Mater. 2018 , 1 , 2476 -2482.
- (20) Shinoda, K.; Miyoshi, N.; Kobayashi, H.; Miura, M.; Kurihara, M.; Maeda, K.; Negishi, N.; Sonoda, Y.; Tanaka, M.; Yasui, N.; Izawa, M.; Ishii, Y.; Okuma, K.; Saldana, T.; Manos, J.; Ishikawa, K.; Hori, M. Selective Atomic-Level Etching Using Two Heating Procedures, Infrared Irradiation and Ion Bombardment, for next-Generation Semiconductor Device Manufacturing. J. Phys. D: Appl. Phys. 2017 , 50 , 194001.
- (21) Lord, A. M.; Ramasse, Q. M.; Kepaptsoglou, D. M.; Evans, J. E.; Davies, P. R.; Ward, M. B.; Wilks, S. P. Modifying the Interface Edge to Control the Electrical Transport Properties of Nanocontacts to Nanowires. Nano Lett. 2017 , 17 , 687 -694.
- (22) Lieberman, M. A.; Lichtenberg, A. J. Principles of Plasma Discharges and Materials Processing; II ; John Wiley &amp; Sons: Hoboken, New Jersey, USA, 2005.
- (23) Jhon, Y. I.; Min, K. S.; Yeom, G. Y.; Jhon, Y. M. Understanding Time-Resolved Processes in Atomic-Layer Etching of Ultra-Thin Al2 O3 Film Using BCl3 and Ar Neutral Beam. Appl. Phys. Lett. 2014 , 105 , 093104.
- (24) Park, S. D.; Oh, C. K.; Bae, J. W.; Yeom, G. Y.; Kim, T. W.; Song, J. I.; Jang, J. H. Atomic Layer Etching of InP Using a Low Angle

Forward Reflected Ne Neutral Beam. Appl. Phys. Lett. 2006 , 89 , 043109.

- (25) Lee, Y.; DuMont, J. W.; George, S. M. Trimethylaluminum as the Metal Precursor for the Atomic Layer Etching of Al2O3 Using Sequential, Self-Limiting Thermal Reactions. Chem. Mater. 2016 , 28 , 2994 -3003.
- (26) Lee, Y.; DuMont, J. W.; George, S. M. Atomic Layer Etching of HfO2 Using Sequential, Self-Limiting Thermal Reactions with Sn(acac)2 and HF. ECS J. Solid State Sci. Technol. 2015 , 4 , N5013 -N5022.
- (27) Zywotko, D. R.; George, S. M. Thermal Atomic Layer Etching of ZnO by a ' Conversion-Etch ' Mechanism Using Sequential Exposures of Hydrogen Fluoride and Trimethylaluminum. Chem. Mater. 2017 , 29 , 1183 -1191.
- (28) Johnson, N. R.; Sun, H.; Sharma, K.; George, S. M. Thermal Atomic Layer Etching of Crystalline Aluminum Nitride Using Sequential, Self-Limiting Hydrogen Fluoride and Sn(acac) 2 Reactions and Enhancement by H2 and Ar Plasmas. J. Vac. Sci. Technol., A 2016 , 34 , 050603.
- (29) Sherpa, S. D.; Ventzek, P. L. G.; Ranjan, A. Quasiatomic Layer Etching of Silicon Nitride with Independent Control of Directionality and Selectivity. J. Vac. Sci. Technol., A 2017 , 35 , 05C310.
- (30) Miyoshi, N.; Kobayashi, H.; Shinoda, K.; Kurihara, M.; Watanabe, T.; Kouzuma, Y.; Yokogawa, K.; Sakai, S.; Izawa, M. Atomic Layer Etching of Silicon Nitride Using Infrared Annealing for Short Desorption Time of Ammonium Fluorosilicate. Jpn. J. Appl. Phys. 2017 , 56 , 06HB01.
- (31) Shinoda, K.; Izawa, M.; Kanekiyo, T.; Ishikawa, K.; Hori, M. Thermal Cyclic Etching of Silicon Nitride Using Formation and Desorption of Ammonium Fluorosilicate. Appl. Phys. Express 2016 , 9 , 106201.
- (32) Ikeda, K.; Imai, S.; Matsumura, M. Atomic Layer Etching of Germanium. Appl. Surf. Sci. 1997 , 112 , 87 -91.
- (33) Lee, Y.; DuMont, J. W.; George, S. M. Mechanism of Thermal Al2 O3 Atomic Layer Etching Using Sequential Reactions with Sn(acac)2 and HF. Chem. Mater. 2015 , 27 , 3648 -3657.
- (34) Chen, J. K.-C.; Altieri, N. D.; Kim, T.; Chen, E.; Lill, T.; Shen, M.; Chang, J. P. Directional etch of magnetic and noble metals. II. Organic chemical vapor etch. J. Vac. Sci. Technol., A 2017 , 35 , 05C305.
- (35) Chen, J. K.-C.; Altieri, N. D.; Kim, T.; Chen, E.; Lill, T.; Shen, M.; Chang, J. P. Directional Etch of Magnetic and Noble Metals. II. Organic Chemical Vapor Etch. J. Vac. Sci. Technol., A 2017 , 35 , 05C305.
- (36) Nigg, H. L.; Ford, L. P.; Masel, R. I. Surface-mediated reaction pathways of 2,4-pentanedione on clean and oxygen covered Cu (210). J. Vac. Sci. Technol., A 1998 , 16 , 3064 -3067.
- (37) Kytokivi, A.; Rautiainen, A.; Root, A. Reaction of acetylacetone ̈ vapour with [gamma ]-alumina. J. Chem. Soc. Faraday. Trans. 1997 , 93 , 4079 -4084.
- (38) George, M. A.; Hess, D. W.; Beck, S. E.; Young, K. M.; Roberts, D. A.; Vrtis, R.; Voloshin, G.; Bohling, D. A.; Lane, A. P. Reaction of 1,1,1,5,5,5-Hexafluoro-2,4-Pentanedione (H hfac) with Iron and Iron + Oxide Thin Films. J. Electrochem. Soc. 1996 , 143 , 3257 -3266.
- (39) Jain, A.; Kodas, T. T.; Hampden-Smith, M. J. Thermal DryEtching of Copper Using Hydrogen Peroxide and Hexafluoroacetylacetone. Thin Solid Films 1995 , 269 , 51 -56.
- (40) Hauge, H. I. T.; Conesa-Boj, S.; Verheijen, M. A.; Koelling, S.; Bakkers, E. P. A. M. Single-Crystalline Hexagonal Silicon-Germanium. Nano Lett. 2017 , 17 , 85 -90.
- (41) Https://imagej.nih.gov/ij/.
- (42) Mameli, A.; Merkx, M. J. M.; Karasulu, B.; Roozeboom, F.; Kessels, W. E. M. M.; Mackus, A. J. M. Area-Selective Atomic Layer Deposition of SiO2 Using Acetylacetone as a Chemoselective Inhibitor in an ABC-Type Cycle. ACS Nano 2017 , 11 , 9303 -9311.
- (43) Pecz, B.; Baji, Z.; Labadi, Z.; Kovacs, A. ZnO Layers Deposited ́ ́ ́ by Atomic Layer Deposition. Journal of Physics: Conference Series in 18th Microscopy of Semiconducting Materials Conference (MSM XVIII) , 2013; Vol. 471 , p 12015.
- (44) Profijt, H. B.; Kudlacek, P.; van de Sanden, M. C. M.; Kessels, W. M. M. Ion and Photon Surface Interaction during Remote Plasma ALD of Metal Oxides. J. Electrochem. Soc. 2011 , 158 , G88 -G91.
- (45) National Institute of Standards and Technology. NIST Webbook. In Chemistry WebBook, NIST Standard Reference Database Number 69 ; Linstrom, P. J., Mallard, W. G., Eds.; National Institute of Standards and Technology: Gaithersburg MD, 20899.
- (46) Tayyari, S. F.; Milani-nejad, F. Vibrational Assignment of Acetylacetone. Spectrochim. Acta, Part A 2000 , 56 , 2679 -2691.
- (47) Niven, M. L.; Thornton, D. A. Band Assignment in the Infrared Spectrum of Zinc Acetylacetonate Monohydrate by 18 O, 68 Zn and 64 Zn-Labelling. Spectrosc. Lett. 1980 , 13 , 419 -425.
- (48) Helms, A. B.; Burgess, J. S.; Street, S. C. Surface Studies of 2,4Pentanedione on γ -Al O3/NiAl (100) and NiAl (100). 2 Surf. Sci. 2009 , 603 , 3262 -3266.
- (49) Lee, Y.; George, S. M. Atomic Layer Etching of Al2O3 Using Sequential, Self-Limiting Thermal Reactions with Sn(acac)2. ACS Nano 2015 , 9 , 2061 -2070.
- (50) Lee, Y.; Huffman, C.; George, S. M. Selectivity in Thermal Atomic Layer Etching Using Sequential, Self-Limiting Fluorination and Ligand-Exchange Reactions. Chem. Mater. 2016 , 28 , 7657 -7665. (51) DuMont, J. W.; Marquardt, A. E.; Cano, A. M.; George, S. M. Thermal Atomic Layer Etching of SiO2 by a ' Conversion-Etch ' Mechanism Using Sequential Reactions of Trimethylaluminum and Hydrogen Fluoride. ACS Appl. Mater. Interfaces 2017 , 9 , 10296 -10307.