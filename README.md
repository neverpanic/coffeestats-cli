<!--- vim:tw=120
--->
coffeestats-cli
===============

`coffeestats-cli` is a command-line client for [coffeestats.org](https://coffeestats.org). It is written in bash and
uses [cURL](http://curl.haxx.se/) to submit the data to coffestats.org. It should run on Unix every system that has the
`grep`, `curl` and `bash` binaries.

To use this client, install the `coffeestats-cli` script somewhere in your `$PATH` and run it. The script will detect
whether it is being run for the first time and automatically guide you through the necessary setup scripts.

Usage
-----
To use `coffeestats-cli`, call it with a single argument that specifies the type of drink you're having.

 - `coffee` will cause the submission of a coffee to coffeestats.org,
 - `mate` will tell coffeestats.org you're having a bottle of mate.

License
-------
`coffeestats-cli` is licensed under the 3-clause BSD license.
