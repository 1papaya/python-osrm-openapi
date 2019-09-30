# python-osrm-openapi
Python API for OSRM (Open Source Routing Machine) based upon an OpenAPI Spec

## Installation

### Package Installation

   ```shell
     git clone https://github.com/1papaya/python-osrm-openapi.git
     cd python-osrm-openapi && python3 setup.py install
   ```
   
### API Generation from .yaml

   ```shell
     git clone https://github.com/1papaya/python-osrm-openapi.git
     cd python-osrm-openapi/src && ./generate_api.sh
   ```
   
## Details

python-osrm-openapi is a Python API for OSRM automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project, according to the spec in src/osrm-openapi.yaml

Things to note:
* Currently the OpenAPI spec [doesn't support semicolon-delimited serialization](https://swagger.io/docs/specification/serialization/) of path and query parameter arrays. So, many of the parameters (bearings, radiuses, ...) are accepted instead as strings and must be serialized before being passed along.
* The .yaml was derived from descriptions over at the [OSRM API docs](http://project-osrm.org/docs/v5.22.0/api/)
* Path & query defaults are repeated in the .yaml because multiple parameter definition groupings [aren't yet supported by OpenAPI spec](https://github.com/OAI/OpenAPI-Specification/issues/445). Maybe soon! :)
* Feel free to use src/osrm-openapi.yaml to generate APIs in other languages, and to contribute any changes!

Endpoints currently supported:

* nearest
* route
