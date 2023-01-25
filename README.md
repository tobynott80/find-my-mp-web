# Find My Mp
## Website to gather information on a local MP

[Find My MP](https://fmmp.toby.uk.eu.org)

> Work In Progress

A simple flask app to wrap the [parliament.uk](parliament.uk) API to show an MP's details based off a postcode. Also finds related Guardian articles (work in progress)

### Running with Docker

1. Build the app from Dockerfile

    `docker build app/ -t fmmp:latest`

2. Run the app, supplying with [The Guardian API key](https://open-platform.theguardian.com/), exposing port 80

    `docker run -p 80:80 -e GUARDIAN_KEY={key} -d fmmp:latest`

    > Note: Guardian API key not necessary for full functionality
3. Go to [localhost](localhost)

### Running manually

1. Set Guardian API key as environment variable (Optional)

    Linux: `$Export GUARDIAN_KEY="{key}"`
    
    Powershell: `$Env:GUARDIAN_KEY = "{key}"`

    > Note: Guardian API key not necessary for full functionality

2. Install PIP requirements

    `pip install -r app/requirements.txt`

3. Run app.py

    `python3 app/app.py`

### Known Issues
- Guardian API returns unrelated articles for some MPs.
- Search Page can be slow to load - API limiting