import pandas as pd
import h5py
import numpy as np
import plotly.express as px


# read data out of h5py file and create visualization
# get overview of groups and items in groups
with h5py.File('collected_data.h5', 'r') as hdf:

    base_items = list(hdf.items())
    grp_corona = hdf.get("coronavirus")
    grp_corona_items = list(grp_corona.items())
    grp_art = hdf.get("english_articles")
    grp_art_items = list(grp_art.items())
    grp_btc = hdf.get("bitcoin")
    grp_btc_items = list(grp_btc.items())

    # retrieve datasets and visualize content

    # CORONANVIRUS
    # get each dataset
    corona_insert_datetime = hdf.get("coronavirus/insert_datetime")
    corona_total_cases = hdf.get("coronavirus/total_cases")
    corona_deaths = hdf.get("coronavirus/deaths")
    corona_recovered = hdf.get("coronavirus/recovered")

    # read datasets into arrays
    corona_insert_datetime = np.array(corona_insert_datetime)
    corona_insert_datetime = corona_insert_datetime.astype('datetime64', copy=False)
    corona_total_cases = np.array(corona_total_cases)
    corona_deaths = np.array(corona_deaths)
    corona_recovered = np.array(corona_recovered)

    # read arrays into pandas dataframe
    cor_df_1 = pd.DataFrame(corona_insert_datetime, columns=['insert_datetime'])
    cor_df_2 = pd.DataFrame(corona_total_cases, columns=['Amount of cases'])
    cor_df_3 = pd.DataFrame(corona_deaths, columns=['Deaths'])
    cor_df_4 = pd.DataFrame(corona_recovered, columns=['Recovered'])
    cor_df = pd.concat([cor_df_1, cor_df_2, cor_df_3, cor_df_4], axis=1, join="inner")

    print('COVID-19 DATA')
    print(cor_df.to_markdown())
    print(' ')

    # ENGLISH ARTICLES
    # get each dataset
    art_articles = hdf.get("english_articles/amount_of_articles")
    art_words = hdf.get("english_articles/words_per_article")
    art_insert_datetime = hdf.get("english_articles/insert_datetime")

    # read datasets into arrays
    art_articles = np.array(art_articles)
    art_words = np.array(art_words)
    art_insert_datetime = np.array(art_insert_datetime)
    art_insert_datetime = art_insert_datetime.astype('datetime64', copy=False)

    # read arrays into pandas dataframe
    art_df_1 = pd.DataFrame(art_insert_datetime, columns=['insert_datetime'])
    art_df_2 = pd.DataFrame(art_articles, columns=['Amount of articles'])
    art_df_3 = pd.DataFrame(art_words, columns=['Words per article'])
    art_df = pd.concat([art_df_1, art_df_2, art_df_3], axis=1, join="inner")

    print('WIKIPEDIA ARTICLES IN ENGLISH')
    print(art_df.to_markdown())
    print(' ')

    # BITCOIN
    # get each dataset
    btc_price = hdf.get("bitcoin/price")
    btc_insert_datetime = hdf.get("bitcoin/insert_datetime")

    # read datasets into arrays
    btc_price = np.array(btc_price)
    btc_insert_datetime = np.array(btc_insert_datetime)
    btc_insert_datetime = btc_insert_datetime.astype('datetime64', copy=False)

    btc_df_1 = pd.DataFrame(btc_insert_datetime, columns=['insert_datetime'])
    btc_df_2 = pd.DataFrame(btc_price, columns=['price in $'])

    btc_df = pd.concat([btc_df_1, btc_df_2], axis=1, join="inner")

    print('BITCOIN PRICES')
    print(btc_df.to_markdown())

    bitcoin_fig_temp = px.line(x=btc_df['insert_datetime'], y=btc_df['price in $'],
                              title='Bitcoin prices')
    bitcoin_fig_temp.update_layout(title_x=0.5,
                                plot_bgcolor='#f6f6f6',
                                yaxis_title='Price',
                                xaxis_title='insert datetime')
    bitcoin_fig_temp.update_traces(line_color="#0096FF", line_width=3)
    bitcoin_fig_temp.show()

