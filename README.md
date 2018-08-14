<h1 align="center">
 :evergreen_tree: :evergreen_tree: CampSights :tent: :evergreen_tree:<br /> <br />
    <h3 align="center">
      Seek out new adventures and keep track of those you've had.
    </h3>
   <p align="center">
    Copyright &copy; 2018 Matt Carnovale
  </p>
  <p align="center">
    <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/github/license/mashape/apistatus.svg"></a>
  </p>
</h1>



## About

CampSights is a Backend Service application built with <a href="http://flask.pocoo.org/">Flask</a>, a microframework for Python. <br />To find new places to camp and hike, it utilizes a combination of the following APIs:<br />
* <a href="https://developers.google.com/maps/documentation/geocoding/start"> Google Geocoding</a> <br />
* <a href="https://ridb.recreation.gov/">Recreation Information Database</a> <br />
* <a href="https://www.hikingproject.com/data">REI Hiking Project API</a> <br />


### Vision Moving Forward
If a suggestion seems appealing to a user, it can be saved to create an adventure 'to-do' list. Users can also use CampSights to log the sites they've visited to help keep track of the campgrounds they've already been to and would like to visit again. Other planned features include the ability to add a hiking or camping goal of the month/season, add personal photos or notes associated with completed adventures, and the ability to connect with close friends to get advice or opinions you can trust.

## Getting Started

### Prerequisites
* Install Python 3.6 or higher. If you're using Linux or OSX, I highly recommend checking out <a href="https://medium.com/@henriquebastos/the-definitive-guide-to-setup-my-python-workspace-628d68552e14">these instructions</a>, by Henrique Bastos, on how to setup a Python workspace.

* Register for API Keys for the three services:
  * <a href="https://developers.google.com/maps/documentation/geocoding/get-api-key">Google Geocoding</a>
  * <a href="https://ridb.recreation.gov/?action=register">RIDB.Recreation.gov</a>
  * <a href="https://www.hikingproject.com/data">REI Hiking Project</a> <br />
  :bowtie: _Sorry folks, I'll be working on a better way to get around all of these keys moving forward._ :bowtie:

* Create a secret key for you Flask instance. See <a href="http://flask.pocoo.org/docs/1.0/config/#SECRET_KEY">Flask docs</a>.  
  
* __Optional__
  * Install <a href="https://docs.pipenv.org/install/#installing-pipenv">Pipenv</a>. This is an awesome tool for Python that provides package management similar to what one would expect from node, yarn, or cargo and handles creating a virtualenv for your projects! 

### Installation
1. Clone the repository to your local machine with: <br />
`git clone https://github.com/mattCarnovale/CampSights.git`
2. Using a command line tool, navigate to the directory used to clone the project.
3. Install package depencencies:
   * If using `Pipenv` _(recommended by yours, truly)_, use the command:<br /> 
     `pipenv install`
   * If sticking with `Pip`, use the command: <br />
     ` pip install -r requirements.txt`
4. Create and setup `config.py` _(this is where you'll hide your keys, etc)_ :
   1. In the main directory of the project, create a new directory called `Instances`. <br />
      `mkdir Instances`
   2. Move to the `Instances` directory and create a Python file called `config.py`
   3. This is where you will store the API keys you registered. <br />
   ```
   SECRET_KEY = <Your key for flask>
   GEO_KEY = <YOUR GOOGLE GEOCODE KEY HERE>
   RIDB_KEY = <YOUR RIDB KEY HERE>
   HIKING_PROJECT_KEY = <YOUR REI HIKING PROJECT KEY HERE>
   ```
   _Notice the `Instances` directory is in the `.gitignore`._ <br />
   __Do not share or commit your keys__

* __Optional__
   * If using the temporary cli-client:
      * Execute the command `pipenv install -e .` or `pip install -e .`
   
### Usage
#### Start Flask Server
Working inside the project directory, execute the following: <br />
```
export FLASK_APP=campsights
export FLASK_ENV=development
flask run
```
_For Windows cmd use `set` instead of `export`_ <br />
_For Windows Powershell use `$env:` instead of `export`_ <br />

If the Flask server starts successfully, the output that contains something similar to:<br />
`* Running on http://127.0.0.1:5000/`

__Keep the Flask Server Running and work in another terminal window during use__<br />
__To shutdown the Flask Server, use Ctrl + C__

#### Command Line Interface
General format:<br />
`campsights <command> <option> <request_criteria>`

__Note: if using `pipenv`, don't forget to use `pipenv shell` to work in your virtualenv__

##### Commands
* `camp_list`  -- request list of campgrounds <br />
   The following options are available: <br />
   * `--zipcode` or `-z` -- request using zipcode (5 digit or 9 digit dash separated #####-####)
   * `--address` or `-a` -- request using city & state, comma separated (city, state) <br /> 
Example usage: <br />
   ```
   campgrounds camp_list -z 97201
   campgrounds camp_list --zipcode 97201-0751
   campgrounds camp_list -a Portland, Or
   campgrounds camp_list --address Portland, Oregon
   ```

#### Endpoints
`<FLASK HOST:PORT>` is the url or IP address and Port your Flask Server is Running on.<br />
It should be defined after you ran the `flask run` command. By default, this will be `http://127.0.0.1:5000`.<br />
You can try out consuming these endpoints with the <a href="https://github.com/curl/curl ">curl</a> command. <br /> 

__Method:__ Get List Of Campgrounds Within Given Radius <br />
__Required_Args:__ <br />
Coordinates - 'coordinates': {'lat': # , 'lng': #} <br />
Radius -  'radius': # <br />
__Accepted HTTP Method:__ GET <br />
__Endpoint:__ `<FLASK HOST: PORT>/destinations/campgrounds`<br />

__Method:__ Get Specified Campground <br />
__Required_Args:__ <br />
Campground Name - 'campground_name': _String_ <br />
Two letter State Code -  'state': _String_ <br />
__Accepted HTTP Method:__ GET <br />
__Endpoint:__ `<FLASK HOST: PORT>/destinations/campground`<br />

__Method:__ Get List Of Trails Within Given Radius <br />
__Required_Args:__ <br />
Coordinates - 'coordinates': {'lat': # , 'lng': #} <br />
Radius -  'radius': # <br />
__Accepted HTTP Method:__ GET <br />
__Endpoint:__ `<FLASK HOST: PORT>/destinations/trails`<br />

__Method:__ Get Specified Trail <br />
__Required_Args:__ <br />
Coordinates - 'coordinates': {'lat': # , 'lng': #} <br />
Trail Name -  'trail_name': _String_ <br />
__Accepted HTTP Method:__ GET <br />
__Endpoint:__ `<FLASK HOST: PORT>/destinations/trail`<br />

__Method:__ Get Coordinates By Zipcode <br />
__Required_Args:__ <br />
Zipcode -  'zipcode': # <br />
__Accepted HTTP Method:__ GET <br />
__Endpoint:__ `<FLASK HOST: PORT>coordinates/zipcode`<br />

__Method:__ Get Coordinates By Partial Address <br />
__Required_Args:__ <br />
City -  'city': _String_ <br />
State -  'state': _String_ <br />
__Accepted HTTP Method:__ GET <br />
__Endpoint:__ `<FLASK HOST: PORT>coordinates/partial_address`<br />

__Method:__ Get Coordinates By Specified Trail <br />
__Required_Args:__ <br />
Trail -  'trail': _String_ <br />
__Accepted HTTP Method:__ GET <br />
__Endpoint:__ `<FLASK HOST: PORT>coordinates/specified_trail`<br />

## Built With
* <a href="http://flask.pocoo.org/">Flask</a> <br />
* <a href="http://docs.python-requests.org/en/master/#">Requests</a> <br />
* <a href="https://github.com/googlemaps/google-maps-services-python">Python Client for Google Maps Services</a> <br />
* <a href="https://github.com/theskumar/python-dotenv">python-dotenv </a> <br />
* <a href="https://www.python.org/dev/peps/pep-0008/">Pep8</a> <br />
* <a href="https://github.com/hhatto/autopep8">autopep8</a> <br />
## Authors
* <a href="https://github.com/mattCarnovale">Matt Carnovale</a>

## License
This work is licensed under the **MIT** license. See
the file `LICENSE` in this distribution for license terms.


