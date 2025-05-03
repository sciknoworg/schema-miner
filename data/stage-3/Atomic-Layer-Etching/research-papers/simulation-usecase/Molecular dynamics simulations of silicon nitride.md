## REGULAR PAPER

## Molecular dynamics simulations of silicon nitride atomic layer etching with Ar, Kr, and Xe ion irradiations

To cite this article: Jomar U. Tercero et al 2024 Jpn. J. Appl. Phys. 63 07SP03

<!-- image -->

## You may also like

- Pattern formation on Ge by low energy ion beam erosion Marc Teichmann, Jan Lorbeer, Bashkim -

Ziberi et al.

- Ion dynamics in capacitively coupled argon-xenon discharges M Klich, S Wilczek, J F J Janssen et al. -
- Investigation of facet evolution on Si surfaces bombarded with Xe ions Sukriti Hans, Basanta Kumar Parida, Sebin Augustine et al. -

View the article online for updates and enhancements.

<!-- image -->

## Molecular dynamics simulations of silicon nitride atomic layer etching with Ar, Kr, and Xe ion irradiations

<!-- image -->

Jomar U. Tercero * , Michiro Isobe, Kazuhiro Karahashi, and Satoshi Hamaguchi *

Division of Materials and Manufacturing Science, Osaka University, 2-1 Yamadaoka Suita, Osaka 565-0871, Japan

*

E-mail: jutercero@ppl.eng.osaka-u.ac.jp; hamaguch@ppl.eng.osaka-u.ac.jp

Received March 4, 2024; revised June 19, 2024; accepted July 1, 2024; published online July 17, 2024

Molecular dynamics simulations were performed to understand the gas-surface interactions during silicon nitride (SiN) plasma-enhanced atomic layer etching (PE-ALE) processes with argon (Ar), krypton (Kr), and xenon (Xe) ion irradiations. Changes in the surface height, penetration depths of hydrofluorocarbon (HFC) species, and damaged layer thickness were examined over five PE-ALE cycles. The results showed that the PE-ALE process with Ar + ions etched the SiN surface more efficiently than those with Kr + or Xe + ions under the otherwise same conditions. Slower etching in the case of Kr + or Xe + ion irradiation is likely caused by the accumulation of HFC species. It was also observed that the damaged layer thicknesses of the etched surfaces are nearly the same among those with Ar + , Kr + , and Xe + ion irradiations. © 2024 The Japan Society of Applied Physics

Supplementary material for this article is available online

## 1. Introduction

Plasma-enhanced atomic layer etching (PE-ALE) is a technique to etch a material s surface, ideally in a layer-by-layer ' manner, typically using surface irradiation with low-energy ions generated in a plasma formed with an inert gas such as argon (Ar). 1 -7) The PE-ALE process is made of cyclic processes involving sequential and typically self-limiting surface reaction processes. More speci /uniFB01 cally, each cycle of a PE-ALE process typically consists of adsorption and desorption steps. Some PE-ALE steps have more than two steps in a single cycle, as seen in this article later. In a typical adsorption step, the material surface to be etched is exposed to gas-phase molecules or radicals that modify the material surface. In the desorption step, the modi /uniFB01 ed surface is exposed to low-energy inert-gas ions, and some surface atoms are removed by chemically enhanced sputtering. Ideally, the energy of the incident inert-gas ions should be high enough to etch the modi /uniFB01 ed layer, but low enough to etch the pristine material surface. In this way, once the deposited species introduced in the adsorption are nearly exhausted, the etching stops, and thus a self-limiting desorption of the surface material can be achieved.

PE-ALE has been extensively studied due to its importance in meeting the current needs of the semiconductor industry. As the dimensions of advanced semiconductor devices continue to diminish and complex three-dimensional device structures are employed, demand for more precise etching to remove thin layers has increased. 8 -11) Horiike et al. performed pioneering research on PE-ALE of silicon (Si) in 1990. 12,13) In their method, the adsorption step was performed with halogen coverage and the desorption step was performed with Ar plasma irradiation. Since then, most studies on PE-ALE of Si have been performed with chlorine (Cl) adsorption. 14 -18) PE-ALE processes are often used together with more conventional reactive ion etching 19 21) -to achieve the most ef /uniFB01 cient and precise etching results.

Gaining a comprehensive understanding of PE-ALE processes is important for further development of this etching technology. In this study, we examine atomic-scale surface reactions during silicon nitride (SiN) PE-ALE processes, using numerical simulations. In what follows, the abbreviation SiN denotes a general silicon nitride with an arbitrary stoichiometry, i.e. SiN , x as typical SiN /uniFB01 lms used in the semiconductor industry are not crystalline. In a typical SiN PE-ALE process, the surface is /uniFB01 rst exposed to hydro /uniFB02 uorocarbon (HFC) precursors, which modify the material surface chemically, in its adsorption step. In the subsequent desorption step, the modi /uniFB01 ed surface layer is irradiated with lowenergy Ar ions. In the current fabrication methods, Ar ions are usually employed due to their wide availability and low cost. However, other non-reactive ions can be also used in the desorption step. Although, in the adsorption step, HFC precursor radicals are expected to deposit on the surface, too much carbon (C) deposition can result in an etch stop. 22,23) Therefore, O2 plasma irradiation is employed to help minimize C accumulation on the surface. 24 -26)

The goal of this study is to clarify the surface reactions on the atomic scale during SiN PE-ALE processes with ions made of different inert gases, i.e. Ar, krypton (Kr), and xenon (Xe) under the otherwise same conditions, using molecular dynamics (MD) simulations. It is known that while being non-reactive species, these inert-gas species exhibit unique characteristics originating from differences in atomic sizes, mass, and ionization energies. There have been a few attempts to understand their in /uniFB02 uence on etching in general 27 -29) but, to the best of the authors ' knowledge, no study has been published on the effects of Kr + , and Xe + ion irradiation in PE-ALE processes although there have been several studies on Kr and Xe low-temperature plasmas. 30 32) -

## 2. Simulation methods

We performed MD simulations to study the effect of different inert-gas ions in the desorption step on the SiN PE-ALE process. The simulation method is essentially the same as that of Ref. 26. A rectangular SiN model material used in the simulations of this study represents a nearly crystalline Si N 3 4 with a surface area of 4.035 × 2.33 nm 2 and an initial depth of 2.25 nm. Although typical SiN /uniFB01 lms used in semiconductor processes are amorphous and may contain some hydrogen (H) atoms, we use a crystalline SiN as the initial material structure for simplicity, assuming that the

simulations would effectively represent the qualitative nature of PE-ALE processes of SiN with a low H content. This is because, as we shall see in Sect. 3, the surface is amorphized by ion bombardment in any way.

For the model to mimic an in /uniFB01 nitely large surface layer, periodic boundary conditions were applied in the horizontal, i.e. x and y , directions. The depth of the SiN model material in the negative z -direction increases during the simulation as the etching proceeds. More speci /uniFB01 cally additional layers of the same SiN material are added whenever the system temperature exceeds a pre-de /uniFB01 ned threshold value or incident atoms pass through the bottom. During the simulations, the atoms in the bottom two monolayers of the model material were /uniFB01 xed in position to prevent the downward drift of the surface model due to the momentum transfer from the incident ions.

All atomic species involved in the simulations, including incident ions, were treated as charge-neutral atoms in terms of interatomic interactions, as Ref. 26. This is likely to be justi /uniFB01 ed because of a possible neutralization of incident ions by the Auger effect immediately before the impact. 33) Incident species were injected at randomly selected horizontal positions with pre-speci /uniFB01 ed incident energies from suf /uniFB01 ciently above the top material surface. The angle of incidence was set to be normal to the initial top surface. The initial surface temperature was 300 K. The equation of motion for each atom in the system was integrated numerically. For the interactions with inert-gas ions, the two-body interactions were integrated using the Moliére repulsive pair potential function. 34,35) The other force/uniFB01 eld models were, as in Ref. 26, based on the modi /uniFB01 ed Stillinger -Weber-type interatomic potential functions, 35 -37) whose parameters are 26) found in the Supplementary Material. Comprehensive details and technical information on the comparisons between simulations and experimental results can be found in Refs. 18, 25, 26, 38 -43.

The simulation of a SiN PE-ALE process is composed of computational surface-irradiation cycles of radical or ion irradiation. At the start of each computational surfaceirradiation cycle, a single ionic species or multiple radical species are injected into the SiN model material, as described above, and the MD simulation continues under microcanonical ensemble (NVE) conditions for 0.5 ps. Then the system temperature is gradually brought down toward the initial temperature of 300 K by the Langevin thermostat 44,45) for the following 1.4 ps and then, by the Berendsen thermostat 46,47) for the following 0.1 ps. The total time for a computation surface-irradiation cycle is thus 2.0 ps.

In this study, the SiN PE-ALE process consists of three separate steps, i.e. the adsorption step, the desorption step, and the O2 plasma irradiation step. 25,26) Each step is simulated with a series of corresponding computation surface-irradiation cycles. The details of the simulation conditions and parameters are presented in Table I.

In the adsorption step, CH2F radicals, a representative radical species from a plasma formed with HFC molecules, are deposited on the surface. The choice of CH2F radicals was motivated by the experimental study by Hirata et al. of Ref. 23, where a CH F/Ar gas mixture was used. Among ₃

Table I. Simulation conditions for each cycle of the SiN PE-ALE process.

| Parameters      | Values               |
|-----------------|----------------------|
| CH 2 F          |                      |
| Incident energy | 0.5 eV               |
| Radical dose    | 9.56 × 10 15 cm - 2  |
| Ar, Kr, Xe      |                      |
| Incident energy | 300 eV               |
| Ion dose        | 1.06 × 10 16 cm - 2  |
| O               |                      |
| Incident energy | 15 eV                |
| Ion dose        | 1.596 × 10 15 cm - 2 |

possible C-containing species (as C is the primary focus of this work) generated from a CH F gas ₃ in a plasma, we selected CH2F because it is a radical species (having a higher sticking coef /uniFB01 cient), contained both H and /uniFB02 uorine (F) (both of which are known to etch SiN), and contained more H atoms than F atoms (because the etch rate of SiN typically increases with a higher H content in a /uniFB02 uorocarbon plasma). 38,48 -50)

In each computational surface-irradiation cycle, four CH2F radicals are injected into the surface at randomly selected horizontal positions with an incident energy of 0.5 eV each. This energy, higher than typical thermal energies but lower than typical bond energies, enables computationally faster adsorption of those radicals without signi /uniFB01 cantly affecting the surface chemical compositions. The angle of incidence is assumed to be normal to the initial surface for simplicity. For each adsorption step, this computational radical injection cycle was repeated 225 times to simulate a total CH2F radical dose of 9.56 × 10 15 cm -2 . As will be seen later, a 2 nm thick HFC polymer layer is deposited on the SiN model material in a single adsorption step.

In the desorption step, the SiN model material surface with an HFC polymer layer deposited on it is exposed to energetic inert-gas ions (Ar + , Kr + , and Xe + ) with an incident energy of 300 eV and an ion dose of 1.06 × 10 16 cm -2 . In each computational surface-irradiation cycle for this step, a single inert-gas ion is injected into the surface at a randomly selected horizontal position with an incident energy of 300 eV. This computational inert-ion injection cycle was repeated 1000 times.

The O2 plasma irradiation step, in which the surface was exposed to O2 plasmas without a bias voltage, followed the desorption step discussed above. In the actual O2 plasma irradiation step, the surface was irradiated with both ions and radicals (as well as O2 molecules). For example, when the surface is irradiated with O radicals, it takes a long time for the adsorbed O atoms to diffuse into the subsurface region, where they interact with the remaining C atoms. Therefore, in the simulation, we neglected the irradiation of O atoms and injected only low-energy O ions that penetrated the surface more rapidly, to expedite the simulation while maintaining the physical effects of O atoms interacting with remaining subsurface C atoms. To further speed up the simulation, in each computational surface-irradiation cycle for this step, two separate atomic O ions (rather than a single O ion) were injected at random locations, typically away from each other,

with each O ion having an incident energy of 15 eV. The computational O ion injection cycle was repeated 75 times, equivalent to an ion dose of 1.596 × 10 15 cm -2 .

## 3. Results and discussion

## 3.1. Different regimes of surface desorption

Figure 1 shows changes in the height of the SiN material surfaces with and without HFC adsorption as functions of the Ar + ion irradiation dose, obtained from the MD simulations. After the SiN model material with the /uniFB02 at top surface is exposed to CH2F radicals, as described above, an HFC layer is deposited and the position of its top surface is about 2 nm above the position of the initial top surface of the SiN model material (denoted as 0 nm). The top curve of Fig. 1 (labelled as ' with HFC ) represents the position of the top surface of ' the material with an HFC layer. (More precisely, it represents the position of the atom whose z -coordinate value is the largest among all atoms covalently attached to the surface material.) On the other hand, the bottom curve (labelled as ' without HFC ) indicates the position of the top surface of ' the SiN model material without HFC deposition as a function of the Ar + ion dose. In other words, the bottom curve indicates the height of the SiN model material when its surface is physically sputtered by 300 eV Ar + ions. As we discussed in Sect. 2, the atomic interactions of all species, including incident ions, were treated as charge-neutral atoms.

In the case of HFC adsorption, three different regimes of surface desorption were observed as denoted by I, II, and III in Fig. 1. During regime I, adsorbed C, /uniFB02 uorine (F), and hydrogen (H) atoms were mostly removed from the surface while incident ion impact also move such atoms toward the bulk, forming a mixing layer (i.e. layer where the adsorbed atoms and the surface atoms are mixed) around the interface between the HFC layer and the SiN top surface. During

Fig. 1. Changes in the heights of the material surfaces during 300 eV Ar + ion irradiation, obtained from MD simulations. With HFC, an about 2 nm thick HFC layer was deposited on the /uniFB02 at model SiN surface. Without HFC, the /uniFB02 at model SiN surface was etched without HFC deposition. The horizontal axis represents the ion dose. Two vertical broken lines delineate different desorption regimes I, II, and, III, discussed in the main text. For the atomic representations of the surfaces, the reader is referred to section II of the Supplementary Material.

<!-- image -->

regime II, Si and nitrogen (N) atoms were also removed, together with C, F, and H atoms. In regime III, the deposited C, F, and H atoms were mostly exhausted and physical sputtering of SiN took place. Indeed, the etch rate (which is proportional to the rate of change in height per unit ion dose) for the SiN with HFC adsorption is essentially the same as that by SiN physical sputtering. These three regimes of surface etching are similar to those observed in SiN PE-ALE experiments. 22,51) In what follows, we irradiate inert-gas ions only up to an ion dose of 1.06 × 10 16 cm -2 , close to the end of regime II in the case of Ar + ion irradiation, to minimize the physical sputtering of the SiN /uniFB01 lm.

## 3.2. SiN PE-ALE mechanisms

Figure 2 shows changes in the height of the SiN material surfaces in the case of PE-ALE and physical sputtering (i.e. HFC adsorption) as PE-ALE cycles proceed, obtained from the MD simulations. For the curves representing the cases of physical sputtering (labeled as ' physical sputtering ' ), the horizontal axis is proportional to the inert-gas ion dose. The sputtering yield (i.e. the number of Si atoms removed from the SiN surface per ion injection) can be evaluated from the MD simulations.

In the case of PE-ALE cycles, the adsorption step for CH2F deposition, the desorption step by inert-gas ion irradiation, and the oxidation step of the /uniFB01 rst cycle are denoted by ① , ② , and ③ , respectively, with delineation by vertical broken lines. From the second cycle on, the different steps are not explicitly delineated for the sake of simplicity, but every cycle consists of those three steps. For the PE-ALE simulations, the horizontal axis is proportional to the dose of incident species in each step with the total dose in each step being given in Table I. Especially in the desorption step, the horizontal axis is proportional to the inert-gas ion dose, as for the curves of the corresponding physical sputtering.

As seen in Fig. 2, the simulations were performed for /uniFB01 ve SiN PE-ALE cycles. The cases with Ar + , Kr + , and Xe + ions are given in (a), (b), and (c), respectively. Similarly to Fig. 1, the depth of 0 nm corresponds to the location of the initial top surface of the SiN model material. It is seen that, in each adsorption step, the surface increases by about 2 nm. In each desorption step, the surface height gradually decreases, indicating the etching of the surface material takes place with different etching regimes discussed in the preceding subsection. In the oxidation step, there seems no signi /uniFB01 cant increase in the surface height, suggesting that the incident O ions effectively remove the remaining C atoms without much oxidizing the SiN /uniFB01 lm. 23,25)

It is seen in all cases that, toward the end of the desorption step, the etch rate slowed down and sometimes became close to that of the corresponding physical sputtering at least in some cycles. This indicates that self-limiting etching was (nearly) achieved. However, it is also observed the total etched depth is much lower in the cases of Kr + and Xe + ion irradiation.

Figure 3 shows the cycle number dependence of the total etched depth of SiN in the PE-ALE processes with Ar + , Kr + , and Xe + ion irradiations after /uniFB01 ve cycles, obtained from Fig. 2. The total etched depth is de /uniFB01 ned as the position of the surface (measured from the initial SiN top surface) at the end of each cycle. The average etched depth in a single PE-ALE cycle is called an etch-per-cycle (EPC). From Fig. 3, we

Fig. 2. Changes in the heights of the material surface during three-step SiN PE-ALE with (a) Ar + , (b) Kr + , and (c) Xe + ion irradiations over the /uniFB01 rst /uniFB01 ve cycles, obtained from MD simulations. Each PE-ALE cycle consists of the adsorption step (denoted by ① ), desorption step ( ② ), and oxidation step ( ③ ). The lower curves denoted as ' physical sputtering ' indicate the changes in the SiN material surface positions by physical sputtering with the corresponding ions as functions of the ion dose. For the curves representing the PE-ALE processes, the height changes are also represented as functions of the ion dose during the desorption step and a unit length of the horizontal axis represents the same ion dose for both PE-ALE and physical sputtering curves. The PE-ALE simulation conditions are summarized in Table I.

<!-- image -->

<!-- image -->

<!-- image -->

Fig. 3. Total etched depths after each cycle of the SiN PE-ALE processes with Ar + , Kr, + and Xe + ion irradiations, evaluated from the MD simulations of Fig. 2. The EPC averaged over the /uniFB01 ve cycles are 0.41, 0.17, and 0.08 nm for the PE-ALE processes with Ar + , Kr + , and Xe + ion irradiations, respectively.

<!-- image -->

obtained an EPC of 0.41, 0.17, and 0.08 nm/cycle for the PEALE process with Ar + , Kr + , and Xe + ion irradiations, respectively. However, it is also seen that the etching nearly stopped after the third cycle in the case of Xe + ion irradiation.

Figure 4 shows the depth pro /uniFB01 les of the atomic concentrations at the end of the /uniFB01 rst SiN PE-ALE cycle (i.e. at the end of the oxidation step of the /uniFB01 rst cycle) with (a) Ar + , (b) Kr + , and (c) Xe + ion irradiation. The height or depth is measured from the initial SiN top surface. It is seen in Fig. 4 that, some adsorbed C, F, and H atoms penetrated the bulk SiN, due to the knock-on collisions with the incident energetic ions. Some H atoms even reached a depth of about 4 nm. After the oxidation step of the /uniFB01 rst cycle, the amount of Si oxidation is rather limited (in the sense that the Si density is signi /uniFB01 cantly higher than the O density near the top surface region) and the amount of remaining C species is nearly the same among the three cases.

Figure 5 shows the depth pro /uniFB01 les of atomic compositions near the etched SiN surfaces right after the desorption step (and before the oxidation step) of the 5th cycle, obtained from the MD simulations. In (a) -(c), atoms of speci /uniFB01 c

Fig. 4. Depth pro /uniFB01 les of atomic concentrations at the end of the oxidation step of the /uniFB01 rst SiN PE-ALE cycle with (a) Ar + , (b) Kr + , and (c) Xe + ion irradiations, obtained from MD simulations.

<!-- image -->

<!-- image -->

<!-- image -->

species are represented by spheres of the corresponding colors, as indicated in the /uniFB01 gure. In (d) -(f), the depth pro /uniFB01 les of atomic concentrations are presented, as in Fig. 4. The results of the PE-ALE with Ar + , Kr + , and Xe + ion irradiations are given in (a)/(d), (b)/(e), and (c)/(f), respectively. The top black broken line represents the depth of the material surface measured from the original SiN top surface in each case. The bottom black broken line represents the bottom of the mixed layer, above which a large number of incident atomic species such as C and F exist. (More precisely, the top broken black line is placed at the depth where the sum of the Si and N atomic densities is one-half of that in the bulk, and the bottom black broken line is placed at which the sum of the C, F, H, and O densities is 10% of the sum of Si and N densities in the bulk.)

Unlike Fig. 4, here we plotted the depth pro /uniFB01 les after the desorption step and before the oxidation step in the 5th cycle because the oxidation step is needed to remove excess carbon that could enhance the deposition of HFC and hinder the etching in the subsequent step. In addition, in this way, we could see the effects of C accumulation up to the adsorption step of the 5th cycle on the etching of surface atoms in the preceding desorption step.

As we saw in Figs. 2 and 3, the etched depths in the PEALE with Kr + and Xe + ion irradiations are much lower than that with Ar + ion irradiation. This is because there is a signi /uniFB01 cant amount of C accumulation in the cases of Kr + and Xe + ion irradiations compared with the case of Ar + ion irradiation. Such C accumulation hinders the ion impact on the surface and thus the sputtering yield during the desorption step is reduced. Especially in the PE-ALE with Xe + ion irradiation, a relatively thick /uniFB02 uorocarbon (FC) layer is formed, which can cause an etch stop. In the simulations, we used the same desorption time (or ion dose in the desorption step) for each inert-gas ion species to evaluate the damage formation under the same conditions. Of course, a longer desorption time allows better removal of remaining C atoms (especially in the case of Kr + or Xe + ion irradiation), but the thickness of the damaged layer can be also higher under such conditions due to the extended knock-on collision effects. The comparison of the results with Fig. 4 suggests that more C atoms accumulate over the PE-ALE cycles in the cases of Kr + and Xe + ion irradiations than in the case of Ar + ion irradiation. (It should be noted that, in Fig. 4, the C densities are relatively small because the pro /uniFB01 les were taken after the oxidation step, which is designed to remove excess C atoms.)

## 3.3. Surface damage analysis

The surface damage formation during the SiN PE-ALE process was also evaluated using different inert-gas ions in the desorption step. In Fig. 5, it is seen that a mixing layer, i.e. a layer where a large number of the incident species, i.e. C, F, H, and O atoms, form covalent bonds with the bulk atoms, i.e. Si and N, is formed in each case. The thickness of the mixing layer can be de /uniFB01 ned between the two broken lines, as indicated in the /uniFB01 gure. It is seen that the mixing layer thicknesses are nearly the same (about 2 nm) for the three cases with different inert-gas ion irradiations. The results are consistent with experimental observations. 22,51)

On the other hand, it is seen that H atoms more deeply penetrated the bulk SiN in the cases of Kr + and Xe + ion irradiations. The penetration of H atoms was caused by the knock-on collisions with the energetic incident inert-gas ions. It is interesting to note that heavier and thus slower ions, such as Xe + , do not cause less damage than lighter and thus faster ions such as Ar + under the same ion kinetic energy. Because the incident momentum of a heavier ion is higher than that of a lighter ion with the same kinetic energy, the knock-on collision effects by Kr + and Xe + ions can be stronger than Ar + , depending on the way the momentum transfer occurs in the mixing layer.

Fig. 5. Depth pro /uniFB01 les of atomic compositions near the etched SiN surfaces right after the desorption step (and before the oxidation step) of the 5th cycle, obtained from the MD simulations of Fig. 2. In (a) -(c), atoms of speci /uniFB01 c species are represented by spheres of the corresponding colors, as indicated in the /uniFB01 gure. In (d) -(f), the depth pro /uniFB01 les of atomic concentrations are presented, as in Fig. 4. The results of the PE-ALE with Ar + , Kr + , and Xe + ion irradiations are given in (a)/(d), (b)/(e), and (c)/(f), respectively. The region between the two horizontal broken lines represents the mixing layer, which is also considered to be a damaged region of the etched surface.

<!-- image -->

## 4. Conclusions

MD simulations of 5 cycles of SiN PE-ALE processes were performed with different inert-gas ions, i.e. Ar + , Kr + , and Xe + , in their desorption steps. The study was motivated by the expectation that heavier ions typically have a shorter penetration depth and therefore cause less damage to the etched surface.

desorption or etching in the desorption step, denoted by I, II, and III in Fig. 1. In the /uniFB01 rst regime, the removal of the HFC /uniFB01 lm dominates; in the second regime, the chemical etching of SiN takes place until reactive F and H species are nearly exhausted; and in the third regime, physical sputtering of SiN dominates. This observation is consistent with the experimental observation reported in Refs. 22, 51.

First, we examined the /uniFB01 rst cycle of SiN PE-ALE with an extended period of Ar + ion irradiation for the desorption step. It is found that there are three different regimes of surface

Second, the MD simulations have revealed that the etched depth by PE-ALE with Ar + ion irradiation is much larger than those with Kr + , and Xe + ion irradiations. In other words, under the same PE-ALE conditions with HFC

adsorption, Ar + ion irradiation removes the surface material much more ef /uniFB01 ciently than Kr + or Xe + ion irradiation. Less ef /uniFB01 cient etching by Kr + or Xe + ion irradiation allows the accumulation of a C layer on the surface over the PE-ALE cycles and the oxidation step used in our study was not ef /uniFB01 cient enough to remove the excess C. The gradual formation of a C layer, in turn, hinders the effectiveness of ion impact and thus reduces the etch rate. Especially in the case of Xe + ion irradiation, we observed that a relatively thick FC layer was formed and the PE-ALE essentially stopped after the third cycle. Over the 5 cycles of SiN PEALE processes simulated in this study, the observed depths of EPC were 0.41, 0.17, and 0.08 nm for Ar + , Kr + , and Xe + ion irradiations, respectively.

Third, we evaluated the damage formation on the etched surfaces. The mixed layer that remains at the end of the desorption step process is considered to be a damaged layer caused by the PE-ALE process. The depths of the mixed layers after the 5th cycle are almost the same (about 2 nm) in all three cases, indicating that ion irradiation by heavier ions such as Kr + or Xe + ions does not necessarily cause less damage to the surface during the PE-ALE process.

Furthermore, H atoms were found to penetrate the SiN bulk deeply by knock-on collisions with heavier and thus slower incident ions injected into the surface under the same kinetic energy. The overall conclusion is that, for the PEALE of SiN, the etching proceeds most ef /uniFB01 ciently with Ar + ions irradiation among all three inert-gas ions examined in this study.

## Acknowledgments

We would like to thank Dr. Akiko Hirata of Sony Semiconductor Solutions Corporation and Dr. Masanaga Fukasawa of the National Institute of Advanced Industrial Science and Technology for their valuable insights into this research. The work was partially supported by the Japan Society of the Promotion of Science (JSPS) Grants-in-Aid for Scienti /uniFB01 c Research(S) 15H05736 and (A) 21H04453, the JSPS Core-to-Core Program JPJSCCA2019002, and the Japan Science and Technology Agency (JST) s ' ' Adopting Sustainable Partnerships for Innovative Research Ecosystem (ASPIRE) ' Grant No. PMJAP2321.

## ORCID iDs

Jomar U. Tercero https://orcid.org/0009-0002-8263-3954 Satoshi Hamaguchi https://orcid.org/0000-0001-6580-8797

1) G. S. Oehrlein, D. Metzler, and C. Li, ' Atomic layer etching at the tipping point: an overview, ' ECS J. Solid State Sci. Technol. 4 , N5041 (2015).

- 2) T. Faraz, F. Roozeboom, H. C.-M. Knoops, and W. M.-M. Kessels, ' Atomic layer etching: what can we learn from atomic layer deposition?, ' ECS J. Solid State Sci. Technol. 4 , N5023 (2015).
- 3) S. U. Engelmann, R. L. Bruce, M. Nakamura, D. Metzler, S. G. Walton, and E. A. Joseph, ' Challenges of tailoring surface chemistry and plasma/surface interactions to advance atomic layer etching, ' ECS J. Solid State Sci. Technol. 4 , N5054 (2015).
- 4) M. Honda, T. Katsunuma, M. Tabata, A. Tsuji, T. Oishi, T. Hisamatsu, S. Ogawa, and Y. Kihara, ' Bene /uniFB01 ts of atomic-level processing by quasiALE and ALD technique, ' J. Phys. D: Appl. Phys. 50 , 234002 (2017).
- 5) G. S. Oehrlein and S. Hamaguchi, ' Foundations of low-temperature plasma enhanced materials synthesis and etching, ' Plasma Sources Sci. Technol. 27 , 023001 (2018).
- 6) K. J. Kanarik, T. Lill, E. A. Hudson, S. Sriraman, S. Tan, J. Marks, V. Vahedi, and R. A. Gottscho, ' Overview of atomic layer etching in the semiconductor industry, ' J. Vac. Sci. Technol. A 33 , 020802 (2015).
- 7) I. Adamovich et al., ' The 2022 plasma roadmap: low temperature plasma science and technology, ' J. Phys. D: Appl. Phys. 55 , 373001 (2022).
- 8) R. Blanc, F. Leverd, T. David, and O. Joubert, ' Patterning of silicon nitride for CMOS gate spacer technology: I. Mechanisms involved in the silicon consumption in CH3F/O2/He high density plasmas, ' J. Vac. Sci. Technol. B 31 , 051801 (2013).
- 9) C. G.-N. Lee, K. J. Kanarik, and R. A. Gottscho, ' The grand challenges of plasma etching: a manufacturing perspective, ' J. Phys. D: Appl. Phys. 47 , 273001 (2014).
- 10) C. T. Carver, J. J. Plombon, P. E. Romero, S. Suri, T. A. Tronic, and R. B. Turkot, ' Atomic layer etching: an industry perspective, ' ECS J. Solid State Sci. Technol. 4 , N5005 (2015).
- 11) K. Arts, S. Hamaguchi, T. Ito, K. Karahashi, H. C.-M. Knoops, A. J.M. Mackus, and W. M.-M. (Erwin) Kessels, ' Foundations of atomic-level plasma processing in nanoelectronics, ' Plasma Sources Sci. Technol. 31 , 103002 (2022).
- 12) Y. Horiike, T. Tanaka, M. Nakano, S. Iseda, H. Sakaue, A. Nagata, H. Shindo, S. Miyazaki, and M. Hirose, ' Digital chemical vapor deposition and etching technologies for semiconductor processing, ' J. Vac. Sci. Technol. A 8 , 1844 (1990).
- 13) H. Sakaue, S. Iseda, K. Asami, J. Yamamoto, M. Hirose, and Y. Horiike, ' Atomic layer controlled digital etching of silicon, ' Jpn. J. Appl. Phys. 29 , 2648 (1990).
- 14) T. Matsuura, J. Murota, Y. Sawada, and T. Ohmi, ' Self-limited layer-bylayer etching of Si by alternated chlorine adsorption and Ar + ion irradiation, ' Appl. Phys. Lett. 63 , 2803 (1993).
- 15) S. D. Athavale, ' Realization of atomic layer etching of silicon, ' J. Vac. Sci. Technol. B 14 , 3702 (1996).
- 16) B.-J. Kim, S. Chung, and S. M. Cho, ' Layer-by-layer etching of Cladsorbed silicon surfaces by low energy Ar + ion irradiation, ' Appl. Surf. Sci. 187 , 124 (2002).
- 17) I. L. Berry, K. J. Kanarik, T. Lill, S. Tan, V. Vahedi, and R. A. Gottscho, ' Applying sputtering theory to directional atomic layer etching, ' J. Vac. Sci. Technol. A 36 , 01B105 (2018).
- 18) E. J.-C. Tinacba, M. Isobe, and S. Hamaguchi, ' Surface damage formation during atomic layer etching of silicon with chlorine adsorption, ' J. Vac. Sci. Technol. A 39 , 042603 (2021).
- 19) B. Chapman and J. L. Vossen, ' Glow discharge processes: sputtering and plasma etching, ' Phys. Today 34 , 62 (1981).
- 20) M. A. Lieberman and A. J. Lichtenberg, Principles of Plasma Discharges and Materials Processing (Wiley, Hoboken, NJ, 2005).
- 21) K. Nojiri, Dry Etching Technology for Semiconductors (Springer International Publishing, Cham, 2015).
- 22) Y. Ishii, K. Okuma, T. Saldana, K. Maeda, N. Negishi, and J. Manos, ' Atomic layer etching of silicon nitride using cyclic process with hydro/uniFB02 uorocarbon chemistry, ' Jpn. J. Appl. Phys. 56 , 06HB07 (2017).
- 23) A. Hirata, M. Fukasawa, K. Kugimiya, K. Nagaoka, K. Karahashi, S. Hamaguchi, and H. Iwamoto, ' Mechanism of SiN etching rate /uniFB02 uctuation in atomic layer etching, ' J. Vac. Sci. Technol. A 38 , 062601 (2020).
- 24) T. Tsutsumi, H. Kondo, M. Hori, M. Zaitsu, A. Kobayashi, T. Nozawa, and N. Kobayashi, ' Atomic layer etching of SiO2 by alternating an O2 plasma with /uniFB02 uorocarbon /uniFB01 lm deposition, ' J. Vac. Sci. Technol. A 35 , 01A103 (2017).
- 25) A. Hirata, M. Fukasawa, J. U. Tercero, K. Kugimiya, Y. Hagimoto, K. Karahashi, S. Hamaguchi, and H. Iwamoto, ' Five-step plasma-enhanced atomic layer etching of silicon nitride with a stable etched amount per cycle, ' Jpn. J. Appl. Phys. 61 , 066002 (2022).
- 26) J. U. Tercero, A. Hirata, M. Isobe, K. Karahashi, M. Fukasawa, and S. Hamaguchi, ' Surface chemical reactions of etch stop prevention in plasma-enhanced atomic layer etching of silicon nitride, ' Surf. Coat. Technol. 477 , 130365 (2024).
- 27) D. H. Kim, G. H. Lee, S. Y. Lee, and D. H. Kim, ' Atomic scale simulation of physical sputtering of silicon oxide and silicon nitride thin /uniFB01 lms, ' J. Cryst. Growth 286 , 71 (2006).
- 28) Y. Kondo, K. Ishikawa, T. Hayashi, Y. Miyawaki, K. Takeda, H. Kondo, M. Sekine, and M. Hori, ' Silicon nitride etching performance of CH2F2 plasma diluted with argon or krypton, ' Jpn. J. Appl. Phys. 54 , 040303 (2015).
- 29) Y. Lee, H. Yeom, D. Choi, S. Kim, J. Lee, J. Kim, H. Lee, and S. J. You, ' Database development of SiO2 etching with /uniFB02 uorocarbon plasmas diluted with various noble gases of Ar, Kr, and Xe, ' Nanomaterials 12 , 3828 (2022).

- 30) K. H. Bai, S. J. You, H. Y. Chang, and H. S. Uhm, ' Plasma parameters analysis of various mixed gas inductively coupled plasmas, ' Phys. Plasmas 9 , 2831 (2002).
- 31) H. Shin, W. Zhu, D. J. Economou, and V. M. Donnelly, ' Ion energy distributions, electron temperatures, and electron densities in Ar, Kr, and Xe pulsed discharges, ' J. Vac. Sci. Technol. A 30 , 031304 (2012).
- 32) Y. Kondo, Y. Miyawaki, K. Ishikawa, T. Hayashi, K. Takeda, H. Kondo, M. Sekine, and M. Hori, ' Hydro /uniFB02 uorocarbon ion density of argon- or krypton-diluted CH2F2 plasmas: generation of CH2F + and CHF2 + by dissociative-ionization in charge exchange collisions, ' J. Phys. D: Appl. Phys. 48 , 045202 (2015).
- 33) M. Toth, B. L. Thiel, and A. M. Donald, ' On the role of electron -ion recombination in low vacuum scanning electron microscopy, ' J. Microscopy 205 , 86 (2002).
- 34) I. Torrens, Interatomic Potentials (Academic, New York, 1972) 1st ed.
- 35) H. Ohta and S. Hamaguchi, ' Classical interatomic potentials for Si -O F -and Si -O Cl systems, -' J. Chem. Phys. 115 , 6679 (2001).
- 36) F. H. Stillinger and T. A. Weber, Phys. Rev. B: Condens Matter 31 , 5262 (1985).
- 37) P. C.-L. Stephenson, M. W. Radny, and P. V. Smith, ' A modi /uniFB01 ed Stillinger -Weber potential for modelling silicon surfaces, ' Surface Science 366 , 177 (1996).
- 38) K. Miyake, T. Ito, M. Isobe, K. Karahashi, M. Fukasawa, K. Nagahata, T. Tatsumi, and S. Hamaguchi, ' Characterization of polymer layer formation during SiO2/SiN etching by /uniFB02 uoro/hydro /uniFB02 uorocarbon plasmas, ' Jpn. J. Appl. Phys. 53 , 03DD02 (2014).
- 39) E. J. Capdos Tinacba, M. Isobe, K. Karahashi, and S. Hamaguchi, ' Molecular dynamics simulation of Si and SiO2 reactive ion etching by /uniFB02 uorine-rich ion species, ' Surf. Coat. Technol. 380 , 125032 (2019).
- 40) N. A. Mauchamp and S. Hamaguchi, ' Molecular dynamics simulation of Si trench etching with SiO2 hard masks, ' J. Vac. Sci. Technol. A 40 , 053004 (2022).
- 41) C. M.-D. Cagomoc, M. Isobe, E. A. Hudson, and S. Hamaguchi, ' Molecular dynamics simulation of oxide-nitride bilayer etching with energetic /uniFB02 uorocarbon ions, ' J. Vac. Sci. Technol. A 40 , 063006 (2022).
- 42) C. M.-D. Cagomoc, M. Isobe, and S. Hamaguchi, ' Molecular dynamics study of SiO2 nanohole etching by /uniFB02 uorocarbon ions, ' J. Vac. Sci. Technol. A 41 , 023001 (2023).
- 43) C. M.-D. Cagomoc, M. Isobe, E. A. Hudson, and S. Hamaguchi, ' Inert-gas ion scattering at grazing incidence on smooth and rough Si and SiO2 surfaces, ' J. Vac. Sci. Technol. A 41 , 023003 (2023).
- 44) T. Schneider and E. Stoll, ' Molecular-dynamics study of a three-dimensional one-component model for distortive phase transitions, ' Phys. Rev. B 17 , 1302 (1978).
- 45) D. Frenkel, B. Smit, and M. A. Ratner, ' Understanding molecular simulation: from algorithms to applications, ' Phys. Today 50 , 66 (1997).
- 46) H. J.-C. Berendsen, J. P.-M. Postma, W. F. van Gunsteren, A. DiNola, and J. R. Haak, ' Molecular dynamics with coupling to an external bath J. Chem. Phys. 81 , 3684 (1984).
- 47) S. C. Harvey, R. K.-Z. Tan, and T. E. Cheatham, ' The /uniFB02 ying ice cube: velocity rescaling in molecular dynamics leads to violation of energy equipartition, ' J. Comput. Chem. 19 , 726 (1998).
- 48) K. Karahashi, K. Yanai, K. Ishikawa, H. Tsuboi, K. Kurihara, and M. Nakamura, ' Etching yield of SiO2 irradiated by F + , CF x + ( x = 1, 2, 3) ion with energies from 250 to 2000 eV, ' J. Vac. Sci. Technol. A 22 , 1166 (2004).
- 49) K. Yanai, K. Karahashi, K. Ishikawa, and M. Nakamura, ' Mass-analyzed CF x + ( x = 1, 2, 3) ion beam study on selectivity of SiO2-to-SiN etching and a-C: F /uniFB01 lm deposition, ' J. Appl. Phys. 97 , 053302 (2005).
- 50) T. Ito, K. Karahashi, M. Fukasawa, T. Tatsumi, and S. Hamaguchi, ' Hydrogen effects in hydro /uniFB02 uorocarbon plasma etching of silicon nitride: Beam study with CF + , CF2 + , CHF2 + , and CH2F + ions, ' J. Vac. Sci. Technol. A 29 , 050601 (2011).
- 51) A. Hirata, M. Fukasawa, K. Kugimiya, K. Nagaoka, K. Karahashi, S. Hamaguchi, and H. Iwamoto, ' On-wafer monitoring and control of ion energy distribution for damage minimization in atomic layer etching processes, ' Jpn. J. Appl. Phys. 59 , SJJC01 (2020).