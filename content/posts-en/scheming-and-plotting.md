Title: Scheming and plotting
Summary: First encounters
Date: 2011-03-22 01:04
Author: manufactura
Category: Post
Tags: hacks, plotter
Slug: scheming-and-plotting
Lang: en

![Desktop pen plotter](http://www.plotter-printers.com/wp-content/uploads/2011/03/pen-plotter-pictures.jpg "Desktop pen plotter")

For a long while, we were pretty curious about the workings of plotters.  Like
regular inkjet printers, they work by mechanically moving a printer head over a
sheet of paper. Unlike inkjets, plotters use pens to draw, instead of spraying
little drops of ink over the paper. This came in useful for specific uses such
as architecture plans, which featured mostly linework and few textures or
fillings, which made the pen approach desirable. Finally, while inkjet printers
work with bitmap images, pen plotters draw from vector files.

Sadly, plotters are really hard to find. In most print shops, old-school
plotters have been replaced by large-format inkjet printers which,
thanks to modern bitmap rasterising technology, can take care of
linework decently. Here in Portugal, those are still referred to as
'plotters' (even though they don't 'plot'), probably with the purpose of
making them familiar and avoiding boring technical explanations about
how inkjets have good enough resolution for printing fine lines.

Nevertheless, a secret desire of ours was to be able to fiddle with a
real pen plotter. So we were rather excited when [**Diogo
Tudela**](http://vimeo.com/user6357835) came up with a challenge: he had
bought an old Roland DPX-2200 plotter on Ebay, but there were no drivers
available for any modern operating system, and it was now sitting at the
Digital Arts department of
[UCP](http://www.artes.ucp.pt/ "Escola das Artes - Universidade Católica")
hoping to find use in his MA project. So he had this wonderful machine
but no way to operate it.

Working with Diogo, we looked into
[Chiplotle](http://music.columbia.edu/cmc/chiplotle/ "Chiplotle"), a
Python library which takes care of the communication between computer
and plotter. All one needs is a way to generate HPGL files — HPGL is a
specific graphics description language for plotting, a kind of
mini-Postscript. And once more, free software shines:
[Inkscape](http://inkscape.org) is able to save in HPGL format! So we
had the software to interface with the plotter and a way to send our
files into it. We'd just need to solve how to connect the computer to
the plotter.

The Roland DPX-2200 was manufactured between 1987 and 1990, so it's
no![Image](http://computerpartsdirect.us/images/products/800A-RS232-unit.jpg "Serial cable and adapter")
wonder to find an ancient 25-pin serial plug as the sole means of
connecting to anything else. This meant two parts are needed:

-   a USB to serial cable, which accepts 9-pin serial connections
-   and a 25 to 9-pin serial adapter

Diogo had already taken care of both, but when the time came to connect
everything, the plotter remained silent. After some fiddling with the
switches to no avail, and after some googling and headscratching, we
gambled on the possibility that the 25 to 9-pin serial adapter had to be
rewired. So we broke it open and, armed with the
[schematics](http://music.columbia.edu/cmc/chiplotle/manual/chapters/hardware/index.html)
provided in the wonderful Chiplotle web site, we all got out the
soldering iron and breadboard, hoping that the rewiring would work.

[![Breadboard with serial adapter]({static}/media/DSC02151-1024x768.jpg "Breadboard with serial adapter terminals")]({static}/media/DSC02151.jpg)

By the end of the day, once we tried our new serial adapter, still no
practical results. However, whenever we tried to send instructions to
the plotter, its error light would blink up, which was already
something. We decided to stop there for the day, hoping that we had
somehow made a mistake while making the connections in the breadboard.

The next day, we got up early and ran to the UCP in order to review what
we had done with the serial adapter. And indeed, we had made a couple of
goof-ups with the wire connections. After fixing those and getting
Chiplotle up to speed, it finally woke up! You can hear our enthusiasm
on the background:

<iframe src="http://player.vimeo.com/video/21323028?color=88aa00" width="640" height="480" frameborder="0"></iframe>

[Roland DPX-2200 drawing](http://vimeo.com/21323028) from [Manufactura
Independente](http://vimeo.com/user6367848) on
[Vimeo](http://vimeo.com). Video by Diogo Tudela.

Diogo had the brilliant idea to hook an LED on the print head...

[![LED plotter]({static}/media/DSC02165-1024x768.jpg "DSC02165")]({static}/media/DSC02165.jpg)

...and try some long exposure photography:

[![LED long exposure]({static}/media/DSC02171-1024x768.jpg "DSC02171")]({static}/media/DSC02171.jpg)

Exciting times ahead with this new toy!

