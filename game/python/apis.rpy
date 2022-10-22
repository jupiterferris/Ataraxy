init python:
    # API functions
    def getLocation():
        try:
            ipRequest = requests.get('https://ipwho.is')
            if ipRequest.status_code != 200:
                print("Error making request!")
                return
            json = ipRequest.json()
            return (json["latitude"], json["longitude"])
        except:
            print("IP could not be retrieved! Are you using a VPN?")
            return (53.3676, 3.1626)
    def getTimeBounds():
        lat, lon = getLocation()
        queryParameters = {
            "lat": lat,
            "lon": lon
        }
        try:
            boundsRequest = requests.get("https://api.sunrise-sunset.org/json", params=queryParameters)
            json = boundsRequest.json()
            results = json["results"]
            sunrise = results["sunrise"]
            sunset = results["sunset"]
            noon = results["solar_noon"]
        except:
            print("Local day cycle unavailable! Using default values.")
            sunrise = "06:00:00 AM"
            sunset = "06:00:00 PM"
            noon = "12:00:00 PM"

        return (sunrise, sunset, noon)
    def getTimeOfDay():
        global timeOfDay
        currentTime = datetime.now().strftime("%H:%M:%S")
        midnightTime = datetime.now().replace(hour=0, minute=0, second=0).strftime("%H:%M:%S")
        sunrise, sunset, noon = getTimeBounds()
        sunriseTime = datetime.strptime(sunrise, "%I:%M:%S %p").strftime("%H:%M:%S")
        sunsetTime = datetime.strptime(sunset, "%I:%M:%S %p").strftime("%H:%M:%S")
        noonTime = datetime.strptime(noon, "%I:%M:%S %p").strftime("%H:%M:%S")
        print(f"Current time: {currentTime}")
        print(f"Sunrise today: {sunriseTime}")
        print(f"Sunset today: {sunsetTime}")
        print(f"Noon today: {noonTime}")
        # [midnight] | morning | [sunrise] | day | [noon] | afternoon | [sunset] | night | [midnight]
        if currentTime > midnightTime and currentTime < sunriseTime:
            timeOfDay = "morning"
        elif currentTime > sunriseTime and currentTime < noonTime:
            timeOfDay = "day"
        elif currentTime > noonTime and currentTime < sunsetTime:
            timeOfDay = "afternoon"
        else:
            timeOfDay = "night"
    