import requests
from PIL import Image
from io import BytesIO


class GetImages():
    
    def __init__(self, keyword) -> None:
        self.my_access_key = "BUnyc9CT6tg1UQDenxhxR-10vn4zYhz-mS7zZmyQz_o"        
        self.base_url = "https://api.unsplash.com/photos/"
        self.keyword = keyword
        self.params = {
            'query': keyword,
            'client_id': self.my_access_key
        }

    
    def get_image_from_unsplash(self):
        my_access_key = 'w4sSu2cUlyPGm73mcEugZTE2AWEHh8JuilivcZNuLg5hCKnySHekPv2Z'
        headers = {
            "Authorization": my_access_key,  # Replace with your actual API key
            }
        self.params = {
            "Content-Type": "application/json",
            "size": "medium",
            "page": 1,
            "per_page": 1,
            "orientation": "landscape",
            "locate": "en-US",
            'query': f"{self.keyword}",}    
        url = 'https://api.pexels.com/v1/search'       
        
              
        response = requests.get(url, params=self.params, headers=headers)
        
        if response.status_code != 200:
            print(f"Response status code error - {response.status_code}")
        else:
            data = response.json()
            # Access the first photo in the list and then access the 'src' dictionary       
            for photo in data.get('photos', []):                
                url = photo.get('src', {}).get('large')
                print(url)
                if url is not None:
                    return url
                else:
                    break    
        
    def download_image(self, url:str):
        response = requests.get(url=url)
        if response.content:
            content = response.content
            return content
        else:
            return None
        
        
    def show_images(self, images, save_image = False):
        img = Image.open(BytesIO(images))
        if save_image:
            try:
                img.save(f"{self.keyword}.jpg")
                print(f"Image saved as {self.keyword}.jpg")
            except Exception as e:
                print(f"Error during saving image - {e}")  
        # Display the image
        img.show()


    
    
    
    
    
    
      
    # def get_image_from_unsplash(self):
    #     url = "https://wikimedia-image-search.p.rapidapi.com/wiki/"

    #     querystring = {"query":"Elon Musk","page":"1","results":"12"}

    #     headers = {
    #         "X-RapidAPI-Key": "SIGN-UP-FOR-KEY",
    #         "X-RapidAPI-Host": "wikimedia-image-search.p.rapidapi.com"
    #     }

    #     response = requests.get(url, headers=headers, params=querystring)     
    #     json = response.json()
    #     print(json)
    #     if not response.status_code == 200:
    #         print(f"Response status code error - {response.status_code}")
    #         return False
    #     data = response.json()
        
    #     print(data)
    #     return data  
    
    
            
    # def generate_image_chat_gpt(self):
    #     secret_key_chat_gpt = "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"
    #     headers = {
    #         "Content-Type": "application/json",
    #         "Authorization": f"Bearer {secret_key_chat_gpt}",}
    #     data = {
    #         "model": "dall-e-3",
    #         "prompt": "A cute baby sea otter",
    #         "n": 1,
    #         "size": "1024x1024"}
    #     print(data) 
    #     response = requests.post(url=self.base_url, headers=headers, json=data)
    #     if response.status_code == 200:
    #         data = response.json()
    #         try:
    #             img = Image.open(BytesIO(data))
    #         except Exception as e:
    #             print(f"Error {e}")
    #         img.show()
    #     else:
    #         print(f"Status code is {response.status_code}, {response.text}")
        
        
        
    # def get_image_from_unsplash(self):
    #     print(self.params)       
    #     response = requests.get(self.base_url, params=self.params)
    #     json = response.json()
    #     print(json)
    #     if not response.status_code == 200:
    #         print(f"Response status code error - {response.status_code}")
    #         return False
    #     data = response.json()
    #     image_link = data[0]['urls']['small_s3']   
    #     print(image_link)
    #     return image_link   