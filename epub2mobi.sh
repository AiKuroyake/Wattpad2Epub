#!/bin/bash
# A shell script to convert epub format to mobi
# wrote by joewiz https://www.mobileread.com/forums/showthread.php?t=179686
# Coverts one book per time
for f in *.epub; do ebook-convert "$f" "`basename "$f" .epub`.mobi"; done;
