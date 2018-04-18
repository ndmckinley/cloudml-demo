# imagenet runner

This is just a convenient way to run some google tensorflow code.  Nothing to it.  :)  It's on DockerHub as nmckinley/tensorflow-categorizer.

You just run `docker run -v /some/directory/:/data nmckinley/tensorflow-categorizer`, making sure that `/some/directory` contains only .jpgs, .gifs, and .pngs.  It'll fill up with .txt files describing the images.
