import requests as req

#enter your url here
post_url = "https://56cc436f1cba.ngrok.io/"

#enter your file path here
upload_file = {'file':open("Test-text-2.txt","rb")}

req.post(post_url,files=upload_file)
