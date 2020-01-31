# A Performance Analysis Framework for Local Python Programs

For Python 3.6.

Requires the Python 3 version of VyPR Server (http://github.com/pyvypr/VyPRServer-py3/).  That has its own setup instructions.

## Setup (for Flask)

*Not needed if VyPR is being cloned for VyPR server.*

Once you've cloned the depository (into the root of the project for which you want to do monitoring):

* Write your queries in the file `VyPR_queries.py` in the root of your project.  See the examples in `sample_input/queries/` for ideas.
* Write your configuration in the file `vypr.config`.  See the examples in `sample_input/vypr_config/` for ideas.

To attach VyPR monitoring to your project, use

``
from VyPR import Monitor
vypr = Monitor()
``

and then, wherever you initialise your Flask application object, add

``
vypr.initialise(flask_app)
``

To instrument and monitor:

* Run `python VyPR/instrument.py` from your project's root directory.  This will process `VyPR_queries.py` and generate some new files.
* Run your Flask application, assuming VyPR is attached.

## Licence

(C) Copyright 2018 CERN and University of Manchester.
This software is distributed under the terms of the GNU General Public Licence version 3 (GPL Version 3), copied verbatim in the file "COPYING".
In applying this licence, CERN does not waive the privileges and immunities granted to it by virtue of its status as an Intergovernmental Organization or submit itself to any jurisdiction.

Author: Joshua Dawes - CERN, University of Manchester
