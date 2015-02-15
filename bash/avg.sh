read N
sum=0
for (( c=0; c<=$N; c++ ))
do
    read x
    sum=$((sum+x))
done
printf %.3f `echo "$sum/$N" | bc -l`