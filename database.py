#===============================================================================================================================
#   File with all data functions
#===============================================================================================================================
from regions import findRegion
from utils import *

# function that carries out the processing of the data as requested in the challenge
def formated_data():
  data = database()
  ret = []
  for people in data:
    people['gender'] = people['gender'][0:1]
    people["nationality"]= "BR"
    people['location']['region'] = findRegion(people['location']['state'])
    
    formatPhone(people,'phone','telephoneNumbers')
    formatPhone(people, 'cell','mobileNumbers')

    removeItem(people['dob'], 'age')
    removeItem(people['registered'], 'age')
    removeItem(people, 'cell')
    removeItem(people, 'phone')

    ret.append(people)
  return ret

# JSON simulating data from the database
def database():
  return [
    {
      "gender": "male",
      "name": {
        "title": "mr",
        "first": "antonelo",
        "last": "da conceição"
      },
      "location": {
        "street": "8986 rua rui barbosa ",
        "city": "santo andré",
        "state": "alagoas",
        "postcode": 40751,
        "coordinates": {
          "latitude": "-69.8704",
          "longitude": "-165.9545"
        },
        "timezone": {
          "offset": "+1:00",
          "description": "Brussels, Copenhagen, Madrid, Paris"
        }
      },
      "email": "antonelo.daconceição@example.com",
      "dob": {
        "date": "1956-02-12T10:38:37Z",
        "age": 62
      },
      "registered": {
        "date": "2005-12-05T15:22:53Z",
        "age": 13
      },
      "phone": "(85) 8747-8125",
      "cell": "(87) 2414-0993",
      "picture": {
        "large": "https://randomuser.me/api/portraits/men/8.jpg",
        "medium": "https://randomuser.me/api/portraits/med/men/8.jpg",
        "thumbnail": "https://randomuser.me/api/portraits/thumb/men/8.jpg"
      }
    },
    {
      "gender": "male",
      "name": {
        "title": "mr",
        "first": "Igor",
        "last": "Vessali"
      },
      "location": {
        "street": "8986 rua rui barbosa ",
        "city": "floripa",
        "state": "santa catarina",
        "postcode": 40751,
        "coordinates": {
          "latitude": "-69.8704",
          "longitude": "-165.9545"
        },
        "timezone": {
          "offset": "+1:00",
          "description": "Brussels, Copenhagen, Madrid, Paris"
        }
      },
      "email": "igorvessali@gmail.com",
      "dob": {
        "date": "1956-02-12T10:38:37Z",
        "age": 62
      },
      "registered": {
        "date": "2005-12-05T15:22:53Z",
        "age": 13
      },
      "phone": "(85) 8747-8125",
      "cell": "(87) 2414-0993",
      "picture": {
        "large": "https://randomuser.me/api/portraits/men/8.jpg",
        "medium": "https://randomuser.me/api/portraits/med/men/8.jpg",
        "thumbnail": "https://randomuser.me/api/portraits/thumb/men/8.jpg"
      }
    },
    {
      "gender": "female",
      "name": {
        "title": "sra",
        "first": "Cistina",
        "last": "Doe"
      },
      "location": {
        "street": "8986 rua rui barbosa ",
        "city": "salvador",
        "state": "bahia",
        "postcode": 40751,
        "coordinates": {
          "latitude": "-69.8704",
          "longitude": "-165.9545"
        },
        "timezone": {
          "offset": "+1:00",
          "description": "Brussels, Copenhagen, Madrid, Paris"
        }
      },
      "email": "igorvessali@gmail.com",
      "dob": {
        "date": "1956-02-12T10:38:37Z",
        "age": 62
      },
      "registered": {
        "date": "2005-12-05T15:22:53Z",
        "age": 13
      },
      "phone": "(85) 8747-8125",
      "cell": "(87) 2414-0993",
      "picture": {
        "large": "https://randomuser.me/api/portraits/men/8.jpg",
        "medium": "https://randomuser.me/api/portraits/med/men/8.jpg",
        "thumbnail": "https://randomuser.me/api/portraits/thumb/men/8.jpg"
      }
    },
    {
      "gender": "female",
      "name": {
        "title": "sta",
        "first": "Manuella",
        "last": "Doe"
      },
      "location": {
        "street": "8986 rua rui barbosa ",
        "city": "brasilia",
        "state": "paraná",
        "postcode": 40751,
        "coordinates": {
          "latitude": "-69.8704",
          "longitude": "-165.9545"
        },
        "timezone": {
          "offset": "+1:00",
          "description": "Brussels, Copenhagen, Madrid, Paris"
        }
      },
      "email": "manuelladoe@gmail.com",
      "dob": {
        "date": "1956-02-12T10:38:37Z",
        "age": 62
      },
      "registered": {
        "date": "2005-12-05T15:22:53Z",
        "age": 13
      },
      "phone": "(85) 8747-8125",
      "cell": "(87) 2414-0993",
      "picture": {
        "large": "https://randomuser.me/api/portraits/men/8.jpg",
        "medium": "https://randomuser.me/api/portraits/med/men/8.jpg",
        "thumbnail": "https://randomuser.me/api/portraits/thumb/men/8.jpg"
      }
    },
    {
      "gender": "male",
      "name": {
        "title": "mr",
        "first": "antonelo",
        "last": "da conceição"
      },
      "location": {
        "street": "8986 rua rui barbosa ",
        "city": "santo andré",
        "state": "goiás",
        "postcode": 40751,
        "coordinates": {
          "latitude": "-69.8704",
          "longitude": "-165.9545"
        },
        "timezone": {
          "offset": "+1:00",
          "description": "Brussels, Copenhagen, Madrid, Paris"
        }
      },
      "email": "antonelo.daconceição@example.com",
      "dob": {
        "date": "1956-02-12T10:38:37Z",
        "age": 62
      },
      "registered": {
        "date": "2005-12-05T15:22:53Z",
        "age": 13
      },
      "phone": "(85) 8747-8125",
      "cell": "(87) 2414-0993",
      "picture": {
        "large": "https://randomuser.me/api/portraits/men/8.jpg",
        "medium": "https://randomuser.me/api/portraits/med/men/8.jpg",
        "thumbnail": "https://randomuser.me/api/portraits/thumb/men/8.jpg"
      }
    },
    {
      "gender": "male",
      "name": {
        "title": "mr",
        "first": "antonelo",
        "last": "da conceição"
      },
      "location": {
        "street": "8986 rua rui barbosa ",
        "city": "santo andré",
        "state": "acre",
        "postcode": 40751,
        "coordinates": {
          "latitude": "-69.8704",
          "longitude": "-165.9545"
        },
        "timezone": {
          "offset": "+1:00",
          "description": "Brussels, Copenhagen, Madrid, Paris"
        }
      },
      "email": "antonelo.daconceição@example.com",
      "dob": {
        "date": "1956-02-12T10:38:37Z",
        "age": 62
      },
      "registered": {
        "date": "2005-12-05T15:22:53Z",
        "age": 13
      },
      "phone": "(85) 8747-8125",
      "cell": "(87) 2414-0993",
      "picture": {
        "large": "https://randomuser.me/api/portraits/men/8.jpg",
        "medium": "https://randomuser.me/api/portraits/med/men/8.jpg",
        "thumbnail": "https://randomuser.me/api/portraits/thumb/men/8.jpg"
      }
    },
    {
      "gender": "male",
      "name": {
        "title": "mr",
        "first": "antonelo",
        "last": "da conceição"
      },
      "location": {
        "street": "8986 rua rui barbosa ",
        "city": "santo andré",
        "state": "amapá",
        "postcode": 40751,
        "coordinates": {
          "latitude": "-69.8704",
          "longitude": "-165.9545"
        },
        "timezone": {
          "offset": "+1:00",
          "description": "Brussels, Copenhagen, Madrid, Paris"
        }
      },
      "email": "antonelo.daconceição@example.com",
      "dob": {
        "date": "1956-02-12T10:38:37Z",
        "age": 62
      },
      "registered": {
        "date": "2005-12-05T15:22:53Z",
        "age": 13
      },
      "phone": "(85) 8747-8125",
      "cell": "(87) 2414-0993",
      "picture": {
        "large": "https://randomuser.me/api/portraits/men/8.jpg",
        "medium": "https://randomuser.me/api/portraits/med/men/8.jpg",
        "thumbnail": "https://randomuser.me/api/portraits/thumb/men/8.jpg"
      }
    },
    {
      "gender": "male",
      "name": {
        "title": "mr",
        "first": "antonelo",
        "last": "da conceição"
      },
      "location": {
        "street": "8986 rua rui barbosa ",
        "city": "santo andré",
        "state": "são paulo",
        "postcode": 40751,
        "coordinates": {
          "latitude": "-69.8704",
          "longitude": "-165.9545"
        },
        "timezone": {
          "offset": "+1:00",
          "description": "Brussels, Copenhagen, Madrid, Paris"
        }
      },
      "email": "antonelo.daconceição@example.com",
      "dob": {
        "date": "1956-02-12T10:38:37Z",
        "age": 62
      },
      "registered": {
        "date": "2005-12-05T15:22:53Z",
        "age": 13
      },
      "phone": "(85) 8747-8125",
      "cell": "(87) 2414-0993",
      "picture": {
        "large": "https://randomuser.me/api/portraits/men/8.jpg",
        "medium": "https://randomuser.me/api/portraits/med/men/8.jpg",
        "thumbnail": "https://randomuser.me/api/portraits/thumb/men/8.jpg"
      }
    },
    {
      "gender": "male",
      "name": {
        "title": "mr",
        "first": "antonelo",
        "last": "da conceição"
      },
      "location": {
        "street": "8986 rua rui barbosa ",
        "city": "santo andré",
        "state": "rio de janeiro",
        "postcode": 40751,
        "coordinates": {
          "latitude": "-69.8704",
          "longitude": "-165.9545"
        },
        "timezone": {
          "offset": "+1:00",
          "description": "Brussels, Copenhagen, Madrid, Paris"
        }
      },
      "email": "antonelo.daconceição@example.com",
      "dob": {
        "date": "1956-02-12T10:38:37Z",
        "age": 62
      },
      "registered": {
        "date": "2005-12-05T15:22:53Z",
        "age": 13
      },
      "phone": "(85) 8747-8125",
      "cell": "(87) 2414-0993",
      "picture": {
        "large": "https://randomuser.me/api/portraits/men/8.jpg",
        "medium": "https://randomuser.me/api/portraits/med/men/8.jpg",
        "thumbnail": "https://randomuser.me/api/portraits/thumb/men/8.jpg"
      }
    },
    {
      "gender": "male",
      "name": {
        "title": "mr",
        "first": "antonelo",
        "last": "da conceição"
      },
      "location": {
        "street": "8986 rua rui barbosa ",
        "city": "santo andré",
        "state": "rio grande do sul",
        "postcode": 40751,
        "coordinates": {
          "latitude": "-69.8704",
          "longitude": "-165.9545"
        },
        "timezone": {
          "offset": "+1:00",
          "description": "Brussels, Copenhagen, Madrid, Paris"
        }
      },
      "email": "antonelo.daconceição@example.com",
      "dob": {
        "date": "1956-02-12T10:38:37Z",
        "age": 62
      },
      "registered": {
        "date": "2005-12-05T15:22:53Z",
        "age": 13
      },
      "phone": "(85) 8747-8125",
      "cell": "(87) 2414-0993",
      "picture": {
        "large": "https://randomuser.me/api/portraits/men/8.jpg",
        "medium": "https://randomuser.me/api/portraits/med/men/8.jpg",
        "thumbnail": "https://randomuser.me/api/portraits/thumb/men/8.jpg"
      }
    },
    {
      "gender": "male",
      "name": {
        "title": "mr",
        "first": "antonelo",
        "last": "da conceição"
      },
      "location": {
        "street": "8986 rua rui barbosa ",
        "city": "santo andré",
        "state": "minas gerais",
        "postcode": 40751,
        "coordinates": {
          "latitude": "-69.8704",
          "longitude": "-165.9545"
        },
        "timezone": {
          "offset": "+1:00",
          "description": "Brussels, Copenhagen, Madrid, Paris"
        }
      },
      "email": "antonelo.daconceição@example.com",
      "dob": {
        "date": "1956-02-12T10:38:37Z",
        "age": 62
      },
      "registered": {
        "date": "2005-12-05T15:22:53Z",
        "age": 13
      },
      "phone": "(85) 8747-8125",
      "cell": "(87) 2414-0993",
      "picture": {
        "large": "https://randomuser.me/api/portraits/men/8.jpg",
        "medium": "https://randomuser.me/api/portraits/med/men/8.jpg",
        "thumbnail": "https://randomuser.me/api/portraits/thumb/men/8.jpg"
      }
    },
    {
      "gender": "male",
      "name": {
        "title": "mr",
        "first": "antonelo",
        "last": "da conceição"
      },
      "location": {
        "street": "8986 rua rui barbosa ",
        "city": "santo andré",
        "state": "santa catarina",
        "postcode": 40751,
        "coordinates": {
          "latitude": "-69.8704",
          "longitude": "-165.9545"
        },
        "timezone": {
          "offset": "+1:00",
          "description": "Brussels, Copenhagen, Madrid, Paris"
        }
      },
      "email": "antonelo.daconceição@example.com",
      "dob": {
        "date": "1956-02-12T10:38:37Z",
        "age": 62
      },
      "registered": {
        "date": "2005-12-05T15:22:53Z",
        "age": 13
      },
      "phone": "(85) 8747-8125",
      "cell": "(87) 2414-0993",
      "picture": {
        "large": "https://randomuser.me/api/portraits/men/8.jpg",
        "medium": "https://randomuser.me/api/portraits/med/men/8.jpg",
        "thumbnail": "https://randomuser.me/api/portraits/thumb/men/8.jpg"
      }
    },
    {
      "gender": "male",
      "name": {
        "title": "mr",
        "first": "antonelo",
        "last": "da conceição"
      },
      "location": {
        "street": "8986 rua rui barbosa ",
        "city": "santo andré",
        "state": "paraná",
        "postcode": 40751,
        "coordinates": {
          "latitude": "-69.8704",
          "longitude": "-165.9545"
        },
        "timezone": {
          "offset": "+1:00",
          "description": "Brussels, Copenhagen, Madrid, Paris"
        }
      },
      "email": "antonelo.daconceição@example.com",
      "dob": {
        "date": "1956-02-12T10:38:37Z",
        "age": 62
      },
      "registered": {
        "date": "2005-12-05T15:22:53Z",
        "age": 13
      },
      "phone": "(85) 8747-8125",
      "cell": "(87) 2414-0993",
      "picture": {
        "large": "https://randomuser.me/api/portraits/men/8.jpg",
        "medium": "https://randomuser.me/api/portraits/med/men/8.jpg",
        "thumbnail": "https://randomuser.me/api/portraits/thumb/men/8.jpg"
      }
    },
    {
      "gender": "male",
      "name": {
        "title": "mr",
        "first": "antonelo",
        "last": "da conceição"
      },
      "location": {
        "street": "8986 rua rui barbosa ",
        "city": "santo andré",
        "state": "são paulo",
        "postcode": 40751,
        "coordinates": {
          "latitude": "-69.8704",
          "longitude": "-165.9545"
        },
        "timezone": {
          "offset": "+1:00",
          "description": "Brussels, Copenhagen, Madrid, Paris"
        }
      },
      "email": "antonelo.daconceição@example.com",
      "dob": {
        "date": "1956-02-12T10:38:37Z",
        "age": 62
      },
      "registered": {
        "date": "2005-12-05T15:22:53Z",
        "age": 13
      },
      "phone": "(85) 8747-8125",
      "cell": "(87) 2414-0993",
      "picture": {
        "large": "https://randomuser.me/api/portraits/men/8.jpg",
        "medium": "https://randomuser.me/api/portraits/med/men/8.jpg",
        "thumbnail": "https://randomuser.me/api/portraits/thumb/men/8.jpg"
      }
    },
    {
      "gender": "male",
      "name": {
        "title": "mr",
        "first": "antonelo",
        "last": "da conceição"
      },
      "location": {
        "street": "8986 rua rui barbosa ",
        "city": "santo andré",
        "state": "mato grosso",
        "postcode": 40751,
        "coordinates": {
          "latitude": "-69.8704",
          "longitude": "-165.9545"
        },
        "timezone": {
          "offset": "+1:00",
          "description": "Brussels, Copenhagen, Madrid, Paris"
        }
      },
      "email": "antonelo.daconceição@example.com",
      "dob": {
        "date": "1956-02-12T10:38:37Z",
        "age": 62
      },
      "registered": {
        "date": "2005-12-05T15:22:53Z",
        "age": 13
      },
      "phone": "(85) 8747-8125",
      "cell": "(87) 2414-0993",
      "picture": {
        "large": "https://randomuser.me/api/portraits/men/8.jpg",
        "medium": "https://randomuser.me/api/portraits/med/men/8.jpg",
        "thumbnail": "https://randomuser.me/api/portraits/thumb/men/8.jpg"
      }
    },
    {
      "gender": "male",
      "name": {
        "title": "mr",
        "first": "antonelo",
        "last": "da conceição"
      },
      "location": {
        "street": "8986 rua rui barbosa ",
        "city": "santo andré",
        "state": "alagoas",
        "postcode": 40751,
        "coordinates": {
          "latitude": "-69.8704",
          "longitude": "-165.9545"
        },
        "timezone": {
          "offset": "+1:00",
          "description": "Brussels, Copenhagen, Madrid, Paris"
        }
      },
      "email": "antonelo.daconceição@example.com",
      "dob": {
        "date": "1956-02-12T10:38:37Z",
        "age": 62
      },
      "registered": {
        "date": "2005-12-05T15:22:53Z",
        "age": 13
      },
      "phone": "(85) 8747-8125",
      "cell": "(87) 2414-0993",
      "picture": {
        "large": "https://randomuser.me/api/portraits/men/8.jpg",
        "medium": "https://randomuser.me/api/portraits/med/men/8.jpg",
        "thumbnail": "https://randomuser.me/api/portraits/thumb/men/8.jpg"
      }
    },
    {
      "gender": "male",
      "name": {
        "title": "mr",
        "first": "antonelo",
        "last": "da conceição"
      },
      "location": {
        "street": "8986 rua rui barbosa ",
        "city": "santo andré",
        "state": "bahia",
        "postcode": 40751,
        "coordinates": {
          "latitude": "-69.8704",
          "longitude": "-165.9545"
        },
        "timezone": {
          "offset": "+1:00",
          "description": "Brussels, Copenhagen, Madrid, Paris"
        }
      },
      "email": "antonelo.daconceição@example.com",
      "dob": {
        "date": "1956-02-12T10:38:37Z",
        "age": 62
      },
      "registered": {
        "date": "2005-12-05T15:22:53Z",
        "age": 13
      },
      "phone": "(85) 8747-8125",
      "cell": "(87) 2414-0993",
      "picture": {
        "large": "https://randomuser.me/api/portraits/men/8.jpg",
        "medium": "https://randomuser.me/api/portraits/med/men/8.jpg",
        "thumbnail": "https://randomuser.me/api/portraits/thumb/men/8.jpg"
      }
    },
    {
      "gender": "male",
      "name": {
        "title": "mr",
        "first": "antonelo",
        "last": "da conceição"
      },
      "location": {
        "street": "8986 rua rui barbosa ",
        "city": "santo andré",
        "state": "pará",
        "postcode": 40751,
        "coordinates": {
          "latitude": "-69.8704",
          "longitude": "-165.9545"
        },
        "timezone": {
          "offset": "+1:00",
          "description": "Brussels, Copenhagen, Madrid, Paris"
        }
      },
      "email": "antonelo.daconceição@example.com",
      "dob": {
        "date": "1956-02-12T10:38:37Z",
        "age": 62
      },
      "registered": {
        "date": "2005-12-05T15:22:53Z",
        "age": 13
      },
      "phone": "(85) 8747-8125",
      "cell": "(87) 2414-0993",
      "picture": {
        "large": "https://randomuser.me/api/portraits/men/8.jpg",
        "medium": "https://randomuser.me/api/portraits/med/men/8.jpg",
        "thumbnail": "https://randomuser.me/api/portraits/thumb/men/8.jpg"
      }
    },
    {
      "gender": "male",
      "name": {
        "title": "mr",
        "first": "antonelo",
        "last": "da conceição"
      },
      "location": {
        "street": "8986 rua rui barbosa ",
        "city": "santo andré",
        "state": "mato grosso do sul",
        "postcode": 40751,
        "coordinates": {
          "latitude": "-69.8704",
          "longitude": "-165.9545"
        },
        "timezone": {
          "offset": "+1:00",
          "description": "Brussels, Copenhagen, Madrid, Paris"
        }
      },
      "email": "antonelo.daconceição@example.com",
      "dob": {
        "date": "1956-02-12T10:38:37Z",
        "age": 62
      },
      "registered": {
        "date": "2005-12-05T15:22:53Z",
        "age": 13
      },
      "phone": "(85) 8747-8125",
      "cell": "(87) 2414-0993",
      "picture": {
        "large": "https://randomuser.me/api/portraits/men/8.jpg",
        "medium": "https://randomuser.me/api/portraits/med/men/8.jpg",
        "thumbnail": "https://randomuser.me/api/portraits/thumb/men/8.jpg"
      }
    },
    {
      "gender": "male",
      "name": {
        "title": "mr",
        "first": "antonelo",
        "last": "da conceição"
      },
      "location": {
        "street": "8986 rua rui barbosa ",
        "city": "santo andré",
        "state": "goiás",
        "postcode": 40751,
        "coordinates": {
          "latitude": "-69.8704",
          "longitude": "-165.9545"
        },
        "timezone": {
          "offset": "+1:00",
          "description": "Brussels, Copenhagen, Madrid, Paris"
        }
      },
      "email": "antonelo.daconceição@example.com",
      "dob": {
        "date": "1956-02-12T10:38:37Z",
        "age": 62
      },
      "registered": {
        "date": "2005-12-05T15:22:53Z",
        "age": 13
      },
      "phone": "(85) 8747-8125",
      "cell": "(87) 2414-0993",
      "picture": {
        "large": "https://randomuser.me/api/portraits/men/8.jpg",
        "medium": "https://randomuser.me/api/portraits/med/men/8.jpg",
        "thumbnail": "https://randomuser.me/api/portraits/thumb/men/8.jpg"
      }
    },
    {
      "gender": "male",
      "name": {
        "title": "mr",
        "first": "antonelo",
        "last": "da conceição"
      },
      "location": {
        "street": "8986 rua rui barbosa ",
        "city": "santo andré",
        "state": "são paulo",
        "postcode": 40751,
        "coordinates": {
          "latitude": "-69.8704",
          "longitude": "-165.9545"
        },
        "timezone": {
          "offset": "+1:00",
          "description": "Brussels, Copenhagen, Madrid, Paris"
        }
      },
      "email": "antonelo.daconceição@example.com",
      "dob": {
        "date": "1956-02-12T10:38:37Z",
        "age": 62
      },
      "registered": {
        "date": "2005-12-05T15:22:53Z",
        "age": 13
      },
      "phone": "(85) 8747-8125",
      "cell": "(87) 2414-0993",
      "picture": {
        "large": "https://randomuser.me/api/portraits/men/8.jpg",
        "medium": "https://randomuser.me/api/portraits/med/men/8.jpg",
        "thumbnail": "https://randomuser.me/api/portraits/thumb/men/8.jpg"
      }
    },
    {
      "gender": "male",
      "name": {
        "title": "mr",
        "first": "antonelo",
        "last": "da conceição"
      },
      "location": {
        "street": "8986 rua rui barbosa ",
        "city": "santo andré",
        "state": "santa catarina",
        "postcode": 40751,
        "coordinates": {
          "latitude": "-69.8704",
          "longitude": "-165.9545"
        },
        "timezone": {
          "offset": "+1:00",
          "description": "Brussels, Copenhagen, Madrid, Paris"
        }
      },
      "email": "antonelo.daconceição@example.com",
      "dob": {
        "date": "1956-02-12T10:38:37Z",
        "age": 62
      },
      "registered": {
        "date": "2005-12-05T15:22:53Z",
        "age": 13
      },
      "phone": "(85) 8747-8125",
      "cell": "(87) 2414-0993",
      "picture": {
        "large": "https://randomuser.me/api/portraits/men/8.jpg",
        "medium": "https://randomuser.me/api/portraits/med/men/8.jpg",
        "thumbnail": "https://randomuser.me/api/portraits/thumb/men/8.jpg"
      }
    },
    {
      "gender": "male",
      "name": {
        "title": "mr",
        "first": "antonelo",
        "last": "da conceição"
      },
      "location": {
        "street": "8986 rua rui barbosa ",
        "city": "santo andré",
        "state": "paraná",
        "postcode": 40751,
        "coordinates": {
          "latitude": "-69.8704",
          "longitude": "-165.9545"
        },
        "timezone": {
          "offset": "+1:00",
          "description": "Brussels, Copenhagen, Madrid, Paris"
        }
      },
      "email": "antonelo.daconceição@example.com",
      "dob": {
        "date": "1956-02-12T10:38:37Z",
        "age": 62
      },
      "registered": {
        "date": "2005-12-05T15:22:53Z",
        "age": 13
      },
      "phone": "(85) 8747-8125",
      "cell": "(87) 2414-0993",
      "picture": {
        "large": "https://randomuser.me/api/portraits/men/8.jpg",
        "medium": "https://randomuser.me/api/portraits/med/men/8.jpg",
        "thumbnail": "https://randomuser.me/api/portraits/thumb/men/8.jpg"
      }
    },
    {
      "gender": "male",
      "name": {
        "title": "mr",
        "first": "antonelo",
        "last": "da conceição"
      },
      "location": {
        "street": "8986 rua rui barbosa ",
        "city": "santo andré",
        "state": "rio grande do sul",
        "postcode": 40751,
        "coordinates": {
          "latitude": "-69.8704",
          "longitude": "-165.9545"
        },
        "timezone": {
          "offset": "+1:00",
          "description": "Brussels, Copenhagen, Madrid, Paris"
        }
      },
      "email": "antonelo.daconceição@example.com",
      "dob": {
        "date": "1956-02-12T10:38:37Z",
        "age": 62
      },
      "registered": {
        "date": "2005-12-05T15:22:53Z",
        "age": 13
      },
      "phone": "(85) 8747-8125",
      "cell": "(87) 2414-0993",
      "picture": {
        "large": "https://randomuser.me/api/portraits/men/8.jpg",
        "medium": "https://randomuser.me/api/portraits/med/men/8.jpg",
        "thumbnail": "https://randomuser.me/api/portraits/thumb/men/8.jpg"
      }
    },
    {
      "gender": "male",
      "name": {
        "title": "mr",
        "first": "antonelo",
        "last": "da conceição"
      },
      "location": {
        "street": "8986 rua rui barbosa ",
        "city": "santo andré",
        "state": "alagoas",
        "postcode": 40751,
        "coordinates": {
          "latitude": "-69.8704",
          "longitude": "-165.9545"
        },
        "timezone": {
          "offset": "+1:00",
          "description": "Brussels, Copenhagen, Madrid, Paris"
        }
      },
      "email": "antonelo.daconceição@example.com",
      "dob": {
        "date": "1956-02-12T10:38:37Z",
        "age": 62
      },
      "registered": {
        "date": "2005-12-05T15:22:53Z",
        "age": 13
      },
      "phone": "(85) 8747-8125",
      "cell": "(87) 2414-0993",
      "picture": {
        "large": "https://randomuser.me/api/portraits/men/8.jpg",
        "medium": "https://randomuser.me/api/portraits/med/men/8.jpg",
        "thumbnail": "https://randomuser.me/api/portraits/thumb/men/8.jpg"
      }
    },
    {
      "gender": "male",
      "name": {
        "title": "mr",
        "first": "antonelo",
        "last": "da conceição"
      },
      "location": {
        "street": "8986 rua rui barbosa ",
        "city": "santo andré",
        "state": "minas gerais",
        "postcode": 40751,
        "coordinates": {
          "latitude": "-69.8704",
          "longitude": "-165.9545"
        },
        "timezone": {
          "offset": "+1:00",
          "description": "Brussels, Copenhagen, Madrid, Paris"
        }
      },
      "email": "antonelo.daconceição@example.com",
      "dob": {
        "date": "1956-02-12T10:38:37Z",
        "age": 62
      },
      "registered": {
        "date": "2005-12-05T15:22:53Z",
        "age": 13
      },
      "phone": "(85) 8747-8125",
      "cell": "(87) 2414-0993",
      "picture": {
        "large": "https://randomuser.me/api/portraits/men/8.jpg",
        "medium": "https://randomuser.me/api/portraits/med/men/8.jpg",
        "thumbnail": "https://randomuser.me/api/portraits/thumb/men/8.jpg"
      }
    },
    {
      "gender": "male",
      "name": {
        "title": "mr",
        "first": "antonelo",
        "last": "da conceição"
      },
      "location": {
        "street": "8986 rua rui barbosa ",
        "city": "santo andré",
        "state": "santa catarina",
        "postcode": 40751,
        "coordinates": {
          "latitude": "-69.8704",
          "longitude": "-165.9545"
        },
        "timezone": {
          "offset": "+1:00",
          "description": "Brussels, Copenhagen, Madrid, Paris"
        }
      },
      "email": "antonelo.daconceição@example.com",
      "dob": {
        "date": "1956-02-12T10:38:37Z",
        "age": 62
      },
      "registered": {
        "date": "2005-12-05T15:22:53Z",
        "age": 13
      },
      "phone": "(85) 8747-8125",
      "cell": "(87) 2414-0993",
      "picture": {
        "large": "https://randomuser.me/api/portraits/men/8.jpg",
        "medium": "https://randomuser.me/api/portraits/med/men/8.jpg",
        "thumbnail": "https://randomuser.me/api/portraits/thumb/men/8.jpg"
      }
    },
    {
      "gender": "male",
      "name": {
        "title": "mr",
        "first": "antonelo",
        "last": "da conceição"
      },
      "location": {
        "street": "8986 rua rui barbosa ",
        "city": "santo andré",
        "state": "santa catarina",
        "postcode": 40751,
        "coordinates": {
          "latitude": "-69.8704",
          "longitude": "-165.9545"
        },
        "timezone": {
          "offset": "+1:00",
          "description": "Brussels, Copenhagen, Madrid, Paris"
        }
      },
      "email": "antonelo.daconceição@example.com",
      "dob": {
        "date": "1956-02-12T10:38:37Z",
        "age": 62
      },
      "registered": {
        "date": "2005-12-05T15:22:53Z",
        "age": 13
      },
      "phone": "(85) 8747-8125",
      "cell": "(87) 2414-0993",
      "picture": {
        "large": "https://randomuser.me/api/portraits/men/8.jpg",
        "medium": "https://randomuser.me/api/portraits/med/men/8.jpg",
        "thumbnail": "https://randomuser.me/api/portraits/thumb/men/8.jpg"
      }
    },
    {
      "gender": "male",
      "name": {
        "title": "mr",
        "first": "antonelo",
        "last": "da conceição"
      },
      "location": {
        "street": "8986 rua rui barbosa ",
        "city": "santo andré",
        "state": "santa catarina",
        "postcode": 40751,
        "coordinates": {
          "latitude": "-69.8704",
          "longitude": "-165.9545"
        },
        "timezone": {
          "offset": "+1:00",
          "description": "Brussels, Copenhagen, Madrid, Paris"
        }
      },
      "email": "antonelo.daconceição@example.com",
      "dob": {
        "date": "1956-02-12T10:38:37Z",
        "age": 62
      },
      "registered": {
        "date": "2005-12-05T15:22:53Z",
        "age": 13
      },
      "phone": "(85) 8747-8125",
      "cell": "(87) 2414-0993",
      "picture": {
        "large": "https://randomuser.me/api/portraits/men/8.jpg",
        "medium": "https://randomuser.me/api/portraits/med/men/8.jpg",
        "thumbnail": "https://randomuser.me/api/portraits/thumb/men/8.jpg"
      }
    },
    {
      "gender": "male",
      "name": {
        "title": "mr",
        "first": "antonelo",
        "last": "da conceição"
      },
      "location": {
        "street": "8986 rua rui barbosa ",
        "city": "santo andré",
        "state": "santa catarina",
        "postcode": 40751,
        "coordinates": {
          "latitude": "-69.8704",
          "longitude": "-165.9545"
        },
        "timezone": {
          "offset": "+1:00",
          "description": "Brussels, Copenhagen, Madrid, Paris"
        }
      },
      "email": "antonelo.daconceição@example.com",
      "dob": {
        "date": "1956-02-12T10:38:37Z",
        "age": 62
      },
      "registered": {
        "date": "2005-12-05T15:22:53Z",
        "age": 13
      },
      "phone": "(85) 8747-8125",
      "cell": "(87) 2414-0993",
      "picture": {
        "large": "https://randomuser.me/api/portraits/men/8.jpg",
        "medium": "https://randomuser.me/api/portraits/med/men/8.jpg",
        "thumbnail": "https://randomuser.me/api/portraits/thumb/men/8.jpg"
      }
    },
    {
      "gender": "male",
      "name": {
        "title": "mr",
        "first": "antonelo",
        "last": "da conceição"
      },
      "location": {
        "street": "8986 rua rui barbosa ",
        "city": "santo andré",
        "state": "santa catarina",
        "postcode": 40751,
        "coordinates": {
          "latitude": "-69.8704",
          "longitude": "-165.9545"
        },
        "timezone": {
          "offset": "+1:00",
          "description": "Brussels, Copenhagen, Madrid, Paris"
        }
      },
      "email": "antonelo.daconceição@example.com",
      "dob": {
        "date": "1956-02-12T10:38:37Z",
        "age": 62
      },
      "registered": {
        "date": "2005-12-05T15:22:53Z",
        "age": 13
      },
      "phone": "(85) 8747-8125",
      "cell": "(87) 2414-0993",
      "picture": {
        "large": "https://randomuser.me/api/portraits/men/8.jpg",
        "medium": "https://randomuser.me/api/portraits/med/men/8.jpg",
        "thumbnail": "https://randomuser.me/api/portraits/thumb/men/8.jpg"
      }
    },
    {
      "gender": "male",
      "name": {
        "title": "mr",
        "first": "antonelo",
        "last": "da conceição"
      },
      "location": {
        "street": "8986 rua rui barbosa ",
        "city": "santo andré",
        "state": "santa catarina",
        "postcode": 40751,
        "coordinates": {
          "latitude": "-69.8704",
          "longitude": "-165.9545"
        },
        "timezone": {
          "offset": "+1:00",
          "description": "Brussels, Copenhagen, Madrid, Paris"
        }
      },
      "email": "antonelo.daconceição@example.com",
      "dob": {
        "date": "1956-02-12T10:38:37Z",
        "age": 62
      },
      "registered": {
        "date": "2005-12-05T15:22:53Z",
        "age": 13
      },
      "phone": "(85) 8747-8125",
      "cell": "(87) 2414-0993",
      "picture": {
        "large": "https://randomuser.me/api/portraits/men/8.jpg",
        "medium": "https://randomuser.me/api/portraits/med/men/8.jpg",
        "thumbnail": "https://randomuser.me/api/portraits/thumb/men/8.jpg"
      }
    },
    {
      "gender": "male",
      "name": {
        "title": "mr",
        "first": "antonelo",
        "last": "da conceição"
      },
      "location": {
        "street": "8986 rua rui barbosa ",
        "city": "santo andré",
        "state": "santa catarina",
        "postcode": 40751,
        "coordinates": {
          "latitude": "-69.8704",
          "longitude": "-165.9545"
        },
        "timezone": {
          "offset": "+1:00",
          "description": "Brussels, Copenhagen, Madrid, Paris"
        }
      },
      "email": "antonelo.daconceição@example.com",
      "dob": {
        "date": "1956-02-12T10:38:37Z",
        "age": 62
      },
      "registered": {
        "date": "2005-12-05T15:22:53Z",
        "age": 13
      },
      "phone": "(85) 8747-8125",
      "cell": "(87) 2414-0993",
      "picture": {
        "large": "https://randomuser.me/api/portraits/men/8.jpg",
        "medium": "https://randomuser.me/api/portraits/med/men/8.jpg",
        "thumbnail": "https://randomuser.me/api/portraits/thumb/men/8.jpg"
      }
    },
    {
      "gender": "male",
      "name": {
        "title": "mr",
        "first": "antonelo",
        "last": "da conceição"
      },
      "location": {
        "street": "8986 rua rui barbosa ",
        "city": "santo andré",
        "state": "santa catarina",
        "postcode": 40751,
        "coordinates": {
          "latitude": "-69.8704",
          "longitude": "-165.9545"
        },
        "timezone": {
          "offset": "+1:00",
          "description": "Brussels, Copenhagen, Madrid, Paris"
        }
      },
      "email": "antonelo.daconceição@example.com",
      "dob": {
        "date": "1956-02-12T10:38:37Z",
        "age": 62
      },
      "registered": {
        "date": "2005-12-05T15:22:53Z",
        "age": 13
      },
      "phone": "(85) 8747-8125",
      "cell": "(87) 2414-0993",
      "picture": {
        "large": "https://randomuser.me/api/portraits/men/8.jpg",
        "medium": "https://randomuser.me/api/portraits/med/men/8.jpg",
        "thumbnail": "https://randomuser.me/api/portraits/thumb/men/8.jpg"
      }
    },
    {
      "gender": "male",
      "name": {
        "title": "mr",
        "first": "antonelo",
        "last": "da conceição"
      },
      "location": {
        "street": "8986 rua rui barbosa ",
        "city": "santo andré",
        "state": "santa catarina",
        "postcode": 40751,
        "coordinates": {
          "latitude": "-69.8704",
          "longitude": "-165.9545"
        },
        "timezone": {
          "offset": "+1:00",
          "description": "Brussels, Copenhagen, Madrid, Paris"
        }
      },
      "email": "antonelo.daconceição@example.com",
      "dob": {
        "date": "1956-02-12T10:38:37Z",
        "age": 62
      },
      "registered": {
        "date": "2005-12-05T15:22:53Z",
        "age": 13
      },
      "phone": "(85) 8747-8125",
      "cell": "(87) 2414-0993",
      "picture": {
        "large": "https://randomuser.me/api/portraits/men/8.jpg",
        "medium": "https://randomuser.me/api/portraits/med/men/8.jpg",
        "thumbnail": "https://randomuser.me/api/portraits/thumb/men/8.jpg"
      }
    },
    {
      "gender": "male",
      "name": {
        "title": "mr",
        "first": "antonelo",
        "last": "da conceição"
      },
      "location": {
        "street": "8986 rua rui barbosa ",
        "city": "santo andré",
        "state": "santa catarina",
        "postcode": 40751,
        "coordinates": {
          "latitude": "-69.8704",
          "longitude": "-165.9545"
        },
        "timezone": {
          "offset": "+1:00",
          "description": "Brussels, Copenhagen, Madrid, Paris"
        }
      },
      "email": "antonelo.daconceição@example.com",
      "dob": {
        "date": "1956-02-12T10:38:37Z",
        "age": 62
      },
      "registered": {
        "date": "2005-12-05T15:22:53Z",
        "age": 13
      },
      "phone": "(85) 8747-8125",
      "cell": "(87) 2414-0993",
      "picture": {
        "large": "https://randomuser.me/api/portraits/men/8.jpg",
        "medium": "https://randomuser.me/api/portraits/med/men/8.jpg",
        "thumbnail": "https://randomuser.me/api/portraits/thumb/men/8.jpg"
      }
    },
    {
      "gender": "male",
      "name": {
        "title": "mr",
        "first": "antonelo",
        "last": "da conceição"
      },
      "location": {
        "street": "8986 rua rui barbosa ",
        "city": "santo andré",
        "state": "santa catarina",
        "postcode": 40751,
        "coordinates": {
          "latitude": "-69.8704",
          "longitude": "-165.9545"
        },
        "timezone": {
          "offset": "+1:00",
          "description": "Brussels, Copenhagen, Madrid, Paris"
        }
      },
      "email": "antonelo.daconceição@example.com",
      "dob": {
        "date": "1956-02-12T10:38:37Z",
        "age": 62
      },
      "registered": {
        "date": "2005-12-05T15:22:53Z",
        "age": 13
      },
      "phone": "(85) 8747-8125",
      "cell": "(87) 2414-0993",
      "picture": {
        "large": "https://randomuser.me/api/portraits/men/8.jpg",
        "medium": "https://randomuser.me/api/portraits/med/men/8.jpg",
        "thumbnail": "https://randomuser.me/api/portraits/thumb/men/8.jpg"
      }
    },
    {
      "gender": "male",
      "name": {
        "title": "mr",
        "first": "antonelo",
        "last": "da conceição"
      },
      "location": {
        "street": "8986 rua rui barbosa ",
        "city": "santo andré",
        "state": "santa catarina",
        "postcode": 40751,
        "coordinates": {
          "latitude": "-69.8704",
          "longitude": "-165.9545"
        },
        "timezone": {
          "offset": "+1:00",
          "description": "Brussels, Copenhagen, Madrid, Paris"
        }
      },
      "email": "antonelo.daconceição@example.com",
      "dob": {
        "date": "1956-02-12T10:38:37Z",
        "age": 62
      },
      "registered": {
        "date": "2005-12-05T15:22:53Z",
        "age": 13
      },
      "phone": "(85) 8747-8125",
      "cell": "(87) 2414-0993",
      "picture": {
        "large": "https://randomuser.me/api/portraits/men/8.jpg",
        "medium": "https://randomuser.me/api/portraits/med/men/8.jpg",
        "thumbnail": "https://randomuser.me/api/portraits/thumb/men/8.jpg"
      }
    },
  ]