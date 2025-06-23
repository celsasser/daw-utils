# Color Palettes
These are our color palettes for *Studio One*. *Studio One* doesn't totally honor the colors in our palette. He manhandles and rearranges the lines. Some of the changes aren't so wonderful, so we touch them up after they are imported. Subsequently, be mindful when reimporting palettes into *Studio One*.

## Importing
Generate your palette and name it whatever you would like to call it. There are commands below primed with suggested names. Once generated, launch *Studio One*. *Studio One 7* treats color palettes like plug-ins. You may drag them over the app and drop them in the browser. I suggest you are explicit with the destination, cuz I don't know where he will put them otherwise.

## Palettes

### Full Spectrum
*Full Spectrum* covers as much of the visible spectrum as we would like. It does not include red nor orange. It generates a total of 160 colors. That's too much too chose from. So, use it to harvest from.
| Light Bright | Dark Bright | Dark Muted | Light Muted |
|------------|----------|------------|----------|
| #FFFFEA | #FFFF00 | #D6D800 | #E6E6D1 |
| #F9FFF0 | #A9FF00 | #36B400 | #D2E2C2 |
| #ADFFFB | #00E2D6 | #4A9591 | #D0E5E4 |
| #BEDFEF | #48A5D1 | #5B8FA0 | #CEDEE3 |
| #B9BFFF | #2F38EA | #5567B6 | #C6CCE7 |
| #E0BCF6 | #7935E4 | #8061B2 | #C8BADE |
| #E2B9F9 | #A729EC | #8F64A7 | #CFBDD9 |
| #F4C2F9 | #D828EB | #9B58A2 | #DBC3DE |
| #F9C2F0 | #EB25CB | #AD64A1 | #DCBCD7 |
| #F9B8DD | #ED1791 | #B67299 | #DCBCCE |
| #DDDDDD | #8c8c8c | #828282 | #2E2E2E |


To generate, run the following in a console and follow the instructions in [Importing](#importing).
```
./palette-presonus/main.py -c 8 -p "#FFFFEF,#FFFF00,#D6D800,#E6E6D1,#F9FFF0,#A9FF00,#36B400,#D2E2C2,#ADFFFB,#00E2D6,#4A9591,#D0E5E4,#BEDFEF,#48A5D1,#5B8FA0,#CEDEE3,#B9BFFF,#2F38EA,#5567B6,#C6CCE7,#E0BCF6,#7935E4,#8061B2,#C8BADE,#E2B9F9,#A729EC,#8F64A7,#CFBDD9,#F4C2F9,#D828EB,#9B58A2,#DBC3DE,#F9C2F0,#EB25CB,#AD64A1,#DCBCD7,#F9B8DD,#ED1791,#B67299,#DCBCCE,#DDDDDD,#8c8c8c,#828282,#2E2E2E" > ~/Downloads/Curtis-Spectrum.colorpalette
```

### Partial Spectrum: Bright
We have selected a subset of the bright colors from [Full Spectrum](#full-spectrum). We are going to generate 4 colors from each pair, for a total of 40 colors.
| Light | Dark |
|-----------|----------|
| #FFFFEA | #d2ac00 |
| #d6facd | #A9FF00 |
| #cdfffc | #00E2D6 |
| #BEDFEF | #48A5D1 |
| #B9BFFF | #464bb6 |
| #E0BCF6 | #6a36be |
| #E2B9F9 | #8c10cf |
| #F4C2F9 | #ba1bcb |
| #F9C2F0 | #d317b4 |
| #e1e1e1 | #6b6b6b |


To generate, run the following in a console and follow the instructions in [Importing](#importing).
```
./palette-presonus/main.py -c 4 -p "#FFFFEA,#d2ac00,#A9FF00,#d6facd,#cdfffc,#00E2D6,#48A5D1,#BEDFEF,#B9BFFF,#464bb6,#6a36be,#E0BCF6,#E2B9F9,#8c10cf,#ba1bcb,#F4C2F9,#F9C2F0,#d317b4,#6b6b6b,#e1e1e1" > ~/Downloads/Curtis-Bright.colorpalette
```

### Partial Spectrum: Muted
We have selected a subset of the muted colors from [Full Spectrum](#full-spectrum). We are going to generate 4 colors from each pair, for a total of 40 colors.
| Light Muted | Dark Muted |
|-----------|----------|
| #e6e6d1 | #a38532 |
| #D2E2C2 | #01a46d |
| #bfdbd9 | #449295 |
| #c1dbe3 | #4f879a |
| #c6cce7 | #54619c |
| #C8BADE | #71569c |
| #e0c9e5 | #79448a |
| #DCBCD7 | #8f4f84 |
| #DCBCCE | #8e4870 |
| #e1e1e1 | #606060 |

To generate, run the following in a console and follow the instructions in [Importing](#importing).
```
./palette-presonus/main.py -c 4 -p "#e6e6d1,#a38532,#01a46d,#D2E2C2,#bfdbd9,#449295,#4f879a,#c1dbe3,#c6cce7,#54619c,#71569c,#C8BADE,#e0c9e5,#79448a,#8f4f84,#DCBCD7,#DCBCCE,#8e4870,#606060,#e1e1e1" > ~/Downloads/Curtis-Muted.colorpalette
```

### Partial Spectrum: Tab20b
This is based on the Seaborn color palette "Tab20b".
|Number|Color|
|------|-----|
| 1 | #4e5083 |
| 2 | #5254A3 |
| 3 | #6B6ECF |
| 4 | #9C9EDE |
| 5 | #637939 |
| 6 | #8CA252 |
| 7 | #B5CF6B |
| 8 | #CEDB9C |
| 9 | #8C6D31 |
| 10 | #bba46b |
| 11 | #ebca7b |
| 12 | #e8d6ac |
| 13 | #824d4d |
| 14 | #AD494A |
| 15 | #D6616B |
| 16 | #E7969C |
| 17 | #7B4173 |
| 18 | #A55194 |
| 19 | #CE6DBD |
| 20 | #DE9ED6 |

To generate, run the following in a console and follow the instructions in [Importing](#importing). We don't interpolate for this one. We take the colors as they are in the palette. Nonetheless, we still construct it via the CLI to be consistent with the rest of our palettes.

```
./palette-presonus/main.py -c 2 -p "#4e5083,#5254A3,#6B6ECF,#9C9EDE,#637939,#8CA252,#B5CF6B,#CEDB9C,#8C6D31,#bba46b,#ebca7b,#e8d6ac,#824d4d,#AD494A,#D6616B,#E7969C,#7B4173,#A55194,#CE6DBD,#DE9ED6" > ~/Downloads/Curtis-Tab20.colorpalette
```
