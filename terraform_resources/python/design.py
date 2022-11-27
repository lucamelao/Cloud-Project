''''
Design relacionado a User Interface.    
'''

class UI:
    def draw_header(self):
        with open("start_image.txt", 'r') as f:
            content = f.read()
            print(f"{COLORS.orange}{content}{COLORS.ENDC}")
    def show_options(self):
        print(f"{COLORS.BOLD}{COLORS.HEADER}{COLORS.UNDERLINE}MAIN MENU\n{COLORS.ENDC}")
        print(f"  {COLORS.BOLD}{COLORS.HEADER}Options: \n\n  1. [B]uild \n\n  2. [L]ist \n\n  3. [D]estroy \n\n  4. [Q]uit \n{COLORS.ENDC}")

class COLORS:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m' 
    orange = '\033[38;5;214m'