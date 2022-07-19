# starting with pands
import pandas
# dataFrame with data, column name and row names
df1 = pandas.DataFrame([[2, 4, 6], [4, 8, 12], [8, 16, 24]], columns=[
                       "Price", "Age", "Volume"], index=["First", "Second", "Third"])

print(df1)

# accessing individual data fram
print(df1.Price)

# work on individual column data
print("Max ", df1.Price.max())
print("Mean ", df1.Price.mean())

# DataFrame key value of dictionary
df2 = pandas.DataFrame(
    [{"Name": "John", "age": 12}, {"Name": "Cena", "age": 16}])
print(df2)
