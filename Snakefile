FASTQ = "data/barcode77.fastq"

rule all:
    input:
        "results/metrics.csv",
        "results/summary_stats.txt",
        "plots/gc_content.png",
        "plots/read_length.png",
        "plots/mean_quality.png"

rule compute_metrics:
    input:
        FASTQ
    output:
        "results/metrics.csv"
    shell:
        """
        if not exist results mkdir results
        python scripts/fastq_metrics.py --input {input} --output {output}
        """

rule plot_metrics:
    input:
        "results/metrics.csv"
    output:
        "plots/gc_content.png",
        "plots/read_length.png",
        "plots/mean_quality.png",
        "results/summary_stats.txt"
    shell:
        """
        if not exist plots mkdir plots
        python scripts/plot_metrics.py --input {input} --plotdir plots --summary results/summary_stats.txt
        """