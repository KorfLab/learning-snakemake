# Make shakefiles
import argparse

parser = argparse.ArgumentParser(description='Make Snakefiles')
parser.add_argument('--aligner', type=str, metavar='<str>', required=False,
	help='input sequence aligner {bwa_mem, bowtie2, STAR} (default: bwa_mem)')
parser.add_argument('-nd', '--no_deduplication', action='store_true',
	help='if tagged, bam files will not be deduplicated')
# call peak
# report
# ...
arg = parser.parse_args()
