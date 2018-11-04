import argparse
import functions

def main():
    parser = argparse.ArgumentParser(description='CT Image Reconstruction')
    parser.add_argument('-i', '--input_image', type=str, help='path to the location of input image')
    parser.add_argument('-f', '--input_image', type=str, help='path to the location of input image')
    args = parser.parse_args()

    if(args.input_image == None):
        print("Please specify an input image")
        exit()

    img = cv2.imread(args.input_image,0)

    if(args.function == None):
        print("Please specify which function to apply")

    if(args.function == 'img2radon'):
        out = functions.img2radon(img)

    
if __name__ == '__main__':
    main()