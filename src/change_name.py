
# Pythono3 code to rename multiple  
# files in a directory or folder 
  
# importing os module 
import os 
import argparse
ap = argparse.ArgumentParser()
ap.add_argument("--folder",help="directory")
ap.add_argument("--prefix",help="prefix")
ap.add_argument("--ext",help="extension")
folder = ap.parse_args().folder 
prefix = ap.parse_args().prefix 
extension = ap.parse_args().ext 


# Function to rename multiple files 
def main(folder, prefix, extension): 
  
    for count, filename in enumerate(os.listdir(folder)): 
        dst = prefix + str(count) + extension
        src = folder + filename 
        dst = folder + dst 
          
        # rename() function will 
        # rename all the files 
        os.rename(src, dst) 
  
# Driver Code 
if __name__ == '__main__': 
      
    # Calling main() function 
    main(folder, prefix, extension) 