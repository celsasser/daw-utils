# Color Palettes
These are our color palettes for *Studio One*. *Studio One* doesn't totally honor the colors in our palette. He manhandles and rearranges the lines. Some of the changes aren't so wonderful, so we touch them up after they are imported. Subsequently, be mindful when reimporting palettes into *Studio One*.

## Importing
Generate your palette and name it whatever you would like to call it. There are commands below primed with suggested names. Once generated, launch *Studio One*. *Studio One 7* treats color palettes like plug-ins. You may drag them over the app and drop them in the browser. I suggest you are explicit with the destination, cuz I don't know where he will put it otherwise.

## Palettes

### Full Spectrum: Brighter
| Light Bright | Dark Bright | Dark Matte | Light Matte |
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
./palette-presonus/main.py -c 8 -p "#FFFFEF,#FFFF00,#D6D800,#E6E6D1,#F9FFF0,#A9FF00,#36B400,#D2E2C2,#ADFFFB,#00E2D6,#4A9591,#D0E5E4,#BEDFEF,#48A5D1,#5B8FA0,#CEDEE3,#B9BFFF,#2F38EA,#5567B6,#C6CCE7,#E0BCF6,#7935E4,#8061B2,#C8BADE,#E2B9F9,#A729EC,#8F64A7,#CFBDD9,#F4C2F9,#D828EB,#9B58A2,#DBC3DE,#F9C2F0,#EB25CB,#AD64A1,#DCBCD7,#F9B8DD,#ED1791,#B67299,#DCBCCE,#DDDDDD,#8c8c8c,#828282,#2E2E2E" > ~Downloads/Curtis-Spectrum.colorpalette
```
