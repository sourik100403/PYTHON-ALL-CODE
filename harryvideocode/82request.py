# import requests
# r=requests.get("https://www.google.com/search?q=icc+t20+world+cup&rlz=1C1CHBD_enIN964IN964&sxsrf=APq-WBu3z0vBLOJr3aenxqF_OEWfaGhUTw%3A1645586995115&ei=M6oVYoqyBpKRrwSdjYv4Cg&ved=0ahUKEwjKl6mi8ZT2AhWSyIsKHZ3GAq8Q4dUDCA4&uact=5&oq=icc+t20+world+cup&gs_lcp=Cgdnd3Mtd2l6EAMyCwgAEIAEELEDEIMBMggILhCABBCxAzIICAAQgAQQsQMyCwgAEIAEELEDEIMBMggIABCABBCxAzIICC4QsQMQgwEyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEOgcIABBHELADOgcIABCwAxBDOgoIABCwAxBDEIsDOg0IABDkAhCwAxCLAxgAOg8ILhDIAxCwAxBDEIsDGAE6FQguEMcBENEDEMgDELADEEMQiwMYAToKCC4QsQMQ1AIQQzoECAAQQzoNCC4QsQMQgwEQ1AIQQzoKCAAQsQMQgwEQQzoFCC4QkQI6BQgAEJECOggIABCxAxCDAToLCAAQsQMQgwEQkQI6CAgAELEDEJECOgQILhANOgQIABANSgQIQRgASgQIRhgBULkHWLgzYPM3aAJwAXgAgAGeAogB6RiSAQYwLjMuMTKYAQCgAQHIARO4AQLAAQHaAQYIABABGAnaAQYIARABGAg&sclient=gws-wiz")
# print(r.text)
import requests
r = requests.get("https://financialmodelingprep.com/api/company/price/AAPL")
print(r.text)
print(r.status_code)

# url = "www.something.com"
# data = {
#     "p1":4,
#     "p2":8
# }
# r2 = requests.post(url=url, data=data)