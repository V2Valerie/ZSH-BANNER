#!/bin/env python3

banner = '''
   ▌ ▐· ▄▄▄· ▄▄▌  ▄▄▄ .▄▄▄  ▪  ▄▄▄ .
  ▪█·█▌▐█ ▀█ ██•  ▀▄.▀·▀▄ █·██ ▀▄.▀·
  ▐█▐█•▄█▀▀█ ██▪  ▐▀▀▪▄▐▀▀▄ ▐█·▐▀▀▪▄
   ███ ▐█ ▪▐▌▐█▌▐▌▐█▄▄▌▐█•█▌▐█▌▐█▄▄▌
  . ▀   ▀  ▀ .▀▀▀  ▀▀▀ .▀  ▀▀▀▀ ▀▀▀ 
     '''

green = "\033[1;32m"
purple = "\033[1;95m"
blink = "\033[5m"
reset = "\033[m"

banner = banner.replace("•", f"{blink}{green}•{reset}")
banner = banner.replace("▪", f"{blink}{purple}▪{reset}")
banner = banner.replace("·", f"{blink}·{reset}")


print(banner)
