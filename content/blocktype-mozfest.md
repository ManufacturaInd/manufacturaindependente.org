Title: Blocktype
Summary: Open web fonts in Minecraft
Date: 2014-10-26 16:44
Author: manufactura
Category: Workshops
Tags: type
Slug: blocktype-mozfest
Lang: en

![Workshop poster](http://media.manufacturaindependente.org/blocktype-poster.jpg "Workshop poster")

We love scripting and hacking the font creation process. Some of our
experiments led us to Lasse Fister's wonderful [Graphicore
Bitmap](https://github.com/graphicore/graphicoreBMFB) library, which we've
tweaked to be able to generate simple vector fonts from bitmap data.  This took
us back to the olden days of screen pixel fonts, looking through the early
designs by Susan Kare to the Amiga demo scene. It wasn't long before we came up
with the odd question: how hard would it be to hack Minecraft as a font editor?

After some productive late evenings, we whipped up a working script that could
read a specifically crafted Minecraft world and convert it to a bitmap image,
and from there generate a typeface using the exported bitmaps.

We were really eager to try this idea out. It isn't just a weird connection
between a game and a type tool; it was an experiment to see how a change in
interface (switching font editors for games) could alter and eventually
complement  the design process. We were delighted to hear that [Mozilla
Festival](http://2014.mozillafestival.org/) was up for hosting our weird
interface experiment -- and off to London we went.

We were honoured to participate in the vibrant Art of the Web track alongside
selfie taxonomies, alt-reality scavenger hunts], [video remixes] and
smartphone gallery archaeologies.


The workshop
------------

![Sketching](http://media.manufacturaindependente.org/blocktype-sketching.jpg "Sketches")
![Sketching 2](http://media.manufacturaindependente.org/blocktype-sketching2.jpg "More Sketches")

We started our workshop by sketching the first two characters of our collective
typeface. After looking at each contribution, we made a joint decision as to
what design direction we'd follow.

![Progress board](http://media.manufacturaindependente.org/blocktype-board.jpg "The progress board")
![Decisions](http://media.manufacturaindependente.org/blocktype-board2.jpg "Making decisions")

From there, the group was divided into a builder team and a designer team. The
"designers" would go on sketching and defining the remaining characters,
whereas the "builders" would begin work on building those characters in a
Minecraft world.

![Minecraft screen](http://media.manufacturaindependente.org/blocktype-screen.jpg "Minecraft font design")

<video src="http://media.manufacturaindependente.org/blocktype-minecraft.mp4" controls>
  Your browser does not support embedded HTML5 video.
</video>

The builders were quick in constructing the uppercase version, while the
designers went full-speed ahead to tackle not only the uppercase, but numbers
and lowercase as well! After that, the designers lent a hand in making the
digital versions of the lowercase and numbers using another font making tactic
with text files and ASCII art (we'll detail this approach in a later post.)


The result
----------

After much work and refinement, our script did its magic and the Mozblock
typeface was born!

![Mozblock specimen](http://media.manufacturaindependente.org/blocktype-specimen.png "Mozblock type specimen")

You can download the font package containing all necessary formats for
inclusion in HTML pages.


Our last Minecraft workshop
---------------------------

If you've been following your work, you'll know that one of the main directions
in our practice is the integral use of free software and free culture licenses
in our work. That said, it will sound strange that we'd use Minecraft, a
proprietary game, as part of our practice. In short: we tried, and now we
realise it was a mistake.

We have been big fans of Minecraft since ginger showed us why it was a
fantastic game, a couple of years ago. And while our values have always put us
on the side of free software, Minecraft was the one exception we were willing
to make: even though it's proprietary, their friendly product policy (pay 20€
for the license, never pay again for upgrades or other add-ons) made us and
other free software activists give it a pass and embrace it.

However, the recent acquisition of Mojang by Microsoft, an entity which has a
terrible track record of preserving openness and privacy, made it clear to us
that we had to reconsider our stance towards Minecraft and its role in our
work. While it is a brilliant framework to cook up design experiments (as our
workshop showed,) the Microsoft connection makes its proprietary nature stand
out clearly. Since we had already committed to teaching this workshop by the
time the acquisition was announced, we decided to go through with it and make a
statement afterwards about what these new developments mean to people
interested in Minecraft as a game or a tool.

For this workshop, we developed an extensive set of tools to work with
Minecraft worlds and translate them into bitmaps and fonts; we gave the name
"Blocktype" to the set of scripts and gizmos that makes this happen. Our
original plan was to release all the code under the GPL so that more people
could try and improve it. However, the new state of affairs means that we'd be
actively promoting a Microsoft product, and indirectly its values, by releasing
code that works with it and enables it to do more cool stuff. 

So Blocktype will probably be the one software library that we made which we
will not release.

While we feel burned, we have to admit that our judgment in adopting a
proprietary product was wrong, and it's yet another episode where Richard
Stallman is proven right: respect for users' freedom can only be assured by the
use of free software. In hindsight, it feels very naive to have believed that
Minecraft and Mojang could be "different", but the outcome is again the same as
previous cases: proprietary software is inevitably led towards goals that
undermine users' agency, privacy and control. Microsoft has made its business
practice clear by siding with surveillance, mining users' data and adopting
extorsion tactics in markets where it has power. We will not support the
products of such an entity.

We are now about to consider our options. We certainly don't mean to throw all
the work behind Blocktype away, and plan to look at possible alternatives. The
two most interesting ones are Minetest and Voxel.js. If you can help us adapt
our Python scripts to these frameworks, we'd be more than happy to work
together in order to release what we think is a really useful tool: a library
that allows you to draw pixel fonts in a 3D world, something that we've just
found is incredibly fun, productive and encouraging.


Credits
-------

*Image credits*

  * Photos by [Metod Blejec](http://twitter.com/metodb). Personal use is allowed, please get in touch for commercial use.
  * Screencast by [Louis Reed](http://twitter.com/_louisreed).

*Acknowledgments*

  * Mozilla Festival and the Art of the Web track organisers:
    * [Kat Braybrooke](https://twitter.com/codekat)
    * [Paula le Dieu](https://twitter.com/archiville)
    * [Erik Nelson](http://wreckandsalvage.com)

  * Workshop participants:
    * [Jens Aronsson](https://twitter.com/jensaronsson)
    * [Metod Blejec](https://twitter.com/metodb)
    * [Johan Hermansson](https://twitter.com/oans)
    * [David Moulton](https://twitter.com/davidcmoulton)
    * [Louis Reed](https://twitter.com/_louisreed)
    * [Oliver Roick](https://twitter.com/oliverroick)
    * [Adam Sofokleous](https://twitter.com/adam_cy)
    * [Jennifer Steele](https://twitter.com/jenieloulou)
    * [Camellia Xueyi](https://twitter.com/11thme)
    
