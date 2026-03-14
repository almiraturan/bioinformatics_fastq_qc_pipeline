Project Description

In this project, I implemented a small bioinformatics pipeline to perform quality control analysis on a long-read FASTQ sequencing dataset.

The goal of the pipeline is to calculate some basic read-level metrics and visualize their distributions. The pipeline processes a FASTQ file and computes three important metrics for each read:

Read length

GC content

Mean quality score

These metrics help us understand the overall quality and characteristics of the sequencing data before performing downstream analyses such as alignment.

The pipeline is implemented using Snakemake to make the workflow reproducible and easy to run.
-------------------------------------------------------------------------------------------------------
Pipeline Overview

The pipeline performs the following steps:
1.Input FASTQ file is read
2.For each read, the following metrics are calculated:
3.Read length
4.GC content
5.Mean read quality score
6.The metrics are stored in a CSV file.
7.Distribution plots are generated for each metric.
8.Summary statistics are calculated and saved in a text file.
------------------------------------------------------------------------------------------------------
Interpretation

These metrics provide an initial quality assessment of the sequencing dataset.
Read length distribution helps determine whether the sequencing run produced reads in the expected size range.
GC content distribution can reveal unusual patterns or biases in the dataset.
Mean quality score distribution indicates the overall reliability of the reads.
If these distributions appear reasonable and quality scores are not extremely low, the dataset can be considered suitable for downstream analysis such as alignment.
-------------------------------------------------------------------------------------------------------
Note: The FASTQ file is not included in the repository due to GitHub file size limits.
To run the pipeline, place the FASTQ file inside the data/ directory.