Handy little script I wrote a while back that could prove useful in the future - doesn't work with tensorflow-gpu > 2.4 at the moment.

If future me is using conda, see the following:

~~~
conda create -n onnx-production
conda activate onnx-production
pip install -r requirements.txt
~~~


Example usage of h5_to_onnx.py

~~~
python3 h5_to_onnx.py --input_model_path /path/to/model/model.h5 --model_name model --output_model_path /path/to/model/model.onnx
~~~