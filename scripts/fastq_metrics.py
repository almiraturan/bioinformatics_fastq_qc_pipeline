import argparse
import csv
from Bio import SeqIO


def calculate_gc(seq):
    seq = seq.upper()
    if len(seq) == 0:
        return 0.0
    gc_count = seq.count("G") + seq.count("C")
    return (gc_count / len(seq)) * 100


def calculate_mean_quality(qualities):
    if not qualities:
        return 0.0
    return sum(qualities) / len(qualities)


def main():
    parser = argparse.ArgumentParser(description="Calculate per-read FASTQ metrics")
    parser.add_argument("--input", required=True, help="Input FASTQ file")
    parser.add_argument("--output", required=True, help="Output CSV file")
    args = parser.parse_args()

    with open(args.output, "w", newline="", encoding="utf-8") as out_file:
        writer = csv.writer(out_file)
        writer.writerow(["read_id", "read_length", "gc_content", "mean_quality"])

        for record in SeqIO.parse(args.input, "fastq"):
            sequence = str(record.seq)
            qualities = record.letter_annotations["phred_quality"]

            read_id = record.id
            read_length = len(sequence)
            gc_content = calculate_gc(sequence)
            mean_quality = calculate_mean_quality(qualities)

            writer.writerow([
                read_id,
                read_length,
                round(gc_content, 2),
                round(mean_quality, 2)
            ])


if __name__ == "__main__":
    main()