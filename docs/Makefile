# Makefile for DocBook XML directories
#	$Revision: 1.1 $  $Date: 2004/04/03 23:11:02 $
#================================================================
# Definitions:
#	TCC_XSL:  Where our customization layer lives
#	TARGET:  The base file name of the input & output document
#----------------------------------------------------------------
 
TCC_XSL  =  /u/khan/work/doc/docbook
TARGET   =  requirements

#--
# Add the suffixes that we are interested in
#--
# .xml      Input files in DocBook XML format
# .fo       XSL-FO output
# .html     HTML web pages                 
# .ps       PostScript files               
# .pdf      Page Description Format (Abode)
#--

.SUFFIXES: .xml .html .fo .ps .pdf

#================================================================
# Default suffix rules
#----------------------------------------------------------------

.xml.html:
	xsltproc -o $@ $(TCC_XSL)/tcc_html.xsl $<

.xml.fo:
	xsltproc -o $@ $(TCC_XSL)/tcc_fo.xsl $<

.fo.pdf:
	xep $< $@ 

#--
# Two other ways to make the PostScript, and why we don't use them:
#   (1) Make the PostScript directly from the FOP using a rule:
#          .fo.ps:
#              fop $< $@           # Takes forever.
#   (2) Make the PostScript from the PDF using:
#          .pdf.ps:
#              pdf2ps $< $@        # Slow and sometimes doesn't work.
#--

.pdf.ps:
	acroread -toPostScript $<

#================================================================
# Targets
#----------------------------------------------------------------

####all: $(TARGET).html $(TARGET).pdf
all: $(TARGET).pdf

clean:
	rm -f $(TARGET).fo $(TARGET).ps $(TARGET).pdf *.html
