{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>age</th>\n",
       "      <th>gender</th>\n",
       "      <th>occupation</th>\n",
       "      <th>zip_code</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>user_id</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>24</td>\n",
       "      <td>M</td>\n",
       "      <td>technician</td>\n",
       "      <td>85711</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>53</td>\n",
       "      <td>F</td>\n",
       "      <td>other</td>\n",
       "      <td>94043</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>23</td>\n",
       "      <td>M</td>\n",
       "      <td>writer</td>\n",
       "      <td>32067</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>24</td>\n",
       "      <td>M</td>\n",
       "      <td>technician</td>\n",
       "      <td>43537</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>33</td>\n",
       "      <td>F</td>\n",
       "      <td>other</td>\n",
       "      <td>15213</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "         age gender  occupation zip_code\n",
       "user_id                                 \n",
       "1         24      M  technician    85711\n",
       "2         53      F       other    94043\n",
       "3         23      M      writer    32067\n",
       "4         24      M  technician    43537\n",
       "5         33      F       other    15213"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import pandas as pd\n",
    "url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user'\n",
    "df = pd.read_csv(url, index_col = 'user_id', sep = '|')\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "------------first 10 entries------------\n",
      "          age gender     occupation zip_code\n",
      "user_id                                    \n",
      "1         24      M     technician    85711\n",
      "2         53      F          other    94043\n",
      "3         23      M         writer    32067\n",
      "4         24      M     technician    43537\n",
      "5         33      F          other    15213\n",
      "6         42      M      executive    98101\n",
      "7         57      M  administrator    91344\n",
      "8         36      M  administrator    05201\n",
      "9         29      M        student    01002\n",
      "10        53      M         lawyer    90703 \n",
      "------------last 10 entries------------\n",
      "          age gender     occupation zip_code\n",
      "user_id                                    \n",
      "934       61      M       engineer    22902\n",
      "935       42      M         doctor    66221\n",
      "936       24      M          other    32789\n",
      "937       48      M       educator    98072\n",
      "938       38      F     technician    55038\n",
      "939       26      F        student    33319\n",
      "940       32      M  administrator    02215\n",
      "941       20      M        student    97229\n",
      "942       48      F      librarian    78209\n",
      "943       22      M        student    77841\n"
     ]
    }
   ],
   "source": [
    "# See the first 10 and last 10 entries\n",
    "print('------------first 10 entries------------\\n',df.head(10),'\\n------------last 10 entries------------\\n',df.tail(10))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Number of Observations : 943\n"
     ]
    }
   ],
   "source": [
    "# What is the number of observations in the dataset?\n",
    "obs = df.shape[0]\n",
    "print('Number of Observations :', obs)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Number of columns : 4\n"
     ]
    }
   ],
   "source": [
    "# What is the number of columns in the dataset?\n",
    "ncol = df.shape[1]\n",
    "print('Number of columns :', ncol) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Index(['age', 'gender', 'occupation', 'zip_code'], dtype='object')\n"
     ]
    }
   ],
   "source": [
    "# Print the name of all the columns.\n",
    "print(df.columns)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Int64Index([  1,   2,   3,   4,   5,   6,   7,   8,   9,  10,\n",
      "            ...\n",
      "            934, 935, 936, 937, 938, 939, 940, 941, 942, 943],\n",
      "           dtype='int64', name='user_id', length=943)\n"
     ]
    }
   ],
   "source": [
    "# How is the dataset indexed?\n",
    "indexed = df.index\n",
    "print(indexed)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "age            int64\n",
      "gender        object\n",
      "occupation    object\n",
      "zip_code      object\n",
      "dtype: object\n"
     ]
    }
   ],
   "source": [
    "# What is the data type of each column?\n",
    "print(df.dtypes)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "user_id\n",
      "1         technician\n",
      "2              other\n",
      "3             writer\n",
      "4         technician\n",
      "5              other\n",
      "           ...      \n",
      "939          student\n",
      "940    administrator\n",
      "941          student\n",
      "942        librarian\n",
      "943          student\n",
      "Name: occupation, Length: 943, dtype: object\n"
     ]
    }
   ],
   "source": [
    "# Print only the occupation column\n",
    "print(df['occupation'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "21\n"
     ]
    }
   ],
   "source": [
    "# How many different occupations are in this dataset?\n",
    "print(df['occupation'].nunique())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "21\n"
     ]
    }
   ],
   "source": [
    "# How many different occupations are in this dataset?\n",
    "print(df['occupation'].value_counts().count())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0    student\n",
      "Name: occupation, dtype: object\n"
     ]
    }
   ],
   "source": [
    "# What is the most frequent occupation?\n",
    "print(df['occupation'].mode())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "student          196\n",
      "other            105\n",
      "educator          95\n",
      "administrator     79\n",
      "engineer          67\n",
      "Name: occupation, dtype: int64\n"
     ]
    }
   ],
   "source": [
    "# What is the most frequent occupation?\n",
    "print(df['occupation'].value_counts().sort_values(ascending=False).head())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "Int64Index: 943 entries, 1 to 943\n",
      "Data columns (total 4 columns):\n",
      " #   Column      Non-Null Count  Dtype \n",
      "---  ------      --------------  ----- \n",
      " 0   age         943 non-null    int64 \n",
      " 1   gender      943 non-null    object\n",
      " 2   occupation  943 non-null    object\n",
      " 3   zip_code    943 non-null    object\n",
      "dtypes: int64(1), object(3)\n",
      "memory usage: 36.8+ KB\n",
      "None\n"
     ]
    }
   ],
   "source": [
    "# DataFrame Info.\n",
    "print(df.info())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "               age gender occupation zip_code\n",
      "count   943.000000    943        943      943\n",
      "unique         NaN      2         21      795\n",
      "top            NaN      M    student    55414\n",
      "freq           NaN    670        196        9\n",
      "mean     34.051962    NaN        NaN      NaN\n",
      "std      12.192740    NaN        NaN      NaN\n",
      "min       7.000000    NaN        NaN      NaN\n",
      "25%      25.000000    NaN        NaN      NaN\n",
      "50%      31.000000    NaN        NaN      NaN\n",
      "75%      43.000000    NaN        NaN      NaN\n",
      "max      73.000000    NaN        NaN      NaN\n"
     ]
    }
   ],
   "source": [
    "# Describe all the columns\n",
    "print(df.describe(include='all'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "count         943\n",
      "unique         21\n",
      "top       student\n",
      "freq          196\n",
      "Name: occupation, dtype: object\n"
     ]
    }
   ],
   "source": [
    "# Summarize only the occupation column\n",
    "print(df['occupation'].describe())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "34.05196182396607\n"
     ]
    }
   ],
   "source": [
    "# What is the mean age of users?\n",
    "print(df['age'].mean())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "73    1\n",
      "Name: age, dtype: int64\n"
     ]
    }
   ],
   "source": [
    "# What is the age with least occurrence?\n",
    "print(df['age'].value_counts().tail(1))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [],
   "source": [
    "# What is the age with least occurrence?\n",
    "print(df['age'].min())"
   ]
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
   "version": "3.9.12"
  },
  "vscode": {
   "interpreter": {
    "hash": "a135a2979dcc31b13684e0092fc272a0229e357331cfbb7d4f1db7898b97e5e4"
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
