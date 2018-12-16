import json
import person

tony = person.Person('Tony', 'Soprano')
ralph = person.Person('Ralph', 'Ciffareto')

tony.clip(ralph, "You cooked that f*ckin' horse alive!")

print(json.dumps(ralph.__dict__))
print(json.dumps(tony.__dict__))
