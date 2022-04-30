import requests
from bu4 import Beautifulsoup
import pandas
import argparse
import connect

parser=argparse.ArgumentParser()
parser. add_argument("__page_num_max", help="Enter the number of pages to parse",type=int)
parser.add_argument("__dbname",help="Enter the name of sb",type=str)
args=parser.parse_args()

oyo_url="https://www.oyorooms. com hotels_in-bangalore/? page="
page_num_Max=args.page_num_max
scraped_info_list=[]
connect. connect(args.dbname)

for page_num in range (1,page_num_Max):
    url=oyo_url+str(page_num)
    print("GET Request for:"+url) 
    req=request.get(url)
    content=req.contnent
    
    soup=BeautifulSoup(content, "html.parser")
    
    all_hotels=soup.find_all("div", {"class":"hotelCardListing"})
    
    for hotel in all_hotels:
        hotel_dict={}
        hotel_dict["name"]=hotel.find("h3",{"class":"listing HotelDescription_hotel Name",}).text
        hotel_dict["adress"]=hotel.find("span", {"itemprop":"streetAdress"}).text
        hotel_dict["price"]= hotel. find("span", {"class":"listing price_final price"}). text
        try:
            hotel_dict["rating"]=hotel.find("span",{"class":" hotelRating__rating summary"}).text
        except AttributeError:
            hotel_dict["rating"]=None
            
        parent_amenities_elements=hotel.find("div", {"class":"amenitywrapper"})
        
        amenities_list=[]
        for amenirt in parent_amenities_elemet.find_all("div",{"class":"amenitywrapper__amenity"}) :
            amenities_list.append(amenity.find("span",{"class: "d-body-sm"}).text.strip()) 
            hitel_dict["amenities"]='1'join(amenities_list[:-1])
            scraped_info_list.append(hotel.dict)
            connect. insert_into.table(arge.dbname, tuple hotel_dict.values())
dataframe=pandas.DataFrame(scrapped_infi_list)
print("creating csv file...")
dataFrame. to. csv("oyo.csv")
connect. get. hotel_info(args.dbname)
                
         
        
