Title: Foundry-in-a-box proposal for Servus.at Virtual Residency
Date: 2015-07-05 15:14
Author: manufactura
Status: draft
Category: Post
Slug: servus-residency-proposal
Lang: en

Our proposal in one sentence
------------------------

"Foundry-in-a-box" is the working name for our ongoing project to propose a
workflow to facilitate the publishing of libre fonts.


Main points
-----------

We love fonts, but found a lot of friction in publishing them. For several
months now, we've been developing a set of freely licensed tools to facilitate
the process, using our libre type workshops and fonts we created as the base
for their development. We know for a fact that other free-culture-aware
designers face the same issues when making their foundry sites, and are led to
develop custom frameworks that end up as a wasteful duplication of efforts (we
participated on a [birds-of-a-feather meeting about
this](http://titanpad.com/lgm13-typography) at [Libre Graphics Meeting
2013](http://libregraphicsmeeting.org/2013/)).  Additionally, we see a need to
decentralize open font distribution, currently based on very few nodes (mostly
Google Web Fonts and other non-free portals like Font Squirrel), which can only
be possible if there are tools that enable people to create their own type
foundries and collections.  As for current progress, we still have a way to go.
The architecture for our ideal font publishing system was initially described
in a published paper; however, the project's focus on open fonts and libre type
design makes its development dependent on outside funding, which is why we
believe this virtual residency program is a precious opportunity to support its
development and release of a first working version of our vision.


Project goals
-------------

* Provide a way to publish font collections with a focus on free culture and
  libre type design
* Reduce friction in the font publishing process
* Facilitate a network effect by proposing a "standard" to publish fonts and a
  set of best practices for modification and redistribution
* Give libre typographers all the tools for self-publishing, cutting out
  middlemen and reducing the overhead of maintaining a foundry site
* Allow for the easy creation of curated font collections
* Create a free software toolchain based on Fontforge, Git, Python and
  other libre tools


Use cases
---------

* Take some of the the pain out of cataloguing and indexing open fonts
* Straightforwardly create type foundry sites
* Quickly publish the outcomes of libre type design workshops
* Facilitate the publishing of curated font selections
* Serve as the backend for projects like the Open Font Library
* With further development of the Font Package Format, facilitate font
  distribution in F/LOSS operating systems


Current state
-------------

We've already [presented](http://web.ipca.pt/5et/painel4_pt.html#p4_ana) and
published a paper detailing the architecture of this project
(<small>[ODT](http://media.manufacturaindependente.org/files/foundry-in-a-box_5et.odt
"Foundry-in-a-box paper, 192Kb") or
[PDF](http://media.manufacturaindependente.org/files/foundry-in-a-box_5et.pdf
"Foundry-in-a-box paper, 585Kb")</small>).  We have also
developed a minimal version of the command-line tool
([repository](https://gitlab.com/manufacturaind/fib)), as well as a tentative
first version of the Font Package format, which we need to invest
further time to develop into a full specification.

If this project is accepted, the residency would enable us to finish the
development and documentation of the spec and scripts, as well as a first
working version of a foundry-hosting service which takes advantage from the
Font Package format.


Deliverables
------------

### Specification for the Font Package Format

The Font Package format is a container format we have been developing that provides:

* the working font files
* extended metadata to comprehensively document the font's information,
  authorship, history and other relevant data

The rationale for such a format is to have a "source" format from which it
would be straightforward to generate versions in the most common font formats
(TrueType, OpenType, etc), as well as containing enough information to
facilitate the automatic generation and management of a type foundry site.
Another concern in its design is that it's easy to store as a Git repository,
making these packages easily redistributable.

We have already fleshed out parts of the spec in our paper, but want to develop
these into a full specification document, using the [Data Package format
spec](http://data.okfn.org/doc/data-package) as reference (this format was the
direct inspiration for the Font Package format).

### Command line tool for working with font packages

We've already started development of fib, a command-line based tool to work
with font packages. The main features are:

* create new fontpkgs
* validate fontpkgs and point out any errors
* publish fontpkgs
* convert font packages to all common font formats, and vice-versa
* generate foundry sites
* install fonts by fontpkg name (GNU/Linux only)

The plan is to also take time to publish and fully document the design and
usage of this tool.

### Live hosted web service for font distribution and foundry hosting

The final piece is a simple web service that can:

* host Git repositories for font package publishing
* provide a searchable index for hosted fonts
* deliver web fonts for usage in any website
* freely host foundry websites and curated font collections
* allow for the upload and generation of font packages from existing font files

Our plan is to populate this index with existing open fonts, and approach
designers to publish their fonts there. We also have a plan for the service's
architecture that makes it feasible to use a simple low-spec GNU/Linux web
server.


Other details
-----------

There are many technical and not-so-technical details that can't be described
while respecting the length of this proposal, so we're happy to clear up any
questions that remain regarding the project's feasibility.

