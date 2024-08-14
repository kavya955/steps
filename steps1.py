import pandas as p
import numpy as n
d={
    'slno':[0,1,2,3,4,5,6,7,8,9],
    'Day':[1,2,3,4,5,6,7,8,9,10],
    'steps':[4335,9552,7332,4504,5335,7552,8332,6504,8965,7689]
}
df=p.DataFrame(d)
df["+1000 steps"]=df["steps"]+1000
fi=df[df["+1000 steps"]<7000]["Day"]
print("\n DataFrame:\n",df)
print("\n Day on which steps were >7000:\n",fi)