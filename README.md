
## Listenlocal.ly

This (defunct) project was a local music events scraper with minimal (basic
text) UI.  It was basically a (very default, very unsecured) Django app running
on Heroku using default configuration settings.

It existed to scrape local concerts (using a service that no longer exists,
"Kimono", from "Kimono Labs") from the listings available on the "Songkick"
website, and then use that data to pull the most 'popular' track for each
local artist playing locally over the next few days (via Spotify).

When the Kimono service was still alive, this app would get a list of artists
playing nearby in the next few days (from Songkick), then get their top track
(from Spotify).  The list of artist names and the name of their top track
would be displayed, and one could listen to a 30-second sample of the top track
(via an embedded 30 second sample from Spotify).  So, one could easily hear
what sort of sound you might expect at an upcoming concert, straightforward and
without any extra advertising or self-aggrandizing notes about how the artist
or band views themselves, why they are cooler than your neighbor's Trentemøller
tribute group, or other non-actionable, not super valuable information.

The unmodified code still attempts to run at http://listenlocally.herokuapp.com, where it will gladly spew forth errors due to the failure to connect to the
Kimono Labs servers any longer.

There may be reference to defunct "SECRET_KEY" values/etc in this repository.
Good luck :).

### Licensing

Really, this code is probably not very useful to you.  But to appease those
who consider such things of extreme value or philosophical worth, consider
this MIT licensed.  Do whatever you'd like with it.

Text below:

MIT License

Copyright (c) [2016] [Pikk A. Chew]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

### Various Reference Notes Used during this Project

### From docs.djangoproject.com tutorial
listenlocally/ = the root container/folder for the project
listenlocally/config = the Django site / python package for this project
listenlocally/main = the app

#redone
listenlocally/config - config directory
listenlocally/musicinfo - app for getting info from spotify
listenlocally/concertinfo - app for getting local concert info (based on city)
listenlocally/settings/ - contains two separate 'settings.py' files, one for 
local deployment, one for production
