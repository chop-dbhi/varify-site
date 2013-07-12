---
layout: default
title: "Varify"
---

### Verify with Varify.
Quickly discover clinically relevant variants using integrated annotations sources.


### First Features and Annotations

Deleterious Probabilities

SIFT
PolyPhen2
Allele Frequency Data

1000G, combined allele frequency, combined allele count
EVS, combined allele frequency, combined allele count
Genes

approved HGNC gene symbols, names, and synonyms
transcripts and exons from RefSeq that can be mapped to HGNC genes
Gene Lists

the single gene list will be in there as well
Disease and Phenotype

diseases loaded from HGMD linked at the gene level and variant level
early stages of phenotype data loaded from NCBO linked to gene
Variant Effects

SNPEff variant effects and impact
PubMed IDs

derived from HGMD and linked to genes and variants
Project-level hierarchy

all samples are tracked via the following hierarchy (this enables a permissions system): PROJECT → COHORT → SAMPLE → RESULTS
Samples

Standard VCF fields - genotype, quality, depth of coverage, etc.
Analysis Workflow

the first step is to select a sample that is of interest
a step-by-step dialog taking the user through most of the above listed annotations with proper defaults





#### Don't Forget

- Add your own content to this page (i.e. `index.md`) and change the `title`
- Change `title` and `subtitle` defined in `config.yml` for your site
- Set the `baseurl` in `_config.yml` for your repo if deploying to GitHub pages
