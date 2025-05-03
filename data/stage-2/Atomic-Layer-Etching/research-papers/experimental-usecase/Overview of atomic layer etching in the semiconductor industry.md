<!-- image -->

REVIEW ARTICLE |  MARCH 05 2015

## Overview of atomic layer etching in the semiconductor industry

Keren J. Kanarik; Thorsten Lill; Eric A. Hudson; Saravanapriyan Sriraman; Samantha Tan; Jeffrey Marks; Vahid Vahedi; Richard A. Gottscho

<!-- image -->

Check for updates

J. Vac. Sci. Technol. A 33, 020802 (2015) https://doi.org/10.1116/1.4913379

## Articles You May Be Interested In

AC thin-film electroluminescence: A historical overview with a look ahead

J. Vac. Sci. Technol. B (October 2024)

Atomic-scale imaging and spectroscopy via scanning probe microscopy: An overview

J. Vac. Sci. Technol. B (October 2023)

Self-healing ceramic coatings that operate in extreme environments: A review

J. Vac. Sci. Technol. A (August 2020)

<!-- image -->

 

<!-- image -->

<!-- image -->

## REVIEWARTICLE

## Overview of atomic layer etching in the semiconductor industry

a) Thorsten Lill, Eric A. Hudson, Saravanapriyan Sriraman, Samantha Tan,

Keren J. Kanarik, Jeffrey Marks, Vahid Vahedi, and Richard A. Gottscho

Lam Research Corporation, 4400 Cushing Parkway, Fremont, California 94538

(Received 17 December 2014; accepted 9 February 2015; published 5 March 2015)

Atomic layer etching (ALE) is a technique for removing thin layers of material using sequential reaction steps that are self-limiting. ALE has been studied in the laboratory for more than 25 years. Today, it is being driven by the semiconductor industry as an alternative to continuous etching and is viewed as an essential counterpart to atomic layer deposition. As we enter the era of atomic-scale dimensions, there is need to unify the ALE field through increased effectiveness of collaboration between academia and industry, and to help enable the transition from lab to fab. With this in mind, this article provides defining criteria for ALE, along with clarification of some of the terminology and assumptions of this field. To increase understanding of the process, the mechanistic understanding is described for the silicon ALE case study, including the advantages of plasmaassisted processing. A historical overview spanning more than 25 years is provided for silicon, as well as ALE studies on oxides, III-V compounds, and other materials. Together, these processes encompass a variety of implementations, all following the same ALE principles. While the focus is on directional etching, isotropic ALE is also included. As part of this review, the authors also address the role of power pulsing as a predecessor to ALE and examine the outlook of ALE in the manufacturing of advanced semiconductor devices. V C 2015 Author(s). All article content, except where otherwise noted, is licensed under a Creative Commons Attribution 3.0 Unported License .

[http://dx.doi.org/10.1116/1.4913379]

## I. INTRODUCTION

Following the trajectory of Moore's law, the semiconductor industry has transitioned from microelectronics in the 1980s and nanoelectronics in the early 2000s, to today, when we are entering the atomic-scale era. Developing advanced technology for the sub-10 nm technology node presents an unprecedented challenge for chipmakers. These devices will require atomic-scale fidelity, where fidelity refers to the degree of matching to the intent of design engineers in shape and composition. Fidelity is dependent on the process variability brought about by manufacturing trillions of transistors per day. Although process variability has always been a constraint to semiconductor manufacturing, margins shrink with each technology generation, and today variability is one of the biggest barriers to future scaling. 1,2 Within the next 10 years, acceptable feature size variability is expected to be on the order of 3-4 atoms of silicon, including contributions from surface imperfections. Surfaces have become a significant fraction of the device size and can appreciably affect device electronic properties. 3,4 There is significant impact to device performance from variability (including surface contributions), which increases current leakage and battery power loss and ultimately reduces yield due to failed devices. 2 With etching processes increasingly critical to state-of-the-art semiconductor devices, the tight control of etch variability offered by atomic layer etching (ALE) is necessary.

a) Electronic mail: keren.kanarik@lamresearch.com

ALE is a technique that removes thin layers of material using sequential self-limiting reactions and is considered one of the most promising techniques for achieving the low process variability necessary in the atomic-scale era. The basic ALE concept, shown in Fig. 1(a), starts with a modification step to form a reactive layer, followed by a removal step to take off only this modified layer. Using ions allows for the directional etching required to form deep, narrow structures. Although ALE has been reported in literature for over 25 years, one of the main challenges in applying the technique in the semiconductor industry has been providing sufficient productivity to make it suitable for cost-sensitive manufacturing environments. 5,6 As ALE overcomes these hurdles and moves toward widespread adoption, 7 it builds upon established technology and capability of its counterpart of atomic layer deposition (ALD), widely used in the semiconductor industry for depositing thin, conformal films. 8-11

To help unify this developing field, this review article examines the fundamental criteria, mechanistic understanding, and future potential of ALE in the semiconductor industry. We explain limitations of traditional etching that motivate the development of ALE solutions. Although this article focuses on plasma etching, the conclusions are largely applicable to other processes, including wet etching. The current understanding of ALE mechanisms will be discussed using the silicon system as the prototypical example, followed by history of ALE on silicon and other materials. Our literature survey focused on /C24 100 ALE reports explored since 1988 under a wide variety of terms. As part of this

<!-- image -->

<!-- image -->

FIG. 1. (Color) Schematic of ALE (a) generic concept, (b) for the silicon case study, and (c) in comparison to ALD. ALE is similar to ALD except that removal takes place instead of adsorption in reaction B.

<!-- image -->

review, we aim to clarify some of the terminology and assumptions and thereby enable more effective collaboration between academia and industry.

## II. LIMITATIONS OF CONTINUOUS ETCHING

The majority of etch processes in the semiconductor industry today require directional removal, as shown in Fig. 2(a), to maintain critical dimension of the mask. 12,13 The most extensively used process is reactive ion etching (RIE), which is a type of (dry) plasma etching involving a partially ionized plasma glow discharge that provides a mixture of reactive and nonreactive ions, electrons, reactive neutrals, passivating species, and photons. Directionality for positively charged ions is provided by accelerating them normal to the wafer surface through a negative voltage bias on the wafer substrate. In this way, energetic ions work in synergy with neutral chemical species from the plasma to remove film from the wafer surface. 14,15 For decades, plasma etching such as RIE has been operated with all reactions occurring continuously and simultaneously for the duration of the process (referred to as 'continuous' etching). This can be represented by A þ B, where, in RIE, reaction A represents neutral reactions and reaction B represents energetic ions above an etching threshold. Continuous processing is beneficial for fast etch rates, but also presents limitations for onwafer performance due to process variability coming from chamber mismatch, nonuniformity across the wafer and within die, and surface composition/roughness.

<!-- image -->

a)  Directional Etching

<!-- image -->

b)  Isotropic Etching

FIG. 2. Schematic of (a) directional etching, showing a greater rate of material removal in the vertical direction than lateral, and (b) isotropic etching, showing material removed at the same rate in all directions.

The limitations of continuous and simultaneous processes originate from transport-limited phenomena, highly coupled parameters, and propagation of the damaged etch front. Continuous etching tends to depend strongly on delivery of one or more species (e.g., neutrals or ions) that drives reaction at the etch front, making them transport-limited. Consequently, process variability may be compromised at all length scales as species fluxes inevitably vary due to depletion and gradients in the reaction chamber, along the wafer, within the die, and in the feature. 16 While neutral- or ionlimited regimes can help, they are not always practical and can be a challenge to tune to the appropriate conditions. This difficulty in tuning to optimum process conditions is due to another limitation with continuous processes: the coupling of the transport (or flux) of each species. Generation of ions and neutrals are coupled to the same electron energy distribution. 17 Meanwhile, incoming ions and reactant species

progressively 'blur' the surface, forming a thick mixed layer characterized by increased roughness, mixed composition of reactant and substrate atoms, dangling bonds, and voids. 18,19 Uninhibited reactivity with continuous bombardment degrades postetch surface quality and can impact device performance. 3 While the mixed layer could be reduced with lower ion energy, 18,20 the paradox is that the layer is produced by the same high ion energies needed to perform etching in the first place. Thus, damage and etching remain convoluted when processing is continuous. These issues limit the pattern transfer fidelity that can be achieved.

Over the past 40 years, intense efforts have been focused on improving process variability within these limitations. 12,21 In the 1980s, batch reactors that processed dozens of wafers at the same time switched to single-wafer reactors, which provided consistent reactant delivery to each wafer. In the 1990s, control was enhanced by adding multiple driving frequencies to decouple, at least partially, plasma density from ion bombardment energy. 22 An ongoing effort to reduce variability of process parameters such as pressure, temperature, power, and gas flow has facilitated tool matching. 23 In the early 2000s, conditioning chamber walls with in situ wall deposition significantly improved wafer-to-wafer repeatability. 24 However, a significant portion of process control still relies on compensation to correct for systematic nonuniformities that are amplified by the coupled transport of ions and neutrals to the wafer surface during continuous processing. Despite widespread usage of balancing competing behaviors, compensation adds cost and complexity to the system, thereby providing a smaller process window. Overall, while process variability in continuous etching has been reduced dramatically over the years, 25 it is becoming increasingly difficult and expensive to manage around the fundamental limitations especially as we progress to smaller technology nodes.

While some sources of process variability are controllable, current capability does not achieve all of the necessary requirements for the most advanced structures. With systematic methodology for chamber matching, chamber-to-chamber repeatability of dimensions is achievable to within &lt; 0.5 nm. 25 Current capability can also achieve critical dimensional uniformity to within &lt; 0.5 nm across the wafer 16 although some problems still remain at the outermost 2 mm of the wafer edge. However, within die variability remains an ongoing challenge, as it is not always possible to compensate for different layout pattern densities and aspect ratios. 26,27 Compounding this challenge are complicated topographies, multiple patterning schemes, and aspect ratios larger than 60:1. Surface quality is also an unsolved challenge today in continuous etching due to the thick mixed layer. For example, etch-induced damage from plasma during gate etching has been shown to penetrate &gt; 20 nm into the surface and degrade device performance by increasing sheet resistance due to altered doping levels. 28-30 Damage is often estimated by material loss after subsequent wet etching. All of the factor discussed above drives the need for revolutionary etching methods beyond the continuous and simultaneous-such as atomic layer etching.

## III. ALE FUNDAMENTALS

## A. Historical background and terminology

ALE has been studied for over 25 years, with the semiconductor industry being the main driver of this research. The earliest report traces back to Yoder in 1988 on ALE of diamond for synthetic diamond films. 31 Yoder also studied ALD and cited reciprocity of the processes as his motivation. Another early contribution in 1989 from Maki and Ehrlich reported 'bilayer etching' of GaAs using chlorine chemisorption. 32 Figure 3 shows the number of reports published over the past three decades. A first wave of ALE reports started in the 1990s, with focus on directional ALE as an alternative to RIE. 33 Isotropic ALE has also been studied since the early years, 34 and compromises about one third of ALE reports. Overall, silicon and GaAs have been the most studied ALE materials, with GaAs predominately in the 1990s when it was the III-V material of focus for replacing silicon. Altogether, ALE has been demonstrated on well over 20 materials including elemental semiconductors, compound semiconductors, insulators, and metals, which are described in Sec. V. Nearly all early references on ALE cite direct connection to ALD, suggesting that the onset of atomic layer etching in the late 1980s originated as a concurrent expansion of work on atomic layer deposition. After a slower pace of publications in the 2000s, there has recently been a resurgence of ALE activity (Fig. 3). Consequently, there is more focused effort to unite the field, as done for ALD over 14 years ago. 11 In April 2014, Sematech hosted an inaugural ALE workshop, and the second annual ALE workshop is planned for 2015 in conjunction with the ALD conference in Portland. In addition, ALE has recently become a special topic in conferences and journals, including focus sessions at the 2014 International Symposium on Dry Processing in Japan and at the American Vacuum Society 2014 conference in Baltimore.

FIG. 3. Number of ALE publications per year from 1988 to 2014. The first wave of publications occurred in the 1990s. A resurgence of ALE activity is now occuring.

<!-- image -->

TABLE I. Variety of names and acronyms have been used for atomic layer etch processes.

| Name                            | Acronym   |   Early Reference |
|---------------------------------|-----------|-------------------|
| Atomic layer etching            |           |                31 |
| Atomic layer etching            | ALE       |                35 |
| Atomic layer etching            | ALET      |                36 |
| Atomic layer etching            | ALET      |                37 |
| Plasma atomic layer etching     | PALE      |                 5 |
| Digital etching                 |           |                38 |
| Layer by layer etch             |           |                39 |
| Molecular layer etching         |           |                40 |
| Molecular bilayer etching       |           |                32 |
| Single layer etching            |           |                41 |
| Thin layer etching              |           |                42 |
| Monolayer chemical beam etching | ML-CBET   |                43 |
| Atomic layer removal            |           |                44 |

Table I shows the variety of names and acronyms found in literature for processes that all meet the ALE criteria as described in this article. We want to clarify some of the terminology and assumptions, since inconsistent naming can be confusing and make literature searches difficult as multiple groups work in different areas of the world unaware of one another. A probable reason for this confusion was that the deposition community was using the acronym ALE for atomic layer epitaxy in the 1990s, when atomic layer etching was first introduced. However, in 2001, the deposition community instead adopted 'ALD.' 11 For consistency and clarity, we follow the lead from deposition and use the simplest analogous term: 'ALE.' This acronym is intended to encompass a majority of work in our field. Another point of confusion has been the meaning of 'atomic layer' in ALE. As Puurunen points out for ALD, the term gives the impression that these processes are defined by the amount of material involved in each cycle-an exact monolayer. 9 However, this assumption does not generally hold true even for ALD. Instead, the benefits come from separated self-limiting reactions rather than the exact amount of material removed, as discussed in Sec. III B. The atomic layer name sticks because it resonates with the intention of controlling dimensions with atomic-scale fidelity. We hope the clarifications here will encourage researchers in related areas to join and contribute to the ALE field.

## B. ALE criteria

Atomic layer etching is defined as a film etching technique that uses sequential self-limiting reactions [Figs. 1(a) and 1(b)]. The concept is analogous to ALD [Fig. 1(c)], except that removal occurs in place of a second adsorption step, resulting in layer-by-layer material subtraction instead of addition. The simplest ALE implementation consists of two sequential steps: surface modification (reaction A) and removal (reaction B). Modification forms a thin reactive surface layer with a well-defined thickness that is subsequently more easily removed than the unmodified material. The layer is characterized by a sharp gradient in chemical composition and/or physical structure of the outermost layer of a material. The removal step takes away the modified layer while keeping the underlying substrate intact, thus 'resetting' the surface to a pristine or near-pristine state for the next etching cycle. The total amount of material removed is determined by the repeated cycles, for example, three cycles: A ! B ! A ! B ! A ! B, as shown in Fig. 4. The general ALE concept applies to a wide variety of etching schemes including directional or isotropic, selective or nonselective, and reactants delivered by gases, plasma, wet (liquid) chemistry, or other sources. All schemes share the same defining ALE criteria: (1) separation into a sequence (cycling) of independent unit process reactions, and (2) at least one step is as selflimiting as possible.

Separation of reactions means the composite process runs as a repeated series of two or more independent unit steps, with each step designed to be as simple as possible. In plasma etching, this typically involves each step with distinct chemistry, speciation, and plasma energy composition. The separation is either temporal or spatial, although the time domain is most common using a single chamber with sophisticated process control technology to modulate process parameters such as gas composition, gas flow, pressure, and plasma power. The advantage of separation is that it decouples the generation and transport of ions, electrons, and neutrals, thereby increasing access to desirable species fluxes and their relative ratios, i.e., opens the process window. It has also been suggested that discontinuity avoids the unlimited reactivity that forms the thick mixed layer in continuous plasma etching. 22,45 One of the primary advantages of separation is that it facilitates self-limiting reactions.

Self-limiting reactions refer to those reactions that slow down or stop as a function of time or, equivalently, as a function of species dosage. Figure 5 shows examples of selflimiting behavior, where etching takes place in an initial 'burst' followed by a removal rate that approaches zero. The etched amount per cycle is referred to as EPC, analogous to growth per cycle in ALD. 9 (This term substitutes for etch

Process Time

<!-- image -->

FIG. 4. Total amount of material removed in three sequential ALE cycles: A ! B ! A ! B ! A ! B. The amount of material etched per cycle is EPC. Ideally, removal only occurs during reaction B and is selflimiting. The time needed to switch between reactions is indicated by gray zones.

## Saturation Curve

Removal Time or Dosage

<!-- image -->

FIG. 5. 'Saturation curves' showing self-limiting removal in (a) ALE for small EPC, (b) ALE for larger EPC, and (c) ALE quasi-self-limiting. In curve (d), continuous etching is shown for comparable etch time to illustrate lack of self-limiting behavior.

rate since the amount removed in ALE is not linear in time.) Self-limiting reactions replace transport-limited reactions of continuous processing, and in this way avoids the associated limitations of continuous etching. The importance of selflimiting behavior is explained in Fig. 5. The near-zero slopes in Figs. 5(a)-5(c) show that etching for that cycle is effectively complete. As a result, any geometric loading effectsmicroscopic or macroscopic-that are prevalent in continuous processing are mitigated because the reactions essentially stop. One way to imagine this is as slow reactions catching up to fast reactions once the etching is complete. In contrast, Fig. 5(d) illustrates continuous etching that lacks any self-limitation, which leads to etching strongly dependent on local species fluxes. Even if the continuous process is slowed, by dilution, for example, it is not equivalent to the self-limiting nature of an ALE cycle. Considering Figs. 5(a) and 5(b), we can also conclude that EPC does not factor as an ALE criteria as long as it is finite. It is important to note that even if the reaction has not stopped, i.e., it is not truly self-limiting [Fig. 5(c)], many benefits of self-limiting behavior can be realized with only minor trade-offs compared to continuous processing. This is why we refer to reactions that are as self-limiting as possible , and operating in this quasi-self-limiting regime can be attractive for economic reasons. For instance, ALE can be made faster and thus more cost-efficient by operating in subsaturation mode, in which reactions have slowed down but not completely stopped, an advantage that has been recognized in ALD as well. 46 In summary, ALE is fundamentally less subject to process variability induced by transport limitations when compared to continuous etching, a direct consequence of the extent to which the ALE process is self-limiting.

## C. Characterization tests

In the design of ALE processes, we have identified three complementary tests to characterize ALE for a particular reactant and substrate combination: synergy test, saturation curve (etched amount versus time for a fixed removal energy), and an energy scan (etched amount as a function of energy for a fixed removal time). Versions of these tests have appeared in ALE studies, 39,47,48 although not necessarily called out or in context to one another. These tests can help indicate to what degree the ALE process approaches ideal behavior, albeit nonideal conditions may still yield significant benefit. In addition to these tests, ultimately, ALE will be characterized by the benefits on the wafer: features with atomically smooth and flat surfaces, 6,49,50 reproducibility of stoichiometry, 50-54 uniformity across the wafer, 6 etching without loading (pattern-density independence), 55 low-damage to remaining material, 28,50,56-58 and etch selectivity to other materials. 44,57,59-61

The first test is the synergy test, which measures the amount of material etched per cycle (typically averaged over many cycles) compared to the amount from each individual step. Ideally, there is no etching during the modification step (i.e., reaction A). Similarly, there should be no etching beyond the surface modified layer in reaction B. In practice, each step may result in removal of some material but the conditions should be chosen such that this etching is small compared to that achieved by combining the steps into an ALE cycle. We will discuss how to minimize nonideal behavior further when we consider the case example of silicon ALE in Sec. IV. The second test is the saturation curve, and its importance was discussed in Sec. III B and shown in Fig. 5. They are used to determine the degree of self-limiting behavior for the chosen conditions.

The third test is less frequently used and so is discussed here in more detail. The energy scan is illustrated in Fig. 6 for the removal step, plotting EPC as a function of energy. The energy can generally be from thermal, ion, or other

## Energy Scan

Etch Per Cycle (EPC)

<!-- image -->

Removal Energy (e.g., Ion Energy)

FIG. 6. (Color) Illustration of an energy scan for the ALE removal step. The ALE window in Regime II indicates the desirable operating range.

sources. The scan is divided into three regions. Region I represents incomplete etching for low removal energy, while region III represents over-etching for high removal energy (e.g., sputter). Region II represents the 'ALE window' with complete removal independent of energy, indicative of selflimiting behavior. The window is analogous to the so-called ALD window where energy is typically denoted by substrate temperature. 10 The window exists because the energy barrier to remove the modified layer has been lowered relative to the unmodified layer. Therefore, the width depends on the specific reactant-target-energy combination, and is a measure of how much the modification step lowers the energy barrier to removal. An additional 'selectivity window' can be identified if the window for one material is offset from another. Overall, these tests are valuable in characterizing ALE processes and offering a framework to understanding how different processes depend on the most important parameters in ALE: time and energy.

## IV. SILICON ALE: A CASE STUDY

## A. Background

As the dominant material in the semiconductor industry, silicon has been the principal material in ongoing ALE studies for over 25 years. For illustrative purposes, this section focuses on directional silicon ALE achieved by alternating between chlorination and Ar þ bombardment [Fig. 1(b)]. The chlorine reactant is introduced into the chamber to modify the silicon surface (reaction A). We will discuss delivery of the chlorine thermally as Cl2 gas and also with plasma to increase the reaction rate by dissociating Cl2 into reactive species. Chlorine-based chemistry is commonly used in ALE for silicon, as well as germanium, 62 metal oxides, 51,52,63 and III-V materials. 40,64-69 After purging the excess chlorine from the chamber, an Ar plasma provides ion bombardment to activate removal of the silicon chloride reactive layer (reaction B), followed by purging of by-products. Henceforth, silicon chloride will be represented by SiClx (where x can be 1, 2, 3, or 4) unless otherwise specified. Although the mechanisms are not entirely understood even in the ALE case study, separation into unit steps allows a much more systematic investigation than possible for continuous etching.

## B. Thermal chlorination

The purpose of the modification step is to form a thin, reactive surface layer with a well-defined thickness that is more easily removed than the unmodified material in the subsequent removal step. This step is not intended to etch, as shown in the flat portions of Fig. 4. In our example here, chlorine modifies the silicon surface by chemisorption. Chlorine gas spontaneously chemisorbs onto a clean silicon surface at room temperature to form a SiClx layer: Cl2 (g) þ Si (s) ! SiClx (s). This reaction is dissociative, as one chlorine atom at a time from the dimer adsorbs onto a silicon dangling bond. 70 In the simplest two-dimensional model, each silicon surface atom bonds to one chlorine atom. X-ray photoelectron spectroscopy (XPS) data show the SiCl bonding on the surface, with some SiCl3 groups that may be related to damage generated by the removal step that produces addition silicon reaction sites. 71 The role of chlorine is to weaken the underlying Si-Si bond to make it more easily removable from the pristine silicon lattice. The Si-Cl bonding energy of 4.2 eV is stronger than the pristine Si-Si bond of 3.4 eV. 72 Park et al. explained that electron transfer by the electronegative Cl weakens the silicon-to-silicon binding energy just underneath the SiClx layer. 71 This lowers the threshold energy for removing the SiClx layer with respect to the pristine silicon, as the underlying Si-Si bond strength is reduced from 3.4 eV down to an estimated 2.3 eV. 73 The concept of enhanced removal by chemical means is also fundamental in continuous plasma etching, where chemical reactants are used to enhance sputter yields. 12,74 The main distinction in ALE is that chemical modification and removal are separate reaction steps.

In addition, understanding the reaction kinetics is important for making the modification step to proceed as fast as possible. Kinetics of chemisorption are similar to those described in ALD and follow the Langmuir adsorption model. 39 The reaction rate is limited by surface site availability and any steric hindrance, which is minimal in this case since chlorine atoms are smaller in diameter than silicon atoms. The time it takes for chlorine to saturate is given by the surface coverage h ð Þ ¼ ð t 1 /C0 e /C0 K P t /C1 /C1 Þ , where P is chlorine partial pressure and K is the rate constant for adsorption. Thermal chlorination onto silicon was reported to take 8-40 s under typical laboratory conditions. 39 Faster chlorination can happen either by increasing substrate temperatures based on the Arrhenius rate law, or by increasing partial pressure of the chlorine gas. But the substrate temperature should be maintained well below 650 /C14 C, the temperature at which chlorine spontaneously etches silicon. 75 Note that silicon surfaces form a native oxide layer upon exposure to air. Laboratory studies typically remove this layer using a solution of HF diluted in deionized water immediately prior to loading wafers into vacuum. 48

## C. Plasma chlorination

To be productive for manufacturing, adsorption reactions need to proceed at a reasonable rate, with specific requirements depending widely on application. For example, a requirement of etching 1 nm of silicon in only 10 s would translate into about a monolayer (0.14 nm) removed every couple of seconds. Plasma can be used to speed up chlorination by producing highly reactive chlorine radicals and/or energetic species to induce the surface modification. 5 Adsorption rate constants for reactions in plasma are known to increase by orders of magnitude compared to thermal methods. 55 In the silicon ALE case study, chlorination time was reported to saturate in less than 1 s. 76 The use of plasma is also well known in ALD, where plasma-assisted steps replace reactions that might otherwise be difficult or slow using thermal methods. 77 ALD articles suggest many advantages that include decreased cycle time, more freedom in precursor choice, and lower operating temperature. The

productivity of ALE may also benefit as multiple monolayers are removed per cycle due to subsurface chlorination.

The plasma-assisted ALE technique was demonstrated on silicon in 2013 by Lam Research, as reported by several of the authors of this review article, using a commercial transformer coupled plasma (TCP) reactor. 6,55 After HF dip to remove the native oxide, we chlorinated the silicon surface with pure Cl2 plasma (using conditions with minimal spontaneous etching). The excess chlorine was then purged from the chamber, and the wafer was exposed to an Ar plasma with applied bias of 50 eV to accelerate the ions toward the wafer surface. Self-limiting 55 removal of the chlorinated layer was observed with EPC of /C24 0.7 nm, which corresponds closely to the estimated /C24 0.5 nm reactive layer thickness in simulations by Brichon et al. 20 In validation of the plasma-assisted ALE concept, the technique produced characteristic ALE benefits as shown in Fig. 7, including atomically smooth silicon surfaces, excellent etch depth uniformity across the wafer (with no compensation), and flat silicon etch front. 6

The chlorinated silicon surface is more complex with exposure to plasma than from using thermal methods. Generally, in processing plasmas, neutral densities typically are several orders of magnitude higher than ion densities. Therefore, surface chemistry is thought to be dominated by

<!-- image -->

## c) Surface Smoothness

FIG. 7. Plasma-assisted silicon ALE, after etching 50 nm directionally. The results show characteristic ALE benefits at all length scales: (a) excellent depth uniformity across the wafer, (b) flat silicon etch front on the feature, and (c) smooth surface. Reprinted with permission from Kanarik et al. , Solid State Technol., 56 , 24 (2013). Copyright 2013, Lam Research Corporation.

<!-- image -->

interaction of the silicon wafer with chlorine radicals, with some influence from chlorine ions, Cl2 þ and Cl þ , photons, and electrons. 77 Researchers have performed molecular dynamics simulations to better understand the modified surface. 20,78 Brichon et al. obtained self-limiting SiClx layer thickness of /C24 0.5 nm by controlling ion energy &lt; 10 eV and using a weakly dissociated plasma. 20 This reactive layer is significantly thinner than the mixed layer in continuous plasma etching, estimated at 4 nm SiClx at 50 eV (Ref. 18) and &gt; 20 nm at high ion energy. 28 Overall, this highlights the importance of advanced plasma techniques for controlling ion energy distributions arriving at the wafer and plasma species generation pathways for successful plasma-assisted ALE. Plasma-surface interactions are especially complex and further in-depth study would be useful.

## D. Argon ion bombardment

In this section, we discuss the mechanistic understanding of Ar þ bombardment in the removal step. The purpose of the removal step is to provide energy to break the Si-Si bonds underneath the surface Si-Cl. This energy can be supplied thermally by raising the wafer temperature to above 650 /C14 C for desorption of SiCl2. 75 However, this results in an isotropic process since both chlorination and thermal desorption are nominally isotropic [Fig. 2(b)]. Also, high wafer temperatures are detrimental to active devices, so lower processing temperatures are desirable. The advantage of using ions is that they can be accelerated toward the wafer to provide the added benefit of directionality, while maintaining low wafer temperature. Although the ion neutralizes before it reaches the surface, we still refer to the particle as an ion for simplicity. 79 Also, Ar does not generally remain in the silicon substrate, as most of the Ar recoils or reflects back into vacuum after impact. 36 All in all, the primary role of the Ar þ is to provide energy to the etch front.

Typically /C24 50 eV Ar þ are directed toward the wafer surface, as this energy is within the ALE window for this silicon example. Perhaps surprisingly, 50 eV is significantly greater than weakened Si-Si bond energies of 2.3 eV, and greatly exceeds the energy equivalence of 650 /C14 C ( /C24 0.1 eV) used for thermal desorption. The higher energy is required due to the inefficiency in transferring the ion energy to the target bond, as explained by collision theory of ion bombardment, which is applicable to chemically assisted ion etching. 80,81 Ion energy is deposited by the impinging ion into the nearsurface region, leading to a collision cascade of silicon atoms. The Si-Si bond is broken and SiClx product emitted into the vacuum only when the trajectory of the SiClx is upward with sufficient kinetic energy to overcome the surface energy. 81,82 Most of the incident ion energy is dispersed as at least three atoms must collide in order for the SiClx product to escape in an upward direction. Thus, ion energy must be significantly higher than bond energy in order for removal to take place. Another consequence of the inefficiency is that even at energies above the removal threshold, the majority of Ar þ are not efficient. The ion yield estimate of /C24 0.1 suggests that approximately ten ions (50 eV) are needed to

emit one SiClx by-product in ALE. 36 These low ion yields limit the removal step times, which can be very long in laboratory conditions-greater than a minute. 49,83 Fortunately, many commercial etching reactors have relatively high ion flux capability that helps reduce process step times. 22 Still, finding ways to further reduce these process times effectively would be a useful area of research for increasing ALE productivity.

There is some discrepancy as to the expected amount of material removed per cycle during the Ar bombardment step. The removal pathway was studied by Athavale and Economou using molecular dynamic simulations on an ideal silicon surface covered with a monolayer of chlorine atoms. 36 Their work suggested that with Ar ion-assisted removal at 50 eV, 84% of the silicon is removed as SiCl. This mechanism implies that the ideal EPC is the distance between atomic layers, 0.14 nm for the Si (100) surface. 49 There are other feasible pathways that have also been proposed. For example, the pathway for thermal desorption in silicon ALE involves surface diffusion and the product is expected to be SiCl2 based on the reaction Si-SiClx(s) fi Si (s) þ SiCl2 (g). 75 In this case, the first-order estimated EPC would be half a monolayer, or 0.07 nm. In fact, in early ALE studies, self-limited half a monolayer EPC was observed in ion-assisted removal of chlorinated silicon surface. 39,88 The reason for the different EPC values in silicon ALE is not entirely understood. However, it serves to show that EPC is not a defining factor in ALE even in relatively ideal circumstances, and that monolayer removal is not a universal expectation. In addition to different pathways, other effects such as steric hindrance and initial surface roughness will also factor into the amount etched per cycle. 9

The removal step can have the effect of resetting the silicon surface after completion of each cycle. This phenomenon differs from continuous etching, in which the surface tends to accumulate roughness and inhomogeneity. Continuous plasma etching simultaneously exposes the surface to energetic Ar þ , as well as reactive ions such as Cl þ and Cl2 þ that are similarly energetic as the Ar þ . Energetic reactant ions damage the silicon as they break Si-Si surface bonds, thus allowing Cl atoms to diffuse and alter the lattice structure. 12 Accumulated surface roughness occurs with the strong Si-Cl bonding that produces a high activation barrier for surface diffusion and prevents flattening of the silicon surface. 82,84,85 In ALE, the difference is that the removal step does not involve reactive chlorine ions because chlorine is not intentionally present. Although energetic Ar þ can break Si-Si bonds, at Ar þ energy values well below the sputtering threshold, these bonds can reform once the chlorine bonds are removed. 12 This smoothing or resetting effect in silicon ALE is thus attributed to the higher surface atom mobility under Ar þ bombardment at suitable ion energies. 82

Over the years, a wide variety of plasma sources have been used for generating the Ar þ in ALE. These include electron cyclotron resonance plasma, 33,39,56,62,86,87 helicon source plasma, 49,88 TCP, 6 capacitively coupled plasma, 5,60,89 and inductively coupled plasma. 90 Other types of energetic species have also been evaluated, including ion beams, 40,48 neutral beams, 35,50-52,68,69,83,91-96 and laser beams. 32,66,67,97,98 While specialized equipment certainly plays an integral part in basic understanding of ALE, it may be more practical to adapt conventional etching equipment for use in ALE. 5,6

## E. Nonideal reactions

Silicon ALE works best when chlorination produces a well-defined reactive layer and Ar þ remove just this layer, no more or less. However, nonideal behavior can occur in subsaturation mode or when secondary reactions are present. Examples of two secondary reactions are discussed in this section: etching during chlorination and pure sputtering during removal. Both phenomena do not saturate in time and so eliminating them is important for self-limited behavior. The synergy test is designed to measure contributions from these two nonsynergistic sources. To clarify, ion-neutral synergy is desirable in ALE, similar to the synergy encountered by Coburn and Winters in their classic 1978 experiments. 15 The difference is that in ALE the ion and neutral reactions are separated and not simultaneous.

The first example of a secondary reaction is 'background' etching during the modification step. Chemical etching during chlorination can compromise process results by undercutting the mask or increasing surface roughness. 33,99 Chemical etching is less problematic in thermal chlorination because chlorine molecules do not spontaneously etch silicon. In general, chemical etching can be suppressed by cooling the substrate, based on the Arrhenius equation for temperature dependence of reactions. 33 However, plasma chlorination considerably increases the possibility of background etching due to the presence of radicals, ions, photons, metastables, and low energy electrons, all of which can potentially induce etching. 13 Photons may play a role, as they are known to induce subthreshold etching as described by Shin et al. 100 Low energy ions should not etch at subthreshold energies ( &lt; 16 eV), although molecular dynamic simulations by Brichon et al. show a finite silicon etching yield for chlorine ions with kinetic energies as low as 5 eV. 20 Even 'nonreactive' species in plasma such as He neutrals can deliver substantial ( &gt; 10 eV) energy through relaxation of Rydberg states. 101 Addressing this challenge involves operating in a plasma process regime that minimizes generation of excited states, ions, and photons. Experiments have shown that careful selection of this plasma regime can greatly reduce unintended silicon etching during plasmaassisted adsorption, as well as minimizing chlorination time to only the amount needed for saturation. 76

The second example of a secondary reaction is physical sputtering of pristine silicon in the removal step. This can hinder etching selectivity to an underlayer or mask material, as pure physical sputtering can be indiscriminate. Furthermore, sputtering of mask material onto the etch front can lead to etch stop or micromasking. However, the onset of pristine silicon sputtering may be difficult to avoid, especially if the width of ion energy distribution is not sufficiently narrow relative to the ALE window. Delivering ion energy within a very specific range is thus important, and

narrow ion energy and angular distributions are desirable. 5,14 Another proposal has been to replace Ar with other atoms that have lower sputtering yields since Ar is especially efficient at sputtering silicon due to the similar masses. Other bombarding particles such as neon 50,68,69,96 have been explored as well. More studies are needed to better understand the trade-offs in using different bombarding particles, and in managing any unintentional sputtering.

## V. MATERIALS STUDIED BYALE

## A. Overview

This section gives an overview of the more than 20 materials used in ALE studies, including elemental semiconductors, compound semiconductors, insulators, and metals. There is still opportunity to study many others, especially in comparison to the 160 systems in ALD. 11 In studying materials, the focus has generally been on directional etching, usually by providing bombardment in the removal step. Isotropic ALE has also been studied and contributes to about one third of surveyed ALE reports. A timeline highlighting some of the diversity of ALE reports is shown in Fig. 8. Modeling efforts started in the late 1990s and includes computational techniques such as molecular dynamics, kinetic Monte Carlo simulations, density functional theory, and feature scale simulators. 5,36,95,99,102-104 Experimentally, a variety of self-limiting mechanisms have been investigated as described throughout this section. Illustrations of different modification mechanisms are shown in Fig. 9, including: chemisorption, deposition, conversion (e.g., oxidation), and extraction. Removal methods include thermal desorption, particle bombardment, and chemical reaction. A number of these ALE systems use plasma assistance in the modification and/or removal step. All the techniques follow the ALE principles outlined earlier.

## B. Silicon

The earliest silicon ALE study was by Horiike et al. in 1990 using fluorine atoms from CF4-plasma at wafer temperature of /C0 60 /C14 C, because fluorine atoms require low temperatures to suppress spontaneous reaction during adsorption. 33

Other fluorine sources have included NF3 (Ref. 86) and fluorocarbons. 102 Fluorocarbons provide the fluorine reactant at room temperature without spontaneously etching, and will be discussed further in Sec. V C. Overall, chlorine has been the reactant of choice in reaction A of silicon ALE, 6,28,39,49,75,83,88,91 most typically by thermal chemisorption [Fig. 9(a)]. The first to report on chlorine reactant in silicon ALE was Matsuura et al. 39 Other experimental studies followed, such as Athavale and Economou reporting removal of one atomic layer of silicon per cycle. 49 In 1995, isotropic ALE of silicon using thermal desorption was first reported by Imai et al. , showing that the chlorinated layer could be removed with heat instead of ions. 75 The use of neutral beam in the 2000s was applied to silicon ALE with the intention to minimize any charge-related damage. 91 In 2013, Kim et al. used a neutral beam in ALE to remove damaged silicon at the bottom of a 20 nm-node high aspect ratio (HAR) contact. 28 Device benefits were indicated, as the resistance of the remaining silicon was similar to the unetched silicon. Most recently, ALE silicon using chlorine plasma was successfully demonstrated by the authors in 2014 on a commercially available reactor (Fig. 7), 6,55 showing that ALE can be adapted to the manufacturing environment. High selectivity was demonstrated for etching silicon directionally and selective to silicon dioxide (SiO2), achieved by lowering removal ion energies to below 40 eV. 61 Besides fluorine and chlorine, higher halogens such as bromine have only occasionally been studied. 105 (For more information on silicon ALE, see also Sec. IV).

## C. Oxides

Etching of silicon dioxide (SiO2) and high dielectric constant oxides is an important part of integrated circuit manufacturing and has been a focus of ALE studies. Studies of high dielectric oxides in the 2000s used the approach of alternating chemisorption [Fig. 9(a)] and ion bombardment, as in the silicon ALE example. Yeom's research group at Sungkyunkwan University has been especially prolific in publishing ALE studies for high k oxides including hafnium oxide (HfO2), 35,51,106 titanium dioxide (TiO2), 52 aluminum oxide (Al2O3), 54,95 and

FIG. 8. Timeline of highlighted ALE reports between 1988 and 2014.

<!-- image -->

Generic

ALE Cycle:

FIG. 9. (Color) Comparison of different mechanisms to modify the surface in ALE by (a) chemisorption, (b) deposition, (c) conversion, and (d) extraction. In the extraction case, the original material is a compound, with the modification removing one element preferentially from the topmost surface, while the other element is removed in the subsequent removal step (not shown here). Examples of mechanisms are given throughout Sec. V. Colored atoms represent reactant chemical species.

<!-- image -->

beryllium oxide (BeO). 53 In adapting the silicon ALE example, Cl2 was substituted with BCl3 gas because B-O bonding of 8.39 eV is much stronger than Cl-O bonding of 2.82 eV, which is too weak to form the reactive layer with oxygen in metal oxides. 52 Oxides provide an opportunity to study stoichiometry, and a number of studies have confirmed that surface stoichiometry is maintained during ALE. XPS measurements showed that in HfO2 ALE the atomic percentage of Hf and O remains relatively constant, especially compared to the hafnium-rich surfaces obtained after continuous RIE. 51 This result was found in the other oxide cases as well, and highlights the benefit of ALE in maintaining stoichiometry and providing smooth surfaces during directional etching. This is in contrast to continuous etching of compound materials, which has high tendency to alter stoichiometry as one element is favorably removed relative to another. 4,51-53

aligned contact etching, which requires etching narrow ( &lt; 15 nm) oxide spaces more than 100 nm deep without removing the nitride spacer surrounding the gate. 60 To clarify a possible confusion regarding deposition-based ALE, it is indeed similar to a Bosch process in that both alternate between deposition and etching steps. 108 However, the Bosch process is usually optimized to protect the feature sidewall and to remove much more than just the reactive layer in each cycle.

For ALE of SiO2, a fluorocarbon deposition approach was developed that provides both fluorine and carbon reactants in the modification step, as represented in Fig. 9(b). The process is directional due to ion bombardment in the removal step. In this instance, simulations came before relevant experimental data, as deposition-based ALE was first proposed in the 2000s based on the ability of fluorocarbons to form thin reactive layers using low energy CFx ions and radicals from plasma. 5,102 This deposition-based ALE concept was experimentally verified by Metzler et al. in 2013 using a /C24 0.1-0.7 nm thick fluorocarbon film. 90 Their work was heralded as a milestone 107 as it demonstrated that SiO2, the most widely used dielectric material in the semiconductor industry, can be atomically removed using ALE. Recently, Hudson et al. further verified that this process has benefits for etching SiO2 selective to Si3N4. 60 This is possible because the presence of carbon facilitates oxygen removal but hinders etching of silicon and Si3N4. The selectivity obtained is important for critical applications such as self-

A third type of oxide ALE was reported in 1994 for removal of SiO2 in which the film surface is consumed to form a silicate salt product followed by sublimation of the salt at elevated temperatures ( &gt; 100 /C14 C). 109 The process has been referred to as 'atomic layer removal' 44 and is nominally isotropic. The salt is formed when F and N atoms (e.g., NF3 downstream plasma) react with SiO2 at room temperature to consume the top of the film to form a /C24 5-10 nm reactive layer, as represented by Fig. 9(c). The salt formation is substantially self-limiting because it acts as a diffusion barrier to further reaction at the SiO 2 interface. An advantage of this mechanism is high selectivity, made possible when F and N reactants do not readily form salts with other materials, such as Si3N4 or silicon. This process was originally conceived as a continuous etching process, with the salt formation simultaneous with heating. 110 The difference in ALE is that the salt formation and heating are separated self-limiting reaction steps.

## D. III-V materials

Compound III-V materials are high electron mobility materials that are under consideration as enablers in future devices to replace silicon. These materials include GaAs, and also ternary alloy III-Vs such as arsenides, phosphides, nitrides, and antimonides. 111 These materials tend to have more complicated surfaces than silicon that require surface

stoichiometry nearly identical to that of bulk to keep electronic properties from degrading. 4,111 The benefit of ALE in maintaining stoichiometry and providing smooth surfaces during directional etching is especially attractive for these materials. ALE has been studied on several III-V materials, include GaAs, 32,38,40,43,47,56,64-67,98,112-116 InGaAs, InP, AlGaAs, InAlAs, and AlGaN. 34,50,56-58,68,69,97 The majority are on directional ALE using alternating chlorination [Fig. 9(a)] and particle bombardment. For example, Park et al. studied ALE on the gate recess process in InP high electron mobility transistor. The stoichiometry of InP remained similar to the original film, indicating no preferential removal of indium or phosphorous, in contrast to continuous etching. 68,69 Similar benefit was found for other III-V materials, including tertiary compounds such as InAlAs. 50 Researchers have concluded minimal damage in directional ALE of III-Vs based also on electrical characteristics similar to the unetched surface. 50,56-58

About a quarter of the studies on III-V materials involved isotropic ALE, 34,114-116 originally referred to as 'digital etching' and dating back to the 1990s. The reactive layer is formed by oxidizing the substrate consuming the topmost surface (reaction A), as represented in Fig. 9(c). This is followed by removal of the oxidized layer by submerging the wafer into a wet acid bath (e.g., HCl solution) (reaction B). A wide variety of oxidizing methods have been used. The earliest reference is by Djamdji and Blunt on InGaAs with self-regulating anodic oxidation in an electrochemical solution. 34 A few years later, DeSalvo et al. reported an entirely wet ALE approach for GaAs and other III-V semiconductor materials using wet solution oxidation (e.g., H2O2). 114 Alternative oxidation methods have included dry delivery, such as atomic oxygen from plasma 57 and ambient air. 114,116 The oxidation is self-limiting by diffusion kinetics that saturate to a certain thickness, following a logarithmic growth rate that slows sufficiently with time. 114 The oxidized layer thickness was reported to be 1.5 nm in GaAs 115 and 0.5 nm layer in AlGaN (Ref. 57) at room temperature. The isotropic ALE approach offers an improvement over continuous wet etching, which operates both reactions A þ B continuously. By separating the distinct chemical reactions into two steps, the etch amount and variability of the wet etch can be better controlled, and stoichiometry can be maintained. 34,114,115

## E. Other materials

Metals are used throughout device manufacturing to form gates, interconnects, and electrical connections of the device. New metal materials are potential candidates for emerging memory devices, such as MRAM. Etching metals using continuous etching is often itself challenging, because many metals form nonvolatile etch byproducts that redeposit on sidewalls rendering the device useless. If ALE can address this challenge it will have a big impact on enabling metal integration into devices. 117 However, only a few metal ALE reports have been published. In 2000, Kuo and Lee reported a two-step self-limiting process for copper (Cu) by chlorinating the surface, followed by immersion into dilute HCl bath to dissolve the CuClx product, which leaves the Cu substrate intact. 118 More recently, Hess et al. reported an all-dry ALE approach for Cu by chlorinating with plasma and then using H2-plasma to remove the CuClx layer. 119-121 Although the copper ALE etching has directional components, it has limitations for small feature sizes due to significant profile taper. 121 ALE of germanium (Ge) metalloid was reported using chlorination to form the reactive layer, and then either thermal (i.e., isotropic) removal, 59 or ion-assisted (i.e., directional) removal. 62 In isotropic thermal ALE of Ge, selectivity to Si or SiGe was achieved by controlling temperature of removal, since the critical temperature was 260 /C14 C for Ge compared with 650 /C14 C for Si. 59

Graphene and other 2D structure materials are candidates for futuristic post-CMOS technology devices to replace silicon. 122 Removal of a controlled number of layers has been demonstrated using ALE on graphene and graphene-like materials. 92,93,123 A highly publicized report of graphene ALE appeared in Science magazine in 2011. 123 In this report, Dimiev et al. used zinc deposited by sputtering onto the top layer of graphene, as represented in Fig. 9(b). The data indicates that sputtering caused damage to the top layer of carbon atoms and partially embedded it into the zinc lattice. The damaged layer was subsequently removed by an acid treatment that washed away the layer along with zinc. 41,123 Graphene was also studied with directional ALE, using oxygen atoms from plasma to form the reactive layer on the uppermost graphene layer, followed by an Ar neutral beam, removing one monolayer of graphene in each cycle. 92,93 Besides graphene, directional ALE has also been successful on other potential 2D supermaterials, such as transition-metal dichalcogenide semiconductor (MoS2). 63

Polymer surfaces were explored with ALE by Vogli et al. on a polystyrene-based polymer, where a modified surface was produced by exposing polymer surface to oxygen gas (O2) (reaction A). 89 Oxygen adsorbed to the surface, and the reactive polymer surface was rapidly removed in a selflimiting manner under exposure to a low power Ar plasma (reaction B). The authors noted, as others have too, that the modification step (i.e., oxide adsorption here) is likely facilitated by the modification that occur due to ion bombardment.

Silicon nitride (Si3N4) is used for gate spacers and other parts of devices. Two different ALE approaches have been demonstrated for removal of Si3N4. 42,87 In this case, chlorine is not a suitable precursor because Si-N bonding is stronger than Cl-N bonds. 87 Instead, in 1999, Matsuura et al. demonstrated a novel directional ALE approach where reaction A consisted of removing nitrogen on the surface by excited hydrogen gas exposure to form ammonia (NH3) gas byproduct, as represented in Fig. 9(d). In the subsequent reaction B, the remaining outermost silicon atoms were removed by irradiation with low energy ion bombardment, using well-controlled condition that suppresses further removal of any nitrogen. Another approach was demonstrated by Posseme et al. and referred to as 'thin layer etching.' The Si3N4 was modified by light ion implantation (H2-plasma) to implant hydrogen into 10-20 nm of the surface. This step

was followed by wet etching in aqueous HF solution that removed the modified layer an order of magnitude faster than the nonmodified material. The data in this study suggests that the substantially self-limiting behavior is related to the gradient of hydrogen concentration in the film, 42 an example of the conversion mechanism shown Fig. 9(c).

While the semiconductor industry has been driving research on ALE, a number of examples were found in related industries. In 1991, an electrochemistry-based ALE process was reported for the compound semiconductor cadmium telluride (CdTe) used in electro-optics. 124 This approach is an example of the 'extraction' category as the oxidation actually removes specific elements in the compound (e.g., Cd in CdTe) in the top material layer. Other compounds such as GaAs could also work with this method. Another example outside the semiconductor industry was reported in 2009 for ALE of gold-based materials (e.g., AuSn) used in light-emitting diodes. 125 For binary etching of compounds, each element of the component was preferentially extracted in only the topmost layer using separate wet etchants, leaving an atomic layer of the other element to be removed in the subsequent step, as shown in Fig. 9(d).

## VI. RELATION TO POWER PULSING

Pulsing or pulsed operation refers to the modulation of process parameters, which is necessary for achieving separation in atomic layer etching. However, the subject of plasma pulsing in etching has largely been studied independently of ALE, with much of the pulsing literature motivated by the desire to better control plasma parameters. There has been a strong focus on 'power' pulsing, where the plasma powers are modulated in time while keeping the pressure and gas composition fixed. 126 Power pulsing has been studied for many years, with over 50 000 references since 1985 representing up to 15% of plasma etching literature. 22 It is widely used in semiconductor industry today due to its ability to enable better uniformity, greater selectivity, and less ioninduced damage. 30,126-131 The productivity advantage of power pulsing is that it does not involve gas exchange and so can be made faster by eliminating overhead time involved in evacuating the chamber between chemically distinct reaction steps. 5

The connection between power pulsing and ALE has been recognized, 5,7,12,22,126,131,132 as suggested by Agarwal and Kushner. 5 This is because power pulsing offers effectively partial separation of reactions A and B. 12,126 An example is substrate bias pulsing, which acts to modulate the ion energy of the plasma at rates 0.1-1000 kHz while keeping other parameters fixed. Figure 10 compares modulation of plasma neutrals and ion energy that can occur in continuous etching, bias pulsing, and ALE involving full gas separation. In the bias pulsing, bias pulsing effectively turns etching on and off in rapid succession, since etching only occurs when the ions are above the threshold ion energy. The 'off' phase has the opportunity to saturate the surface in reaction A, while etching takes place during the 'on' phase. However, one problem with power pulsing is that the etching on phase

FIG. 10. Comparison of etching with (a) continuous and simultaneous delivery of plasma species, (b) pulsed substrate bias pulsing to modulate ion energy, while keeping neutral delivery is fixed, and (c) ALE with fully separation of neutrals and ions, using gas cycling to also modulate the plasma neutrals. In this schematic, neutrals represent reaction A and ion energy represents reaction B.

<!-- image -->

has reactions A and B simultaneously without gas exchange, and so is not self-limiting or able to 'reset' the surface state. Overall, power pulsing can be considered an historical predecessor to ALE, and with proper design achieve some degree of ALE benefits.

## VII. OUTLOOK

While ALE laboratory work has been ongoing for decades, the transition into semiconductor high-volume manufacturing has been slow. A reason is that high-volume manufacturing requires cost-efficiency, and multistep processes like ALE can have low throughputs due to either slow reaction steps or slow switching between steps. To give a sense of process times involved, one of the earliest studies on silicon ALE reported that a single cycle took over 3 h. 86 More typically, cycle times for silicon ALE in the laboratory have varied from /C24 1 min to over 5 min. 6,12 Thus, new manufacturing-focused approaches are being developed to make ALE faster and lower in cost. The approaches include plasma-assisted ALE using existing etching equipment, 5,6,102 application as a final touch-up after continuous etching, 5 and development of more advanced control systems for faster gas modulation. 60 In addition, certain applications may tolerate slower cycle times. For example, feature scaling means

an increasing opportunity for thin film removal ( &lt; 10 nm), where throughputs are dominated not by process time but instead by transfer times into and out of the reactor. At the other extreme, applications that require large amount of material removal ( &gt; 50 nm), such as those for HAR features, may tolerate faster ALE schemes that operate in subsaturation mode or deviate from ideal ALE behavior. Thick film removal steps can often be split into a fast (main) etch step and a slower (over-etch) step, where ALE could be used in the over-etch with little throughput impact. Ultimately, ALE may not be needed in every application: each application will drive its own set of requirements and trade-offs between throughput, cost, and performance.

Looking ahead, atomic layer etching is well-aligned with the needs for formation of devices and interconnects below the 10 nm technology node. As dimensions shrink, properties of surfaces and subsurface layers are becoming increasingly important, especially for alternative materials such as III-V compound semiconductors. This has implications for the ALE roadmap, as novel devices and interconnect schemes drive development of ALE processes for materials other than silicon. While surface quality is usually given the most attention in ALE, other benefits, such as reduced feature loading in high aspect ratio etching applications and higher selectivity, are often just as desirable and warrant further attention. All of this is a great challenge and opportunity for the etch community. A challenge, because much of the future of Moore's law and the semiconductor industry will depend on the progress of this endeavor. An opportunity, because etching may finally, truly shed the stigma of being a 'black box.' 133,134

## ACKNOWLEDGMENTS

The authors would like to thank Wenbing Yang, Rich Wise, John Holland, Dennis Hausmann, Shelly Miyasato, and Steve Grantham from Lam Research for their contributions.

- 1 S. Borkar, IEEE Micro 25 , 10 (2005).
- 2 K. J. Kuhn, M. D. Giles, D. Becher, P. Kolar, A. Kornfeld, R. Kotlyar, S.

T. Ma, A. Masheshwari, and S. Mudanai, IEEE Trans. Electron Devices

, 2197 (2011).

58

- 3 K. Eriguchi and K. Ono, J. Phys. D 41 , 024002 (2008).
- 4 T. Ivanov et al. , Jpn. J. Appl. Phys. 53 , 04EC20 (2014).
- 5 A. Agarwal and M. J. Kushner, J. Vac. Sci. Technol. A 27 , 37 (2009).
- 6 K. J. Kanarik, S. Tan, J. Holland, A. V. V. Eppler, J. Marks, and R. A. Gottscho, Solid State Technol. 56 , 14 (2013).
- 7 E. Korczynski, August 2014, http://semimd.com/blog/2014/08/04/ atomic-layer-etch-now-in-fab-evaluations/.
- 8 P. Kirsch, SEMI Technology Symposium at SEMICON , Japan, Tokoy, Japan, 2013.
- 9 R. L. Puurunen, J. Appl. Phys. 97 , 121301 (2005).
- 10 S. M. George, Chem. Rev. 110 , 111 (2010).
- 11 G. N. Parsons et al. , J. Vac. Sci. Technol. A 31 , 050818 (2013).
- 12 V. M. Donnelly and A. Kornblit, J. Vac. Sci. Technol. A 31 , 050825 (2013).
- 13 K. Nojiri, Dry Etching Technology for Semiconductors (Springer International Publishing, New York, 2015).
- 14 R. A. Gottscho, C. W. Jurgensen, and D. J. Vitkavage, J. Vac. Sci. Technol. B 10 , 2133 (1992).
- 15 J. W. Coburn and H. F. Winters, J. Appl. Phys. 50 , 3189 (1979).
- 16 C. G. N. Lee, K. J. Kanarik, and R. A. Gottscho, J. Phys. D 47 , 273001 (2014).
- 17 M. A. Lieberman, 10th Asia-Pacific Conference on Plasma Science and Technology , Jeju Islnad, Korea, 2010.
- 18 M. E. Barone and D. B. Graves, Plasma Sources Sci. Technol. 5 , 187 (1996).
- 19 M. Wang and M. J. Kushner, J. Vac. Sci. Technol. A 29 , 051306 (2011).
- 20 P. Brichon, E. Despiau-Pujo, and O. Joubert, J. Vac. Sci. Technol. A 32 , 021301 (2014).
- 21 M. A. Lieberman, AVS 60th International Symposium and Exhibition , Long Beach, CA, 2013.
- 22 R. A. Gottscho and K. J. Kanarik, APS 64th Annual GEC , Salt Lake City, UT, 2011.
- 23 S. Hwang and E. Tonnis, Advanced Semiconductor Manufacturing Conference (ASMC) , Saratoga Springs, New York, 2014.
- 24 G. Cunge, B. J. O. Pelissier, R. Ramos, and C. Maurice, Plasma Sources Sci. Technol. 14 , 599 (2005).
- 25 R. A. Gottscho, 34th International Symposium on Dry Process (DPS) , Tokyo, Japan, 2012.
- 26 A. D. Bailey and R. A. Gottscho, Jpn. J. Appl. Phys. 34 , 2083 (1995).
- 27 P. D. Agnello, IBM J. Res. Dev. 46 , 317 (2002).
- 28 J. K. Kim, S. I. Cho, S. H. Lee, C. K. Kim, K. S. Min, and G. Y. Yeom, J. Vac. Sci. Technol. A 31 , 061302 (2013).
- 29 H. Lee, K. Shin, N. Cho, G. Min, C. Kang, W. Han, and J. Moon, Thin Film Solids 517 , 3844 (2009).
- 30 C. Petit-Etienne, M. Darnon, L. Vallier, E. Pargon, G. Cunge, F. Boulard, O. Joubert, S. Banna, and T. Lill, J. Vac. Sci. Technol. B 28 , 926 (2010).
- 31 M. N. Yoder, U.S. patent 4,756,794 (12 July 1988).
- 32 P. A. Maki and D. J. Ehrlich, Appl. Phys. Lett. 55 , 91 (1989).
- 33 Y. Horiike, T. Tanaka, M. Nakano, S. Iseda, H. Sakaue, A. Nagata, H. Shindo, S. Miyazaki, and M. Hirose, J. Vac. Sci. Technol. A 8 , 1844 (1990).
- 34 F. Djamdji and R. Blunt, Mater. Sci. Eng. B 20 , 77 (1993).
- 35 K. S. Min et al. , IEEE International Electron Devices Meeting (IEDM) , Baltimore, MD, 2009.
- 36 S. D. Athavale and D. J. Economou, J. Vac. Sci. Technol. A 13 , 966 (1995).
- 37 'Workshop on Atomic-Layer-Etch and Clean Technology, SEMATECH,' April 2014, http://www.sematech.org/meetings/archives/fep/10605/ index.htm, accessed 7 December 2014.
- 38 T. Meguro, M. Hamagaki, S. Modaressi, T. Hara, Y. Aoyagi, M. Ishii, and Y. Yamamoto, Appl. Phys. Lett. 56 , 1552 (1990).
- 39 T. Matsuura, J. Murota, Y. Sawada, and T. Ohmi, Appl. Phys. Lett. 63 , 2803 (1993).
- 40 Y. Aoyagi, K. Shinmura, K. Kawasaki, T. Tanaka, K. Gamo, S. Namba, and I. Nakamoto, Appl. Phys. Lett. 60 , 968 (1992).
- 41 D. Jariwala, A. Srivastava, and P. M. Ajayan, J. Nanosci. Nanotechnol. 11 , 6621 (2011).
- 42 N. Posseme, O. Pollet, and S. S. Barnola, Appl. Phys. Lett. 105 , 051605 (2014).
- 43 W. T. Tsang, T. H. Chiu, and R. M. Kapre, Appl. Phys. Lett. 63 , 3500 (1993).
- 44 N. Draeger, H. te Nijenhuis, H. Meinhold, B. van Schravendijk, and L. Nittala. U.S. patent 8,058,179 (15 November 2011).
- 45 O. Joubert, E. Despiau-Pujo, G. Cunge, L. Vallier, P. Brichon, R. Blanc, S. Banna, R. Achutharaman, and Y. Zhang, Workshop on Atomic-LayerEtch and Clean Technology , San Francisco, CA, 2014.
- 46 D. Hausmann, 226th Meeting of the Electrochemical Society (ECS) , Cancun, 2014.
- 47 T. Meguro, M. Ishii, H. H. M. Kodama, T. Hara, Y. Yamamoto, and Y. Aoyagi, Jpn. J. Appl. Phys. 29 , 2216 (1990).
- 48 S.-D. Park, K.-S. Min, B.-Y. Yoon, D.-. H. Lee, and G.-Y. Yeom, Jpn. J. Appl. Phys. 44 , 389 (2005).
- 49 S. D. Athavale and D. J. Economou, J. Vac. Sci. Technol. B 14 , 3702 (1996).
- 50 T.-W. Kim et al. , IEEE Trans. Electron Devices 55 , 1577 (2008).
- 51 S. D. Park, W. S. Lim, B. J. Park, H. C. Lee, J. W. Bae, and G. Y. Yeom, Electrochem. Solid-State Lett. 11 , H71 (2008).
- 52 J. B. Park, W. S. Lim, S. D. Park, B. J. Park, and G. Y. Yeom, J. Korean Phys. Soc. 54 , 976 (2009).
- 53 K. S. Min et al. , Microelectron. Eng. 114 , 121 (2014).
- 54 K. S. Min, S. H. Kang, J. K. Kim, Y. I. Jhon, M. S. Jhon, and G. Y. Yeom, Microelectron. Eng. 110 , 457 (2013).

- 55 R. A. Gottscho, K. J. Kanarik, and S. Sriraman, AVS 60th International Symposium &amp; Exhibition , Long Beach, CA, 2013.
- 56 K. K. Ko and S. W. Pang, J. Vac. Sci. Technol. B 11 , 2275 (1993).
- 57 D. Buttari, S. Heikman, S. Keller, and U. K. Mishra, Proceedings of the IEEE Lester Eastman Conference on High Performance Devices , Newark, DE, 2002.
- 58 A. Alian, C. Merckling, G. Brammertz, M. Meuris, M. Heyns, and K. De Meyer, ECS J. Solid State Sci. Technol. 1 , P310 (2012).
- 59 K. Ikeda, S. Imai, and M. Matsumura, Appl. Surf. Sci. 112 , 87 (1997).
- 60 E. Hudson, V. Vidyarthi, R. Bhowmick, R. Bise, H. J. Shin, G. Delgadino, B. Jariwala, D. Lambert, and S. Deshmukh, AVS 61st International Symposium and Exhibition , Baltimore, MD, 2014.
- 61 T. Lill et al ., 226th Meeting of the Electrochemical Society (ECS) , Cancun, Mexico, 2014.
- 62 T. Sugiyama, T. Matsuura, and J. Murota, Appl. Surf. Sci. 112 , 187 (1997).
- 63 G. Y. Yeom, Atomic Layer Etch and Atomic Layer Clean Conference , San Francisco, CA, 2014.
- 64 M. Ishii, T. Meguro, H. Kodama, Y. Yamamoto, and Y. Aoyagi, Jpn. J. Appl. Phys. 31 , 2212 (1992).
- 65 T. Meguro, M. Ishii, K. Kodama, Y. Yamamoto, K. Gamo, and Y. Aoyagi, Thin Solid Films 225 , 136 (1993).
- 66 M. Ishii, T. Meguro, K. Gamo, T. Sugano, and Y. Aoyagi, Jpn. J. Appl. Phys. 32 , 6178 (1993).
- 67 T. Meguro, M. Ishii, T. Sugano, K. Gamo, and Y. Aoyagi, Appl. Surf. Sci. 82-83 , 193 (1994).
- 68 S. D. Park, C. K. Oh, J. W. Bae, G. Y. Yeom, T. W. Kim, J. I. Song, and J. H. Jang, Appl. Phys. Lett. 89 , 043109 (2006).
- 69 W. S. Lim, G. Y. Yeom, S. D. Park, Y. Y. Kim, and B. J. Park, 9th IEEE Conference on Nanotechnology (NANO) , Genoa, Italy, 2009.
- 70 Y. L. Li et al. , Phys. Rev. Lett. 74 , 2603 (1995).
- 71 C. K. Oh, S. D. Park, H. C. Lee, J. W. Bae, and G. Y. Yeom, Electrochem. Solid-State Lett. 10 , H94 (2007).
- 72 L. Sha and J. P. Chang, J. Vac. Sci. Technol. A 22 , 88 (2004).
- 73 S. Sakurai and T. Nakayama, J. Cryst. Growth 237-239 , 212 (2002).
- 74 J. P. Chang, J. C. Arnold, G. C. H. Zau, H.-S. Shin, and H. H. Sawin, J. Vac. Sci. Technol. A 15 , 1853 (1997).
- 75 S. Imai, T. Haga, O. Matsuzaki, T. Hattori, and M. Matsumura, Jpn. J. Appl. Phys. 34 , 5049 (1995).
- 76 T. Lill, S. Tan, W. Yang, K. J. Kanarik, X. Hua, M. Shen, V. Vahedi, J. Marks, and R. A. Gottscho, 36th International Symposium on Dry Process (DPS) , Yokohama, Japan, 2014.
- 77 H. B. Profijt, S. E. Potts, M. C. M. van de Sanden, and W. M. M. Kessels, J. Vac. Sci. Technol. A 29 , 050801 (2011).
- 78 F. Gou, E. Neyts, M. Eckert, S. Tinck, and A. Bogaerts, J. Appl. Phys. 107 , 113305 (2010).
- 79 H. D. Hagstrum, Phys. Rev. 96 , 325 (1954).
- 80 C. Steinbruchel, Appl. Phys. Lett. 55 , 1960 (1989).
- 81 P. Sigmund, Phys. Rev. 184 , 383 (1969).
- 82 H. Feil, J. Dieleman, and B. J. Garrison, J. Appl. Phys. 74 , 1303 (1993).
- 83 S. D. Park, D. H. Lee, and G. Y. Yeom, Electrochem. Solid-State Lett. 8 , C106 (2005).
- 84 D. Humbird and D. B. Graves, J. Appl. Phys. 96 , 791 (2004).
- 85 D. E. Hanson, A. F. Voter, and J. D. Kress, J. Appl. Phys. 82 , 3552 (1997).
- 86 H. Sakaue, S. Iseda, K. Asami, J. Yamamoto, M. Hirose, and Y. Horike, Jpn. J. Appl. Phys. 29 , 2648 (1990).
- 87 T. Matsuura, Y. Honda, and J. Murota, Appl. Phys. Lett. 74 , 3573 (1999).
- 88 B. J. Kim, S. H. Chung, and S. M. Cho, Proceedings of the International Symposium on Thin Film Materials, Processes, and Reliability (Electrochemical Society, San Francisco, CA, 2001), Vol. 2001-24.
- 89 E. Vogli, D. Metzler, and G. S. Oehrlein, Appl. Phys. Lett. 102 , 253105 (2013).
- 90 D. Metzler, R. L. Bruce, S. Engelmann, E. A. Joseph, and G. S. Oehrlein, J. Vac. Sci. Technol. A 32 , 020603 (2014).
- 91 S. D. Park, C. K. Oh, D. H. Lee, and G. Y. Yeom, Electrochem. SolidState Lett. 8 , C177 (2005).
- 92 Y. Y. Kim, W. S. Lim, J. B. Park, and G. Y. Yeom, J. Electrochem. Soc. 158 , D710 (2011).
- 93 W. S. Lim et al. , Carbon 50 , 429 (2012).
- 94 S. D. Park, D. H. Lee, and G. Y. Yeom, J. Korean Phys. Soc. 47 , 469 (2005).
- 95 Y. I. Jhon, K. S. Min, G. Y. Yeom, and Y. M. Jhon, Appl. Phys. Lett. 105 , 093104 (2014).
- 96 T.-W. Kim, J.-I. Song, J. H. Jang, D.-H. Kim, S. D. Park, J. W. Bae, and G. Y. Yeom, Appl. Phys. Lett. 91 , 102110 (2007).
- 97 O. L. Bourne, D. Hart, D. M. Rayner, and P. A. Hackett, J. Vac. Sci. Technol. B 11 , 556 (1993).
- 98 B. Y. Han, C. Y. Cha, and J. H. Weaver, J. Vac. Sci. Technol. A 16 , 490 (1998).
- 99 A. Agarwal and M. J. Kushner, TECHCON, Austin, TX, 2007.
- 100 H. Shin, W. Zhu, V. M. Donnelly, and D. J. Economou, J. Vac. Sci. Technol. A 30 , 021306 (2012).
- 101 A. Fridman and L. A. Kennedy, Plasma Physics and Engineering (Taylor &amp;Francis, New York, 2004).
- 102 S. Rauf, T. Sparks, P. L. G. Ventzek, V. V. Smirnov, A. V. Stengach, K. G. Gaynullin, and V. A. Pavlovsky, J. Appl. Phys. 101 , 033308 (2007).
- 103 P. Moroz, AVS 61st International Symposium &amp; Exhibition, Baltimore, MD, 2014.
- 104 P. Moroz and D. Moroz, 67th Annual Gaseous Electronics Conference (GEC) , Raleigh, NC, 2014.
- 105 C. M. Aldao and J. H. Weaver, Prog. Surf. Sci. 68 , 189 (2001).
- 106 J. B. Park, W. S. Lim, B. J. Park, I. H. Park, Y. W. Kim, and G. Y. Yeom, J. Phys. D 42 , 055202 (2009).
- 107 AVS, January 2014, http://www.avs.org/AVS/files/b4/b40f7ced-2eda4d76-9c42-5152e8947bbc.pdf.
- 108 F. Laermer and A. Schilp, U.S. patent 5,501,893 (26 March 1996).
- 109 S.-J. Jeng, W. C. Natzle, and C. Yu, U.S. patent 5282925 (1 February 1994).
- 110 H. Nishino, N. Hayasaka, and H. Okano, J. Appl. Phys. 74 , 1345 (1993).
- 111 P. Ye, 39th International Symposium on Compound Semiconductor , 29-31 April 2008.
- 112 S. Takatani and T. Kikawa, Appl. Phys. Lett. 65 , 2585 (1994).
- 113 W. T. Tsang, T. H. Chiu, and R. M. Kapre, J. Cryst. Growth 135 , 377 (1994). 114
- G. C. DeSalvo et al. , J. Electrochem. Soc. 143 , 3652 (1996).
- 115 C. A. Bozada et al. , U.S. patent 6,004,881 (21 December 1999).
- 116 K. Hennessy, A. Badolato, A. Tamboli, P. M. Petroff, E. Hu, M. Atature, € J. Dreiser, and A. Imamoglu, Appl. Phys. Lett. 87 , 021108 (2005).
- 117 R. Turkot, Workshop on Atomic-Layer-Etch and Clean Technology , San Francisco, CA, 2014.
- 118 Y. Kuo and S. Lee, Jpn. J. Appl. Phys. 39 , L188 (2000).
- 119 P. A. Tamirisa, G. Levitin, N. S. Kulkarni, and D. W. Hess, Microelectron. Eng. 84 , 105 (2007).
- 120 F. Wu, G. Levitin, and D. W. Hess, J. Electrochem. Soc. 157 , H474 (2010).
- 121 D. W. Hess, Workshop on Atomic-Layer-Etch and Clean Technology , San Francisco, CA, 2014.
- 122 M. LaPedus, Semiconductor Engineering Magazine , 2014.
- 123 A. Dimiev, D. Kosynkin, A. Sinitskii, A. Slesarev, Z. Sun, and J. M. Tour, Science 331 , 1168 (2011).
- 124 J. L. Stickney, Q. Lei, and C. K. Rhee, U.S. patent 5,385,651 (31 January 1995).
- 125 A. Chitnis, U.S. patent 20090050903 A1 (26 February 2009).
- 126 D. J. Economou, J. Phys. D 47 , 303001 (2014).
- 127 M. Schaepkens, G. S. Oehrlein, and J. M. Cook, J. Vac. Sci. Technol. B 18 , 856 (2000).
- 128 S. Samukawa and K. Terada, J. Vac. Sci. Technol. B 12 , 3300 (1994).
- 129 H. Ohtake, S. Samukawa, K. Noguchi, H. Iida, A. Seto, and X. Y. Qian, 4th International Symposium on Plasma Process-Induced Damage , Monterey, CA, 1999.
- 130 A. Agarwal, P. J. Stout, S. Banna, S. Rauf, K. Tokashiki, J.-Y. Lee, and K. Collins, J. Appl. Phys. 106 , 103305 (2009).
- 131 K. J. Kanarik, G. Kamarthy, and R. A. Gottscho, Solid State Technol. 55 , 15 (2012).
- 132 V. M. Donnelly and D. J. Economou, U.S. patent 0,139,748 (16 June 2011).
- 133 R. A. Gottscho, D. Cooperberg, and V. Vahedi, Workshop on Frontiers in Low Temperature Plasma Diagnostics III (LTPD) , Saillon, Switzerland, 1999.
- 134 H. F. Winters, J. W. Coburn, and E. Kay, J. Appl. Phys. 48 , 4973 (1977).