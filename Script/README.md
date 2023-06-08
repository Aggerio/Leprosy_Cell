WARNING !!! --> This is a very stripped down approach of Approach 2a based in <link> Approach 2 

the aim is to generate masks for a neural network to train on 

since contouring makes marking the bacteria cells easier it leads to be able generate a lot of masks 
from just 44 images as given in the above example

How to run --> 

Copy all your images in the directory and name it img 

1) Install dependencies

```python
pip install -r requirements.txt
```

2) running --> 

assuming your directory contains jpg or jpeg
the program generates a folder Predicted Masks

which contains the image masks corresponding to the the images in the input directory

for example if you directory is "img"

``` python
python main.py -i img 
```

this generates "Predicted Masks"

