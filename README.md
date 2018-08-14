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

## V.1.0 Roadmap

### Planned Features:

### Stretch goals:

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


