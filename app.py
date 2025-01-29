{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "b9ccb802-ff36-496b-b93d-327ad4b6053e",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Import necessary libraries\n",
    "import streamlit as st\n",
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "50378a86-ad02-4d20-98eb-e8368eadf969",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Load the dataset\n",
    "df = pd.read_csv('Enhanced_Cleaned_updated_combined_data.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "f280386b-24c0-44ce-a320-28d58e1bb80d",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-01-29 19:28:16.509 WARNING streamlit.runtime.scriptrunner_utils.script_run_context: Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-29 19:28:22.249 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run C:\\Users\\user\\anaconda3\\Anaconda folder\\Lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n",
      "2025-01-29 19:28:22.256 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "DeltaGenerator()"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Set up the Streamlit app layout\n",
    "st.title('Data Insights Dashboard')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "bf8392e0-6b00-4963-88fe-c3fd8c0f4964",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-01-29 19:28:35.498 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-29 19:28:35.507 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-29 19:28:35.517 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-29 19:28:35.518 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-29 19:28:36.409 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-29 19:28:36.438 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "DeltaGenerator()"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Display the dataframe\n",
    "st.write('### Data Overview')\n",
    "st.dataframe(df.head())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "8aeae803-654e-4904-918a-478a69e822a7",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-01-29 19:28:50.135 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-29 19:28:50.142 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-29 19:28:50.144 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-29 19:28:50.171 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-29 19:28:50.178 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    }
   ],
   "source": [
    "# Add a slider for filtering data based on a specific column (e.g., Maths scores)\n",
    "maths_score = st.slider('Select Maths Score', min_value=int(df['Maths'].min()), max_value=int(df['Maths'].max()), value=(60, 100))\n",
    "filtered_data = df[(df['Maths'] >= maths_score[0]) & (df['Maths'] <= maths_score[1])]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "bd3af7af-f326-4dc3-a78a-493005153d53",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-01-29 19:29:08.130 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-29 19:29:08.134 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-29 19:29:08.143 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-29 19:29:08.148 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-29 19:29:09.197 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-29 19:29:09.199 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    }
   ],
   "source": [
    "# Display filtered data\n",
    "st.write('### Filtered Data', filtered_data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "3fabae10-bcd7-4d34-8baf-1d6a143d94b5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "({66.0: 9,\n",
       "  61.333333333333336: 9,\n",
       "  73.0: 9,\n",
       "  71.0: 9,\n",
       "  69.0: 9,\n",
       "  77.33333333333333: 8,\n",
       "  68.0: 8,\n",
       "  70.0: 8,\n",
       "  64.33333333333333: 8,\n",
       "  68.66666666666667: 7,\n",
       "  67.0: 7,\n",
       "  75.66666666666667: 7,\n",
       "  83.0: 7,\n",
       "  84.0: 7,\n",
       "  73.33333333333333: 7,\n",
       "  74.33333333333333: 7,\n",
       "  64.66666666666667: 7,\n",
       "  65.66666666666667: 7,\n",
       "  54.66666666666666: 6,\n",
       "  56.0: 6,\n",
       "  79.33333333333333: 6,\n",
       "  78.0: 6,\n",
       "  60.333333333333336: 6,\n",
       "  60.0: 6,\n",
       "  68.33333333333333: 6,\n",
       "  70.33333333333333: 6,\n",
       "  74.66666666666667: 6,\n",
       "  52.66666666666666: 6,\n",
       "  75.33333333333333: 6,\n",
       "  71.33333333333333: 6,\n",
       "  59.0: 6,\n",
       "  82.33333333333333: 6,\n",
       "  72.66666666666667: 6,\n",
       "  65.33333333333333: 6,\n",
       "  75.0: 5,\n",
       "  58.66666666666666: 5,\n",
       "  80.33333333333333: 5,\n",
       "  67.33333333333333: 5,\n",
       "  51.0: 5,\n",
       "  85.66666666666667: 5,\n",
       "  77.0: 5,\n",
       "  78.66666666666667: 5,\n",
       "  58.333333333333336: 5,\n",
       "  51.66666666666666: 5,\n",
       "  55.66666666666666: 5,\n",
       "  63.0: 5,\n",
       "  63.66666666666666: 5,\n",
       "  55.333333333333336: 5,\n",
       "  61.66666666666666: 5,\n",
       "  76.0: 5,\n",
       "  54.0: 4,\n",
       "  61.0: 4,\n",
       "  63.333333333333336: 4,\n",
       "  89.0: 4,\n",
       "  80.66666666666667: 4,\n",
       "  50.0: 4,\n",
       "  62.333333333333336: 4,\n",
       "  71.66666666666667: 4,\n",
       "  69.33333333333333: 4,\n",
       "  60.66666666666666: 4,\n",
       "  59.333333333333336: 4,\n",
       "  64.0: 4,\n",
       "  65.0: 4,\n",
       "  62.0: 4,\n",
       "  86.33333333333333: 4,\n",
       "  57.333333333333336: 4,\n",
       "  79.66666666666667: 4,\n",
       "  81.66666666666667: 4,\n",
       "  59.66666666666666: 4,\n",
       "  53.66666666666666: 4,\n",
       "  77.66666666666667: 3,\n",
       "  74.0: 3,\n",
       "  83.33333333333333: 3,\n",
       "  57.66666666666666: 3,\n",
       "  48.66666666666666: 3,\n",
       "  84.66666666666667: 3,\n",
       "  66.66666666666667: 3,\n",
       "  46.333333333333336: 3,\n",
       "  56.333333333333336: 3,\n",
       "  78.33333333333333: 3,\n",
       "  72.33333333333333: 3,\n",
       "  56.66666666666666: 3,\n",
       "  49.333333333333336: 3,\n",
       "  50.333333333333336: 3,\n",
       "  69.66666666666667: 3,\n",
       "  87.33333333333333: 3,\n",
       "  86.0: 3,\n",
       "  70.66666666666667: 3,\n",
       "  82.0: 3,\n",
       "  76.33333333333333: 3,\n",
       "  88.33333333333333: 3,\n",
       "  52.333333333333336: 3,\n",
       "  82.66666666666667: 3,\n",
       "  85.0: 3,\n",
       "  51.333333333333336: 3,\n",
       "  94.0: 3,\n",
       "  57.0: 3,\n",
       "  100.0: 3,\n",
       "  46.66666666666666: 3,\n",
       "  79.0: 3,\n",
       "  49.0: 3,\n",
       "  39.66666666666666: 2,\n",
       "  81.33333333333333: 2,\n",
       "  52.0: 2,\n",
       "  67.66666666666667: 2,\n",
       "  29.666666666666668: 2,\n",
       "  48.0: 2,\n",
       "  54.333333333333336: 2,\n",
       "  43.333333333333336: 2,\n",
       "  80.0: 2,\n",
       "  50.66666666666666: 2,\n",
       "  40.66666666666666: 2,\n",
       "  97.0: 2,\n",
       "  92.0: 2,\n",
       "  53.333333333333336: 2,\n",
       "  86.66666666666667: 2,\n",
       "  96.33333333333331: 2,\n",
       "  44.66666666666666: 2,\n",
       "  87.66666666666667: 2,\n",
       "  72.0: 2,\n",
       "  55.0: 2,\n",
       "  91.33333333333331: 2,\n",
       "  44.333333333333336: 1,\n",
       "  97.66666666666669: 1,\n",
       "  30.666666666666668: 1,\n",
       "  47.66666666666666: 1,\n",
       "  93.66666666666669: 1,\n",
       "  34.333333333333336: 1,\n",
       "  88.66666666666667: 1,\n",
       "  96.66666666666669: 1,\n",
       "  42.333333333333336: 1,\n",
       "  66.33333333333333: 1,\n",
       "  45.66666666666666: 1,\n",
       "  85.33333333333333: 1,\n",
       "  43.0: 1,\n",
       "  47.333333333333336: 1,\n",
       "  53.0: 1,\n",
       "  39.333333333333336: 1,\n",
       "  81.0: 1,\n",
       "  76.66666666666667: 1,\n",
       "  62.66666666666666: 1,\n",
       "  48.333333333333336: 1,\n",
       "  43.66666666666666: 1,\n",
       "  91.0: 1,\n",
       "  90.33333333333331: 1,\n",
       "  39.0: 1,\n",
       "  46.0: 1,\n",
       "  45.333333333333336: 1,\n",
       "  23.0: 1,\n",
       "  29.33333333333333: 1,\n",
       "  91.66666666666669: 1,\n",
       "  89.33333333333333: 1,\n",
       "  89.66666666666667: 1,\n",
       "  44.0: 1,\n",
       "  40.0: 1,\n",
       "  58.0: 1,\n",
       "  31.0: 1,\n",
       "  84.33333333333333: 1,\n",
       "  9.0: 1,\n",
       "  37.333333333333336: 1,\n",
       "  26.0: 1,\n",
       "  38.333333333333336: 1,\n",
       "  32.333333333333336: 1,\n",
       "  73.66666666666667: 1,\n",
       "  31.33333333333333: 1,\n",
       "  99.0: 1,\n",
       "  83.66666666666667: 1},\n",
       " {'Learn More: Go to About the NHES': 64,\n",
       "  'This First Look report introduces new National Household Education Survey (NHES) survey data that presents findings from the Parent and Family Involvement in Education Survey of the National Household Education Surveys Program of 2023 (PFI-NHES:2023).': 64,\n",
       "  'This report presents data about various aspects of parent involvement in education and reasons for choosing the child’s school. These data represent circumstances before the implementation of coronavirus pandemic restrictions.': 64,\n",
       "  'NCES Annual Reports': 64,\n",
       "  'The NCES Annual Reports and Information program produces several reports each year that draw from over 25 surveys by NCES and other government agencies. Many of these reports include information on enrollment in public charter schools and private schools. The Digest of Education Statistics includes additional information on school choice and parent involvement.': 64,\n",
       "  'Longitudinal Studies': 64,\n",
       "  'State Education Practices (School Choice)': 64,\n",
       "  'Parent Involvement Toolkit': 64,\n",
       "  'Back to Top ': 64})"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Analyzing overall performance categories and parental involvement insights\n",
    "performance_counts = df['Overall Performance'].value_counts()\n",
    "parental_involvement_counts = df['Parental Involvement Insights'].value_counts()\n",
    "\n",
    "# Creating a summary of the counts for overall performance and parental involvement\n",
    "performance_summary = performance_counts.to_dict()\n",
    "parental_involvement_summary = parental_involvement_counts.to_dict()\n",
    "\n",
    "performance_summary, parental_involvement_summary"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "443dc128-94da-455e-a49a-a633536f9345",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-01-29 19:29:28.966 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-29 19:29:28.973 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-29 19:29:28.981 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-29 19:29:28.983 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-29 19:29:30.521 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-29 19:29:34.386 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-29 19:29:34.394 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "DeltaGenerator()"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Create a simple plot\n",
    "st.write('### Maths Score Distribution')\n",
    "plt.figure(figsize=(10, 5))\n",
    "plt.hist(df['Maths'], bins=20, color='blue', alpha=0.7)\n",
    "plt.title('Distribution of Maths Scores')\n",
    "plt.xlabel('Scores')\n",
    "plt.ylabel('Frequency')\n",
    "\n",
    "# Display the plot in Streamlit\n",
    "st.pyplot(plt)"
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
   "version": "3.12.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
