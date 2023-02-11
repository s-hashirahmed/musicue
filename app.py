import streamlit as st

import requests as req

st.title("Musciue: A Music Streaming Platform")

opt = st.text_input("Search Song", "Perfect")

if opt:
    res = req.get(f"https://saavn.me/search/songs?query={opt}").json()['data']['results']

    if st.button("Find"):
        x = list(map(lambda x: [x['name'],x['image'][2]['link'], x['downloadUrl'], x['primaryArtists'], x['label']], res))
        for i in range(len(x)):
            col1, col2, col3 = st.columns(3)
            try:

                with col1:
                    st.image(x[i][1])
                    st.header(x[i][0])
                    st.caption(x[i][3])
                    st.caption(x[i][4])

                    st.audio(x[i][2][4]['link'])

                    if i == (len(x)-2): break

                with col2:
                    st.image(x[i+2][1])
                    st.header(x[i+2][0])
                    st.caption(x[i+2][3])
                    st.caption(x[i+2][4])
                    st.audio(x[i+2][2][4]['link'])
            except(TypeError):
                pass



