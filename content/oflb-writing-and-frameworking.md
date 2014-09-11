Title: OFLB: Writing and frameworking
Date: 2011-08-31 17:39
Author: manufactura
Category: Hidden
Tags: oflb
Slug: oflb-writing-and-frameworking

<!--:en-->  

Documenting open fonts
----------------------

Writing extensive documentation is something that we're not used to --
and it's never too late to get started! As a reference, we based our
structure on the wonderful and highly regarded Django documentation, as
well as the Django book. We posted before on our approach of following a
book structure, along with a set of reference lists (appendices).

As we revise and edit the existing Guidebook, we came up with a more
sensible structure, divided in 3 main sections about creating, sharing
and using open fonts. Here's our table of contents so far:

> **Introduction**  
>  What is the Open Font Guidebook?  
>  Use cases and where you should start reading
>
> **Creating fonts**  
>  Get started designing fonts  
>  How to design a font  
>  Design a new typeface from scratch  
>  Revive a historic design  
>  Remix a font  
>  Fonts needed for OFLB
>
> **FontForge**  
>  Installing  
>  Setting up  
>  Using  
>  Scripting with Python
>
> **Sharing fonts**  
>  Uploading your fonts to the Open Font Library  
>  Using FontForge to work with Open Font Library
>
> **Using fonts**  
>  Using open fonts in your web site  
>  Using open fonts in your graphic design programs  
>  Managing fonts in your system  
>  Fontmatrix (OSX, Windows)  
>  Fontbook
>
> **Legal issues**  
>  Fonts and the law  
>  About licensing  
>  How font licensing works  
>  The Open Font License  
>  The GNU General Public License  
>  Proprietary licensing  
>  Other licenses
>
> **Reference lists**  
>  Glossary  
>  Font formats  
>  Licenses  
>  Web typography toolkits  
>  Existing libre fonts  
>  Specimens and scans  
>  Open fonts People  
>  External Resources  
>  Software  
>  Knowledge  
>  Education

We've completed some of the reference lists, and just finished a
step-by-step tutorial around scripting FontForge, using as a practical
example our script for generating outline fonts. There's still a lot of
writing and editing before we hit version 1.0 of the Guidebook, and we
believe it will become a priority read for anyone who wants to know more
about fonts.

Getting to grips with the Aiki Framework
----------------------------------------

Now that the core mockups have been finished, it's time to port them
over to Aiki, the framework that takes care of all the work inside the
Open Font Library. The way it works is new to us -- we normally use
Django -- and there's some very interesting concepts in Aiki. One good
example is Aiki widgets, which in our opinion can be best described as
blocks: a page is made of several widgets, which consist of HTML code,
CSS additions, SQL calls and other options. By joining all these blocks
together in order, you have a dynamic page.

So our work now has been to get the HTML from our mockups and placing it
inside the relevant widgets, doing the necessary tweaks and adjustments
in order to fit inside Aiki. We've been rather busy refreshing our
limited knowledge of SQL in order to be able to pull this through. So
far we've nailed down the header and footer, and are now busy
implementing the Catalogue and Font Family pages, which require finer
adjustments to the queries and templates. All this work is going on in a
private server, which will be then merged with the main site as soon as
the new design is fully implemented (soon!)

Translation!
------------

We've also started work on translating OFLB. Fabricatorz are hard at
work setting up a translation infrastructure for Aiki, and we've done
the first steps of a total Portuguese translation -- starting with
translating Aiki itself, and moving to OFLB-specific content. We'll also
be working to translate the Guidebook, and then hope that other
languages might be included by other contributors.  
<!--:-->

