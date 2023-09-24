"""
    @Author: Rezvee Rahman
    @Date: 09/19/2023
    @Version: Python 3.10 

    Descritpion: This is the main runner for my applicaton.
"""
from time import sleep
import Algorithm
import Operations

# WOOOOO SOME ANSI COLORS FINALLY NO MORE BORING STUFF

color_Red = "\033[38;5;196m"
color_Green = "\033[38;5;78m"
color_Yellow = "\033[38;5;190m"
color_Blue = "\033[38;5;39m"
color_Bold = "\033[1m"
color_Reset = "\033[0;0;0m"

Operations_time = Operations.Operations()
Algorithm_algo = Algorithm.Algorithm()
Int_IOPS = 0
Float_FLOPS = 0

def menu():
        try: 
            print(f"""\n
                  \r{color_Blue}CPU - Benchmarking by Rezvee Rahman{color_Reset}\n 
                  \r\t1 - Benchmark with IOPS (Integer Oper. per sec)\n
                  \r\t2 - Benchmark with FLOPS (Floating Point Oper. per sec)\n
                  \r\t3 - Benchmark All\n 
                  \r\t4 - Quit\n

                  """)
            chc = int(input("Enter value Integer value corresponding with the menu: "))
            if(chc  == 4):
                print(f"\n\r{color_Yellow}Exiting the program{color_Reset}")
                input("\nPress Enter to continue: ")
                return 4 
            elif(chc == 1):
                print(f"\n\r{color_Blue}Executing IOPS Benchmarking.{color_Reset}")
                return 1
            elif(chc == 2):
                print(f"\n\r{color_Blue}Executing FLOPS Benchmarking.{color_Reset}")
                return 2
            elif(chc == 3):
                print(f"\n\r{color_Blue}Starting benchmarking both IOPS and FLOPS.{color_Reset}")
                return 3
            else:
                print(f"\n\r{color_Yellow}There is no option associated with the inputs please enter something corresponding with the menu choices{color_Reset}")
        except:
            print(f"\n\r{color_Red}Unknown entry was given please try again. {color_Reset}")
            return None  


def iopsExecution():
    float_TimeList = []
    for i in range(0, 20):
        print(f"Starting Benchmark [{i}]")
        Operations_time.__init__()
        Algorithm_algo.__init__()
        Operations_time.start()
        Algorithm_algo.startIOPS()
        Operations_time.end()
        float_TimeList.append(Operations_time.getDiff())
    print(f"{color_Green}Completed program.{color_Reset}")
    avg = 0
    for i in range(0, len(float_TimeList)):
        avg += Algorithm_algo.INT_LIMIT/(float_TimeList[i]/10_000_000_000) 
    avg = avg/len(float_TimeList)
    print(f"Average time for computation of the IOPS is approximately: {avg} Integer Point Ops per Second.")
    input("Press [enter] to continue ")

"""
    Dear god why did I decide to design my code like this?
    The idea at least in my head is to make my code modular
    but I think I made this into some frankenstein abomination
    ~ Rezvee
"""
def flopsExecution():
    float_TimeList = []
    for i in range(0, 20):
        print(f"Starting Benchmark [{i}]")
        Operations_time.__init__()
        Algorithm_algo.__init__()
        Operations_time.start()
        Algorithm_algo.startFlops()
        Operations_time.end()
        float_TimeList.append(Operations_time.getDiff())
    print(f"{color_Green}Completed program.{color_Reset}")
    avg = 0
    for i in range(0, len(float_TimeList)):
        avg += Algorithm_algo.INT_LIMIT/(float_TimeList[i]/10_000_000_000)
    avg = avg/len(float_TimeList)
    print(f"Average time for computation of the FLOPS is approximately: {avg} Floating Point Ops per Second")

def main():
    while(True):
        int_Option = menu()
        if(int_Option == 4):
            print("\nExiting program.\n")
            break;
        elif(int_Option == 1):
            print("Starting in")
            sleep(1)
            print("3")
            sleep(1)
            print("2")
            sleep(1)
            print("1")
            sleep(1)
            iopsExecution()
        elif(int_Option == 2):
            print("Starting in")
            sleep(1)
            print("3")
            sleep(1)
            print("2")
            sleep(1)
            print("1")
            flopsExecution()
        elif(int_Option == 3):
            print("Starting in")
            sleep(1)
            print("3")
            sleep(1)
            print("2")
            sleep(1)
            print("1")
        else:
            print("Retrying Program")
        




    return None


if __name__ == '__main__':
    main()