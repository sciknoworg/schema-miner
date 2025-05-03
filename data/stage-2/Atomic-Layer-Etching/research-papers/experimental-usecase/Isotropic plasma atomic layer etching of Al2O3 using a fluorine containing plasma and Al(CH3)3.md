<!-- image -->

RESEARCH ARTICLE |  OCTOBER 20 2020

<!-- image -->

## Isotropic plasma atomic layer etching of Al O  using a 2 3 fluorine containing plasma and Al(CH ) 3 3 

Nicholas J. Chittock; Martijn F. J. Vos; Tahsin Faraz ; Wilhelmus M. M. (Erwin) Kessels ; Harm C. M. Knoops ; Adriaan J. M. Mackus 

<!-- image -->

Check for updates

Appl. Phys. Lett. 117, 162107 (2020)

https://doi.org/10.1063/5.0022531

 

<!-- image -->

<!-- image -->

## Articles You May Be Interested In

Atomic layer deposition on porous powders with in situ gravimetric monitoring in a modular fixed bed reactor setup

Rev. Sci. Instrum. (July 2017)

Process study of gadolinium aluminate atomic layer deposition fromthegadolinium tris-diisopropylacetamidinate precursor

J. Vac. Sci. Technol. A (December 2011)

Isotropic atomic layer etching of GaN using SF 6  plasma and Al(CH 3 ) 3

J. Appl. Phys. (August 2023)

<!-- image -->

## Isotropic plasma atomic layer etching of Al2O3 using a fluorine containing plasma and Al(CH3)3

<!-- image -->

## AFFILIATIONS

1 Department of Applied Physics, Eindhoven University of Technology, P.O. Box 513, 5600 MB Eindhoven, The Netherlands 2 Oxford Instruments Plasma Technology, North End, Bristol BS49 4AP, United Kingdom

- a) Author to whom correspondence should be addressed: a.j.m.mackus@tue.nl

## ABSTRACT

Nanofabrication techniques with atomic level precision are needed for advancement to smaller technology nodes in the semiconductor industry. Thermal atomic layer etching (ALE) is currently being developed to isotropically etch material for future applications. In this Letter, an alternative plasma-based ALE process for isotropic etching of Al2O3 is introduced involving SF6 plasma and trimethylaluminium [TMA, Al(CH3)3] pulses, providing higher etch rates and lower processing temperatures than conventional thermal ALE. This process illustrates that a fluorine-containing plasma can serve as a viable reactant for ALE and that plasmas-besides their conventional use in anisotropic ALE-can be employed for isotropic ALE. In situ spectroscopic ellipsometry measurements confirmed saturation of both SF6 plasma and TMA half-cycles, which results in an etch per cycle (EPC) of 3.1 6 0.1 A at 260 ˚ /C14 C. The isotropic nature of the plasma ALE process was demonstrated by transmission electron microscopy analysis of Al2O3-coated 3D trench structures after performing ALE cycles. A mechanism of fluorination by F radicals and ligand exchange reactions involving TMA is proposed for this plasma ALE process based on observations from infrared spectroscopy, which are supported by reactant synergy analysis. This work establishes the benefits that a plasma can deliver for isotropic ALE.

Published under license by AIP Publishing. https://doi.org/10.1063/5.0022531

As industry strives to keep up with Moore's law, new fabrication techniques need to be developed to produce complex features with atomic-scale precision. 1,2 Atomic layer etching (ALE) is poised to be an enabling technology for this pursuit, allowing for precise removal of material in a layer-by-layer fashion. 1,3-5 ALE is a cyclic process, similar to atomic layer deposition (ALD), which typically consists of two sequential and self-limiting half-reactions separated by purge steps. 1 Half-cycle A of an ALE process creates a modified surface layer that is removed during half-cycle B. By ensuring that each half-cycle is selflimiting, a high level of etch control can be achieved. Compared to currently available etch technologies, ALE typically offers accurate control of etch depth, minimal substrate damage, and a smooth surface after etching. 1,3,6 These properties are vital for fabrication of next generation devices such as gate-all-around transistors, 2,7 3D flash memory (3D NAND), 8 and high-electron-mobility-transistors. 9 Furthermore, ALE processes are also considered for other processing steps, such as surface preparation or cleaning to remove thin native oxides or contamination, 10 and as correction steps to improve the selectivity of area-selective deposition processes. 11-13

ALE is divided into plasma and thermal varieties, which are oftentimes inadequately considered to be synonymous with anisotropic and isotropic etching, respectively. Plasma ALE has so far predominantly been employed for anisotropic etching in which directional ions from the plasma play a role. In contrast, isotropic ALE typically involves thermal chemistries, where the activation energy of the reaction is overcome by employing an elevated substrate temperature. Thermal ALE processes often include fluorination, chlorination, or oxidation reactions, which readily proceed at elevated substrate temperatures without the need for a plasma. 10,11,14-21 As an emerging technique, the research on isotropic thermal ALE has focused on finding viable precursors and co-reactants to achieve etching of a variety of materials. A selection of these isotropic ALE processes can be seen in Table I. From the table, we can see that dielectrics are commonly etched using fluorination chemistries, whereas isotropic ALE of metals is often achieved using chlorination or oxidation reactions to generate a modified surface. 22,23 Recently, it has been shown that isotropic ALE can also be achieved in an alternative manner by employing radicaldriven plasmas with a minimal ion contribution. 21,24-26 Radicals are

TABLE I. List of materials that can be etched via isotropic ALE, showing the type of reaction employed to modify the surface. Processes taken from the AtomicLimits ALE database. 36

| Modification step   | Materials etched                                                              |
|---------------------|-------------------------------------------------------------------------------|
| Fluorination        | Al 2 O 3 , HfO 2, ZnO, ZrO 2 , VO 2 , TiO 2, SiO 2 , AlN, GaN, AlF 3 , InGaAs |
| Chlorination        | TiN, TaN, Si, Ge, Fe, Co, GaAs                                                |
| Oxidation           | TiN, WS 2, MoS 2 , GaAs, SiGe, Si 3 N 4 , Si, Cu, W                           |
| Other               | ZnO, WO 3 , Cu, GaAs, Si 3 N 4                                                |

more reactive (due to their unpaired valence electrons) than molecular reactants (e.g., HF) and do not have to be dissociated before they can react at a substrate. This increased reactivity is expected to lead to the formation of a thicker modified surface layer and may enable etching of materials which are typically resistant to modification by thermal reactants (e.g., crystalline materials). In comparison to thermal isotropic ALE processes, the use of highly reactive plasma radicals potentially allows for a higher etch per cycle (EPC), as well as access to a broader temperature window. 21,25

ALE of Al2O3 has previously been achieved by using fluorinating reactants, such as hydrogen fluoride (HF) derived from HF pyridine or sulphur tetrafluoride (SF ), combined with tri-methyl aluminium 4 [TMA, Al(CH3)3], dimethyl aluminium chloride [DMAC, AlCl(CH3)2], or tin acetylacetone [Sn(acac)2] as an etchant. 14-20 One of the most documented approaches for ALE of Al2O3 is the use of HF and TMA. 10,14-19 Half-cycle A of this thermal ALE process consists of the formation of an AlF3/AlOxFy surface layer by exposure to HF gas. This modified layer can then be removed by dosing TMA in half-cycle B, which produces volatile Al-containing species [namely AlF(CH3)2] via a transmetalation ligand exchange reaction. 14,16-19 However, HF pyridine can be a difficult reactant to work with and, therefore, alternative co-reactants are desired. For example, in recent work, SF4 was explored as a replacement thermal reactant for the fluorination step. 20 Another possible substitute for HF is a fluorine-containing plasma, such as sulfur hexafluoride (SF6), which is an inert non-toxic gas. When ignited as a plasma, SF6 produces highly reactive fluorine radicals, which provide the aforementioned benefits of a plasma process. SF6 plasma is a promising alternative due to its widespread availability, ease of use, and safety benefits. 27-29 Since it is a commonly used etchant, SF 6 plasmas have been extensively studied and this knowledge can be leveraged to aid the development of atomic-scale processes. 28,29 SF6 plasmas are known for having high concentrations of F radicals, which can be /C24 10 3 times higher in concentration than S radicals. Other neutral species such as F 2 and SF4 can also be formed in an SF6 plasma, while the most prominent charged species are SF5 þ and F /C0 ions. 30 In our previous work, SF6 plasma and TMA were employed at low temperatures to deposit AlF3 by plasma ALD. 30 In that work, the growth per cycle (GPC) was seen to be strongly correlated with the substrate temperature, with higher temperatures giving a reduced GPC. 30

In this Letter, an isotropic plasma ALE process consisting of SF 6 plasma and TMA pulses is introduced. Considering that other fluorine radical sources (such as NF3 plasma) are expected to allow for ALE with similar surface reactions, this process can be seen as a model system for demonstrating the benefits of employing a fluorinating plasma. Since the SF6/TMA is inspired on an existing thermal ALE chemistry, the reaction mechanism as studied using infrared (IR) spectroscopy is discussed first. The observations from the IR experiments support a mechanism involving fluorination and ligand exchange reactions. Subsequently, it is confirmed that SF 6 plasma and TMA satisfy the main requirements of ALE reactants in terms of saturation of the two half-cycles and synergy of the reactants. The merits of this process as compared to the thermal ALE process were assessed by measuring the etch rate as a function of temperature. Finally, TEM analysis confirmed the isotropic nature of the process, highlighting that plasmas are viable reactants for isotropic processing.

To study the reaction mechanisms of the Al2O3 plasma ALE process, IR spectroscopy experiments were conducted at 250 /C14 C as depicted in Fig. 1. Al O3 2 was first deposited on a SiO2 powder and then exposed to SF6 plasma and TMA pulses. Figure 1(a) shows that the Al-O absorbance band at 800-1100cm /C0 1 decreases with the increasing number of ALE cycles, which corresponds to the removal of material after each ALE cycle. Figure 1(b) shows the IR absorbance peaks at 2900 and 2950 cm /C0 1 , corresponding to the AlCH3 symmetric and asymmetric stretching modes, respectively. Following TMA dosing, AlCH3 surface species are observed as indicated by an increase in the CH3 absorbance peak. These methyl groups are thought to be formed after removal of the fluorinated surface layer, allowing excess TMAto adsorb on the bulk Al2O3. After SF6 plasma exposure, a negative CH3 peak is observed, indicating the removal of surface methyl groups, which is attributed to ligand exchange reactions between methyl groups and fluorine atoms. The replacement of surface methyl groups by fluorine radicals generates a fluorinated surface layer on the Al2O3 substrate.

FIG. 1. Difference infrared spectra collected at 250 /C14 C, in which a decrease in absorption corresponds to the removal of species, while an increase in absorption represents the formation of species. Graph (a) shows the broad absorbance region between 800 and 1100 cm /C0 1 corresponding to Al-O in the film. These spectra are taken after each SF6 plasma/TMA ALE cycle and are referenced to the asdeposited Al O3 2 spectrum taken prior to the ALE cycles. Graph (b) shows the AlCH3 absorbance peaks at 2900 and 2950 cm /C0 1 . Spectra were recorded after each SF6 plasma and TMA half-cycle and are referenced to the previous half-cycle.

<!-- image -->

Based on the IR data, a reaction pathway is proposed, assuming for simplicity that only AlF(CH3)2 is formed as a volatile reaction product,

$$1 2 \, F _ { ( g ) } + 2 \, A l _ { 2 } O _ { 3 } \to 4 \, A l F _ { 3 ( s ) } + 3 \, O _ { 2 ( g ) }, \quad \ \ ( 1 a ) \quad \widehat { c } \ |$$

$$\ A I F _ { 3 ( s ) } + 2 \, A I ( \mathrm C H _ { 3 } ) _ { 3 ( g ) } \to 3 \, A I F ( \mathrm C H _ { 3 } ) _ { 2 ( g ) }. \quad ( 1 b ) \quad \breve { \hookrightarrow } ^ { 2 } \, \shortparallel.$$

The fluorination step is described in Eq. (1a), in which fluorine radicals from the plasma react with the Al2O3 surface by creating an AlF3 layer. Ligand exchange reactions between the modified surface and TMA are shown in Eq. (1b), where etching is achieved through the formation of volatile Al-containing reaction products. This reaction is based on the mechanism proposed for thermal ALE of Al2O3 using HF/TMA, which has been confirmed by mass spectroscopy studies on both fluorinated Al O3 2 and AlF3 surfaces. 16,17,19 The reaction by-product (AlF(CH3)2) is the same for both surfaces and was observed to also exist as a dimer with either itself or TMA. 19

Saturation curves for both half-cycles were determined on Al O 2 3 coated Si coupons at a substrate temperature of 260 /C14 C (corresponding to a table temperature of 300 /C14 C, see supplementary material SIII). 31,32 The film thickness was recorded after every five cycles using in situ SE, and the EPC was calculated from the slope of film thickness plotted against the number of ALE cycles. The EPC as a function of plasma and precursor dose time are depicted in Fig. 2. The SF 6 plasma exposure and TMA dose show saturation behavior that is typical for ALE processes involving fluorination. 3,10,14,15 Cycles with a SF6 plasma exposure of /C24 5 s, a TMA dose of /C24 0.5 s, and a 10 s TMA hold step yield an etch rate of 3.1 6 0.1 A/cycle. ˚ Additional experiments performed without a TMA hold step after dosing required very long TMAdoses ( /C24 10 s) to achieve etching. Furthermore, as shown in Figs. 2(b) and 2(d), pump steps of 10 s are sufficient to avoid a parasitic etching component. The measured EPC is higher than the literature results reported for thermal ALE of Al2O3 with HF/TMA at a comparable temperature. 10,14-18 A recipe with pulses of 5 s SF 6 plasma exposure and 0.5 s TMA dosing, 10 s TMA hold step, separated by 10 s pump steps, is referred to as the 'standard ALE cycle' in the remainder of this Letter.

The SF6 plasma saturation curve in Fig. 2(a) shows quasisaturation behavior similar to the modification steps observed for many other ALE processes. 14,24 The initial steep increase in EPC for short plasma exposure is thought to be due to the rapid fluorination of the surface region. For longer plasma exposure times, the EPC tapers off as the surface AlF 3 layer begins to act as a diffusion barrier, hindering further fluorination of the bulk Al2 O3 underneath. This surface fluorination reaction shows similarities to the oxidation of Si and other materials as described by Deal-Grove adsorption kinetics. 14,33 Exposure of the substrate to SF6 gas without igniting a plasma does not lead to etching of the film, signifying the key role plasma radicals play in the etching mechanism. Figure 2(c) shows that the TMA dose saturates quickly for doses longer than 0.3 s. Doses shorter than 0.2 s were found to cause a negligible thickness change, which is likely related to the consumption of TMA by AlF3 deposition on the reactor walls (100 /C14 C) that are at a lower temperature than the substrate holder (300 /C14 C). Previous work has shown that AlF3 ALD using SF6 plasma and TMA readily occurs at low temperatures. It is, therefore, likely that a significant amount of dosed TMA is adsorbed on the reactor walls before it can reach the substrate. 30 Overall, the self-limiting

FIG. 2. Saturation curves for (a) SF 6 plasma exposure using a 0.5 s TMA dose, (b) the pump step following SF 6 plasma exposure, (c) TMA dosing using a 5 s SF 6 plasma exposure, and (d) the pump step following the TMA dose. All experiments were conducted at a substrate temperature of 260 /C14 C with 10 s TMA hold steps. The dashed lines are guides to the eye.

<!-- image -->

behavior shown by both SF6 plasma and TMA identifies them as viable reactants for ALE.

A key requirement for ALE is that etching should only occur if the substrate is exposed to alternating half-cycles. To investigate synergistic effects of the reactants in this plasma ALE process, the film thickness was recorded after every 5 pulses/cycles while the substrates were exposed to 30 pulses of SF 6 plasma, 30 pulses of TMA, followed by 50 standard ALE cycles. Al2O3 is resistant to spontaneous etching by SF 6 plasma, with etching observed only when alternating between SF6 plasma and TMA doses. Similar behavior was exhibited by HfO2 substrates, as depicted in Fig. S2 of the supplementary material. Figure 3(a) shows that exposure of Al2O3 to multiple SF6 plasma pulses without dosing TMA (half-cycle A) causes an initial 1A ˚ increase in film thickness, which corresponds to the formation of a thin fluorinated surface layer. 15,17,18 When subsequently exposing the substrate to TMA pulses [Fig. 3(b)], the thickness initially decreases by /C24 3A ˚ , and this is attributed to the removal of the modified AlF3 surface layer. After the initial 3 A of etching, the film thickness remains ˚ constant during further TMA doses, confirming that the TMA exposure is self-limiting. The thickness change observed when switching from SF6 plasma to TMA pulses in Figs. 3(a) and 3(b) is consistent with a fluorination and ligand exchange reaction mechanism, as etching only occurs when TMA is dosed onto a fluorinated surface. 16 Alternating pulses of SF6 plasma and TMA [Fig. 3(c)] show a linear dependence between the number of cycles and etch depth of the Al2O3

FIG. 3. Film thickness, measured every five cycles, as a function of number of pulses or cycles performed on Al O . (a) SF 2 3 6 plasma without a TMA dose representing half-cycle A. (b) TMA and SF 6 gas dosing without striking a plasma representing half-cycle B. (c) Full ALE cycles with alternating SF6 plasma and TMA doses, confirming a linear relationship between the etch depth and the number of cycles. The inset shows a magnification of the transition between half-cycles A and B. Standard ALE recipe conditions are used for each step. The horizontal dashed lines indicate the initial film thickness before processing.

<!-- image -->

film, yielding an etch rate of 3.1 A/cycle. Using this ALE etch rate and ˚ the observed film thickness changes for each half-cycle, the ALE synergy is calculated to be 99.9%. 1,3

The etch rate for the SF 6 plasma/TMA process was evaluated as a function of substrate temperature for table temperatures ranging from 175 to 375 /C14 C. By monitoring the optical constants of the Si substrate using in situ SE, 31,32 this table temperature range was found to correspond to actual substrate temperatures between 140 and 285 /C14 C. The standard ALE cycle (with saturating doses of SF6 plasma and TMA determined at 300 /C14 C) was used for all temperatures. It can be seen from Fig. 4 that the EPC is strongly dependent on substrate temperature and increases from 0.2 A/cycle at 155 ˚ /C14 C to 3.4 A/cycle at 285 ˚ /C14 C. At low temperatures, a transition from ALE to ALD is observed, indicated by a negative EPC value at 140 /C14 C. The transition temperature found in this study is lower than for thermal ALE processes using HF/ TMAreported in the literature (170-250 /C14 C) 14,17 and is comparable to transition temperatures observed for HF/DMAC and HF/Sn(acac)2 (as shown in Fig. S3 of the supplementary material). In previous work, ALD of AlF3 was observed to proceed in the wide temperature range of 50-300 /C14 C when using a short 10 ms TMA dose. 30 This suggests that not only the temperature but also exposure to the precursor determines whether deposition or etching occurs. Using a large TMA dose will likely result in etching if the temperature is above the ALD/ALE transition temperature, while using a small TMA dose is more likely to lead to deposition. In comparison to thermal ALE, the plasma ALE process exhibits a higher EPC over the entire temperature range investigated here. A significant etch rate of 0.8 A/cycle was already observed ˚ at a relatively low temperature of 185 /C14 C, highlighting one of the benefits of using a plasma process. It is thought that the fluorine radicals provided by the plasma allow for higher etch rates as a thicker fluorinated surface region is formed as compared to when using HF.

To confirm the isotropic nature of this ALE process, etching was performed in 3D trench structures with an aspect ratio (AR) of /C24 2.5.

FIG. 4. Comparison of literature values of the etch per cycle (EPC) for thermal HF/ TMA processes and the SF6 plasma/TMA process outlined here. 10,14,15,18 Temperatures reported from this work are measured using in situ spectroscopic ellipsometry, while the literature values are the reported set point temperatures. Substrate temperature values from the literature may deviate depending on process conditions and reactors used, as discussed in more detail in the supplementary material. Additional data for thermal ALE processes utilizing alternate reactants are presented in Fig. S3 in the supplementary material.

<!-- image -->

Al2O3 films were deposited by plasma ALD (with TMA/O2 plasma) to a thickness of 210 A. Figure 5(a) shows an as-deposited trench struc-˚ ture, in which the film thickness is indicated in four different locations within the structure. In Fig. 5(b), a similar trench structure is shown after being exposed to 40 ALE cycles, where the thickness of the removed film is highlighted. The average etch rate over the 3D trench structures was calculated to be 2.9 6 0.1 A/cycle, which agrees with the ˚ EPC value obtained for blanket substrates. In contrast to the highly directional etch profiles characteristic for anisotropic plasma ALE, this plasma process exhibits a comparable etch depth for both horizontal

FIG. 5. Cross-sectional TEM images of Al O3 2 deposited and etched on 3D Si trench structures. (a) Trench structure coated with an Al O 2 3 film by plasma ALD, showing average film thickness in four regions. (b) A similar trench structure after 40 ALE cycles, in which the thickness etched in each region is highlighted. The standard ALE cycle was used to perform the etching.

<!-- image -->

and vertical surfaces of 111 6 4A ˚ and 119 6 4A ˚ , respectively (note that anisotropic etching would lead to a higher etch rate on horizontal surfaces). This suggests that directional ions in the SF 6 plasma do not significantly contribute to etching of the Al2O3 surface. A possible explanation for why the etch rate on the horizontal surfaces appears slightly lower than that on the vertical surfaces is densification of the film due to ion exposure during the O2 plasma steps of the Al O3 2 ALD cycle. 34,35 Despite these minor variations, it can be concluded from the high consistency of the etch rate over the trench structure that the ALE process is isotropic in nature.

In summary, this work demonstrates that the isotropic plasma ALE of Al2O3 can be achieved using alternating pulses of SF 6 plasma and TMA. A reaction mechanism for Al2O3 ALE was proposed where SF6 plasma fluorinates the Al2 O3 surface and TMA etches the fluorinated surface region by producing volatile AlF(CH3)2. The etch rate was found to be strongly dependent on the substrate temperature, with higher temperatures yielding an increased EPC. When compared to thermal Al2O3 ALE processes, this plasma ALE process exhibits higher etch rates, as well as etching at low temperatures. The use of a plasma thereby extends the parameter space for isotropic ALE of Al2O3, for example, by allowing for processing of substrates sensitive to high temperatures. TEM analysis revealed an isotropic etch profile on 3D trench structures, demonstrating that plasmas can be employed as reactants for isotropic ALE. SF 6 plasma has been introduced as a viable co-reactant for isotropic ALE, highlighting that fluorinecontaining plasmas are suitable for isotropic processing; however, care must be taken to avoid spontaneous etching of certain substrates. Future investigations will look to expand the SF 6 plasma/TMA process to a wider range of materials, as well as identifying plasma chemistries beyond fluorination that can be employed for isotropic ALE. Overall, this work contributes to expanding the toolbox of isotropic plasma ALE, a technique that will aid in the fabrication of 3D structures for next generation semiconductor devices.

See the supplementary material for experimental details, etching data for HfO2, discussion of substrate temperature during experiments, and a comparison of plasma ALE to thermal ALE with alternative reactants.

This work is part of the research program HTSM with Project No. 17124, which is financed by the Netherlands Organisation for Scientific Research NWO. The authors would like to acknowledge J. W. Woollam Co. for lending the iSE in situ spectroscopic ellipsometer and ASM for providing patterned substrates as well as TEM analysis. The authors would also like to thank J. J. A. Zeebregts, C. A. A. van Helvoirt, C. van Bommel, J. J. L. M. Meulendijks, and B. Krishnamoorthy for technical support and M. J. M. Merkx for fruitful discussions on this work.

The authors declare no competing financial interest.

## DATA AVAILABILITY

The data that support the findings of this study are openly available in 4TU.ResearchData at https://data.4tu.nl/, Ref. 37.

## REFERENCES

1 K. J. Kanarik, S. Tan, and R. A. Gottscho, J. Phys. Chem. Lett. 9 (16), 4814-4821 (2018).

- 2
- H. H. Radamson, X. He, Q. Zhang, J. Liu, H. Cui, J. Xiang, Z. Kong, W. Xiong, J. Li, J. Gao, H. Yang, S. Gu, X. Zhao, Y. Du, J. Yu, and G. Wang, Micromachines 10 (5), 293 (2019).
- 3 K. J. Kanarik, T. Lill, E. A. Hudson, S. Sriraman, S. Tan, J. Marks, V. Vahedi, and R. A. Gottscho, J. Vac. Sci. Technol., A 33 (2), 020802 (2015).
- 4 R. Clark, K. Tapily, K. Yu, T. Hakamata, S. Consiglio, D. O'Meara, C. Wajda, J. Smith, and G. Leusink, APL Mater. 6 (5), 058203 (2018).
- 5 T. Faraz, F. Roozeboom, H. C. M. Knoops, and W. M. M. Kessels, ECS J. Solid State Sci. Technol. 4 (6), N5023-N5032 (2015).
- 6 C. Fang, Y. Cao, D. Wu, and A. Li, Prog. Nat. Sci. 28 (6), 667-675 (2018).
- 7 C. T. Carver, J. J. Plombon, P. E. Romero, S. Suri, T. A. Tronic, and R. B. Turkot, ECS J. Solid State Sci. Technol. 4 (6), N5005-N5009 (2015).
- 8 R. Micheloni, S. Aritome, and L. Crippa, Proc. IEEE 105 (9), 1634-1649 (2017). 9 Y. He, H. Gao, C. Wang, Y. Zhao, X. Lu, C. Zhang, X. Zheng, L. Guo, X. Ma, and Y. Hao, Phys. Status Solidi A 216 (16), 1900115 (2019).
- 10 J. Hennessy, C. S. Moore, K. Balasubramanian, A. D. Jewell, K. France, and S. Nikzad, J. Vac. Sci. Technol., A 35 (4), 041512 (2017).
- 11 S. K. Song, H. Saare, and G. N. Parsons, Chem. Mater. 31 (13), 4793-4804 (2019).
- 12 A. J. M. Mackus, M. J. M. Merkx, and W. M. M. Kessels, Chem. Mater. 31 (1), 2-12 (2019).
- 13 M. F. J. Vos, S. N. Chopra, M. A. Verheijen, J. G. Ekerdt, W. M. M. Kessels, and A. J. M. Mackus, Chem. Mater. 31 (11), 3878-3882 (2019).
- 14 A. M. Cano, A. E. Marquardt, J. W. DuMont, and S. M. George, J. Phys. Chem. C 123 (16), 10346-10355 (2019).
- 15 Y. Lee, J. W. DuMont, and S. M. George, Chem. Mater. 28 (9), 2994-3003 (2016).
- 16
- Y. Lee, C. Huffman, and S. M. George, Chem. Mater. 28 (21), 7657-7665 (2016).
- 17 J. W. DuMont and S. M. George, J. Chem. Phys. 146 (5), 052819 (2017).
- 18 D. R. Zywotko, J. Faguet, and S. M. George, J. Vac. Sci. Technol., A 36 (6), 061508 (2018).
- 19 J. W. Clancey, A. S. Cavanagh, J. E. T. Smith, S. Sharma, and S. M. George, J. Phys. Chem. C 124 (1), 287-299 (2020).
- 20 J. C. Gertsch, A. M. Cano, V. M. Bright, and S. M. George, Chem. Mater. 31 (10), 3624-3635 (2019).
- 21 N. R. Johnson, J. K. Hite, M. A. Mastro, C. E. Eddy, Jr., and S. M. George, Appl. Phys. Lett. 114 , 243103 (2019).
- 22 E. Mohimi, X. I. Chu, B. B. Trinh, S. Babar, G. S. Girolami, and J. R. Abelson, ECS J. Solid State Sci. Technol. 7 (9), P491-P495 (2018).
- 23 M. Konh, C. He, X. Lin, X. Guo, V. Pallem, R. L. Opila, A. V. Teplyakov, Z. Wang, and B. Yuan, J. Vac. Sci. Technol., A 37 , 021004 (2019).
- 24 S. D. Sherpa, P. L. G. Ventzek, and A. Ranjan, J. Vac. Sci. Technol., A 35 (5), 05C310 (2017).
- 25 A. Mameli, M. A. Verheijen, A. J. M. Mackus, W. M. M. Kessels, and F. Roozeboom, ACS Appl. Mater. Interfaces 10 , 38588-38595 (2018).
- 26 J. Li, Y. Li, N. Zhou, G. Wang, Q. Zhang, A. Du, Y. Zhang, J. Gao, Z. Kong, H. Lin, J. Xiang, C. Li, X. Yin, Y. Li, X. Wang, H. Yang, X. Ma, J. Han, J. Zhang, T. Hu, T. Yang, J. Li, H. Yin, H. Zhu, W. Wang, and H. H. Radamson, Materials 13 (3), 771 (2020).
- 27 S. J. Oh, H. C. Lee, and C. W. Chung, Phys. Plasmas 24 (1), 013512 (2017).
- 28 C. Cardinaud, C. R. Chim. 21 (21), 723 (2018).
- 29 S. J. Ullal, H. Singh, J. Daugherty, V. Vahedi, and E. S. Aydil, J. Vac. Sci. Technol., A 20 , 1195-1201 (2002).
- 30 M. F. J. Vos, H. C. M. Knoops, R. A. Synowicki, W. M. M. Kessels, and A. J. M. Mackus, Appl. Phys. Lett. 111 (11), 113105 (2017).
- 31 I. E. Clemente and A. V. Miakonkikh, Proc. SPIE 10224 , 1022425 (2016).
- 32 H. C. M. Knoops, E. M. J. Braeken, K. de Peuter, S. E. Potts, S. Haukka, V. Pore, and W. M. M. Kessels, ACS Appl. Mater. Interfaces 7 , 19857-19862 (2015).
- 33 B. E. Deal and A. S. Grove, J. Appl. Phys. 36 (12), 3770-3778 (1965).
- 34 R. A. Ovanesyan, N. Leick, K. M. Kelchner, D. M. Hausmann, and S. Agarwal, Chem. Mater. 29 (15), 6269-6278 (2017).
- 35
- T. Faraz, M. van Drunen, H. C. M. Knoops, A. Mallikarjunan, I. Buchanan, D. M. Hausmann, J. Henri, and W. M. M. Kessels, ACS Appl. Mater. Interfaces 9 (2), 1858-1869 (2017).
- 36 See https://www.atomiclimits.com/aledatabase/ for further information on the ALE processes shown in Table I.
- 37 N. Chittock, 'Isotropic plasma atomic layer etching of Al2O3,' 4TU.ResearchData, https://data.4tu.nl/