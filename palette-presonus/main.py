#!/usr/bin/env python3
"""
Palette CLI for Presonus applications
"""

import argparse
import json
import sys

def parse_args():
    parser = argparse.ArgumentParser(description="Palette generator for Presonus applications")
    parser.add_argument(
        '-p', '--palette',
        required=True,
        type=str,
        help='Comma-separated list of hexadecimal color pairs (e.g. FF00FF,00FF00)'
    )
    parser.add_argument(
        '-c', '--count',
        required=True,
        type=int,
        help='Total number of colors per pair.'
    )
    return parser.parse_args()

def generate_output(colors: list[int]) -> str:
    structure = {
        'colors': [f"{c:X}" for c in colors]
    }
    return json.dumps(structure, indent=4)

def generate_seq_int(num1:int, num2:int, count:int) -> list[int]:
    list = [num1, num2]
    for index in range(1, count-1):
        value = num1+index*((num2-num1)/(count-1))
        list.insert(-1, round(value))
    return list

def generate_seq_rgb(num1:int, num2:int, count:int) -> list[int]:
    rs = generate_seq_int((num1&0xff0000)>>16, (num2&0xff0000)>>16, count)
    gs = generate_seq_int((num1&0xff00)>>8, (num2&0xff00)>>8, count)
    bs = generate_seq_int(num1&0xff, num2&0xff, count)
    return [(0xff000000|(rs[i]<<16)|(gs[i]<<8)|bs[i]) for i in range(0, count)]

def main():
    result = []
    args = parse_args()
    color_list = [c.strip() for c in args.palette.split(',')]
    print(f"Parsed colors: {color_list}")
    for color1, color2 in zip(color_list[::2], color_list[1::2]):
        result.extend(generate_seq_rgb(int(color1, 16), int(color2, 16), args.count))
    sys.stdout.write(generate_output(result))

if __name__ == "__main__":
    main()
