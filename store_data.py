import numpy as np
import corona
import articles
import bitcoin
import h5py

# write new hdf5 file and load with data
try:
    filename_hdf = 'collected_data.h5'
    with h5py.File(filename_hdf, 'a') as hdf:
        dt = h5py.special_dtype(vlen=str)

        # CORONAVIRUS
        # create group
        # set attributes/metadata for group
        grp_corona = hdf.create_group("coronavirus")

        grp_corona.attrs['SOURCE'] = 'Data collected from the website: ' \
                                     'https://www.worldometers.info/coronavirus/'
        grp_corona.attrs['DATA COLLECTION'] = 'Data collected through web scraping from Aug 24, 2023. '

        # create datasets

        # cor = np.array([corona.corona_data], dtype=dt)
        corona_datetime = np.array([corona.insert_datetime], dtype=dt)

        corona_insert_datetime = grp_corona.create_dataset("insert_datetime", (1,), data=corona_datetime,
                                                           maxshape=(None,))
        corona_total_cases = grp_corona.create_dataset("total_cases", (1,), data=corona.total_cases, maxshape=(None,))
        corona_deaths = grp_corona.create_dataset("deaths", (1,), data=corona.deaths, maxshape=(None,))
        corona_recovered = grp_corona.create_dataset("recovered", (1,), data=corona.recovered, maxshape=(None,))

        # ARTICLES
        # create group
        # set attributes/metadata for group
        grp_art = hdf.create_group("english_articles")

        grp_art.attrs['SOURCE'] = 'Data on temperature was collected from the website: ' \
                                  'https://wikicount.net/'
        grp_art.attrs['DATA COLLECTION'] = 'Data collected through web scraping from Aug 24, 2023. '

        # create datasets for groups
        art_datetime = np.array([articles.insert_datetime], dtype=dt)
        art_insert_datetime = grp_art.create_dataset("insert_datetime", (1,), data=art_datetime, maxshape=(None,))
        art_amount = grp_art.create_dataset("amount_of_articles", (1,), data=articles.articles, maxshape=(None,))
        art_words = grp_art.create_dataset("words_per_article", (1,), data=articles.words, maxshape=(None,))

        # BITCOIN
        # create group

        # set attributes/metadata for group
        grp_bitcoin = hdf.create_group("bitcoin")

        grp_bitcoin.attrs['SOURCE'] = 'Data on temperature was collected from the website: ' \
                                      'https://coinmarketcap.com/currencies/bitcoin/'
        grp_bitcoin.attrs['DATA COLLECTION'] = 'Data collected through web scraping from Aug 24, 2023. '

        # create datasets for groups
        btc_datetime = np.array([bitcoin.insert_datetime], dtype=dt)
        btc_insert_datetime = grp_bitcoin.create_dataset("insert_datetime", (1,), data=btc_datetime, maxshape=(None,))
        btc_price = grp_bitcoin.create_dataset("price", (1,), data=bitcoin.price, maxshape=(None,))


except FileExistsError and ValueError:
    filename_hdf = 'collected_data.h5'
    with h5py.File(filename_hdf, 'r+') as hdf:
        dt = h5py.special_dtype(vlen=str)

        # CORONAVIRUS
        # get datasets
        corona_deaths = hdf.get("coronavirus/deaths")
        corona_recovered = hdf.get("coronavirus/recovered")
        corona_insert_datetime = hdf.get("coronavirus/insert_datetime")
        corona_total_cases = hdf.get("coronavirus/total_cases")

        # add new values to datasets
        corona_datetime = np.array([corona.insert_datetime], dtype=dt)

        corona_insert_datetime.resize(corona_insert_datetime.shape[0] + 1, axis=0)
        corona_insert_datetime[-1:, ] = corona_datetime

        corona_total_cases.resize(corona_total_cases.shape[0] + 1, axis=0)
        corona_total_cases[-1:, ] = corona.total_cases

        corona_deaths.resize(corona_deaths.shape[0] + 1, axis=0)
        corona_deaths[-1:, ] = corona.deaths

        corona_recovered.resize(corona_recovered.shape[0] + 1, axis=0)
        corona_recovered[-1:, ] = corona.recovered

        # ARTICLES
        # get datasets
        art_amount = hdf.get("english_articles/amount_of_articles")
        art_words = hdf.get("english_articles/words_per_article")
        art_insert_datetime = hdf.get("english_articles/insert_datetime")

        # add new values to datasets
        art_datetime = np.array([articles.insert_datetime], dtype=dt)

        art_insert_datetime.resize(art_insert_datetime.shape[0] + 1, axis=0)
        art_insert_datetime[-1:, ] = art_datetime

        art_amount.resize(art_amount.shape[0] + 1, axis=0)
        art_amount[-1:, ] = articles.articles

        art_words.resize(art_words.shape[0] + 1, axis=0)
        art_words[-1:, ] = articles.words

        # BITCOIN
        # get datasets
        btc_price = hdf.get("bitcoin/price")
        btc_insert_datetime = hdf.get("bitcoin/insert_datetime")

        # add new values to datasets
        btc_datetime = np.array([bitcoin.insert_datetime], dtype=dt)

        btc_insert_datetime.resize(btc_insert_datetime.shape[0] + 1, axis=0)
        btc_insert_datetime[-1:, ] = btc_datetime

        btc_price.resize(btc_price.shape[0] + 1, axis=0)
        btc_price[-1:, ] = bitcoin.price
