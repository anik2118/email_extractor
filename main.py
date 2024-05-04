from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import JSONResponse
import time
from bs4 import BeautifulSoup
import time 
import requests
import email_scraper
app = FastAPI()
templates = Jinja2Templates(directory="template")
@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("indexfinal.html", {"request": request})
@app.post("/process")
async def process_data(request: Request, input_data: list[str] = Form(...)): 
    def final(input_data):
        list_of_printed_cars=[]
        for url in input_data:
            
            try:
                search_query=f'https://{url}'
                result_urls=[search_query]
                print(url)
                html2=requests.get(search_query)
                time.sleep(1)
                soup2=BeautifulSoup(html2.content, 'html.parser')
                try:
                    # Find all the links inside the sub-menu
                    sub_menu_links = soup2.find_all("a")
                    # Print the links
                    for link in sub_menu_links:
                        anik=(link.get("href"))
                        if search_query not in result_urls:
                            continue
                        elif anik in result_urls:
                            continue
                        elif any(substring in str(anik) for substring in ["contact","about"]) and all(substring in str(anik)for substring in[url]):
                            result_urls.append(str(anik))
                        else:
                            continue
                    print(result_urls)
                    try:
                        time.sleep(2)
                        email_scraper.final(result_urls,url,list_of_printed_cars)

                    except:
                        print("not going to final")
                except :
                    continue
            except:
                time.sleep(5)
                continue
    final(input_data)
    return JSONResponse(content={"message": "the result documented in D:\ ahref_checker directory"})