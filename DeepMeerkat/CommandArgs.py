import argparse
import logging
import os

def CommandArgs(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", help="path of single video",type=str,default='Hummingbird.avi')
    parser.add_argument("--draw_size", help="'Draw' or 'enter' object size",type=str,default='enter')
    parser.add_argument("--size", help="Minimum size of contour",default=0.01,type=float)
    parser.add_argument("--tensorflow_threshold", help="Confidence level to ignore frames",default=0.95, type=float)    
    parser.add_argument("--moglearning", help="Speed of MOG background detector, lowering values are more sensitive to movement",default=0.10,type=float)
    parser.add_argument("--mogvariance", help="Variance in MOG to select background",default=20,type=int)
    parser.add_argument("--crop", help="Set region of interest?",action='store_true')
    parser.add_argument("--draw_box", help="Draw boxes to highlight motion'?",action="store_true")
    parser.add_argument("--show", help="Show frames as you process",action='store_true')
    parser.add_argument("--threaded", help="Run two instances simultaneously on different cores",action='store_true')    
    parser.add_argument("--tensorflow", help="Classify motion objects using tensorflow",action='store_false')
    parser.add_argument("--write_text", help="Write tensorflow label on image",action='store_true')    
    parser.add_argument("--training", help="Just return crop images",action='store_true')    
    parser.add_argument("--output_video", help="Return clips of videos, rather than frames",action='store_true')    
    parser.add_argument("--resize", help="reduce to half size",action='store_true')    
    
    #couple OS specific paths
    if os.name=="nt":
        parser.add_argument("--path_to_model", help="Path to model/ directory",default="C:/Users/ben/Dropbox/GoogleCloud/DeepMeerkat_20180109_090611/model")
        parser.add_argument("--output", help="output directory",default="C:/Users/Ben/DeepMeerkat")        
    else:
        parser.add_argument("--path_to_model", help="Path to model/ directory",default="/Users/ben/Dropbox/GoogleCloud/DeepMeerkat_20180109_090611/model")
        parser.add_argument("--output", help="output directory",default="/Users/Ben/DeepMeerkat")
        
    #if additional args were passed by string from CloudDataFlow
    if argv:
        args,_=parser.parse_known_args(argv)
    else:
        args,_=parser.parse_known_args()
        
    print("DeepMeerkat args: " + str(args))
    logging.info("DeepMeerkat args: " + str(args))
    
    #If training, no tensorflow
    if args.training:
        args.tensorflow=False
        
    return(args)
