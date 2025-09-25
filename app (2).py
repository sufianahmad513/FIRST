{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "3e25adc9-9922-4880-82a9-9b9f308989ee",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "import pandas as pd\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "aae592a1-44b6-4508-b231-1f2415e5711f",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-09-25 22:02:58.973 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-09-25 22:02:58.974 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-09-25 22:02:58.975 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-09-25 22:02:58.976 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-09-25 22:02:58.977 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-09-25 22:02:58.978 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-09-25 22:02:58.979 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-09-25 22:02:58.980 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-09-25 22:02:58.981 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-09-25 22:02:58.982 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-09-25 22:03:00.499 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-09-25 22:03:00.500 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-09-25 22:03:00.501 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-09-25 22:03:00.502 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-09-25 22:03:00.505 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-09-25 22:03:00.506 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "DeltaGenerator()"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "st.set_page_config(page_title=\"Hello Streamlit\", layout=\"wide\")\n",
    "st.title(\"Hello, Streamlit \")\n",
    "st.write(\"Turn notebooks into shareable apps in minutes.\")\n",
    "# A tiny dataset\n",
    "sales = pd.DataFrame({\n",
    "\"month\": [\"Jan\",\"Feb\",\"Mar\",\"Apr\"],\n",
    "\"revenue\": [120, 150, 130, 180]\n",
    "})\n",
    "# Widget + computed view\n",
    "threshold = st.slider(\"Highlight revenue above\", 100, 200, 140)\n",
    "st.bar_chart(sales.set_index(\"month\"))\n",
    "st.write(\"Rows above threshold:\")\n",
    "st.dataframe(sales[sales.revenue > threshold])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4872f9d6-6f8e-4c79-ab3d-4fd0000e9688",
   "metadata": {},
   "outputs": [],
   "source": [
    "!streamlit run app.py "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "28a5d49a-af66-4146-b1f7-2b8da7b3ec50",
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
   "version": "3.13.5"
  },
  "widgets": {
   "application/vnd.jupyter.widget-state+json": {
    "state": {},
    "version_major": 2,
    "version_minor": 0
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
