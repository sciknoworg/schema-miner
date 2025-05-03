<!-- image -->

## RESEARCH ARTICLE |  JANUARY 30 2024

## Atomic layer etching of indium tin oxide

Special Collection: Atomic Layer Etching (ALE)

Christoffer Kauppinen



<!-- image -->

<!-- image -->

Check for updates

J. Vac. Sci. Technol. A

42, 022601 (2024)

https://doi.org/10.1116/6.0003170

## Articles You May Be Interested In

Focused ion beam direct patterning of hardmask layers

J. Vac. Sci. Technol. B (July 2014)

Correlation between optical emission spectroscopy of hydrogen/germane plasma and the Raman crystallinity factor of germanium layers

Appl. Phys. Lett. (April 2013)

Thermal recrystallization of short-range ordered WS 2  films

- J. Vac. Sci. Technol. A (July 2018)

<!-- image -->

<!-- image -->

 

<!-- image -->

<!-- image -->

<!-- image -->

## Atomic layer etching of indium tin oxide

Cite as: J. Vac. Sci. Technol. A 42 , 022601 (2024); doi: 10.1116/6.0003170 Submitted: 25 September 2023 · Accepted: 26 December 2023 · Published Online: 30 January 2024

Christoffer Kauppinen a)

<!-- image -->

## AFFILIATIONS

Quantum photonics research team, VTT Technical Research Centre of Finland Ltd, Tietotie 3, Espoo FI-02044 VTT, Finland

Note: This paper is part of the 2024 Special Topic Collection on Atomic Layer Etching (ALE).

a) Author to whom correspondence should be addressed: christoffer.kauppinen@vtt.fi

## ABSTRACT

This work presents the atomic layer etching (ALE) process for sputtered indium tin oxide (ITO) thin films using thermal surface modification with BCl3 and modified surface removal by low ion energy Ar plasma. In this approach, an elevated temperature is required for high synergy ALE due to the low volatility of indium chlorides, and 150 C is proved to be suitable. An etch per cycle (EPC) of 1.1 Å and ALE /C14 synergy of 82% was achieved. Both surface modification and modified surface removal steps exhibited self-limited EPC. The ALE process was developed in a conventional reactive ion etching tool and retains the thin film absolute uniformity on the wafer. ITO was photolithographically patterned on whole wafers using photoresist as an etch mask for the ALE, and clear smoothing of the unmasked areas is observed, which is a characteristic of an ideal ALE process. This confirms that the developed ALE process can be utilized to pattern ITO using conventional photolithography. The demonstrated ITO ALE can be used to fabricate, for example, thin channel or recessed channel transistors, with self-smoothened channels for reduced surface scattering.

Published under an exclusive license by the AVS. https://doi.org/10.1116/6.0003170

## I. INTRODUCTION

Indium tin oxide (ITO) is a degenerate n-type semiconductor with a wide bandgap, 1 making it widely used as a transparent conducting oxide in various applications, such as displays 2 and solar cells, 3 but has not been widely used as an active material in logic applications like transistors. Lately, oxide semiconductors are being studied as emerging materials for back-end-of-line (BEOL) compatible transistors for monolithic 3D integration on complementary metal-oxide-semiconductor (CMOS) logic. 4 Controlling lateral doping, like in Si transistors used in CMOS, is challenging in oxide semiconductors. Even having p-type doping is a challenge as the oxide semiconductors are typically n-type not to even speak of having lateral anisotype homojunctions like in conventional Si CMOS. For these reasons, the high-off state resistance in oxide transistors is commonly provided with a very thin layer of semiconductor forming the channel. The channel is fabricated then either by depositing a thin layer of semiconductor or having a recessed channel where the channel has been thinned down via etching. Examples of oxide transistors having high ( . 10 6 ) on/off ratios stemming from the thin channel semiconductors are thin ( /C25 4 0 : -10 nm) channel ITO transistors where the sputtering rate and uniformity are painstakingly finely controlled, 5 atomic layer deposition (ALD) 6 indium oxide channel transistors with very thin

( /C25 1 0 : -3.5 nm) channels 7 (enabled naturally by ALD), and ITO transistors with ultra-thin ( /C25 1 0 : -2.0 nm) recessed channels wet etched with a dilute acid solution. 8

While ALD can naturally control the channel thickness quite ideally, the throughput of ALD is inferior to sputtering, and having a recessed channel has been demonstrated to achieve low contact resistivity merely by having a thicker semiconductor layer as the source and drain regions. 8 Therefore, etching a channel recess has some benefits over depositing an ultra-thin channel material. Thus, etching the channel recess is critical for oxide semiconductors in 3D monolithic CMOS integration. Wet etching the channel recess by dilute acid has been demonstrated, 8 but this is undoubtedly difficult to control due to nm -scale s etch rate 8 and isotropic etch profiles typical in wet etching, 9 which cause unwanted undercut. In addition, while the dilution slows the etch process, it is not selflimited and can still be highly dependent on pattern density due to differences in local density of reactants/reaction products, also known as the loading effect. A digital etch has been demonstrated for amorphous indium gallium zinc oxide (IGZO) nanowire field-effect transistors using sequential BCl3 plasma treatment and isopropanol rinse to remove the chloride layer, 10,11 but naturally, a true dry process would be preferred as the described process is extremely slow and mandates taking into account the unavoidable undercut due to the wet etch isotropicity.

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

Atomic layer etching (ALE) 13 is ideally suited to controllably etch semiconductor materials layer by layer with a self-limited etch rate, giving simple control of the channel recess thickness. ALE is a technique where a material is removed layer by layer using sequential self-limiting reactions, usually two sequential gas-solid reactions (Reaction A and Reaction B) with purges (Purge A and Purge B) in between, 13 where typically, Reaction A is the surface modification step and Reaction B is the modified surface removal step.

ALE processes have been developed for a multitude of oxide materials like insulating oxides, e.g. , alumina (Al2O3), 14 silica (SiO2), 15 zirconia (ZrO2), 16 and hafnia (HfO2), 17 as well as for semiconducting oxides, e.g., titania (TiO2), 18 zinc oxide (ZnO) 19,20 and gallium oxide (Ga2O3), 21 but for ITO there is no reported ALE process. For etching, the channel recess for high performance ITO transistors, an anisotropic ALE process is highly desired, thus the BCl3 surface modification and anisotropic modified surface removal, that is popular in oxide ALE, 14,16 -18 is a tempting starting point.

In this work, an ALE process for sputtered ITO thin films is studied using thermal surface modification with BCl3 and modified surface removal by low ion energy Ar plasma in a conventional reactive-ion etching (RIE) system. This is the first published oxide ALE using BCl3 and Ar ions, as previous works used an Ar neutral beam in their studies. 14,16 -18

## II. EXPERIMENT

First, ITO thin films were fabricated for ALE studies. ITO was sputtered onto 4 in. Si wafers from an ITO target (from Testbourne) with a composition of 90 wt% In2O3 and 10 wt% SnO2 with a purity of 99.99%, using RF sputtering at 400 W in a VonArdenne CS 730 S cluster system sputtering tool. For the ALE tests, the sputtered films had over 100 nm thickness measured by ellipsometry.

The ALE experiments were conducted in an Oxford Instruments PlasmalabSystem 100, a conventional inductively coupled plasma (ICP) reactive ion etching (RIE) tool, though the ICP function was not used, so the system was used essentially in a capacitively coupled plasma RIE configuration. To clarify the system is a conventional dry etch tool and not a dedicated ALE tool. The author used the same system for GaN ALE studies previously, 22 and the same model has been used in various ALE studies. 23 -25 The tool handles one wafer at a time, and, before the ALE process begins, the wafer is first vacuumed in a load-lock below p ¼ 4 /C2 10 /C0 2 Torr, then inserted in the main chamber, where the wafer is pumped to vacuum that is lower than p ¼ 9 /C2 10 /C0 5 Torr. The ALE process is schematically shown in Fig. 1. In Reaction A, the BCl3 reacts with the surface forming surface metal chlorides and boron oxychlorides (BOCl). BCl3 gas is known to efficiently bind with surface oxygen and to form stable volatile boron oxychlorides, 26 which is commonly exploited when dry etching oxide materials or surface deoxidation in dry etching. 26 BCl3 has been used as the surface modification step in realizing oxide ALE, 14,16 -18 as the BCl3 gas can react with oxides to form volatile boron oxychlorides. 26 In Purge A, the excess, unreacted BCl3 is purged out. Then, in Reaction B, the modified surface is removed with low energy Ar ions. The Ar ions provide energy to volatilize the tin and indium surface chlorides on the surface. The oxygen is removed as boron oxychlorides like BOCl, 17,26 which is known to be volatile. The thermal energy also contributes in removing the modified surface, and two temperatures: room temperature 22 C and 150 C were used in the end for ALE experi/C14 /C14 ments. Finally, in Purge B, the reaction products are removed and the cycle can start again. He backing was used to keep the wafers at the set (platen) temperature. Thermal surface modification with BCl3 was chosen over plasma modification due to the simplicity of thermal surface modification. Although plasma modification can be faster than thermal due to enhanced plasma reactivity, there are less parameters to optimize in thermal surface modification, namely, no plasma inductively couple power nor RF power at all in Reaction A. An additional issue with plasma surface modification using BCl3 is the formation of chemically passivating BCl x polymers, that the low energy Ar ions in Reaction B would have to punch through. 26 Thus, if plasma modification using BCl3 would be used it might necessitate using higher ion energies due to polymer formation, which could lower the synergy.

The etch per cycle (EPC) was monitored ex situ with a He -Ne laser ellipsometer (Philips Plasmos SD-2300). 30 points from each wafer was measured at 70 /C14 angle of incidence before and after each ALE run. EPC was calculated from the change of the average thickness divided by the number of cycles, and ALE effect on uniformity was obtained from the average, and standard deviation, of the thin film thickness.

Atomic force microscopy (AFM) was used to study resulting topography and roughness. An Oxford Instruments model Jupiter XR AFM tool was used in tapping mode for this purpose. For this study, ITO was sputtered onto 6 in. wafers and patterned using standard photolithography using AZ5214E photoresist (from Microchemicals). The ITO was then etched using the ALE process, after which the photoresist was removed using acetone. Acetone was then rinsed first in isopropanol and de-ionized water. Finally, photoresist residues were removed using O2 plasma stripping in a PRS900 plasma stripper (Oxford Instruments) to have a clean surface for the AFM.

The Gwyddion software was used in analyzing the AFM data. 27 The VESTA 3 software 12 was used to visualize and draw the crystals, atoms, and molecules in Fig. 1.

## III. RESULTS AND DISCUSSION

Initially, ITO ALE at room temperature was investigated. The parameters are similar to the ones discussed later (see Fig. 1 for the parameters) except that room temperature was used and the required RF powers were much higher. The room temperature ALE process uses thermal surface modification with BCl3 (Reaction A), and modified surface removal with Ar ions (Reaction B), with corresponding Ar purges in between. The room temperature ALE resulted in a very low etch per cycle (EPC) of EPC = 0.47 Å when using RF = 50 W (DC bias /C25 /C0 25 V). See supplementary material 28 for Fig. S1 for the saturation curve of Reaction B at room temperature. This room temperature ITO ALE process was then tested for synergy using the conventional definition S ¼ ALE /C0 ( α þ β ) ALE /C2 100 % where ALE is the ALE EPC, α is the EPC for just Reaction A and β is the EPC for just Reaction B. 29 See

14 April 2025 12:42:33

<!-- image -->

FIG. 1. Atomic layer etching process for ITO. Final developed process parameters below each step schematic. In Reaction A, the BCl3 pulse modifies the surface. Surface metal atoms are chlorinated and surface oxygen forms boron oxychlorides with the reactant. Purge A is an argon purge that removes excess unreacted BCl3 from the chamber. Reaction B is the modified surface removal step. A low ion energy Ar ion bombardment gives enough energy to volatilize and remove metal chlorides and the surface boron oxychlorides. Purge B removes reaction products with argon. Oxygen in black, argon in red, boron in yellow, chlorine in green, indium in purple, and tin in blue. VESTA 3 was used in drawing the images. 12

<!-- image -->

supplementary material 28 for Fig. S2 for the synergy test at room temperature. For this, runs with only Reaction A followed by purges were done as well as runs with only Reaction B followed by purges and naturally the whole sequence (Reaction A, Purge A, Reaction B, Purge B). 100 cycles of BCl3 exposure (Reaction A) followed by Ar purges (Purge A) did not etch the surface but according to ellipsometry increased the thickness by 3 Å. This could be the added thickness due to BCl3 chemisorption as the van der Walls diameter of a Cl atom is roughly 3.5 Å. 30 The individual Ar ion step (Reaction B) followed by an Ar purge (Purge B) gave an EPC = 1.26 Å, which has a higher EPC than the combined ALE process. So, in fact, at room temperature, BCl3 actually lowers ITO ALE EPC. This is very likely due to the low volatility of indium chlorides, which have high boiling points. 30 As for the synergy parameter, 29 the higher etch rate with only Reaction B and only Reaction A giving essentially zero EPC compared to the combined ALE cycle (Reaction A+B) gives a synergy parameter of S ¼ 0 47 Å : /C0 ( /C0 0 03 Å : þ 1 26 Å) : 0 47 Å : /C2 100 % /C25 /C0 163 % . To the best of the author s knowledge, this is the first reported ' negative synergy parameter. It is not entirely impossible to imagine an ALE process where the surface modification step (Reaction A) is pulsing one chemical to inhibit the etch rate in Reaction B (Ar milling or other step) to obtain self-limited layer-by-layer ALE. However, in the context of this work, where argon ions are used in Reaction B, the milling without BCl3 pulsing is so aggressive that there is a risk of damage ITO. Then, the desired application, recessed transistor channels, would surely be impacted detrimentally, for example, by reduced mobility due to damage in the polycrystalline material. The room temperature experiments proved to be unfruitful, but the results are in supplementary material 28 for the enthusiastic reader. Figure S1 28 shows the saturation curve for Reaction B at room temperature, where no self-limiting EPC is seen. Figure S2 28 shows the room temperature ALE synergy test with the described negative synergy parameter.

To combat the low volatility of the indium chlorides, the temperature of the ALE process was increased to 150 /C14 C and this temperature was used in all following experiments and data points. This temperature of 150 /C14 C was chosen as typically when InP is dry etched using Cl2 plasma an elevated temperature, between 150 and 180 C, /C14 31 is needed due to the low volatilities of indium chlorides. The elevated temperature enhanced the EPC, as can be seen in the energy scan in Fig. 2(a). Figure 2(a) shows the ALE EPC (red

FIG. 2. (a) Energy scan and (b) synergy scan of the ITO ALE process at 150 /C14 C. Error bars in (a) and (b) show standard deviation from the mean, when multiple measurements are done with the same parameters.

<!-- image -->

<!-- image -->

crosses) and the Ar milling EPC (black squares) as a function of the RF power. The Ar milling (Reaction B) process is just the ALE process with BCl3 surface modification (Reaction A) removed. The Ar milling only data are presented here to asses when the Ar ions might start to appreciably mill or damage the ITO and to visually show the etch synergy. The resulting DC bias from the RF power is shown on the top axis. The DC bias accelerates the Ar ions during Reaction B and thus determines the ion energy. Figure 2(a) shows that now at 150 C the EPC is higher at 10 W plasma power than /C14 with 50 W at room temperature, a clear indication that the temperature was initially too low for efficient desorption of the indium chlorides. Furthermore, the ALE EPC seems to plateau after 20 W indicating that the ALE energy window could be 20 -30 W. However, the Ar milling EPC starts to rise appreciably after 15 W, and a more careful analysis is warranted.

Figure 2(b) presents the synergy scan that is the synergy parameter as a function of the plasma power. For the synergy scan, energy scan data were used together with a measurement of Reaction A only to calculate the synergy parameter 29 as a function of the plasma power. The shapes and behavior of both the energy scan (which does not extend to the unwanted sputtering regime) and synergy scan are very similar to other ALE work. 29 Figure 2(b) shows both 15 W and 20 W ALE processes to have good synergies of 82% and 78%, respectfully, but drops below 60% for 30 W. Clearly using only the energy scan, see Fig. 2(a), alone to determine the ALE energy window is not practical. It is then determined here that the practical ALE energy window to lay here roughly between 15 and 20 W as in this region (1) the EPC has roughly saturated to an appreciable level, (2) the parasitic milling is low, and (3) the synergy is high. The following discussion will revolve around characterizing the 15 W plasma power ITO ALE process at 150 C. /C14

Figure 3(a) shows the synergy test for the ITO ALE process at 15 W. In the synergy test, the ALE cycle was run with both reactions (Reaction A+B) with purges in between, and with the individual Reactions A or B (with purges in between) whose EPC is marked respectfully α and β . Ideally, the individual reactions do not etch the ITO. The EPC was measured for each bar from 100 cycles and measured with ellipsometry as described earlier. Both Reaction A and Reaction B remove a small amount of material. The BCl3 surface modification in Reaction A has an EPC of α ¼ 0 09 Å. Then, apparently at the elevated temperature of 150 C : /C14 Reaction A can remove material from the surface but extremely slowly. Interestingly the boiling point of SnCl4 30 is below the used process temperature, so it is possible that in the absence of ion bombardment that BCl3 first attacks tin on the surface and thus enables further, albeit slow, attack to the surface indium and oxygen. Reaction B s ' milling has an EPC of β ¼ 0 11 Å. : A small but measurable milling rate like this is expected. The combined ALE cycle of Reaction A+B has an average EPC = 1.10 Å. Thus, the combined Reaction A and B into the ALE cycle gives a much higher EPC than the individual reactions, indicating high synergy. The ALE EPC = 1.10 Å is in line with other oxide ALE EPCs using BCl3 and argon removal, where the EPCs are roughly around 1 Å. 14,16 -18 Here Ar ions are for the first time used for modified surface removal in combination with BCl3 surface modification for oxide ALE instead of energetic Ar neutrals that have been used in many pioneering oxide ALE studies with BCl3. 14,16 -18 Ar ions are commonly available in RIE tools and often used in many ALE studies for Reaction B. 22,24,25,29 The synergy parameter value of S = 82% is very high and indicates a quite ideal ALE process.

Figure 3(b) shows the etch depth and EPC of the ITO ALE process as a function of the number of cycles. The EPC seems to be nearly constant and, therefore, does not depend on the number cycles as expected for a quite ideal ALE process, see Fig. 3(a). Therefore, the etch depth naturally increases fairly linearly, which is typical for ALE processes. 13

Figure 3(c) presents the saturation curve for Reaction A. The EPC seems to be at least quasi-self-limiting if not totally selflimiting. There seems to be a gentle upward slope when increasing the BCl3 exposure time. This is not surprising when looking at the

14 April 2025 12:42:33

<!-- image -->

FIG. 3. (a) Synergy test for the chosen ITO ALE parameters. For parameters, see Fig. 1. Synergy parameter, ALE EPC, and the individual reaction EPCs, α , for Reaction A and β for Reaction B, are displayed in the graph. (b) ALE EPC (crosses) and etch depth (circles) as a function of the number of cycles. The lines are linear fits. The EPC line fit is nearly parallel. (c) Saturation curve for Reaction A. The BCl3 exposure time is varied. Other parameters are constant. (d) Saturation curve for Reaction B. The ALE EPC and Ar milling only EPC as a function of the Ar plasma exposure time are shown. Other parameters constant. Error bars in (b) -(d) show standard deviation from the mean, when multiple measurements are done with the same parameters.

<!-- image -->

synergy test in Fig. 3(a). At the used elevated temperature of 150 /C14 C the BCl3 seems to slightly attack the surface ( α ¼ 0 09 Å). The very : small slope could probably be mitigated to perfect self-saturation by reducing temperature as at room temperature BCl3 alone did not cause etching, but this is not worth the effort as lowering temperature from 150 C would likely strongly decrease the overall /C14 ALE EPC and the synergy due to the low volatility of the indium chlorides. The chosen time of 20 s for surface modification (Reaction A) saturates the EPC well. Furthermore, the long reactant pulse choice most likely enables also surface modification not only on planar ITO surfaces where the gas easily reaches, but also into narrow photoresist openings. Finally, the saturation behavior in Fig. 3(c) is a clear sign that the BCl3 contributing to ALE is chemisorbed to the surface instead of physisorbed. 6 The EPC is selflimiting even when the BCl3 dose is increased from 5 to 20 s so the BCl3 contributing to ALE has to be chemisorbed to a layer of self-limited thickness. 6 As physisorbtion is always reversible the very long 20 s Purge A would remove physisorbed BCl3 from the surface, 6 the removal of which would induce a large change in EPC, especially at low doses, if the BCl3 contributing to the ALE would be physisorbed. Some BCl3 can be physisorbed but the Purge A seems to be long enough that extra BCl3 is removed and only the chemisorbed reactant contributes to ALE.

Figure 3(d) present the saturation curve for Reaction B, the modified surface removal step using Ar ions. The ITO ALE EPC is plotted as a function of the Ar plasma step time (red crosses). There seems to be an initial lag time of roughly 2 s before the EPC starts to aggressively rise, as it does between 5 and 8 s of Ar plasma exposure. The lag time can be attributed to the finite ignition time of the plasma. After ignition, the Ar ions hitting the ITO surface start removing the volatile compounds, and the EPC saturates to a near constant value after 8 s. The ALE process window is clearly the plateau from 8 to 15 s where the EPC is nearly constant with a very small increase in EPC due to Ar ion milling. However, after

14 April 2025 12:42:33

<!-- image -->

15 s there is a nonliner increase in the EPC. Similar behavior related to prolonged ion removal step in ALE causing a nonlinear increase in EPC has been found in other works. 32,33 As the behavior is only apparent at long ion bombardment times in Reaction B, then the heat accrued during the step might lead to enhanced milling at the ITO top surface. For this reason, Fig. 3(d) also shows the Ar milling only (Reaction B only) EPC as a function of the step time (black squares). Clearly, Ar milling has linear EPC as a function of the ion dose. Therefore, the nonlinear increase in EPC when the ion dose is increased is not related to heat but is unfortunately connected somehow to the surface modification step Reaction A. The increase might be due to the prolonged Ar milling creating a more reactive surface, for example, by amorphizing the surface with increasing dose or increasing the reactive surface area in the ångströmscale. However, when the ion dose is kept moderate, 8 -15 s, the EPC shows good self-saturation.

The thin film uniformity is of vital importance in semiconductor technology processes and, especially, when discussing accurate dry etching processes like the ångström-scale accuracy of the ITO ALE. Table I shows the uniformity data of the samples in Fig. 3(b), which are all with same ALE process parameters but with varying cycles. As is the standard in ALD and ALE literature when discussing uniformity the nonuniformity metrics (lower is better) are used. In Table I, both the absolute nonuniformity or standard deviation ( σ ) and relative nonuniformity (CV) are given. For the relative nonuniformity, the coefficient of variation (standard deviation divided by the average thickness hence the acronym CV) is used as a metric instead of the often used max-min divided by average as with 30 measurement points the σ describes the film better than the max-min. The change in uniformity after ALE is the most interesting information in Table I. What jumps out from the data is that for every sample the absolute uniformity is slightly better ( σ decreases). If the ALE would only retain the absolute uniformity one would expect that by process variability alone that Δ σ would have both small negative and positive values. The dataset in Table I is not large enough for proper statistical analysis (the ALE treatments are with varying cycles with maximum 2 point with the exact same treatment) but what can be said even from this data is that the absolute uniformity does not degrade, that is, the absolute uniformity is either retained or improved. The relative uniformity

TABLE I. ALE effect on ITO thin film thickness nonuniformity. Thickness nonuniformity is characterized on the wafer level as absolute nonuniformity (standard deviation, σ ) and as relative nonuniformity (coefficient of variation or standard deviation divided by average, CV) in percentage.

|            | Before   | Before   | After   | After   | Change   | Change      |
|------------|----------|----------|---------|---------|----------|-------------|
| ALE        | σ (Å)    | CV (%)   | σ (Å)   | CV (%)  | Δ σ (Å)  | Δ CV (%pt.) |
| 50 cycles  | 36.5     | 3        | 33.5    | 3       | - 3.0    | 0           |
| 50 cycles  | 33.5     | 6        | 33.2    | 6       | - 0.3    | 0           |
| 100 cycles | 41.9     | 4        | 41.6    | 5       | - 0.3    | 1           |
| 100 cycles | 33.2     | 6        | 30.0    | 7       | - 3.3    | 1           |
| 150 cycles | 34.1     | 3        | 29.1    | 3       | - 5.1    | 0           |
| 200 cycles | 24.3     | 4        | 23.4    | 6       | - 0.9    | 2           |
| 200 cycles | 32.1     | 3        | 30.0    | 3       | - 2.1    | 0           |

on the other hand seems to degrade a bit especially with longer cycle numbers. This is hardly surprising as if the surface features would be perfectly retained and the film would be just thinned, then the relative nonuniformity would naturally increase even in this scenario. From Table I, the ITO ALE etch nonuniformity (ALE effect on relative nonuniformity or Δ CV) is then 2%pt. in the worst case. Overall, the developed ITO ALE process shows excellent properties as the absolute uniformity is at least retained if not improved. Only very few works 34,35 report the ALE effect on uniformity, and if ALE processes are going to be widely adopted there is a need to report uniformity in a standardized fashion and the absolute nonuniformity σ and relative nonuniformity CV are natural candidates.

Figure 4 shows an AFM scan of a grating photolithographically patterned on ITO using the ALE process. The ITO grating has 1 μ m lines with 3 μ m period. Conventional photoresist (AZ5241E, from Microchemicals) was photolithographically patterned on ITO and then used as a soft mask for the ALE, see Experiment section for details. 100 cycles using 20 W RF power was used for the ALE.

FIG. 4. AFM micrograph of a photolithographically patterned ITO grating using ALE. The ITO grating has 1 μ m lines with 3 μ m period. Conventional photoresist was used as an etch mask. The etched areas are visibly smoother than unetched areas. 100 cycles using 20 W RF power was used. (a) shows the 3D view and (b) shows the conventional 2D AFM measurement of the same region. The scan area was 10 /C2 10 μ m.

<!-- image -->

<!-- image -->

<!-- image -->

Figure 4(a) shows the 3D map of the topography, and Fig. 4(b) shows the 2D map of the topography of the grating. The etched stripes in Fig. 4(a) are clearly smoother when looking at the 3D graph, and overall, the ALE seems to produce nice clean and anisotropic etch profiles. Anisotropicity is much valued in dry etch processes for high resolution photolithography as it enables dense lines to be patterned without fear of undercut. Figure 4(b) shows the 2D topography of the grating, and the lines are well defined. Some shallow scratches are visible on the unetched surface.

From Fig. 4(b), the root mean square (RMS) areal surface roughness can be calculated. The etched areas have a surface roughness of 0.49 nm while the unetched areas have a surface roughness of 0.99 nm. Thus, the developed ALE has a smoothing effect on the etched ITO surface. The 100 cycles reduced surface roughness by 51% and a deeper etch would probably reduce this even more. This dramatic roughness reduction is not entirely unexpected, as high synergy ALE processes are expected to show the ALE smoothing effect, 34 and the developed ITO ALE showed a very high synergy of 82%. The ALE smoothing effect is well known 34 and manifests also in anisotropic ALE processes and is one of the emerging key benefits of dry etching with ALE. 34 Smoothing of the etched surface is highly desirable when patterning transistor channels as surface roughness causes extra surface scattering, which reduces carrier mobility. A self-smoothing dry etch process brings either extra flexibility or speed to nanofabrication processes, as initially rougher films can be used in nanofabrication to make smooth channels, or processing steps can be reduced for thin films, as there is no need for an additional smoothing step after dry etching as roughness does not increase.

As the described ALE process worked on ITO, then it is reasonable to expect that it would also work on undoped indium oxide thin films with the exact same parameters as described here. The ALE on undoped indium oxide could have even higher synergy than the already high 82% for ITO as some Sn can be removed as SnCl4 just in Reaction A as the process temperature is over its boiling point. 30 BCl3 and Ar are widely available in many conventional dry etch tools and the author hopes that many ALE processes for oxide semiconductors are developed using this simple and widely available chemistry.

## IV. CONCLUSIONS

The ALE process for ITO was demonstrated using thermal surface modification with BCl3 and modified surface removal by low ion energy Ar plasma. An elevated temperature of 150 C was /C14 needed for high synergy ALE, which resulted in a synergy parameter of 82%. Room temperature ALE of ITO with the described chemistry proved to have a negative synergy parameter and was deemed unsuccessful for the ITO ALE application. The 150 C ALE /C14 ITO process gave self-limited EPC for both the surface modification and modified surface removal step. The ALE EPC = 1.1 Å is comparable to other oxide ALE processes using BCl3. The developed ALE process did not increase the absolute nonuniformity of the thin film. The presented ITO ALE was used successfully to etch ITO gratings with a micrometer scale period using standard photolithography and conventional photoresist as an etch mask. This demonstrates the straightforward applicability of the ITO ALE process with soft masks. Self-smoothing by ALE was observed in the etched ITO surfaces, indicating a very ideal ALE process. Dry etch processes, like the demonstrated ITO ALE, that reduce surface roughness while keeping highly anisotropic or vertical sidewalls are extremely useful when patterning very small features. Furthermore, a conventional RIE system was used in the ALE enabling scalable adoption of the process without need for dedicated tools. The low processing temperature, retention of thin film uniformity, photolithographic patterning with standard photoresists as etch masks, anisotropic etch profile, combined with self-smoothing make this ITO ALE process suitable for fabricating recessed channel ITO transistors and other ITO components.

## ACKNOWLEDGMENTS

The author would like to thank Olli-Pekka Kilpi and Karl-Magnus Persson for interesting talks about ITO as a prospective material for ALE as well as for support. The author would also like to thank Kimmo Rutanen and Kristiina Rutanen for their technical help in sputtering the ITO. This work was partially supported by the European Union s Horizon 2020 research and innovation ' programme s MISEL Project (Grant No. 101016734). '

## AUTHOR DECLARATIONS

## Conflict of Interest

The authors have no conflicts to disclose.

## Author Contributions

Christoffer Kauppinen: Conceptualization (lead); Data curation (lead); Formal analysis (lead); Investigation (lead); Methodology (lead); Software (lead); Validation (lead); Visualization (lead); Writing -original draft (lead); Writing -review &amp; editing (lead).

## DATA AVAILABILITY

The data that support the findings of this study are available from the corresponding author upon reasonable request.

## REFERENCES

1 I. Hamberg, C. G. Granqvist, K.-F. Berggren, B. E. Sernelius, and L. Engström, Phys. Rev. B 30 , 3240 (1984).

- 3 S.-Y. Lien, Thin Solid Films 518 , S10 (2010).
- 2 J. Y. Kwon and J. K. Jeong, Semicond. Sci. Technol. 30 , 024002 (2015).
- 4 S. Datta, S. Dutta, B. Grisafe, J. Smith, S. Srinivasa, and H. Ye, IEEE Micro 39 , 8 (2019).
- 6 R. L. Puurunen, J. Appl. Phys. 97 , 121301 (2005).
- 5 S. Li, M. Tian, Q. Gao, M. Wang, T. Li, Q. Hu, X. Li, and Y. Wu, Nat. Mater. 18 , 1091 (2019).
- 7 M. Si, Z. Lin, Z. Chen, X. Sun, H. Wang, and P. D. Ye, Nat. Electron. 5 , 164 (2022).
- 9 S. Franssila, Introduction to Microfabrication , 2nd ed. (Wiley, Chichester, UK 2010).
- 8 M. Si, J. Andler, X. Lyu, C. Niu, S. Datta, R. Agrawal, and P. D. Ye, ACS Nano 14 , 11542 (2020).
- 10 K. Han, et al. , ' First demonstration of oxide semiconductor nanowire transistors: A novel digital etch technique, IGZO channel, nanowire width down to 20 nm, and ion exceeding 1300 μ A/ μ m, ' in 2021 Symposium on VLSI Technology , Kyoto, Japan, 13 -19 June 2021 (IEEE, Piscataway, NJ 2021), pp. 1 -2.

<!-- image -->

- 11 K. Han, et al. , IEEE Trans. Electron Devices 68 , 6610 (2021).
- 13 K. J. Kanarik, T. Lill, E. A. Hudson, S. Sriraman, S. Tan, J. Marks, V. Vahedi, and R. A. Gottscho, J. Vac. Sci. Technol. A 33 , 020802 (2015).
- 12 K. Momma and F. Izumi, J. Appl. Crystallogr. 44 , 1272 (2011).
- 14 K. Min, S. Kang, J. Kim, Y. Jhon, M. Jhon, and G. Yeom, Microelectron. Eng. 110 , 457 (2013).
- 16 W. Lim, J. Park, J. Park, B. Park, and G. Yeom, J. Nanosci. Nanotechnol. 9 , 7379 (2009).
- 15 D. Metzler, R. L. Bruce, S. Engelmann, E. A. Joseph, and G. S. Oehrlein, J. Vac. Sci. Technol. A 32 , 01B101 (2014).
- 17 S. Park, W. Lim, B. Park, H. Lee, J. Bae, and G. Yeom, Electrochem. Solid-State Lett. 11 , H71 (2008).
- 19 D. R. Zywotko and S. M. George, Chem. Mater. 29 , 1183 (2017).
- 18 J. B. Park, W. S. Lim, S. D. Park, B. J. Park, and G. Y. Yeom, J. Korean Phys. Soc. 54 , 976 (2009).
- 20 A. Mameli, M. A. Verheijen, A. J. Mackus, W. M. Kessels, and F. Roozeboom, ACS Appl. Mater. Interfaces 10 , 38588 (2018).
- 22
- 21 Y. Lee, N. R. Johnson, and S. M. George, Chem. Mater. 32 , 5937 (2020).
- C. Kauppinen, S. A. Khan, J. Sundqvist, D. B. Suyatin, S. Suihkonen, E. I. Kauppinen, and M. Sopanen, J. Vac. Sci. Technol. A 35 , 060603 (2017).
- 23 S. A. Khan, D. Suyatin, J. Sundqvist, M. Graczyk, M. Junige, C. Kauppinen, A. Kvennefors, M. Huffman, and I. Maximov, ACS Appl. Nano Mater. 1 , 2476 (2018).
- 24 V. Kuzmenko, Y. Lebedinskij, A. Miakonkikh, and K. Rudenko, Vacuum 207 , 111585 (2023).
- S. Dallorto, A. Goodyear, M. Cooke, J. E. Szornel, C. Ward, C. Kastl, A. Schwartzberg, I. W. Rangelow, and S. Cabrini, Plasma Process. Polym. 16 , 1900051 (2019).
- 25
- 26 A. Kobelev, N. Andrianov, Y. Barsukov, and A. Smirnov, ' Boron trichloride dry etching, ' in Encyclopedia of Plasma Technology-Two Volume Set (CRC, Boca Raton, 2016), pp. 193 -202.
- 28 See supplementary material online for the saturation curve of Reaction B at room temperature and for the synergy test at room temperature.
- 27 D. Ne as and P. Klapetek, Cent. Eur. J. Phys. č 10 , 181 (2012).
- 29 K. J. Kanarik, et al. , J. Vac. Sci. Technol. A 35 , 05C302 (2017).
- 31 F. Karouta, J. Phys. D: Appl. Phys. 47 , 233501 (2014).
- 30 W. Haynes, D. Lide, and T. Bruno, CRC Handbook of Chemistry and Physics (CRC, Boca Raton, FL, 2017), Vol. 97.
- 32 C. Mannequin, C. Vallée, K. Akimoto, T. Chevolleau, C. Durand, C. Dussarrat, T. Teramoto, E. Gheeraert, and H. Mariette, J. Vac. Sci. Technol. A 38 , 032602 (2020).
- 34 K. J. Kanarik, S. Tan, and R. A. Gottscho, J. Phys. Chem. Lett. 9 , 4814 (2018).
- 33 J. Michaels, N. Delegan, Y. Tsaturyan, J. Renzas, D. Awschalom, J. Eden, and F. Heremans, J. Vac. Sci. Technol. A 41 , 032607 (2023).
- 35 J. Hennessy, C. S. Moore, K. Balasubramanian, A. D. Jewell, K. France, and S. Nikzad, J. Vac. Sci. Technol. A 35 , 041512 (2017).