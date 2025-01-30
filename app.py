{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "d6025f1e-e5d4-4903-9c47-6e9e5acce499",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import streamlit as st\n",
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "9529e7e6-a623-48e5-85a7-71d1ac295a01",
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.read_csv('Enhanced_Cleaned_updated_combined_data.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "bcbf9204-e1f1-44b0-aba0-16c143dd8dda",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-01-30 12:16:22.302 WARNING streamlit.runtime.scriptrunner_utils.script_run_context: Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-30 12:16:25.754 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run C:\\Users\\user\\anaconda3\\Anaconda folder\\Lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n",
      "2025-01-30 12:16:25.756 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-30 12:16:25.760 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-30 12:16:25.762 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-30 12:16:25.765 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-30 12:16:25.766 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    }
   ],
   "source": [
    "st.title('Student Performance Dashboard')\n",
    "st.write('Explore key insights from the student performance dataset.')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "4d9fbc1f-b431-440f-8ca1-6a5f1282a1c4",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-01-30 12:16:36.368 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-30 12:16:36.424 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-30 12:16:36.465 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-30 12:16:36.522 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-30 12:16:36.523 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    }
   ],
   "source": [
    "if st.checkbox('Show raw data'):\n",
    "    st.write(df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "a8159591-9349-40fa-89a8-7a355a0a14b4",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-01-30 12:16:56.748 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-30 12:16:56.750 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-30 12:16:56.901 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-30 12:16:56.934 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-30 12:16:56.935 Session state does not function when running a script without `streamlit run`\n",
      "2025-01-30 12:16:57.012 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-30 12:16:57.016 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-30 12:16:57.684 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-30 12:16:57.687 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    }
   ],
   "source": [
    "performance_category = st.selectbox('Select Performance Category', df['Performance Category'].unique())\n",
    "filtered_df = df[df['Performance Category'] == performance_category]\n",
    "st.write(filtered_df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "13dac98e-51db-4226-a67d-d7151ec3af09",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-01-30 12:17:12.598 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-30 12:17:12.605 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-30 12:17:12.698 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-30 12:17:12.700 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-30 12:17:12.704 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-30 12:17:12.883 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-30 12:17:13.194 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-30 12:17:13.196 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    }
   ],
   "source": [
    "sleep_time = st.slider('Select Sleep Time', min_value=int(df['Sleep Time'].min()), max_value=int(df['Sleep Time'].max()))\n",
    "filtered_df = df[df['Sleep Time'] == sleep_time]\n",
    "st.write(filtered_df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "9393fda6-176f-4e36-9633-4d22fb3c6cfc",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-01-30 12:17:30.386 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-30 12:17:30.392 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-30 12:17:32.566 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-30 12:17:34.512 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-30 12:17:34.514 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
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
    "st.subheader('Performance Category Distribution')\n",
    "fig, ax = plt.subplots()\n",
    "sns.countplot(x='Performance Category', data=df, ax=ax)\n",
    "st.pyplot(fig)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "63e8452a-5429-4ca3-b387-b1e488b1c37e",
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
