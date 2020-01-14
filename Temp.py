import pandas as pd 
from bokeh import charts, output_notebook, show 
  
# output to notebook 
output_notebook() 
  
# read data in dataframe 
df = pd.read_csv(r"D:/kaggle/mcdonald/menu.csv") 
  
# create bar 
p = Bar(df, "Category", values = "Calories", 
        title = "Total Calories by Category",  
                        legend = "top_right") 
  
# show the results 
show(p) 
