
# To remove the image files' extensions

echo "Removing file extensions..."

for d in ./*/;do (cd "$d" && for f in *;do (mv $f $(echo ${f%*.*}));done); done




# To append .jpg extension in the above filename

echo "Appending .jpg extension"

for d in ./*/;do (cd "$d" && for f in *;do (mv $f `basename $f `.jpg;);done); done > /dev/null 2>&1




# Using the image formatting command 'mogrify' to make all the images' format same i.e. jpeg

echo "Changing the image format into jpeg"


for d in ./*/;do (cd "$d" && for f in *;do (mogrify -format jpg *.jpg;);done); done > /dev/null 2>&1




	
# to format all images except for those having JPEG format

echo "formatting all images except for those having JPEG format"

for d in ./*/;do (cd "$d" && for f in *;do (file $f| grep -v JPEG|mogrify -format jpg $f);done); done






# rename files starting with hyphen(-)

echo "Renaming files whose name starts with -"

for d in ./*/;do (cd "$d" && echo $d  && for f in -*;do ([ -f "$f" ] || continue && mv -- "$f" "${f/-/x}" );done); done




# Find and delete copies of files

echo "Deleting copies of files"

find .  -name "*(*copy).jpg" -exec rm {} \;



# rename .jpg.jpg extensions to .jpg (if any)

echo "Rename all files having .jpg.jpg to .jpg ..."

for d in ./*/;do (cd "$d" && for f in *;do (rename 's/.jpg.jpg/.jpg/' *);done); done







# for changing the image dimensions recursively for folder of folders having multiple images

echo "Reducing width of images to 224..."

for d in ./*/;do (cd "$d" && find . -name '*' -execdir mogrify -resize 224x {} \;); done > /dev/null 2>&1
