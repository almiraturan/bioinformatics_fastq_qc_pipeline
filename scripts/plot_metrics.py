import argparse
import os
import pandas as pd
import matplotlib.pyplot as plt


def save_histogram(data, xlabel, title, output_path, bins=30):
    plt.figure(figsize=(8, 5))
    plt.hist(data, bins=bins, edgecolor="black")
    plt.xlabel(xlabel)
    plt.ylabel("Frequency")
    plt.title(title)
    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    plt.close()


def write_summary_stats(df, output_file):
    metrics = ["gc_content", "read_length", "mean_quality"]

    with open(output_file, "w", encoding="utf-8") as f:
        for metric in metrics:
            f.write(f"{metric}\n")
            f.write(f"count  : {df[metric].count()}\n")
            f.write(f"mean   : {df[metric].mean():.2f}\n")
            f.write(f"median : {df[metric].median():.2f}\n")
            f.write(f"min    : {df[metric].min():.2f}\n")
            f.write(f"max    : {df[metric].max():.2f}\n")
            f.write(f"std    : {df[metric].std():.2f}\n\n")


def main():
    parser = argparse.ArgumentParser(description="Generate FASTQ plots and summary statistics")
    parser.add_argument("--input", required=True, help="Input metrics CSV")
    parser.add_argument("--plotdir", required=True, help="Output plot directory")
    parser.add_argument("--summary", required=True, help="Output summary statistics file")
    args = parser.parse_args()

    os.makedirs(args.plotdir, exist_ok=True)

    df = pd.read_csv(args.input)

    print("CSV columns:", df.columns.tolist())
    print("Number of rows:", len(df))

    save_histogram(
        df["gc_content"],
        xlabel="GC Content (%)",
        title="Distribution of GC Content",
        output_path=os.path.join(args.plotdir, "gc_content.png")
    )

    save_histogram(
        df["read_length"],
        xlabel="Read Length",
        title="Distribution of Read Length",
        output_path=os.path.join(args.plotdir, "read_length.png")
    )

    save_histogram(
        df["mean_quality"],
        xlabel="Mean Quality Score",
        title="Distribution of Mean Read Quality",
        output_path=os.path.join(args.plotdir, "mean_quality.png")
    )

    write_summary_stats(df, args.summary)

    print("Plots and summary statistics created successfully.")


if __name__ == "__main__":
    main()