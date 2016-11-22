# ENHANCE

## Install

```
conda install theano opencv 
pip install enhance
```

## Usage

```
enhance lena.jpg
```

Also optionally accepts output path as second argument

## Example

`enhance` doubles an image's resolution. You can achieve any power-of-two upsampling through recursive calls, but unless you have a beastly workstation I don't recommend it.

Lenna and 4x upsampled Lenna 

![slide](https://raw.githubusercontent.com/rueberger/enhance/master/assets/lenna_crop_upsample.jpg) ![slide](https://raw.githubusercontent.com/rueberger/enhance/master/assets/lenna_4x_crop.jpeg)


## Disclaimer

I do do machine learning, but I did not teach these machines. Just wanted to make this easily installable and usable. 

All credit goes to [corochann](https://github.com/corochann/theanonSR). 
