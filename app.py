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
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "34ee2b12-dbaf-440e-882e-700b8d7518e2",
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
   "version": "3.12.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
