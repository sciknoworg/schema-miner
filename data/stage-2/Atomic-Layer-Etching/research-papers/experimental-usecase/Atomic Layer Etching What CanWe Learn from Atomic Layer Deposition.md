## ECS Journal of Solid State Science and Technology

## OPEN ACCESS

## Atomic Layer Etching: What Can We Learn from Atomic Layer Deposition?

To cite this article: T. Faraz et al 2015 ECS J. Solid State Sci. Technol. 4 N5023

View the article online for updates and enhancements.

## Watch Your Electrodes Breathe!

Measure the Electrode Expansion in the Nanometer Range with the ECD-4-nano.

- Battery Test Cell for Dilatometric Analysis (Expansion of Electrodes)
- Capacitive Displacement Sensor (Range 250 pm, Resolution &lt; 5 nm)
- Detect Thickness Changes of the Individual Half Cell or the Full Cell

Temperature Sensor (-20 to 80" C)

<!-- image -->

See Sample Test Results:

<!-- image -->

Download the Data Sheet (PDF):

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

## You may also like

- Electrochemical Atomic Layer Etching (eALE) of Copper - Thermodynamic and Diffusion-Reaction Considerations of the Surface-Limited Sulfidization of Copper Yukun Gong and Rohan Akolkar -
- Challenges of Tailoring Surface Chemistry and Plasma/Surface Interactions to Advance Atomic Layer Etching S. U. Engelmann, R. L. Bruce, M. Nakamura et al. -
- (Invited) Atomic Layer Etching Using Thermal Reactions: Atomic Layer Deposition in Reverse -

Younghee Lee, Jaime W. DuMont and Steven M. George

<!-- image -->

electrochemical test equipment

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

Or contact us directly:

+49 40 79012-734

sales@el-cell.com

WWW.el-cell.com

<!-- image -->

## JSS FOCUS ISSUE ON ATOMIC LAYER ETCHING AND CLEANING

## Atomic Layer Etching: What Can We Learn from Atomic Layer Deposition?

T. Faraz, F. Roozeboom, ∗ H. C. M. Knoops, and W. M. M. Kessels ∗∗ ,z

Department of Applied Physics, Eindhoven University of Technology, 5600 MB Eindhoven, The Netherlands

Current trends in semiconductor device manufacturing impose extremely stringent requirements on nanoscale processing techniques, both in terms of accurately controlling material properties and in terms of precisely controlling nanometer dimensions. To take nanostructuring by dry etching to the next level, there is a fast growing interest in so-called atomic layer etching processes, which are considered the etching counterpart of atomic layer deposition processes. In this article, past research efforts are reviewed and the key defining characteristics of atomic layer etching are identified, such as cyclic step-wise processing, self-limiting surface chemistry, and repeated removal of atomic layers (not necessarily a full monolayer) of the material. Subsequently, further parallels are drawn with the more mature and mainstream technology of atomic layer deposition from which lessons and concepts are extracted that can be beneficial for advancing the field of atomic layer etching.

' The Author(s) 2015. Published by ECS. This is an open access article distributed under the terms of the Creative Commons Attribution Non-Commercial No Derivatives 4.0 License (CC BY-NC-ND, http://creativecommons.org/licenses/by-nc-nd/4.0/), which permits non-commercial reuse, distribution, and reproduction in any medium, provided the original work is not changed in any way and is properly cited. For permission for commercial reuse, please email: oa@electrochem.org. [DOI: 10.1149/2.0051506jss] All rights reserved.

Manuscript submitted January 28, 2015; revised manuscript received March 12, 2015. Published March 24, 2015. This paper is part of the JSS Focus Issue on Atomic Layer Etching and Cleaning.

Since its inception in the late 1950s, the semiconductor industry has shown an unsurpassed and continuous potential to double the number of transistors on logic and memory dies typically every two years. This 2-year pace in scaling was recognized by Gordon Moore as early as in 1965 1 and has been referred to as Moore's Law. The driving business forces for scaling have been twofold: cost efficiency and device performance. Until the early 2000s, traditional optical lithography has enabled the continuous scaling of gate pitch and areal scaling of the planar CMOS units. New strategies were conceived in the International Technology Roadmap for Semiconductors (ITRS) 2 for the next, second era of scaling by using new materials such as strained silicon, gate stacks of highk dielectrics and metals with optimum work function, 3,4 and high-mobility channels of Ge and III-V compound semiconductors. 5 However, these materialsenabled solutions also have a 2D scaling nature and are reaching fundamental limits. Consequently, for both logic and memory devices, the use of the third (vertical) dimension is now being explored, thus introducing the so-called third era of scaling. Here, 3D architectures and low power consumption designs are developed to further increase the areal transistor density, ranging from FinFETs with conducting channels on three sides of a vertical fin structure, to 'gate-allaround' structures, 6,7 multiple transistor stacks in one die (e.g., 3D NAND 8 ) and multiple die-stacks connected by through silicon vias (TSVs). 9

The choice of materials and structures in semiconductor devices will greatly depend on the advancements in processing techniques and equipment. As devices approach single-digit nanometer critical dimensions (CDs), tolerances are required that are on the order of a few atoms. In addition, aspect ratios will become larger and topographies more complicated. The ability to precisely and selectively add and/or remove functional materials at an atomic scale has become imperative. The overall challenge in the processing of semiconductor devices lies therefore, in the accurate control of the material properties as well as in the control of the nanometer dimensions, hence in 'materials control' and 'dimensions control'. This puts a heavy burden on processing techniques such as deposition and etch.

One technique that has been introduced in semiconductor device manufacturing in the past decade as a true enabling technology is atomic layer deposition (ALD). 10,11,12,13 ALD by itself is not a new

∗

Electrochemical Society Fellow.

∗∗

Electrochemical Society Active Member.

technique - it was already developed by Suntola in 1977 14 - but it was not until the late 1990s that the semiconductor community started realizing that ALD could enable dedicated processes to meet the stringent demands on material quality, precise thickness and layer conformality control in future nanoscale device manufacturing. 15 Today, the technique has grown to be an essential technology in semiconductor device mass-manufacturing, especially of FinFET and other devices with elevated 3D topology. Moreover, the processing at low temperatures ( &lt; 150 C) by ALD gained importance (e.g., in nanopatterning) ◦ which has led to the development of energy-enhanced ALD processes such as plasma-enhanced ALD. 16

Initially, ALD served mainly as a method to replace the thermallygrown SiO2 gate oxide in CMOS transistors by thin films of highk oxide materials. Among the vapor phase deposition methods, ALD is the preferred method of choice rather than physical or chemical vapor deposition (PVD and CVD). This is due to its layer-by-layer growth characteristic, its soft nature (no plasma or sputter damage), its conformality on 3D surface topologies, and its low thermal budget (ALD processes are typically limited to temperatures &lt; 500 C). Fur-◦ thermore, the fact that high quality films can be prepared with precise growth control is a key merit of the technique.

ALD is not a continuous process or a continuous process divided into steps (i.e., a pulsed process, see Fig. 1). Instead, ALD is a cyclic process in which film growth takes place by a repetition of cycles with every cycle consisting of several steps. Typically, an ALD cycle consists of four basic steps: two reactant dosing steps that are separated by two purge steps. Thus each ALD cycle can be divided into two halfreactions, i.e., half-reaction A during the first reactant dosing step (for the first reactant the term 'precursor' is often employed) and halfreaction B during the second reactant dosing step (for the second half reaction the term 'co-reactant' is appropriate). In each half-reaction, chemical reactions take place at the surface of the film in such a way that the surface chemistry is self-limiting. Thus half-reactions A and B can contribute to film growth but add at most one atomic layer (defined here as a layer of atoms, not necessarily a full monolayer). Hence, after a full 'AB cycle' with sufficiently long dosing times for the precursor and co-reactant species (i.e., under so-called 'saturation conditions'), the film thickness is increased by a well-defined value representing at most one atomic layer of material independent of the exact dosing times. This well-defined thickness is very repeatable cycle-over-cycle such that the targeted film thickness can be reached very precisely upon careful selection of the required number of ALD cycles. Evidently, the self-limiting surface chemistry is also the reason

Figure 1. Several approaches can be adopted for thin film deposition and etching for vapor phase based techniques. (a) In a continuous process, the process A is started at t = 0 and stopped after the deposited or etched thickness has been reached. In this basic approach, the control of the deposited or etched thickness is limited as the deposited or etched thickness is 'flux-controlled'. Variations in the process conditions easily lead to variations in the flux of species and hence, in the final deposited or etched thickness, both over multiple deposition runs (i.e., wafer-to-wafer) or over the substrate area (i.e., within-wafer). (b) In a pulsed process, the continuous process is basically divided up into pulses and the pulses are repeated until the deposited or etched thickness has been reached. When the pulse length is well-defined, pulsing provides typically additional control over the continuous process but due to the flux-controlled nature similar drawbacks as in the continuous process hold. (c) Atomic layer processes are 'surface-controlled' as they are based on self-limiting surface chemistries during, e.g., two half-reactions (A and B) that make up a full cycle. Every cycle yields a well-defined, fixed thickness that is deposited or etched when the time per cycle for the half-cycles is sufficiently long (i.e., when working in 'saturated conditions'). This means that the thickness of the deposited or etched film can be controlled very accurately by choosing the right number of cycles. This holds when comparing one deposition run to another but it also leads to an excellent uniformity over the full substrate. Ideal atomic layer processes are very independent of variations in timings or process conditions.

<!-- image -->

for the excellent conformality and unparalleled uniformity that can be achieved by ALD.

Since the commercial onset of ALD, many dedicated ALD chemistries and processes have been developed for a growing set of materials. Other embodiments of ALD have also been developed but they all share the same defining characteristics where the processes take place cycle-wise with several steps per cycle and are based on self-limiting surface chemistry. Meanwhile, a large variety of ALD equipment has entered the market, including tools for single-wafer and batch processing, energy-enhanced and plasma-enhanced ALD tools, and more recently, even spatial ALD equipment. 17 These developments have made ALD currently a mainstream technology for creating uniform and conformal nanomaterials and nanostructures with atomic scale accuracy.

Next-generation nanoscale devices will also require precise material removal or 'etching'. In the past 40 years Moore's Law could be continued by the numerous developments in plasma etching with continuously higher levels of dimensional control. Several of such developments have, for example, been enabled by approaches relying on pulsed operation, i.e., by time-modulation of the power, gas flows or bias voltages. 18 Yet, every new technology node imposes new challenges in selectivity, plasma damage, aspect-ratio-dependent etching (ARDE)andline-edge roughness (LER). 18,19 These challenges related to current dry etching techniques provide a window of opportunity for being potentially tackled by an atomic scale etching method analogous to ALD known as atomic layer etching (here abbreviated as 'ALEt', see also below). Although several efforts have been undertaken to develop layer-by-layer methods with precise etch control similar to its ALDcounterpart, the development of ALEt has comparatively lagged behind.

In this article, the efforts with respect to ALEt will be first briefly reviewed (The early days of atomic layer etching section). Next, an attempt is made to identify the key aspects of ALEt as well as its potential to become a novel technology option for producing singledigit nanometer critical dimensions (What can we learn from ALD? section). This will be done by highlighting the cues it can take from the strengths and successes of its counterpart ALD process. Finally, the conclusions and a brief future outlook are presented (Conclusions section).

## The Early Days of Atomic Layer Etching

The concept of removing a single atomic layer from the surface of a solid was first claimed in a patent by Yoder in 1988 where he outlined a method for 'atomic layer etching' of crystalline diamond. 20 In this patent, a cyclic process was described in which every cycle consisted of four steps [see Fig. 2a]: the diamond surface is flooded with NO2 in the first step and with excited ions in step 3. Steps 2 and 4 are purge steps. Since then, a large set of publications has appeared in scientific literature and the method has come to be known by a variety of other names, namely digital etching, 21 layer-by-layer etching, 22 molecular-layer etching, 23 plasma atomic layer etching (PALE), 24 etc. Yet, the original name of 'atomic layer etching' coined in the first patent has remained most popular. The acronym 'ALEt' 25 has often been used to distinguish the method from the abbreviation of atomic layer epitaxy (ALE), 10 the latter being used to identify atomic layer deposition processes before the term atomic layer deposition (with acronym 'ALD') gained widespread adoption. 15

Experimental efforts aimed at realizing ALEt, commenced with the work of Maki et al. for GaAs 26 in 1989. They outlined a process, referred to as 'atomic bilayer etching', where the exposure of a GaAs substrate to molecular chlorine led to a self-terminating spontaneous adsorption of the gas on the substrate surface producing a weakly bound surface chloride layer. A subsequent exposure of this

(a)

(2)

<!-- image -->

(3)

Figure 2. (a) Schematic from Yoder's early patent in 1988 showing the layout of the cycles for atomic layer etching of crystalline diamond. The flooding of the diamond surface with NO2 is alternated with flooding the surface with excited ions. Purging takes place in between these steps. Image from Ref. 20. (b) Saturation curves for atomic layer etching of GaAs by Cl2 dosing and Ar + ion irradiation. Data is shown for various Cl2 dosing or feed times. From Ref. 28. Reprinted with permission. Copyright 1993, Elsevier. (c) Schematic of the atomic layer etching process of silicon by Cl2 dosing and Ar + ion irradiation. The filled circles represent Cl atoms, the open circles represent Si atoms, and + represent Ar + ions. From Ref. 33. Reprinted with permission. Copyright 1995, American Institute of Physics. The processes shown in (a)-(c) are similar and form only one particular embodiment of atomic layer etching processes.

chlorinated surface layer to a low-fluence 193 nm ArF excimer laser pulse induced desorption leading to the removal or etching of the halogenated surface layer. Meguro et al. 27 presented a 'digital etching' process in which they used a Cl2 gas pulse to passivate the surface of GaAs followed by a purge cycle to remove residual Cl2, a subsequent bombardment of the halogenated surface layer with 100 eV electrons followed by another purge of the etch products. Using this electron beam excited plasma process, an etch rate of 0.1 nm/cycle, i.e., 1 3 of a monolayer of GaAs was obtained, independent of the Cl2 flow rate and the electron current density for the ranges investigated. The etch rate for GaAs was increased to 0.2 nm/cycle using a similar method 28 but using low energy 25 eV Ar + ions instead of electrons. In this work typical saturation curves were also provided showing zero etching at zero Ar + irradiation and a saturated etch rate for sufficiently long Ar + irradiation [see Fig. 2b]. For 'layer-by-layer' etching, Ko et al. 29 used an electron cyclotron resonance (ECR) plasma source placed on top of a radio frequency (RF) powered electrode to generate reactive radicals with independent control over ion energy and ion flux. Bombardment

of a surface-chlorinated GaAs layer with low energy but high-density Ar + ions at room temperature led to an etch rate of 0.5 nm/cycle, independent of the chlorine radical or Ar + ion exposure time. They also demonstrated ALEt of other III-V semiconductors like GaInAs, AlInAs and InP. Ishii et al. 30 took an approach similar to that of Maki et al. by employing a 248 nm KrF excimer laser in place of a charged particle beam (ions, electrons) to irradiate a Cl2 adsorbed GaAs surface. With their 'digital etching' process, they obtained an etch rate of 0.2 nm/cycle, independent of excimer laser repetition rate and the amount of initially injected Cl2.

In parallel to these investigations of atomic layer etching of III-V semiconductors, atomic layer etching of silicon was explored. Sakaue et al. 31 extrapolated the pioneering work of Horiike et al. 21 for 'digital etching' of Si using molecular chlorine instead of fluorine as the adsorbate precursor. Removal of the surface-chlorine adsorbed species subsequently took place via desorption induced by Ar + ion irradiation. Asaturated etch rate of about 0.4 Å/cycle was obtained as the Ar + ion irradiation time was increased. The value of 0.4 Å/cycle corresponds to about 1 3 of a monolayer of Si(100). Upon increasing substrate bias voltage, the etch rates increased rapidly with increased amounts of higher-order etch products (SiCl3, SiCl4). Matsuura et al. 22 and Suzue et al. 32 reported on 'self-limited layer-by-layer etching' and 'selflimited atomic layer etching' of Si, respectively, using ECR plasmas. The etch rate per cycle increased with the chlorine exposure time and saturated to a constant value of about 1 2 and 1 3 of a monolayer per cycle for Si(100) for Si(111), respectively, independent of the chlorine partial pressure. In their work, they also addressed the influence of the crystal orientation on the etch rate and the fact that only a fractional number of a monolayer is etched every cycle. On the basis of a molecular dynamics simulation study, 25 Athavale and Economou reported that ALEt of a monolayer per cycle may be achieved with Cl2 and Ar + ions [see Fig. 2c]. They presented experimental results in a follow up work in which they used a helicon plasma for generating the Ar + ions. 33 By applying and tuning a DC bias on the substrate, the Ar + ion bombardment energy could be adjusted to etch one monolayer off from silicon in an ∼ 100 s cycle. The process was self-limiting with respect to both chlorine dose and the ion dose while the etch rate was found to be a strong function of the DC bias on the substrate, i.e., the ion bombardment energy.

ALEt of silicon that makes use of energetic ions, albeit at low energy, may exclude any physical damage but may not be immune to any damage due to charging. To account for this charging damage, Park et al. 34,35 investigated ALEt of silicon by using Cl2 surface passivation followed by bombardment with energetic Ar neutrals. One monolayer per cycle of silicon (100) and (111) was etched in the process but with comparatively longer cycle durations of ∼ 500 s and ∼ 800 s, respectively, for the two orientations as the etch rates depended on the Cl2 pressure and Ar neutral beam fluence. To overcome the drawback of such long cycle times, an ALEt method incorporating pulsed plasmas has been proposed. 36,37 The concept relies on the formation of a self-limited halogenated surface layer in the presence of a plasma without initial substrate bias thus preventing ion bombardment induced etching. By using pulsed biasing, the halogenated surface layer is sputtered off faster than it can reform. Complete removal of this layer inhibits any further etching of the substrate provided the ion energy is below the sputtering threshold of the substrate. The bias is then switched off which again leads to the formation of a halogenated layer and the cycle can be repeated to obtain a fast ALEt process.

Furthermore, attention was given to the ALEt of oxides. Yeom and co-workers reported on ALEt of HfO2 using BCl3 and an Ar neutral beam. They showed a considerable improvement in the electrical characteristics of the devices prepared by ALEt when compared to results obtained for devices etched by conventional wet or dry etch techniques. 38,39 These improved results were attributed to a low edge damage of the gate oxide during ALEt by maintaining the surface composition at the edge of the gate oxide together with exact control of the Si etch depth. Recently, Metzler et al. 40 also demonstrated ALEt of SiO2 using a steady-state Ar plasma, periodic injection of a defined amount of C4F8 gas and synchronized plasma-based Ar +

ion bombardment. Injecting a predefined amount of C4F8 gas leads to the controlled deposition of a fluorocarbon (FC) layer in the one to several Ångstroms thickness range onto the SiO2 surface. Applying low-energy Ar + ion bombardment induces etching of the FC layer together with reaction of carbon and fluorine with the underlying SiO2 surface layer. The resulting modified SiO2 surface layer is etched by the low-energy Ar + ion bombardment until the modified layer is removed at which point the SiO2 etching terminates.

## What Can We Learn From ALD?

Ascanbeseenfromthe previous section, efforts for establishing an atomic scale etching process analogous to ALD have been quite limited so far. They have been restricted to a few particular embodiments, material systems, and chemistries and the approaches developed till nowhave had limited success and/or a limited range of potential applicability. Yet, the efforts also demonstrate the potential opportunities provided by the ALEt process concept, particularly in view of the current developments in the semiconductor industry. To significantly advance the applicability of ALEt, it is worthwhile to look in more detail at the ins and outs of ALD. It can be meaningful to learn from the state-of-the-art features of this technology as well as from its historical developments and emerging trends. Identifying similarities and differences between ALEt and its ALD counterpart can certainly contribute to expanding the toolbox of ALEt processes with sufficient performance to tackle future challenges in semiconductor and other device manufacturing.

First, it is instructive to define atomic layer etching and to introduce a generalized ALEt cycle. From the research efforts so far, it is clear that ALEt is a layer-by-layer etching method with - similar to ALD - the following defining characteristics (see Fig. 1): the process takes place cycle-wise with several steps per cycle, and is based on selflimiting surface chemistry. However, contrary to what is claimed or suggested in many previous reports (especially in the work related to silicon etching), it is not necessary or useful to restrict ALEt to processes in which a full monolayer of material is etched. To achieve atomic layer etch precision in a very repeatable manner, the processes do not necessarily have to yield one monolayer per cycle. Removal of a submonolayer per cycle is adequate and, as a matter of fact, even better as the etch control can be even more precise. Note, that in virtually all ALD processes, the thickness increase per cycle is also limited to less than a monolayer (see Table I) although there have been some cases reported in which the thickness increase is more than a monolayer. 41,42 Yet whether the decrease in thickness after one cycle of ALEt is less or more than a monolayer, atomic scale precision in thickness and atomically smooth surfaces can still be obtained. In fact, it would be more sensible to add the criterion of (atomically) smooth surfaces to the definition of ALEt. Furthermore, note that the limitation to processes that yield one monolayer per cycle is only well-defined when etching single-crystalline materials such as silicon. A monolayer is very ill-defined when etching amorphous or polycrystalline materials, for example highk oxides such as HfO2 in gate stacks.

A generalized ALEt cycle can also be introduced by identifying parallels with ALD (see Fig. 3). So far, the ALEt technique has manifested itself mostly based on a chemically enhanced process in which passivation of the surface of the material to be etched with a layer of adsorbed precursor species decreases the activation energy required by energetic particle bombardment to remove that layer (see The early days of atomic layer etching section). Limiting the discussion to a process with two half-reactions and four steps per cycle for simplicity, it is more relevant and more comprehensive to identify an adsorption step and an activation step. In the adsorption step, the surface is exposed to a precursor gas which adsorbs onto the surface in a self-limiting way, i.e., preventing further multilayer adsorption. This adsorption of a precise amount of precursor is similar for ALEt and ALD. This similarity also holds for the purge steps that separate the two half-reactions and which remove excess precursor species and reaction products from the reactor.

Table I. The growth-per-cycle (GPC) for selected ALD processes. The GPC is given in metal atoms ( M at.) per nm 2 and per cycle as well as equivalent monolayer ( eq. ML ) per cycle. For ALD, the GPC values can, for example, be ruled by the ionic radius of the metal center to be deposited, 64,65 the ligand sizes of the precursors, 64,66,67 or the density of adsorption sites on the surface. 68,69 For the calculation of the GPC as eq. ML , the approximate distance between the metal atoms was used as derived from the atomic density of the bulk material neglecting the influence of crystal orientations, surface reconstructions, etc.

| Material   | Process details (substrate temperature)   |   GPC (Å) |   GPC ( M at. nm - 2 ) |   GPC ( Eq. ML ) | Reference   |
|------------|-------------------------------------------|-----------|------------------------|------------------|-------------|
| ZnO        | ZnEt 2 + H 2 O (150 ◦ C)                  |      2    |                    7.1 |             0.6  | 70          |
| Al 2 O 3   | AlMe 3 + H 2 O (200 ◦ C)                  |      1    |                    3.5 |             0.33 | 71          |
| HfO 2      | HfCl 4 + H 2 O (300 ◦ C)                  |      0.4  |                    1.1 |             0.12 | 72          |
| TiN        | TiCl 4 + NH 3 (350 ◦ C)                   |      0.28 |                    1.1 |             0.09 | 73          |
| TaN x      | Ta(NMe 2 ) 5 + H 2 plasma (225 ◦ C)       |      0.56 |                    2.1 |             0.19 | 59,74       |
| Pt         | MeCpPtMe 3 + O 2 (300 ◦ C)                |      0.45 |                    3   |             0.2  | 75          |
| Pd         | Pd(hfac) 2 H 2 plasma (100 ◦ C)           |      0.17 |                    0.9 |             0.05 | 76          |

+

However, the main differences lie in the third step. In ALEt, the surface is activated by co-reactant species which remove volatile etch products from the surface in a self-limiting way. After purging, this leads to the removal of one atomic layer from the surface (not necessarily a monolayer as discussed earlier). For ALD on the other hand, the activation step consists of exposing the surface to a co-reactant that completes the addition of an atomic layer of the material to be deposited on the surface, and, at the same time activates the surface for the next ALD cycle. The activation of the surface for the next cycle in the third step is a strict criterion for both ALD and ALEt and this holds also for the self-limiting nature of the second half-cycle. For ALD, whether the elements of the co-reactant are added to the surface layer or not is insignificant from a conceptual point of view. Some co-reactants only activate the surface without contributing to growth, e.g., ALD of W from WF6 and Si2H6 43 and ALD of Pt from (CH3)3Pt(CpCH3) and O2. 44,45

defines the metal oxide, nitride, sulfide, etc. to be deposited. For ALEt, it is typically a species which contains elements that can form volatile reaction products with the material to be etched. Fluorineor chlorine-based precursors are typical examples used during ALEt of silicon. The co-reactant during the activation step is less welldefined and is not limited to atoms or molecules. It can also consist of many other species such as ions, electrons, energetic neutrals from a neutral beam or photons. The activation step could even involve a substrate temperature ramp. 46 For ALEt, such a multitude of possible co-reactants is apparent from the past research efforts reviewed in the previous section. However, for ALD, processes based on such co-reactants have been reported but have gained more attention fairly recently (see Ref. 47 and references therein).

The precursor in the adsorption step is typically well-defined. For ALD, it consists of an element to be deposited, e.g., the metal that

Regarding the surface chemistry occurring during the two halfreactions in atomic layer processes, a large variety of surface reactions exists. For ALD, the surface chemistry can be based on reaction mechanisms such as ligand exchange, dissociation, association, combustion, abstraction, reduction, etc. 48 For ALEt, in principle similar

Figure 3. Schematic representation of one complete, generalized cycle of (a) atomic layer etching (ALEt) and (b) atomic layer deposition (ALD). In (c), the so-called saturation curves for the various steps in the ALEt and ALD processes are schematically illustrated. The depicted processes consist of two half-reactions Aand B and the total cycle is divided into four process steps. Step 1 is the 'adsorption step' and step 3 is the 'activation step'. In these steps, the surface is exposed to reactants, here defined as 'precursor' in step 1 and 'co-reactant' in step 3. Steps 2 and 4 are 'purge steps'. The cycles, and hence the process steps, are repeated multiple times when etching or depositing a film. Every cycle removes or adds an atomic layer from or to the film for ALEt and ALD, respectively. The saturation curves show that exposure to the reactants in steps 1 and 3 should be sufficiently long to reach saturation. The purging in between these steps should be sufficiently long to avoid parasitic CVD or parasitic etch reactions that compromise the ALEt or ALD character of the processes.

<!-- image -->

reaction mechanisms can take place although most studies so far relied on dissociation (e.g., dissociation of Cl2 at active surface sites) in combination with desorption reactions, e.g., assisted by ions, electrons, or photons (See The early days of atomic layer etching section). However, many processes relying on other chemistries can also be potentially developed, e.g., as demonstrated in a recent article by Lee and George who developed a thermally driven 'reverse ALD' process. 49

ate the Ar + might dissociate residual Cl2 when the reactor has not been purged sufficiently. This will lead to uncontrolled etching of the silicon during the second half-reaction of the process.

For both ALEt and ALD, the self-limiting behavior of the surface chemistry is key and should be verified by saturation curves. In case of ALD, one needs to verify whether or not an atomic layer of material has been added to the film independent of the dosing times as long as these are sufficiently long. The same holds for the removal of one atomic layer in ALEt. In both cases, this can be done by varying the dosing times for one step while keeping the dosing times for the other step(s) sufficiently long [see Fig. 3c]. One should also ensure that no atomic layer has been added or removed with zero dosing time for the precursor or co-reactant. If the latter does not hold true, the processes do not - strictly speaking - consist of two half-reactions and subsequently, the condition of an atomic layer deposition or etching process is not met. Another aspect is the purging after the two half-reactions. The purges should be long enough to ensure that excess precursor molecules and reaction products are completely removed from the reactor before the co-reactant is introduced, and vice versa. When the purging times are too short, precursor and co-reactant molecules can interact leading to parasitic CVD reactions occurring during ALD. Consequently, key features of ALD such as precise growth control, excellent conformality and unparalleled uniformity are compromised. For ALEt, a similar phenomenon can occur, i.e., parasitic etch, which means that the etching is not restricted to one well-defined atomic layer. For example, in the processes reported for Si etching by Cl2 adsorption and Ar + irradiation (see The early days of atomic layer etching section), the Ar plasma used in the 2 nd half-cycle to gener-

Besides comparing ALEt and ALD cycles and their process steps, it is also worthwhile to pay attention to the key (desired) features of the processes. From this perspective it is possible to identify some clear similarities and differences between ALEt and ALD (see Fig. 4). What both processes (should) have in common is that they should lead to a very good uniformity over a large substrate area, i.e., basically over the full wafer size when processing wafer-based semiconductor devices. For ideal ALEt and ALD processes, this aspect is guaranteed by the fact that the processes are surface-controlled and self-limiting. This provides the opportunity to expose the wafer surface for a sufficiently long period to the precursor and co-reactant doses such that saturation of the surface chemistry can be reached over the full substrate area without multilayer removal or addition on highly-exposed surface regions. Obviously, another similarity lies in the control of the atomic layer processes: every cycle should lead to precise removal or addition of a well-defined atomic layer for ALEt and ALD, respectively. However, major differences between ALEt and ALD can be identified when considering the processing of 3D features at the substrate surface. The fact that ALD can yield very conformal films on demanding 3D topologies is a key asset of ALD intrinsic to the process. When depositing a film in, e.g., high aspect ratio trenches or holes, ALD processes will deposit a film with uniform thickness across the entire surface area of the substrate which includes the sidewalls and the bottom of the trenches or holes [see Fig. 4b]. Ideally, this is independent of the surface density of the features and their corresponding pitch. For the etching counterpart, the desired situation is however different. Dry etching is generally carried out to create vertical structures such as (high aspect ratio) trenches and holes within the surface region of the substrate and, therefore, anisotropic etch processes are generally employed. The anisotropy is typically achieved by directional

Figure 4. Schematic illustration of the key features for (a) atomic layer etching (ALEt) and (b) atomic layer deposition (ALD). The processes yield a precise control of the thickness etched (etch control) or deposited (growth control) per cycle for ALEt and ALD, respectively. The latter holds for the full substrate surface such that the uniformity is excellent. When processing a substrate with three-dimensional features, the situation for ALEt and ALD is however different. For ALD, the coverage of three-dimensional features is similar throughout the features and comparable to the planar surface, hence the conformality of ALD-prepared films is excellent. For etching processes such as ALEt, there is generally interest in etching vertical features which requires anisotropic processes in which only material is removed from the bottom of the vertical feature. In other cases, isotropic etching can be desired. In this case, the material should be etched equally on all exposed surfaces, independent of the orientation of the local surface on the substrate. For ALEt, also the selectivity of the etch process is key. Ideally, only the to-be-etched material should be removed and not masking materials or materials lying underneath the to-be-etched material.

<!-- image -->

processes such as physical sputtering by (plasma-generated) ion beams or by so-called reactive ion etching processes (in all kinds of plasma reactors) in which a physical component is added to a chemical etching process. In this case, the so-called ion-radical synergism 50 leads to significantly enhanced etch rates perpendicular to the substrate surface compared to those occurring parallel to the substrate surface. In this manner, the patterns to be etched can be effectively transferred to the substrate through the pre-defined openings in a hard mask covering the substrate material (see also discussion about selectivity below). Thus, if the etching of vertical structures is intended, the ALEt processes should be designed to have an anisotropic character. This is, e.g., the case for ALEt processes in which the co-reactant consists of directional, energetic species such as ions, electrons or energetic atoms from a neutralized ion beam. In the research efforts reported so far (see The early days of atomic layer etching section), this has often been the case. However, such anisotropic ('non-conformal') etching is only one possible manifestation of ALEt. It can be envisioned that isotropic ('conformal') etching by ALEt processes is also imperative for particular situations. This will however impose quite different requirements on the ALEt process steps, in particular on the co-reactants used. For example, ALEt processes that rely on a co-reactant consisting only of directional species are not an option for isotropic etching. A true 'reverse ALD' process is probably more suited for isotropic etching, e.g., an ALEt process which is purely thermally driven. 49

cycles and its process steps. For example, it restricts the energy of ions when these are used as the co-reactant to activate the surface. Their energy should be sufficiently high to activate the to-be-etched surfaces but should be sufficiently low to leave the mask or underlying material intact. 24 This calls for precise ion-energy control under such conditions.

Another aspect that is different for etch and deposition processes is that etch processes are characterized by an additional parameter which, by definition, does not have an equivalent for deposition processes. This parameter is the selectivity of the etch process, which is defined as the ratio between the rate of the layer being etched relative to that of a masking or underlying layer. Selectivity is critical for all etch processes including ALEt and it also imposes constraints on the ALEt

Having addressed the selectivity that needs to be achieved for etch processes based on ALEt, it is also interesting to consider the currently increasing interest in area-selective ALD processes 51 and draw parallels here as well. Nanopatterning of films and structures by area-selective ALD in bottom-up processes is receiving growing attention as this could eliminate compatibility issues with topdown etch processes which are associated with the use of etchants, lift-off chemicals or resist films. Therefore, area-selective ALD processes relying on area-deactivation and area-activation (see Fig. 5) are currently being explored. 51 However, for cases where incentives exist to restrict to top-down etching, it is interesting to explore areaselective ALEt processes as well. Besides traditional masking of the substrate surface (i.e., 'selective by surface deactivation'), the surfacecontrolled ALEt processes can potentially also be designed such that one substrate material is etched while other substrate materials are not ('inherently selective'). Another possibility is area-activation ('selective by surface activation'), e.g., by carrying out the activation step during an ALEt process [see Fig. 3a] only locally by a spatially defined co-reactant exposure, e.g., an focused electron or ion beam. Examples of such processes are illustrated and discussed in Fig. 5.

Several challenges for ALEt have been discussed in this section. So far, these challenges were mainly process-related and a brief and probably incomplete overview is presented in Table II. It is evident that it will not be a trivial task to overcome these challenges. At the same

Figure 5. Approaches to realize area-selective ALD [(a), (c) and (e)] and area-selective ALEt [(b), (d) and (f)]. (a) and (b) show an approach that can be labeled 'inherently selective'. The substrate is composed of several materials and on the surface of some of the materials, deposition or etching does (virtually) not occur for the ALD or ALEt surface chemistry chosen. The selectivity is therefore, inherent to the specific ALD or ALE process. (c) and (d) show an approach that can be labeled as 'selective by deactivation' since part of the substrate is deactivated by a layer of molecules or a film (mask). No etching or deposition takes place at the parts of the surface that are deactivated. This approach is standard for etching. It is not problematic if the mask material is somewhat etched as long as it etches much slower than the to-be-etched material. (e) and (f) show an approach that can be labeled 'selective by activation'. Film growth or etching only initiates on those parts of the surface that are activated, e.g., by a focused electron or ion beam that locally interacts with the surface. For ALD, processes exist in which this activation only needs to be done before the first cycle; 51 for ALEt, the local activation step needs to take place every cycle. In all the displayed cases for ALD [(a), (c) and (e)], the area-selective ALD processes depend on an effect known as nucleation delay. The film material easily deposits on some surfaces whereas on other areas, the film hardly nucleates or it takes much longer for the film to nucleate. For area-selective ALEt approaches (b) and (d), selectivity has the same meaning as that typical for etch processes. The to-be-etched material should etch much faster than any other material used. In (d), the selectivity should preferably approach infinity. Furthermore, it is noted that the possibility exists for designing area-selective ALEt approaches by combining ALEt and ALD. For example, area-selective ALD films can serve as a local mask.

<!-- image -->

Table II. Prominent challenges for atomic layer etching divided into process-related and equipment-related challenges

## Process-related

-ALEt processes for more material systems

-More diverse ALEt surface chemistries

-Processes for isotropic and anisotropic ALEt

-Area-selective ALEt processes

-. . .

## Equipment-related

-Dedicated ALEt reactors

-Versatile, well-controlled co-reactant sources

-Process monitoring and control

-High-throughput methods and reactors

-. . .

time, it has become clear that inspiration can be obtained from ALD processing and the associated trends and developments within that field. This should also hold particularly for the surface chemistries that need to be developed. At this point it is important to stress that ALD or ALEt processes are not necessarily limited to conventional AB-cycles (more precisely: (AB) n with n being the number of cycles). Also, multistep cycles such as (ABC) n or supercycles ((A1B1) m (A2B2) ) n x (with m and n being the number of A1B1 and A2B2 cycles, respectively and x being the total number of supercycles) 48 can be employed (see Fig. 6). For ALD, such multistep cycles and supercycles have proven extremely powerful, e.g., in extending the temperature window of ALD processes (e.g., for Pt 52 ), improving the properties of ALDprepared materials (e.g., for Pd 76 ), or depositing doped materials (e.g., Al-doped ZnO 53 ) or complex oxides (e.g., SrTiO3 54 ).

Table II also lists some of the challenges for ALEt which are equipment-related. Obviously, much like ALD, it is essential that

<!-- image -->

dedicated ALEt reactors will need to be developed. These reactors can be optimized for precursor and co-reactant dosing while at the same time accounting for the design and implementation of versatile co-reactant sources. These co-reactants can be atoms, molecules, ions, electrons and photons, etc., and they can be delivered from the gas phase isotropically or directionally, e.g., using beams. ALEt processes based on energetic ions will require accurate ion-energy control, e.g., by incorporating advanced substrate biasing schemes 55 yielding monodisperse ion energies which can be precisely controlled. Note that (advanced) substrate biasing 18 is already at the heart of the technology in plasma etching while it has just entered the field of plasma-enhanced ALD. 56,57 Furthermore, when working with plasmabased co-reactants, process and reactor design should take into account whether or not surface reaction products liberated from the surface during the co-reactant step can be dissociated in the plasma, e.g., by electron-impact. These dissociated reaction products can interact again with the surface and lead to additional etching or (re)deposition. Such effects have clearly been observed for plasma-enhanced ALD processes. 58,59 Next, also equipment-related challenges will exist that are economically driven. A particularly important challenge lies in reaching sufficiently high throughput numbers for the processes. So far, ALEt processes suffer from long cycle times, even much more so than many ALD processes. However, at this point inspiration can also be derived from the developments and progresses made in ALD. Approaches such as operating under not-fully saturated conditions to reduce cycle times or resorting to spatial ALEt concepts, 46,60,61 similar to spatial ALD processes, 62 can also provide pathways for increasing the throughput of ALEt reactors, as illustrated in Fig. 7. It goes without saying that eventually, it is the application that will determine the tolerance thresholds for the processes involved and their parameters, not the fact of whether the processes themselves are strictly ALEt or not.

<!-- image -->

<!-- image -->

<!-- image -->

Figure 6. A schematic representation of various types of cycles for ALD 48 that can also be employed for ALEt: (a) a regular process, (b) a multistep process and (c) a supercycle process. In a multistep process, one or more additional steps are added to the cycle to form, for instance, an ABC process. In a supercycle, the steps of two regular processes are combined where m cycles of the first process are followed by n cycles of the second process. The variables m and n can be chosen so as to obtain the desired properties for the ALD or ALEt process.

Figure 7. Approaches that are being used to increase the throughput of ALD reactors that, in principle, can also be adopted for ALEt reactors. In (a), the approach is shown where the process is not operated under fully saturated conditions. When working with slightly shorter exposure times the cycle time can significantly be reduced (e.g., by a factor of two) while the thickness deposited or removed is only slightly reduced. For many processes and device architectures, the level of growth or etch control remains acceptable. In (b), the socalled spatial atomic layer process is shown. The cycles are not carried out in the time domain but in the spatial domain. It is noted however, that developing appropriate processes for spatial ALD is not straightforward and this is probably even more so for spatial ALEt.

<!-- image -->

## Conclusions

Atomic layer etching (ALEt) is an etch approach that can potentially tackle issues in semiconductor device manufacturing now that critical dimensions are nearing single-digit nanometer values. Being the etch counterpart of the commercially established method of atomic layer deposition (ALD), the aim of this article is to draw parallels between ALEt and ALD in order to more precisely define atomic layer etching, introduce a generalized ALEt cycle and identify similarities and differences between the two processes. It is expected that this will assist in significantly advancing the field of ALEt, both through conceptual considerations as well as by highlighting practical guidelines and recommendations. ALEt has been researched already for over 25 years now with relatively limited endeavors and successes. However, this does not mean that the progress will remain slow. For ALD, it also took 25 years before interest in this technology increased explosively owing to the fact that atomic layer precision in deposition became highly necessary. From that point onwards, many breakthroughs in both research and industrial applications were realized. A similar situation seems to exist at the moment for ALEt although the application range for this process will be smaller than that for ALD (the latter having many applications both within and outside the semiconductor industry). Moreover, ALEt seems to have process requirements that are less trivial and more demanding. However, continued development of ALEt processes and equipment will evidently advance the field of etching even if ideal ALEt processes remain unfeasible over the coming years. Research on ALEt will certainly contribute to etching with more atomic layer precision.

Finally, it is noted that a recently appeared review article by Kanarik et al. 63 addresses some similar considerations as presented in this article.

## Acknowledgments

The research of W.M.M.K. has been made possible by the Dutch Technology Foundation STW and the Netherlands Organization for Scientific Research (NWO) through the VICI program on Nanomanufacturing.

## References

- 1. G. Moore, Electronics 38 , 8 (1965).
- 2. International Technology Roadmap for Semiconductors , 2013 Edition, Executive Summary.
- 3. R. Chau, S. Datta, M. Doczy, B. Doyle, J. Kavalieros, and M. Metz, IEEE Electron Device Lett . 25 , 408 (2004).
- 4. M. T. Bohr, R. S. Chau, T. Ghani, and K. Mistry, IEEE Spectrum 44 (10), 29 (2007).
- 5. M. Radosavljevic, B. Chu-Kung, S. Corcoran, G. Dewey, M. K. Hudait, J. M. Fastenau, J. Kavalieros, W. K. Liu, D. Lubyshev, M. Metz, K. Millard, N. Mukherjee, W. Rachmady, U. Shah, and R. Chau, Tech. Dig. IEDM , 319 (2009).
- 6. K. J. Kuhn, U. Avci, A. Cappellani, M. D. Giles, M. Haverty, S. Kim, R. Kotlyar, S. Manpatruni, D. Nikonov, C. Pawashe, M. Radosavljevic, R. Rios, S. Shankar, R. Vedula, R. Chau, and I. Young, Tech. Dig. IEDM , 171 (2012).
- 7. C.-H. Jan, U. Bhattacharya, R. Brain, S.-J. Choi, G. Curello, G. Gupta, W. Hafez, M.Jang, M. Kang, K. Komeyli, T. Leo, N. Nidhi, L. Pan, J. Park, K. Phoa, A. Rahman, C. Staus, H. Tashiro, C. Tsai, P. Vandervoorn, L. Yang, J.-Y. Yeh, and P. Bai, Tech. Dig. IEDM , 44 (2012).
- 8. C.-Y. Lu, J. Nanoscience Nanotechnology 12 , 7604 (2012).
- 9. Handbookof3-DIntegration: Technology and Applications of 3D Integrated Circuits , (P. Garrou, C. Bower, and P. Ramm, eds.), Wiley-VCH Verlag, Weinheim (2008).
- 10. T. Suntola, Mater. Sci. Reports 4 , 261 (1989).
- 11. M. Leskel‹ a and M. Ritala, Thin Solid Films 409 , 138 (2002).
- 12. R. L. Puurunen, J. Appl. Phys. 97 , 121301 (2005).
- 13. S. M. George, Chem. Rev. 110 , 111 (2010).
- 14. T. Suntola and J. Antson, US Pat. 4058430 A (1977).
- 15. G. N. Parsons, J. W. Elam, S. M. George, S. Haukka, H. Jeon, W. M. M. Kessels, M. Leskel‹ a, P. Poodt, M. Ritala, and S. M. Rossnagel, J. Vac. Sci. Technol. A 31 , 050818 (2013).
- 16. H. B. Profijt, S. E. Potts, M. C. M. van de Sanden, and W. M. M. Kessels, J. Vac. Sci. Technol. A 29 , 050801 (2011).
- 17. P. Poodt, D. C. Cameron, E. Dickey, S. M. George, V. Kuznetsov, G. N. Parsons, F. Roozeboom, G. Sundaram, and A. Vermeer, J. Vac. Sci. Technol. A 30 , 010802 (2012).
- 18. V. M. Donnelly and A. Kornblit, J. Vac. Sci. Technol. A 31 , 050825 (2013).
- 19. C. A. Mack, Proc. of SPIE 9189 , 91890D (2014).
- 20. M. N. Yoder, US Pat. 4,756,794 A (1988).
- 21. Y. Horiike, T. Tanaka, M. Nakano, S. Iseda, H. Sakaue, A. Nagata, H. Shindo, S. Miyazaki, and M. Hirose, J. Vac. Sci. Technol. A 8 , 1844 (1990).
- 22. T. Matsuura, J. Murota, Y. Sawada, and T. Ohmi, Appl. Phys. Lett. 63 , 2803 (1993).
- 23. Y. Aoyagi, K. Shinmura, K. Kawasaki, T. Tanaka, K. Gamo, S. Namba, and I. Nakamoto, Appl. Phys. Lett. 60 , 968 (1992).
- 24. A. Agarwal and M. J. Kushner, J. Vac. Sci. Technol. A 27 , 37 (2009).
- 25. S. D. Athavale and D. J. Economou, J. Vac. Sci. Technol. A 13 , 966 (1995)
- 26. P. A. Maki and D. J. Ehrlich, Appl. Phys. Lett. 55 , 91 (1989).
- 27. T. Meguro, M. Hamagaki, S. Modaressi, T. Hara, Y. Aoyagi, M. Ishii, and Y. Yamamoto, Appl. Phys. Lett. 56 , 1552 (1990).
- 28. T. Meguro, M. Ishii, K. Kodama, Y. Yamamoto, K. Gamo, and Y. Aoyagi, Thin Solid Films 225 , 136 (1993).
- 29. K. K. Ko and S. W. Pang, J. Vac. Sci. Technol. B 11 , 2275 (1993).
- 30. M. Ishii, T. Meguro, K. Gamo, T. Sugano, and Y. Aoyagi, Jap. J. Appl. Phys. 32 , 6178 (1993).
- 31. H. Sakaue, K. Asami, T. Ichihara, S. Ishizuka, K. Kawamura, and Y. Horiike, MRS Symp. Proc. 222 , 195 (1991).
- 32. K. Suzue, T. Matsuura, J. Murota, Y. Sawada, and T. Ohmi, Appl. Surf. Sci. 82 , 422 (1994).
- 33. S. D. Athavale and D. J. Economou, J. Vac. Sci. Technol. B 14 , 3702 (1996).
- 34. S. D. Park, D. H. Lee, and G. Y. Yeom, Electrochem. Solid. State Lett. 8 , C106 (2005).
- 35. S. D. Park, C. K. Oh, D. H. Lee, and G. Y. Yeom, Electrochem. Solid. State Lett. 8 , C177 (2005).
- 36. R. A. Gottscho and K. J. Kanarik, APS 64th Annual Gaseous Electronics Conference , Salt Lake City, UT (2011)
- 37. V. M. Donnelly and D. J. Economou, US Pat. 20110139748 A1 (2011).
- 38. S. D. Park, W. S. Lim, B. J. Park, H. C. Lee, J. W. Bae, and G. Y . Yeom, Electrochem. Solid-State Lett. 11 , H71 (2008).
- 39. K. Min, C. Park, C. Kang, C. Park, B. Park, Y. Kim, B. Lee, J. C. Lee, G. Bersuker, P. Kirsch, R. Jammy, and G. Yeom, Solid-State Electron . 82 , 82 (2013).
- 40. D. Metzler, R. L. Bruce, S. Engelmann, E. A. Joseph, and G. S. Oehrlein, J. Vac. Sci. Technol. A 32 , 020603 (2014).
- 41. D. Hausmann, J. Becker, S. L. Wang, and R. G. Gordon, Science 298 , 402 (2002).
- 42. B. B. Burton, M. P. Boleslawski, A. T. Desombre, and S. M. George, Chem. Mater . 20 , 7031 (2008).
- 43. J. W. Klaus, S. J. Ferro, and S. M. George, Appl. Surf. Sci. 162 , 479 (2000).
- 44. T. Aaltonen, A. Rahtu, M. Ritala, and M. Leskel‹ a, Electrochem. Solid-State Lett. 6 , C130 (2003).
- 45. H. C. M. Knoops, A. J. M. Mackus, M. E. Donders, M. C. M. van de Sanden, P. H. L. Notten, and W. M. M. Kessels, Electrochem. Solid. State Lett. 12 , G34 (2009).
- 46. M. Chang and J. Yodovsky, US patent 8,633,115B2 (2014).
- 47. S. E. Potts and W. M. M. Kessels, Coord. Chem. Rev. 257 , 3254 (2013).
- 48. H. C. M. Knoops, S. E. Potts, A. A. Bol, and W. M. M. Kessels, in Handbook of Crystal Growth (T. Kuech ed.), Elsevier (2015).
- 49. Y. Lee and S. M. George, ACS Nano 9 , 2061 (2015)
- 50. J. W. Coburn and H. F. Winters, J. Appl. Phys. 50 , 3189, (1979).
- 51. A. J. M. Mackus, A. A. Bol, and W. M. M. Kessels, Nanoscale 6 , 10941 (2014)
- 52. A. J. M. Mackus, D. Garica-Alonso, H. C. M. Knoops, A. A. Bol, and W. M. M. Kessels, Chem. Mater. 25 , 1769 (2013).
- 53. T. Tynell and M. Karppinen, Semicond. Sci. Technol. 29 , 043001 (2014)
- 54. M. Vehkam‹ aki, T. Hatanp‹ a‹, T. H‹nninen, M. Ritala, and M. Leskel‹ a, a a Electrochem. Solid. State Lett. 2 , 504 (1999).
- 55. S.-B. Wang and A. E. Wendt, J. Appl. Phys. 88 , 643 (2000).
- 56. H. B. Profijt, M. C. M. van de Sanden, and W. M. M. Kessels, Electrochem. Solid. State Lett. 15 , G1 (2012).
- 57. H. B. Profijt, M. C. M. van de Sanden, and W. M. M. Kessels, J. Vac. Sci. Technol. A 31 , 01A106 (2013).
- 58. S. B. S. Heil, P. Kudlacek, E. Langereis, R. Engeln, M. C. M. van de Sanden, and W. M. M. Kessels, Appl. Phys. Lett. 89 , 131505 (2006).
- 59. H. C. M. Knoops, E. Langereis, M. C. M. van de Sanden, and W. M. M. Kessels, J. Vac. Sci. Technol. A 30 , 01A101 (2012).
- 60. F. Roozeboom, B. Kniknie, A. M. Lankhorst, G. Winands, R. Knaapen, M. Smets, P. Poodt, G. Dingemans, W. Keuning, and W. M. M. Kessels, IOP Conf. Ser.: Mater. Sci. Eng. 41 , 012001 (2012).
- 61. F. Roozeboom, F. van den Bruele, Y. Creyghton, P. Poodt, and W. M. M. Kessels, submitted for publication (in this JSS Focus Issue).
- 62. W. M. M. Kessels and M. Putkonen, MRS Bulletin 36 , 907 (2011).
- 63. K. J. Kanarik, T. Lill, E. A. Hudson, S. Sriraman, S. Tan, J. Marks, V. Vahedi, and R. A. Gottscho, J. Vac. Sci. Technol. A 33 , 020802 (2015).
- 64. M. Ylilammi, Thin Solid Films 279 , 124 (1996).
- 65. J. P‹iv‹saari, M. Putkonen, and L. Niinist‹, a a o Thin Solid Films 472 , 275 (2005).
- 66. R. L. Puurunen, Chem. Vap. Deposition 9 , 327 (2003).
- 67. Y. Wu, S. E. Potts, P. M. Hermkens, H. C. M. Knoops, F. Roozeboom, and W. M. M. Kessels, Chem. Mater. 25 , 4619 (2013).
- 68. A. C. Dillon, A. W. Ott, J. D. Way, and S. M. George, Surf. Sci. 322 , 230 (1995).
- 69. R. L. Puurunen, Appl. Surf. Sci. 245 , 6 (2005).
- 70. D. Garcia-Alonso, S. E. Potts, C. A. A. van Helvoirt, M. A. Verheijen, and W. M. M. Kessels, J. Mater. Chem. C (2015).
- 71. S. E. Potts, W. Keuning, E. Langereis, G. Dingemans, M. C. M. van de Sanden, and W. M. M. Kessels, J. Electrochem. Soc. 157 , P66 (2010).
- 72. A. Delabie, R. L. Puurunen, B. Brijs, M. Caymax, T. Conard, B. Onsia, O. Richard, W. Vandervorst, C. Zhao, M. M. Heyns, M. Meuris, M. M. Viitanen, H. H. Brongersma, M. de Ridder, L. V. Goncharova, E. Garfunkel, T. Gustafsson, and W. Tsai, J. Appl. Phys. 97 , 064104 (2005).

- 73. A. Satta, A. Vantomme, J. Schuhmacher, C. M. Whelan, V. Sutcliffe, and K. Maex, Appl. Phys. Lett. 84 , 4571 (2004).
- 74. E. Langereis, H. C. M. Knoops, A. J. M. Mackus, F. Roozeboom, M. C. M. van de Sanden, and W. M. M. Kessels, J. Appl. Phys. 102 , 083517 (2007).
- 75. W. M. M. Kessels, H. C. M. Knoops, S. A. F. Dielissen, A. J. M. Mackus, and M. C. M. van de Sanden, Appl. Phys. Lett. 95 , 013114 (2009).
- 76. M. J. Weber, A. J. M. Mackus, M. A. Verheijen, V. Longo, A. A. Bol, and W. M. M. Kessels, J. Phys. Chem. C 118 , 8702 (2014).