# Nagios Plugin Tool

Library to facilitate implementing the Nagios Core Plugin API with custom Nagios plugins

## Installation

```
pip install sld.nagios_plugin
```

## Usage 

```python 
from nagios_plugin import Plugin

plugin = Plugin()
# Do stuff and determine result
plugin.return_ok(message="OK", perf_data="/=123;0;")
```

## Credits



---
Version: 0.0.5