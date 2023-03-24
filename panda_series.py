{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "567508ab",
   "metadata": {},
   "source": [
    "# 1.\n",
    "Determine the number of elements in fruits."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "cbac09f0",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "dca39c0b",
   "metadata": {},
   "outputs": [],
   "source": [
    "fruits = [\"kiwi\", \"mango\", \"strawberry\", \"pineapple\", \"gala apple\", \"honeycrisp apple\", \n",
    " \"tomato\", \"watermelon\", \"honeydew\", \"kiwi\", \"kiwi\", \"kiwi\", \"mango\", \"blueberry\", \n",
    " \"blackberry\", \"gooseberry\", \"papaya\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "26bbe052",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "17"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(fruits)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5e4c9946",
   "metadata": {},
   "source": [
    "# 2.\n",
    "Output only the index from fruits."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "dd6f3160",
   "metadata": {},
   "outputs": [],
   "source": [
    "my_fruits = np.array(fruits)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "257b54bb",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['kiwi', 'mango', 'strawberry', 'pineapple', 'gala apple',\n",
       "       'honeycrisp apple', 'tomato', 'watermelon', 'honeydew', 'kiwi',\n",
       "       'kiwi', 'kiwi', 'mango', 'blueberry', 'blackberry', 'gooseberry',\n",
       "       'papaya'], dtype='<U16')"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "my_fruits"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "ef730904",
   "metadata": {},
   "outputs": [],
   "source": [
    "fruit_series = pd.Series(fruits)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "05595eeb",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0                 kiwi\n",
       "1                mango\n",
       "2           strawberry\n",
       "3            pineapple\n",
       "4           gala apple\n",
       "5     honeycrisp apple\n",
       "6               tomato\n",
       "7           watermelon\n",
       "8             honeydew\n",
       "9                 kiwi\n",
       "10                kiwi\n",
       "11                kiwi\n",
       "12               mango\n",
       "13           blueberry\n",
       "14          blackberry\n",
       "15          gooseberry\n",
       "16              papaya\n",
       "dtype: object"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "fruit_series"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "caf6ff05",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "list(fruit_series.index)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "37cb7beb",
   "metadata": {},
   "source": [
    "# 3.\n",
    "Output only the values from fruits."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "ab62fc23",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['kiwi', 'mango', 'strawberry', 'pineapple', 'gala apple',\n",
       "       'honeycrisp apple', 'tomato', 'watermelon', 'honeydew', 'kiwi',\n",
       "       'kiwi', 'kiwi', 'mango', 'blueberry', 'blackberry', 'gooseberry',\n",
       "       'papaya'], dtype=object)"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "fruit_series.values"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2a199626",
   "metadata": {},
   "source": [
    "# 4.\n",
    "Confirm the data type of the values in fruits."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "0dc5fa7a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "dtype('O')"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "fruit_series.dtype"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a939e703",
   "metadata": {},
   "source": [
    "# 5.\n",
    "Output only the first five values from fruits. Output the last three values. Output two random values from fruits."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "166fd103",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0          kiwi\n",
       "1         mango\n",
       "2    strawberry\n",
       "3     pineapple\n",
       "4    gala apple\n",
       "dtype: object"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "fruit_series.head(5)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a8b86c6a",
   "metadata": {},
   "source": [
    "# 6.\n",
    "Run the .describe() on fruits to see what information it returns when called on a Series with string values."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "a4532c01",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "count       17\n",
       "unique      13\n",
       "top       kiwi\n",
       "freq         4\n",
       "dtype: object"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "fruit_series.describe()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a9f3a9b4",
   "metadata": {},
   "source": [
    "# 7.\n",
    "Run the code necessary to produce only the unique string values from fruits."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "id": "16f8b5bc",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['kiwi', 'mango', 'strawberry', 'pineapple', 'gala apple',\n",
       "       'honeycrisp apple', 'tomato', 'watermelon', 'honeydew',\n",
       "       'blueberry', 'blackberry', 'gooseberry', 'papaya'], dtype=object)"
      ]
     },
     "execution_count": 48,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "fruit_series.unique()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "24043fcb",
   "metadata": {},
   "source": [
    "# 8.\n",
    "Determine how many times each unique string value occurs in fruits."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "e8edda0e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "kiwi                4\n",
       "mango               2\n",
       "strawberry          1\n",
       "pineapple           1\n",
       "gala apple          1\n",
       "honeycrisp apple    1\n",
       "tomato              1\n",
       "watermelon          1\n",
       "honeydew            1\n",
       "blueberry           1\n",
       "blackberry          1\n",
       "gooseberry          1\n",
       "papaya              1\n",
       "dtype: int64"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "fruit_series.value_counts()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "25b07925",
   "metadata": {},
   "source": [
    "# 9.\n",
    "Determine the string value that occurs most frequently in fruits."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "19fbc011",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "kiwi    4\n",
       "dtype: int64"
      ]
     },
     "execution_count": 46,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# print(fruit_series)\n",
    "# fruit_series.describe()\n",
    "fruit_series.value_counts().nlargest(1)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1c349032",
   "metadata": {},
   "source": [
    "# 10.\n",
    "Determine the string value that occurs least frequently in fruits."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "c736ef85",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "strawberry          1\n",
       "pineapple           1\n",
       "gala apple          1\n",
       "honeycrisp apple    1\n",
       "tomato              1\n",
       "watermelon          1\n",
       "honeydew            1\n",
       "blueberry           1\n",
       "blackberry          1\n",
       "gooseberry          1\n",
       "papaya              1\n",
       "dtype: int64"
      ]
     },
     "execution_count": 49,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "fruit_series.value_counts().nsmallest(keep='all')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0c6179c2",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
