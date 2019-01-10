Data Downloading 

install resnet and resnext (instruction on github) 
location : ~/vikram_files/
----------------
download files 
dest/train/mcatid/image
dest/val/mcatid/image

you need an excel with following format 
pcid mcatid image_url 
in tsv format 
while read -r mcat pcid url; do if [ ! -d "${mcat}" ]; then mkdir -p ${mcat}; fi; cd $mcat; wget -O $pcid $url; cd ..; done < file

command for downloading train folder as desired (to be provided by vikram)
----------------
data cleaning - 2 
convert all other format to jpg 
name them simple .. remove space special char
ddup all data 
-----------------------------
for changing image file dimension in a folder 

find . -name '*' -execdir mogrify -resize 224x {} \;

for changing the image dimensions recursively for folder of folders having multiple images

for d in ~/excavator/pmcat_clean_224_test/train/*/;do (cd "$d" && find . -name '*' -execdir mogrify -resize 224x {} \;); done > /dev/null 2>&1
<change folder name>
---------------------
data level loading - 2
use https://medium.com/nanonets/how-to-use-deep-learning-when-you-have-limited-data-part-2-data-augmentation-c26971dc8ced
mirror image on vertical axis 
use 15deg rotations ... clockwise as well as anticlockwise 
scale (remove white space and transparent background) .. use imagemagik
gaussian noise 

level load ... use simple copy paste and .. make a query for automation 

---------------------

go to torch folder 
rm -rf gen 
edit class no (its no of mcats) 
edit classify.lua # replace image labels from imagenet.lua with our current labels, and pass new imagenet.lua file in classify.lua.

main training command 
th main.lua -nClasses 122 -nEpochs 100 -data ~/excavator/pmcat_clean_224/ -save ~/Desktop/pmcat_clean_224_c122e100b10t4g1 -batchSize 10 -nThreads 4 -nGPU 1

for testing results 
for f in ~/excavator/pmcat_clean_224/train/* ;do ( [ -d $f ] && cd "$f" && echo Entering into $f && th ~/vikram_files/fb.resnet.torch/pretrained/classify_new.lua ~/Desktop/pmcat_clean_224_c9e100b10t4g1/model_best.t7 $f/*  >> ~/Desktop/pmcat_clean_224_c9e100b10t4g1_108.txt); done
