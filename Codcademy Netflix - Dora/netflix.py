
from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns



netflix_stocks = pd.read_csv('NFLX.csv')
print(netflix_stocks.head())



dowjones_stocks = pd.read_csv('DJI.csv')
print(dowjones_stocks.head())



netflix_stocks_quarterly = pd.read_csv('NFLX_daily_by_quarter.csv')
print(netflix_stocks_quarterly.head())


#Rename stocks column with Price
netflix_stocks.rename(columns={'Adj Close': 'Price'}, inplace=True)
dowjones_stocks.rename(columns={'Adj Close': 'Price'}, inplace=True)
netflix_stocks_quarterly.rename(columns={'Adj Close': 'Price'}, inplace=True)

print(netflix_stocks.head())
print(netflix_stocks_quarterly.head())
print(dowjones_stocks.head())


#make figure 1
plt.figure(1)
# palette = sns.color_palette("bright")
# sns.palplot(palette)

ax = sns.violinplot(data = netflix_stocks_quarterly, x='Quarter', y='Price')
ax.set_title('Distribution of 2017 Netflix Stock Prices by Quarter')
ax.set_ylabel('Closing Stock Price')
ax.set_xlabel('Business Quarters in 2017')
# plt.savefig("distribution.png")



plt.figure(2)
x_positions = [1, 2, 3, 4]
chart_labels = ["1Q2017","2Q2017","3Q2017","4Q2017"]
earnings_actual =[.4, .15,.29,.41]
earnings_estimate = [.37,.15,.32,.41 ]

plt.scatter(x_positions, earnings_actual, color='red', alpha=0.5)
plt.scatter(x_positions, earnings_estimate, color='blue', alpha=0.5)
plt.legend(["Actual", "Estimate"])
plt.xticks(x_positions, chart_labels)
plt.title('Quarterly earnings Per Share in Cents')
# plt.show()
# plt.savefig("earnings.png")




# The metrics below are in billions of dollars
revenue_by_quarter = [2.79, 2.98,3.29,3.7]
earnings_by_quarter = [.0656,.12959,.18552,.29012]
quarter_labels = ["2Q2017","3Q2017","4Q2017", "1Q2018"]

# Revenue
n = 1  # This is our first dataset (out of 2)
t = 2 # Number of dataset
d = 4 # Number of sets of bars
w = 0.8 # Width of each bar
bars1_x = [t*element + w*n for element
             in range(d)]



# Earnings
n = 2  # This is our second dataset (out of 2)
t = 2 # Number of dataset
d = 4 # Number of sets of bars
w = 0.8 # Width of each bar
bars2_x = [t*element + w*n for element
             in range(d)]

plt.figure(3)
plt.bar(bars1_x, revenue_by_quarter)
plt.bar(bars2_x, earnings_by_quarter)



middle_x = [ (a + b) / 2.0 for a, b in zip(bars1_x, bars2_x)]
labels = ["Revenue", "Earnings"]

plt.xticks(middle_x, quarter_labels)
plt.title('Netflix 2017 quarterly revenue and earnings')
plt.legend(labels)
# plt.show()
# plt.savefig("Netflixrevenue.png")

# ## Graph Literacy
# What are your first impressions looking at the visualized data?
# 
# - Does Revenue follow a trend?
# - Do Earnings follow a trend?
# - Roughly, what percentage of the revenue constitutes earnings?

# In[ ]:


# earnings graudally increasing, as a small percentage 10%? of revenue also increasing


# ## Step 8
# 
# In this last step, we will compare Netflix stock to the Dow Jones Industrial Average in 2017. We will accomplish this by plotting two line charts side by side in one figure. 
# 
# Since `Price` which is the most relevant data is in the Y axis, let's map our subplots to align vertically side by side.
# - We have set up the code for you on line 1 in the cell below. Complete the figure by passing the following arguments to `plt.subplots()` for the first plot, and tweaking the third argument for the second plot
#     - `1`-- the number of rows for the subplots
#     - `2` -- the number of columns for the subplots
#     - `1` -- the subplot you are modifying
# 
# - Chart the Netflix Stock Prices in the left-hand subplot. Using your data frame, access the `Date` and `Price` charts as the x and y axes respectively. Hint: (`netflix_stocks['Date'], netflix_stocks['Price']`)
# - Assign "Netflix" as a title to this subplot. Hint: `ax1.set_title()`
# - For each subplot, `set_xlabel` to `"Date"` and `set_ylabel` to `"Stock Price"`
# - Chart the Dow Jones Stock Prices in the left-hand subplot. Using your data frame, access the `Date` and `Price` charts as the x and y axes respectively. Hint: (`dowjones_stocks['Date'], dowjones_stocks['Price']`)
# - Assign "Dow Jones" as a title to this subplot. Hint: `plt.set_title()`
# - There is some crowding in the Y axis labels, add some space by calling `plt.subplots_adjust(wspace=.5)`
# - Be sure to `.show()` your plots.
# 

# In[91]:


plt.figure(figsize=(15,5))
l = len(netflix_stocks.Date)

xt = [element-1 for element in range(1,l+1)]
print(xt)


# Left plot Netflix
ax1 = plt.subplot(1, 2, 1)
plt.plot(netflix_stocks.Date, netflix_stocks.Price)
ax1.set_xlabel('Date')
ax1.set_ylabel('Stock Price')

plt.xticks(rotation=45)
ax1.set_title('Netflix')

# Right plot Dow Jones
# ax2 = plt.subplot(total number rows, total number columns, index of subplot to modify)

ax2 = plt.subplot(1, 2, 2)
plt.plot(dowjones_stocks.Date, dowjones_stocks.Price)
ax2.set_xlabel('Date')
ax2.set_ylabel('Stock Price')
plt.xticks(rotation=45)
ax2.set_title('Dow Jones')

plt.subplots_adjust(wspace=0.5)
plt.gcf().subplots_adjust(bottom=0.3)
# plt.show()
plt.savefig("netflixvsdowjones.png")



# - How did Netflix perform relative to Dow Jones Industrial Average in 2017?
# - Which was more volatile?
# - How do the prices of the stocks compare?

#  

# # Step 9
# 
# It's time to make your presentation! Save each of your visualizations as a png file with `plt.savefig("filename.png")`.
# 
# As you prepare your slides, think about the answers to the graph literacy questions. Embed your observations in the narrative of your slideshow!
# 
# Remember that your slideshow must include:
# - A title slide
# - A list of your visualizations and your role in their creation for the "Stock Profile" team
# - A visualization of the distribution of the stock prices for Netflix in 2017
# - A visualization and a summary of Netflix stock and revenue for the past four quarters and a summary
# - A visualization and a brief summary of their earned versus actual earnings per share
# - A visualization of Netflix stock against the Dow Jones stock (to get a sense of the market) in 2017
# 
