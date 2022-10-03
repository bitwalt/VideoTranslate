from re import A
import streamlit as st
import asyncio
from aiohttp.client import ClientSession
from pylnbits.config import Config
from pylnbits.user_wallet import UserWallet
from utils import get_btc_price, get_dollar_sat, dollar_to_sat
import qrcode
import io
import requests
import os
import pandas as pd 

c = Config(config_file="config.yml")
csv_file = './historycal_btc_price.csv'

daily_price = lambda df: df[['day', 'price_btc']].set_index('day')


def create_qr_image(bolt11: str):
    qr = qrcode.QRCode()
    qr.add_data(bolt11)
    qr.make()
    img = qr.make_image()
    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format='JPEG')
    img_byte_arr = img_byte_arr.getvalue()
    return img_byte_arr 

def get_dollar_sats_data(daily_price):
    daily_price['sat_price'] = daily_price['price_btc'].apply(lambda d: dollar_to_sat(d))
    return daily_price['sat_price']
       

def download_data(csv_file):
    """Downloads data from bitcoinvisuals.com"""
    st.write("Downloading data from bitcoinvisuals.com")
    req = requests.get("https://bitcoinvisuals.com/static/data/data_daily.csv")
    url_content = req.content
    with open(csv_file, 'wb') as csv_file:
        csv_file.write(url_content)
    st.write("Download complete")
    
def get_historical_data(csv_file):
    if not os.path.exists(csv_file):
        download_data(csv_file)
    df = pd.read_csv(csv_file).fillna(0)
    filter_df = df[df['price_btc'] > 0 ]
    return filter_df


async def main():
    st.set_page_config(page_title="LN WALLET API", page_icon="🤖")
    st.title("LNBITs Invoicer")
    
    historical_data = get_historical_data(csv_file)
    # st.write(historical_data)
    
    btc_price = get_btc_price()
    dollar_sat = get_dollar_sat(btc_price)
    col1, col2 = st.columns(2)
    col1.metric(label='BTC price', value=f"{btc_price} $")
    
    # daily_data = daily_price(historical_data)
    # col1.line_chart(daily_data)
    # col2.metric(label='1$ in sat', value=f"{dollar_sat} sat")
    # sats_data = get_dollar_sats_data(daily_data)
    # col2.line_chart(sats_data)
    
    
    async with ClientSession() as session:
        uw = UserWallet(c, session)
        user_wallet = await uw.get_wallet_details()
        
        st.write(f"User Wallet: {user_wallet}")
        with st.container():
    
            amount_option = st.radio("Invoice type", ["SAT", "DOLLAR"])
            if amount_option == "SAT":
                st.header("Price in SAT")
                tot_sats = st.number_input("Set Invoice Amount in sat", min_value=50, step=50)
                dollar_value = tot_sats / int(dollar_sat)
                st.metric(label='Dollar Value', value=f"{dollar_value:.4f} $")
            
                
            if amount_option == "DOLLAR":
                st.header("Price in Dollar")
                tot_dollar = st.number_input("Set Invoice Amount in $", min_value=0.01, step=0.01)
                tot_sats = int(tot_dollar * int(dollar_sat))
                st.metric(label='Tot Sats', value=f"{tot_sats} SAT")
            
                
            memo = st.text_input("Memo", value="Demo Invoice")
                
            submitted = st.button("Request")
            if submitted:
                invoice = await uw.create_invoice(direction=False, amt=tot_sats, memo=memo, webhook="")
                st.json(invoice)
                # decoded_invoice = await uw.get_decoded(invoice['payment_request'])
                # st.json(decoded_invoice)
                bolt11 = invoice["payment_request"]
                qr_image = create_qr_image(bolt11)
                image_caption = f"INVOICE OF {tot_sats} SATS, {dollar_value:.2f} $ - MEMO: {memo}"
                st.image(qr_image, caption=image_caption, width=600)


                
if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    loop.run_until_complete(main())