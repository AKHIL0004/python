from typing import Text
from pandas.core.frame import DataFrame
import requests
from bs4 import BeautifulSoup
import pandas
import argparse
import connect
parser = argparse.ArgumentParser()
parser.add_argument("--page_num_max", help ="enter the number of pages to parse", type =int)
parser.add_argument("--dbname",help="enter the name of db", type=str)
args = parser.parse_args()

oyo_url = "https://www.oyorooms.com/search/?location=Ghaziabad%2C%20Uttar%20Pradesh%2C%20India&city=Ghaziabad&searchType=city&coupon=&checkin=02%2F06%2F2021&checkout=03%2F06%2F2021&roomConfig%5B%5D=2&showSearchElements=false&guests=2&rooms=1&country=india&filters%5Bcity_id%5D=9"
page_num_MAX = args.page_num_max
scrapped_info_list =[]
connect.connect(args.dbname)

for page_num in range(1, page_num_MAX):
    print("get request for: " + oyo_url)
    req = requests.get(oyo_url+str(page_num))
    content = req.content

    soup = BeautifulSoup(content, "html.parser")

    all_hotels = soup.find_all("div",{"class": "ListingHotelCardWrapper"})

    for hotel in all_hotels:
        hotel_dict = {}
        hotel_dict["name"] = hotel.find("h3",{"class": "listingHotelDescription_hotelName"})
        hotel_dict["address"] = hotel.find("span",{"class": "streetAddress"}).text
        hotel_dict["price"] = hotel.find("span",{"class": "listingPrice_finalPrice"}).text
    try:
        hotel_rating = hotel.find("span",{"class": "hotelRating_ratingSummary"}).text
    except AttributeError:
        pass 

    parent_amenities_element = hotel.find("div",{"class": "amenityWrapper"})

    amenities_list = []
    for amenity in parent_amenities_element.find_all("div", {"class": "amenityWrapper_amenity"}):
        amenities_list.append(amenity.find("span", {"class": "d-body-sm"}).text.strip())
    hotel_dict["amenities"] = ','.join(amenities_list[:-1])
    scrapped_info_list.append(hotel_dict)    
DataFrame = pandas.DataFrame(scrapped_info_list)
print("creating csv file..")
DataFrame.to_csv("oyo.csv")