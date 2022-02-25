# Read the fucking "tqdm" duc , Tnx 

from tqdm import tqdm 
import time



for i in tqdm(range(100),desc="Just wait...", colour="green",ncols=90) :
    time.sleep(1)
    print(" Done ")
    pass
