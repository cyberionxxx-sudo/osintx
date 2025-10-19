# OSINT ASCII logo - corrected S

PURPLE = "\033[95m"
WHITE = "\033[97m"
RESET = "\033[0m"

osint_ascii = f"""
{PURPLE}  Root of Shadows
 ██████╗  ██████╗ ██╗███╗   ██╗████████╗
██╔═══██╗██╔═══   ██║████╗  ██║╚══██╔══╝
██║   ██║██║██║██║██║██╔██╗ ██║   ██║   
██║   ██║      ██║██║██║╚██╗██║   ██║   
╚██████╔╝╚██████╔╝██║██║ ╚████║   ██║   
 ╚═════╝  ╚═════╝ ╚═╝╚═╝  ╚═══╝   ╚═╝   
{WHITE}              OSINT
{RESET} 
[1]\tContinue
[2]\tExit
"""


a= input(osint_ascii)

if a=='1':
    name=input("Name:")
    lis_medi=[("tiktok:   ","tiktok.com"),('instagram',"instagram.com"),('facebook: ',"facebook.com"),('x:        ',"x.com"),('telegtam: ',"telegram.org")]

    for m, l in lis_medi:
        link=(f"https://www.google.com/search?client=firefox-b-lm&channel=entpr&q=site%3A{l}+intext%3A{name}")
        print(f'[+] {m}\t{link}')
else:
    print("Exit")