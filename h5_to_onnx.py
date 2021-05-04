from tensorflow import keras 
from tensorflow.keras.models import load_model
import keras2onnx
import argparse 
import parser
import os 

print("keras2onnx version is "+ keras2onnx.__version__)


def convert_to_onnx(input_model_path, model_name, output_model_path):

    model = load_model(input_model_path)

    onnx_model = keras2onnx.convert_keras(model, model_name, debug_mode=1)
    
    return keras2onnx.save_model(onnx_model, output_model_path)



def main():

    parser = argparse.ArgumentParser(description="Convert H5 to onnx")
    

    ## Required parameters 

    parser.add_argument(
        "--input_model_path",
        default=None,
        type=str,
        required=True,
        help="Input model path. Should be the path to saved .h5 file"
    )

    parser.add_argument(
        "--model_name",
        default=None,
        type=str,
        required=True,
        help="Name of model"

    )

    parser.add_argument(
        "--output_model_path",
        default=None,
        type=str,
        required=True,
        help="output model path. Should be the path to saved .onnx file"
    )

    args = parser.parse_args()

    convert_to_onnx(args.input_model_path, args.model_name, args.output_model_path)



if __name__ == "__main__":
    main()

    
