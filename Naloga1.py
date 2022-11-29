import  json #vkljucimo json

podatki = {
  "name": "John",
  "age": 30,
  "city": "New York"
}
#izpisemo podatke v json obliki
print(json.dumps(podatki))
