## ReseaRch aRticle

<!-- image -->

## Combining Experimental and DFT Investigation of the Mechanism Involved in Thermal Etching of Titanium Nitride Using Alternate Exposures of NbF5 and CCl4, or CCl 4  Only

Varun Sharma,* Suresh Kondati Natarajan, Simon D. Elliott, Tom Blomberg, Suvi Haukka, Michael E. Givens, Marko Tuominen, and Mikko Ritala*

## 1. Introduction

Thermally activated chemical vapor-phase etching of titanium nitride (TiN) is studied by utilizing either alternate exposures of niobium pentafluoride (NbF5) and carbon tetrachloride (CCl 4 ) or by using CCl 4 alone. Nitrogen (N 2 ) gas purge steps are carried out in between every reactant exposure. Titanium nitride is etched in a non-self-limiting way by NbF -CCl  based binary chemistry 5 4 or by CCl 4 at temperatures between 370 and 460  C. Spectroscopic ellipsometry ° and a weight balance are used to calculate the etch per cycle. For the binary chemistry, an etch per cycle of ≈ 0.8 Å is obtained for 0.5 and 3 s long exposures of NbF5 and CCl4, respectively at 460  C. On the contrary, under the ° same conditions, the etch process with CCl 4  alone gives an etch per cycle of about 0.5 Å. In the CCl 4 -only etch process, the thickness of TiN films removed at 460 ° C varies linearly with the number of etch cycles. Furthermore, CCl 4 alone is able to etch TiN selectively over other materials such as Al 2 O3, SiO2, and Si 3 N4. X-ray photoelectron spectroscopy and bright field transmission electron microscopy are used for studying the post-etch surfaces. To understand possible reaction products and energetics, first-principles calculations are carried out with density functional theory. From thermochemical analysis of possible reaction models, it is found that NbF 5  alone cannot etch TiN while CCl4 alone can etch it at high temperatures. The predicted byproducts of the reaction between the CCl4  gas molecules and TiN surface are TiCl 3  and ClCN. Similarly, TiF , NbFCl 3 4 , and ClCN are predicted to be the likely products when TiN is exposed to both NbF5 and CCl4. A more favorable etch reaction is predicted when TiN is exposed to both NbF5 and CCl4 ( ∆ G = -2.7 eV at 640 K) as compared to exposure to CCl4 only ( ∆ G = -2 eV at 640 K) process. This indicates that an enhanced etch rate is possible when TiN is exposed alternately to both NbF5 and CCl4, which is in close agreement with the experimental results.

With  the continuous  scaling of device dimensions  in  integrated  circuits,  more complex  3D  device  architectures  are  constantly being  developed. [1,2] In  order  to keep developing such non-line-of-sight features,  processing  techniques  that  provide  conformal  as  well  as  precise  control  of  thickness  at  the  atomic  scale  have become indispensable. [3-5] Deposition and  etching  are  two  of  the  most  widely employed techniques in the fabrication of today's  nanoelectronic  devices.  Semiconductor  tool  manufacturers  have  stretched their limits to gain atomic precision when depositing and etching various materials. [3-7] Atomic layer deposition is a well established  chemical  gas  phase  deposition technique with hundreds of reported processes. [8,9] On  the  other  hand,  reports on  plasma-free  chemical-based  etch  processes  are  limited  and  especially  so  for the recently developed thermal atomic layer etching (ALE). [10,11] Thermal ALE is  a  technique  that  uses  sequential  selflimiting surface-gas reactions in order to  etch  material  from  the  surface. [12] The self-limiting  surface  reactions  may  provide  important  advantages,  such  as  isotropic etching, [11,12] thickness  control  in the atomic regime and possibly improved etch selectivity. Therefore, thermal ALE is

V. Sharma, S. Haukka, M. E. Givens, M. Tuominen ASM Microchemistry Oy Pietari Kalmin katu 3 F2, Helsinki, Uusimaa 00560, Finland E-mail: varun.sharma@asm.com, varun.sharma@helsinki.fi V. Sharma, M. Ritala Department of Chemistry University of Helsinki Helsinki, Uusimaa 00014, Finland E-mail: mikko.ritala@helsinki.fi

- The ORCID identification number(s) for the author(s) of this article can be found under https://doi.org/10.1002/admi.202101085.

DOI: 10.1002/admi.202101085

Adv. Mater. Interfaces 2021 , 8 , 2101085

S. Kondati Natarajan Department of Electrical Engineering and Automation Aalto University Espoo 02156, Finland S. D. Elliott Schrödinger 120 West 45th Street, New York, NY 10036-4041, USA T. Blomberg Department of Chemistry and Materials Science Aalto University Espoo, Uusimaa 02150, Finland

<!-- image -->

www.advancedsciencenews.com a promising technique for fabricating non-line-of-sight features in 3D nanoscale devices.

Titanium  nitride  (TiN)  is  a  crucial  material  for  the  semiconductor  industry  due  to  its  CMOS  compatibility  and  has found use in applications such as tunable work-function metal gate [13] in  FIN-field-e/uniFB00ect-transistor  and  gate-all-around  nanowire metal-oxide-semiconductor-field-e/uniFB00ect-transistor, [14] gate electrode  in  metal-insulator-semiconductor  field  e/uniFB00ect  transistor, [15] di/uniFB00usion  barrier, [16] metal hard mask, [17] anti-reflective coating, [18] extreme  ultra-violet  patterning, [19] sub-bandgap [20] and Schottky photodetector, [21] and in plasmonics. [22,23]

So  far,  most  of  the  TiN  etch  processes  utilize  either  solutions [24-26] or plasma chemistries, [27-30] and a very few purely vapor etch  processes  have  been  reported. [31,32] Lee  et  al. [31] proposed a  conversion-etch  mechanism  for  TiN.  First,  the  surface  of  the TiN films was oxidized to TiO 2  by ozone (O 3 ) and then TiO 2 was etched by HF vapor in the form of volatile TiF 4  and H 2 O species. Ozone is a strong oxidant [31] and is capable of oxidizing also other materials in the vicinity on the integrated circuit chips. HF is toxic and its use may result in the dreaded fluorine contamination that not only a/uniFB00ects the performance of CMOS devices but also poses compatibility  issues  with  storage  as  well  as  semiconductor  processing equipment. Thus, new thermal processes with other etchants for TiN would be beneficial in fabricating complex devices.

We  report  novel  chemical  etching  processes  for  titanium nitride. Two types of etching processes were studied: first, a twostep gas-surface reaction based on sequential exposures of NbF 5 CCl4 reactants, and second a spontaneous etching by CCl 4  alone which can be defined as gas-phase pulsed etching (GPPE). [32]  N 2 purge steps were introduced in between reactant pulses to avoid any reactant overlap, and to purge the etch system from excess reactant molecules as well as reaction products.

First  principles  calculations  using  density  functional  theory (DFT) are employed to study the thermochemistry of the reactions involved in the etch process. First principles calculations provide  an  e/uniFB00ective  approach  for  evaluating  the  free  energies of  the  etch  reactions.  This  is  particularly  important  in  this study as many exotic chemical species may be involved in the reaction  for  which  experimental  thermodynamic  data  are  not available  in  the  literature.  We  also  use  DFT  to  predict  probable  etch  products  from  the  product  pressures  evaluated  at thermodynamic equilibrium.

## 2. Experimental Section

## 2.1. Substrates and Process Gases

P-doped  silicon  wafers  of  200  mm  diameter  were  chosen  as substrates.  The  target  films  subjected  to  etching  were  SiO , 2 Si 3 N4,  Al O 3 2 ,  and  TiN.  The  SiO   was  either  thermally  grown 2 silicon  oxide  of  about  22  nm  thick  or  15  nm  SiO   grown  by 2 the  plasma-enhanced  atomic  layer  deposition  technique. [33] A 20  nm  thick  LPCVD  nitride  (Si 3 N4)  was  used.  Al O 3 2 of  about 20  nm  was  deposited  at  300 ° C  by  the  trimethylaluminum and water (H2O) ALD process. [34]  TiN was deposited on 22 nm thermal oxide at 400 ° C by thermal ALD process utilizing TiCl 4 and NH3. [35] The TiN films used in these etch experiments were from 10 to 50 nm in thickness.

<!-- image -->

www.advmatinterfaces.de

NbF5  (98%,  CAS  Number  7783-68-8)  and  anhydrous  CCl4 (CAS  Number  56-23-5)  were  purchased  from  Sigma  Aldrich, Inc.  (Germany).  The  NbF 5   vessel  was  kept  at  45-50 ° C.  The CCl4 vessel was kept at room temperature and the vapors were drawn  into  the  chamber.  The  CCl 4   dose  was  controlled  by  a needle valve and the NbF5 outlet line did not have the needle valve installed. Nitrogen of 5.0 purity was used as a carrier gas, and was further purified by a purifier to ≥ 6.0 level.

## 2.2. Experimental Setup and Methodology

The etch experiments were performed in a Pulsar 2000 (P2000) reaction  chamber,  manufactured  by  ASM.  The  etch  temperature  was  varied  from  370  to  460 ° C  under  isothermal  conditions.  Due to the hardware limitation of this particular P2000 module, the 460 ° C was the maximum obtainable temperature and therefore the choice of the range. This temperature range may require  highly  thermally  stable  reactants  such  as  CCl 4 [36] and NbF5. [37,38] More details of a setup and methodology can be found in earlier reports. [32,39]

The etch rate per cycle (EPC) was calculated from the removed thickness values. Before and after etching, the thickness values were determined by spectroscopic ellipsometry (SE) and weight measurements as described earlier. [32] In order to verify the etch process, in situ grown TiN films were also subjected to etching. No  significant  di/uniFB00erences in  EPC  were  found  between  airoxidized and in situ grown TiN films. In some cases, an X-ray reflectometer was also used to confirm the thickness and extract density values of TiN films. For simplicity, EPC values reported here  were  extracted  from  the  weight  measurements  except  in Figure 4, where SE thickness values are reported.

## 2.3. Characterization Techniques and Equipment

The  SAG  204  balance  from  Mettler  Toledo  with  a  resolution  of about 0.1 mg was used for the weight measurements. The EPC and removed thickness values were extracted by using simple massdensity-volume relationship, as described in previous report. [32]

For  thickness,  optical  constants  and  density  measurements the  SE  800  (from  SENTECH)  ellipsometer  and  X'pert  PRO XRR (from Malvern Panalytical Ltd.) were used.

The  surface  composition  as  well  as  depth  profiles  were determined with the help of X-ray photoelectron spectroscopy (XPS).  The  XPS used here was a K-Alpha  from Thermo Sci-+ entific. The aluminum K α (1486.6 eV /15 kV) X-ray source was used with a spot size of about 400 µ m. In the XPS depth profile measurements,  the  argon  ion  energy  was  set  to  1000  eV.  For the survey scan, a total of 10 scans were performed with a pass energy of 200 eV, and an increment of 0.5 eV.

The transmission electron microscopy was executed by Evans Analytical  Group,  California.  For  the  imaging  the  FEI  Tecnai TF-20 FEG/TEM operated at 200 kV was used in the bright-field TEM mode. For the sample preparation, an in situ focused ion beam (FIB) lift-out  technique  on  an  FEI  dual  beam  FIB/SEM was  used.  Prior  to  the  ion  milling,  the  samples  were  carbon coated followed by sputtering iridium on top. The thickness of the TEM lamella was about 100 nm.

<!-- image -->

www.advancedsciencenews.com

## 3. Theory and Computational Setup

The Vienna Ab initio Simulation Package (VASP v5.3) [40,41]  was used  for  the  quantum  chemical  calculations  reported  in  this manuscript.  We  have  used  spin-polarized  DFT  to  describe  the electronic  structure  of  the  system  under  study.  The  exchangecorrelation interactions are approximated by the Perdew-BurkeErnzerhof [42] generalized  gradient  corrected  density  functional. The  valence  electrons  are  expanded  in  a  plane  wave  basis  set with a 400 eV cuto/uniFB00,  whereas  the  core  electrons  are  treated  by projector augmented wave (PAW) potentials. [43]  The PAW potentials have 13 valence electrons for Nb, 4 for Ti, 5 for N, and 7 each for F and Cl. The geometries are relaxed within 1 meV of energy and within 0.02 eV Å -1 of magnitude of each force component.

The cubic phase of TiN (space group Fm 3 m) is chosen for the DFT study. The bulk unit cell consists of 4 TiN units and its shape and volume are simultaneously relaxed with a higher energy  cuto/uniFB00  of  550  eV .  A  Monkhorst-Pack  k-point  mesh  of 6 × 6 × 6  is  used  to  sample  the  first  Brillouin  zone.  The  minimum energies of the isolated molecules are computed by optimizing their geometries within a noncubic box of dimensions 15 Å × 16 Å × 15.5 Å. The computation setup for the surface reaction are given in Section S0, Supporting Information.

For the reaction free energy computation, the free energy of a system at a given temperature T is given by

$$G & = E + H - T S & ( 1 ) & \text{reactor}$$

in  which E is  the  electronic  energy  of  the  system, H is  the enthalpy  and S is  the  entropy.  Enthalpy  and  entropy  of  gas phase species are obtained from the 'freeh' tool in the TURBOMOLE suite. [44] The  enthalpy and entropy of bulk systems are obtained with the Phonopy code, [45]  which uses the force constants  obtained  from  a  density  functional  perturbation  theory calculation in VASP with an energy threshold of 1.0 e -8 eV  for the self consistent field evaluation of the electronic energy. The reaction free energy is then computed as

$$\Delta G = \Delta E + \Delta H - T \Delta S + R T \, \ln ( \prod P _ { \text{products} } ^ { n p } / \prod P _ { \text{reactants} } ^ { n r } ) \quad \quad ( 2 ) \quad \text{cts is}$$

in which the ∆ symbol signifies di/uniFB00erence between the product and  reactant  state  contributions.  The  'np'  and  'nr'  are  the number of gas phase molecules in the product state and reactant state, respectively. P is pressure and R is the gas constant. We can also  calculate  product  pressure P p at  an  user  defined temperature T that  will  bring ∆ G = 0.  If  at  some  temperature T , ∆ G without  the RT ln( Q )  term  is  positive,  then P p value must be lowered to bring the reaction to equilibrium and vice versa. A very low value of P p indicates that the corresponding reaction byproducts are less likely at that temperature and vice versa.  Please  note  that  this  analysis  cannot  be  used  to  obtain the product pressure value in Equation (2).

## 4. Results and Discussion

## 4.1. Thermochemistry: Free Energies of Proposed Reactions

Let  us  start  by  discussing  the  thermochemistry  of  the  overall etch cycle and the individual reactant pulses using DFT data. In

<!-- image -->

www.advmatinterfaces.de

Table 1. A list of reactions and computed thermochemistry representing the overall etch process in which 1 solid TiN bulk unit is converted into gas phase products on reacting with 1 NbF5 and 1 CCl4 molecules. R2, R4, and R5 (shown in bold font) are redox reactions. All species other than TiN are in gas phase. P p at ∆ G = 0 is the product pressure at 740 K that will bring the reaction to equilibrium at a constant reactant pressure of  2.5  Torr.  A  low P p value  indicates  the  reaction  products  are  unlikely and vice versa.

|      | Reactions                                                | ∆ G [eV]   | ∆ G [eV]   | P p [Torr]            |
|------|----------------------------------------------------------|------------|------------|-----------------------|
|      | Reactions                                                | 640 K      | 740 K      | at ∆ G = 0; T = 740 K |
| R1:  | 1 TiN + 1 NbF 5 + 1 CCl 4 → 1 TiCl 3 + 1 NbNFCl + 1 CF 4 | 2.8        | 2.5        | 7.3E - 14             |
| R2 : | 1 TiN + 1 NbF 5 + 1 CCl 4 → 1 TiCl 4 + 1 NbNF + 1 CF 4   | 3.3        | 2.9        | 1.5E - 15             |
| R3:  | 1 TiN + 1 NbF 5 + 1 CCl 4 → 1 TiCl 3 + 1 NbClF 4 + 1 CNF | - 1.2      | - 1.6      | 3.8E + 00             |
| R4 : | 1 TiN + 1 NbF 5 + 1 CCl 4 → 1 TiCl 4 + 1 NbF 4 + 1 CNF   | - 0.8      | - 1.2      | 1.4E - 01             |
| R5 : | 1 TiN + 1 NbF 5 + 1 CCl 4 → 1 TiF 4 + 1 NbFCl 3 + 1 ClCN | - 2.7      | - 3.1      | 3.8E + 05             |

Table 1 we show the reaction free energies for a number of reactions postulated for the overall etch cycle considering a reactant pressure of 2.5 Torr and a product pressure of 0.01 Torr. Please note that the product pressure cannot be controlled in an etch reactor  and  it  is  typically  much  lower  than  the  reactant  pressure, so we choose a value of 0.01 Torr for our calculations.

In reactions R1-R5, we consider a unit of bulk TiN reacting simultaneously with 1 NbF5 and 1 CCl4 molecules to form different  gas  phase  products.  It  is  to  be  noted  that  Nb  can  take di/uniFB00erent oxidation states and thus there are very many possible combinations  of  volatile  products.  Since  it  is  not  practical  to consider  all  of  them,  we  have  computed  a  small  set  of  representative product combinations.

The  reactions  R2,  R4,  and  R5  (with  labels  in  bold  font  in Table 1) are redox reactions in which the Ti atoms are oxidized and  Nb  atoms  are  reduced.  The  production  of  gaseous  products  is  often  entropically  favored  and  therefore  the  reaction free energies decrease as the temperature is increased to 740 K (467 ° C), with R5 being the most favorable at ∆ G = -3.1 eV. R3 and R4 become favorable at 740 K although not as favorable as R5. At 640 K (367 ° C),  the  favorable  reactions  are  R3,  R4,  R5, and R9. R1 and R2 are more unlikely compared to R3 and R4 not because of the Ti compound but because of the Nb and C compounds. From the reaction energies, Nb-N compounds are found to be less favorable in gas phase when compared to C-N compounds. For a similar reason, R3 and R4 are more favorable than R1 and R2, respectively, although both reactions in each set form the same Ti compound. R5 is the most favorable, because it results in a C-N compound and TiF4, which is a well-known volatile  and  stable  gas  molecule.  The  TiF   as  a  byproduct  was 3 not considered due to its high boiling point of 1400 ° C [31] and nonvolatility, [31,46] especially  within  the  experimented  temperature range, that is, 370-460 ° C.

Even at 740 K, the calculations show that reactions R1 and R2 are not favorable as the change in Gibbs free energy is + 2.5 and + 2.9 eV, respectively. The product pressure evaluated at ∆ G = 0 and 740 K gives an indication of the likelihood of the formation of the considered reaction products. This value is very small for

<!-- image -->

www.advancedsciencenews.com

Table 2. Potential reactions of individual reagent pulses with bulk TiN in the etch process, assessed via thermochemistry computed with DFT. R6-R8 represent the fluorination pulse and R9 represents the chlorination pulse. Pp at ∆ G = 0 is the product pressure at 740 K that will bring the reaction to equilibrium at a constant reactant pressure of 2.5 Torr. A low P p value indicates the reaction products are unlikely and vice versa.

|      | Reactions                            | ∆ G [eV]   | ∆ G [eV]   | P p [Torr]            |
|------|--------------------------------------|------------|------------|-----------------------|
|      | Reactions                            | 640 K      | 740 K      | at ∆ G = 0; T = 740 K |
| R6 : | 1 TiN + 1 NbF 5 → 1 TiNF + 1 NbF 4   | 6.1        | 5.7        | 7.3E - 24             |
| R7:  | 1 TiN + 1 NbF 5 → 1 TiF 3 + 1 NbNF 2 | 3.5        | 3.1        | 4.2E - 15             |
| R8:  | 1 TiN + 1 NbF 5 → 1 TiF 4 + 1 NbNF   | 3.9        | 3.5        | 2.5E - 16             |
| R9:  | 1 TiN + 1 CCl 4 → 1 TiCl 3 + 1 ClCN  | - 2        | - 2.4      | 1.8E + 04             |

R1 and R2 suggesting that NbNF/Cl and CF4 are not very probable  products.  On  the  other  hand,  a  high  product  pressure  at ∆ G = 0  and  740  K  is  registered  for  reaction  R5  indicating  an increased  likelihood  in  the  formation  of  the  volatile  products TiF4 , NbFCl 3 , and ClCN, hence the etching.

The reactions where N2 is an etch product were also considered, and are as follows: 2 TiN(s) + 6  NbF (g) 5 + 6  CCl (g) 4 → 6 NbFCl3(g) + N 2 (g) + 2  TiCl (g) 3 + 6  CF (g),  and  2  TiN(s) 4 + 8 NbF5(g) + 8 CCl 4 (g) → 8 NbFCl3(g) + N2(g) + 2 TiCl (g) 4 + 8 CF4 (g). Both the reactions are highly endothermic and unfavorable even at 500 K with reaction energies of 9.5 and 8.5 eV, respectively.

In Table 2 , we consider representative etch reactions (R6-R9) in  the  individual  pulses  when  either  NbF   or  CCl   is  used  as 5 4 reactant.  The  fluorination  pulse  is  presented  as  reactions  R6R8, in which NbF5 may interact with TiN and form gas phase TiF   and  NbNF   species.  The  reaction  free  energies  are  very x y high ( + 3.1 to + 5.7 eV at 740 K). The product pressure at ∆ G = 0 and 740 K is correspondingly very small. This indicates that etch reactions are not possible when pulsing only NbF 5  mainly due  to  the  unfavorable  Nb-N  compounds.  The  adsorption mechanism  of  NbF5  on  the  TiN  surface  has  been  computed and  is  described  in  Section  S1,  Supporting  Information.  We find  that  NbF 5 dissociates  on  the  TiN(211)  surface  spontaneously  at  400  K  and  results  in  the  formation  of  strong  surface bound Ti-F and Nb-N bonds (see Section S1, Supporting Information).  Thermodynamically,  the  Ti-F  bonds  on  TiN  surface are more stable and favorable when compared to Ti-Cl bonds (see Section S3, Supporting Information). The formation of any gas phase byproducts was not observed from the DFT simulations of the fluorination pulse.

Reaction R9 shows the TiN etch reaction by CCl 4  and a spontaneous  etching  at  640  and  740  K,  as  evidenced  by  the  negative free energy change, is observed. The preferred products are TiCl3   and  ClCN.  Expressed  in  another  way,  the  product  pressure at ∆ G = 0  and  740  K  is  very  large.  From  simulations, we also  found  that  CCl 4 molecule  dissociated  spontaneously  on TiN(211) surface (see Section S2, Supporting Information).

Thus,  the  first  principles  thermochemistry  suggests  that the  NbF5   pulse  could  not  etch  (TiN)  by  itself,  while  the  CCl 4 pulse  alone  could  etch  (TiN)  spontaneously,  however  subject to  kinetic  barriers.  Comparing  R5  and  R9,  the  combination of (NbF5) and (CCl4) pulses at 740 K is predicted to give more e/uniFB00ective etching  of  TiN  than  etching  by  CCl 4 alone.  The  C compound in the two reactions is the same ClCN and the Ti

<!-- image -->

www.advmatinterfaces.de compounds TiCl3 and TiF4 have very similar thermochemistry as  well.  However,  NbFCl 3 o/uniFB00ers  lower  zero  point  energy  and higher  entropy  than  NbF 5   which  allowed  R5  to  have  a  lower reaction free energy than R9.

From  simulations,  a  CCl 4   is  found  to  dissociate  spontaneously  at  a  surface  bound  fluorine  free  Nb  site-which  is  the precursor  for  the  formation  of  NbF Cl   species  in  R9.  Please x y refer to Section S2, Supporting Information of the Supporting Information  for  more  information  on  the  explicit  reaction mechanisms that have been computed with DFT for this etch process.  This  enhanced  etching  phenomenon  with  sequential pulses of NbF5 and CCl4 is experimentally verified and observed in Figures 2 and 3.

## 4.2. Experimental Etching Characteristics

TiN  films  were  etched  by  two  types  of  etch  processes:  1)  a binary process that involves alternating exposures of NbF 5  and CCl4 reactants in a cyclic manner and 2) a pulsing CCl 4  alone in a chemical vapor etching (CVE) or GPPE process. One cycle of pulsed CVE of TiN films consists of a CCl4 exposure followed by  an  inert  gas  (N )  purge.  The  N   purges  were  introduced 2 2 to  ensure  the  products  and  excess  precursor  molecules  were removed properly from the etch system.

In this context, an etch system is an aggregate term used to describe all  the  components such as gas lines, valves and the reaction  chamber  and  its  parts.  The  concept  and  feasibility studies performed under this section demonstrate TiN etching in  the  atomic  regime.  The  CCl 4 based  CVE  process  provides selectivity over Al O 3 2 , SiO 2 , and Si 3 N4. However, the NbF5-CCl4 based etch process is able to etch Al 2 O 3 and provides selectivity over SiO2 and Si 3 N 4 . [39]

Figure 1 shows  a  change  in  the  TiN  EPC  with  varying  NbF 5 pulse time for the NbF 5 -CCl 4 etch process at 460 ° C and 1 s long CCl4  pulse  time.  The  etch  temperature  of  460 ° C  was  chosen

Figure 1. Etch per cycle for TiN films versus NbF 5  pulse time at 460 ° C. The  duration  of  N 2 purges  and  CCl 4 pulses  were  fixed  at  6  and  1  s, respectively.

<!-- image -->

<!-- image -->

www.advancedsciencenews.com

Figure 2. Etch  per  cycle  of  TiN  films  with  varying  CCl   pulse  time  at 4 460 ° C. 6 s long N2  purges were used. The figure compares the EPC for the binary process (red) to the CVE process (blue).

<!-- image -->

because  it  was  limited  by  the  hardware.  The  figure  reveals  that when no NbF5 is used, an EPC of 0.3 Å is obtained which indicates that CCl 4 alone is capable of etching TiN films as will be discussed later. This is consistent with the favorable thermochemistry that is predicted with DFT. The EPC increases from 0.3 to about 0.6 Å when the NbF5 pulse time is varied from 0 to 1 s. At 3 s NbF 5 pulse time an EPC of about 0.8 Å is measured. There is no clear saturation of EPC with the NbF 5  pulse time, but a marginal slowing of an EPC is observed. We speculate that this nonsaturated behavior can be attributed to various factors such as partially self-limiting nature  of  the  surface  reaction,  insu/uniFB03cient  purge  time,  low  volatility ,  or  otherwise  slow  removal  of  the  products  from  the  TiN surface and presence of finite vapors of CCl 4  in the etch system. This soft-saturation of the EPC with NbF 5  pulse time can also be assigned to a slow di/uniFB00usion of F species through grain boundaries to form a converted TiN surface and form fluorinated TiN surface.

In Figure 2 EPCs for two etch processes are plotted against CCl4  pulse  time  at  an  etch  temperature  of  460 ° C.  From  the graph,  it  is  worth  noticing  that  the  EPC  for  the  NbF -CCl 5 4 etch process is higher than that for the CCl 4  only CVE process. This holds true for a given set of process parameters such as gas flows, partial pressure of both the precursors, the pulse and purge times up to 3 and 6 s, respectively, and total pressure of the reaction chamber.

The  earlier  presented  first  principles  simulations  also  predicted a more favorable etch reaction for the NbF 5 -CCl 4  process than for CCl4 only. For both etch processes, the EPC tends to increase with the CCl 4  pulse time.

Figure 2 shows that no etching was observed when 0.5 s of NbF5  and  no  CCl 4   was  used,  for  total  300  cycles.  No  change in the TiN thickness was observed even after 300 cycles of 1 s NbF5 pulse. At temperatures below 460  C, NbF5 alone was not ° able to etch TiN by itself. This is consistent with the first principles  simulations.  The  TiN  thickness  values  before  and  after NbF5 exposure were confirmed by XRR measurements.

<!-- image -->

www.advmatinterfaces.de

For  both  etch  processes,  no  clear  saturation  of  EPC  is observed.  The  EPC  continues  to  increase  linearly  with  CCl 4 pulse time from 0.5-3.0 s, with no sign of saturation. At 3 s long CCl4 pulse time, EPC values of about 0.8 and 0.5 Å are observed for  the  NbF -CCl 4 5 and  CCl   only  CVE  processes,  respectively. 4 NbF5 enhances the etch rate of TiN and this could be due to an enhanced reactivity of the CCl 4  with fluorinated TiN surface or the formation of more volatile species such as TiCl 4  (R5 in Table 1) instead of TiCl 3 , [47] TiOCl, or TiF 3 . The TiCl  at 427 3 ° C, has  a  su/uniFB03ciently  high  vapor  pressure  of  37  mTorr. [48] On  the contrary, TiF 3 has a very high boiling point of 1400 ° C [31] and is nonvolatile. [31,46] The vapor pressures of TiCl 4  and TiF 4  at 90 ° C are 190 Torr [49] and 18 mTorr, [50] respectively.

Another possible reason for the faster etching could be fluorine  species  di/uniFB00using  through  the  TiN  grain  boundaries  and therefore  the  etching  may  proceed  three  dimensionally  rather than  being  limited  to  the  surface.  Later  in  Figure  7,  the  XPS depth profile analysis did show some fluorine penetration into the  remaining  TiN  film,  after  exposing  it  to  the  NbF -CCl 4 5 CVE process.

The simulation results provided in the Supporting Information  (see  Section  S2,  Supporting  Information)  reveal  that  the Nb sites are important for CCl 4  to react with when the rest of the  surface  is  covered  with  F.  It  is  found  that  the  a  favorable binding between the Cl atoms and Nb atom is possible (more details  in  the  Section  S2,  Supporting Information) even when the Nb atom is weakly bound to 2 F atoms. However, a strong dissociative  adsorption of CCl 4   ( -3.2  eV)  is  possible  when  the Nb  atom  is  free  of  Nb-F  bonds  (see  Figure  S5b,  Supporting Information)  in  the  Supporting  Information).  Based  on  the computational  results,  we  propose  that  the  ALE  of  TiN  proceeds by self-limiting reaction of NbF 5  molecules with TiN surface in the first pulse (see Section S1, Supporting Information) followed by the dissociative adsorption of CCl 4  catalyzed by the Nb sites in the second pulse leading to the etch of TiN. Additionally, from the two it can be seen that the NbF 5  alone did not etch TiN and is predicted by the computational results.

In Figure 3 , the e/uniFB00ect of etch temperature on etch per cycle is  captured  for  the  both  etch  processes.  The  NbF   and  CCl 5 4 pulse times were set to 1 s with 6 s long N 2  purges. For the data points in this graph, a total of 200, 200, 300, and 400 etch cycles were  performed  at  etch  temperatures  of  370,  380,  400,  and 460  C, respectively. For the NbF 5 -CCl 4 ° etch process, a low EPC of 0.03 Å per cycle at 370 ° C is obtained and the EPC increases almost linearly to about 0.4 Å per cycle at 400 ° C. At 460 ° C, a higher  etch  rate  of  0.55  Å  per  cycle  is  noted.  In  contrast,  the CCl4 only etch process shows an etch rate of 0.07 Å per cycle at 370 ° C and linearly increases to about 0.3 Å per cycle at 460 ° C. Both the etch processes were unable to etch TiN significantly at temperatures below 370 ° C, even after total 1000 etch cycles. This  is  in  disagreement  with  DFT  thermochemistry  predictions, which shows possible etching at 500 K (227 ° C) and the reason for this can be due to higher activation barrier.

## 4.3. Etch Selectivity

Etch  selectivity  of  TiN  against  di/uniFB00erent materials  such  as Al2 O 3 ,  SiO ,  and  Si N   was  also  studied  for  the  reported  etch 2 3 4

<!-- image -->

www.advancedsciencenews.com

Figure 3. E/uniFB00ect of etch temperature on etch per cycle for the binary process (blue curve) as well as CCl 4   alone  (blue  curve)  process.  Both  the precursor pulses and the purge times were fixed to 1 and 6 s, respectively.

<!-- image -->

processes. Figure 4 investigates  the  ability  of  the  CCl   alone 4 CVE process to etch TiN selectively over Al 2 O 3 , SiO , and Si N 4 2 3 at  460 ° C. The figure plots the etched thickness with the total number of etch cycles, where each cycle consisted of 1 s long CCl4  pulse  followed  by  6  s  long  N   purge.  EPC  of  0.3  Å  per 2 cycle is deduced from a linear fit. After 500 etch cycles, about 13 nm TiN film is removed. No change in thickness is observed for  Al O 3 2 ,  SiO ,  and  Si N   even  after  exposing  them  to  1000 2 3 4 cycles of 1 s long CCl 4 pulses. Moreover, at temperatures below 460 ° C, CCl4 is unable to etch Al 2 O3, SiO2, and Si 3 N4 either and therefore  the  selective  etching  of  TiN  is  possible  within  temperature window of 370-460  C. °

<!-- image -->

Figure 4. A  change  in  the  thickness  values  with  total  number  of  etch cycles at 460 ° C for TiN, SiO 2 , Al 2 O3, and Si 3 N4 films. A TiN is selectively etched away by CCl4 alone over other materials.

<!-- image -->

## www.advmatinterfaces.de

Figure 5. An X-ray photoelectron spectroscopy of SiO 2  surface after complete removal of TiN film by CCl 4  based CVE process at 460 ° C.

<!-- image -->

## 4.4. Post-Etch Analysis

After removing all 25 nm TiN film from the SiO2 substrate, an ex situ XPS spectra of the post-etch surface was measured and is shown in Figure 5 .  The main constituents of the remaining surface  were  32.7  at%  Si,  60.9  at%  O,  5.1  at%  C,  and  1.2  at% of N, as revealed by XPS. Both the titanium and chlorine were below the detection limit of the XPS ( &lt; 0.1 at%). The TiN film was  etched  at  460 ° C  by  600  CVE  'cycles,'  where  each  etch cycle  was  comprised  of  3  s  long  CCl   pulse  followed  by  6  s 4 long N2 purge. After 600 etch cycles, about 30 nm TiN film was anticipated to have been etched. Keeping real etch applications in  mind,  this  over-etch  condition  was  deliberately  chosen  to remove any TiN remnants from the SiO2 surface. Moreover, it was important to study possible surface contamination arising from the etch process itself. The XPS analysis in Figure 5 suggests  that  the  surface  is  mostly  composed  of  silicon,  oxygen, and  some  adventitious  carbon.  In  addition,  about  1.2  at% nitrogen is seen. Titanium and chlorine were not detected. The detection limit of the particular XPS used here is 0.1 at%. The nitrogen and carbon signals were detected around 399.1 eV ( ± 0.1 eV) and 284.8 eV ( ± 0.2 eV), respectively, and are most probably due to organic surface contamination. Hence they can be associated  with  handling,  storage  and  transportation  of  samples within non clean-room environment. The unetched silicon dioxide substrate shows no damage and matches with reference thermal SiO2 films.

The same sample from the Figure 5 was subjected to a crosssectional  bright  field  transmission  electron  microscopy  (BFTEM). The BF-TEM images shown in Figure 6 reveal that TiN was completely removed from the SiO2 surface by the CCl4-only etch  process.  Spin-on  carbon  was  deposited  prior  to  the  TEM imaging  for  highlighting  the  material  contrast.  The  unetched sample  is  shown  for  reference  and  was  not  exactly  the  same sample. The TEM image depicts that after complete removal of the TiN film from the SiO2 surface, the surface appears to be clean and free of any surface contaminants from either the TiN film or the etch process.

<!-- image -->

www.advancedsciencenews.com

Figure 6. BF-TEM images of a) the reference unetched 25 nm TiN film on 22 nm SiO2 film, b) after complete etching of 25 nm TiN film by 600 cycles of each 3 s long CCl 4 pulse separated by 6 s of N 2  purges.

<!-- image -->

Figure 7 plots an XPS depth profile of the elements found in an about 9 nm TiN film remaining when the etch process was incomplete. The TiN film was etched by 300 cycles of the NbF5-CCl4  etch  process  at  460 ° C.  The  total  of  60  s  sputter time is estimated to etch about 1.8 nm of the TiN film. From the  figure  it  can  be  seen  that  the  surface  contains  about 26  at%  carbon,  31  at%  oxygen,  20  at%  nitrogen,  15  at%  titanium, and about 5 at% niobium. In addition, small amounts of silicon and fluorine were also detected with both being below 2 at%. The silicon signal is from the SiO 2  film underneath the TiN film. After 15 s of argon ion sputtering, the carbon signal is dropped to about 4 at% and goes further down to 3 at% after 1  min  of  sputtering.  The  atomic  percentages  for  titanium,

<!-- image -->

Figure 7. An XPS depth profiling through remaining TiN film after partial etching at 460  C. Total 300 cycles were performed with 0.5 s of both NbF 5 ° and CCl4 pulse lengths with 6 s of N 2  purges.

<!-- image -->

www.advmatinterfaces.de nitrogen,  and  oxygen  are  observed  around  24,  32,  and  28 respectively after sputtering the surface for 15 s. A fairly high niobium amount from 5 to 6 at% along with fluorine of about 0.9-1.7  at%  may  indicate  that  the  NbF 5 is  capable  of  either reacting  or  dissociating  on  TiN  or  the  TiN  surface  modified by CCl4. The presence of niobium is evidently consistent with the  DFT  adsorption  studies  discussed  in  Section  S1,  Supporting Information. After sputtering for a minute, the presence of significant amounts of niobium, fluorine and carbon inside the top layer of the TiN films may be attributed to various reasons such as surface di/uniFB00usion of the elements at etch temperatures preferentially through TiN grain boundaries, or increased surface area due to preferential etching along grain boundaries.  They  can  also  result  from  energetic  argon  ions bombarding the atoms deeper into  the  film.  The  absence  of chlorine on or in the post-etch TiN layer points toward the formation of volatile products containing chlorine such as TiCl 3 , TiCl4 ,  NbFCl 3 ,  NbClF 4 ,  and  ClCN.  All  these  compounds  are predicted by the DFT simulation results.

Figure 8 is a series of TEM images taken from 3D horizontal FIN structures.  For  a  reference,  schematic  1  provides  an  idea of such a 3D structure where the blue horizontal fins are SiO 2 fins and the black back-bone is silicon. This 3D structure was coated by a thin ALD TiN film [35]  with extremely high conformality.  One big advantage of gas-phase chemical etching over plasma-based  etching  is  its  capability  to  etch  material  from non-line-of-sight  features  of  this  sort.  Another  advantage  can be maintaining conformality during the etching or thinning of the  films.  However,  the  non-self-limiting  gas-phase  chemical etching  reactions  can  also  a/uniFB00ect  the  conformality.  In  order  to improve  the  etch  conformality,  another  etchant  or  controlreactant  can  be  introduced  to  either  improve  conformality  or modify  the  etch  rate  such  that  etching  from  non-line-of-sight features may follow more uniform removal.

In  Figure  8a,  a  reference  SiO   fin  structure  is  covered  by 2 on average 3.3 nm pristine TiN film. The goal of this etching test  was to observe the etch conformality and isotropic nature of  the  binary  NbF -CCl 4 5 etch  process.  The  same  sample  was subjected to the binary etch process and from Figure 8b it can be concluded that after removal of about 0.8 nm of TiN conformally, no significant increase in the surface defects is observed. After applying over-etch the TiN is removed completely as seen in Figure 8c. From these TEM images, no etching of SiO2 fins was observed, thus confirming the selectivity.

## 5. Summary

We  successfully  demonstrated  two  novel  gas-phase  etching processes  for  titanium  nitride.  The  binary  etching  process  is based  on  alternate  exposures  of  NbF 5 -CCl 4 ,  each  separated by N2 purge. The chemical vapor etch (CVE) etch process utilizes  CCl   exposures  alone  in  a  pulsed  fashion.  In  addition, 4 the  selective  etching  of  TiN  with  respect  to  SiO ,  Si N ,  and 2 3 4 Al2 O 3 was  also demonstrated.  Furthermore,  the  gas-phase etching reported here also exhibits nondirectional etching from non-line-of-sight features.

From the first  principles  based  DFT  thermochemistry  simulations  the  possible  reactions  and  the  candidate  products

<!-- image -->

## www.advancedsciencenews.com

<!-- image -->

www.advmatinterfaces.de

Figure 8. Cross-sectional bright field transmission electron micrograph (BF-TEM) of 3D structures: a) about 3.3 nm TiN film deposited on SiO 2  fins with lateral cavities, b) the same after about 0.8 nm TiN is etched by the NbF 5 -CCl 4  etch-process, and c) after removing the TiN film completely. The etching was performed at 460  C. °

<!-- image -->

involved in TiN etching were assessed. The surface etch mechanism is also presented in the Supporting Information.

In a two-step etch process, the DFT MD studies predict that the NbF5 is able to fluorinate the TiN surface but is unable to etch it by itself. This non-etching is attributed to the formation NbNF  species that are di/uniFB03cult to desorb from the surface. In x corroboration  with  this,  the  presence  of  Nb  and  F  on  surface was confirmed by XPS in Figure 7 .

However, the simulations predict that in NbF 5 -CCl 4  etch process,  NbF 5 could  enhance  the  etch  rate  (favorable  reaction  free energy compared to CCl 4  only process) and this was experimentally verified. The Ti-F bonds are stronger and highly polar when compared to Ti-Cl bonds. [51] Thus,  in  comparison  to  Cl  covered  TiN surfaces, F covered TiN surfaces are more favorable for etching.

In the etching step, the CCl 4  has a tendency to chlorinate the Ti-F bonds and Nb atoms on the surface via halide-exchange mechanism [52]   and  hence  fluorinated  TiN  and  surface  Nb  as well as N atoms are etched by CCl4  in the form of volatile compounds such as TiF4, NbFCl3, ClCN, and TiCl4.

For the NbF5-CCl4 etch process, the EPC varied from 0.03 Å at 370 ° C to a higher value of 0.55 Å at 460 ° C. It was found that the  EPC  at  460 ° C  increases  with  an  increase  in  either  NbF 5 or CCl4 pulse durations and a no clear self-limiting behavior is observed for either of the pulse durations.

Consistent  with  the  simulation  results,  experiments  found that CCl4  is able to etch TiN spontaneously in a CVE fashion. The  formation  of  volatile  species  such  as  TiCl   and  ClCN  is 3 predicted  by  the  thermochemical  studies.  The  CCl 4 -only  CVE process shows an EPC of about 0.07Å per cycle at 370 ° C, linearly increasing to about 0.3Å per cycle at 460 ° C. At 460 ° C, for a  given  pulse  duration,  the  TiN  removal  proceeds  in  a  linear fashion with etch exposures.

After  a  complete  removal  of  titanium  nitride  film  by  CCl , 4 the XPS as well as TEM analysis revealed a SiO2 surface with no significant amounts of residues arising either from the etch process or the TiN film itself.  In  case  of  incomplete  removal of  TiN  by  the  NbF -CCl 4 5 process,  XPS  showed  the  presence of  niobium  and  fluorine  on  the  remaining  TiN  film.  The absence of chlorine on the surface suggests e/uniFB00ective formation of  volatile  species  containing  chlorine,  as  predicted  by  the simulations. The TEM images verify uniform, conformal thinning,  leading  eventually  to  complete  removal  of  TiN  from 3D structures.

## Supporting Information

Supporting  Information  is  available  from  the  Wiley  Online  Library  or from the author.

## Acknowledgements

The authors thank Eurofins EAG Materials Science, LLC (California, USA) for the TEM analysis. S.K.N. thanks ICHEC and the Science Foundation Ireland funded  computing  center  of  Tyndall  National  Institute  for computer  time.  S.K.N.  thanks  Rita  Mullins  for  help  with  reaction  free energy calculations.

## Conflict of Interest

The authors declare no conflict of interest.

## Data Availability Statement

Research data are not shared.

## Keywords

atomic layer etching, density functional theory, thermal etching

Received: June 28, 2021

Revised: September 26, 2021

Published online: October 22, 2021

[1]  A. Busnaina, Nanomanufacturing Handbook , 1 ed., CRC Press/Taylor &amp; Francis, Boca Raton, FL 2007 .

[2]  J. Meena, S. Sze, U. Chand, T.-Y. Tseng, Nanoscale Res. Lett. 2014 , 9 , 526.

<!-- image -->

www.advancedsciencenews.com

- [3]  M. Ritala, J. Niinistö, ECS Trans. 2019 , 25 , 641.
- [4]  C.  T.  Carver,  J.  J.  Plombon,  P.  E.  Romero,  S.  Suri,  T.  A.  Tronic, R. B. Turkot, Solid State Sci. Technol. 2015 , 4 , N5005.
- [5]  G. Oehrlein, D. Metzler, C. Li, ECS J. Solid State Sci. Technol. 2015 , 4 , N5041.
- [6]  K.  J.  Kanarik,  T .  Lill,  E.  A.  Hudson,  S.  Sriraman,  S.  Tan,  J.  Marks, V. Vahedi, R. A. Gottscho, J. Vac. Sci. Technol. A 2015 , 33 , 020802.
- [7]  E. Marin, A. Lanzutti, F. Andreatta, M. Lekka, L. Guzman, L. Fedrizzi, Corros. Rev. 2011 , 29 , 191.
- [8]  V. Miikkulainen, M. Leskelä, M. Ritala, R. L. Puurunen, J. Appl. Phys. 2013 , 113 , 021301.
- [9]  P. O. Oviroh, R. Akbarzadeh, D. Pan, R. A. M. Coetzee, T.-C. Jen, Sci. Technol. Adv. Mater. 2019 , 20 , 465.
- [10]  S. M. George, Acc. Chem. Res. 2020 .
- [11]  C. Fang, Y . Cao, D. Wu, A. Li, Prog. Nat. Sci. 2018 , 28 , 667.
- [12]  Y . Lee, S. M. George, ACS Nano 2015 , 9 , 2061.
- [13]  H.  Dadgour,  K.  Endo,  V.  De,  K.  Banerjee, IEEE  Trans.  Electron. Devices 2010 , 57 , 2504.
- [14]  L. Lü, Wei-Feng; Dai, Microelectron. J. 2019 , 84 , 54.
- [15]  K.  Matsuura, M. Hamada, T. Hamada, H. Tanigawa, T. Sakamoto, A. Hori, I. Muneta,  T. Kawanago,  K.  Kakushima,  K.  Tsutsui, A. Ogura, H. Wakabayashi, Jpn. J. Appl. Phys. 2020 , 59 , 080906.
- [16]  H. Kim, J.  Vac. Sci. Technol. B Microelectron. and Nanometer Struct. 2003 , 21 , 2231.
- [17]  M.  Darnon,  T.  Chevolleau,  D.  Eon,  L.  Vallier,  J.  Torres,  O.  Joubert, J. Vac.  Sci.  Technol.  B:  Microelectron.  Nanometer  Struct.-Process., Meas., Phenom. 2006 , 24 , 2262.
- [18]  S. C. Abraham, J. Vac. Sci. Technol. A Vac. Surf. Films 1997 , 15 , 702.
- [19]  S. DeVries, E. A. De Silva, D. Canaperi, A. Simon, A. A. de la Pena, W. Wang, J. Maniscalco, L. Meli, B. Mendoza, in 31st Annual SEMI Advanced  Semiconductor  Manufacturing  Conference  (ASMC) ,  IEEE, Piscataway, NJ 2020 , pp. 1-5.
- [20]  S. L. Shinde, S. Ishii, T . Nagao, ACS Appl. Mater. Interfaces 2019 , 11 , 21965.
- [21]  J. Gosciniak, F. B. Atar, B. Corbett, M. Rasras, ACS Omega 2019 .
- [22]  F. Mehmood, R. Pachter, N. R. Murphy, W. E. Johnson, J. Appl. Phys. 2015 , 118 , 195302.
- [23]  P. Patsalas, N. Kalfagiannis, S. Kassavetis, Materials 2015 , 8 , 3128.
- [24]  E.  I.  Cooper,  R.  Rajaram,  M.  Payne,  S.  Lippy, Solid  State  Phenom. 2012 , 195 , 143.
- [25]  Y .  Liu,  T .  Kamei,  K.  Endo,  S.  O'uchi,  J.  Tsukada,  H.  Yamauchi, T.  Hayashida,  Y .  Ishikawa,  T.  Matsukawa,  K.  Sakamoto,  A.  Ogura, M. Masahara, Jpn. J. Appl. Phys. 2010 , 49 , 06GH18.
- [26]  D. Bhattacharyya, S. Kuchibhatla, A. Sehgal, Y. P. Shen, W. Haiting, J.  Prasad,  in 26th  Annual  SEMI  Advanced  Semiconductor  Manufacturing Conference (ASMC) , IEEE, Piscataway, NJ 2015 , pp. 305-308.
- [27]  J. Tonotani, T. Iwamoto, F. Sato, K. Hattori, S. Ohmi, H. Iwai, J. Vac. Sci.  Technol.,  B:  Microelectron.  Nanometer  Struct.-Process.,  Meas., Phenom. 2003 , 21 , 2163.

<!-- image -->

www.advmatinterfaces.de

- [28]  Y .-Y .  Wang,  Y .-H.  Joo,  C.-I.  Kim, J.  Nanosci.  Nanotechnol. 2016 , 16 , 12933.
- [29]  N. Marchack, J. M. Papalia, S. Engelmann, E. A. Joseph, J. Vac. Sci. Technol. Vac. Surf. Films 2017 , 35 , 05C314.
- [30]  K.  Shinoda,  N.  Miyoshi,  H.  Kobayashi,  M.  Izawa,  K.  Ishikawa, M. Hori, J. Phys. D: Appl. Phys. 2019 , 52 , 475106.
- [31]  Y . Lee, S. M. George, Chem. Mater. 2017 , 29 , 8202.
- [32]  V.  Sharma,  T.  Blomberg,  S.  Haukka,  S.  Cembella,  M.  E.  Givens, M. Tuominen, R. Odedra, W. Gra/uniFB00, M. Ritala, Appl. Surf. Sci. 2020 , 52 , 148309.
- [33]  G. Dingemans, C. Van Helvoirt, M. Van de Sanden, W. M. Kessels, in ECS Transactions [ECS 219th ECS Meeting - Montreal, QC, Canada (May 1 - May 6, 2011)] - Plasma-Assisted Atomic Layer Deposition of Low Temperature SiO2 , IOP Publishing, Bristol 2011 , pp. 191-204.
- [34]  L.  Gosset,  J.-F.  Damlencourt,  O.  Renault,  D.  Rouchon,  P.  Holliger, A.  Ermolie/uniFB00,  I.  T rimaille,  J.-J.  Ganem,  F.  Martin,  M.-N.  Séméria, J. Non-Cryst. Solids 2002 , 303 , 17.
- [35]  C.  H.  Ahn,  S.  G.  Cho,  H.  J.  Lee,  K.  H.  Park,  S.  H.  Jeong, Metals Mater. Int. 2001 , 7 , 621.
- [36]  J.  V .  Michael, K. P. Lim, S. S. Kumaran, J. H. Kiefer, J.  Phys. Chem. 1993 , 97 , 1914.
- [37]  F.  Huang,  H.  Zhao,  A.  Yan,  Z.  Li,  H.  Liang,  Q.  Gao,  Y .  Qiang, J. Alloys Compd. 2017 , 695 , 489.
- [38]  R. J. M. Konings, Struct. Chem. 1994 , 5 , 9.
- [39]  V.  Sharma,  S.  D.  Elliott,  T.  Blomberg,  S.  Haukka,  M.  E.  Givens, M. Tuominen, M. Ritala, Chem. Mater. 2021 , 33 , 2883.
- [40]  G. Kresse, J. Furthmuller, Phys. Rev. B 1996 , 54 , 11169.
- [41]  G. Kresse, D. Joubert, Phys. Rev. B 1999 , 59 , 1758.
- [42]  J. P. Perdew, K. Burke, M. Ernzerhof, Phys. Rev. Lett. 1996 , 77 , 3865.
- [43]  P. Blochl, Phys. Rev. B 1994 , 50 , 17953.
- [44]  TURBOMOLE V6.2 2010, a development of University of Karlsruhe and  Forschungszentrum  Karlsruhe  GmbH,  1989-2007,  TURBOMOLE GmbH (2010), http://www.turbomole.com (accessed: November 2019).
- [45]  A. Togo, I. Tanaka, Scr. Mater. 2015 , 108 , 1.
- [46]  G. Ramanath,  J. E. Greene, J. R. A. Carlsson, L. H. Allen, V. C. Hornback, D. J. Allman, J. Appl. Phys. 1999 , 85 , 1961.
- [47]  H.  Sekimoto,  Y .  Nose,  T.  Uda,  H.  Sugimura, High  Temp.  Mater. Processes 2011 , 30 , 435.
- [48]  K. Kelley, A. Mah, Metallurgical Thermochemistry of Titanium , Report of investigations/U.S.  Dept.  of  the  Interior,  Bureau  of  Mines, University of Michigan, Ann Arbor, MI 1959 .
- [49]  F. P. Pike, C. T. Foster, J. Chem. Eng. Data 1959 , 4 , 305.
- [50]  E.  H.  Hall,  J.  M.  Blocher,  I.  E.  Campbell, J.  Electrochem. Soc. 1958 , 105 , 275.
- [51]  S. P. Webb, M. S. Gordon, J. Am. Chem. Soc. 1999 , 121 , 2552.
- [52]  G. Evano, A. Nitelet, P. Thilmany, D. F. Dewez, Front. Chem. 2018 , 6 , 114.