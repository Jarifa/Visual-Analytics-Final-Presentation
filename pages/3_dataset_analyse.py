#######packages

import pandas as pd
import numpy as np
import missingno as msno


##########Code voor regression
###################################################################################################################
def add_bg_from_url():
    st.markdown(
        f"""
         <style>
         .stApp {{
             background-image: url("https://th.bing.com/th/id/R.c6d89244cbb1c6d916e87acd4984c09e?rik=5PX6aQALkMW6vg&riu=http%3a%2f%2fimg06.deviantart.net%2fca80%2fi%2f2014%2f196%2fb%2f1%2fminimal_new_york_by_kevichan-d61zr27.jpg&ehk=k9sZxjAJ%2blmBlAiGwtw0kJmHNRzbU4GLxez%2f42eOMo4%3d&risl=&pid=ImgRaw&r=0");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
        unsafe_allow_html=True
    )


add_bg_from_url()
#######################################################################################################################

data = df.to_csv('clean_df.csv')