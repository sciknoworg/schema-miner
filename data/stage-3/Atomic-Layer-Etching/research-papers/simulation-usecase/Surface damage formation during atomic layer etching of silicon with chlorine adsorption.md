<!-- image -->

RESEARCH ARTICLE |  JUNE 16 2021

## Surface damage formation during atomic layer etching of silicon with chlorine adsorption 

<!-- image -->

Special Collection: Atomic Layer Etching (ALE)

Erin Joy Capdos Tinacba 

; Michiro Isobe; Satoshi Hamaguchi



<!-- image -->

<!-- image -->

Check for updates

J. Vac. Sci. Technol. A 39, 042603 (2021) https://doi.org/10.1116/6.0001117

## Articles You May Be Interested In

Mechanism of SiN etching rate fluctuation in atomic layer etching

J. Vac. Sci. Technol. A (November 2020)

Etch-stop mechanisms in plasma-enhanced atomic layer etching of silicon nitride: A molecular dynamics study

J. Vac. Sci. Technol. A (August 2024)

Selective atomic layer etching of HfO 2  over silicon by precursor and substrate-dependent selective deposition

J. Vac. Sci. Technol. A (March 2020)

<!-- image -->

 

<!-- image -->

<!-- image -->

<!-- image -->

## Surface damage formation during atomic layer etching of silicon with chlorine adsorption

Cite as: J. Vac. Sci. Technol. A 39 , 042603 (2021); doi: 10.1116/6.0001117 Submitted: 5 May 2021 · Accepted: 26 May 2021 · Published Online: 16 June 2021

<!-- image -->

<!-- image -->

Erin Joy Capdos Tinacba,

Michiro Isobe, and Satoshi Hamaguchi a)

<!-- image -->

<!-- image -->

## AFFILIATIONS

Center for Atomic and Molecular Technologies, Graduate School of Engineering, Osaka University, 2-1 Yamadaoka, Suita, Osaka 565-0871, Japan

Note:

This paper is part of the 2022 Special Topic Collection on Atomic Layer Etching (ALE).

a) Author to whom correspondence should be addressed: hamaguch@ppl.eng.osaka-u.ac.jp

## ABSTRACT

As semiconductor device structures continue to approach the nanometer size range, new challenges in the fabrication of such devices have arisen. For example, the need for high-aspect-ratio, highly selective, controllable, and isotropic or anisotropic etching at the nanometer scale are some of them. Recently, atomic layer etching (ALE) has attracted much attention as an alternative to the conventional reactive ion etching (RIE) to address these issues. In comparison with RIE, ALE offers highly uniform etching over a large area with a precise etched depth and little damage to the underlying material surface. However, the extent of the surface damage formation in ALE processes has not been extensively reported yet. In this study, molecular dynamics simulation is used to examine the surface damages and reaction mechanisms during plasma-assisted (PA-) ALE of silicon (Si) with chlorine (Cl) radical adsorption and low-energy Ar þ ion irradiation for desorption. Several ALE cycles have been simulated and reproducible etched depths per cycle have been obtained. Based on the depth profiles, a damaged surface layer with a thickness of about 1.5 nm is found to be caused by the ALE process even at a very low ion incident energy of 20 eV in the simulation. The thickness of a damaged-layer on the etched surface slightly increases with the ion incident energy for the energy range examined in this study (20 -60 eV), and Cl atoms deposited on the surface in the ALE adsorption step are transported deeper in the damaged-layer by the ion bombardment. Our simulation results indicate that a certain damage formation cannot be avoided on the ' as-etched ' surface of a PA-ALE process and, if the damaged-layer inadvertently affects the device performance, further action to mitigate the damage needs to be taken.

Published under an exclusive license by the AVS. https://doi.org/10.1116/6.0001117

## I. INTRODUCTION

Recent advances in semiconductor technology have continued to drive the miniaturization of semiconductor devices and their minimum dimensions are now approaching the atomic size, i.e., the fundamental physical limit of miniaturization. Therefore, the industry is now adopting new device technologies such as threedimensional structures and the use of nonconventional materials to improve their performance further. Accordingly, the mass manufacturing of such devices is facing tremendous challenges in developing highly precise and controllable processing technologies. 1

(ALD) 2,3 and the latter is called atomic layer etching (ALE). 4 -11 In a typical ALP, once a monolayer (or a very thin layer close to a monolayer) of the material is deposited or etched, the process automatically stops and the subsequent step will not occur unless it receives a trigger to proceed further. This is called a self-limiting feature of the ALP.

Some of the promising solutions to such manufacturing challenges are atomic layer processes (ALPs), i.e., cyclic processes of the formation of a uniform film with a near monolayer (ML) thickness, or the removal of a material with a near monolayer thickness at specific locations. The former is called atomic layer deposition

Plasma technologies 12,13 are often used to materialize ALPs. Plasma processing 14 18 -has been widely used for deposition and etching technologies in semiconductor manufacturing. Plasmas generate ions and radicals that can physically and chemically modify the surface typically at low surface temperatures. Unlike thermal ALPs, 11,19 -25 which require surface heating, plasma-assisted ALPs are suited for low-temperature processes. One of the problems of plasma processing in the era of nanoscale devices is, however, the damage formation on the processed surface 26 -30 caused by ion bombardment.

<!-- image -->

CrossMark

28 April 2025 14:43:34

<!-- image -->

The goal of this study is to understand the damage formation by low-energy ion bombardment used in silicon (Si) plasma-assisted ALE (PA-ALE) based on chlorine (Cl) adsorption. Figure 1 shows a schematic process flow of such an ALE process. In the adsorption step, a Si surface is exposed to a Cl-containing plasma or Cl2 gas and its surface is chlorinated. This is to activate the surface by weakening the binding energies of surface atoms. If a Cl-containing plasma is used without bias voltage in this step, the surface is chlorinated by Cl radicals as well as Cl þ ions incident upon the surface at the plasma potential energy. If a Cl2 gas is used, Cl2 molecules are dissociated at the Si surface and only the top layer gets chlorinated. Under the ideal conditions, no etching occurs in the adsorption step. In the desorption step, the surface is irradiated with low-energy Ar þ ions and the Cl modified surface may be removed by the impact. Because our aim is to remove the Cl modified surface layer only, the incident Ar þ ions should not be energetic enough to etch a bare Si surface. Once the Cl modified surface is depleted, the etching is expected to stop. This defines the self-limit feature of ALE. These two steps form a single cycle of ALE, which is repeated a number of times until the desired etching depth is achieved.

Effects of ion impact on a material surface have been widely studied by ion beam experiments. 31 For example, detailed studies were performed to determine the sputtering yields of Si by Ar þ or Cl þ ions, 32 -38 and chlorinated Si surfaces by Ar þ ions, 39,40 for a wide range of ion incident energy. Molecular dynamics (MD) simulations 41 -43 were also used to study such systems and their results 42,44 -48 are in good agreement with the experimental observations in general. Therefore, the basic nature of the desorption step of Si PA-ALE by Cl adsorption has been reasonably well understood. What we attempt to clarify in this study is how the etched surface of the preceding cycles affects the outcome of the following ALE cycles, depending on the ion incident energy. To achieve this goal, we also use MD simulation in this study.

Earlier experimental studies of PA-ALE by halogen adsorption were first reported by Horiike et al. 49,50 in 1990 and several studies on PA-ALE by Cl adsorption followed. 51 -56 In these experiments, Cl2 gas was used in the adsorption step, depositing a thin layer of Cl atoms on the Si surface. Thus, the measured etch per cycle (EPC), i.e., the averaged etched depth in a single ALE cycle, was small. A more recent study by Tan et al. 57 used a Cl plasma in the adsorption step, which led to the formation of a relatively thick Cl -Si mixed layer on the surface and exhibited a higher EPC. MD simulations 45,58 and simulations based on other models 59 -63 were also used to study PA-ALE of Si by Cl adsorption. Athvale and Economou 58 first performed an MD simulation of an ALE process. They briefly discussed the surface damage of Si PA-ALE but focused only on the first cycle. Kubota et al. 45 examined the reaction pathways of the desorbed species. A recent study by Huard et al. 61 used a hybrid plasma equipment model to study the factors affecting ideal ALE processes. Sherpa et al. 62 examined a Cl adsorption step by ab initio MD simulation. Berry et al. 63 used Monte Carlo simulations to investigate the effect of ion impact angle on the ALE window. Regarding the past studies on PA-ALE for other materials, the reader is referred to, e.g., Refs. 64 -70 for SiO2, Refs. 70 -79 for SiN, and Refs. 80 -83 for metal oxides.

Most of the previous simulation studies on PA-ALE focused only on the first ALE cycle and there was no extensive discussion on the magnitude of surface damage formed over multicycle ALE. In this study, we performed MD simulations for multicycle Si PA-ALE processes to assess the surface damage formation. The rest of the article is organized as follows. Section II presents an outline of the MD simulation used in this study. Section III gives the MD simulation results for multicycle Si PA-ALE processes with Cl adsorption under various conditions. Finally, the conclusions are given in Sec. IV.

## Adsorption Step

## Desorption Step

FIG. 1. Single cycle of Si PA-ALE by Cl adsorption and Ar þ ion irradiation. Each cycle consists of the adsorption step, where the Si surface is modified by incident Cl atoms and/or ions, and the desorption step, where the Cl modified surface is removed by low-energy Ar þ ion impact. Here, gray, orange, and blue spheres represent Si, Cl, and Ar atoms (or ions), respectively.

<!-- image -->

28 April 2025 14:43:34

<!-- image -->

## II. MD SIMULATION

MD simulation 41,43 was employed to reproduce PA-ALE of Si by Cl adsorption. The details of the simulation were discussed in previous publications. 46,47,84 -89 The interatomic potential functions for the Si -Cl -Ar system used in this study are the same as those used in Ref. 89. The interatomic potential functions for ions are assumed to be the same as those for the corresponding chargeneutral atoms for the sake of simplicity. An incident Ar þ ion is

<!-- image -->

FIG. 2. Si substrates after Cl deposition MD simulations. (a) Crystalline Si substrate model with a (100) top surface at 300 K after it was exposed to 0.1 eV Cl atoms with an atomic dose of 0 94 : /C2 10 15 cm /C0 2 in MD simulation. (b) Depth profiles of atomic densities corresponding to (a). (c) Crystalline Si substrate model with a (100) top surface at 300 K after it was exposed to 20 eV Cl þ ions with an ion dose of 9 4 : /C2 10 15 cm /C0 2 in MD simulation. (d) Depth profiles of atomic densities corresponding to (c). In both (a) and (c), the angle of incidence of the impinging ions was normal to the initial (100) Si surface. The depth is measured from the position of the top (100) surface of the initial Si substrate prior to the deposition of Cl. The atomic density was obtained as a moving average with an interval of 3 Å as a function of the depth. The Cl adsorption conditions for (a) and (c) are called the ' thin Cl layer deposition ' and ' thick Cl layer adsorption ' in this article.

<!-- image -->

<!-- image -->

<!-- image -->

considered to be charge-neutralized right before it impacts upon the Si surface owning to the Auger emission process.

The top surface prior to the ALE process examined in this study is the (100) crystalline Si surface. The model substrate has a top surface with an area of 3 26 : /C2 3 26 nm 2 : and the initial substrate depth is 2.72 nm. Periodic boundary conditions are imposed in the horizontal directions, such that the model surface emulates a large surface of the actual substrate. The substrate is kept sufficiently deep (if necessary, additional layers of Si atoms are added from the bottom automatically) during the simulation so that the injection of particles (i.e., ions or charge-neutral species) would not affect the motions of atoms near the bottom of the substrate. The initial temperature of the substrate is set at 300 K. The simulation is composed of repeated ' injection cycles, ' in each of which an ion or charge-neutral species is injected into the substrate with a predetermined incident kinetic energy at a random horizontal location of the substrate surface. The angle of incidence is set perpendicular to the substrate surface.

The duration of each injection cycle is 2000 fs. Newton s equa-' tion of motion is solved for each particle in the system, except for the atoms located in the two monolayers at the bottom of the substrate. The atoms in these layers are fixed in position to prevent the substrate from moving downward due to the momentum transfer from the incident particles. A variable time step is used in the simulation code to ensure the accuracy of the simulation and the typical time step employed in this study is 0.4 fs.

In each injection cycle, the MD simulation is performed under the constant-total-energy (i.e., microcanonical) conditions for the first 300 fs. During this period, we have confirmed that the substrate temperature increases due to the particle injection and most surface chemical reactions (i.e., the breakage and reformation of chemical bonds) take place. After the microcanonical simulation, the system is then cooled down to the initial temperature, using the Langevin thermostat 43,90 for the subsequent 1600 fs and Berendsen thermostat for the final 100 fs with a target temperature of 300 K. We have confirmed that the simulation system successfully returns to thermodynamical equilibrium at 300 K before the subsequent injection cycle starts.

In this study, we examined two different cases for Cl adsorption. In the first case, a thin layer of Cl atoms was deposited on the

TABLE I. Simulation parameters for Si PA-ALE.

| Parameters                                            | Values                     |
|-------------------------------------------------------|----------------------------|
| Incident kinetic energy of an incident Cl atom or ion |                            |
| Thin Cl layer deposition                              | 0.1 eV                     |
| Thick Cl layer deposition                             | 20 eV                      |
| Dose of Cl atoms or ions                              |                            |
| Thin Cl layer deposition                              | 0.94 - 1.88 × 10 15 cm - 2 |
| Thick Cl layer deposition                             | 9.4 × 10 15 cm - 2         |
| Ar + ion energy                                       | 20 - 60 eV                 |
| Ar + ion dose                                         | 1.88 × 10 17 cm - 2        |
| Angle of incidence for Ar + ions Number of cycles     | Normal to the surface 6    |

28 April 2025 14:43:34

<!-- image -->

Si surface in the adsorption step, terminating nearly all Si dangling bonds on the surface. In the MD simulation, we created such a Cl monolayer by injecting a sufficiently large number of Cl atoms with a kinetic energy of 0.1 eV in the (negative) vertical direction, i.e., the direction normal to the initial substrate surface. Figure 2(a) shows a side view of a Cl-adsorbed (100) crystalline Si surface obtained from MD simulation in this way. In this particular example, 75 Cl atoms (i.e., 7 1 : /C2 10 14 cm /C0 2 ) remained on the surface. The depth profiles of Si and Cl atoms of (a) are given in (b). The horizontal axis represents the atomic density and the vertical axis represents the depth (in negative values). The atomic density here is evaluated as a moving average over an interval of 3 Å as a function of the depth. It is seen that nearly all Cl atoms were bonded with Si atoms on the top layer. In experiments, such a layer may be formed by the exposure of a clean Si surface to Cl2 gas. The thin Cl layer of Fig. 2(a) represents the final atomic configuration

## Thin Cl layer deposition

<!-- image -->

## Thick Cl layer deposition

FIG. 3. Changes in the substrate height as functions of the Ar þ ion dose during the desorption steps over 6 ALE cycles, obtained from MD simulations. No Cl adsorption step is included in this figure. The dark gray (blue online) curve represents the position of the Cl-adsorbed top surface. The adsorption steps for (a) and (b) were performed under the ' thin Cl layer deposition ' conditions and those for (c) and (d) were under the ' thick Cl layer deposition ' conditions. The incident Ar þ ion energy in the desorption steps for (a) and (c) is 20 eV and that for (b) and (d) is 50 eV . The vertical axis represents the substrate height (i.e., the position of the top surface), measured from the position of the initial (100) Si surface, denoted by the horizontal dashed line. The horizontal axis is proportional to the Ar þ ion dose, whose cycle number is denoted by C n with n ¼ 1 , . . . , 6 for the n th cycle. The Ar þ ion dose in each cycle is 1 88 : /C2 10 17 = cm 2 . The light gray (orange online) curve represents the position of the top Si surface subject only to Ar þ ion bombardment (i.e., without Cl layer adsorption steps). The dashed vertical lines delineate separate cycles.

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

of the adsorption step of the first ALE cycle in this case. In later cycles, where the surface may be rough and no longer crystalline due to the ion bombardment in the preceding cycles, we also performed similar MD simulations to emulate the adsorption steps. As the surface became rough and more active sites for Cl adsorption appeared in later cycles, we varied the atomic Cl dose to ensure that a Cl monolayer was formed on the surface in the adsorption step of each cycle.

In the second case, a thick Cl-containing layer was formed with 20 eV Cl þ ion injection in MD simulation. As in the cases of (a) and (b) of Fig. 2, ions were injected in the direction normal to the substrate surface and the total number of injected Cl þ ions were 1000 (i.e., 9 4 : /C2 10 15 cm /C0 2 ) and the number of Cl atoms that remained on or under the Si surface was 704 (i.e., 6 6 : /C2 10 15 cm /C0 2 ). Figure 2(c) shows a side view of the Si substrate surface after this simulation and (d) shows the corresponding depth profiles of atomic densities. It is seen that a layer of mixed Cl and Si atoms with a thickness of about 2 nm is formed on the Si surface. In experiments, such a layer may be formed by the exposure of a clean Si surface to a chlorine-containing plasma. The relatively thick Cl layer of Fig. 2(c) represents the final atomic configuration of the adsorption step of the first ALE cycle in this case. As in the first case, in later cycles, we also performed the same MD simulations to emulate the adsorption steps of this case. The Cl deposition processes of the first and second cases above will be referred to hereinafter as the ' thin Cl layer deposition ' and ' thick Cl layer deposition ' in this article.

## Thin Cl layer deposition

<!-- image -->

FIG. 4. Changes in the etched depth (black) and surface concentration of Cl atoms (blue) as functions of the Ar þ ion dose in the desorption step. Here, the etched depth is defined as the position of the top surface measured from its position at the end of the previous desorption step. The ALE conditions for (a) -(d) are the same as those for (a) -(d) of Fig. 3, respectively. The results shown here are the averages of those over C3 -C6 cycles.

<!-- image -->

After the Cl adsorption step, 20 000 Ar þ ions (corresponding to an ion dose of 1 88 : /C2 10 17 cm /C0 2 ) were injected into the Cl-adsorbed surface to remove the chlorinated Si layer. The Ar þ ion energy was varied from 20 to 60 eV in both cases. The angle of incidence was normal to the substrate surface. A summary of the simulation parameters is given in Table I.

## III. RESULTS AND DISCUSSION

## A. Changes in etched depth

Changes in etched depth during the desorption steps of Si PA-ALE obtained from MD simulations are summarized in Fig. 3. The dark gray (blue online) curve represents the position of the Cl-adsorbed top surface (i.e., substrate height) as a function of the Ar þ ion dose in the desorption steps over six ALE cycles. No adsorption step is shown in this figure. The substrate height is measured from the position of the initial crystalline Si surface prior to the first Cl adsorption step, as in Fig. 2. The Ar þ ion dose in the horizontal axis is denoted by the cycle number ' C n ' with n ¼ 1, . . . , 6 for the n th ALE cycle. Each cycle corresponds to an Ar þ ion does of 1 88 : /C2 10 17 = cm 2 . The origin of the horizontal axis is the beginning of the desorption step of the first ALE cycle (C1). Its end, marked by a dashed vertical line, is also the beginning of the desorption step of the second ALE cycle (C2). Later cycles are also delineated by vertical dashed lines. The sudden increase in the dark gray (blue online) curve at each vertical line indicates the increase of the surface height due to the Cl adsorption step not shown in this figure. The adsorption steps of (a) and (b) were performed under the ' thin Cl layer deposition ' conditions while those of (c) and (d) were under the ' thick Cl layer deposition ' conditions. The ion incident energies in the desorption steps were 20 for (a) and (c) and 50 eV for (b) and (d).

The Si etching by Ar þ ion bombardment only, i.e., without Cl deposition, was also simulated to differentiate the Cl effects on the ALE process. The light gray (orange online) curve represents the position of the Si top surface subject to Ar þ ion physical sputtering only as a function of the Ar þ ion dose. The ion energy for (a) and (c) is 20 eV and that for (b) and (d) is 50 eV.

It is seen in Fig. 3(a) that the etched depth in a single cycle increased initially and became nearly constant in later cycles. This is because Ar þ ion bombardment in the first two cycles roughened the Si surface and created more active sites that can be bonded with Cl atoms in the subsequent adsorption cycles. This process formed a thicker Si -Cl mixed layer that can be more readily removed in the subsequent desorption step than crystalline Si. 62 A similar trend is also seen in (c) but to less extent. Light gray (orange online) in (a) and (c) show that Si was hardly etched by 20 eV Ar þ ions. It is also seen that Ar þ ion bombardment amorphized the surface and increased the volume of the surface region, resulting in a surface higher than the initial crystalline surface.

For 50 eV Ar þ ion bombardment, there is no notable difference in the slope between the etched depths with and without Cl adsorption. Especially in (c) for the thin Cl layer deposition, the etching was essentially due to physical sputtering only. This is because 50 eV energy is sufficiently high to etch a pristine Si surface for about a nanometer over this ion dose. In (d), for the thick Cl layer deposition, it is seen that an Si -Cl mixed layer was

FIG. 5. EPCs of Si PA-ALE processes obtained from MD simulations as functions of Ar þ ion incident energy. The solid and dashed lines represent those for the thin and thick Cl layer deposition cases. Other ALE conditions are listed in Table I. The value of EPC given here is the average of etched depths per cycle from C3 to C6.

<!-- image -->

removed in the very early stage of each desorption step and the etching became essentially due to physical sputtering for the remaining period of the step.

The etched depth and surface concentration of Cl atoms in a single ALE cycle averaged from the third to sixth cycle are plotted in Fig. 4 as functions of the Ar þ ion dose in the desorption step. Here, the etched depth is defined as the position of the top surface measured from its position at the end of the previous desorption step. In this figure, the etched depth is plotted only when it takes a positive value. As in Fig. 3, (a) and (b) are for the thin Cl layer

FIG. 6. Atomic configurations and the corresponding atomic-density depth profiles at the end of the first ALE cycle (C1) with the thin Cl layer deposition and 20 eV Ar þ ion bombardment. The other conditions are the same as those in Table I. The gray, red, and blue spheres represent Si, Cl, and Ar atoms, respectively. The depth profile was obtained in the same way as in Fig. 2.

<!-- image -->

FIG. 7. Thicknesses of damaged-layers formed during the Si PA-ALE processes, obtained from MD simulations, as functions of the Ar þ ion incident energy. The solid and dashed lines represent those for thin and thick Cl layer deposition cases. Other ALE conditions are listed in Table I. The value of the thickness here is the average of those over all six cycles, i.e., from C1 to C6.

<!-- image -->

<!-- image -->

deposition case and (c) and (d) are for the thick Cl layer deposition case. The incident Ar þ ion energy is 20 eV for (a) and (c) and 50 eV for (b) and (d). At low Ar þ ion incident energy, it is seen that, with the increasing Ar þ ion dose, the etched depth in (a) increased slowly with a weakly decreasing slope, whereas the etched depth in (c) increased rapidly with a clear sign of saturation, i.e., the self-limit. The surface concentrations of Cl atoms also decreased slowly and nearly one-half of the initial Cl atoms remained on the surface at the end of the ALE cycle in (a), whereas the surface concentrations of Cl atoms in (c) decreased sharply with the Ar þ ion dose. It should be noted, however, that, even in the case of (c), a small amount of Cl, with a surface concentration similar to that in (a), still remained on the Si surface at the end of the ALE cycle.

At high Ar þ ion incident energy, it is seen in (b) that, with a small amount of Cl deposited in the adsorption step, the etched depth monotonically increased all throughout the Ar þ ion injection, indicating that physical sputtering dominates the etching process. In (d), where a larger amount of Cl was deposited in the adsorption step, the etched depth increased drastically until about 5 /C2 10 16 cm /C0 2 and then increased monotonically in the same way as in (b). In both cases, the density of Cl atoms at the end of the ALE cycle is almost negligible. This shows that, as we saw in Fig. 3, no self-limit took place with 50 eV Ar þ ions.

The EPCs with the thin and thick Cl layer deposition conditions obtained from MD simulations are summarized in Fig. 5 as functions of the Ar þ ion energy. The figure shows that the EPC is higher in the thick Cl layer deposition case than in the thin Cl layer deposition case, indicating that the thickness of the chlorinated layer is an important factor in determining the EPC. The simulated EPCs at 20 eV Ar þ ion energy with thin and thick Cl layer deposition cases are 1.6 and 4.2 Å/cycle. In terms of the thickness of a single monolayer (ML) of Si (i.e., 1.36 Å), these correspond to 1.2 and 3.0 ML/cycle. No ALE window 54 -57 was observed in our simulation.

## B. Damage formation

The depth profiles after each ALE cycle were used to measure the surface damage formed during the ALE processes. Figure 6 shows the atomic configurations of the substrate and the corresponding atomic-density depth profiles after the first ALE cycle (C1) with the thin Cl layer deposition and 20 eV Ar þ ion bombardment. To characterize the damage formation, the thickness of the

<!-- image -->

## Thick Cl layer\_deposition

FIG. 8. Dominant desorbed species during the desorption steps for different Ar þ ion energies in the thin (a) and thick (b) Cl layer deposition cases. Reflected or desorbed Ar ions or atoms are not counted.

<!-- image -->

28 April 2025 14:43:34

<!-- image -->

damaged-layer was measured from the depth profile, as illustrated in the figure, which is 1.5 nm in this case. In this article, the damaged-layer thickness is defined as the penetration depth of Cl or Ar atoms measured from the etched surface.

Figure 7 shows the damaged-layer thicknesses as functions of the Ar þ ion incident energy for the thin (solid lines) and thick (dashed lines) Cl layer deposition cases. The damaged-layer thickness was averaged over the first six cycles (i.e., from C1 to C6) under each ALE condition. Considering the uncertainty arising from the cycle-to-cycle variations, we can conclude from this figure that, for both thin and thick Cl layer deposition cases, the damaged-layer thicknesses weakly and more-or-less linearly increase with the increasing incident ion energy in the energy range studied here. With an increasing ion incident energy, the penetration depths of Ar þ ions and recoiled Cl atoms increase but so do the etch rates. In other words, a large part of the damaged-layer formed during the desorption step is etched away at high ion incident energy. It is also seen that the damaged-layer is slightly thicker in the thick Cl layer deposition case.

The fact that, in both thin and thick Cl deposition cases, the observed damaged-layer thickness was about 1.5 nm (i.e., approximately 11 Si monolayers) even at 20 eV ion incident energy can be problematic. The damaged-layer thickness observed here is significantly higher than the corresponding EPC at 20 eV ion energy and comparable at 60 eV. Therefore, the ALE damage formation may not be ignored in actual applications.

## Thin Cl layer deposition

FIG. 9. Numbers of desorbed species as functions of the Ar þ ion dose during the desorption step of the 6th cycle (C6) of Si PA-ALE processes. The ALE conditions are the same as those in Table I. The vertical axis denotes the accumulated number of species desorbed from a unit area of the substrate surface during the desorption step of this cycle. The adsorption steps for (a) and (b) are the thin Cl layer deposition and those for (c) and (d) are the thick Cl layer deposition. The incident energy of Ar þ ions is 20 eV for (a) and (c) and 50 eV for (b) and (d).

<!-- image -->

<!-- image -->

## C. Desorbed species

We also analyzed the desorbed species during the ALE processes to understand the etching mechanisms better. Figure 8 shows the percentage of the number of desorbed species in the ALE desorption steps obtained from MD simulations. Here, (a) is for the thin Cl layer deposition case and (b) is for the thick Cl layer deposition case. Any species emitted from the surface has a form of Ar or Si Cl n m with n and m being non-negative integers. The total number of emitted species in the form of Si n Cl m during the sixth cycle (C6) examined here corresponds to 100%. No Ar atom or ion emitted or reflected from the surface is counted because most of the incident Ar þ ions are reflected once they hit the surface. The dominant desorbed species are listed on the horizontal axis.

As it is seen in Fig. 8(a), only a small percentage of Cl bonded Si species such as SiCl and SiCl2 desorbed from the surface. This is most likely due to the limited availability of Cl atoms on the surface under the thin Cl layer deposition conditions. The percentage of monoatomic Si atoms as desorbed species increases with the increasing Ar þ ion energy, which indicates that physical sputtering of Si by Ar þ ion impact dominates at higher ion incident energy.

It is seen in (b), where more Cl atoms are available for surface reactions, that desorbed species with higher Cl content, including SiCl3 and SiCl4, are more visible. The percentage of monoatomic Si atoms also increases with the increasing Ar þ ion energy, as in (a). These results indicate that ALE with the thick Cl layer deposition is enhanced by chemical etching, i.e., the formation of more SiCl m ( m ¼ 1, … ,4), due to the abundant presence of Cl atoms supplied during the adsorption step.

Figure 9 shows the accumulated numbers of desorbed species in the desorption step of C6 as functions of the Ar þ ion dose under various conditions. The vertical axis denotes the accumulated number of each species desorbed from a unit area of the substrate surface measured from the beginning of the desorption step. The adsorption steps for (a) and (b) are the thin Cl layer deposition and those for (c) and (d) are the thick Cl layer deposition, as given in Table I. The incident energy of Ar þ ions is 20 eV for (a) and (c) and 50 eV for (b) and (d).

It is seen in (a) that the dominant desorbed species is monoatomic Cl and the accumulated numbers of desorbed monoatomic Si atoms and SiCl radicals, which are the next highest after monoatomic Cl, are almost the same initially. However, as the amount of Cl on the surface depletes, the rates of desorption for SiCl and SiCl2 decrease while monoatomic Si atoms continue to desorb. Furthermore, the desorption rate of monoatomic Si decreases as that of monoatomic Cl also decreases. It should be noted that the desorption of monoatomic Si does not mean the etching is purely due to physical sputtering. As we have seen in Fig. 3, the physical sputtering yield of Si by 20 eV Ar þ ion bombardment is null essentially. The enhanced desorption of monoatomic Si atoms is likely caused by the bond breaking of Si atoms by Cl atoms remaining in the substrate.

With more abundant Cl species on the surface, we observe in (c) that Si atoms mostly desorb as Cl bonded species in an early stage of the desorption step. At 50 eV Ar þ ion injection, as seen in (b) and (d), the desorption of SiCl m is observed only in the very early stage of the Ar þ ion injection. On the other hand, the desorption of monoatomic Si continues to increase with the

Ar þ ion dose due to physical sputtering. This is consistent with the observation in Fig. 3.

## IV. CONCLUSIONS

We performed MD simulations of PA-ALE processes of Si with Cl adsorption under various conditions and examined the effects of the amount of deposited Cl and Ar þ ion incident energy on the etch rates, values of EPC, and damage layer formation.

In this study, we used a rather large Ar þ ion dose of 1 88 : /C2 10 17 cm /C0 2 to clarify the self-limit feature of the PA-ALE process. The ion flux Γ i from an Ar plasma may be given approximately by

$$\Gamma _ { i } = n _ { e } u _ { B },$$

where ne and uB ¼ ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi ffi kBTe = M p are the electron density and Bohm velocity with kB , Te , and M being the Boltzmann constant, electron temperature, and Ar mass, respectively. For a typical inductively coupled plasma (ICP) 91 with Te ¼ 5 eV and ne ¼ 2 0 : /C2 10 11 cm /C0 3 , we obtain Γ i ¼ 7 0 : /C2 10 14 cm /C0 2 s /C0 1 , i.e., an ion current of 0.11 mA/cm . 2 With this ion flux, the duration of the desorption step with an Ar þ ion dose of 1 88 : /C2 10 17 cm /C0 2 is 270 s or 4.5 min. Since few past publications on PA-ALE experiments presented the ion flux used in their studies, it is not clear how realistic our simulation results are. However, based on the plasma conditions reported in those publications, we surmise that the present study uses rather extended desorption steps, compared with typical PA-ALE experiments.

Figures 3(a), 4(a), and 9(a) show that, in the thin Cl layer deposition case, the self-limit was not observed at 20 eV Ar þ ion injection even with this long desorption step. Figures 4(a) and 9(a) seem to imply that the etched depth and the amount of desorbed Cl were going to saturate and the self-limit could have occurred eventually. However, nearly a half of the original amount of Cl desorbed on the surface would remain in the substrate even in the self-limit state. On the other hand, as seen in Figs. 3(c), 4(c), and 9(c), with a larger amount of Cl on the surface, the etched depth and desorbed species reached their steady states and the self-limit of PA-ALE was achieved during the desorption step. At 20 eV Ar þ ion irradiation, it took this long desorption time to show the self-limit under our simulation conditions.

At 50 eV Ar þ ion irradiation, the physical sputtering yield of Si may not be negligible. The data compiled by Yamamura and Tawara 37 suggest that the Si sputtering yield at 50 eV Ar þ ion bombardment is about 0.01. In our simulation, it is shown to be about 0.025. As shown in (b) and (d) of Fig. 3, the etched depth purely by Si physical sputtering during this desorption period is about 1 nm, based on our MD simulation. Even if our MD simulation overestimates the etch rate at this ion energy, the etched depth during this desorption period is likely to be at least a few angstroms. This means that, if the EPC is about a monolayer (i.e., 1.36 Å), physical sputtering cannot be ignored in this energy range unless the desorption time or ion flux is kept small significantly. 56 As seen in Fig. 3(d), with a sufficient amount of Cl on the surface, chemically enhanced etching occurs at a very early stage of each desorption step, which would make the depth change look more self-limiting if the desorption time were sufficiently short.

28 April 2025 14:43:34

<!-- image -->

The results of our study thus indicate that, to obtain an etch stop in a single ALE cycle (i.e., self-limit), one has to employ the right combination of the amount of Cl deposited in the adsorption step and the ion energy in the desorption step. If the amount of adsorbed Cl is too low or the ion energy is too high, physical sputtering dominates during the desorption step. In the opposite case, either no etching occurs or etching takes place too slowly to deplete the deposited Cl atoms and does not exhibit a self-limiting etch stop during the desorption step. In general, a sufficient amount of Cl needs to be adsorbed or deposited in the adsorption step to have a sufficiently high chemical etch rate compared with the physical sputtering rate of pristine Si at the given Ar þ ion energy.

As seen in Fig. 5, in our MD simulation, we did not observe an ALE window, which has been reported in earlier experimental studies 54 57 -under various conditions. It is not clear why we did not observe it even with a sufficiently long desorption time. Indeed, above 40 eV, the major part of the EPC shown in Fig. 5 is due to physical sputtering in this figure. (In the thin Cl layer deposition case, EPC is nearly entirely due to physical sputtering at or above 40 eV.) Our simulations have shown that a chlorinated Si layer has a higher etch rate than the physical sputtering rate of pristine Si but the chemical etch rate also depends on the Ar þ ion energy. Such a difference in the etch rate of chlorinated Si is reflected in the difference in EPC between 20 and 30 eV of Fig. 5. Another possible reason is the lack of thermal desorption of Si in our MD simulation. As discussed earlier, our MD simulation quenches the system soon after the sputtering or emission of surface atoms occurs by a single ion impact, which prevents slow thermal desorption of surface atoms and moieties. At low ion incident energy, where the etch rate due to the direct Ar þ ion impact is sufficiently low, the contribution from thermal processes may not be negligible. Detailed discussion on the lack of ALE windows in our simulation is the subject of a future study.

The damaged-layer thickness, i.e., the thickness of a subsurface region where recoiled Cl (and possibly Ar) atoms remain after the ALE, is plotted in Fig. 7. Under the conditions that we examined, the damaged-layer thickness was higher than 1.5 nm and a weakly increasing function of the ion energy. The difference in the damaged-layer thicknesses between the thin and thick Cl layer deposition cases was not particularly large. As shown in Fig. 6, the density of Cl atoms in the damaged-layer is about 0 5 : /C2 10 22 cm /C0 3 . Because the damaged-layer thickness is significantly larger than the EPC at low ion incident energy and at best comparable with the EPC at relatively high ion energy, the formation of a damaged-layer whose thickness is not negligible compared with the EPC is unavoidable for all the energy range examined here. Depending on the device structures to which such ALE processes are applied, the damage formation may affect device performance.

## ACKNOWLEDGMENTS

This work was partially supported by the Japan Society of the Promotion of Science (JSPS) Grant-in-Aid for Scientific Research (S) (No. 15H05736) and (A) (No. 21H04453), and the JSPS Core-to-Core Program (No. JPJSCCA2019002). E.J.C.T. also appreciates financial support from the Ministry of Education, Culture, Sports, Science and Technology (MEXT) of Japan for her graduate study.

## DATA AVAILABILITY

The data that support the findings of this study are available from the corresponding author upon reasonable request.

## REFERENCES

- 1 G. S. Oehrlein and S. Hamaguchi, Plasma Sources Sci. Technol. 27 , 023001 (2018).
- 2 S. M. George, Chem. Rev. 110 , 111 (2010).
- 3 H. C. M. E. Knoops, T. Faraz, K. Arts, and W. M. M. Kessels, J. Vac. Sci. Technol. A 37 , 030902 (2019).
- 4 S. U. Engelmann, R. L. Bruce, M. Nakamura, D. Metzler, S. G. Walton, and E. A. Joseph, ECS J. Solid State Sci. Technol. 4 , N5054 (2015).
- 5 T. Faraz, F. Roozeboom, H. C. M. Knoops, and W. M. M. Kessels, ECS J. Solid State Sci. Technol. 4 , N5023 (2015).
- 6 K. J. Kanarik, T. Lill, E. A. Hudson, S. Sriraman, S. Tan, J. Marks, V. Vahedi, and R. A. Gottscho, J. Vac. Sci. Technol. A 33 , 020802 (2015).
- 7 G. S. Oehrlein, D. Metzler, and C. Li, ECS J. Solid State Sci. Technol. 4 , N5041 (2015).
- 8 K. Ishikawa, et al. , Jpn. J. Appl. Phys. 56 , 06HA02 (2017).
- 9 R. J. Gasvoda, Z. Zhang, S. Wang, E. A. Hudson, and S. Agarwal, J. Vac. Sci. Technol. A 38 , 050803 (2020).
- 10 X. Sang and J. P. Chang, J. Phys. D: Appl. Phys. 53 , 183001 (2020).
- 11 S. M. George, Accounts Chem. Res. 53 , 1151 (2020).
- 12 I. Adamovich et al. , J. Phys. D: Appl. Phys. 50 , 323001 (2017).
- 13 K.-D. Weltmann, et al. , Plasma Process. Polym. 16 , 1800118 (2019).
- 14 B. N. Chapman, Glow Discharge Processes: Sputtering and Plasma Etching (Wiley, New York, 1980).
- 15 S. Hamaguchi, IBM J. Res. Develop. 43 , 199 (1999).
- 16 M. A. Lieberman and A. J. Lichtenberg, Principles of Plasma Discharges and Materials Processing , 2nd ed. (Wiley, New Jersey, 2005).
- 17 K. Nojiri, Dry Etching Technology for Semiconductors (Springer, New York, 2015).
- 18 T. Makabe and Z. L. Petrovic, Plasma Electronics (Routledge, Florida, 2016).
- 19 Y. Lee and S. M. George, ACS Nano 9 , 2061 (2015).
- 20 Y. Lee and S. M. George, J. Phys. Chem. C 123 , 18455 (2019).
- 21 M. Konh, C. He, X. Lin, X. Guo, V. Pallem, R. L. Opila, A. V. Teplyakov, Z. Wang, and B. Yuan, J. Vac. Sci. Technol. A 37 , 021004 (2019).
- 22 A. H. Basher, Marjan Krsti, T. Takeuchi, M. Isobe, T. Ito, M. Kiuchi, K. Karahashi, W. Wenzel, and S. Hamaguchi, J. Vac. Sci. Technol. A 38 , 022610 (2020).
- 23 A. H. Basher, Marjan Krsti, K. Fink, T. Ito, K. Karahashi, W. Wenzel, and S. Hamaguchi, J. Vac. Sci. Technol. A 38 , 052602 (2020).
- 24 A. H. Basher, I. Hamada, and S. Hamaguchi, Jpn. J. Appl. Phys. 59 , 090905 (2020).
- 25 R. Sheil, J. M. P. Martirez, X. Sang, E. A. Carter, and J. P. Chang, J. Phys. Chem. C 125 , 1819 (2021).
- 26 T. Ohchi, S. Kobayashi, M. Fukasawa, K. Kugimiya, T. Kinoshita, T. Takizawa, S. Hamaguchi, Y. Kamide, and T. Tatsumi, Jpn. J. Appl. Phys. 47 , 5324 (2008).
- 27 T. Ito, K. Karahashi, M. Fukasawa, T. Tatsumi, and S. Hamaguchi, Jpn. J. Appl. Phys. 50 , 08KD02 (2011).
- 28 T. Ito, K. Karahashi, K. Mizotani, M. Isobe, S.-Y. Kang, M. Honda, and S. Hamaguchi, Jpn. J. Appl. Phys. 51 , 08HB01 (2012).
- 29 K. Mizotani, M. Isobe, and S. Hamaguchi, J. Vac. Technol. A 33 , 021313 (2015).
- 30 K. Mizotani, M. Isobe, M. Fukasawa, K. Nagahata, T. Tatsumi, and S. Hamaguchi, J. Phys. D: Appl. Phys. 48 , 152002 (2015).
- 31 K. Karahashi and S. Hamaguchi, J. Phys. D: Appl. Phys. 47 , 224008 (2014).
- 32 S. Tachi, K. Miyake, and T. Tokuyama, Jpn. J. Appl. Phys. 20 , L411 (1981).
- 33 P. C. Zalm, J. Appl. Phys. 54 , 2660 (1983).
- 34 S. Tachi and S. Okudaira, J. Vac. Sci. Technol. B 4 , 459 (1986).
- 35 D. J. Oostra, A. Haring, R. P. van Ingen, and A. E. de Vries, J. Appl. Phys. 64 , 315 (1988).

<!-- image -->

- 36 M. Balooch, M. Moalem, W.-E. Wang, and A. V. Hamza, J. Vac. Sci. Technol. A 14 , 229 (1996).
- 37 Y. Yamamura and H. Tawara, Atom. Data Nucl. Data 62 , 2 (1996).
- 38 T. Ito, K. Karahashi, S.-Y. Kang, and S. Hamaguchi, J. Vac. Sci. Technol. A 31 , 031301 (2013).
- 39 J. P. Chang and H. H. Sawin, J. Vac. Sci. Technol. A 15 , 610 (1997).
- 40 J. A. Levinson, E. S. G. Shaqfeh, M. Balooch, and A. V. Hamza, J. Vac. Sci. Technol. B 18 , 172 (2000).
- 41 J. M. Haile, Molecular Dynamics Simulation: Elementary Methods (Wiley, New York, 1997).
- 42 B. A. Helmer and D. B. Graves, J. Vac. Sci. Technol. A 16 , 3502 (1998).
- 43 M. P. Allen and D. J. Tildesley, Computer Simulation of Liquids , 2nd ed. (Oxford University, United Kingdom, 2017).
- 44 M. E. Barone and D. B. Graves, J. Appl. Phys. 78 , 6604 (1995).
- 45 N. A. Kubota, D. J. Economou, and S. J. Plimton, J. Appl. Phys. 83 , 4055 (1998).
- 46 H. Ohta and S. Hamaguchi, J. Chem. Phys. 115 , 6679 (2001).
- 47 H. Ohta and S. Hamaguchi, J. Vac. Sci. Technol. A 18 , 2373 (2001).
- 48 P. Brichon, E. Despiau-Pujo, and O. Joubert, J. Vac. Sci. Technol. A 32 , 021301 (2014).
- 49 Y. Horiike, T. Tanaka, M. Nakano, S. Iseda, H. Sakaue, A. Nagata, H. Shindo, S. Miyazaki, and M. Hirose, J. Vac. Sci. Technol. A 8 , 1844 (1990).
- 50 H. Sakaue, S. Iseda, K. Asami, J. Yamamoto, M. Hirose, and Y. Horiike, Jpn. J. Appl. Phys. 29 , 2648 (1990).
- 51 H. Sakaue, K. Asami, T. Ichihara, S. Ishizuka, K. Kawamura, and Y. Horiike, Mat. Res. Soc. Symp. Proc. 222 , 195 (1991).
- 52 Y. S. T. Matsuura, J. Murota, and T. Ohmi, Appl. Phys. Lett. 20 , 2803 (1993).
- 53 S. D. Athvale and D. J. Economou, J. Vac. Sci. Technol. B 14 , 3702 (1996).
- 54 B.-J. Kim, S. Chung, and S. M. Cho, Appl. Surf. Sci. 187 , 124 (2002).
- 55 S. D. Park, D. H. Lee, and G. Y. Yeom, Electrochem. Solid-State Lett. 8 , C106 (2005).
- 56 S.-D. Park, K.-S. Min, B.-Y. Yoon, D.-H. Lee, and G.-Y. Yeom, Jpn. J. Appl. Phys. 44 , 389 (2005).
- 57 S. Tan, W. Yang, K. J. Kanarik, T. Lill, V. Vahedi, J. Marks, and R. A. Gottscho, ECS J. Solid State Sci. Technol. 4 , N5010 (2015).
- 58 S. D. Athvale and D. J. Economou, J. Vac. Sci. Technol. A 13 , 966 (1995).
- 59 A. Agarwal and M. J. Kushner, J. Vac. Sci. Technol. A 27 , 37 (2009).
- 60 A. Ranjan, M. Wang, S. D. Sherpa, V. Rastogi, A. Koshiishi, and P. G. G. Ventzek, J. Vac. Sci. Technol. A 34 , 031304 (2016).
- 61 C. M. Huard, Y. Zhang, S. Sriraman, A. Paterson, K. J. Kanarik, and M. J. Kushner, J. Vac. Sci. Technol. A 35 , 031306 (2017).
- 62 S. D. Sherpa, P. L. G. Ventzek, M. Lee, G. S. Hwang, and A. Ranjan, J. Vac. Sci. Technol. A 36 , 031303 (2018).
- 63 I. L. Berry, K. J. Kanarik, T. Lill, S. Tan, V. Vahedi, and R. A. Gottscho, J. Vac. Sci. Technol. A 36 , 01B105 (2018).
- 64 H. Nishino, N. Hayasaka, and H. Okano, J. Appl. Phys. 74 , 1345 (1993).
- 65 S. Rauf, T. Sparks, P. L. G. Ventzek, V. V. Smimov, A. V. Stengach, K. G. Gaynnullin, and V. A. Pavlovsky, J. Appl. Phys. 101 , 033308 (2007).
- 66 D. Metzler, R. L. Bruce, S. Engelmann, E. A. Joseph, and G. S. Oehrlein, J. Vac. Sci. Technol. A 32 , 020603 (2014).
- 67 D. Metzler, C. Li, S. Engelmann, R. L. Bruce, E. A. Joseph, and G. S. Oehrlein, J. Vac. Sci. Technol. A 34 , 01B101 (2016).
- 68 M. Honda, T. Katsunuma, M. Tabata, A. Tsuji, T. Oishi, T. Hisamatsu, S. Ogawa, and Y. Kihara, J. Phys. D: Appl. Phys. 50 , 234002 (2017).
- 69 T. Tsutsumi, H. Kondo, M. Hori, M. Zaitsu, A. Kobayashi, T. Nozawa, and N. Kobayashi, J. Vac. Sci. Technol. A 35 , 01A103 (2017).
- 70 C. M. Huard, S. Sriraman, A. Paterson, and M. J. Kushner, J. Vac. Sci. Technol. A 36 , 06B101 (2018).
- 71 T. Matsuura, Y. Honda, and J. Murota, Appl. Phys. Lett. 74 , 3573 (1999).
- 72 C. Li, D. Metzler, C. S. Lai, E. A. Hudson, and G. S. Oehrlein, J. Vac. Sci. Technol. A 34 , 041307 (2016).
- 73 Y. Ishii, K. Okuma, T. Saldana, K. Maeda, N. Negishi, and J. Manos, Jpn. J. Appl. Phys. 56 , 06HB07 (2017).
- 74 S. D. Sherpa and A. Ranjan, J. Vac. Sci. Technol. A 35 , 01A102 (2017).
- 75 S. D. Sherpa, P. L. G. Ventzek, and A. Ranjan, J. Vac. Sci. Technol. A 35 , 05C310 (2017).
- 76 K. Nakane, R. H. J. Vervuurt, T. Tsutsumi, N. Kobayashi, and M. Hori, ACS Appl. Mater. Inter. 11 , 37263 (2019).
- 77 K. Shinoda, N. Miyoshi, H. Kobayashi, M. Izawa, T. Saeki, K. Ishikawa, and M. Hori, J. Vac. Sci. Technol. A 37 , 051002 (2019).
- 78 A. Hirata, M. Fukasawa, K. Kugimiya, K. Nagaoka, K. Karahashi, S. Hamaguchi, and H. Iwamoto, Jpn. J. Appl. Phys. 59 , SJJC01 (2020).
- 79 A. Hirata, M. Fukasawa, K. Kugimiya, K. Nagaoka, K. Karahashi, S. Hamaguchi, and H. Iwamoto, J. Vac. Sci. Technol. A 38 , 062601 (2020).
- 80 J. B. Park, W. S. Lim, B. J. Park, I. H. Park, Y. W. Kim, and G. Y. Yeom, J. Phys. D: Appl. Phys. 42 , 055202 (2009).
- 81 S. E. Potts, W. Keuning, E. Langereis, G. Dingemans, M. C. M. van de Sanden, and W. M. M. Kessels, J. Electrochem. Soc. 157 , P66 (2010).
- 82 M. Omura, K. Furumoto, K. Matsuda, T. Sasaki, I. Sakai, and H. Hayashi, Plasma Sources Sci. Technol. 26 , 065015 (2017).
- 83 A. Hirata, M. Fukasawa, K. Nagahata, H. Li, K. Karahashi, S. Hamaguchi, and T. Tatsumi, Jpn. J. Appl. Phys. 57 , 06JB02 (2018).
- 84 H. Yamada and S. Hamaguchi, J. Appl. Phys. 96 , 6147 (2004).
- 85 M. Taguchi and S. Hamaguchi, Thin Solid Films 515 , 4879 (2007).
- 86 Y. Murakami, S. Horiguchi, and S. Hamaguchi, Phys. Rev. E 81 , 041602 (2010).
- 87 K. Miyake, T. Ito, M. Isobe, K. Karahashi, M. Fukasawa, K. Nagahata, T. Tatsumi, and S. Hamaguchi, Jpn. J. Appl. Phys. 53 , 03DD02 (2014).
- 88 S. Numazawa, K. Machida, M. Isobe, and S. Hamaguchi, Jpn. J. Appl. Phys. 55 , 116204 (2016).
- 89 E. J. C. Tinacba, M. Isobe, K. Karahashi, and S. Hamaguchi, Surf. Coat. Technol. 380 , 125032 (2019).
- 90 T. Schneider and E. Stoll, Phys. Rev. B 17 , 1302 (1978).
- 91 V. A. Godyak, Plasma Sources Sci. Technol. 20 , 025004 (2011).